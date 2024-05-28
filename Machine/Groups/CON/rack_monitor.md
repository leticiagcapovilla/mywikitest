---
title: Rack Monitoring Platform
description: 
published: 1
date: 2024-05-28T21:16:44.610Z
tags: 
editor: markdown
dateCreated: 2024-05-28T21:15:58.763Z
---

# CON: Rack Monitoring Platform

## Introduction

|![](/img/groups/con/rack_monitor/Prototipe_v0-4.png)|
|-|
|**Figure 6**: Hardware prototype version v0.4.|

This is a hardware and software solution for Sirius cabinets monitoring designed by [[CON:CON|LNLS Controls Group (CON)]]. It's based on [[CON:SPIxxCON|SPIxxCON]](link), a Serial Peripheral Interface Protocol (SPI) bus present on [[CON:SERIALxxCON|the main node for Sirius Controls System]] and NXP's microcontroller: FRDM-KL25Z. Since version v1.6 the microcontroller was changed to LPC1768.

The designed board can provide values for temperature, humidity, outlet supply voltage, fan electric current consumption and door status inside Sirius Control System cabinet.

The platform's Software includes:
* a Python3 module to read values from the board
* Graphical User Interface (GUI) with current values
* EPICS - Archiving Interface

The project's files can be found in [Rack Monitoring Platform's GitLab repository](https://gitlab.cnpem.br/vitor.santos/racks)(available only through CNPEM's network) or in [RackMon GitHub/lnls-sirius repository](https://github.com/lnls-sirius/rack-mon).

## Hardware

The baseboard works as a shield for NXP's development platform and is connected to [[CON:SERIALxxCON|SERIALxxCON]] through a RJ25(6P6C) connector and cable, which contains the 4 necessary SPI buses and 2 extra buses that power the cabinet monitoring platform. The most recent version also includes a adapter for LPC1768 pinout.

The microcontroller works as a Slave in the SPI communication and uses the peripherals present on the baseboard to read [[CON:Rack_Monitoring_Platform#Temperature_sensor_-_LM35|temperature]](link), [[CON:Rack_Monitoring_Platform#Temperature_and_humidity_sensor_-_DHT11|humidity]](link), [[CON:Rack_Monitoring_Platform#Voltage_Transformer|voltage]](link), [[CON:Rack_Monitoring_Platform#Electric_current_sensor_-_CST1010|electric current]](link) and [[CON:Rack_Monitoring_Platform#Magnetic_sensor_-_SM1001|magnetic]](link) sensors, so it can then provide the acquired data in [ASCII](https://en.wikipedia.org/wiki/ASCII) string format to the Master of the Serial communication (SERIALxxCON).

### 6P6C Connector

Even though the platform box contains a power plug and a voltage transformer, they are not used to provide energy to the baseboard. To power up the platform and enable it's [[CON:Rack_Monitoring_Platform#SPI_Protocol|serial communication]] with SERIALxxCON hardware, a Printed Circuit Board(PCB) adapter connects RJ25 plug to [[CON:SPIxxCON|SPIxxCON]](link) necessary signals:

|![](/img/groups/con/rack_monitor/SPIxxCON-RJ25_adapter.jpeg)|
|-|
|**Figure 6**: SPIxxCON to 6P6C adapter.|

* +5V
* GND
* MOSI
* MISO
* CLK
* CS

The board does not consume a big amount of energy, so the first 2 power buses are enough to power the microcontroller and the peripherals, including all the sensors.

### Sensors

The current version is able to process data from the following sensors:
* [[CON:Rack_Monitoring_Platform#Temperature_sensor_-_LM35|LM35]](link) temperature sensor
* [[CON:Rack_Monitoring_Platform#Temperature_and_humidity_sensor_-_DHT11|DHT11]](link) humidity and temperature sensor
* [[CON:Rack_Monitoring_Platform#Voltage_Transformer|Voltage transformer]](link)
* [[CON:Rack_Monitoring_Platform#Electric_current_sensor_-_CST1010|CST1010]](link) electric current transformer
* [[CON:Rack_Monitoring_Platform#Magnetic_sensor_-_SM1001|SM1001]](link) magnetic sensor

Both LM35 and DHT11 sensors are connected to the board by RJ11(4P4C) connectors.

#### Temperature sensor - LM35

|![](/img/groups/con/rack_monitor/LM35_circuit.jpeg)|
|-|
|**Figure 6**: LM35 circuit.|

LM35 is a low-cost, yet very accurate, temperature sensor that provides a 10mV variation for every degree. It is soldered to a 1-meter serial cable that is connected to the board by one of the 4P4C connectors.

These small variations are amplified by one of the four operational amplifiers on LM324, working as a [non-inverting amplifier](https://en.wikipedia.org/wiki/Operational_amplifier#Non-inverting_amplifier) with an approximate 3x voltage gain, enabling getting final temperature values from 0°C up to approximately 82°C.

#### Temperature and humidity sensor - DHT11

|![](/img/groups/con/rack_monitor/DHT11_circuit.jpeg)|
|-|
|**Figure 6**: DHT11 circuit.|

DHT11 is a very popular low-cost digital humidity sensor designed by Aosong Electronics, widely used in Arduino projects, even though it's not as precise as other sensors it is very good for qualitative applications. It communicates with the microcontroller through a Single-Wire half duplex serial protocol, using requests from the microcontroller and responses from the sensor. It's circuit only needs a 5kΩ Pull-Up external resistor, and since it's used to provide humidity and temperature values near the platform box, it is soldered to a 10-centimeter serial cable which is also connected to the board by a 4P4C connector.

It is capable of providing humidity values from 20% to 90% with a 5% accuracy and temperature values from 0°C to 50°C with a 2°C accuracy.

#### Voltage Transformer

[[File:Voltage_circuit.jpeg|thumb|left|]]

|![](/img/groups/con/rack_monitor/Voltage_circuit.jpeg)|
|-|
|**Figure 6**: Voltage Transformer circuit.|


Using a commercial voltage transformer the board is capable of estimating with 2% accuracy voltage values from 80V to 250V.

The box is connected to the cabinets power outlet using a simple AC power cord that energizes the 220:9V transformer. The reduced electric voltage is rectified by a simple diode bridge, stabilized with a 100μF electrolytic capacitor and finally reduced again by a voltage divider.


#### Electric current sensor - CST1010

##### Stage 1 - Precision rectifier

|![](/img/groups/con/rack_monitor/CST1010-Stage1_circuit.jpeg)|
|-|
|**Figure 6**: Stage 1 - Precision rectifier.|

CST1010 is a reliable electric current sense transformer fabricated by Triad Magnetics with a turns ratio of 1000:1 mA. Since KL25Z is not capable of detecting electric current variations, in the first stage of the circuit the alternate electric current that comes out of the transformer is used to make a voltage source using two 1kΩ in parallel.The voltage is then rectified by a [precision rectifier](https://en.wikipedia.org/wiki/Precision_rectifier) with a voltage gain of 10x (since the average fan electric current is lesser than 0,5A), made with another one of the operational amplifiers present on LM324.

##### Stage 2 - Analog to Digital Converter

|![](/img/groups/con/rack_monitor/CST1010-Stage2_circuit.jpeg)|
|-|
|**Figure 6**: Stage 2 - Analog to Digital Converter (ADC).|

|PTD6| PTD7| Status |
|-|-|-|
|0| 0| Off |
|0| 1| On |
|1| 0| Error |
|1| 1| Overload  |


When being used to monitor Controls Group cabinets, the baseboard also provides ternary information about the fan status: On, Off or Overload. The last one informing if the fan is consuming more electric current than the usual, which can result in long term problems.

These values are created by analyzing two digital inputs , which are generated by the remaining two modules of LM324 Operational Amplifiers working as an [ADC](https://en.wikipedia.org/wiki/Analog-to-digital_converter).

#### Magnetic sensor - SM1001

[[File:Switch_mounting.jpeg|thumb|200px|left|Magnetic sensor mounting]]

|![](/img/groups/con/rack_monitor/CST1010-Stage2_circuit.jpeg)|
|-|
|**Figure 6**: Stage 2 - Analog to Digital Converter (ADC).|

[[File:Sm1000.jpg|thumb|200px|right|SM1001 sensor and SM1000 magnet]]

|![](/img/groups/con/rack_monitor/CST1010-Stage2_circuit.jpeg)|
|-|
|**Figure 6**: Stage 2 - Analog to Digital Converter (ADC).|


SM1001 is a small magnetic sensor with one normally open electrical contact manufactured by Metaltex, even though it's not as cheap as mechanical switches it's also not as easy to break or to be damaged.

There is no circuit to process it's information in the baseboard, it is simply connected by a Push-in external connector. A simple aluminum board was designed to attach the sensor close enough to the door with Parker Screws.

Metaltex also manufactures proper magnets for this sensor (SM1000 magnets), instead of using them, a simple circular neodymium magnet was chosen due to it's versatility.

### KL25Z

Pinout in versions up to v0.5

|Bus Name| GPIO| Description |
|-|-|-|
|MOSI| PTC7| Master Output Slave Input |
|MISO| PTC6| Master Input Slave Output |
|CLK| PTC5| Clock |
|CS| PTC4| Slave Select |
|Interruption| PTD4| Interruption associated to CS  |

|Bus Name| GPIO| Description |
|-|-|-|
|LM35| PTB0| Amplified voltage correspondent to LM35 temperature |
|Voltage Transformer| PTC2| Reduced, rectified and stabilized voltage from voltage transformer |
|Fan Current| PTC1| Amplified, rectified and stabilized voltage from CST1010 electric current sensor |
|GPAIn| PTB2| General Purpose Analog Input  |

|Bus Name| GPIO| Description |
|-|-|-|
|Front Door| PTD5| Front door status |
|Back Door| PTD0| Back door status |
|Max Current| PTD6| Fan status overload bus |
|Min Current| PTD7| Fan status minimum electric current |
|DHT| PTB3| DHT11 or DHT22 communication bus |
|GPDIn| PTD2| General Purpose Digital Input  |

|Bus Name| GPIO| Description |
|-|-|-|
|RControl| PTB8| WatchDog feed (or reset) control  |

### LPC1768

Pinout in version v1.6

|Bus Name| GPIO| Description |
|-|-|-|
|MOSI| p11| Master Output Slave Input |
|MISO| p12| Master Input Slave Output |
|CLK| p13| Clock |
|CS| p14| Slave Select  |

|Bus Name| GPIO| Description |
|-|-|-|
|LM35| p15| Amplified voltage correspondent to LM35 temperature |
|Voltage Transformer| p20| Reduced, rectified and stabilized voltage from voltage transformer |
|Fan Current| p19| Amplified, rectified and stabilized voltage from CST1010 electric current sensor |
|GPAIn| p18| General Purpose Analog Input  |


|Bus Name| GPIO| Description |
|-|-|-|
|Front Door| p8| Front door status |
|Back Door| p7| Back door status |
|Max Current| p5| Fan status overload bus |
|Min Current| p6| Fan status minimum electric current |
|DHT| p26| DHT11 or DHT22 communication bus |
|GPDIn| p9| General Purpose Digital Input  |


|Bus Name| GPIO| Description |
|-|-|-|
|RControl| p30| WatchDog feed (or reset) control  |


### WatchDog Timer

|![](/img/groups/con/rack_monitor/WDOG_ciruit.jpeg)|
|-|
|**Figure 6**: WatchDog Timer circuit.|

Hardware prototype v0.6 (02/2020), is the first one with a WatchDog Timer implemented via hardware.

This circuit was based on 74HC123 integrated circuit, which is a dual retriggerable monostable multivibrator. When KL25z or LPC1768 is working properly, a digital output feeds the watchdog circuit with a square wave. If the microcontroller stops feeding the dog, the output goes to logic zero resetting NXP's development platform.

## Software
This platform's software consists of: KL25Z's firmware (written in C), a Python3 SPI module for BeagleBone Black (BBB), a SPI-Master/TCP-IP server (written in Python3), an EPICS Input/Output Controller (IOC) which is also a TCP-IP client and a Graphical Users Interface.

The following chart illustrates the data flow along the project: every sensor is read by KL25Z, which is a slave to a [[CON:Rack_Monitoring_Platform#SPI_Protocol|SPI communication]] and answers to a BBB in a SERIALxxCON node the information it requests. The BBB can them finally send the information to a TCP-IP client through sockets.

|![](/img/groups/con/rack_monitor/Data_flowchart.png)|
|-|
|**Figure 6**: Data flowchart.|


### SPI Protocol
[Serial Peripheral Interface or SPI](https://en.wikipedia.org/wiki/Serial_Peripheral_Interface) is, in few words, a full-duplex synchronous serial communication protocol used for short-distance communication. It uses a Master-Slave structure and needs 4 wires to communicate: Master Output Slave Input (MOSI), Master Input Slave Output (MISO), Clock (CLK) and Slave Select (CS).

In this monitoring platform a SPI protocol is used to send the information from KL25Z (working as Slave) to the BBB (working as Master) in a request-response system, with 1 byte requests from the Master and 10 bytes responses from the Slave, each byte sent one activation of CS at a time. These bytes are [ASCII coded characters](https://en.wikipedia.org/wiki/ASCII).

|Character| ASCII correspondent (Hexadecimal)| Request |
|-|-|-|
|C| 43| Fan electric current consumption |
|T| 54| DHT11 or DHT22 temperature |
|b| 62| Back door status |
|c| 63| Fan status |
|f| 66| Front door status |
|t| 74| LM35 temperature |
|u| 75| Humidity |
|v| 76| Outlet voltage  |


Every information flowing through this protocol is treated as a string and no parity bit or byte is implemented. Instead, BBB uses a filter function that verifies if the measurement unit is correct for the requested information. For example, if the request is the character 't' for LM35 temperature, it expects to get "oC"  in the end of the string that was answered.

### KL25Z Firmware

The firmware for KL25Z was developed through [MBED's platform and operating system](https://os.mbed.com/platforms/KL25Z/) in C programming language and is Interrupt based. It has 3 modes of operation: [[CON:Rack_Monitoring_Platform#Read_Mode|Read Mode]](link) (or idle mode), [[CON:Rack_Monitoring_Platform#Buffer_Copy|Buffer Copy]](link) and [[CON:Rack_Monitoring_Platform#Response_Mode|Response Mode]](link). It switches through these modes when an interruption happens on pin PTD4, which is electrically connected to the SPI CS bus (PTC4), in other words, it switches from mode to mode every time the Master reads or writes in the SPI protocol.

|![](/img/groups/con/rack_monitor/CS_interruption_diagram.png)|
|-|
|**Figure 6**:|

When the program starts the [[CON:Rack_Monitoring_Platform#DHT_library|DHT sensor is read and a timer is initiated]](link), the mode variables are also defined. The mode variables are used to control whether the program makes an operation inside any interruption.

|![](/img/groups/con/rack_monitor/Slave_SW_flowchart.png)|
|-|
|**Figure 6**: Firmware modes of operation and mode control variables.|

#### Read Mode

This is the main thread of the program, an unconditional loop where no arithmetic operation happens. The only thing the microprocessors does is feed the hardware watchdog by constantly switching the Digital Output RControl.

The program exits this mode when a rise interruption happens, it stores the request set by the SPI master and enters Buffer Copy.

#### Buffer Copy

This mode of operation is a switch-case conditional inside the main thread of the program. It compares the request stored previously in Read Mode with [[|CON:Rack_Monitoring_Platform#SPI_Protocol|the known SPI requests]], case it is a valid request it reads the sensor to which the information was requested, formats this data as a string, copies the string characters to a 10-byte integer response buffer and finally enters Response Mode.

Case the request stored is not a valid request it switches back to Read Mode.

#### Response Mode

Inside the rise interruption function is where this mode of operation works. It sends each byte from the response buffer via SPI one interruption at a time. By construction the first byte sent is 0x00 and the last byte of the buffer is lost, so the information should only contain 8 bytes (or 8 characters).

After the whole information is sent it returns to idle mode and awaits a next request.

#### DHT library

A public library was used to read Aosong's sensor but it needs a 5 second gap between requisitions. To prevent any troubles, a timer is used to block the sensor to be read case the 5 seconds did not pass.


### LPC1768 Firmware

The newest version of RackMon uses LPC1768 microcontroller in instead of KL25Z. This microcontroller was also programmed in C language using MBed development interface, but it operates with no parallel threads. WatchDog feeding, SPI command receiving, buffer copy and SPI response are all done through the main loop.

### SPI-Master/TCP-IP server

The Python3 program running in a BBB to communicate with the baseboard and provide all the information necessary via TCP/IP server to the network. It runs an object with two simultaneous threads:

* the first one, the SPI Master, sends requests and reads every information from the baseboard (voltage, temperature, humidity,etc...), filters the data by verifying if the last character is the correct measurement unit for the requested information and stores this strings in global variables.

* the second one, the TCP/IP server, opens one connection to port 5006, where the connected devices can request the information by using the [[CON:Rack_Monitoring_Platform#BSMP_Entities|BSMP entities specified further in this project]]. Currently this connection is used by [[CON:Sirius_control_system_servers|the Sirius control system servers]] to acquire the data and turn this information into EPICs Process Variables.


#### BBB Configuration

Whilst SERIALxxCON can't yet automatically identify the baseboard, it needs to be manually configured by running the following commands via SSH:

* Configure the SPI buses
 $ config-pin P9_17 spi_cs
 $ config-pin P9_21 spi
 $ config-pin P9_18 spi
 $ config-pin P9_22 spi_sclk
<section end=systemUpgrade />

* Write the previous commands on `/etc/rc.local` if desired

* Stop bbb-function
 $ systemctl stop bbb-function
<section end=systemUpgrade />

* Disable bbb-function if desired
 $ systemctl disable bbb-function
<section end=systemUpgrade />

#### Python3 module

A Python3 module was written to facilitate the communication between SERIALxxCON and the baseboard.

The Very Simple Protocol (VSP) module functions are:

* send(char, timeout_ms = 1)

Sends a character to the monitoring board and returns a string with its response

* get(*chars)

Sends multiple characters to the monitoring board and returns a list with it's response in order

* get_all()

Returns a list with values for supply voltage, fan status, DHT's temperature measurement, fan current, humidity, LM35's temperature measurement, back door status and front door status in that order. It takes about 1 second to return the finish the acquisition.

It also filters the values, so if they are not valid it will be 'None'.

* nf_all()

Similar to get_all() but does not filter values, returning the list as is.

* get_LM35()

Returns LM35's temperature value

* get_DHT()

Returns the boards DHT's temperature value

* get_humidity()

Returns humidity value

* get_fdoor()

Returns front door status

* get_bdoor()

Returns back door status

* get_fanstat()

Returns fan status

* get_current()

Returns electrical current value

* get_voltage()

Returns supply voltage value

* isBoard()

Returns the board version if version is v1.6 or higher.

### EPICS-Input/Output Controller

Runs o Control System Servers, requesting data through TCP-IP to the BBB that controls the baseboard and then converts the information into EPICS Process Variables. The program connects to every BBB registered as a baseboard owner.

The Current PV names are:

- IA-XY:CO-LM35:Temperature-Mon

- IA-XY:CO-DHT:Temperature-Mon

- IA-XY:CO-DHT:Humidity-Mon

- IA-XY:CO-FrontDoor:Status-Mon

- IA-XY:CO-BackDoor:Status-Mon

- IA-XY:CO-Fan:Status-Mon

- IA-XY:CO-Fan:Current-Mon

- IA-XY:CO-Outlet:Voltage-Mon

### Graphical User Interface

In older versions, the other possible TCP/IP client developed for this project is a Graphical User Interface, which shows the current information per rack room. In more recent versions, the GUI is based on PyDM, a EPICS client, so the software does not need to connect to every baseboard-owner individually, it gets the value directly from the PV.

|![](/img/groups/con/rack_monitor/GUI_sr.jpeg)|
|-|
|**Figure 6**: Rack Room screen (old version).|

## BSMP Entities
The higher level of communications (TCP/IP) uses [[CON:Basic_Small_Messages_Protocol_(BSMP)|Basic Small Messages Protocol(BSMP)]].


|ID| Variable| Size (bytes)| Access |
|-|-|-|-|
|0x43| Fan electric current consumption| 1| R |
|0x54| DHT11 or DHT22 temperature |
|0x62| Back door status |
|0x63| Fan status |
|0x66| Front door status   |
| |
| |
|0x74| LM35 temperature| 2  |
| |
| |
|0x75| Humidity| 1 |
|0x76| Outlet voltage  |

### Variable: Fan current

  `ID: 0x43     Size: 1 byte     Read-only` 

Value that corresponds to 100 times the real value of current (in Amperes):    $Current = \frac{Byte}{100}$


### Variable: DHT temperature

  `ID: 0x54     Size: 1 byte     Read-only` 

Exact value of integer DHT measured temperature.


### Variable: Door status

  `ID: 0x62 and 0x66     Size: 1 byte     Read-only` 

In instead of using whole strings to inform the door status, the following representation values are used:

*0: Door open
*1: Door closed

### Variable: Fan status

  `ID: 0x63     Size: 1 byte     Read-only` 

In instead of using whole strings to inform the fan status, the following representation values are used:

*0: Fan off
*1: Fan on
*2: Error - Invalid value
*3: Overload - current above safe value

### Variable: LM35 temperature

  `ID: 0x74     Size: 2 bytes [Byte1|Byte0]     Read-only` 

Value that corresponds to 100 times the real value of temperature measured by LM35 sensor. Can be calculated by:

$ Temperature = \frac{(Byte[1] << 8) + Byte[0]}{100}$

### Variable: Humidity

  `ID: 0x75     Size: 1 byte     Read-only` 

Exact value of integer DHT measured humidity.

### Variable: Outlet voltage

  `ID: 0x76     Size: 1 byte     Read-only` 

Exact value of integer outlet voltage.
