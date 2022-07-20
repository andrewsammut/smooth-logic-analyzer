// Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
// --------------------------------------------------------------------------------
// Tool Version: Vivado v.2018.2 (win64) Build 2258646 Thu Jun 14 20:03:12 MDT 2018
// Date        : Wed Jul 20 14:44:15 2022
// Host        : Gregory running 64-bit major release  (build 9200)
// Command     : write_verilog -force -mode funcsim
//               c:/Users/Greg/Capstone/InputModule/InputModule.srcs/sources_1/bd/InputMod/ip/InputMod_selectio_wiz_0_0/InputMod_selectio_wiz_0_0_sim_netlist.v
// Design      : InputMod_selectio_wiz_0_0
// Purpose     : This verilog netlist is a functional simulation representation of the design and should not be modified
//               or synthesized. This netlist cannot be used for SDF annotated simulation.
// Device      : xc7s50csga324-1
// --------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* DEV_W = "1" *) (* SYS_W = "1" *) 
(* NotValidForBitStream *)
module InputMod_selectio_wiz_0_0
   (data_in_from_pins,
    data_in_to_device,
    clk_in,
    io_reset);
  input [0:0]data_in_from_pins;
  output [0:0]data_in_to_device;
  input clk_in;
  input io_reset;

  wire clk_in;
  (* IBUF_LOW_PWR *) (* IOSTANDARD = "LVCMOS33" *) wire [0:0]data_in_from_pins;
  wire [0:0]data_in_to_device;
  wire io_reset;

  (* DEV_W = "1" *) 
  (* SYS_W = "1" *) 
  InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz inst
       (.clk_in(clk_in),
        .data_in_from_pins(data_in_from_pins),
        .data_in_to_device(data_in_to_device),
        .io_reset(io_reset));
endmodule

(* DEV_W = "1" *) (* ORIG_REF_NAME = "InputMod_selectio_wiz_0_0_selectio_wiz" *) (* SYS_W = "1" *) 
module InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz
   (data_in_from_pins,
    data_in_to_device,
    clk_in,
    io_reset);
  input [0:0]data_in_from_pins;
  output [0:0]data_in_to_device;
  input clk_in;
  input io_reset;

  wire clk_in;
  wire [0:0]data_in_from_pins;
  wire data_in_from_pins_int;
  wire [0:0]data_in_to_device;
  wire io_reset;

  (* BOX_TYPE = "PRIMITIVE" *) 
  (* IOB = "TRUE" *) 
  FDRE #(
    .INIT(1'b0),
    .IS_C_INVERTED(1'b0),
    .IS_D_INVERTED(1'b0),
    .IS_R_INVERTED(1'b0)) 
    \pins[0].fdre_in_inst 
       (.C(clk_in),
        .CE(1'b1),
        .D(data_in_from_pins_int),
        .Q(data_in_to_device),
        .R(io_reset));
  (* BOX_TYPE = "PRIMITIVE" *) 
  (* CAPACITANCE = "DONT_CARE" *) 
  (* IBUF_DELAY_VALUE = "0" *) 
  (* IFD_DELAY_VALUE = "AUTO" *) 
  IBUF \pins[0].ibuf_inst 
       (.I(data_in_from_pins),
        .O(data_in_from_pins_int));
endmodule
`ifndef GLBL
`define GLBL
`timescale  1 ps / 1 ps

module glbl ();

    parameter ROC_WIDTH = 100000;
    parameter TOC_WIDTH = 0;

//--------   STARTUP Globals --------------
    wire GSR;
    wire GTS;
    wire GWE;
    wire PRLD;
    tri1 p_up_tmp;
    tri (weak1, strong0) PLL_LOCKG = p_up_tmp;

    wire PROGB_GLBL;
    wire CCLKO_GLBL;
    wire FCSBO_GLBL;
    wire [3:0] DO_GLBL;
    wire [3:0] DI_GLBL;
   
    reg GSR_int;
    reg GTS_int;
    reg PRLD_int;

//--------   JTAG Globals --------------
    wire JTAG_TDO_GLBL;
    wire JTAG_TCK_GLBL;
    wire JTAG_TDI_GLBL;
    wire JTAG_TMS_GLBL;
    wire JTAG_TRST_GLBL;

    reg JTAG_CAPTURE_GLBL;
    reg JTAG_RESET_GLBL;
    reg JTAG_SHIFT_GLBL;
    reg JTAG_UPDATE_GLBL;
    reg JTAG_RUNTEST_GLBL;

    reg JTAG_SEL1_GLBL = 0;
    reg JTAG_SEL2_GLBL = 0 ;
    reg JTAG_SEL3_GLBL = 0;
    reg JTAG_SEL4_GLBL = 0;

    reg JTAG_USER_TDO1_GLBL = 1'bz;
    reg JTAG_USER_TDO2_GLBL = 1'bz;
    reg JTAG_USER_TDO3_GLBL = 1'bz;
    reg JTAG_USER_TDO4_GLBL = 1'bz;

    assign (strong1, weak0) GSR = GSR_int;
    assign (strong1, weak0) GTS = GTS_int;
    assign (weak1, weak0) PRLD = PRLD_int;

    initial begin
	GSR_int = 1'b1;
	PRLD_int = 1'b1;
	#(ROC_WIDTH)
	GSR_int = 1'b0;
	PRLD_int = 1'b0;
    end

    initial begin
	GTS_int = 1'b1;
	#(TOC_WIDTH)
	GTS_int = 1'b0;
    end

endmodule
`endif
