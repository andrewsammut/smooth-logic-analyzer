-- Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2018.2 (win64) Build 2258646 Thu Jun 14 20:03:12 MDT 2018
-- Date        : Wed Jul 20 14:44:15 2022
-- Host        : Gregory running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode synth_stub
--               c:/Users/Greg/Capstone/InputModule/InputModule.srcs/sources_1/bd/InputMod/ip/InputMod_selectio_wiz_0_0/InputMod_selectio_wiz_0_0_stub.vhdl
-- Design      : InputMod_selectio_wiz_0_0
-- Purpose     : Stub declaration of top-level module interface
-- Device      : xc7s50csga324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity InputMod_selectio_wiz_0_0 is
  Port ( 
    data_in_from_pins : in STD_LOGIC_VECTOR ( 0 to 0 );
    data_in_to_device : out STD_LOGIC_VECTOR ( 0 to 0 );
    clk_in : in STD_LOGIC;
    io_reset : in STD_LOGIC
  );

end InputMod_selectio_wiz_0_0;

architecture stub of InputMod_selectio_wiz_0_0 is
attribute syn_black_box : boolean;
attribute black_box_pad_pin : string;
attribute syn_black_box of stub : architecture is true;
attribute black_box_pad_pin of stub : architecture is "data_in_from_pins[0:0],data_in_to_device[0:0],clk_in,io_reset";
begin
end;
