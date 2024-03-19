---
title: FAC Documentation
description: 
published: 1
date: 2024-03-19T18:49:31.391Z
tags: 
editor: markdown
dateCreated: 2024-03-19T15:38:12.312Z
---

# FAC: FAC Documentation

## Introduction

Accelerator Physics Group main wiki page. This page contains a list of the group's members, infrastructure, projects and activities, with associated documentation. 

**Content available**

- [Amplification Factors and Magnet Tolerances](/Machine/Groups/FAC/amplif_fac_mag_tol)
- [Cookbook](/Machine/Groups/FAC/cookbook)
- [Discussions tutorial on FAC tools](/Machine/Groups/FAC/discussions_tutorial)
- [Fieldmap analysis](/Machine/Groups/FAC/fieldmap_analysis)
- [Girder Possibilities](/Machine/Groups/FAC/girder_possibilities)
- [LOCO](/Machine/Groups/FAC/loco)
- [Log](/Machine/Groups/FAC/fac_log)
- [Low-alpha optics mode](/Machine/Groups/FAC/low-alpha_optics_mode)
- [Matlab Accelerator Toolbox](/Machine/Groups/FAC/matlab_at)
- [Matlab Middle Layer](/Machine/Groups/FAC/matlab_middle_layer)
- [Setup workstations for Sirius](/Machine/Groups/FAC/setup_workstations)
- [Trackcpp](/Machine/Groups/FAC/trackcpp)
- [Virtual accelerator](/Machine/Groups/FAC/virtual_acc)
{.links-list}

<br />

## Infrastructure
**New Machines Configurations**

For a complete guide on configuring new machines with a fresh install of Ubuntu16.04 LTS operating system, check the link Workstations Setup.

**FAC Repositories**

We have code and data repositories hosting the software tools that the FAC group develops for sirius and the UVX machine studies. Code repositories are usually stored at GitHub, while data repos, due to their large sizes, are stored in one of our workstations, currently lnls82-linux.

**Installation of Working Directories**

To compile (when necessary) and install the projects, check for specific documentation in README and INSTALL files or makefiles.

**Directory `fac_files`**

Directory `/home/fac_files` in the system is where all the working directories of the repositories should reside. Binaries and scripts from this directory get installed in various system locations eventually. The directory `/home/fac_files` should be read-write accessible for everyone in the fac group; moreover, any new file or directory a group user creates should automatically be writable to eveyone else in the group. In order to accomplish this a finer file attribute system called facl has to be used. Below is the recipe on how to configure `facl` control on `/home/fac_files`

- use `groups` to check if all users have `fac` as their primary group
- add option `acl` entry in `/etc/fstab` corresponding to `/home` partition
- if it does not exist yet create directory `/home/fac_files`
- run `sudo chown -R 'whoami'.fac /home/fac_files`
- run script `fac-setfacl.sh` in order to set attributes of `/home/fac_files` directory.

After these steps /home/fac_files should be ready to receive all repositories.

**Repos Management**

The accelerator physics group manages file repositories for codes and data. Git is used as version control system for them. It can be installed in a Linux Ubuntu machine issuing the command, 

```
sudo apt-get install git
```

or binaries can be installed from [http://git-scm.com/](http://git-scm.com/) for Microsoft Windows machines.

The code repositories are hosted at the [GitHub](https://github.com/) site, whereas the master repository for data is located at `/home/fac_files/repo/fac_data.git` at the group's lnls82-linux workstation. The code repositories contains mostly small files written in MATLAB, python, C++ and C. The data repository, on the other hand, has input and output files used in our applications that are sometimes too large for the master repo to be hosted outside our gigabit network. On a default installation, local copies of these repositories reside respectively at the paths

```
<ROOT>/fac_files/code
<ROOT>/fac_files/data
```

The `<ROOT>` path depends on the operating system. On Linux machines, `<ROOT>` is usually `/home`, whereas on Windows machines it can be either `C:\Arq` or `D:\Arq`. 

**Cloning**

A local copy of the repositories can be created by cloning an existing copy of the repository. You can clone a repository (scripts, in this example) from GitHub with the commands

```
cd /home/fac_files/code
git clone https://github.com/lnls-fac/scripts.git
```

In order to contribute code, the user must have a [GitHub account](https://github.com/join) and optionally a registered [public key](https://help.github.com/articles/generating-ssh-keys) (in the absence of a key, login information will be asked when interacting with the remote repositories). Moreover you need to belong to GitHub's [LNLS Accelerator Physics Group](https://github.com/lnls-fac) (contact a FAC member). Once all requirements are fulfilled you can clone the code repositories with the command above, and set up user information with (Linux): 

```
git config --global user.name <USERNAME>
git config --global user.mail <USERNAME>
git config --global user.email <EMAIL>
```

where `<USERNAME>` should be replaced with the GitHub username and `<EMAIL>` by the email address. An auxiliary script (fac-cloneall.sh) is provided for cloning all lnls-fac code repositories. The script can be downloaded from the [scripts](https://github.com/lnls-fac/scripts) repository, or the repository may be cloned as in the example above. When run, it will only clone the repositories not found in the destination directory. 

**Working with repos**

Once a repository is cloned, the working directory with all files is ready to be used: you can create, edit or delete files as you would do normally under Linux or Windows. To check what has been modified since last time you pulled from the master repository, under any directory within the repository root, you use

```
git status
```

A list with modified and newly created files will be displayed, if this is the case. When you are ready to commit the changes after work you need to explicitly tell git which modified files you want to add to the next commit to your local repository (again, use `git status` to check which files were created/modified). This is accomplished using the command

```
git add <FILE OR DIRECTORY NAME>
```

The output from git status comes in handy fro copying and pasting into the `git add` command. You can also tell `git` to add all created and modified files under the working directory using the flag `--all`:

```
git add --all
```

Finally commit from the working directory to the local repository is accomplished with

```
git commit -m "a simple message about this commit"
```

If the message option (`-m "message"`) is missing a text editor will be called where you should edit the commit message. After exiting the editor your changes will be committed. The final step is to push your updated version of the local repository to the master repository, from which everyone's local repositories pull their synchronizations. This is done with

```
git push
```

To synchronize your local repository and working directory, on the other hand, you can use

```
git pull
```

There is a help system available from within the `git` application. You can access it with calls to `git`. For example,

```
git help
git help status
git help commit
git help log
```

There is also online documentation on Git in various sites. For help on a succinct list of command, see [gitref.org](http://gitref.org/). For a more comprehensive documentation look at the [Git site](http://git-scm.com/doc).

The local copies of the code and data repositories will usually reside, as pointed out, at `<ROOT>/fac_files.` In Linux machines it is a good idea to create a symbolic link at the user home directory point to this directory:

```
cd ~
ln -s /home/fac_files
```

**Code repos**

The former `code` repository has been split into several project-related repositories; they are structured as follows:

```
apsuite              # Accelerator Physics utilities
collective_effects   # MATLAB scripts for collective effects and impedance bugdets calculations
fieldmaptrack        # fieldmap class library to be used for magnetic fieldmaps analysis 
insertion_devices    # a c++ library that reads IDs fieldmaps and calcs kick tables
job_manager          # set of python scripts for distributed computing
lnls                 # LNLS-specific configurations for code
mathphys             # mathematical and physical utilities
magfield             # magnetostatic calculations of magnet blocks (IDs)
MatlabMiddleLayer    # MATLAB scripts: AT, MML, lattice_errors, magnet_modelling, insertion_devices, etc
pyaccel              # library for beam dynamics calcs (optics, tracking etc.; uses trackcpp)
scripts              # various scripts (bash, python) for managing files for tracy3, gerenciador_disparos, ssh, etc
sirius               # pyaccel Sirius lattices
siriusdb             # Sirius parameters for use in control system
sirius_wiki          # the script that generate wiki Parameter: pages automatically
tools                # auxiliary tools (e.g., Parameters MediaWiki extension)
trackcpp             # tracking code (optics, tracking etc.)
tracy_sirius         # LNLSTracy3 code
va                   # virtual accelerator
vacpp                # incipient version of the virtual accelerator written in c++ for efficiency purpose.
```

A good guide to version numbering can be found at [http://semver.org/](http://semver.org/). 

**Data repo**

In this repository analysis and result files are stored.

```
sirius               # current directory where sirius calculation and analysis files are stored
sirius_col_effec     # results for studies of collective effects in sirius
sirius_mml           # data corresponding to old sirius lattice versions
sirius_python        # data corresponding to old sirius lattice versions
sirius_tracy         # data corresponding to old sirius lattice versions
uxv_epu              # misc data for the EPU in the UVX storage ring
```

**HLA repo**

```
hla                  # high level applications
hla-vagrant          # environment for hla development and test with Vagrant and SaltStack
```

**UVX-HLA repo**

The source code of the UVX control system high level software is kept in Git repositories, with remotes hosted at lnls82-linux, in the `/home/fac_files/repo/uvx_hla directory`. It includes a repository with the Dimfei libraries for beam image acquisition and calculation.

**Centaurus-FAC**

Server Centaurus in the ABTLUS domain has a folder containing FAC legacy files. Periodic backups of this folder are managed by TIC. The folder structure is as follows:

```
Atividades          
Biblioteca
      Apresentações
      Artigos
      Cursos
      Didaticos
      Livros
      Notas Internas
      Publicacoes FAC
      Python
      Teses
      Workshops  
DFE
DFX
Eventos
      2009-09 Visita do H. Wiedemann
      2009 Nash Boaz
      2010 IPAC
      2011-04 Visita do Laurent Nadolski
      2011 IPAC-ALBA-DIAMOND
      2011 NA-PAC
      2012 IPAC
      2013 Ryutaro Nagaoka
Experimentos
Ferramentas
IntraFac
LNLS Booster
LNLS UVX
NovasMaquinas
Pessoal
Projetos
Publica
Sirius
WebFAC
```

<br />

## Projects

**UVX - Low-alpha mode**

The idea in this optics mode is to generate a very short beam for terahertz experiments. This is accomplished by reducion the linear compaction factor as much as possible. For details please read the [Low-alpha optics mode page](Machine/Groups/FAC/low-alpha_optics_mode)

**UVX - Low-emittance with Insertion Devices mode (BEDI)**

Realizamos estudos no modo BEDI para controlar instabilidades coletivas longitudinais e transversais com o sistema de feedback. Também tentamos otimizar o tempo de vida desse modo alterando a tensão de GAP das cavidades de RF, sem sucesso e atualmente estamos trabalhando para gerar um modo similar ao BEDI que possua tempo de vida mais elevado. A vantagens desses modos de baixa emitância é que eles possuem feixes de elétrons menores, o que melhora a qualidade da luz síncrotron gerada. Assim, tornar um desses modos adequado para a operação do UVX seria benéfico para os usuários da máquina. Ainda, aprender a usar equipamentos avançados, como o sistema de feedback, serve como treinamento para a operação futura do sírius, onde tais ferramentas serão essenciais para o funcionamento da máquina. (see FAC:Project BEDI optics mode)(link)

**UVX - LNLSLink**

This is a Delphi client running at the OPR1 computer that communicates with UVX control system IDPM server. It is a process variable server whose rôle is to allow high level applications to read machine parameters and change set-points. It communicates with other clients through a simple in-home defined ASCII-stream protocol. For example, a string "A2QF01_SP,112.5," received through port number 53131 will set the power supply A2QF01 to the value of 112.5 A. The string "AMP01A_AM,AMP01B_AM,", on the other hand, will return the string "AMP01AH_AM,-2.345,AMP01BH_AM,-1.823,", for example, which contains the horizontal readout values of -2.345 mm and -1.823 mm for the AMP01A and AMP01B bpms, respectively.

At this moment not all but most of the storage ring and booster parameters are implemented in LNLSLink. The main client that uses LNLSLink is the MML at MATLAB for beam dynamics machine experiments, routine corrector cycling and periodical optics measurements.

**SIRIUS - Lattice versions**

In the course of the Sirius project's history, each submachine has been tagged with a version string identification. This identification consists in a two-letter initial indicating the submachine, a lattice version and, optionally, an identification of the optics of the lattice. Letters SI refer to the storage ring, TS refers to the booster to storage ring transport line, BO to the booster, TB refers to the linac to booster transport line and finally, LI refers to the linac. (see FAC:Sirius lattice versions)

**SIRIUS - Parameter specifications**

The Accelerator Physics Group is responsible for defining a large number of parameters which are critical in design various subsystems in the Sirius project.

**SIRIUS - Fieldmap analysis**

Field specification of every 3D nominal model of magnets is checked. This is accomplished by having its 3D-field map sampled on the mid-plane (at y = 0 mm) and analyzed. It can be demonstrated that knowledge of the 3D magnetic field on any plane, and on the mid-plane in particular, is enough for the reconstruction of the 3D field over the entire gap region. Apart from the discreteness of the fieldmap grid on the xz plane, numerical trajectories with arbitrary precision can be computed using standard Runge-Kutta integration algorithms. Multipoles around these trajectories can then be calculated and compared to specifications. (see [Fieldmap analysis](/Machine/Groups/FAC/fieldmap_analysis))
SIRIUS - Magnets measurement

Accelerator Physics Group should closely interact with the Magnet Group for the definition of the characterization benches (Hall Probe, Rotating coil) and for magnetic measurements of magnet prototype and serial production elements.

> we have created a set of python scripts to analyze data from rotating coil measurements. These scripts are in the directory `<ROOT>/code/python/BobinaGirante`. These scripts are being superseded by a corresponding set developed at the Magnets group
{.is-info}


**SIRIUS - Diagnostics beamlines**

**SIRIUS - Wiki**

This wiki is maintained for listing and discussing machine parameters and subsystems, alongside with a tutorial. The Parameters extension available at tools is used to retrieve parameter values from a MySQL database. tions).

**Parameters extension**

There are three tables in the parameters mySQL database in order to manage Sirius parameters. By default, these tables are accessed by user prm_editor using password prm0.

**parameter**: six-column table (name,team,symbol,units,is_derived,value).

**dependency**: two-column table (name, dependency). Each line has a A = f(B) dependency. In this example A goes in the first column and B goes in the second column. A formula A = B + C, for example, generates two rows in this table.

**expression**: two-column table (name, expression). Expression is a string.

> A new version of the extension is available to be installed.
{.is-info}


**Wiki maintenance**

Currently, wiki administration is done by the SOL group. For help with wiki maintenance tasks, look at the FAC:Cookbook page. The following recipes are available:

- [Access MySQL parameter tables](/Machine/Groups/FAC/cookbook#access-mysql-parameter-tables)
- [Perform tests with the fac-wiki virtual machine](/Machine/Groups/FAC/cookbook#perform-tests-with-the-fac-wiki-virtual-machine)
- [Install the Parameters MediaWiki extension](/Machine/Groups/FAC/cookbook#install-the-parameters-mediawiki-extension)
- [Reset user password](/Machine/Groups/FAC/cookbook#reset-user-password)

**Figures**

Figures generated for the Sirius Wiki by the Accelerator Physics group members should, in general, be uploaded the group's SharePoint Library, in the sirius_wiki_figures directory; this allows future modification for updates. Figures automatically generated by scripts and analysis programs do not need to be uploaded.

**SIRIUS - High Level Applications**

The high level applications for the Sirius control system comprise software for monitoring and controlling parameters; parameter data archiving, visualisation and analysis; and the operations and maintenance management systems. (see [Machine: High Level Applications and Virtual Accelerator](/Machine/high_level_app_virt_acc)

**SIRIUS - Fluka/Flair support**

FAC has been involved in providing installation support of Fluka/Flair package used for radiation dose calculations:

**FLUKA** is a fully integrated particle physics MonteCarlo simulation package. It has many applications in high energy experimental physics and engineering, shielding, detector and telescope design, cosmic ray studies, dosimetry, medical physics and radio-biology. It is an application that is run from the command-line.

**FLAIR** is an advanced user friendly interface for FLUKA to facilitate the editing of FLUKA input files, execution of the code and visualization of the output files. It is based entirely on python and Tkinter.

**GEOVIEWER** is a C++ library for visualization of 3D geometries used in post-processing. 

```
Download
--------

00.	From https://www.fluka.org/fluka.php?id=download&sub=packages
	User Name: fuid-5457
	Password: <see /home/ximenes/fluka-flair/README.txt at lnls208-linux>

	download three files:

- fluka2011.2b-linux-gfor64bitAA.tar.gz
- flair-2.0-3.tgz
- flair-geoviewer-2.0-3.tgz

into folder a ~/flukaflair-installation
```

```
NEW INSTALLATION
================

Required packages
-----------------

01. sudo apt-get install gcc
02. sudo apt-get install g++
03. sudo apt-get install gfortran
04. sudo apt-get install tcl
05. sudo apt-get install tcl-dev
06. sudo apt-get install tk
07. sudo apt-get install tk-dev
08. sudo apt-get install python-dev
09. sudo apt-get install gnuplot
10. sudo apt-get install gnuplot-x11
11. sudo apt-get install make

Fluka
-----

12. add 'export FLUPRO=~/fluka' and 'export FLUFOR=gfortran' into .bashrc
13. source ~/.bashrc
14. unzip fluka2011.2b-linux-gfor64bitAA.tar.gz into <FLUPRO> dir (~/fluka)
15. cd $FLUPRO; make

Flair
-----

16. copy flair-2.0-3.tgz to ~/ and unzip it (look at README file for flair and flair-geoviewer installation)


Flair-geoviewer
---------------

17. tar xzf flair-geoviewer-2.0-3.tgz in ~/flair-2.0
18. cd ~/flair-2.0
19. make
20. make DESTDIR=~/flair-2.0 install


flair configuration
-------------------

21. configure flair to set gnuplot terminal to 'x11'.
```

```
NEW VERSION UPDATING
====================

-- fluka --

01. open gnome-terminal
02. go to user home ( 'cd ~' )
03. move old fluka folder to system temporary folder ( 'mv fluka /tmp/' )
04. move old flair folder to system temporary folder ( 'mv flair-2.0 /tmp/' )
05. create fluka folder ( 'mkdir fluka' )
06. copy all 3 files to ~/fluka
07. cd ~/fluka
08. tar xzf fluka2011.2c-linux-gfor64bitAA.tar.gz (or newer version)
09. compile fluka ( 'make' )
10. check if file 'flukahp' is created

-- flair --

11. copy flair-2.0-8.tgz (or newer version) to ~/
12. cd ~
13. tar xzf flair-2.0-8.tgz

-- geoviewer --

14. cd ~/fluka
15. tar xzf flair-geoviewer-2.0-8.tgz (or newer version)
16. cd flair--geoviewer-2.0
17. make
18. make install DESTDIR=~/flair-2.0 install
```

**SIRIUS - Beam Dynamics Studies**

1. Amplification Factors and Magnet Tolerances: In this section the alignment and excitation error tolerances for the Sirius storage ring magnets will be studied by the analysis of their orbit and optics distortion amplification factors.
2. Girder Possibilities: We have performed a study where several possible girder configurations have been considered and analyzed. In this study amplification factors are defined and calculated, serving as a way to quickly estimate the statistical effects of misalignment errors on the beam optics. Amplification factors are calculated for free and corrected beam oscillations in the Sirius storage ring.
3. Segmented and Rectangular Sirius Dipole Models: AT this point the Sirius dipoles are supposed to be rectangular but with curved poles. We have studied feasibility of different dipole models for the Sirius storage ring. The first model studied is that of a rectangular dipole in which the pole is also rectangular, that is, with constant field and gradient in the rectangular coordinate system. In this case the field varies along the trajectory of the beam. We analyzed the impact of this varying field on the beam optics and equilibrium parameters in order to ascertain the feasibility of the model. The second model studied was that of breaking Sirius dipoles into a composition of basic segments: B1 dipoles would be made of two identical segments, B2 dipoles would be made of three segments and B3 dipoles are made of a single segment. In this case we analyzed the impact of independent alignment of the segments on the alignment tolerance, due to the impact on the beam optics.

<br />

### Activities

**UVX control system high level applications**

The UVX control system high level applications run on Windows and are mostly written in Delphi. The source code is available in repositories in the lnls82-linux workstation. (see FAC:UVX control system high level applications)(link)

- Add ion pump (LOCOMUX R5N6, module 7) to archiving system.
- Fix alarm threshold persistence in operations program in OPR1.
- Add FOFB disabled as an alarm in operations program in OPR1.
- Evaluate possibility of aborting undulator motion commands from beamline.

**UVX beam size calculation**

The UVX beam size calculation system, located at the DFX beamline, consists of an Ethernet camera connected to a desktop computer running the Dimfei Delphi application. Dimfei uses DLLs to communicate with the camera and perform the beam size calculation. (see FAC:UVX beam size calculation)(link)

- We need to get another film to be able to convert X-ray into visible light. The one we have right now is damaged.
- We need to recalibrate the new camera.

### Beam dynamics codes

**MAD**

MAD is a beam dynamics code used in the accelerator physics group at LNLS mainly for creation of new lattices from afresh and for parameter match. Our current version is MAD8 which runs under Microsoft Windows.

**Matlab**

Currently the accelerator physics group uses MATLAB as a platform for both simulations and high level machine control of the UVX storage ring. The main packages used are **MML** and **AT**. Various packages have been written in-house around these main two for studying beam dynamics for Sirius and for the existing UVX storage rings. Below we describe very succinctly all these packages. Matlab library path has to be configured so that the main function of MML and AT are accesible within its workspace. When this configuration is done all, relevant paths can be loaded into matlab prompt executing the global script `lnls_setpath_mml_at`

**Accelerator Toolbox**

Accelerator Toolbox (**AT**) is a Matlab package [developed at SLAC](http://www.slac.stanford.edu/pubs/slacpubs/8000/slac-pub-8732.html) that implements a number of functions (scripts) that help in modeling elements, calculating optics in transport lines and storage rings and performing tracking simulations. A non-exhaustive list with help for available scripts can be obtained with the command `athelp`. Since AT is composed of a very large number of scripts there is no single document that describes every of its functionalities. The best documentation happens to be the source code of the scripts, which can looked at with matlab editor. (see AT page)

**MatlabMiddleLayer**

MatlabMiddleLayer (**MML**) is a Matlab package containing a set of scripts and data structures that are used to 1) map an AT simulation model into the real machine and 2) perform process variable readouts and setpoint modifications. It is a software layer between the machine control system (LNLS1Link for UVX, EPICS for Sirius) on the bottom and high-level machine study algorithms or routine operations on the top. MML's basic data structures can be accessed from Matlab workspace through two functions: `getao` (accelerator object) and `getad` (accelerator data). Parametrization of these two structures is done through other scripts which have to be tailored for each machine in particular. (see [MML page](http://10.39.50.85:3000/en/Machine/Groups/FAC/matlab_middle_layer))

`lattice_errors` **package**

A set of scripts to generate machines with random errors and to correct the optics. From the resulting corrected models flat files are generated and imported from Tracy3 for dynamical aperture calculation.

> revise how we implement rotation errors in bending magnets!!!
{.is-warning}

`magnet_modelling` **package**

A set of scripts that take field maps from 3D magnetostatic calculations and perform Runge-Kutta trajectory integrations to calculate important field parameters such as integrated nominals and error multipoles. A segmented model of the magnet can be generated using theses scripts.

`insertion_devices` **package**

Another set of script which defines which insertion devices are to be included in Sirius lattice, load their Radia kicktables, and does focusing compensation and tune adjustements.

`lnls_at2tracy_flatfile` **script**

The script lnls_at2tracy_flatfile generates tracy-like output flat files from the AT lattice model. It is mainly used to prepare tracy input run data from `lattice_errors`.

`tracy3_*` **package**

This is a set of scripts used to analyze and plot output results of Tracy runs. 

