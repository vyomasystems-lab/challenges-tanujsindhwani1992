# Bit Manipulation Processor Design Verification

The Bit Manipulation Processor Design verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/109667378/182141921-6aadf5b3-9b0c-49d6-99e8-7d7b833aa5d0.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Bit Manipulation Processor module here) which takes in clk (unused) , reset (unused) , max_putvalue_instr , max_put_value_src1 ,  max_put_value_src2 ,  max_put_value_src3 and EN_mav_putvalue as inputs. max_putvalue_instr acts as the opcode and also provides which operands to choose between max_put_value_src1 ,  max_put_value_src2 &  max_put_value_src3. Depending upon the max_putvalue_instr , max_put_value_src1 ,  max_put_value_src2 ,  max_put_value_src3 values , the DUT provides mav_putvalue as an output. The LSB bit of mav_putvalue indicates that output is valid and the remaining 32 bits provides the result.

The values are assigned to the input port using :
```
    # Instruction Dictionary
    Instruction_dict = {  'ANDN'        :  [ 0x40007033 , 0x41FFFFB3 ],  #Error Found
                          'ORN'         :  [ 0x40006033 , 0x41FFEFB3 ],
                          'XNOR'        :  [ 0x40004033 , 0x41FFCFB3 ],
                          'SLO'         :  [ 0x20001033 , 0x21FF9FB3 ],
                          'SRO'         :  [ 0x20005033 , 0x21FFDFB3 ],
                          'ROL'         :  [ 0x60001033 , 0x61FF9FB3 ],
                          'ROR'         :  [ 0x60005033 , 0x61FFDFB3 ],
                          'SH1ADD'      :  [ 0x20002033 , 0x21FFAFB3 ],
                          'SH2ADD'      :  [ 0x20004033 , 0x21FFCFB3 ],
                          'SH3ADD'      :  [ 0x20006033 , 0x21FFEFB3 ],
                          'SBCLR'       :  [ 0x48001033 , 0x49FF9FB3 ],
                          'SBSET'       :  [ 0x28001033 , 0x29FF9FB3 ],
                          'SBINV'       :  [ 0x68001033 , 0x69FF9FB3 ],
                          'SBEXT'       :  [ 0x48005033 , 0x49FFDFB3 ],
                          'GORC'        :  [ 0x28005033 , 0x29FFDFB3 ],
                          'GREV'        :  [ 0x68005033 , 0x69FFDFB3 ],
                          'CMIX'        :  [ 0x06001033 , 0xFFFF9FB3 ],
                          'CMOV'        :  [ 0x06005033 , 0xFFFFDFB3 ],    
                          'FSL'         :  [ 0x04001033 , 0xFDFF9FB3 ],
                          'FSR'         :  [ 0x04005033 , 0xFDFFDFB3 ],
                          'CLZ'         :  [ 0x60001013 , 0x600F9F93 ],
                          'CTZ'         :  [ 0x60101013 , 0x601F9F93 ],
                          'PCNT'        :  [ 0x60201013 , 0x602F9F93 ],
                          'SEXT.B'      :  [ 0x60401013 , 0x604F9F93 ],
                          'SEXT.H'      :  [ 0x60501013 , 0x605F9F93 ],
                          'CRC32.B'     :  [ 0x61001013 , 0x610F9F93 ],
                          'CRC32.H'     :  [ 0x61101013 , 0x611F9F93 ],
                          'CRC32.W'     :  [ 0x61201013 , 0x612F9F93 ],
                          'CRC32C.B'    :  [ 0x61801013 , 0x618F9F93 ],
                          'CRC32C.H'    :  [ 0x61901013 , 0x619F9F93 ],
                          'CRC32C.W'    :  [ 0x61A01013 , 0x61AF9F93 ],
                          'CLMUL'       :  [ 0x0A001033 , 0x0BFF9FB3 ],
                          'CLMULH'      :  [ 0x0A003033 , 0x0BFFBFB3 ],
                          'CLMULR'      :  [ 0x0A002033 , 0x0BFFAFB3 ],
                          'MIN'         :  [ 0x0A004033 , 0x0BFFCFB3 ],
                          'MAX'         :  [ 0x0A005033 , 0x0BFFDFB3 ],
                          'MINU'        :  [ 0x0A006033 , 0x0BFFEFB3 ],
                          'MAXU'        :  [ 0x0A007033 , 0x0BFFFFB3 ],
                          'BDEP'        :  [ 0x48006033 , 0x49FFEFB3 ],
                          'BEXT'        :  [ 0x08006033 , 0x09FFEFB3 ],
                          'PACK'        :  [ 0x08004033 , 0x09FFCFB3 ],
                          'PACKU'       :  [ 0x48004033 , 0x49FFCFB3 ],
                          'PACKH'       :  [ 0x08007033 , 0x09FFFFB3 ],
                          'SLOI'        :  [ 0x20001013 , 0x27FF9F93 ],
                          'SROI'        :  [ 0x20005013 , 0x27FFDF93 ],
                          'RORI'        :  [ 0x60005013 , 0x67FFDF93 ],
                          'SBCLRI'      :  [ 0x48001013 , 0x4FFF9F93 ],
                          'SBSETI'      :  [ 0x28001013 , 0x2FFF9F93 ],
                          'SBINVI'      :  [ 0x68001013 , 0x6FFF9F93 ],
                          'SBEXTI'      :  [ 0x48005013 , 0x4FFFDF93 ],
                          'SHFL'        :  [ 0x08001033 , 0x09FF9FB3 ],
                          'UNSHFL'      :  [ 0x08005033 , 0x09FFDFB3 ],
                          'SHFLI'       :  [ 0x08001013 , 0x0BFF9F93 ],
                          'UNSHFLI'     :  [ 0x08005013 , 0x0BFFDF93 ],
                          'GORCI'       :  [ 0x28005013 , 0x2FFFDF93 ],
                          'GREVI'       :  [ 0x68005013 , 0x6FFFDF93 ],
                          'FSRI'        :  [ 0x04005013 , 0xFFFFDF93 ],
                          'BFP'         :  [ 0x48007033 , 0x49FFFFB3 ]
    }
    
        for key , values in Instruction_dict.items() :
            for value in values :
                print(hex(value))
                mav_putvalue_instr = value

                # driving the input transaction
                dut.mav_putvalue_src1.value = mav_putvalue_src1
                dut.mav_putvalue_src2.value = mav_putvalue_src2
                dut.mav_putvalue_src3.value = mav_putvalue_src3
                dut.EN_mav_putvalue.value = 1
                dut.mav_putvalue_instr.value = mav_putvalue_instr
```

The assert statement is used for comparing the BitManipulation's output to the expected value.

The following error is seen:
```
    error_message = f'ERROR : DUT OUTPUT = {hex(dut_output)} does not match REF MODEL = {hex(expected_mav_putvalue)} for OPCODE = {key}'
    if( dut_output != expected_mav_putvalue ) :
        dut._log.info(error_message)
        ERROR_COUNT = ERROR_COUNT + 1
    
    # Final Error Checking to make the test decision.    
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message            
```

## Test Scenario **(Important)**
- Test Inputs: 
```
    11.49ns INFO     ANDN : INSTRUCTION =0x40007033
    11.49ns INFO     ANDN : SRC1 =0xdf238233
    11.49ns INFO     ANDN : SRC2 =0x708005fb
    11.49ns INFO     ANDN : SRC3 =0xe3b44375
    11.49ns INFO     ANDN : DUT OUTPUT =0xa0000067
    11.49ns INFO     ANDN : EXPECTED OUTPUT=0x11e470401
    11.49ns INFO     ERROR : DUT OUTPUT = 0xa0000067 does not match REF MODEL = 0x11e470401 for OPCODE = ANDN
```
- Expected Output: 0x11e470401
- Observed Output in the DUT dut.mav_putvalue = 0xa0000067

Output mismatches for the above inputs proving that there is a design bug with ANDN opcode.


## Design Bug
Based on the above test input and analysing the design, we see the following

```
  assign mav_putvalue =
	     { x__h33,
	       (mav_putvalue_instr[6:0] == 7'b0110011 ||
		mav_putvalue_instr[6:0] == 7'b0010011) &&
	       mav_putvalue_instr_BITS_31_TO_25_EQ_0b100000_A_ETC___d2336 } ;
           
  assign x__h33 =
	     NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d196 ?
	       field1___1__h3327 :
	       (NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d299 ?
		  field1___1__h4164 :
		  IF_NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ETC___d2279) ;
         
  assign IF_NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ETC___d2279 =
	     NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ma_ETC___d339 ?
	       field1___1__h4621 :
	       (NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d365 ?
		  IF_mav_putvalue_instr_BITS_21_TO_20_66_EQ_0b0__ETC___d2277 :
		  field1__h109) ;
          
  assign field1__h109 =
	     (mav_putvalue_instr[31:25] == 7'b0100000 &&
	      x__h254 == 10'b1110110011) ?
	       x__h39889 :
	       IF_mav_putvalue_instr_BITS_31_TO_25_EQ_0b10000_ETC___d2273 ;
  
  assign x__h39889 = mav_putvalue_src1 & mav_putvalue_src2 ;
```
The Output for the above buggy code is as follows:

![image](https://user-images.githubusercontent.com/109667378/182144137-e29b3cee-9e60-43e7-acfe-3acd843755ef.png)

The above code clearly suggests that mav_putvalue_src1 & mav_putvalue_src2 is assigned to field1__h109 which in turn is assigned to IF_NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ETC___d2279 which is assigned to x__h33 which is the output mav_putvalue

For the BitManipulation Processor design, the correct code is shown below.

```
  assign mav_putvalue =
	     { x__h33,
	       (mav_putvalue_instr[6:0] == 7'b0110011 ||
		mav_putvalue_instr[6:0] == 7'b0010011) &&
	       mav_putvalue_instr_BITS_31_TO_25_EQ_0b100000_A_ETC___d2336 } ;
           
  assign x__h33 =
	     NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d196 ?
	       field1___1__h3327 :
	       (NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d299 ?
		  field1___1__h4164 :
		  IF_NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ETC___d2279) ;
         
  assign IF_NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ETC___d2279 =
	     NOT_mav_putvalue_instr_BITS_14_TO_12_CONCAT_ma_ETC___d339 ?
	       field1___1__h4621 :
	       (NOT_mav_putvalue_instr_BITS_31_TO_25_EQ_0b1000_ETC___d365 ?
		  IF_mav_putvalue_instr_BITS_21_TO_20_66_EQ_0b0__ETC___d2277 :
		  field1__h109) ;
          
  assign field1__h109 =
	     (mav_putvalue_instr[31:25] == 7'b0100000 &&
	      x__h254 == 10'b1110110011) ?
	       x__h39889_local :
	       IF_mav_putvalue_instr_BITS_31_TO_25_EQ_0b10000_ETC___d2273 ;
  
  assign x__h39889 = mav_putvalue_src1 & mav_putvalue_src2 ;
  assign x__h39889_local = mav_putvalue_src1 & (~mav_putvalue_src2) ;
```
Here a new wire x__h39889_local is created for ANDN operation and the same is assigned to field1__h109 to correct the output for ANDN operation.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109667378/182145587-05049d68-aff5-446a-8e67-2394930f1597.png)

The updated design is checked in at https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/blob/master/level2_design_bug_free/mkbitmanip.v

## Verification Strategy
The verification strategy used for the verification of Sequener Design design is as follows:

```
a) An Instruction Dictionary was created for all opcodes mentioned in the ref model.
b) All opcodes mentioned within the dict created in a) was applied to the DUT with a delay of 1ns and also to the reference model present within the TB.
c) The DUT output mav_put_value was compared with the reference model output and ERROR_COUNT was asserted in case of mismatch.
d) Outside the for loop the , ERROR_COUNT variable was checked to be 0, if false then assertion error was flashed causing the test to fail.
```

## Is the verification complete ?
All the opcodes provided by the Reference model were applied to the DUT and the max_put_value_src1 ,  max_put_value_src2 ,  max_put_value_src3 values were put to random values between ( 0 , 2**32 - 1 ) and the same was executed for 100 times. An increase in the count of the number of times the opcode is executed will provide better coverage for max_put_value_src1 ,  max_put_value_src2 ,  max_put_value_src3 values. 

Providing the above inputs, we can say that the all possible input combinations have been tried , and the complete code has been excercised. This provides us more confidence about the verification strategy used to verify the Sequence Dectector 1011 design.
