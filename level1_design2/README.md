# Sequence Detector 1011 Design Verification

The Sequence Detector 1011 Design verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/109667378/182130860-8b1095c0-ffae-4e2b-839a-3f354b9f4d8f.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes in clk , reset and inp_bit as inputs. The DUT asserts seq_seen bit when the pattern seen on inp_bit on 4 consecutive clocks is 1011. 

The values are assigned to the input port using 
```
    # Send a random sequence of 0 & 1 for 1000 cycles.
    for i in range(1000) :
        # Driving random value between 0 & 1 to the DUT.
        INPUT = random.randint(0,1)
        dut.inp_bit.value = INPUT
        dut._log.info(f'Input value Driven = {INPUT}')
```

The assert statement is used for comparing the Sequence Detector's outut to the expected value.

The following error is seen:
```
    # Comparing DUT 'seq_seen' with LOCAL_DUT_SEEN variable
    if(dut.seq_seen.value != LOCAL_DUT_SEEN ) :
       dut._log.info(f'ERROR : DUT OUTPUT = {dut.seq_seen.value} , REF MODEL OUTPUT = {LOCAL_DUT_SEEN} , PREVIOUS 4 INPUTS = {bin(INPUT_REGISTER_MOD_16)}')
       ERROR_COUNT = ERROR_COUNT + 1
    
    # In order to make the test run without terminating , incrementing ERROR_COUNT variable 
    # If ERROR_COUNT !=0 , assert Error to make the Test Fail
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message             
```

## Test Scenario **(Important)**
- Test Inputs: 
```
    9895000.00ns INFO     Input value Driven = 1
    9905000.00ns INFO     Input value Driven = 0
    9915000.00ns INFO     Input value Driven = 1
    9925000.00ns INFO     Input value Driven = 0
    9935000.00ns INFO     Input value Driven = 1
    9945000.00ns INFO     Input value Driven = 1
    9955000.00ns INFO     SEQUENE DETECTED BY REF MODEL
    9955000.00ns INFO     ERROR : DUT OUTPUT = 0 , REF MODEL OUTPUT = 1 , PREVIOUS 4 INPUTS = 0b1011
```
- Expected Output: seq_seen should have been 1 at 9955000.00 ns
- Observed Output in the DUT dut.seq_seen = 0

Output mismatches for the above inputs proving that there is a design bug
From the above test input, it is clear that Design has incorrect state transitions mentioned within the code.

## Design Bug
Based on the above test input and analysing the design, we see the following

```
  // state transition based on the input and current state
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;        ===> BUG : Design should have stayed in SEQ_1 state if inp_bit seen was 1{1}.
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;        ===> BUG : Design should move to 10 state when inp_bit seen is 101{0} as last 2 LSB can become the new pattern. 
      end
      SEQ_1011:
      begin
        next_state = IDLE;          ===> BUG : Design should move to SEQ_1 or SEQ_10 state depending upon 1011{1} or 1011{0} received 
      end
    endcase
  end
```
The Output for the above buggy code is as follows:
![image](https://user-images.githubusercontent.com/109667378/182135983-b234ad21-9fb8-4e2d-b524-9cf75ddc1610.png)

From the above test input and code , we see that the Design is not for an overlapping 1011 sequence detector.
For the Sequence Detector design, the correct code is shown below.

```
  always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      SEQ_10:
      begin
        if(inp_bit == 1)
          next_state = SEQ_101;
        else
          next_state = IDLE;
      end
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;
      end
      SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
    endcase
  end
```

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109667378/182136084-4f4e166e-974c-445b-9d27-1fb68cead31c.png)

The updated design is checked in at https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/blob/master/level1_design2_bug_free/seq_detect_1011.v

## Verification Strategy
The verification strategy used for the verification of Sequener Design design is as follows:

```
a) Send a random sequence of 0 & 1 on inp_bit input for 1000 cycles.
b) Save the same inp_bit applied to the DUT onto a 4 bit shift register by shifting left the previous content by 1 bit and adding the inp_bit 
c) If the 4 bit shift register contains value 1011 , assert golden seq_seen bit.
d) Compare DUT seq_seen and golden seq_seen. If mismatch , increase ERROR COUNT
e) Assert ERROR_COUNT == 0 to make the decision about test fail or pass.
```

## Is the verification complete ?
A random sequnce of 0 & 1 was applied to the DUT for 1000 cycles and on the fly checking was done by using a 4 bit shift register.
A mismatch between the DUT's output and shift register's contents was highlighted within the Error.

Providing the above inputs, we can say that the all possible input combinations have been tried , and the complete code has been excercised. This provides us more confidence about the verification strategy used to verify the Sequence Dectector 1011 design.
