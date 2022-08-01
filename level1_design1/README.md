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
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(a or b) 
  begin
    sum = a - b;             ====> BUG
  end
```
For the adder design, the logic should be ``a + b`` instead of ``a - b`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
