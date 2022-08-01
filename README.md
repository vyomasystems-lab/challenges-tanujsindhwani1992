# Capture the Bug - A Design Verification Hackathon

```
To provide a basic hands-on for design verification, which enhances practical verification knowledge. The verification challenge helps to understand the verification intent to detect bugs in designs, understand debugging and fix the buggy designs. It provides a practical exposure to real world design verification activities

The  Hackathon  aims  to generate skilled manpower in the domain of Design Verification, which will strengthen the quality of designs being manufactured.
It reduces chip failure which in turn improves the time to market cycle of Semiconductor products.

The Indian Govt initiative Chips to Startup (C2S) aims to propel innovation, build domestic capacities to ensure hardware sovereignty, and build a Semiconductor Ecosystem that requires 85,000+ highly trained engineers. Working towards this vision statement, we have planned the 3-Week “Capture the Bug” , a Design Verification Challenge.

This Hackathon is organized by NIELIT  Calicut and technically facilitated by  Vyoma Systems , VLSI System Design & Robotics and Automation Society, IEEE Kerala Section.

The program is supported  by the Chips to Startup (C2S) Program of the Govt of India and Mentored by IIT Madras 
```

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
dut.a.value = 7
dut.b.value = 5
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
