//Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2018.2 (win64) Build 2258646 Thu Jun 14 20:03:12 MDT 2018
//Date        : Wed Jul 20 15:11:53 2022
//Host        : Gregory running 64-bit major release  (build 9200)
//Command     : generate_target InputMod.bd
//Design      : InputMod
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

(* CORE_GENERATION_INFO = "InputMod,IP_Integrator,{x_ipVendor=xilinx.com,x_ipLibrary=BlockDiagram,x_ipName=InputMod,x_ipVersion=1.00.a,x_ipLanguage=VERILOG,numBlks=4,numReposBlks=4,numNonXlnxBlks=0,numHierBlks=0,maxHierDepth=0,numSysgenBlks=0,numHlsBlks=0,numHdlrefBlks=0,numPkgbdBlks=0,bdsource=USER,synth_mode=OOC_per_IP}" *) (* HW_HANDOFF = "InputMod.hwdef" *) 
module InputMod
   (InP,
    clk,
    outP,
    rst);
  input InP;
  (* X_INTERFACE_INFO = "xilinx.com:signal:clock:1.0 CLK.CLK CLK" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME CLK.CLK, CLK_DOMAIN InputMod_clk, FREQ_HZ 100000000, PHASE 0.000" *) input clk;
  output [0:0]outP;
  (* X_INTERFACE_INFO = "xilinx.com:signal:reset:1.0 RST.RST RST" *) (* X_INTERFACE_PARAMETER = "XIL_INTERFACENAME RST.RST, POLARITY ACTIVE_HIGH" *) input rst;

  wire InP_1;
  wire clk_1;
  wire clk_wiz_0_clk_out1;
  wire [0:0]fifo_generator_0_dout;
  wire rst_1;
  wire [0:0]selectio_wiz_0_data_in_to_device;
  wire [0:0]xlconstant_0_dout;

  assign InP_1 = InP;
  assign clk_1 = clk;
  assign outP[0] = fifo_generator_0_dout;
  assign rst_1 = rst;
  InputMod_clk_wiz_0_0 clk_wiz_0
       (.clk_in1(clk_1),
        .clk_out1(clk_wiz_0_clk_out1),
        .reset(rst_1));
  InputMod_fifo_generator_0_0 fifo_generator_0
       (.clk(clk_wiz_0_clk_out1),
        .din(selectio_wiz_0_data_in_to_device),
        .dout(fifo_generator_0_dout),
        .rd_en(xlconstant_0_dout),
        .rst(1'b0),
        .wr_en(xlconstant_0_dout));
  InputMod_selectio_wiz_0_0 selectio_wiz_0
       (.clk_in(clk_wiz_0_clk_out1),
        .data_in_from_pins(InP_1),
        .data_in_to_device(selectio_wiz_0_data_in_to_device),
        .io_reset(1'b0));
  InputMod_xlconstant_0_0 xlconstant_0
       (.dout(xlconstant_0_dout));
endmodule
