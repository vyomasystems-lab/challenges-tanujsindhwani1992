# Capture the Bug - A Design Verification Hackathon

To provide a basic hands-on for design verification, which enhances practical verification knowledge. The verification challenge helps to understand the verification intent to detect bugs in designs, understand debugging and fix the buggy designs. It provides a practical exposure to real world design verification activities

The  Hackathon  aims  to generate skilled manpower in the domain of Design Verification, which will strengthen the quality of designs being manufactured.
It reduces chip failure which in turn improves the time to market cycle of Semiconductor products.

The Indian Govt initiative Chips to Startup (C2S) aims to propel innovation, build domestic capacities to ensure hardware sovereignty, and build a Semiconductor Ecosystem that requires 85,000+ highly trained engineers. Working towards this vision statement, we have planned the 3-Week “Capture the Bug” , a Design Verification Challenge.

This Hackathon is organized by NIELIT  Calicut and technically facilitated by  Vyoma Systems , VLSI System Design & Robotics and Automation Society, IEEE Kerala Section.

The program is supported  by the Chips to Startup (C2S) Program of the Govt of India and Mentored by IIT Madras 


## CTB Challenge Level 1 - Multiplexer 

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 5 bit select signal and 31 2 bit input signals. Depending upon the value of select signal , the multiplexer selects a particular input as 2 bit output signal. For ex : If SEL == 10 , then OUT = INP10 and so on.

For more details refer : https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/tree/master/level1_design1

## CTB Challenge Level 1 - Sequene Detector 1011

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes in clk , reset and inp_bit as inputs. The DUT asserts seq_seen bit when the pattern seen on inp_bit on 4 consecutive clocks is 1011.

For more details refer : https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/tree/master/level1_design2

## CTB Challenge Level 2 - Bit Manipulation Coprocessor

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Bit Manipulation Processor module here) which takes in clk (unused) , reset (unused) , max_putvalue_instr , max_put_value_src1 , max_put_value_src2 , max_put_value_src3 and EN_mav_putvalue as inputs. max_putvalue_instr acts as the opcode and also provides which operands to choose between max_put_value_src1 , max_put_value_src2 & max_put_value_src3. Depending upon the max_putvalue_instr , max_put_value_src1 , max_put_value_src2 , max_put_value_src3 values , the DUT provides mav_putvalue as an output. The LSB bit of mav_putvalue indicates that output is valid and the remaining 32 bits provides the result.

For more details refer : https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/tree/master/level2_design

## CTB Challenge Level 3 - APB3 Slave

The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (APB3 Slave module here) which takes in PCLK , PRESETn , PADDR , PWRITE , PSEL and PWDATA as inputs. The DUT contains a memory reg [DATAWIDTH-1:0] RAM [0:2^ADDRWIDTH -1] which is used for storing the Write Data provied by the Master. Also, the same memory provides the PRDATA as output from the Slave.

For more details refer : https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/tree/master/level3_design

## About Me


