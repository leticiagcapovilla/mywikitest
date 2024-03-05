---
title: High Level Applications and Virtual Accelerator
description: 
published: 1
date: 2024-03-05T21:44:25.984Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:16.484Z
---

# Machine: High Level Applications and Virtual Accelerator

The high level applications for the Sirius control system comprise software for monitoring and controlling parameters; parameter data archiving, visualisation and analysis; and the operations and maintenance management systems.

<br />

## Development and testing

The development of high level applications, operator interfaces and associated software needs to take into consideration the different stakeholders involved in the project, which include:
* Accelerator Physicists
* Beamline users
* External community members
* Machine operators
* Managers
* Software developers
* Technical groups

Moreover, the different phases of the project will reflect on different requirements for software. The phases could be divided in the following way:
* Equipment and control system testing
* Assembly
* Commissioning
* Operation
    * User shifts
    * Maintenance
    * Machine study

Existing HLA solutions must be used as much as possible, at least in the initial stages of development. This could allow for parallel developments of software components. For example, [MML](/home/Groups/FAC/matlab_middle_layer) is planned be used for testing the virtual accelerator as it is being developed.

The standard procedures used by the operators at UVX are an interesting source of knowledge for eliciting and evaluating requirements. These should be considered taking into account the differences between UVX and Sirius, but can provide ideas for scenarios to help design applications and their integration with the other control system applications.

<br />

### Requirements

The list of software to be developed is kept in an an excel with restricted access ([HLA planning.xlsx](https://cnpemcamp-my.sharepoint.com/personal/liu_lnls_br/_layouts/15/WopiFrame.aspx?docid=16ec60489f90540bd8a8154db55b8b243&authkey=AfpsHA1RXE77w4f2-ARAKJY&action=view))
The [list of UVX high level applications](https://wiki-sirius.lnls.br/mediawiki/index.php/FAC:UVX_high_level_application_list) may assist in the definition and development of high level software for Sirius.

<br />

### Architecture

Discussions are necessary to define the system layers to which certain functions, such as magnet current to field conversion, will be assigned. A service-oriented architecture could be used (see [Service Oriented Architecture for High Level Applications (NSLS-II)](http://accelconf.web.cern.ch/AccelConf/IPAC10/papers/tupec072.pdf) and [NSLS-II High Level Application Infrastructure and Client Design](http://accelconf.web.cern.ch/AccelConf/PAC2011/papers/mop250.pdf)).

<br />

### Environment and tools

The environment for developing and testing high level applications will be base on the Ubuntu 16.04 linux distribution with python3.6 and EPICS >R3.14. GUI will be developed preferably with PyDM but CS-Studio will also be used for simpler interfaces and for control interfaces already available.

<br />

#### Setting up the development and testing environment

This [wiki page](/home/Groups/FAC/setup_workstations) describes the installation process of all libraries necessary for the HLA development.

<br />

#### CS-Studio

We have created a [LNLS distribution of CS-Studio](https://github.com/lnls-sirius/lnls-studio) that should be used to develop HLA for Sirius.

<br />

####  Soft IOCs and CASs

Templates are available for creating IOCs (EPICS-provided) and CASs (in [hla](https://github.com/lnls-fac/hla)). Usage instructions are available in the [Cookbook](/home/Groups/FAC/cookbook):
* [Creating empty IOC from template](/home/Groups/FAC/cookbook#create-empty-ioc-from-template)
* [Creating empty PCASPy CAS](/home/Groups/FAC/cookbook#create-empty-pcaspy-channel-access-server)

<br />

#### EPICS Extensions

##### Gateway

When running IOCs in a different subnet from the clients, use the EPICS Gateway. Set Channel Access environment variables. [Set the Channel Access environment variables](/home/Groups/FAC/cookbook#set-channel-access-environment-variables) in the clients to look for PVs using it.

<br />

### Repositories

Each LNLS group may have its own organization on Github with various group's repositories. The Accelerator Physics group, for example, manages its repositories in the [lnls-fac](https://github.com/lnls-fac) organization. Repositories which are relevant for Sirius developments by many groups should be located in the [lnls-sirius](https://github.com/lnls-fac) organization.

<br />

### Versioning

The [Semantic Versioning](http://semver.org/) (version 2.0.0) system is the basic scheme used to define version numbers. For Python packages, [PEP 440](https://www.python.org/dev/peps/pep-0440/) provides a useful set of rules that are understood by installation automation tools. From this PEP, we add to the Semantic Versioning scheme the rule for developmental releases, by appending the suffix .devN to the version number in versions between final releases. The following example illustrates the use of the proposed versioning scheme; versions are chronologically ordered with more recent versions on the bottom.

|Version| Description |
| --- | --- |
|0.1.0| Initial release |
|0.1.1| Bug fixes, no new functionality |
|0.2.0.dev0| Initial developmental release with new functionality |
|0.2.0.dev1| Second developmental release with new functionality |
|0.2.0| Final release with new functionality (in comparison with 0.1.1) |
|1.0.0| Public API defined |
|1.0.1| Bug fixes, no new functionality |
|1.1.0| New functionality, no bug fixes |
|1.2.0| New functionality, with bug fixes |
|2.0.0| Incompatible public API changes  |

**Table 1**: Versioning scheme example.

When a version is ready to be shipped, create a Release in the corresponding GitHub repository. A procedure for this is available in the [FAC:Cookbook](/home/Groups/FAC/cookbook) (see [Create a repository release](/home/Groups/FAC/cookbook#create-a-repository-release).)

<br />

### Guidelines

The following guidelines apply to high level application development (detailed requirements may be written for specific projects); the software should be
* Concisely implemented: it should reuse existing data structures and code in order to avoid replications that introduce code/data maintenance overheads 
* Easy to install and configure (write instructions and dependency lists when necessary)
* Well documented (non-obvious functionality and design decisions)
* Based on well tested and supported packages and libraries
* Testable
* Safe

Tool integration must also be addressed; applications must provide ways of importing and exporting data to be analysed, preferably in a seamless way.

<br />

### Visual Style Guide

The visual style guide for Sirius defines guidelines for building graphical user interfaces. (see [Machine:High Level Applications Visual Style Guide](/home/Machine/hla_visual_guide)) 

<br />

## Deployment and support

Automated schemes for software installation are preferred. When adding external dependencies (those which are not listed above), versions available on standard Linux package repositories should be given preference.

<br />

### Installation

Final releases are made available in the GitHub repositories, as .tar.gz files. The distributions should include a README file describing the software, and an INSTALL file describing requirements and installation procedure; the user is responsible for ensuring the appropriate versions of requirements are available.

The lnls-fac package dependencies are shown in the figure below, where an arrow pointing from A to B means A uses (depends on) B.

![](/img/machine/high_level_app/Package_dependencies.svg)

**Figure 1**:

|Package| Version| lnls| mathphys| pyaccel| sirius| trackcpp| va |
| --- | --- | --- | --- | --- | --- | --- | --- |
|lnls| 0.8.0| 	0.7| 			 |
|mathphys| 0.7.0| 					 |
|pyaccel| 0.12.0| 	0.7| 		3.3|  |
|sirius| 0.11.1| 0.8| 0.7| 0.12| 		 |
|trackcpp| 3.3.0| 					 |
|va| 0.15.0| 	0.7| 0.12| 0.11| 	 |

**Table 2**: Package dependencies; columns contain dependencies for the package and version in row.

<br />

#### C/C++

Makefiles must be provided, with targets *all* and *install* for compiling and installing C/C++ applications, respectively. On Linux, the *install* target must install files on `/usr/local/<bin|include|lib>`. Additionally, a *develop* target may be provided; this should install symbolic links to the files in the development directory, so that any changes made are immediately available for development and testing purposes.

<br />

#### Python

Packages must include a `setup.py` file, using [setuptools](https://bitbucket.org/pypa/setuptools). Dependencies must not be defined in this file for automatic download and installation, but be listed in the INSTALL file instead.

<br />

#### Matlab

Installation of Matlab on a few computers are planned using, maybe, network licenses. [MML](/home/Groups/FAC/matlab_middle_layer) will be used primarily for machine studies.

<br />

### Infrastructure

We need to discuss how to store and retrieve data such as excitation curves. A DBMS may also be necessary for archiving and other applications (the EPICS Archiver Appliance, for example, uses MySQL).

<br />

## Machine Applications

Machine applications are soft IOCs running on the control system whose purpose is to process low level PVs, providing derived high level PVs for client applications. There will be a number of such machines applications: `sirius-vaca`, `si-ap-currlt`, `si-tune`, `si-sofb`, `si-fam-ma`, and so on.

### Virtual accelerator

A virtual accelerator (VA) with an EPICS interface is being developed for testing high level applications and will be integrated with the Sirius control system. Code is in the [va repository](https://github.com/lnls-fac/va). (see [FAC:Virtual accelerator][link]) 

### [Optics Correction][link]
{{#lst:Machine Application:Optics Correction|introduction}}

### [Current Information][link]

### [Injection Position and Angle Correction][link]

### [Slow Orbit Feedback System][link]

### [Hight Level Timing][link]

### [Hight Level Magnet Power Supply][link]


## HLA - High Level Applications

FAC HLAs are part of the Control System for the Sirius. They are available in the *github* repository https://github.com/lnls-sirius/hla and have the following dependencies:
* PyEpics
* Qt5/PyQt5
* [pydm](https://github.com/slaclab/pydm)
* [devpackages](https://github.com/lnls-sirius/dev-packages.git)

### Power Supply Commands Application - PSCommands

* The application user manual, in portuguese, can be [accessed here](https://cnpemcamp.sharepoint.com/:b:/s/Comissionamento/EQCxIhA6GShAkEJbe4KKDgUBayx3xv0_wAYxhTTrRQlRhA?e=UZ0KIk) (available only through CNPEM Office-365 login).

### Hight Level RF

####  Low Level Control Windows 

* [link to Low Level Control Windows in EDM](http://git.cnpem.br/eduardo.coelho/dllrf-edm-screens) from Diamond (available only within ABTLUS domain)

* [link to Low Level Control Windows in CS-Studio](http://git.cnpem.br/claudio.carneiro/dllrf-css-screens) developed by CON (available only within ABTLUS domain)
