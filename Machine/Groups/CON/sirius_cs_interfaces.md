---
title: Sirius control system interfaces
description: 
published: 1
date: 2024-06-03T16:29:19.993Z
tags: 
editor: markdown
dateCreated: 2024-06-03T16:28:38.118Z
---

# CON: Sirius control system interfaces

<br>

## Introduction

This page contains listings of control hardware and its interfaces to Sirius control system, from a point of view of the integration tasks assigned to [LNLS Controls Group](/Machine/Groups/CON).

<br>

## Beam diagnostics and feedback

Beam diagnostics and feedback systems are under responsibility of [[DIG:DIG|LNLS Beam Diagnostics Group]]. All devices associated with these systems will be plugged into the control system through an Ethernet interface. EPICS IOCs will run on dedicated rackmount computers. In the future, this section will contain documentation about all beam diagnostics and feedback devices, network points and IOCs.

<br>

## Interlock system

[[IMA:IMA|LNLS Magnets group]](link) is developing an interlock system for Sirius based on Rockwell Automation Allen-Bradley programmable logic controllers (PLCs). Default communication interface for interlock modules will be 100 Mbps Ethernet, under a device-level ring (DLR) topology. With this topology, the interlock system will interface to the [[CON:Sirius_control_system_network|control system network]] using a few Ethernet ports.

We intend to design an EPICS interface for the interlock system using [EtherIP](http://ics-web.sns.ornl.gov/kasemir/etherip/){target=_blank}.

This section will be updated soon with details about the network connections and supervisory software of the interlock system.

<br>

## Linac

Sirius Linac will be supplied by the Shanghai Institute of Applied Physics (SINAP). As a turnkey solution, it has its own control system (based on EPICS), with client computers, operator interfaces and an archiving software, among others.

Installation of Linac is scheduled to early 2018. After its assembly at the new building, we will plug its control system to [Sirius control system network](/Machine/Groups/CON/counting_system) and develop some integration with other [control system](/Machine/control_system) applications.

<br>

## Power supplies

Sirius power supplies are under development by [ELP:ELP|LNLS Power Electronics Group (ELP)](link). [Controls Group](/Machine/Groups/CON) is responsible for integrating them to the control system.

Remote operation of power supplies is possible through a serial interface (RS-485). Communication protocol for this interface is [Basic Small Messages Protocol (BSMP)](/Machine/Groups/CON/bsmp).

There will be seven different models of power supplies in Sirius. Tables below show an old specification of BSMP entities of power supplies. As this specification is being modified, in a few weeks this section will be updated.

Translation of BSMP entities into EPICS process variables will be performed by an application running at a BeagleBone Black SBC. This application will handle BSMP entities in an adequate manner, depending on what type of power supply is being managed.

**Table 1**: BSMP variables of Sirius power supplies 

|ID| Size (in bytes)| C type| R/W| Name| Description| Unit |
|-|-|-|-|-|-|-|
|0| 4| float| R| iLoad1| Load current measurement given by DCCT 1| A |
|1| 4| float| R| iLoad2| Load current measurement given by DCCT 2| A |
|2| 4| float| R| iMod1| Current at power module 1 (Hall sensor reading)| A |
|3| 4| float| R| iMod2| Current at power module 2 (Hall sensor reading)| A |
|4| 4| float| R| iMod3| Current at power module 3 (Hall sensor reading)| A |
|5| 4| float| R| iMod4| Current at power module 4 (Hall sensor reading)| A |
|6| 4| float| R| vLoad| Load voltage| V |
|7| 4| float| R| vDCMod1| DC-link voltage measurement at power module 1| V |
|8| 4| float| R| vDCMod2| DC-link voltage measurement at power module 2| V |
|9| 4| float| R| vDCMod3| DC-link voltage measurement at power module 3| V |
|10| 4| float| R| vDCMod4| DC-link voltage measurement at power module 4| V |
|11| 4| float| R| vOutMod1| Output voltage at power module 1| V |
|12| 4| float| R| vOutMod2| Output voltage at power module 2| V |
|13| 4| float| R| vOutMod3| Output voltage at power module 3| V |
|14| 4| float| R| vOutMod4| Output voltage at power module 4| V |
|15| 4| float| R| temp1| Temperature measurement 1| °C |
|16| 4| float| R| temp2| Temperature measurement 2| °C |
|17| 4| float| R| temp3| Temperature measurement 3| °C |
|18| 4| float| R| temp4| Temperature measurement 4| °C |
|19| 2| uint16_t| R| ps_OnOff| Status of power supply: 0 = turned off, 1 = turned on| - |
|20| 2| uint16_t| R| ps_OpMode| Power supply mode of operation: 0 = SlowRef, 1 = FastRef, 2 = WfmRef, 3 = SigGen| - |
|21| 2| uint16_t| R| ps_Remote| Power supply command mode: 0 = remote, 1 = local, 2 = PC host| - |
|22| 2| uint16_t| R| ps_OpenLoop| Power supply control mode: 0 = closed loop, 1 = open loop| - |
|23| 4| uint32_t| R| ps_SoftInterlocks| Variable which indicates the ocurrence of soft interlocks. Each bit correspond to one interlock event.| - |
|24| 4| uint32_t| R| ps_HardInterlocks| Variable which indicates the ocurrence of hard interlocks. Each bit correspond to one interlock event.| - |
|25| 4| float| R| iRef| Current reference| A |
|26| 2| uint16_t| R| sigGen_Type| Type of waveform for signal generator: 0 = sine wave, 1 = square wave, 2 = triangular wave, 3 = frequency sweep| - |
|27| 4| float| R| sigGen_Freq| Frequency for signal generator| Hz |
|28| 4| float| R| sigGen_Amplitude| Amplitude for signal generator (under the frequency sweep mode, amplitudes are given by curve 1)| A |
|29| 4| float| R| sigGen_Offset| Offset for signal generator| A |
|30| 4| float| R| wfmRef_Gain| Gain value for WfmRef reference| - |
|31| 4| float| R| wfmRef_Offset| Offset value for WfmRef reference| A |
|32| 2| uint16_t| R/W| dp_ID| ID of DP module to be configured| - |
|33| 2| uint16_t| R/W| dp_Class| Class of DP module to be configured| - |
|34| 32| float[8]| R/W| dp_Coeffs[8]| Set of coefficients for DP module configuration|


**Table 2**: BSMP curves of Sirius power supplies 

|ID| Block size (in bytes)| Number of blocks| C type| R/W| Name| Description| Unit |
|-|-|-|-|-|-|-|-|
|0| 8192| 2| float| R/W| wfmRef_Curve[4096]| Reference waveform points| A |
|1| 148| 1| float| R/W| sigGen_SweepAmp[37]| Amplitudes corresponding to each frequency of frequency sweep module (1 - 9 Hz, 10 - 90 Hz, 100 - 900 Hz, 1000 - 10000 Hz)| A |
|2| 8192| 2| float| R| samplesBuffer[4096]| Generic circular buffer| A  |

**Table 3**: BSMP functions of Sirius power supplies 

|ID| Name| Input| Output| Description |
|-|-|-|-|-|
|0| TurnOn| -| uint8_t command_ack| Turn on the power supply. Mode of operation is the last programmed one. |
|1| TurnOff| -| uint8_t command_ack| Turn off the power supply. |
|2| OpenLoop| -| uint8_t command_ack| Open the control loop. After that, all controllers are disabled and the input of PWM modulators becomes the reference given by RefManager. |
|3| ClosedLoop| -| uint8_t command_ack| Close the control loop. |
|4| OpMode| uint16_t ps_opmode| uint8_t command_ack| Configure power supply mode of operation: 0 = SlowRef, 1 = FastRef, 2 = WfmRef, 3 = SigGen. |
|5| RemoteInterface| -| uint8_t command_ack| Put power supply in the remote command mode. |
|6| SetISlowRef| float iSlowRef| uint8_t command_ack| Set new SlowRef current reference. Input is given in amperes. |
|7| ConfigWfmRef| float gain| uint8_t command_ack| Set new parameters for WfmRef reference. Offset is given in amperes. |
|float offset |
|8| ConfigSigGen| uint16_t sigtype| uint8_t command_ack| Set new parameters for SigGen signal generator. Possible options for sigtype: 0 = sine wave, 1 = square wave, 2 = triangular wave, 3 = frequency sweep (for sigtype = 3, amplitude values are given by curve 1). Frequency is given in hertz. Amplitude and offset are given in amperes. |
|float freq |
|float amplitude |
|float offset |
|9| ConfigDPModule| -| uint8_t command_ack| Configure DP module with parameters stored in corresponding BSMP variables. |
|10| WfmRefUpdate| -| -| Broadcast command for ramp synchronization.  |


In the last table, ''command_ack'' answer is one of the following:

* 0x00: command acknowledged.
* 0x01: power supply operating in local mode.
* 0x02: power suply operating in PC host mode.
* 0x03: power supply locked due to soft interlock event.
* 0x04: power supply locked due to hard interlock event.

<br>

## Pulsed magnets

Current prototype of Sirius pulsed magnets controller unit has inside it a [[CON:PUC|PUC]](link) stack, with one analog and one digital interfaces. We intend to communicate to all controller units of the pulsed magnets with one BeagleBone Black, through a RS-485 serial network.

In Sirius, there will be ten controller units for pulsed magnets, distributed over six racks. Two extra controller units will be kept as a backup.

**Table 4**: Sirius pulsed magnets controller units 

|Rack| Pulsed magnet| Number of magnets |
|-|-|-|
|1| Booster injection septum| 1 |
|2| Booster injection kicker| 1 |
|3| Booster extraction kicker| 1 |
|4| Booster extraction septum| 2 |
|5| Storage ring injection thick septum| 2 |
|Storage ring injection thin septum| 1 |
|6| "On-axis" injection kicker| 1 |
|Pulsed multipole magnet| 1  |


Here, [[CON:PUC|PUC]](link)'s analog output signal is used as the reference for a Glassman high voltage power supply. Output level of the same power supply is read with [[CON:PUC|PUC]](link)'s analog input. Digital interface pins works as general-purpose inputs/outputs for remote operation of the controller unit:


**Table 5**: PUC input digital pins for pulsed magnets controller unit 

|Bit| Description |
|-|-|
|0| Thyratron fan status |
|1| Interlock |
|2| Personnel safety (door is open) |
|3| Temperature |
|4| Thyratron filament supply |
|5| Thyratron reservoir supply |
|6| High voltage supply overcurrent |
|7| Mode of operation (local/remote)  |


**Table 6**: PUC input digital pins for pulsed magnets controller unit 

|Bit| Description |
|-|-|
|0| Turn on/off the high voltage power supply |
|1| Turn on/off thyratron filament supply |
|2| Turn on/off thyratron trigger |
|3| Stand by/normal |
|4| Reset  |


We will start to perform tests with a prototype of the pulsed magnets controller unit soon. In order to interface it to EPICS, a server application named [Sirius-CAS-PM](http://git.cnpem.br/eduardo.coelho/sirius-cas-pm){target=_blank} was developed in Python with [pcaspy](https://github.com/paulscherrerinstitute/pcaspy){target=_blank}. It serves four process variables (PVs), each of them related to one of the analog/digital inputs or outputs of the [[CON:PUC|PUC]](link) inside the controller unit:

`PM:PUC:AnalogInput`
`PM:PUC:AnalogOutput`
`PM:PUC:DigitalInput`
`PM:PUC:DigitalOutput`

These PV names are provisory. Proper names will be defined later, and other PVs may also be added to the software already written.

[Sirius-CAS-PM](http://git.cnpem.br/eduardo.coelho/sirius-cas-pm){target=_blank} was created under an effort of evaluating [pcaspy](https://github.com/paulscherrerinstitute/pcaspy){target=_blank} as a reliable and easy-to-use tool for creating EPICS server applications. Overall, we are very satisfied with this Python module capabilities.

<br>

## RF system

[Controls Group](/Machine/Groups/CON) is working on the integration of these RF devices into the control system:

* RF power amplifiers designed by our [[RF:RF|Radiofrequency Group]](link);
* Low-level radiofrequency (LLRF) systems;
* PLCs (the same Allen-Bradley used on the interlock system).

<br>

## Vacuum systems

By now, we are working on EPICS interfaces for two equipments of Sirius vacuum systems. They are:

* Agilent 4UHV Ion Pump Controller;
* MKS 937B Digital Combination Vacuum Gauge Controller.

Communication interface of these devices is serial RS-232/RS-485. We are considering to adopt RS-485, so this way we can control several equipments with a single serial interface. But we still have to evaluate if this is the best approach, since communication baud rates are slow and maybe it is not a good idea to share the same interface between various devices.

Moreover, Sirius vacuum systems will have about 480 temperature measurements. For them, data acquisition hardware is a combination of [MBTemp](/Machine/Groups/CON/mbtemp) boards with Pt100 sensors.

The EPICS interface for controlling all vacuum devices is [CON:Stream-IOC|Stream-IOC](link).
