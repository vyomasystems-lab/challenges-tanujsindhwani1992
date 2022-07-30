# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
export PYTHONPATH := $(PWD):$(PYTHONPATH)  # reference model

VERILOG_SOURCES = $(PWD)/APB_Slave.v               # provide your design path

TOPLEVEL := APB_Slave         # design file
MODULE   := test_apb3slave    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
