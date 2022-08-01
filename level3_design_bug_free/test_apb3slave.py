# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.clock import Clock


# Sample Test
@cocotb.test()
async def test_apb3slave(dut):
    
    # Clock Generation
    clock = Clock(dut.PCLK, 10, units="us")  # Create a 10us period clock on port PCLK
    cocotb.start_soon(clock.start())         # Start the clock

    # Reset Generation
    dut.PRESETn.value = 0
    for i in range(5) :
        await RisingEdge(dut.PCLK)  
    
    dut.PRESETn.value = 1
    await RisingEdge(dut.PCLK)              

    # Reset all input value
    dut.PADDR.value  = 0
    dut.PSEL.value   = 0 
    dut.PWRITE.value = 0
    dut.PWDATA.value = 0  
    await RisingEdge(dut.PCLK)               
    ERROR_COUNT = 0

    # Random Write followed by Read to the APB3 Slave
    for i in range(100) :
        dut.PADDR.value  = random.randint(0,255)
        dut.PSEL.value   = 1 
        dut.PWRITE.value = 1  # must be 1 for Write transaction
        dut_write_data   = random.randint(0,4294967295)
        dut.PWDATA.value = dut_write_data
        await RisingEdge(dut.PREADY)       
        await RisingEdge(dut.PCLK)          
        cocotb.log.info(f'DUT WRITE DATA ={hex(dut_write_data)}')

        dut.PSEL.value   = 1 
        dut.PWRITE.value = 0  # must be 0 for Read transaction
        await RisingEdge(dut.PREADY)          
        await RisingEdge(dut.PCLK) 

        # obtaining the output
        dut_read_data = dut.PRDATA.value
        cocotb.log.info(f'DUT READ DATA ={hex(dut_read_data)}')

        # comparison
        error_message = f'ERROR : Read Data from DUT = {hex(dut_read_data)} does not match Write Data = {hex(dut_write_data)}'
        if( dut_read_data != dut_write_data ) :
            dut._log.info(error_message)
            ERROR_COUNT = ERROR_COUNT + 1 

    cocotb.log.info(f'ERROR_COUNT = {ERROR_COUNT}')
    for i in range(5) :
        await FallingEdge(dut.PCLK)

    # Final Error Checking to make the test decision.    
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message 




