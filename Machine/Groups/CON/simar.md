---
title: simar
description: 
published: 1
date: 2024-06-03T15:48:35.930Z
tags: 
editor: markdown
dateCreated: 2024-05-29T15:59:54.692Z
---

# CON: Simar

<br>

## Introduction

The Internet of things Group has developing a general communication board, with the focus of making it a modular system which will serve as a basis for new group projects. The base board of Simar project has been developed with the ability to communicate with others modules though one of its four communication protocol, that are:

* Onewire;
* Inter-Integrated Circuit - I2C;
* Serial Peripheral Interface - SPI;
* Universal Asynchronous receiver-transmitter - UART;

<br>

## Hardware Overview

<br>

##  Base board 

The base board is responsible to work as master on communication's bus, generate the necessaries power voltages to each integrate circuit and  controlling a general bus though the Processing Real Time Unit - PRU. The master controlling chosen was BeagleBone Black and its PRU0 and PRU1 are used to real time data processing.

<br>

###  Board Power Circuits 

|![](/img/groups/con/simar/3_3VLT3080.png)|
|-|
|**Figure 6**: Circuit regulator to 3.3V.|

There are three voltages values available on base board, 5Vdc, 3.3Vdc and 1.8Vdc. The 5V level voltage is obtained by an external power supply, which is then regulated to other voltages. The 1.8V level is provided by BeagleBone Black, using its internal voltage converter and 3.3V is generate using the integrated circuit [LT3080](https://www.analog.com/media/en/technical-documentation/data-sheets/3080fc.pdf){target=_blank}. 

The LT3080 is a linear adjustable voltage regulator, where its output is defined by configuration resistors, according to the equation below. To converter operates with efficiently and reliably, a minimum output current is required, that must to be higher than 0,5 mA and it is performed putting a LED on circuit output. The circuit is showed on figure 01.

`Vout = Rset . 10uA`

<br>

###  Bus and Communication Circuits 

All protocols communication are disposable in a db9 connector, see figure 02. Two of them are directly connected to the BeagleBone pins, the One Wire and Uart protocols, according to the table below:

|Protocol| Data traffic lines| BBB pins| BUS pins |
|-|-|-|-|
|UART0| Tx0| P4 - Cosole BBB| P14 |
|UART0| Rx0| P5 - Cosole BBB| P16 |
|UART4| Rx4| P9.11| P7 |
|UART4| Tx4| P9.13| P9 |
|One Wire| 1-wire| P9.12| P4  |


The serial SPI communication is, before the bus, burrefed by a 74HC245 buffer circuit in order to isolated the primary board from the other boards and, in addition, the integrated circuit changes the digital voltage level, from 3.3V to 5V.

Furthermore, the bus possibilities data traffic of up to four dispositives though the I2C protocol, using for it a dual 4-channel analog demultiplexer, the HEF4052 B circuit, which switches SDA and SCLK signs between the secundary boards. So, for the I2C communication, the base board needs send two more data signals, addr 0 and addr 1, to select the demultiplexer channel.

The BeagleBone pins used to SPI and I2C communication are described below:


|Protocol| Data traffic lines| BBB pins| BUS pins |
|-|-|-|-|
|I2C| ADDR 0| P9.15| --- |
|I2C| ADDR 1| P9.16| --- |
|I2C| SDA| P9.20| --- |
|I2C| SCLK| P9.22| --- |
|SPI 0| DS| P9.14| P3 |
|SPI 0| CS| P9.17| P10 |
|SPI 0| MOSI| P9.18| P8 |
|SPI 0| MISO| P9.21| P6 |
|SPI 0| CLK| P9.22| P12 0 |

After the Demultiplexer switches the I2C signals, eigth outputs are available on communication bus, four SDA pins and others four SCLK pins, described in the following table, as well as, the values associated to "addr 0" and "addr 1".

  
|Addressing| Data traffic lines| BUS pins |
|-|-|-|-|
|00| SCL 0| P17 |
|00| SDA 0| P18 |
|01| SCLK 1| P19 |
|01| SDA 1| P20 |
|10| SCLK 2| P21 |
|10| SDA 2| P22 |
|11| SCLK 3| P23 |
|11| SDA 3| P24  |

<br>

####  Chip Select enable 

A simple circuit was developed in order to disable the CS singnal during a rise edge of "DS" signal. So, the "chip select" is just enable if the "DS" is set to HIGH. The final circuit is show below, where the CS of BUS following the boolean equation: 

`CS_SPI = CS_BBB + ¬DS`

<br>

###  PRU BUS 

Beyond the communication bus, there are on base board a PRU BUS, where are available the pins of two Programeble Real-Time Unit, PRU 0 and PRU 1.
Both are buffered by a 74HC245, whitch have theirs outputs enables after the the complete boot of BeagleBone, and its functions are isolate the prymary board from others boards and change the voltage values of signals, once that PRU pins of BeagleBone work junt on 3.3V.

The outputs pins of PRU 1 are still connected on a 74LS06 circuit integrated, six inverters buffers with open-collector outputs, and its inputs pins, have theirs voltages divided by a resistors divider, before are also connected on buffer 74HC245.

The pins of the PRU Bus are described on table below:

|Pin| Function| Configuration |
|-|-|-|
|1, 2, 13, 14| Voltage Output| +3.3 Vdc |
|3, 4, 15, 16| Voltage Output| +5 Vdc |
|5, 7, 9, 11| Step motor| Output |
|6| Generic Input| Input |
|8| Generic Output| Output |
|10, 12, 18, 20, 22, 24| Voltage Output| GND |
|17, 21, 25| Bico| Output |
|19| Trigger pulses| Input |
|23| RPM pulses| Input |
|26| Bomba| Output  |

<br>

##  Digital/Analog board 

The first shield board of SIMAR is a general in/out digital data and read analogical data. It is divided on six blocks: board enable, module selector, read digital data, write digital data, memory and read analogical values.

First of all, a SIPO register 74HC595 is used to receive one byte of data by spi protocol, that will determined which module will be enable. four bit from data received are connected on XOR logic gates (74HC86), that has the aim to determinate the parity of them ("0" if even, "1" furthermore).

The Board enable block is compound by a magnitude comparator (74LS688) and a dip switch of five positions. It will compared the four bits on dip switch and the output of XORs gates (mod_0 ⊕ mod_1 ⊕ mod_2 ⊕ mod_3) with the addressing and the bit parity, sent by spi.

<br>

###  Protocol 

In order to write or read any value on the board, it is necessary to send at least two bytes. As the board has three modules for selection, the first data byte must choose one of them, after, the others bytes can be sent according the selected module. 

To send the first byte, it's ***necessary*** set the pin "P9_14" to low, and generate a rising edge on it after all the data has been sent, now setting  it high. Once a module is selected, it is not necessary to do it again, if more then one byte is read or written.

Two initial settings must be made, related with spi, the *mode* set to three and the most significant bit sent first. This setting are showed below:

```
from Adafruit_BBIO.SPI import SPI
```

```
# /dev/spidev0.0
spi = SPI(0, 0)
spi.mode = 3             # CPHA = 1 ; CPOL = 1
spi.lsbfirst = false  
```

```
spi.bpw = 8
spi.msh = 10000000       # [[Testar qual a máxima taxa]]
```


> Note: In all examples, the parity is only related to the board's address.
{.is-info}

<br>

####  Select modules

[w: 1 byte]

To select the interested module, its necessary send 1 byte of data serially. The sent data sequence must be:

1) Set the BeagleBone Black pin "P9_14" to low;
2) Send one byte data by spi;
3) Set the BeagleBone Black pin "P9_14" to high.

The data byte is divided on: 

`(MSB)(1 bit: Even Parity) (4 bits: Board Addressing) (3 bits: Module Addressing)(LSB)`

The table below shows the addresses to each module present on board:

|Address| Modules Addressing |
|-|-|
|000| Enable the EEPROM memory |
|001| Enable SIPO register for writing digital data |
|010| Load digital data on PISO register |
|011| Enable PISO register for reading digital data |
|100| Configure the potentiometer counter |
|101| Enable digital potentiometer  |


**E.g.:**

```
import time
import Adafruit_BBIO.SPI as SPI
import Adafruit_BBIO.GPIO as GPIO
```

```
DS = "P9_14"
```

```
#---------- Set Pinouts ----------
GPIO.setup(DS, GPIO.OUT) #Set DS
GPIO.output(DS, GPIO.LOW)
#---------------------------------
```

```
#------------ Set SPI ------------
spi = SPI.SPI(0, 0) # set which SPI will be used
spi.bpw = 8
spi.lsbfirst = False
spi.mode = 3
spi.msh = 10000000
#---------------------------------
```

```
#-------- Select Module ----------
GPIO.output(DS, GPIO.LOW)
message = [41]             #(0)(0101) (001)
spi.writebytes([message])
time.sleep(1)
GPIO.output(DS, GPIO.HIGH)
#---------------------------------
```

In this example, it's selected the SIPO register.

<br>

####  Read digital data 

[w: 2 bytes (1 + 1)] [r: 1 byte]

To read the values of the digital data, it is necessary to first load the read register, after, enable the read register and then, read one byte data by **mode 3** serial spi. It isn't necessary to select the register again, or load it, if you want read the same value, just read the data by spi.

Then, the sequence to read the digital data will be:

1. Send: ***(MSB)[1 bit: Even Parity] [4 bits: Board Addressing] [ 0 1 0 ](LSB)*** (Load read register)

2. Send: ***(MSB)[1 bit: Even Parity] [4 bits: Board Addressing] [ 0 1 1 ](LSB)*** (Enable register)

3. Read one byte through spi.

<br>

####  Write digital data 

[w: n bytes (1 + (1+1+...+1))] [r: none]

To write on digital bus, first select the SIPO register and, then, send one byte of data. It's not necessary to select again the module if you want write others data bytes on bus.

The sequence will be:

1) Send: ***(MSB)[1 bit: Even Parity] [4 bits: Board Addressing] [ 0 0 1 ](LSB)*** (Enable register)

2) Send: ***[8 bits: digital data]*** (Writes data)
3) Send: ***[8 bits: digital data]*** (Writes data)
4) Send: ***[8 bits: digital data]*** (Writes data)
...

####  Read/Write memory 


####  Set potentiometer 

[w: 2 bytes (1 + 1)] [r: None]

The digital potentiometer has its resistance value changed using the spi clock sign and the chip used was the X9C104S, of 100k. 
Always, on board start up, the U/¬D pin will set to LOW and any clock pulse, will decrease its value.

To changes the U/¬D value, first select the address 0x05 and then, generate a rising edge on CS pin. After U/¬D is right, select the potentiometer CS pin and send a word via spi to generate eigh pulses on clock pin of potentiometer (Here, the minimum adjustment on potentiometer is provided by 8 pulses).

Then, the sequence to set the potentiometer value is:

1) Send: ***(MSB)[1 bit: Even Parity] [4 bits: Board Addressing] [ 1 0 1 ](LSB)*** (Change U/¬D value, if necessary)
2) Generate a rising edge on CS pin; 

3) Send: ***(MSB)[1 bit: Even Parity] [4 bits: Board Addressing] [ 1 0 0 ](LSB)*** (Enable potentiometer)

4) Send: ***[8 bits: digital data]*** (Move potentiometer wiper through 8 positions)
5) Send: ***[8 bits: digital data]*** (Move potentiometer wiper through 8 positions)
6) Send: ***[8 bits: digital data]*** (Move potentiometer wiper through 8 positions)
...


##  SPI Interface Board 

The second SIMAR shielding board is an SPI communication extender, which aims to enable communication with up to six different devices. The choice of the device is made by the switching of Chip Select sign among them. Furthermore, an EEPROM memory are available to storage generals data from the Base Board.

All input signals are connected to the board through two db9 connector (except +3.3Vdc), which are connected in parallel to each other, making it possible to connect more than one board to the serial bus (SPI interface or other). The db9 pins are shown below.

|Pin| Function| Configuration |
|-|-|-|
|1| Voltage Input| +3.3 Vdc (generated at board) |
|2| Voltage Input| +5 Vdc |
|3| SPI| DS |
|4| SPI| MISO |
|5| SPI| CLOCK |
|6| SPI| MOSI |
|7| NC| --- |
|8| SPI| CS |
|9| Voltage Input| GND  |

Each board output is composed of a 01x06 connector and each of its pins has their signals obtained from a resistive voltage divider, making it possible the connection of the SPI board with devices powered with +5Vdc or +3.3Vdc.


The SPI Interface Board also has an addressing block, composed of a magnitude comparator (74LS688) and xor logic gates (74HC86) to specify the parity of data received from the base board. In addition to the parity bit, the 74LS138 also compares an addressing nibble, which is defined by a dip switch.

.

.

.

.

###  Protocol 

All board functions are set sending one byte serially though SPI communication. This byte are responsible to enable the SPI board and select what output of decoder will be reset.

The data byte is divided on: 

`***(MSB)(1 bit: Even Parity) (4 bits: Board Addressing) (3 bits: Chooses Chip Select)(LSB)***`

The table below shows which "CS" is enabled according to the data received:


|Data received| CS enabled |
|-|-|
|000| EEPROM memory |
|001| CS Output 01 |
|010| CS Output 02 |
|011| CS Output 03 |
|100| CS Output 04 |
|101| CS Output 05 |
|110| CS Output 06 |
|111| CS Output 07  |


##  SPIxxSWI 

###  Protocol 

## Software Overview

##  Protocol 
