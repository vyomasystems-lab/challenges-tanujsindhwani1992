# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    cocotb.log.info('##### CTB: Develop your test here ########')
    ERROR_COUNT = 0 ;
    for i in range(32):
        SEL = i ;
        dut._log.info(f'The value of i = {i:05}')
        dut.sel.value = SEL 
        VALUE = random.randint(0,3)
        dut.inp0.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp1.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp2.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp3.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp4.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp5.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp6.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp7.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp8.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp9.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp10.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp11.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp12.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp13.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp14.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp15.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp16.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp17.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp18.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp19.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp20.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp21.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp22.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp23.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp24.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp25.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp26.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp27.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp28.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp29.value = VALUE
        VALUE = random.randint(0,3)
        dut.inp30.value = VALUE

        await Timer(2, units='ns')

        if dut.sel.value == 0 & dut.out.value != dut.inp0.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;

        if dut.sel.value == 1 & dut.out.value != dut.inp1.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;

        if dut.sel.value == 2 & dut.out.value != dut.inp2.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;

        if dut.sel.value == 3 & dut.out.value != dut.inp3.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 4 & dut.out.value != dut.inp4.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 5 & dut.out.value != dut.inp5.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 6 & dut.out.value != dut.inp6.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 7 & dut.out.value != dut.inp7.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 8 & dut.out.value != dut.inp8.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 9 & dut.out.value != dut.inp9.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 10 & dut.out.value != dut.inp10.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 11 & dut.out.value != dut.inp11.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 12 & dut.out.value != dut.inp12.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 13 & dut.out.value != dut.inp13.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 14 & dut.out.value != dut.inp14.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 15 & dut.out.value != dut.inp15.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 16 & dut.out.value != dut.inp16.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 17 & dut.out.value != dut.inp17.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 18 & dut.out.value != dut.inp18.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                        
        if dut.sel.value == 19 & dut.out.value != dut.inp19.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 20 & dut.out.value != dut.inp20.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 21 & dut.out.value != dut.inp21.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 22 & dut.out.value != dut.inp22.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 23 & dut.out.value != dut.inp23.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 24 & dut.out.value != dut.inp24.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 25 & dut.out.value != dut.inp25.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 26 & dut.out.value != dut.inp26.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 27 & dut.out.value != dut.inp27.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 28 & dut.out.value != dut.inp28.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 29 & dut.out.value != dut.inp29.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 30 & dut.out.value != dut.inp30.value:
            ERROR_COUNT = ERROR_COUNT + 1 ;
                                    
        if dut.sel.value == 31 & dut.out.value != 0:
            ERROR_COUNT = ERROR_COUNT + 1 ;

    await Timer(2, units='ns')                        
    assert ERROR_COUNT == 0 , f"Mux result incorrect for sel value : {dut.sel.value}"            