# Multiplexer Design Verification

The Multiplexer verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/109667378/182103268-e7b66947-15ca-4646-a9d3-5ff62db7d6e8.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 5 bit select signal and 31 2 bit input signals. Depending upon the value of select signal , the multiplexer selects a particular input as 2 bit output signal.
For ex : If SEL == 10 , then OUT = INP10 and so on.

The values are assigned to the input port using 
```
# Here i ranges from 0 to 31 ( all possible values for 5 bit select line ) and a random value is selected for all inputs between 1 & 3.
SEL = i ;
dut.sel.value = SEL 
VALUE = random.randint(1,3)
dut.inp0.value = VALUE
```

The assert statement is used for comparing the Multiplexer's outut to the expected input value.

The following error is seen:
```
# Comparing Output depending upon the value of SEL applied.
if dut.sel.value == 0 :
   if dut.out.value != dut.inp0.value :
      dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp0.value} , Output value = {dut.out.value}')
      ERROR_COUNT = ERROR_COUNT + 1 

# Final Error Checking to make the test decision
error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
assert ERROR_COUNT == 0 , error_message
```
## Test Scenario **(Important)**
Scenario 1 :
- Test Inputs: SEL = 12 ( 0b01100 ) , INP12 ( 0b11 )
- Expected Output: OUT = 0b11
- Observed Output in the DUT dut.out = 00 

Scenario 2 :
- Test Inputs: SEL = 13 ( 0b01101 ) , INP13 ( 0b10 )
- Expected Output: OUT = 0b10
- Observed Output in the DUT dut.out = 01

Scenario 3 :
- Test Inputs: SEL = 30 ( 0b11110 ) , INP12 ( 0b11 )
- Expected Output: OUT = 0b11
- Observed Output in the DUT dut.out = 00 

Output mismatches for the above inputs proving that there is a design bug.
The seed for the above run is "Seeding Python random module with 1659342367"

## Design Bug
Based on the above test input and analysing the design, we see the following

```
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;   ====> BUG : 01101 is 13 in Decimal. For inp 12 , it should be 01100
      5'b01101: out = inp13;   ====> BUG : Multiple declartion for 5'b01101 , Always above one will be picked.
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      default: out = 0;        ====> BUG : No case statement for sel 5'b11110 , causing it to go to default state.
    endcase
```

The Output for the above buggy code is as follows:
![image](https://user-images.githubusercontent.com/109667378/182108628-eddd14b7-0194-47b5-a630-454426037d71.png)


For the multiplexer design, the correct code is shown below:
```
    case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01100: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
      5'b11110: out = inp30;
      default: out = 0;
    endcase
```

## Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/109667378/182108808-0927502e-9835-4ce2-915b-3bbc99e96017.png)

The updated design is checked in at:
https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/blob/master/level1_design1_bug_free/mux.v

## Verification Strategy
The verification strategy used for the verification of multiplexer design is as follows:
a) Providing all SEL values ( 0 to 31 ) inside a for loop to the DUT.
b) After providing inputs , wait for 2ns for the output to appear.
c) Comparing the output value to the appropriate input depending upon the SEL value applied.
d) If there is any mismatch, increase the ERROR_COUNT
e) Outside the for loop , compare if ERROR_COUNT == 0 , failing which will fire an assertion to make the test fail.

## Is the verification complete ?
All inputs values of sel and inp0....inp30 have been verified.
For sel value = 31 , the default statement is also working.

Providing the above inputs, we can say that the all possible input combinations have been tried , and the complete code has been excercised.
This provides us more confidence about the verification strategy used to verify the mux design.
