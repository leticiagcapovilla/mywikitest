---
title: bsb
description: 
published: 1
date: 2024-05-21T20:26:19.079Z
tags: 
editor: markdown
dateCreated: 2024-05-20T21:11:38.464Z
---

# CON: Basic switching board

<br>

## Introduction 
The [LNLS Controls Group](/Machine/Groups/CON) has developed a simple hardware which is able to switching outputs according to the Process Variables value, previously defined by user. The Hardware is based on na adaptation of the [SerialXXCON](link) board and its outputs are controlled by some BeagleBone Blacks pinouts.
To define each PV and its limits, the user writes to an “.xlsx file”, setting maximum and minimum value and which output will be switched if any PV has exceeded the values.

To access the project, [click here](https://gitlab.cnpem.br/robert.polli/basic-switching/){target=_blank} and go to the gitlab page (internal network only).

<br>

## Hardware Overview 
The Hardware is basically four relays controlled by digital pinouts of the BeagleBone, triggered by a transistor configured as a switch. It is used with a SerialXXCON Board, and connects to it via its [CON:SPIxxCON|SPIXXCON](link) bus, where the BBB‘s four digital pins are available.
The table below show where the outputs are connected at SPIXXCON bus as well as which BBB pinouts that controls them. 

<br>

|Output Connector| Name on SPIXXCON bus| Pin Out (BBB) |
|-|-|-|
|Out 01| DIO 01| P8_42 |
|Out 02| DIO 02| P9_27 |
|Out 03| DIO 03| P9_24 |
|Out 04| DIO 04| P8_44  |


Each output is controlled by a circuit similar to shown below, where a transistor controls the current which flowing through coils. Also, the hardware has a jumpers selector, of which it is possible select whether the normal output state is open or closed.
 
|![](/img/groups/con/bsb/OutputBSB.png)|
|-|
|**Figure 1**: Output switching module.|

<br>

## Software Overview 

The BeagleBone Black’s software is responsible to reading the “pvs.xlsx" file, connecting each PV of it and monitoring if any of them has exceeded the limits values.

Initially, the program reads the table and connects the monitoring of each PV by the camonitor command. After that, a suspension loop is triggered while no PV changes its value. When camonitor detects any changes, the comparison function is called (changed_pv) and checks whether the value is out of the user-defined range or not, calling the “set_outputs” function after that.

The second function of program is “set_outputs”, whose objective is to create a list containing the outputs that will be opened (with 1) and those that will be closed (with 0). To do this, first, it reads the table of “pvs.xlsx" file to get the necessary state of each output according the value pvs and then, creates a list for each board output.
Furthermore, the function also is responsible to updating the log file, where writes the name, value and limit of PV that has exceeded the range, as well as the switched output.

Finally, the “switch_out” function is called, where the program will changes the pin-out value that will alternates the relays connected to the outputs. As the outputs are related to a list (created in the “set_outputs” function), here is made the average of these lists of each output, if the average is different from 0, it means that at least one output has been configured as “1”, then, the pin out is set to high.

|![](/img/groups/con/bsb/OutputBSB.png)|
|-|
|**Figure 2**: BSB Fluxogram.|

<br>

### Usage steps 
First, edits the “pvs.xlsx” table, present in the “./basic-switching/src” directory. Put in it all pvs which will control each output. After that, set the minimum and maximum (Range) value that the Process Variable may take on.

Thereafter, choose which output will be switched if some PV exceeded the limit (1 to switch and 0 to not switch) and if it will happen at the High limit, low limit or both.

Important: More than One PV can Switch a single output.

<br>

## Maximum Board Specifications 

|Maximum switching current| 2A resistive |
|-|-|
|Maximum switching voltage| 100 VDC / 70VAC - RMS |
|Maximum switching power| 60 W / 125 VA |
|Operate time| 6 ms |
|Release time| 4 ms  |
