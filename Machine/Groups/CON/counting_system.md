---
title: counting_system
description: 
published: 1
date: 2024-05-21T19:50:15.490Z
tags: 
editor: markdown
dateCreated: 2024-05-21T16:04:10.891Z
---

# CON: CountingPRU

## Introduction

[LNLS Controls Group](/Machine/Groups/CON.md) has designed a simple hardware solution for counting trains of pulses during a pre-defined time base. Based on Beaglebone's PRU (''Processing Real-Time Unit''), the system was first designed in order to compute data from commercial Beam Loss Monitors (BLMs) and in-house Gamma Sensors that will be installed in Sirius.

The current version is capable of counting pulses from up to 8 channels and can achieve the maximum rate of 14.29MHz. The main connection to Control System Network is through an Ethernet Port, where it will also get power from Power over Ethernet (PoE) standard (IEEE 802.3af).

## Hardware description

|![](/img/groups/con/counting_system/Diagram.jpg)|
|-|
|**Figure 1**: Diagram of stages on CountingPRU.|

The hardware is based on Beaglebone's PRU, which will count received pulses and make the counting available to main processor. To make it, some stages are necessary and them are showed on diagram beside:
When the Ethernet data cable entry on board, the first step is divide both electrical circuit and data, made at Power Supply Stage. In it, the circuit's power supply is provided by a Power Over Ethernet (POE) module that allows the electrical current needed for circuit operation to be carried over the Ethernet data cables, minimizing the number of cables required for hardware operations, without compromise the exchange of information. 

Furthermore, there are two types of interface connectors, which will be connected to the external pulsed sensors (detailed in next sections). Inside CountingPRU board, the inputs coming from sensors will be conditioned to +3.3V (BBB compatible) and will trigger the pulse detectors. Once the pulse is read by the respective PRU, the PRU will reset the pulse detector.


###  Power supply stage

|![](/img/groups/con/counting_system/RJ45-Input.png =200x)|
|-|
|**Figure 2**: Connector RJ45, Diode Bridge and XFRMR module.|

The POE used in this version is the Ag9205-S, produced by Silvertel and has 5V output and maximun 13W of power output. This board is also resposible for powering the BLMs and Gamma Sensors with +5V, -5V and +24V. These values are obtained using DC/DC converters: VIBLSD1-S5-S5-DIP and MEV1D0512DC.

Initially, both Rx (3, 6) and Tx (1,2) pins, come from RJ-45 connector, are connected on a POE XFRMR module, a Gigabit Ethernet Transformer POE, which provides the output Tx+, Tx-, Rx+ and Rx- to another RJ-45 connector, that will connet on the BeagleBone Black. The another pins of input connector and centertaps of the XFRMR module are connected in two diode bridges, that provide input voltage for the Ag9205 (Vin+ and Vin-), like figure 02.

After that, the silvertel’s output is connected on two DC/DC converters, already mentioned, which will convert the output to -5V and 24V. The first DC/DC (VIBLSD1-S5-S5-DIP) is a 5V/5V converter, its +VOUT output has been grounded, changing the pin from 0V to -5V. The  MEV1D0512DC converter is a DC/DC that provides -12V and +12V in its output. To get +24V of its, the output -12V also has been grounded, changing the +12V pin to +24V.

On both converters has been connected an output load, because to operate them efficiently and reliably is necessary an minimum output load which must not be less than 10% of maximum load (1W on both). If the actual load is less than the specified minimum load, the output ripple may increase sharply while its efficiency and reliability will reduce greatly (See figure 03).


Board typical power consumption: '''3.3 W''' (total) [[ A CONFIRMAR ]]

####  ***Adjustments in the Silvertel Ag9205-S***

|![](/img/groups/con/counting_system/DC-DC.png =250x)|
|-|
|**Figure 3**: DC/DC Converters and its outputs loads.|


|![](/img/groups/con/counting_system/Ag9205.png =250x)|
|-|
|**Figure 4**: Silvertel Ag9205 hardware configuration.|

The Ag9205-S module has two configures possible, the power and the output voltage. For this, resistors are connected between CP and ADJ pins and in/outputs. The maximum output Power can be adjusted from 3.84 W to 12.95 W and the output voltage, from 4.5V to 5.65V. Each configuration can be seen on datasheet of module.

As 13W and 5V outputs are default values, both CP and ADJ pins haven’t been connected. As the minimum ouput power needs to be confugured, was added output load  on Silvertel Ag9205. In this configuration, the minimum power is 0.44W, therefore, the value of output load is 50Ω. The final circuit of Ag9205 can be seen on figure 04.


###  Bergoz BLMs inputs Stage

|![](/img/groups/con/counting_system/Photdiodes.png =250x)|
|-|
|**Figure 5**: Detail of photodiodes on BLM monitor.|

The commercial BLM (Beam Loss Monitor) is produced by Bergoz Instrumentation and is based on two photodiodes that emit photons when a charged particle passes through them.

At CountingPRU, the BLM’s inputs are a double RJ-45 connector which are connected on a transformer, once that the monitor has a differential output of ±2,5V, but this signals are generate by a transformer on Bergoz’s BLM without center tap, resulting in a signal with offset. To solve this, the input differential signal was converted in a single  ended signal -  grounding one pin of transformer - with double of initial voltage. (See figure 05).
After that, the pulse switch a transistor that generates a pulse down in its collector, this pulse is inverted by a logic NOT  gate, and the result can be seen at figure 06.

The output signal of the logic gate is sended to a Flip-Flop D and used as clock. The objetive is to obtain a pulse with voltage compatible with BeagleBone (+3,3 V) and change it to a square wave, which will be send to BBB.

####  ***Calibration of BLMs***

BLM circuits are calibrated ex-factory for a spurious count rate of 10 kHz ±800 Hz. To make it, is necessary apply a voltage of +5V via a 4.7kΩ resistor to  pin ‘Enable/Disable’ of each photodiode and adjust the referent potentiometer till 9.6~10.4 kHz output. The counter has two electronic switches to this purpose, switching 5V through a resistor on each ‘Enable/Disable’ pin, controlled by four BeagleBone pins (C13, C14, C15, C16 all of them on the P9 pin bus).

####  ***BLMs Interface***

This interface is specified for commercial BLMs whose outputs are differential signals.
There are two channels in two connectors (one channel per connector) for this topology.

* '''Connectors:''' 2 connectors
* '''Channels/connector:''' 1 channel
* '''Connector type:''' RJ45 (8P8C)
* '''Connector Pinout:'''

|Pin| Description |
|-|-|
|1| Data - |
|2| Data + |
|3| +24V (10mA max) |
|4| Enable/Disable A |
|5| Enable/Disable B |
|6| Ground (GND) |
|7| +5V (50mA max) |
|8| -5V (80mA max)  |


### LNLS Gamma inputs

|![](/img/groups/con/counting_system/GammaInput.png =500x)|
|-|
|**Figure 6**: Gamma sensors input pulse circuit.|

On top of that, the CountingPRU also has inputs to up six gamma sensors developed in-house. The pulses coming from gamma detectors are +5V signals, therefore, after connector, the pulses switching a Flip-Flop D. 
The use of FF is to change gamma detectors pulses to a square wave, change its voltage to 3,3V (compatible with BeagleBone) and protect the BBB inputs from high level voltage pulses. The figure 07 show how is the input circuit.
A resistor was also added to the Flip-Flop clock pin to increase the input impedance of the FF and pins of BeagleBone Black are connected on pins of both FF and buffer, to controlling them.


#### ***Gamma Sensors Interface***

This interface is specified for mainly for in-house developed Gamma Sensors whose outputs are TTL compatible.
There are six channels in two connectors (three channels per connector) for this topology.

* '''Connectors:''' 2 connectors
* '''Channels/connector:''' 3 channel
* '''Connector type:''' IDC Header 2x8 pitch 1.27mm ([Board Header](http://www.cnctech.us/productdetails.asp?ID=4168){target=_blank} | [Cable Socket](http://www.cnctech.us/productdetails.asp?ID=3327){target=_blank})
* '''Connector Pinout:'''

|ID|Pin|Pin|ID|
|-|-|-|-|
|GND| 1| 2| Channel 1 |
|GND| 3| 4| Channel 2 |
|GND| 5| 6| Channel 3 |
|GND| 7| 8| GND |
|GND| 9| 10| GND |
|+24V| 11| 12| GND |
|+5V| 13| 14| +5V |
|GND| 15| 16| GND  |


###  Hard reset
The hard reset is responsible for ensure that, if an error occurs and the BBB doesn't respond, the system will be restarted by hardware.


###  Heart beat

The LED on the front of the board has the function of showing the user when  CountingPRU has started and it is available for counting. It is controlled by a BeagleBone GPIO (P8B28). Then it will be described what the control program looks like.


###  Beaglebone Black


### Groupment in PRUs and counting rates

As we have both PRUs working in parallel, we separate the channels proccessing for each of them. In this way, each PRU will treat only four channels, divided according to the table below.

|Type| Connector #| Channel #| Channel Naming| Treated by |
|-|-|-|-|-|
|<br><br><br>LNLS (Gamma)<br><br>|<br> 1<br>| 1| LNLS1| PRU1 |
| |2| LNLS2 |
| |3| LNLS3 |
| |2| 1| LNLS4 |
| |2| LNLS5| PRU0 |
| |3| LNLS6 |
|Commercial (BLM)| 1| 1| Commercial1 |
| |2| 1| Commercial2  |


The maximum counting rate depends on the number of active channels in each PRU. If only one channel is used, the respective PRU can count up to 14.29MHz. However, if all the channels are used (four channels), the maximum counting rate is 10MHz.

|Active Channels| Up to [MHz] |
|-|-|
|1| 14.29 |
|2| 12.50 |
|3| 11.11 |
|4| 10.00  |

## Software interface

In order to communicate with the designed hardware, firmware for PRUs and a library for user interface are needed. Also, once the project deals with PRUs and Beaglebone's general-purpose input/output, it is mandatory to configure its pins before running any code.

All library files for boards in Sirius are available in [Gitlab page](https://gitlab.cnpem.br/patricia.nallin/counting-pru/tree/master/src/v2-3 CountingPRU){target=_blank} (available only through CNPEM network).


### System library

#### Building the library

Run the script ´library_build.sh´. This will compile PRU and host codes, install it to your Beaglebone and create a Python module to use these libraries.

#### Using the library

''Before using it''

1. Apply the Device Tree Overlay (DTO) to configure Beaglebone pins to PRU. Run `DTO_CountingPRU.sh` script.

2. In your python code, you can just:

 import CountingPRU

#### Available Methods

* Init()
PRU initialization. Shared memory configuration and loading binaries into both PRUs.  

* Counting(time_base)
Starts counting during time_base period, in seconds. This method will be blocking until the end of counting.  
Returns: list of 8 itens (32-bit integer each), corresponding to a channel counter value

* Close()
Closes PRUs and memory mapping.

### BSMP Socket

Standard CountingPRU application is based on a TCP/IP socket on port 5000 in order to have its IOC running remotely on a server.

Protocol is defined by BSMP ([Basic Small Message Protocol](https://github.com/lnls-sirius/libbsmp/){target=_blank}) and its variables and groups are defined below:

|ID| Variable| Access| Size (bytes)| Group ID |
|0| TimeBase| R/W| 2| --- |
|1| LNLS1| R| 4| 1 |
|2| LNLS2 |
|3| LNLS3 |
|4| LNLS4 |
|5| LNLS5 |
|6| LNLS6 |
|7| Commercial1 |
|8| Commercial2 |
|9| Inhibit A1 - bit 0| R/W| 1| --- |
|Inhibit B1 - bit 1 |
|Inhibit A2 - bit 2 |
|Inhibit B2 - bit 3 |
|11| Serial Number LNLS1| R/W| 1| --- |
|12| Serial Number LNLS2 |
|13| Serial Number LNLS3 |
|14| Serial Number LNLS4 |
|15| Serial Number LNLS5 |
|16| Serial Number LNLS6 |
|17| Serial Number Commercial1 |
|18| Serial Number Commercial2  |

### IOC

####  Generate Averages 
This program is responsible for calculating the counting averages of each gamma monitor at Sirius and modifying epics variables to show them to users.
For this, the program is based in get data of counting on Archiver View, using requests commands, filter the data from the json obtained and make the averages.

The main program, as well as dockerfile and logs files are disposable in the gitlab repository, [here](https://gitlab.cnpem.br/robert.polli/gamma_monitoring){target=_blank}


### Operator interfaces

####  Gamma Monitoring

The Controls Group also has been developing a simple software to show some information of the counters and their sensors, in addition to having the functionality of setting its time bases. The Gamma Detectors Monitoring is divided in two parts, first is the docker container responsible for generating the averages, already mentioned, and the second is the windows that will interact with users.
To run the program, go to gamma_monitoring folder, at terminal, and write: 
 pydm main.py

##### ***Overview***

|![](/img/groups/con/counting_system/Overview.png)|
|-|
|**Figure 7**: Buttons of Overview function.|

When the program starts, it is possible see two types of “Overview”, Counting and Pulses Average. Each one is an epics variable data group, getting from Archiver View and update every ten seconds. 
The “Counting – Overview” button will show the last count of all gamma sensors present at Storage Ring (in pulses per second), as well as an “'''Overview of Time Bases'''” window, which has the time base information of all detectors.
To see data on “Pulses Average – Overview” it is necessary, first of all, select the check buttons in “'''Pulses Average'''” section whose graph the user wants to show, after that, up to four windows will be displayed.
In the whole overview, when the graphs are opened, it’s necessary to select at “Control of graph” menu which detectors will be displayed in the graph.

##### ***Set Time Bases***

|![](/img/groups/con/counting_system/TimeBase_v2.png)|
|-|
|**Figure 8**: Set Time Bases option.|

The counts of each gamma monitor occur within a time range defined as ‘Time Base’. While this time doesn’t end, pulses come from gamma sensors are counted by CountingPRU. 
With Gamma Monitoring program, the user can define how long this time base will be. First, choose which counter do you want to set the Time Base, after, write the value in the box (in seconds), and then, press “Set Time Base” button. It’s also possible define all the Time Bases, just select the check button ‘Set all time bases’.

##### ***Plot informations***

|![](/img/groups/con/counting_system/ImagePlot.png)|
|-|
|**Figure 9**: Image showing both counter and sensor selected.|


|![](/img/groups/con/counting_system/Plot.png)|
|-|
|**Figure 10**: Informations about Counter and Gamma Monitor.|

Fist, it is necessary select a sector of Storage Ring, on '''''Sector''''' box, choose one of 20 sectors of Sirius. After, '''''Counter''''' box will automatically filled with name of all counters from this sector. Next step is choose one of them, and then, one of '''''Gamma Detector''''' connected to it.
When a counter and a gamma monitor is chosen, some information will automatically appear about the counter and its channel:
 
* In the images, it is possible see where is both selected counter and gamma sensor; 

* On right, it's showed the name and time base of counter;

* In the '''''"Gamma Detectors"''''' list, will appear all channels of counter (None means that channel it's not used) and in which is the detector selected.

* Below, there are two datas, the last sensor count and the name of the PV associated with the gamma monitor.

Both "Time Base" and "Last Count" are configured as Epics Channel Access, in other words, it is possible reading and writing to Epics Process Variables (PVs) associated to each label, via the CA protocol, and update the Time Base and Last Count values automatically.

##### ***Archiver View***

|![](/img/groups/con/counting_system/ArchiverButtons.png)|
|-|
|**Figure 11**: Buttons which open the Archiver View.|

The Gamma Monitoring program also has some show options for the user of graphs of last  pulses count and averages, opened on Archiever View.

When a counter and a sensor are selected by user and the information is displayed, a button "Counting - Archiever View" is enabled and after clicking on it, a window will open with a link to archiver of the selected gamma sensor.

As well as the "Counting - Archiver View", it is possible see graphs of counts averages of each gamma monitor. This function is enabled immediately after plotting a counter, using the "Pulses Averages - Archiever View" button. Once clicked, some averages will appear for the user: "Last Day", "Last Week", "Last Two Weeks" and "Last Month", then, if the user selects a check button, on the next click it will open the average in the archiever view.


### IPs Control software

One of the programs belonging to the "BBB-functions" have the finality of defining the IPs of the counters board. This program are responsible for setting its ip to dhcp, automatically.
It is executed only on boot of BeagleBone, if a Counter Board is identified by it.

#### To dhcp IP

The program responsible to define the internet protocol address of counters to dynamic ip is the "key_dhcp.py". When BeagleBone is started, the inputs pins of the gamma monitors are analyzed, if them are in a specific sequence, the counter's ip is changed.
The sequence required to change ip is "101010", obtained by connecting an external monostable oscillator hardware that will trigger the FF of each input.

If the ip has changed to dhcp, the panel led will blink quickly, wait for the stop and the board will be ready.
