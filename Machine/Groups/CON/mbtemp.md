---
title: MBTemp
description: 
published: 1
date: 2024-05-27T21:57:11.164Z
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

The solution of the quadratic equation yields the following relationship between temperature and resistance:

$$
T = \frac{-A + \sqrt{A^2 - 4B\left(1 - \frac{R_T}{R_0}\right)}}{2B}
$$


Since *B* is relatively small, the resistance changes *almost* linearly with the temperature. Considering that most applications will be around environment temperature, a linear fit is acceptable and is what will be done by Controls Group at first.

<br >

###  Measuring the resistance 

Once Pt100 is a passive temperature sensor, it is needed to have a circuitry in order to have its value. 4-wire Pt100 sensors are recommended the most and its measurement can be seen in the following image:

|![](/img/groups/con/mbtemp/Sch_pt100.png)|
|-|
|**Figure 2**: |

One pair is used for current injection. Having a constant current flowing through a resistance, a voltage drop is generated. The other pair collects the voltage over the Pt100 resistor and makes it available for measurements or conditioning electronics. Having two pair of cables makes the measurement more reliable, once cable resistance (ie, length/section/etc) is not taken into account.

It is important to assure that dissipated power due to the current flowing through Pt100 sensor, which is a resistance, does not heat the sensor itself, otherwise the final value may not correspond to the real environment.

3-wire and 2-wire Pt100 can also be read using the same method. However, final values may not be equal within these three Pt100 types due to cable resistance interference.

<br >

###  Digital filter 

As an overview in this application, implementing a digital filter eliminates noise during measurements. Temperature gradient is low and data acquisition does not need to be fast. It has been chosen to filter the values digitally using the exponential moving average law:

$$
Temperature Average = \frac{OldTemperatureValue*\alpha + NewTemperatureValue*(1000 - \alpha)}{1000}  \;\; (0\; \leq \alpha < 1000)
$$

Alpha factor is user-defined and must be an integer in the range 0 - 999.
For MBTemp application, there will be some exceptions for this filter (explained on firmware section).

<br >

##  Hardware details 

<br >

###  Overview 

The latest MBTemp hardware version, 2.6, was manufactured in 2018 and are currently in use at Sirius installations. This is an Eurocard-size board with a stack, dedicated for Pt100 input connectors routing.

It can interface to up to 8 channels. There is only one current generator, one analog conditional circuitry, one one-channel analog-to-digital converter. It means that channels are multiplexed and read sequentially.

|![](/img/groups/con/mbtemp/Mbtemp-up.png)|
|-|
|**Figure 3**: |


[[[ FOTO DO PAINEL FRONTAL + TRASEIRO ]]]

<br >

###  Power input and filters 

In order to power the board and have it completely functional, connect the front jack with a reliable +5V/2A power source (positive center). Controls Group recommends CUI Inc. power supply brand.

Typical power consumption: **1.5 W**


It is possible to power the board with higher voltages. **Caution: it needs a simple hardware modification on the board!**

<br >

###  Pt100 input connectors 

|![](/img/groups/con/mbtemp/4p4c.png)|
|-|
|**Figure 4**: |


|![](/img/groups/con/mbtemp/Pt100-layout.png)|
|-|
|**Figure 5**: |


Modular RJ-11 (4P4C) connector has been chosen for Pt100 connectivity. Pins 1 and 2 will be connected to a Pt100 side and pins 3 and 4 will be connected to the other side. Current flow from I to GND and V+/V- is differential voltage on the sensor resistance.


MBTemp signals:

**1.** I (1 mA)

**2.** V+

**3.** GND

**4.** V-

<br >

###  PIC microcontroller 

A 16F-family PIC microcontroller (16F887A) is the core of the system. It is responsible for communication routine, data acquisition, coefficient storage and calculations. The code itself was written in C, compiled using MPLAB IDE (free version). More details about programming logic is described in the [CON:MBTemp#Firmware_details|specific section](link).

<br >

###  Power converters for conditioning circuitry 

An important stage for temperature data acquisition is the power converters for the conditioning circuitry. Some devices need symetric power supply or even a power supply greater than 5V for drop-out compensation. For that purpose, this piece of hardware converts and provides +6V and -5V for analog ICs.

<br >

###  Analog multiplexing 

For system optimization, there is only one channel for data acquisition. Once 8 channels are available, a set of multiplexing switches were added to the board, allowing each signal to be read sequentially. Current source is multiplexed as well, what is also interesting because it reduces power dissipation over a Pt100, reducing external interference.

Those switches are digitally controlled by the same microcontroller responsible for digital data acquisition.


|![](/img/machine/rf_system/CESR_cavity_SRF_module.png)|
|-|
|**Figure 6**: Cut view of the CESR cavity SRF module.|

<br >

###  Conditioning circuitry and ADC 

It is mandatory to have a conditioning circuitry for temperature data acquisition. As Pt100 sensors have low resistance and a low current flows, the voltage drop is relatively small and needs a gain and offset to be acquired by the ADC. Instrumentation ICs are  used as well as high precision voltage references and resistors. Digital result is read through SPI interface.

<br >

###  Serial communication (RS-485) 

For serial communication, the standard chosen by Controls Group is also adopted (described [CON:SERIALxxCON|here](link)).

* **Connector and Pinout**
A 6P6C (RJ-12/RJ-25) has been chosen for Controls system as well as its pinout, as shown below. MBTemps also follow this standard.

|![](/img/groups/con/mbtemp/6P6C_ConnectorPinout_RS485.png)|
|-|
|**Figure 7**: |

* **Termination**
Termination is needed ***only in the last device connected to the multi-drop serial network*** in order to match serial transmission line. It can be activated by pulling the correspondent front panel switch on. RS-485 impedance is 120Ω.

<br >

###  Board ID and module address 

Board ID in a unique ID that the board has received after being manufactured.

On the other hand, the module address is specific for communication purpose. As it is a BSMP slave device, it will only reply commands that match their pre-configured address. It is configured through the 5-position switch front panel, binary coded. Valid value: 1 to 31.

**Attention**: once the module address is modified, it is mandatory to reboot the board!

<br >

###  Production units 

400 units have been manufactured in early 2018. They have been installed on Sirius site in several environments (tunnel, power area, RF room, instrumentation area, etc.).

<br >

###  More technical documentation 

Detailed documents can be found at project repository at CNPEM gitlab ([click here](http://gitlab.cnpem.br/patricia.nallin/mbtemp), you must be connected through CNPEM network).

<br >

###  Hardware versions 

Eurocard sized:

* **v2.6 (latest)**
* v2.5

<br >

##  Firmware details 

<br >

###  Brief description 

Firmware running on PIC microcontrollers has one single process. Initially, it gets the board module ID from switches on the front panel, it gets all static variables (stored in its EEPROM memory): alpha, linear and angular coefficients. Also, it configures a DCDC converter in the board (which is currently not in use) and configures the modules that will be used (I2C, SPI, UART, interruption).

* SPI: used for getting data from ADC;
* I2C: communication with DC/DC converter;
* UART: serial interface RS-485;
* Interruption: treating incoming serial data and replying to it (if necessary).

After that, a continuous loop begins, which reads all eight channels sequentially.

<br >

###  Serial communication 

Communication through [[CON:MBTemp#BSMP_entities|BSMP protocol and entities]](link). You can have more information about variables in next section and about [BSMP protocol](/Machine/Groups/CON/bsmp) in a dedicated page.

Serial communication physical layer is based on RS-485, using the pattern predefined by Controls Group, as shown above.

Once a character is received by the board, it enables an interruption signal which will interrupt the continuous loop and treat the incoming message. If the board is the destination, it will reply to the message and go back to reading Pt100 sensors.

<br >

###  Calibration - Linear fit 

MBTemps perform the reading of analog values, which are amplified to a larger and readable signal. Yet, even though specific componentes are used, they may add errors to the final output value. In general, for those purposes, it is needed to calibrate each single system, in order to guarantee correct and reliable readings for all channels.

As seen above, Pt100 temperature-resistance equation is a second-order one. Chosen microcontroller is not able to perform this operations and thus, a linear fit may apply. Almost all applications will be measuring temperatures near environment temperature, so a linear fit around 25 °C does not add elevated errors to final results:

|![](/img/groups/con/mbtemp/Pt100-curves.png)|
|-|
|**Figure 8**: |

So, for a linear fit, it is needed to acquire the values from two different temperature points, at least. Controls Group, while calibrating the boards, takes 3 different points (usually 20, 25 and 30 °C) and 30 samples for each value. It is important to note that, for calibration and temperature reading, it is not needed to calculate what is the Pt100 current resistance. Having the ADC value is enough for calibrating and readings:

$$
Read Temperature = \frac{ADvalue}{k} - b
$$

After calibration, **k ≈ 48** and **b ≈ 258**. They are unique for each piece of hardware.

***INTERESTING NOTE: RECOVERING FROM LINEAR FIT TO REAL VALUE IS POSSIBLE IN HIGH LEVEL SYSTEMS AND IT IS DONE IN CONTROLS IOCS.***

<br >

###  Temperature measurements 

|![](/img/groups/con/mbtemp/Mbtemp-reading-flow.png)|
|-|
|**Figure 9**: |


Sequential readings are done according to the flow chart above. Double ADC reading, with and without current, is performed to eliminate (or highly decrease) interference due to power network (60Hz, in Brazil).
Also, if a temperature value is greater than 1 °C compared to last value, a new reading cycle is performed to assure this new measurement is valid.


Range: 0 °C to ~395 °C from board (linear fit)    |    0 °C to ~420 °C from high level system (quadratic equation)

<br >

##  BSMP entities 

Once MBTemp communication protocol is based on BSMP, data acquisition and variable handling is done using its entities, which are all variables.

{| class="wikitable" style="text-align: center;"
|-
! ID !! Variable !! Access !! Size (bytes) !! Group ID
|-
| 0 || Channel 0 (Input 1) || rowspan="8" | R || rowspan="8" |2 || rowspan="8" | 0 and 1
|-
| 1 || Channel 1 (Input 2)
|-
| 2 || Channel 2 (Input 3)
|-
| 3 || Channel 3 (Input 4)
|-
| 4 || Channel 4 (Input 5)
|-
| 5 || Channel 5 (Input 6)
|-
| 6 || Channel 6 (Input 7)
|-
| 7 || Channel 7 (Input 8)
|-
| 8 || Alpha 1 (a1)|| rowspan="11" | R/W || rowspan="3" | 2 || rowspan="11" | 0 and 2
|-
| 9 || Angular coefficient 1 (k1)
|-
| 10 || Linear coefficient 1 (b1)
|-
| 11 || AD Reading Mode || rowspan="2" | 1 
|-
| 12 || Reading Mode
|-
| 13 || Alpha 2 (a2)|| rowspan="6" | 2
|-
| 14 || Angular coefficient 2 (k2)
|-
| 15 || Linear coefficient 2 (b2)
|-
| 16 || Alpha 3 (a3)
|-
| 17 || Angular coefficient 3 (k3)
|-
| 18 || Linear coefficient 3 (b3)
|}

<br >

###  Variable: Temperature (Channels ID 0 -7) 

  ID: 0 - 7     Size: 2 bytes [Byte1|Byte0]     Read-only 

Acquired temperature according to each channel. To get its value: 

$$
Temperature = \frac{(Byte[1] << 8) + Byte[0]}{100}
$$

<br >

###  Variable: Alpha (IDs 8, 13 and 16) 

  ID: 8, 13 and 16     Size: 2 bytes [Byte1|Byte0]     Read/Write

Moving average factor for temperature reading (performed on board). It must be in the range 0-999.

$$
\alpha = (Byte[1] << 8) + Byte[0]
$$

Variables are stored three times in order to guarantee data consistency after system start up.
Any change on any variable (ID 8, 13 or 16) will change others as well (ID 8, 13 and 16), once they refer to the same constant.

<br >

###  Variable: Angular coefficient (IDs 9, 14 and 17) 

  ID: 9, 14 and 17     Size: 2 bytes [Byte1|Byte0]     Read/Write

Angular coefficient for temperature calculation according to ADC value.

$$
k = \frac{(Byte[1] << 8) + Byte[0]}{100}
$$

Variables are stored three times in order to guarantee data consistency after system start up.
Any change on any variable (ID 9, 14 or 17) will change others as well (ID 9, 14 and 17), once they refer to the same constant.

<br >

###  Variable: Linear coefficient (IDs 10, 15 and 18) 

  ID: 10, 15 and 18     Size: 2 bytes [Byte1|Byte0]     Read/Write

Linear coefficient for temperature calculation according to ADC value.

$$
b = \frac{(Byte[1] << 8) + Byte[0]}{100}
$$

Variables are stored three times in order to guarantee data consistency after system start up.
Any change on any variable (ID 10, 15 or 18) will change others as well (ID 10, 15 and 18), once they refer to the same constant.

<br >

###  Variable: AD Reading Mode (ID 11) 

  ID: 11     Size: 1 byte      Read/Write

In order to read temperature values, it must be 0. If, for any specific reason, user wants to read the last ADC raw value in variables 0 to 7, 1 should be written to "AD Reading Mode" variable. If it is desired to read the average from least 20 readings from one specific channel, variable value should be 2;

* 0: Temperature reading (Op Mode variable (ID 12) must be 8) [DEFAULT VALUE AFTER STARTUP]
* 1: Last ADC raw value reading
* 2: Average from last 20 readings from one specific channel (Op Mode variable (ID 12) must not be 8)

<br >

###  Variable: Reading Mode (ID 12) 

  ID: 12     Size: 1 byte      Read/Write

This variable handles reading mode. If it is equal to 8 (default value after startup), sequential readings for all channels are performed.
If it is between 0 and 7, readings will be performed only in the channel correlated, without temperature conversion. ADC values will be available for reading, according to variable AD Reading Mode (ID 11). Other channels may have invalid data.

8 IS THE DEFAULT VALUE AFTER STARTUP.

<br >

## Integration to EPICS

The [CON:SERIALxxCON|SERIALxxCON](link) board, based on Beaglebone Black Single Board Computer, will handle communication with up to 31 MBTemp boards. This SBC is the bridge between the hardware and the EPICS IOC, running on Controls Server, which publishes each temperature measured by a Pt100 sensor as a process variable.

This EPICS application is [CON:Stream-IOC|Stream-IOC](link), a StreamDevice-based EPICS IOC developed by the Controls Group to interface to EPICS.

<br >

###  Linear Fit Correction 

IOC deals with two variables to each channel: Temperature and Temperature-Raw

Temperature-Raw (Traw) is the value acquired from the board, linear fitted. Temperature value is calculated, based on the real quadratic equation and the value obtained from the board, which leads to:

$$
Temperature = \frac{-{R_0}{B}\sqrt{{R_0}^2}}{2A{R_0}}
$$