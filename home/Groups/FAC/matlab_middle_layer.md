---
title: Matlab Middle Layer
description: 
published: 1
date: 2024-03-05T20:55:22.584Z
tags: 
editor: markdown
dateCreated: 2024-03-05T20:55:22.584Z
---

# FAC: Matlab Middle Layer

MatlabMiddleLayer (**MML**) is a Matlab package containing a set of scripts and data structures that are used to 1) map an AT simulation model into the real machine and 2) perform process variable readouts and setpoint modifications. It is a software layer between the machine control system (LNLS1Link for UVX, EPICS for Sirius) on the bottom and high-level machine study algorithms or routine operations on the top. MML's basic data structures can be accessed from Matlab workspace through two functions: `getao` (accelerator object) and `getad` (accelerator data). Parametrization of these two structures is done through other scripts which have to be tailored for each machine in particular. 

## Available functionality

There is an MML manual in Release/mml/docs, and there are functions in Release/mml. Two of the main GUI applications are `plotfamily` and `mmlviewer`, from which other major scripts may be accessed. Matlab command `help mml` is another source of information on MML. 

**Reading and writing values**

The basic functions for reading and writing PV values are `getpv`, `setpv`, and related functions (starting with `get`, `set`, and `step`). Mode (online/simulation) and units (Physics/hardware) can be selected using the functions starting with `switch`.

**LOCO**

LOCO documentation is available in Release/applications/loco/Documentation. 

## Using labCA

The [labCA](http://www.slac.stanford.edu/~strauman/labca/index.html) package allows setting and getting EPICS process variable values using MATLAB. It is available in Release/links/labca and must be compiled prior to use.

**Compilation**

A makefile is provided for compilation. It may be necessary to set the EPICS_BASE and MATLAB_DIR variables in Release/links/labca/configure/RELEASE to the EPICS Base and MATLAB directories, respectively. To compile and install files, issue `make` inside Release/links/labca.

**Installing LabCA**

- Get last version of LabCA from: LabCA Website
- To build from source: 
 -- go to source folder
 -- in labca/configure/CONFIG set MAKEFOR=MATLAB, CONFIG_USE_CTRLC=YES (optional configuration)
 -- set in labca/configure/RELEASE:
      `INSTALL_LOCATION_APP=/home/facs/repos/MatlabMiddleLayer/Release/links/labca/`
      `EPICS_BASE=/opt/epics/base`
      `MATLABDIR=/usr/local/MATLAB/R2016b`
 -- check if EPICS_HOST_ARCH environment variable is defined, if it is not, define it
 -- in source folder: make clean; make