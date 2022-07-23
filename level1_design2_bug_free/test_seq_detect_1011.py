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
    for i in range(1000) :
        # Driving random value between 0 & 1 to the DUT.
        INPUT = random.randint(0,1)
        dut.inp_bit.value = INPUT
        dut._log.info(f'Input value Driven = {INPUT}')
        
        # Computing the 4 bit 1011 Sequence Detector Gold Logic
        # a. INPUT value selected above is shifted to an INPUT_REGISTER
        # b. INPUT_REGISTER % 16 provides us the previous 4 input bits transmitted
        INPUT_REGISTER = ( INPUT_REGISTER << 1 ) + INPUT
        INPUT_REGISTER_MOD_16 = INPUT_REGISTER % 16

        # If previous 4 bits transmitted == 1011 in binary or 11 in decimal , assert LOCAL_DUT_SEEN
        if( INPUT_REGISTER_MOD_16 == 11 ) :
            LOCAL_DUT_SEEN = 1
        else :
            LOCAL_DUT_SEEN = 0

        # Waiting for DUT to sample value & provide seq_seen
        await FallingEdge(dut.clk)
        if( dut.seq_seen.value == 1) :
            dut._log.info(f'SEQUENE DETECTED BY DUT')
        if( LOCAL_DUT_SEEN == 1) :
            dut._log.info(f'SEQUENE DETECTED BY REF MODEL')

        # Comparing DUT 'seq_seen' with LOCAL_DUT_SEEN variable
        if(dut.seq_seen.value != LOCAL_DUT_SEEN ) :
            dut._log.info(f'ERROR : DUT OUTPUT = {dut.seq_seen.value} , REF MODEL OUTPUT = {LOCAL_DUT_SEEN} , PREVIOUS 4 INPUTS = {bin(INPUT_REGISTER_MOD_16)}')
            ERROR_COUNT = ERROR_COUNT + 1 
    
    # In order to make the test run without terminating , incrementing ERROR_COUNT variable 
    # If ERROR_COUNT !=0 , assert Error to make the Test Fail
    cocotb.log.info(f'ERROR_COUNT = {ERROR_COUNT}')
    for i in range(5) :
        await FallingEdge(dut.clk)
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message 
