---
title: UVX high level application list
description: 
published: 1
date: 2024-03-19T20:00:04.448Z
tags: 
editor: markdown
dateCreated: 2024-03-19T19:52:26.730Z
---

# FAC: UVX high level application list

## Monitoring and control
This category includes applications for monitoring, manually setting and automatically controlling machine parameters; alarms and machine snapshots are also included.

### Monitoring
Screens with read-only data:
* General storage ring information: beam current, sizes, tune, and lifetime
* General booster and transport lines information: status, injection
* General linac information: status
* Orbit distortion and power supplies
* RF system
* Vacuum system
* Machine and personal protection
* Alarms

### Manual and automatic control
Operator interfaces for reading and setting parameter values, and high level physics applications
* Insertion device control
* Tune measurement
* RF system (electronics)
* Power supply diagnostics
* Temperature controllers
* Beam size measurement (transverse and longitudinal)
* Timing system
* Machine snapshot
* Vacuum system (including valves)
* Injection
* Operations manager (configuration)

For specific machine subsystem parameters, a hierarchical structure, such as in the current UVX operations program, could be used. This contains:

**Storage ring**

* Magnets
* Pulsed magnets (including PMM)
* Electrodes
* Optics
  * Mode (including single bunch)
  * Tune control
  * Chromaticity control
  * Position and angle
* Gamma shutter control
* Storage ring access light
* Orbit correction (SOFB (?) and high level interface to FOFB)
* RF cavities
* Scrapers

**Booster**

* Magnets
* Pulsed magnets
* Electrodes
* Optics
  * Tune control
  * Chromaticity control
  * Position and angle
* Ramping
* Orbit correction
* RF cavities

**Transport line**

* Magnets
* Monitors
* Optics
  * Position and angle
    * Storage ring injection
    * Booster injection

**Linac**

* Magnets
* Gun
* Monitors
* RF

## Data archiving, visualisation and analysis
This category includes applications for archiving, visualising and analysing machine parameters.

* Archiver
* Visualisation and analysis: IGOR Pro

## Operations and maintenance management
This category includes applications for logging relevant operation and maintenance events (manually and automatically), generating reports (machine performance and metrics), supplying machine information to users and members of the external community, and databases and applications for storing and retrieving equipment and control system information.

* Logbook: logging events manually and automatically, and generating reports with light source performance data and metrics
* Equipment and parameter database: list of all equipment installed in control system, with location and available parameters
* Machine information: supplying machine information and operator messages to users and the external community
