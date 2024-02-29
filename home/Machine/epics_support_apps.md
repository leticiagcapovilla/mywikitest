---
title: EPICS Support Applications
description: 
published: 1
date: 2024-02-29T15:47:11.198Z
tags: 
editor: markdown
dateCreated: 2024-02-28T20:37:29.076Z
---

# Machine: EPICS Support Applications

##  Introduction 

This section will give an overview on the EPICS Support Applications that can be roughly divided in two groups:
1. **Relational Databases (RDB) Applications**
    
2. **Middlelayer Services**

Note that not all applications are in use by LNLS, but instead constitute a general panorama of Support Applications for 
EPICS-based control systems.

##  Links to Running Support Applications 

###  RBAC Service 
[link to RBAC service at lnls350-linux](https://10.0.7.55:8445) (available only within ABTLUS domain)

###  Naming Service 
[link to Naming service at lnls350-linux](http://10.0.7.55:8089) (available only within ABTLUS domain)

###  CCDB Service 
[link to CCDB service at lnls350-linux](http://10.0.7.55:8083) (available only within ABTLUS domain)

###  Cables Service 
[link to Cables service at lnls350-linux](http://10.0.7.55:8086) (available only within ABTLUS domain)

###  Archiver Service 
[link to Archiver service at Sirius Control System Servers](http://10.0.38.42) (available only within ABTLUS domain)

###  Web Server 
[link to Web Server at lnls350-linux](http://10.128.254.203) (available only within ABTLUS domain)

### Logbook Service
[link to Logbook service at Sirius Control System Servers](http://10.0.38.42/Olog) (available only within ABTLUS domain)

### Alarm Server
The alarm server component of BEAST is running at OPR24. For more information please refer to [this page][link].

##  Relational Databases (RDB) Applications 

This set of applications will compose the foundation of relation databases for storing information about the machine that will help both machine operation and short/long-term maintenance.
A list of possible RDB applications that may be deployed/developed can be found below.

###  Role-Based Access Control (RBAC) 

The RBAC application is used to give permission to selected services based on the users' login

[Official link](https://bitbucket.org/europeanspallationsource/rbac)

###  Controls Configuration Database (CCDB) 

**Description taken from ESS repositories**: https://bitbucket.org/europeanspallationsource/ccdb

The Controls Configuration Database (CCDB) enables the collection, storage, and distribution of
(static) controls configuration data needed to install, commission and operate the Sirius machine.

More specifically, the CCDB manages the information of thousands of (physical and logical) devices
such as cameras, PLCs, IOCs, racks, crates, etc…, that will be in operation at Sirius by defining
their properties and relationships between these from the control system perspective.

This information is then consumed both by end-users and other Support Applications 
(e.g. Cable Database, IOC Factory) to enable these to successfully perform their domain
specific businesses.

[Official link](https://bitbucket.org/europeanspallationsource/ccdb)

###  PV Naming Service (NS) 

The PV Naming Service helps users to adhere to Sirius PV naming convention defined here:
[Naming System][link]

[Official link](https://bitbucket.org/europeanspallationsource/naming-convention-tool)

###  Cables Database (CDB)  

The Cables Database (CDB) defines properties of all cables used to interconnect equipment.

[Official link](https://bitbucket.org/europeanspallationsource/cable-db)

###  IOC Factory 

**Description taken from ESS repositories**: https://bitbucket.org/europeanspallationsource/ioc-factory

The IOC Factory (FACT) is responsible for managing IOCs. It is designed to maximize the 
IOCs development productivity by providing a consistent and automated approach 
on how hundreds of IOCs are configured, generated, browsed and audited which would 
otherwise have to be performed manually.

By managing, it specifically means the following use cases:

1. Configure IOC
2. Generate IOC
3. Browse IOC
4. Audit IOC

The "Configure IOC" allows the user to select a set of EPICS modules for a certain IOC to use to effectively interface its devices. This election/configuration is stored in a persistence layer and it can later be used to generate the IOC. In principle, every time that the topology of the IOC evolves (i.e. the layout of devices that the IOC interface changes) the user creates a new configuration to cope with this evolution.

The "Generate IOC" allows the generation (i.e. building) of an IOC from scratch according to a certain configuration selected by the user. The generated IOC is stored in the official repository server for development or production, depending on what the user has selected. The information about the generation is stored in a persistence layer to enable the browse and audit IOC use cases.

The "Browse IOC" allows the user to retrieve, organize and display information about historical (i.e. past) generation of IOCs. It gives a broad view/understanding of when, how and why a certain IOC was generated in the official repositoryserver and by whom.

Finally, the "Audit IOC" enables the user to track the changes that an IOC (stored in the official repository server) may have suffered. In other words, it provides him/her with a complete list of files/directories belonging to the IOCthat have been added, modified or removed.

**Official link taken from ESS repositories**: https://bitbucket.org/europeanspallationsource/ioc-factory

###  Calibration 

###  Logbook (Olog) 

**Description taken from**: http://olog.github.io

Logbook Service for Accelerator Operations

[Official link](http://olog.github.io)

###  Archiver 

**Description taken from**: https://slacmshankar.github.io/epicsarchiver_docs/

The EPICS Archiver Appliance is an implementation of an archiver for EPICS control systems that aims to archive millions of PVs.

[Official link](https://slacmshankar.github.io/epicsarchiver_docs/)

###  Alarm Server 

The alarm server monitors the status of configured PVs belonging to the control system.

[Official link](https://github.com/ControlSystemStudio/cs-studio/wiki/BEAST)

###  Channel Finder 

**Description taken from**: http://channelfinder.github.io/

ChannelFinder is a directory server, implemented as a REST style web service. Its intended use is within control systems, namely the EPICS Control system, for which it has been written.

[Official link](https://github.com/ChannelFinder/ChannelFinderService)

##  Middlelayer Services 

This set of applications will compose the foundation of services performing any kind of transformation or usage of the control system process variables.
Typically, services in this category are both an EPICS server and client, communicating via Channel Access (EPICS v3) and/or PV Access protocols (EPICS v4).
A list of possible Middlelayer services that may be deployed/developed can be found below.

###  Unit Conversion 

###  Machine Snapshot (MASAR) 

A dockerized MASAR service has been configured and is available as [docker-masar-service-composed](https://github.com/lnls-sirius/docker-masar-service-composed) repository in the lnls-sirius organization at GitHub. An alternative database-based system callse [config-db](https://github.com/lnls-sirius/docker-config-db) has been developed that will probably replace MASAR.

###  Lattice Model 

###  EPICS Gateway 
