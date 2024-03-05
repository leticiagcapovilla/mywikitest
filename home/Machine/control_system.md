---
title: Control System
description: 
published: 1
date: 2024-03-05T19:03:24.155Z
tags: 
editor: markdown
dateCreated: 2024-03-05T18:55:00.249Z
---

# Machine: Control System

<br />

## Introduction

Sirius control system consists of a hardware/software solution that will provide a complete and reliable distributed system for supervision, data acquisition and control of the machine.

This page is a synopsis of all the content related to Sirius control system. Additional pages contain detailed information about each topic cited here.

<br />

## General architecture of the control system

The figure below shows a conceptual overview of the control system architecture.

![Sirius_control_system_architecture.png](/img/machine/control_system/Sirius_control_system_architecture.png)

Next to the accelerator components, there are various types of hardware that interact with them, collecting information or providing configuration parameters and setpoints. These hardware entities consists of in-house developments or commercial equipments, and will implement all fast closed-loop controls. They will communicate to upper levels of the control system through serial interfaces (RS-485, RS-232) or Ethernet.

The serial communication to low-level hardware will be performed by [[CON:Sirius_control_system_SBCs|single-board computers (SBCs)]], each of them controlling one or more devices. By now, our choice of single-board computer model is BeagleBone Black, a low-cost SBC with real-time capabilities that runs Linux operating system. These boards will execute EPICS server applications, which will interoperate between the EPICS Channel Access protocol (over Ethernet) and hardware communication protocols (over RS-485 or RS-232).

Some local hardware interfaces, like the LINAC control hardware, will have an Ethernet connection available with a built-in EPICS Input/Output Controller (IOC). There may be also devices with only Ethernet as a communication interface, but without bult-in EPICS software. For them, a Linux-powered SBC or workstation, located anywhere at the building, will run a corresponding EPICS server application.

EPICS was chosen as the default control software platform. Current server-side software development consists of traditional IOCs and Channel Access servers. At the moment we have worked only with 3.14.12 series of EPICS releases.

A high-performance computer network infrastructure will connect all SBCs and other devices which run server-side EPICS software to client-side applications ([[Machine:High_Level_Applications_and_Virtual_Accelerator|high level applications]]). These will consist of operator interfaces (computer software with graphical interfaces to read/write EPICS process variables), a data archiver application (for storage and retrieval of variable values history) and an alarm handling application (essential for notifying operators of anormal events), among others.

<br />

## In-house hardware design

Some groups at LNLS are developing hardware solutions for Sirius. In order to standardize communication to all these hardware, [[CON:CON|CON]] developed a lightweight application layer protocol named [[CON:Basic_Small_Messages_Protocol_(BSMP)|Basic Small Messages Protocol (BSMP)]]. It may be used over several communication links (current uses are over RS-485 and Ethernet).

[[CON:CON|Controls group]] is responsible for the development of [[CON:PUC|general-purpose analog and digital hardware control interfaces]], an [[CON:CON_Serial_Cape|adapter board with UARTs for BeagleBone Black]] and a [[CON:MBTemp|module for reading temperature data from Pt100 sensors]].

<br />

## Software development and computer network

As mentioned before, EPICS is the default software environment for exchange of data between client and server control applications. See [[CON:Sirius_control_system_interfaces|Sirius control system interfaces]] for more information about server-side EPICS software, its conventions and how they are related to hardware devices.

This Wiki also have a page dedicated to [[Machine:High_Level_Applications_and_Virtual_Accelerator|Sirius high level applications]].

[[CON:Sirius_control_system_network|Sirius control system network]] contains all the details about control system underlying computer network.

<br />

## [[Machine:Power Supply IOCs|Power Supply IOCs]]
{{Machine:Power Supply IOCs}}

<br />

## [[Machine:BPM IOCs|BPM IOCS]]
{{Machine:BPM IOCs}}

<br />

##  [[Machine:Timing Devices IOCs| Timing Devices IOCs]] 
{{Machine:Timing Devices IOCs}}

<br />

##  [[Machine:High Level Timing IOC | High Level Timing IOC]] 
{{Machine:High Level Timing IOC}}
