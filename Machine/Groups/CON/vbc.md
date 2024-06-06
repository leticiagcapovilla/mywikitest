# CON: VBC

<br>

## Introduction

[LNLS Controls Group](/Machine/Groups/CON) has designed a simple hardware and software solution for controlling Vacuum Pumping Cart, to be used in Vacuum Group laboratories and Sirius installation. It controls some gates and other equipment belonging to the Vacuum Pumping System in order to make it more agile, using relays and analogs inputs to know the state of the system and to control it. Besides that, the project includes a convertor RS485 to USB that is used to communicate with the vacuum pumps.
The software developed verify the system status and if it is following the requirements that have been proposed, also allowing to control it manually.

<br>

## Hardware description



<br>

### Analog Input

The Analog Input allows the system to read the value of the pressure measured analogically by a voltage divider. It's made up two resistors of 10kΩ and two resistors of 5kΩ, and the input is by a SMA connector. The maximum allowed voltage input value is 20V, otherwise you may damage the input pin used in the BeagleBone black.
The pressure measured is provided by the Granville-Phillips® Series 835 VQM® Differential Pump System.

<br>

### Inputs

There are also five inputs: two of them are designated to the Serial Interface, one of them provides the analogical pressure values, there is another one to check the status of a gate, one is for the system power by a 5V power supply and the other is for a power supply of 24V.

|Port| Input |
|-|-|
|C1| SMA input - analogical pressure values |
|PWR 24V| Power supply 24V input |
|P3| USB-RS485 converter input/output |
|P4| USB-RS485 converter input/output |
|J5| check gate status |
|BBB power supply| 5VDC input  |

<br>

### Power outputs

The four outputs existent are set by the actuation of four relays, which one controlling exactly one output that provides a **24V voltage output**. They are controlled by the activation of four BeagleBone Black pins. The relation between the pins and the ports are described bellow:

|Port| Pin Out VBC v2.1| Pin Out VBC v2.2| Relay |
|-|-|-|-|
|J1| P8_18| P9_12| K1 |
|J2| P9_24| P9_24| K2 |
|J3| P8_18| P8_18| K3 |
|J4| P9_12| P8_18| K4  |

<br>

### Serial Interface

<br>

## Software interface

<br>

### System library

<br>

### IOC

<br>

### Operator interfaces
