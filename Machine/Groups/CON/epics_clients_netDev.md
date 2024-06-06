---
title: EPICS clients on netDev for Yokogawa PLC
description: 
published: 1
date: 2024-06-06T16:58:13.066Z
tags: 
editor: markdown
dateCreated: 2024-06-06T16:54:56.897Z
---

# CON: EPICS clients on netDev

## Introduction

This page is a tutorial on how to set up and use some EPICS clients with netDev for Yokogawa PLC. All netDev EPICS interfaces created by LNLS Controls Group for Sirius control system will be contained in this application.

## System Requirements

In order to get this software running, you should have installed in your system EPICS base (version 3.14). NetDev-ioc is intended to run in a Linux environment.

## Installation of EPICS Base

Although EPICS R3.15 is the default EPICS version adopted at LNLS Controls Group by now, some applications may not be able to work with the R3.15 series of EPICS releases. So keeping the latest release of EPICS Base R3.14 in the system is necessary to work around this problem. For instance, we use [http://www-linac.kek.jp/cont/epics/netdev/ netDev] and [https://ics-web.sns.ornl.gov/kasemir/etherip/ EtherIP] only with EPICS R3.14.

Below are the instructions for installing EPICS Base R3.14.12.7:

 # cd /opt
 # mkdir epics-R3.14.12.7
 # cd epics-R3.14.12.7
 # wget <nowiki>https://epics.anl.gov/download/base/baseR3.14.12.7.tar.gz</nowiki>
 # tar -xvzf baseR3.14.12.7.tar.gz
 # rm baseR3.14.12.7.tar.gz
 # mv base-3.14.12.7 base
 # cd base
 # make
<section end=AlternativeEPICSBaseInstallation /><section begin=netDevInstallation />

## Instalation of netDev and GitHub repository

#### Git Instalation:

The repository should be cloned with this command:

  $ git clone https://github.com/lnls-sirius/netDev-ioc.git

Here is a brief explanation of the directory structure:

* database - Contains files with record definitions for all devices this application supports.

* sequencer - Folder with Sequencer of Python for communication between the EPICS IOC and some devices. An interface program may create a file with the ".data" extension in this directory, which will be used to store configuration parameters of the interface software or the controlled hardware.

* iocBoot - Directory where the IOC initialization scripts reside. These files must be properly configured, as described at the "Executing the IOC" section.

* netDev-1.0.3 - NetDev version 1.0.3.

#### Terminal Instalation:

[http://www-linac.kek.jp/cont/epics/netdev/ netDev] is an useful module for writing IOCs for Yokogawa programmable logic controllers. Below are the steps for netDev latest release (1.0.3) installation:

 # cd /opt/epics-R3.14.12.7
 # mkdir modules
 # cd modules
 # wget <nowiki>http://www-linac.kek.jp/cont/epics/netdev/netDev-1.0.3.tar.gz</nowiki>
 # tar -xvzf netDev-1.0.3.tar.gz
 # rm netDev-1.0.3.tar.gz
 # sed -i -e '18cEPICS_BASE=/opt/epics-R3.14.12.7/base' netDev-1.0.3/configure/RELEASE
 # cd netDev-1.0.3
 # make
<section end=netDevInstallation /><section begin=EtherIPInstallation />

## Compiling

This software is distributed in the form of source code. In order to compile it, first define at the `install.sh` file the system paths to EPICS base and your netDev-ioc folder on "TOP". By default, these configurations are:

  $ sed -i -e '18cEPICS_BASE=/opt/epics-R3.14.12.7/base' netDev-1.0.3/configure/RELEASE

After editing `install.sh`, run these commands at the top directory:

  ./install.sh

During installation, the system prompts you for a folder creation name. Give a name at your discretion and proceed with your installation.

## Uninstalling

To remove this software from a computer, just delete its parent directory.

PS: Check your execution paths from the .cmd file to run the IOC.
