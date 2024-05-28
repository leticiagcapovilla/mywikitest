---
title: Pulsed magnets EPICS interface
description: 
published: 1
date: 2024-05-28T20:35:13.095Z
tags: 
editor: markdown
dateCreated: 2024-05-28T20:34:37.473Z
---

# CON: Pulsed magnets EPICS interface

## Introduction
This page will contain some documentation about the EPICS interface for [Sirius pulsed magnets](/Machine/pulsed_magnets). The software is under development by [[CON:CON|LNLS Controls Group]].

Pulsed magnets will be interfaced by two applications:
* [[CON:Stream-IOC|Stream-IOC]](link). By now we are adding support for the pulsed magnets controller units on [[CON:Stream-IOC|Stream-IOC]](link).
* An IOC for the oscilloscopes that will be used for acquiring the current profile of pulses. As of November 2017, we are still selecting an oscilloscope manufacturer and model for this.

## Pulsed magnets controller unit PVs

The PVs below will be associated with each of Sirius pulsed magnets controller units. "<Prefix>" is the "Sec-Sub:Dis-Dev[-Idx]" part of our [PV naming system convention](/Machine/naming_system).


**<Prefix>:Voltage-SP** - high voltage power supply output (setpoint).

**<Prefix>:Voltage-RB** - high voltage power supply output (readback).

**<Prefix>:Voltage-Mon** - high voltage power supply output (monitoring).


Range of these three voltage PVs depends on the pulsed magnet, and will be defined on the proper EPICS record fields.


**<Prefix>:PwrState-Sel** - one of {Off|On} (setpoint).


**<Prefix>:CtrlMode-Sts** - one of {Local|Remote} (monitoring).


**<Prefix>:Pulse-Sel** -  one of {Off|On} (setpoint); this defines if the device will accept pulses from the timing system or not.


**<Prefix>:Intlk0-Mon** - interlock signal 0 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk1-Mon** - interlock signal 1 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk2-Mon** - interlock signal 2 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk3-Mon** - interlock signal 3 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk4-Mon** - interlock signal 4 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk5-Mon** - interlock signal 5 ({Fail|Normal}, monitoring).

**<Prefix>:Intlk6-Mon** - interlock signal 6 ({Fail|Normal}, monitoring).


**<Prefix>:Intlk0Label-Cte** - interlock signal 0 label (constant): "External"

**<Prefix>:Intlk1Label-Cte** - interlock signal 1 label (constant): "HVPS Overvoltage"

**<Prefix>:Intlk2Label-Cte** - interlock signal 2 label (constant): "HVPS Overcurrent"

**<Prefix>:Intlk3Label-Cte** - interlock signal 3 label (constant): "Personnel protection"

**<Prefix>:Intlk4Label-Cte** - interlock signal 4 label (constant): "Temperature"

**<Prefix>:Intlk5Label-Cte** - interlock signal 5 label (constant): "AC CPFL OFF"

**<Prefix>:Intlk6Label-Cte** - interlock signal 6 label (constant): "Switch Module"


**<Prefix>:Reset-Cmd** - this PV is used to reset the controller unit.


There will be one control hardware shared between two pulsed magnets: storage ring on-axis and non-linear kickers. For this system, a special PV determines its mode of operation:


**<Prefix>:OpMode-Sel** - one of {OnAxis|NonLinear} operation modes (setpoint).

**<Prefix>:OpMode-Sts** - one of {OnAxis|NonLinear} operation modes (readback).


Each of the other pulsed magnets will have its own control hardware.

## Remote operation of oscilloscopes

Currently we are evaluating some manufacturers and models of oscilloscopes for acquiring the current pulses. Their system will be based on Windows, so controlling them through a remote desktop client will be possible. An EPICS interface for these oscilloscopes is being considered as well.
