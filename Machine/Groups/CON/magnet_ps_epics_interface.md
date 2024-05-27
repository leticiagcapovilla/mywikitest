# CON: Magnet power supplies EPICS interface

## Introduction

This page will contain some documentation about the EPICS interface for Sirius magnet power supplies. The software is under development by [LNLS Controls Group](/Machine/Groups/CON).

All power supplies of the storage ring, booster and transport lines will have the EPICS interface described here. For information about Linac magnet power supplies, please read the page [Linac control system documentation](/Machine/Groups/CON/linac_control_system).

## Magnets cycling procedure

Magnet cycling is the procedure used for eliminating residual magnetism from magnets. It is always executed when there is no beam in the machine, usually just before the beginning of the injection process. Cycling consists in running a previously defined and virtually immutable curve on the power supply that drives the coils of the magnet.

As of February 2018, cycling curves for Sirius magnets have not been specified yet. In UVX, most of them have the shape of a trapezoid or a damped sine wave. Parameters of the curve (amplitude, duration, decay constant and others) depends on the magnet.

The EPICS IOC of power supplies will always load the parameters of the cycling curves from a configuration database at boot. So the user or operator should not worry about the curve configuration.

The procedure for magnets cycling is:

* Change the operation mode of the power supply (PV **<power_supply_name>:OpMode-Sel**) that drives the magnet to **Cycle**. After changing the operation mode of the power supply to **Cycle**, make sure this action was successful by reading the operation mode from the power supply (PV **<power_supply_name>:OpMode-Sts**).

* Change the operation mode of the serial network associated with the power supply to **Sync**.

* Drive the timing system in such a way that it will deliver one pulse to the power supply.

## Booster ramping procedure

## Storage ring migration procedure

## Slow orbit feedback (SOFB) procedure
