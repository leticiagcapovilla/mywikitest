---
title: EPICS clients on Windows
description: 
published: 1
date: 2024-06-06T16:56:53.329Z
tags: 
editor: markdown
dateCreated: 2024-06-06T16:54:54.582Z
---

# CON: EPICS clients on Windows

<br>

## Introduction

This page is a tutorial on how to set up and use some EPICS clients on a Windows environment.

Linux is widely used at [Controls Group](/Machine/Groups/CON) for project developments, and is the recommended operating system for most of our tasks. Nevertheless, there are many computers at LNLS running Windows. So here is a guide on how to configure a Windows-based environment in a way that it could interact with all [[Machine:Control_System|control system]] applications. This page provides instructions on how to work with EPICS software on Windows also.

Although the instructions below may work with other Windows versions, all of them were tested only on a fresh Windows 10 installation.

<br>

## EPICS Windows Tools

EPICS Windows Tools is an EPICS distribution for Windows which packages some Channel Access command-line tools (such as caget, camonitor and caput) and libraries (DLLs), along with a few EPICS extensions (Alarm Handler, MEDM, StripTool and others). All these stuff can be easily installed on Windows through an MSI installer, which can be download from the links below:

* [EPICS Windows Tools installer for 32-bit machines](https://epics.anl.gov/download/distributions/EPICSWindowsTools1.44-x86.msi){target=_blank}
* [https://epics.anl.gov/download/distributions/EPICSWindowsTools1.44-x64.msi EPICS Windows Tools installer for 64-bit machines](){target=_blank}

Latest Windows Tools release (1.44) comes with EPICS Base 3.14.12.4. Although our standard EPICS Base version at the moment is 3.15.5, the reader should not experience any problems while working with EPICS Windows Tools 1.44.

In order to run the graphical EPICS extensions bundled with Windows Tools, an X server is required. VcXsrv is a good free and open-source X server for the Windows environment. Download links for VcXsrv installers are the following:

* [VcXsrv installer for 32-bit machines](https://ufpr.dl.sourceforge.net/project/vcxsrv/vcxsrv/1.19.6.0/vcxsrv.1.19.6.0.installer.exe){target=_blank}
* [VcXsrv installer for 64-bit machines](https://ufpr.dl.sourceforge.net/project/vcxsrv/vcxsrv/1.19.6.0/vcxsrv-64.1.19.6.0.installer.exe){target=_blank}

<br>

## LabVIEW

As LabVIEW for Windows is available at CNPEM, it can be used as an EPICS client of control system applications. First, download the most updated version of [this link](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/downloads_en.html){target=_blank}.

After download run the file and perform the installation, integrating the directory in which LabVIEW is installed.

Restart the computer.

Open the directory to which LabVIEW belongs and check the user.lib folder if the caLab directory belongs to it. If it does not contain the file, perform the installation again in the correct directory. If you have the files, take the next step.

Open the LabVIEW executable and a Blank VI then execute the following instructions:

```
>> Select Tools -> Advanced -> Mass Compile
>> Choose CA Lab directory in your\Path\to\LabVIEW\user.lib\caLab and click the "Select" button
>> Click the "Mass Compile" button
>> Finish with "Done" button
```

Start your first test, by choosing "startDemo" from Start:

```
>> Programs -> National Instruments -> caLab -> "start Demo"
```

This will do following:

```
>> Start a demo IOC Shell with prepared test variables
>> Write random values to those variables
>> Monitors those variables
>> Shows currently used EPICS context
```

If everything works correctly the installation was a success.

Set the environment variables on Windows.

```
>> EPICS_CA_AUTO_ADDR_LIST ##  NO
>> EPICS_CA_ADDR_LIST ##  10.0.6.57 
```

Open the ReadDemo.VI file in the examples in the caLab folder. Enter the name of your PV Epics, run the looped VI, and verify that the reading occurs correctly.

To use the blocks belonging to the caLab library, perform the following steps:

```
>> Select Functions -> User Libraries -> caLab
```

The links below explain the parameters of the caLab library blocks to read and write a PV Epics.

```
>> [Get PV Epics](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/vis/get_en.html){target=_blank}
>> [Put PV Epics](https://www.helmholtz-berlin.de/zentrum/locations/it/software/exsteuer/calab/vis/put_en.html){target=_blank}
```

All instructions presented in this section were tested only on LabVIEW 2010 or superior.

<br>

## MATLAB

Using MATLAB as an EPICS client on Windows is easy. First, download the package [ca_matlab](https://github.com/channelaccess/ca_matlab){target=_blank} through [this link](https://github.com/channelaccess/ca_matlab/releases/download/1.0.0/ca_matlab-1.0.0.jar){target=_blank}. Inside MATLAB, the file can be downloaded to the working directory with:

```
>> websave('ca_matlab-1.0.0.jar', 'https://github.com/channelaccess/ca_matlab/releases/download/1.0.0/ca_matlab-1.0.0.jar');
```

Before interacting with EPICS process variables, it is necessary to load the downloaded library:

```
>> javaaddpath('ca_matlab-1.0.0.jar');
```

Then use the following code to initialize the EPICS client module:

```
>> import ch.psi.jcae.*;
>> ca_properties = java.util.Properties();
>> ca_properties.setProperty('EPICS_CA_ADDR_LIST', '10.0.4.57');
>> ca_properties.setProperty('EPICS_CA_AUTO_ADDR_LIST', 'NO');
>> ca_properties.setProperty('EPICS_CA_MAX_ARRAY_BYTES', '1048576');
>> ca_context = Context(ca_properties);
```

Now it's time to create channels. Each EPICS PV should be mapped into a channel. The example below creates a monitored channel for the PV '''LNLS:ANEL:corrente''':

```
>> machine_current = Channels.create(ca_context, ChannelDescriptor('double', 'LNLS:ANEL:corrente', true));
```

A monitored channel is useful when the user wants to request the value of an EPICS PV periodically. When monitoring a channel, the library always caches the most recent value of the PV, and this value can be obtained with the get() method:

```
>> machine_current.get()
```

Otherwise, when a non-monitored channel is instantiated, the library will access the network to obtain the current PV value every time the method get() is called.

Currently we recommend using ca_matlab instead of the other two MATLAB Channel Access client interfaces listed on [EPICS official web site](https://epics.anl.gov/extensions/index.php){target=_blank} (labCA and MCA). This is because ca_matlab is written in Java and released as a ready to use and operating system independent package. labCA and MCA need to be built when downloaded, and this installation procedure is not straightforward.

More information about ca_matlab can be found on its documentation, available at [GitHub.com](https://github.com/channelaccess/ca_matlab){target=_blank}.

The reader should keep in mind that ca_matlab can only be used for on-line interaction with EPICS PVs. Instructions for reading previous PV data from the archiving system (EPICS Archiver Appliance) will be added to this section soon.

All instructions presented in this section were tested only on MATLAB R2016b.

<br>

## Python

[Pyepics](http://cars9.uchicago.edu/software/python/pyepics3/){target=_blank} is a very useful Python module for writing EPICS client programs in Python.
