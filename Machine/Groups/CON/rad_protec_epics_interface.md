# CON: Radiation protection EPICS interface

## Introduction

This page will contain some documentation about the EPICS interface for Sirius Radiation Protection. The software is under development by [LNLS Controls Group](/Machine/Groups/CON).

## Components

The software was developed for the following radiation detector probes:

-  **Else Nuclear** - Saturn II 5702 containing an ICP-T-PF gamma detector and a LUPIN 5401 BF3-NP neutron detector;
-  **ThermoFisher Scientific** - FHT 6020 containing a FHT 192-10 gamma detector and a FHT 762 neutron detector;
-  **Berthold Technologies** - LB 6420 Dose Meter For Measuring Pulsed Radiation.

**Else Nuclear:** This code presents a program for requesting data via TCP / IP ethernet protocol. For requesting and data from the IHM STURN 5700 interface of the ionic radiation probes of the Italian manufacturer ELSE. The code requests the value of the instamed measurement of the Gamma IP radiation: 192.168.0.100 and the Radiation of Neutrons IP: 192.168.0.200. The communication port of the HMI is 10001 and the machine that retains the data is configured with IP: 192.168.0.50. The algorithm uses the python socket library to communicate with the remote EPICS server and send the information to it. The code is documented and commented.

**Thermo Fisher:** Is a serial communication with he settings of the RS485 protocol is 19200, 7, even and 2 stopbits. The probe outputs a datum every second.
An example is (BEL)Data(CS)(ETX)
Where: Data is the value of radiation in uSv/h

**Berthold Techonologies:**It uses ethernet communication and has a single device that obtains the value of the two probes (gamma and neutron).

The system was shipped in a BeagleBone Black with Linux distribution that managed the devices and communicated via network, ethernet, with the EPICS system binder.

## Development

The links below present the source code of each BeagleBone Black embedded in GitHub with comments on the lines of code.

-  **Cod Else Nuclear** - https://github.com/lnls-sirius/else-probe-ioc;
-  **Cod ThermoFisher Scientific** - https://github.com/lnls-sirius/thermo-probe-ioc;
-  **Cod Berthold Technologies** - https://github.com/lnls-sirius/stream-ioc/blob/master/interface/Berthold-LB6420.py.

BeagleBone Black has a UDP server and communicates with EPICS Archiver through the StreamIOC tool.

-  **Git StreamIOC** - https://github.com/lnls-sirius/stream-ioc

## PV List

All PV names are listed below:

.  RAD:ELSE:Gamma
.  RAD:ELSE:Neutron
.  RAD:ELSE:TotalDoseRate
.  RAD:ELSE:DoseIntegral
.  RAD:ELSE:IntegralGamma
.  RAD:THERMO:Gamma
.  RAD:THERMO:Neutron
.  RAD:THERMO:TotalDoseRate
.  RAD:THERMO:DoseIntegral
.  RAD:THERMO:IntegralGamma
.  RAD:THERMO:IntegralNeutron
.  RAD:Berthold:Gamma
.  RAD:Berthold:TotalNeutronRate
.  RAD:Berthold:TotalDoseRate
.  RAD:Berthold:HighEnergyNeutrons
.  RAD:Berthold:DoseIntegral
.  RAD:Berthold:IntegralGamma
.  RAD:Berthold:IntegralNeutron

Ps.: The Berthold probe, in addition to the cited PVs, there is a dose measurement due to fast neutrons displayed on the second screen (RAD:Berthold:HighEnergyNeutrons).

**Inquieries:** aureo.carneiro@lnls.br
