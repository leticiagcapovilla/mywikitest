# CON: Beam loss monitors data acquisition system

## Introduction

[CON:CON|LNLS Controls Group](link) is designing a simple hardware solution for data acquisition from beam loss monitors (BLMs) that will be installed at Sirius. The current prototype is capable of counting pulses from up to six sensors at a maximum rate of 15 MHz. It has an Ethernet port for connection to the control system network. This port must be connected to a power sourcing equipment (PSE) of the Power over Ethernet (PoE) standard (IEEE 802.3af).

## Hardware detailed

The Hardware was based on Altera's FPGA (Field Programmable Gate Array) MAX 10, a programmable hardware where the control program was developed, which has the function of processing the data acquired by the BLMs (Beam Loss Monitor) and then send it to the user.
Has inputs for up to six sensor, two of Bergoz Instrumantation and four to BLMs developed at LNLS. 
To exchange information between the FPGA and the user, the BeagleBone Black was used, which takes data from the FPGA through the SPI (Serial Peripheral Interface) communication pins and send it  through Ethernet communication.

The circuit's power supply is provided by a Power Over Ethernet (POE) module that allows the electrical current needed for circuit operation to be carried over the Ethernet data cables, minimizing the number of cables required for hardware operations, without compromise the exchange of information. The POE used in this version is the Ag9205 produced by Silvertel and has 5V output. For powering the BLMs, the hardware needs to supply + 5V, -5V and + 24V (-5V is exclusive to Sensors of Bregoz) and these values are obtained using DC / DC converters, the VIBLSD1-S5-S5-DIP and MEV1D0512DC.


|![](/img/groups/con/beam_loss_monitor/ContFóton.jpg)|
|-|
|**Figure 1**: Finished *ContFóton*.|

## EPICS interface

### IOC

### Operator interfaces
