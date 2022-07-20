-- Copyright 1986-2018 Xilinx, Inc. All Rights Reserved.
-- --------------------------------------------------------------------------------
-- Tool Version: Vivado v.2018.2 (win64) Build 2258646 Thu Jun 14 20:03:12 MDT 2018
-- Date        : Wed Jul 20 14:44:15 2022
-- Host        : Gregory running 64-bit major release  (build 9200)
-- Command     : write_vhdl -force -mode funcsim
--               c:/Users/Greg/Capstone/InputModule/InputModule.srcs/sources_1/bd/InputMod/ip/InputMod_selectio_wiz_0_0/InputMod_selectio_wiz_0_0_sim_netlist.vhdl
-- Design      : InputMod_selectio_wiz_0_0
-- Purpose     : This VHDL netlist is a functional simulation representation of the design and should not be modified or
--               synthesized. This netlist cannot be used for SDF annotated simulation.
-- Device      : xc7s50csga324-1
-- --------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz is
  port (
    data_in_from_pins : in STD_LOGIC_VECTOR ( 0 to 0 );
    data_in_to_device : out STD_LOGIC_VECTOR ( 0 to 0 );
    clk_in : in STD_LOGIC;
    io_reset : in STD_LOGIC
  );
  attribute DEV_W : integer;
  attribute DEV_W of InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz : entity is 1;
  attribute ORIG_REF_NAME : string;
  attribute ORIG_REF_NAME of InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz : entity is "InputMod_selectio_wiz_0_0_selectio_wiz";
  attribute SYS_W : integer;
  attribute SYS_W of InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz : entity is 1;
end InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz;

architecture STRUCTURE of InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz is
  signal data_in_from_pins_int : STD_LOGIC;
  attribute BOX_TYPE : string;
  attribute BOX_TYPE of \pins[0].fdre_in_inst\ : label is "PRIMITIVE";
  attribute IOB : string;
  attribute IOB of \pins[0].fdre_in_inst\ : label is "TRUE";
  attribute BOX_TYPE of \pins[0].ibuf_inst\ : label is "PRIMITIVE";
  attribute CAPACITANCE : string;
  attribute CAPACITANCE of \pins[0].ibuf_inst\ : label is "DONT_CARE";
  attribute IBUF_DELAY_VALUE : string;
  attribute IBUF_DELAY_VALUE of \pins[0].ibuf_inst\ : label is "0";
  attribute IFD_DELAY_VALUE : string;
  attribute IFD_DELAY_VALUE of \pins[0].ibuf_inst\ : label is "AUTO";
begin
\pins[0].fdre_in_inst\: unisim.vcomponents.FDRE
    generic map(
      INIT => '0',
      IS_C_INVERTED => '0',
      IS_D_INVERTED => '0',
      IS_R_INVERTED => '0'
    )
        port map (
      C => clk_in,
      CE => '1',
      D => data_in_from_pins_int,
      Q => data_in_to_device(0),
      R => io_reset
    );
\pins[0].ibuf_inst\: unisim.vcomponents.IBUF
     port map (
      I => data_in_from_pins(0),
      O => data_in_from_pins_int
    );
end STRUCTURE;
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
library UNISIM;
use UNISIM.VCOMPONENTS.ALL;
entity InputMod_selectio_wiz_0_0 is
  port (
    data_in_from_pins : in STD_LOGIC_VECTOR ( 0 to 0 );
    data_in_to_device : out STD_LOGIC_VECTOR ( 0 to 0 );
    clk_in : in STD_LOGIC;
    io_reset : in STD_LOGIC
  );
  attribute NotValidForBitStream : boolean;
  attribute NotValidForBitStream of InputMod_selectio_wiz_0_0 : entity is true;
  attribute DEV_W : integer;
  attribute DEV_W of InputMod_selectio_wiz_0_0 : entity is 1;
  attribute SYS_W : integer;
  attribute SYS_W of InputMod_selectio_wiz_0_0 : entity is 1;
end InputMod_selectio_wiz_0_0;

architecture STRUCTURE of InputMod_selectio_wiz_0_0 is
  attribute DEV_W of inst : label is 1;
  attribute SYS_W of inst : label is 1;
begin
inst: entity work.InputMod_selectio_wiz_0_0_InputMod_selectio_wiz_0_0_selectio_wiz
     port map (
      clk_in => clk_in,
      data_in_from_pins(0) => data_in_from_pins(0),
      data_in_to_device(0) => data_in_to_device(0),
      io_reset => io_reset
    );
end STRUCTURE;
