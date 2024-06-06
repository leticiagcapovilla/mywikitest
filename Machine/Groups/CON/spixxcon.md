---
title: SPIxxCON
description: 
published: 1
date: 2024-06-06T15:30:50.576Z
tags: 
editor: markdown
dateCreated: 2024-06-06T15:22:08.848Z
---

# CON: SPIxxCON

<br>

## Introduction
SPIxxCON is a simple standardized bus, based on SPI, developed by the [Controls Group](/Machine/Groups/CON). The idea behind it is to define a default physical communication link between a control hardware interface and a master CPU responsible for dealing with it.

<br>

## SPIxxCON pinout table

Current specification of SPIxxCON consists of 20 pins. High-level voltage of all digital lines is +3.3V.


|Pin| Name| Description |
|-|-|-|
|1| +3.3V| Power supply pin +3.3V - Sources up to 500mADC (pins 1 and 2 together). |
|2| +3.3V| Power supply pin +3.3V - Sources up to 500mADC (pins 1 and 2 together). |
|3| GND| Power supply pin (ground). |
|4| GND| Power supply pin (ground). |
|5| +5V| Power supply pin +5V (pins 5 and 6 together). |
|6| +5V| Power supply pin +5V (pins 5 and 6 together). |
|7| DIO4| General-purpose input/output pin. |
|8| DIO1| General-purpose input/output pin. |
|9| DIO3| General-purpose input/output pin. |
|10| DIO2| General-purpose input/output pin. |
|11| MISO| "Master input, slave output" line of SPI bus. |
|12| MOSI| "Master output, slave input" line of SPI bus. |
|13| INTMISO| Interrupt signal from slave to master. A chip on the interface board can use this to signal it has some data ready to be transferred to the master, for instance. |
|14| INTMOSI| Interrupt signal from master to slave. This can be used to trigger some event, such as a new sample on an analog-to-digital converter. |
|15| CS| "Chip select" line of SPI bus. |
|16| RS| "Register select" line, used when the desired interface board and a specific internal chip from it is selected by the master of the bus. |
|17| GND| Power supply pin (ground). |
|18| CLK| SPI clock signal. |
|19| OUT| General-purpose output only pin. |
|20| GND| Power supply pin (ground).  |

<br>

##  Eurocard connector for SPIxxCON

SPIxxCON signals can also be available in an Eurocard connector for crate purposes. Pinout must be configured as below:


| | A| C |
|-|-|-|
|1| -----| ----- |
|2| -----| ----- |
|3| -----| ----- |
|4| -----| ----- |
|5| -----| ----- |
|6| -----| ----- |
|7| -----| ----- |
|8| -----| ----- |
|9| OUT| GND |
|10| GND| CLK |
|11| RS| CS |
|12| INTMOSI| INTMISO |
|13| MOSI| MISO |
|14| DIO2| DIO3 |
|15| DIO1| DIO4 |
|16| GND| GND |
|17| +3.3V| +3.3V |
|18| -----| ----- |
|19| -----| ----- |
|20| -----| ----- |
|21| -----| ----- |
|22| -----| ----- |
|23| -----| ----- |
|24| -----| ----- |
|25| -----| ----- |
|26| -----| ----- |
|27| -----| ----- |
|28| -----| ----- |
|29| +5V| +5V |
|30| -----| ----- |
|31| GND| GND |
|32| GND| GND  |


<br>

## SPIxxCON addresses

<br>

### Board ID

There are currently three different type of boards compatible with the SPIxxCON bus, one of them being the master (SERIALxxCON) and the others acting as slaves. They are all listed below:

*[SERIALxxCON (master)](/Machine/Groups/CON/serialxxcon)
*[SPIxCONV](/Machine/Groups/CON/spixconv)
*SPIxCONT

For a same type of board, eight different addresses (from 0 to 7) can be chosen.

<br>

### Device ID

Inside of each board there can be up to eight devices (addressed from 0 to 7), with the address number 7 being reserved for the board type identification and the address number 6 reserved for the flash memory, as shown in the following table:

| address| description |
|-|-|
|0| available address |
|1| available address |
|2| available address |
|3| available address |
|4| available address |
|5| available address |
|6| reserved for flash memory |
|7| reserved for board type ID |

<br>

### Board type ID

When device ID number 7 is chosen and a "read" command is requested, a value from 0 to 255 can be returned. Each value is associated with a type of board, as we can see in the next table:

|value| description |
|-|-|
|0x00| --not used-- |
|0x01| reserved |
|0x02| SPIxCONT |
|0x03| reserved |
|0x04| SPIxCONV |
|0x05| available |
|...| ... |
|0xFE| available |
|0xFF| --not used--  |
