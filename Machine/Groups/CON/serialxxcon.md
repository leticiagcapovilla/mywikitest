---
title: SERIALxxCON
description: 
published: 1
date: 2024-06-03T15:57:43.611Z
tags: 
editor: markdown
dateCreated: 2024-05-29T15:36:02.089Z
---

# CON: SERIALxxCON

|![](/img/groups/con/serialxxcon/Serialxxcon.jpg)|
|-|
|**Figure 1**: SERIALxxCON.|

<br>

## Introduction

SERIALxxCON is a general-purpose board based on Beaglebone Black, designed for Sirius Controls System, in order to control and monitor several equipments such as power supplies, interface boards, vacuum and temperature monitors, etc.
This board consists on three functionalities: RS-232/RS-485 communication, interface for Timing System and [CON:SPIxxCON|SPIxxCON](link) master module.

<br>

##  Hardware Overview

|![](/img/groups/con/serialxxcon/SERIALxxCON.png)|
|-|
|**Figure 2**: Hardware overview.|

SERIALxxCON is a baseboard for Beaglebone Black, designed as a multi-serial platform and a dedicated SPI master. In addition, it has been conceived with two timing inputs (optical and electrical) for synchronized operations.

There are two red switches on the panel, which configures the serial communication to one of the following modes: **high-speed RS-485** (via PRU: PRUserial485 project), **default RS-485** (FTDI) or **default RS-232** (FTDI). Note: there is no high-speed RS-232 (PRU).

Another two red switches are available and they are needed when configuring a RS-485 communication network, allowing the user to enable/disable termination and fail-safe resistors.

<br>

###  Powering the board 

In order to power the board and have it completely functional, connect the front jack with a reliable +5V/2A power source (positive center). Controls Group recommends CUI Inc. power supply brand.

Typical power consumption: **XXXXX W**

<br>

###  Versions 

* **v2.3: latest (nov/2017)**
* v2.2: production prototype (early 2017)

<br>

###  Production units 

550 units were manufactured in 2018 (v2.3) and some units are already installed and configured on Controls System Network. They are identified by an ID tag on the right on the front panel.

<br>

###  More technical documentation 

Detailed documents can be found at project repository at CNPEM gitlab ([click here](http://gitlab.cnpem.br/patricia.nallin/serialxxcon){target=_blank}, you must be connected through CNPEM network).

<br>

##  Hardware Details 

|![](/img/groups/con/serialxxcon/Front-serialxxcon.png =500x)|
|-|
|**Figure 3**: Hardware overview.|


|![](/img/groups/con/serialxxcon/Back-serialxxcon.png =500x)|
|-|
|**Figure 4**: Hardware overview.|

<br>

###  Hardware Reset 

It is a "hardware watchdog" for Beaglebone Black. It may be activated or not, depending on the switch on the board. Based on a multi-trigger pulse-width timer, it prevents BBB hardware from being locked after a reboot or a system crash. Once it reaches the timeout, typically 30 seconds, it means that the BBB is locked so a reset pulse is delivered to an specific GPIO.

<br>

###  Multi-purpose LED 

There is a red LED on the board, which can be also seen at the front panel. It is a multi-purpose one, user may use it for any application. Controls Group usually uses it as a heart beat for the system.

<br>

###  PRU-based UART 

There is a dedicated UART interface in SERIALxxCON board. Based on Maxim MAX3107 integrated circuit, this interface has been designed to reach high performance (high baudrate and repetibility, low jitter and latency) concomitantly to the operational system. The 128-byte external UART FIFO is controlled through SPI from one of the [Programmable Real-Time Units](https://processors.wiki.ti.com/index.php/PRU-ICSS){target=_blank}, embedded on Sitara SoC.


|![](/img/groups/con/serialxxcon/Hardware-PRUserial485.jpg =650x)|
|-|
|**Figure 5**: |

It has a wide baudrate range, it is configurable. Standard values are already available as well as 6, 10 and 12 Mbps. Also, it may operate synchonously to input timing signals.

There is a C library and a Python module (built via cython) available to interface with it. For more details about it, see [PRUserial485](/Machine/Groups/CON/pruserial485) project page. This interface is not mapped in any system device (/dev/tty*), making it mandatory to use the pre-developed software module.

<br>

###  FTDI UART 

An UART based on the well-known FTDI driver is available at the board. FTDI chip is connected to Beaglebone Black through an USB-uUSB cable and the device will be available at /dev/ttyUSB0, usually.

FTDI output signals may be connected to two different level converters: either RS-232 or RS-485. This is user-selectable via selection switches on the front panel.

Baudrates to be configured are the standard available at Debian system, reaching up to 3 Mbps.

###  Isolated RS-485 driver 

In order to increase reliability and avoid external interference into board power signals, it has been decided to electrically isolate RS-485 serial communication lines. A regulated 1W DCDC converter is powering the RS-485 driver, as well as its fail-safe resistors.

<br>

###  Selection switches 

|![](/img/groups/con/serialxxcon/Serialxxcon-switch-diagram.png =450x)|
|-|
|**Figure 6**: |

As shown above, there are two different switches that controls serial communication flow. They are located at the front panel and must be configured before communicating. One is dedicated to selection of communication physical layer (RS-232 or RS-485) and the other one selects whether FTDI or PRU interface will be connected to the serial line. They are also mapped on two BBB GPIOs, making it possible to know in which position they are.

<br>

###  Hardware address and Board ID 

It is a 5-position dip switch, making it possible to address from 0 to 31. For the moment, it is not used for any application and is pre-configured to address 21, due to self-tests during board manufacturing.

Board ID is a unique identification for SERIALxxCON unit and there is no link with hardware address switches.

<br>

###  SPIxxCON interface 

[CON:SPIxxCON|SPIxxCON](link) is a SPI interface with some extra signals designed by Controls Group. SERIALxxCON board has its connector as well as an Eurocard footprint, if needed to be extended to a crate-compatible system.

The main purpose for this module, currently, is to interface [CON:SPIxCONV|SPIxCONV](link) boards, which is a multi input/output analog/digital platform.

<br>

###  Timing Receivers 

Two timing inputs are available in SERIALxxCON hardware, an electrical (TTL input, 50Ω-matched) SMA input and an optical link receiver (660 nm red - HFBR-2521Z). Their output are in parallel, being tied to a Beaglebone Black input pin.

The purpose of those inputs is to send serial packages synchronously, available **only** through [PRUserial485](/Machine/Groups/CON/pruserial485) library.

<br>

##  Serial Communication 

It has two serial modules: a specific RS-485 hardware interface for [PRUserial485](/Machine/Groups/CON/pruserial485), which can achieve high baud rates, and a USB/UART bridge (FTDI FT232RL), for communicating at slower baud rates with either RS-232 or RS-485.

<br>

###  RS-232 

Based on FTDI interface.
Connector on board: DB-9 male

All RS-232 signals (CD, RX, TX, DTR, GND, DSR, RTS, CTS and RI) are available.

***Configuring the board to this mode:*** set red switches to FTDI and RS232.

<br>

###  RS-485 

* **Connector, cable and pinout**
A 6P6C (RJ-12/RJ-25) has been chosen for Controls system as well as its pinout, as shown below. Every controlled equipment must use (or be adapted to) this standard.

|![](/img/groups/con/serialxxcon/6P6C_ConnectorPinout_RS485.png)|
|-|
|**Figure 7**: |

It is recommended to use a 6-position modular cable. It has been largely tested under several conditions.
* 6 Mbps: a 10-meter cable is assured to work in a noisy environment.
* 115200 bps: 150-meter cables have been in use, with no communication problems.

Suggested cable is [AlphaWire 1606](http://www.alphawire.com/Products/Cable/Alpha-Essentials/Communication-and-Control-Cable/1606){target=_blank}.


* **Termination**
Termination is needed in order to match serial transmission line. RS-485 impedance is 120Ω.

: *** Master ***
: When used to control a RS-485 network (Master mode), SERIALxxCON must be the first physical device and **termination and fail-safe must be enabled**. This can be done by toggling the red switches in the front panel.
 
: *** Slave ***
: The last physical device of a RS-485 network must connect the differential data lines V+ and V- with a 120Ω resistor.

<br>

###  Overview 

Serial communication - Hardware configuration ("Mode" Panel Switches)

|SW Left| SW Right| Mode |
|-|-|-|
|⬇| ⬇| RS-232 (FTDI) |
|⬇| ⬆️| Not Available * |
|⬆️| ⬇| RS-485 (FTDI) |
|⬆️| ⬆️| RS-485 (High-performance PRU) |


** Although this configuration is not available for serial communication, it can be used to perform any action on the system. For example, Controls Group has used this configuration to force a DHCP address for Beaglebone Black.*
