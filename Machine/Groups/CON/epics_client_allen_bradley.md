---
title: EPICS clients on Rockwell - Allen Bradley PLC with EtherIP
description: 
published: 1
date: 2024-06-06T17:04:58.926Z
tags: 
editor: markdown
dateCreated: 2024-06-06T16:54:52.256Z
---

# CON: EPICS clients on Allen Bradley PLC

<br>

## Introduction

This page is a tutorial on how to set up and use some EPICS clients on Rockwell - Allen Bradly PLC.

The requirement for implementation is that the PLC has access to EPICS network with ethernet connection with etherIP module with the following specifications:

```
>> EtherIP "driver / device support module for EPICS.
>> Allen Bradley PLCs (see www.ab.com) via Ethernet to EPICS IOCs
>> ControlLogix 5000, both original versions with separate controller and ENET module, and L8x series that includes a network port in the controller.
>> Support EPICS R3.14.8 and higher. For an earlier version of EPICS base, including R3.13, see tags older than ether_ip-3-0.
```

For the present tutorial it is recommended to use an opracional Linux system.

<br>

## Installation of EPICS Base

The [EPICS official web site](http://www.aps.anl.gov/epics/base/){target=_blank} presents a good description of what is EPICS Base:

*"This is the main core of EPICS, comprising the build system and tools, common and OS-interface libraries, Channel Access client and server libraries, static and run-time database access routines, the database processing code, and standard record, device and driver support."*

Currently we work only with the 3.15 series of EPICS Base releases (stable releases of EPICS V3). Latest offer from this branch is R3.15.5. To install EPICS Base in */opt*, just execute the commands below:

```
# apt-get -y install libreadline-gplv2-dev
# cd /root
# wget https://epics.anl.gov/download/base/baseR3.14.12.7.tar.gz
# tar -xvzf baseR3.14.12.7.tar.gz 
# rm baseR3.14.12.7.tar.gz 
# cd base-3.14.12.7
# make
```

It's convenient to add EPICS binaries directory to the system path and set other two environment variables. Edit the file */root/.bashrc*, adding at the end of the file:

```
export PATH=/root/base-3.14.12.7/bin/linux-x86_64:$PATH
export EPICS_BASE=/root/base-3.14.12.7
export EPICS_HOST_ARCH=linux-x86_64
export EPICS_CA_MAX_ARRAY_BYTES=1048576
export EPICS_CA_ADDR_LIST=10.0.4.57
```

To apply these settings to the current session, enter:

```
# source /root/.bashrc
```

Setting environment variables with information about EPICS Base is required for all users that will work on this platform. So the steps above should be repeated with the *.bashrc* file on each of these users home directories.

10.0.4.57 is the IP address of the computer at UVX control room that runs [EPICS PV Gateway](http://www.aps.anl.gov/epics/extensions/gateway/index.php){target=_blank} to provide (read) access to accelerator process variables. These variables are published only in a separate, application-specific computer network (UVX control system newtork). We use the PV Gateway to access accelerator control system PVs while working on office.

<br>

## Installation of EtherIP

Download the latest EPICS EtherIP tool release from [Github](https://github.com/EPICSTools/ether_ip/releases){target=_blank}.

Follow these steps:

```
# tar -xvzf ether_ip-ether_ip-2-27.tar.gz
# rm ether_ip-ether_ip-2-27.tar.gz
# cd ether_ip-ether_ip-2-27/configure/
```

Inside the ether_ip-ether_ip-2-27/configure folder open the "RELEASE " file with the nano text editor and change the PATH of your EPICS base by putting the following data:

```
>> EPICS_VER=master
>> EPICS_BASE_RELEASE=/root/base-3.14.12.7/
```

After the change, use the following commands:

```
# cd ..
# make
```

If everything happens correctly the installation was done successfully.

It is worth mentioning that it is recommended before the "Make" command check all PATHs in the Makefile files and check the legitimacy.

<br>

## Implementation

The EtherIP implementation consists of two steps. The first step is to mount a .db file in the following directory:

```
#  cd /root/ether_ip-ether_ip-2-27/db/
```

You can use the files already contained in the .db directory in order to create your own.
Your .db file should contain the PVs and Tag data (variable input or output and variable type (bollean, float, string)) that originated it.
Note the following field:

```
record (bi, "$(IOC):name_of_pv")
{
field (INP, "@$(PLC) name_of_tag")
}
```

In the location "name_of_pv" you will replace with the name you want to give your PV and in the place "name_of_tag" you will put the name of your PLC Tag. The "bi" element means that this variable is a bollen input.

After configuring .bd the next and last step is to configure your .cmd.
Run the following command:

```
#  cd /root/ether_ip-ether_ip-2-27/iocBoot/iocether_ip/
```

Use the st.cmd.host file to build on your .cmd file that you will create to configure for communication with the PLC.

To create your .cmd file use the following tutorial:

```
#! ../../bin/linux-arm/eipIoc
# 3.14 example startup file for a Host - * - shell-script - * -
# Load dbd, register the drvEtherIP .. commands
dbLoadDatabase ("../../dbd/eipIoc.dbd")
eipIoc_registerRecordDeviceDriver (pdbbase)
epicsEnvSet ("EPICS_IOC_LOG_INET", "127.0.0.1")
epicsEnvSet ("EPICS_IOC_LOG_PORT", "6505")
#iocLogInit
# Initialize EtherIP driver, define PLCs
EIP_buffer_limit (450)
drvEtherIP_init ()
EIP_verbosity (7)
drvEtherIP_define_PLC ("NAME OF PLC", "IP OF PLC", "MODULE OF PLC")
dbLoadRecords ("../../db/YOUR DATABASE", "PLC = YOUR PLC NAME, IOC = YOUR PV")
iocInit ()
```

After creating the .cmd file check the execute permission with ls -l, if necessary give chmod execution permission and finally execute the file.

<br>

## Repository etherip-ioc on git LNLS-SIRIUS

In LNLS we have our application in the git lnls-sirius repository that generates the .db and .cmd files for future implementations.

The repository link: [https://github.com/lnls-sirius/etherip-ioc](https://github.com/lnls-sirius/etherip-ioc){target=_blank}

In the README files of the repository teach cloning and use the repository and applications.
