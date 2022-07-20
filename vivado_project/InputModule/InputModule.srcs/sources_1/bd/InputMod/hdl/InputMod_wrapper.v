//Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2018.2 (win64) Build 2258646 Thu Jun 14 20:03:12 MDT 2018
//Date        : Wed Jul 20 15:11:53 2022
//Host        : Gregory running 64-bit major release  (build 9200)
//Command     : generate_target InputMod_wrapper.bd
//Design      : InputMod_wrapper
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module InputMod_wrapper
   (InP,
    clk,
    outP,
    rst);
  input InP;
  input clk;
  output [0:0]outP;
  input rst;

  wire InP;
  wire clk;
  wire [0:0]outP;
  wire rst;

  InputMod InputMod_i
       (.InP(InP),
        .clk(clk),
        .outP(outP),
        .rst(rst));
endmodule
