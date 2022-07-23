# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock

from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    dut._log.info(f'After Reset = {dut.reset.value}')

    # Wait for few cycles before driving input
    dut.inp_bit.value = 0 ;
    for i in range(5) :
        await FallingEdge(dut.clk)

    INPUT_REGISTER = 0b0000 
    ERROR_COUNT    = 0 

    # Send a random sequence of 0 & 1 for 100 cycles.
    for i in range(100000) :
        #INPUT = random.randint(0,1)
        if  i == 0 :
            INPUT = 1 
        elif i == 1 :
            INPUT = 0 
        elif i == 2 :
            INPUT = 1 
        elif i == 3 :
            INPUT = 1 
        elif i == 4 :
            INPUT = 1 
        elif i == 5 :
            INPUT = 1 
        elif i == 6 :
            INPUT = 0
        else :
            INPUT = random.randint(0,1) 

        dut.inp_bit.value = INPUT
        dut._log.info(f'Input value Driven = {INPUT}')
        
        INPUT_REGISTER = ( INPUT_REGISTER << 1 ) + INPUT
        INPUT_REGISTER_MOD_16 = INPUT_REGISTER % 16
        #print(bin(INPUT_REGISTER_MOD_16))
        print(INPUT_REGISTER_MOD_16) 

        if( INPUT_REGISTER_MOD_16 == 11 ) :
            LOCAL_DUT_SEEN = 1
        else :
            LOCAL_DUT_SEEN = 0

        await FallingEdge(dut.clk)
        dut._log.info(f' Sequence Seen = {dut.seq_seen.value}')

        if(dut.seq_seen.value != LOCAL_DUT_SEEN ) :
            dut._log.info(f'ERROR : DUT OUTPUT = {dut.seq_seen.value} , {LOCAL_DUT_SEEN}')
            ERROR_COUNT = ERROR_COUNT + 1 
    
    cocotb.log.info(f'ERROR_COUNT = {ERROR_COUNT}')
    for i in range(5) :
        await FallingEdge(dut.clk)
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message 


