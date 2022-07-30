# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    cocotb.log.info('##### CTB: Develop your test here ########')
    ERROR_COUNT = 0 ;
    for i in range(32):
        
        # Driving Input values
        SEL = i ;
        dut.sel.value = SEL 
        VALUE = random.randint(1,3)
        dut.inp0.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp1.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp2.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp3.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp4.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp5.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp6.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp7.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp8.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp9.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp10.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp11.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp12.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp13.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp14.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp15.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp16.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp17.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp18.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp19.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp20.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp21.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp22.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp23.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp24.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp25.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp26.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp27.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp28.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp29.value = VALUE
        VALUE = random.randint(1,3)
        dut.inp30.value = VALUE

        await Timer(2, units='ns')

        # Comparing Output depending upon the value of SEL applied.
        if dut.sel.value == 0 :
            if dut.out.value != dut.inp0.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp0.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 1 :
            if dut.out.value != dut.inp1.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp1.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 2 :
            if dut.out.value != dut.inp2.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp2.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 3 :
            if dut.out.value != dut.inp3.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp3.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 4 :
            if dut.out.value != dut.inp4.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp4.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 5 :
            if dut.out.value != dut.inp5.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp5.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 6 :
            if dut.out.value != dut.inp6.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp6.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 7 :
            if dut.out.value != dut.inp7.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp7.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 8 :
            if dut.out.value != dut.inp8.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp8.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 9 :
            if dut.out.value != dut.inp9.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp9.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1

        if dut.sel.value == 10 :
            if dut.out.value != dut.inp10.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp10.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 11 :
            if dut.out.value != dut.inp11.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp11.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 12 :
            if dut.out.value != dut.inp12.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp12.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 13 :
            if dut.out.value != dut.inp13.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp13.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 14 :
            if dut.out.value != dut.inp14.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp14.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 15 :
            if dut.out.value != dut.inp15.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp15.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 16 :
            if dut.out.value != dut.inp16.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp16.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 17 :
            if dut.out.value != dut.inp17.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp17.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 18 :
            if dut.out.value != dut.inp18.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp18.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 19 :
            if dut.out.value != dut.inp19.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp19.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 20 :
            if dut.out.value != dut.inp20.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp20.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 21 :
            if dut.out.value != dut.inp21.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp21.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1

        if dut.sel.value == 22 :
            if dut.out.value != dut.inp22.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp22.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 23 :
            if dut.out.value != dut.inp23.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp23.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1

        if dut.sel.value == 24 :
            if dut.out.value != dut.inp24.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp24.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 25 :
            if dut.out.value != dut.inp25.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp25.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 26 :
            if dut.out.value != dut.inp26.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp26.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 27 :
            if dut.out.value != dut.inp27.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp27.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 28 :
            if dut.out.value != dut.inp28.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp28.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 29 :
            if dut.out.value != dut.inp29.value : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp29.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 30 :
            if dut.out.value != dut.inp30.value :
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = {dut.inp30.value} , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

        if dut.sel.value == 31 :
            if dut.out.value != 0 : 
                dut._log.info(f'ERROR : The Select value = {dut.sel.value} , Input value = 0 , Output value = {dut.out.value}')
                ERROR_COUNT = ERROR_COUNT + 1 

    # Final Error Checking to make the test decision.    
    cocotb.log.info(f'ERROR_COUNT = {ERROR_COUNT}')
    await Timer(2, units='ns') 
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message         