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
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

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
          next_state = IDLE;
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
          next_state = IDLE;
      end
      SEQ_1011:
      begin
        next_state = IDLE;
      end
    endcase
  end
```
The Output for the above buggy code is as follows:
```
```

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

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
