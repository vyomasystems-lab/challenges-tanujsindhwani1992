# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    
    Instruction_dict = {  #'ANDN'        :  [ 0x40007033 , 0x41FFFFB3 ],  #Error Found
                          'ORN'         :  [ 0x40006033 , 0x41FFEFB3 ],
                          'XNOR'        :  [ 0x40004033 , 0x41FFCFB3],
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

    # input transaction
    for i in range (1) :
        mav_putvalue_src1 = random.randint(0,4294967296)
        mav_putvalue_src2 = random.randint(0,4294967296)
        mav_putvalue_src3 = random.randint(0,4294967296)
        
        for key , values in Instruction_dict.items() :
            for value in values :
                print(hex(value))
                mav_putvalue_instr = value

                # expected output from the model
                expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

                # driving the input transaction
                dut.mav_putvalue_src1.value = mav_putvalue_src1
                dut.mav_putvalue_src2.value = mav_putvalue_src2
                dut.mav_putvalue_src3.value = mav_putvalue_src3
                dut.EN_mav_putvalue.value = 1
                dut.mav_putvalue_instr.value = mav_putvalue_instr

                yield Timer(1) 

                # obtaining the output
                dut_output = dut.mav_putvalue.value

                cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
                cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

                # comparison
                error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
                assert dut_output == expected_mav_putvalue, error_message
