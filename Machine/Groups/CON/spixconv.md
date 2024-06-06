# CON: SPIxCONV

<br>

## Introduction

SPIxCONV is a general-purpose board featuring analog and digital interfaces. The analog interface contains one digital-to-analog circuit and one analog-to-digital circuit, both with resolution of 18 bits. The digital interface contains two ports with 8 bits each. The port A is always set as input, and the direction of port B is configured by the user through one position of a DIP switch. This project is currently under development by the [Controls Group (CON)](/Machine/Groups/CON).

<br>

## Devices

*Digital-to-analog converter

`component used: AD5781`

*Analog-to-digital converter

`component used: AD7634`

*Flash memory

`component used: W25Q64FV`

*Digital Ports A and B

`component used: a 74LCX245 for each port`


Each device inside the board has a correspondent address, as shown above:

|Address| Device selected |
|-|-|
|0| DAC |
|1| ADC |
|2| FLASH |
|3| Digital Port A |
|4| Digital Port B |
|5| Decoder |
|6| Decoder Flip-Flop's CLK |
|7| board type ID  |


Device 7 is reserved for board type ID. If this device is chosen and a "read" command is requested, the value 0x04 should be returned, as explained [[CON:SPIxxCON#Board_type_ID|here]](link).

Device 5 actually select another decoder, in order to use eight more functionalities, as described below:

|Decoder addresses| Description |
|-|-|
|0| Turns ON DAC circuit |
|1| Turns OFF DAC circuit |
|2| Turns ON ADC circuit |
|3| Turns OFF ADC circuit |
|4| Presets CLR and RST Flip-Flops |
|5| CLR Flip-Flop (DAC clear command) |
|6| RST Flip-Flop (DAC reset command) |
|7| --unused--  |

<br>

## Communication

The communication with the board is made by using the [[CON:SPIxxCON|SPIxxCON]](link) bus, and it uses the SPI protocol together with some control pins.

*RS pin:
   if RS = 0: enable MOSI and CLK for the devices inside the board.
   if RS = 1: enable MOSI and CLK for address selection.

<br>

## BOM

**--under construction--**

<br>

## Software

**--under development--**


The spixconv API:

* init
    * spixconv.init.baudrate(int)
* selection
    * spixconv.selection.address(int)
    * spixconv.selection.dac(int)
    * spixconv.selection.adc(int)
    * spixconv.selection.flash(int)
    * spixconv.selection.portA(int)
    * spixconv.selection.portB(int)

* dac
    * spixconv.dac.config()
    * spixconv.dac.write(int)
    * spixconv.dac.writeVolts(int)
    * spixconv.dac.read()
    * spixconv.dac.reset(board)
    * spixconv.dac.clear(board)

* adc
    * spixconv.adc.read()
    * spixconv.adc.readVolts()
    * spixconv.adc.mean(int)

* digital
    * spixconv.digital.write()
    * spixconv.digital.read()
    * spixconv.digital.check()

* flash
    * spixconv.flash.???()
