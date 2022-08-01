# APB3 Slave Design Verification

The APB3 Slave Design verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/109667378/182148938-c20762f9-a79c-4c9e-878e-47e6488b6472.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (APB3 Slave module here) which takes in PCLK , PRESETn , PADDR , PWRITE , PSEL and PWDATA as inputs. The DUT contains a memory reg [`DATAWIDTH-1:0] RAM [0:2**`ADDRWIDTH -1] which is used for storing the Write Data provied by the Master. Also, the same memory provides the PRDATA as output from the Slave. 

```
APB3 Slave provides a low cost interface to the APB Master which is not pipelined in nature. 
At a given point, the APB Master can only generate a Read or a Write transfer to the Slave but not both. Also, all APB transfers takes a minimum of 2 cycles to complete. 

Signal	Source	Description
PCLK	Clock	The rising edge of PCLK times all transfers on the APB.
PRESETn	Reset	The APB reset signal is active LOW.
PADDR	Master	This is the APB address bus. It can be up to 32 bits wide and is driven by the peripheral bus bridge unit.
PSELx	Master	Each slave device has this signal. It demonstrates which slave is chosen for data transaction
PENABLE	Master	This signal indicates the second and subsequent cycles of an APB transfer
PWRITE	Master	This signal indicates an APB write access when HIGH and an APB read access when LOW.
PWDATA	Master	This bus is driven by the peripheral bus bridge unit during write cycles when PWRITE is HIGH. This bus can be up to 32 bits wide.
PREADY	Slave	The slave uses this signal to extend an APB transfer.
PRDATA	Slave	The selected slave drives this bus during read cycles when PWRITE is LOW. This bus can be up to 32-bits wide.
PSLVERR	Slave	This signal indicates a transfer failure

APB3 Slave State machine is defined as
•	IDLE This is the default state of the APB.
•	SETUP When a transfer is required the bus moves into the SETUP state, where the appropriate select signal, PSELx, is asserted. 
•	ACCESS The enable signal, PENABLE, is asserted in the ACCESS state. The address, write, select, and write data signals must remain stable during the transition from the SETUP to ACCESS state.
```

![image](https://user-images.githubusercontent.com/109667378/182149560-ad5be7a8-ccc8-4993-8316-46ed848966a6.png)

The values are assigned to the input port using 
```
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
```

The assert statement is used for comparing the APB3 Slave Detector's outut to the expected value.

The following error is seen:
```
    error_message = f'ERROR : Read Data from DUT = {hex(dut_read_data)} does not match Write Data = {hex(dut_write_data)}'
    if( dut_read_data != dut_write_data ) :
       dut._log.info(error_message)
       ERROR_COUNT = ERROR_COUNT + 1 
    
    # Final Error Checking to make the test decision.    
    error_message = f'ERROR MESSAGE COUNT =  {hex(ERROR_COUNT)}'
    assert ERROR_COUNT == 0 , error_message            
```

## Test Scenario **(Important)**
- Test Inputs: 
```
4040000.00ns INFO     DUT WRITE DATA =0xf793b730
4060000.00ns INFO     DUT READ DATA =0x7793b730
4060000.00ns INFO     ERROR : Read Data from DUT = 0x7793b730 does not match Write Data = 0xf793b730
```
- Expected Output: Read Data = 0xf793b730
- Observed Output in the DUT dut.PRDATA = 0x7793b730

Output mismatches for the above inputs proving that there is a design bug.
From the above test input, it is clear that Design is not assigning the 31 bit correctly during write.

## Design Bug
Based on the above test input and analysing the design, we see the following

```
    case (State)
      `IDLE : begin
        PRDATA <= 0;
        PREADY <= 0;
        if (PSEL) begin
          if (PWRITE) begin
            State <= `W_ENABLE;
          end
          else begin
            State <= `R_ENABLE;
          end
        end
      end

      `W_ENABLE : begin
        if (PSEL && PWRITE) begin
          RAM[PADDR]  <= PWDATA[30:0];   ===> BUG : 31st bit not assigned during Write.
          PREADY <=1;          
        end
          State <= `IDLE;
      end

      `R_ENABLE : begin
        if (PSEL && !PWRITE) begin
          PREADY <= 1;
          PRDATA <= RAM[PADDR];
        end
        State <= `IDLE;
      end
      default: begin
        State <= `IDLE;
      end
    endcase
```
The Output for the above buggy code is as follows:

![image](https://user-images.githubusercontent.com/109667378/182150506-388e318b-5b5b-4944-b4b0-efdad62526cc.png)

For the APB3 Slave design, the correct code is shown below.

```
    case (State)
      `IDLE : begin
        PRDATA <= 0;
        PREADY <= 0;
        if (PSEL) begin
          if (PWRITE) begin
            State <= `W_ENABLE;
          end
          else begin
            State <= `R_ENABLE;
          end
        end
      end

      `W_ENABLE : begin
        if (PSEL && PWRITE) begin
          RAM[PADDR]  <= PWDATA;
          PREADY <=1;          
        end
          State <= `IDLE;
      end

      `R_ENABLE : begin
        if (PSEL && !PWRITE) begin
          PREADY <= 1;
          PRDATA <= RAM[PADDR];
        end
        State <= `IDLE;
      end
      default: begin
        State <= `IDLE;
      end
    endcase
```

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/109667378/182136084-4f4e166e-974c-445b-9d27-1fb68cead31c.png)

The updated design is checked in at https://github.com/vyomasystems-lab/challenges-tanujsindhwani1992/blob/master/level1_design2_bug_free/seq_detect_1011.v

## Verification Strategy
The verification strategy used for the verification of APB3 Slave Design design is as follows:

```
a) Send a random sequence of 0 & 1 on inp_bit input for 1000 cycles.
b) Save the same inp_bit applied to the DUT onto a 4 bit shift register by shifting left the previous content by 1 bit and adding the inp_bit 
c) If the 4 bit shift register contains value 1011 , assert golden seq_seen bit.
d) Compare DUT seq_seen and golden seq_seen. If mismatch , increase ERROR COUNT
e) Assert ERROR_COUNT == 0 to make the decision about test fail or pass.
```

## Is the verification complete ?
A random sequnce of 0 & 1 was applied to the DUT for 1000 cycles and on the fly checking was done by using a 4 bit shift register.
A mismatch between the DUT's output and shift register's contents was highlighted within the Error.

Providing the above inputs, we can say that the all possible input combinations have been tried , and the complete code has been excercised. This provides us more confidence about the verification strategy used to verify the APB3 Slave design.
