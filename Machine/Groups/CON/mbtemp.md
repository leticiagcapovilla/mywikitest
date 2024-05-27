---
title: mbtemp
description: 
published: 1
date: 2024-05-27T21:38:24.563Z
tags: 
editor: markdown
dateCreated: 2024-05-27T21:20:33.868Z
---

# CON: MBTemp

<br >

## Introduction

MBTemp is a module of the [Sirius control system](/Machine/control_system) designed to perform measurements from Pt100-based temperature sensors. It is has been completely developed by [Controls Group](/Machine/Groups/CON). This module will be used largely on Sirius Engineering Installation Area to monitor temperature on vacuum chambers, pulsed magnets, access-controlled room and so on. It is intended to have over 8000 points of temperature measurement distributed along accelerators' structure and equipment area.

<br >

## General description

|![](/img/groups/con/mbtemp/MBTemp.jpg)|
|-|
|**Figure 1**: MBTemp - Production Unit.|

Each MBTemp is capable of handling up to 8 Pt100 temperature sensors (2, 3 or 4-wire ones). These sensors are connected to the board through modular connectors (RJ11/4P4C). The analog circuit sources 1 mA to the Pt100 sensor and reads the corresponding voltage drop. After an analog chain for signal conditioning, voltages are sampled by a 16-bit analog-to-digital converter. A PIC microcontroller performs digital integration over the samples of the eight channels, and also handles serial communication (RS-485) at 115200 bps for data sharing.

Application layer protocol for communication to MBTemp boards is [Basic Small Messages Protocol (BSMP)](/Machine/Groups/CON/bsmp.md). Each Pt100 channel is mapped into a [BSMP]((/Machine/Groups/CON/bsmp.md)) variable. BSMP variables 0 to 7 are associated to the sensor connected to modular jack 1 to 8. These variables have 2 bytes of size, and must be interpreted as an unsigned integer of 16 bits (big-endian). The temperature measurement (in Celsius degrees) is given by:

$$
Temperature = \frac{(Byte[1] << 8) + Byte[0]}{100}
$$

For instance, if a [BSMP](/Machine/Groups/CON/bsmp.md) variable has a value of 2500, this corresponds to a temperature of 25.00 °C.

<br >

##  Operation principle 

<br >

###  Pt100 sensors 

Pt100 is a resistance temperature detector (RTD) made of platinum (Pt) having a resistance of 100 ohms at 0 °C. Basically, it is a resistor whose resistance varies according to its temperature. RTDs are more accurate and stable than thermocouples. The platinum detecting wire must be away from contamination to remain stable and there are plenty of packages available. Commercial detectors have  a temperature coefficient of resistance α  0.00385/°C, what leads to naming them as "Pt100 385".

The relation between temperature and resistance is given by the Callendar-Van Dusen equation, for positive temperatures:

$$
R_T = R_0 \left[ 1 + AT + BT^2 \right] \; (0\;{}^{\circ}\mathrm{C} \leq T < 850\;{}^{\circ}\mathrm{C})
$$

Here $R_T$ is the resistance at temperature *T*, $R_0$ is the resistance at 0 °C.

the constants for a Pt100 385 are:

$$
A =  3.9083 \times 10^{-3}~^\circ\text{C}^{-1}
$$
$$
B = -5.775 \times 10^{-7}~^\circ\text{C}^{-2}
$$
