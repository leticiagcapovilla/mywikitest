# CON: Pulsed magnets EPICS interface

## Introduction
This page will contain some documentation about the EPICS interface for [Sirius pulsed magnets](/Machine/pulsed_magnets). The software is under development by [[CON:CON|LNLS Controls Group]].

Pulsed magnets will be interfaced by two applications:
* [[CON:Stream-IOC|Stream-IOC]](link). By now we are adding support for the pulsed magnets controller units on [[CON:Stream-IOC|Stream-IOC]](link).
* An IOC for the oscilloscopes that will be used for acquiring the current profile of pulses. As of November 2017, we are still selecting an oscilloscope manufacturer and model for this.

## Pulsed magnets controller unit PVs

The PVs below will be associated with each of Sirius pulsed magnets controller units. "<prefix>" is the "Sec-Sub:Dis-Dev[-Idx]" part of our [PV naming system convention](/Machine/naming_system).


**<prefix>:Voltage-SP** - high voltage power supply output (setpoint).

**<prefix>:Voltage-RB** - high voltage power supply output (readback).

**<prefix>:Voltage-Mon** - high voltage power supply output (monitoring).


Range of these three voltage PVs depends on the pulsed magnet, and will be defined on the proper EPICS record fields.


**<prefix>:PwrState-Sel** - one of {Off|On} (setpoint).


**<prefix>:CtrlMode-Sts** - one of {Local|Remote} (monitoring).


**<prefix>:Pulse-Sel** -  one of {Off|On} (setpoint); this defines if the device will accept pulses from the timing system or not.


**<prefix>:Intlk0-Mon** - interlock signal 0 ({Fail|Normal}, monitoring).

**<prefix>:Intlk1-Mon** - interlock signal 1 ({Fail|Normal}, monitoring).

**<prefix>:Intlk2-Mon** - interlock signal 2 ({Fail|Normal}, monitoring).

**<prefix>:Intlk3-Mon** - interlock signal 3 ({Fail|Normal}, monitoring).

**<prefix>:Intlk4-Mon** - interlock signal 4 ({Fail|Normal}, monitoring).

**<prefix>:Intlk5-Mon** - interlock signal 5 ({Fail|Normal}, monitoring).

**<prefix>:Intlk6-Mon** - interlock signal 6 ({Fail|Normal}, monitoring).


**<prefix>:Intlk0Label-Cte** - interlock signal 0 label (constant): "External"

**<prefix>:Intlk1Label-Cte** - interlock signal 1 label (constant): "HVPS Overvoltage"

**<prefix>:Intlk2Label-Cte** - interlock signal 2 label (constant): "HVPS Overcurrent"

**<prefix>:Intlk3Label-Cte** - interlock signal 3 label (constant): "Personnel protection"

**<prefix>:Intlk4Label-Cte** - interlock signal 4 label (constant): "Temperature"

**<prefix>:Intlk5Label-Cte** - interlock signal 5 label (constant): "AC CPFL OFF"

**<prefix>:Intlk6Label-Cte** - interlock signal 6 label (constant): "Switch Module"


**<prefix>:Reset-Cmd** - this PV is used to reset the controller unit.


There will be one control hardware shared between two pulsed magnets: storage ring on-axis and non-linear kickers. For this system, a special PV determines its mode of operation:


**<prefix>:OpMode-Sel** - one of {OnAxis|NonLinear} operation modes (setpoint).

**<prefix>:OpMode-Sts** - one of {OnAxis|NonLinear} operation modes (readback).


Each of the other pulsed magnets will have its own control hardware.

## Remote operation of oscilloscopes

Currently we are evaluating some manufacturers and models of oscilloscopes for acquiring the current pulses. Their system will be based on Windows, so controlling them through a remote desktop client will be possible. An EPICS interface for these oscilloscopes is being considered as well.
