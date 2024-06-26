---
title: Radiation Protection Software Supervisor
description: 
published: 1
date: 2024-06-03T16:00:16.796Z
tags: 
editor: markdown
dateCreated: 2024-05-29T15:10:29.737Z
---

# CON: Radiation protection software

<br>

## Introduction
This page will contain documentation about the EPICS IOC for radiation protection equipments at Sirius building.

Three radiation monitoring systems (from different manufacturers) were bought for evaluation. Controls group is working on remote interfaces for these equipments. They will be tested during Sirius Linac comissioning (scheduled to start in March 2018).

<br>

## Project description
The supervisory was developed with the purpose of performing the radiological area monitoring in the Sirius facilities. The supervisor is easy to see and to interpret the data. The system compares the reading of different probes in different regions. Each device performs dose readings in uSv / h.

On the main frame of the supervisory we have an overview of all the PV's in two dynamic screens. The readings are performed by the following probes:

-  **Else Nuclear** - Saturn II 5702 containing an ICP-T-PF gamma detector and a LUPIN 5401 BF3-NP neutron detector;
-  **ThermoFisher Scientific** - FHT 6020 containing a FHT 192-10 gamma detector and a FHT 762 neutron detector;
-  **Berthold Technologies** - LB 6420 Dose Meter For Measuring Pulsed Radiation.

The name of the PV consists of RAD, symbolizing the domain of the radiation protection department, followed by the name of the detector manufacturer and, finally, the variable addressed. Gamma radiation dose, neutron dose and total dose (sum of neutron dose and gamma dose) and integrated dose in 4h are performed. Two lines were inserted into the graphs representing the limit for the integrated dose (2uSv) and the mean value for the background.

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

In the second frame on the main frame of the supervisory we see a graph containing lines with the values of the instantaneous dose measurements in uSv / h as a function of time. The first frame contains the readings of the PVs related to the integrated doses in 4h. The integrated dose is the dose that has been achieved within the last four hours, obtained by the trapezoidal method that makes use of the instantaneous measurement and time difference for the calculation.

There are interactive buttons and a legend relating the name of the PV, its value read instantly and the color of the line referring to that PV on the main frame. The buttons allow to open in a new frame the enlargement of each frame for better visualization, opening of a WEB page directed to the ‘Archiver EPICS’ and the access to a configuration menu. The new frames have a button to came back to main frame.

<br>

## Download

The software can be downloaded through GitHub and only need to be downloaded and run with Control System Studio is a graphical tool based on Eclipse which offers many features to monitor and to operate controls systems, being maintained continuously and improved by developers from many laboratories and teaching institutes. Between the projects contained in the CSS repository, one of the them allows the generation of local and customised distributions according to the needs of the respective laboratory. This project, called org.csstudio.product, was, therefore, extended and modified to meet only our group's needs.

For more information see the [Control System Studio](https://wiki-sirius.lnls.br/mediawiki/index.php/CON:Lnls-studio) page on the [Wiki-Sirius](https://wiki-sirius.lnls.br/)

**Inquieries:** aureo.carneiro@lnls.br
