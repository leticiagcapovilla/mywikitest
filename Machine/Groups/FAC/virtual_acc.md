---
title: Virtual accelerator
description: 
published: 1
date: 2024-05-17T20:36:41.057Z
tags: 
editor: markdown
dateCreated: 2024-03-05T21:50:53.503Z
---

# FAC: Virtual accelerator

A virtual accelerator (VA) with an EPICS interface is being developed for testing high level applications and will be integrated with the Sirius control system. Code is in the [va repository](https://github.com/lnls-fac/va).

**Architecture**

With a direct EPICS Channel Access (CA) interface, using the PCAS library, the VA can be used as a tool for developing and testing high level applications (HLA) and operator interfaces (OPI). This is also a possible solution for serving model data during Sirius operations and commissioning.

Simple VIOCs (virtual IOCs) are used to supply model parameters through their EPICS PV names, as defined in the naming system. For the model, [SWIG](http://swig.org/) was used to generate a [Python module](https://github.com/lnls-fac/trackcpp/tree/master/python_swig_module) from the in-house developed FAC:Trackcpp. A Channel Access server on top of the model (using pcaspy) provides the EPICS access to model data. 

Image

**Use**

The VA can be started by running the `sirius-vaca.py` script, optionally passing an EPICS PV prefix as an argument (default is "VA-"). The auxiliary script `sirius-va` (available in the [scripts](https://github.com/lnls-fac/scripts) repository) can be used to start all virtual IOCs (VIOCs) with a single command, by issuing `sirius-va start viocs`. To stop the VIOCs, issue `sirius-va stop viocs`. For procedures to start the VA and set necessary EPICS environment variables, look at the following sections of the [FAC:Cookbook](/home/Groups/FAC/cookbook):

* [Start the virtual accelerator](/home/Groups/FAC/cookbook#start-the-virtual-accelerator)
* [Set Channel Access environment variables](/home/Groups/FAC/cookbook#set-channel-access-environment-variables)

~~**Development and testing environment**~~

~~The hla-vagrant repository contains files for setting up a development and testing environment for the VA and clients using Vagrant and SaltStack (see Setting up the development and testing environment.)~~

