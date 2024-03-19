---
title: UVX control system high level applications
description: 
published: 1
date: 2024-03-19T19:50:04.189Z
tags: 
editor: markdown
dateCreated: 2024-03-19T19:40:12.027Z
---

# FAC: UVX control system high level applications

The UVX control system high level applications run on Windows and are mostly written in Delphi. The source code is available in [[FAC:FAC#UVX-HLA repo|repositories]][link] in the lnls82-linux workstation.

Information and instructions for application usage can be found in the Operations group (GOP) directory in the `centaurus` server.

<br />

## Installation
To install the UVX control system high level applications, BDE is required. The control room main computers and installation steps are described in the next sections.

<br />

### Control room computers
The next sections describe the distribution of control system high level application functionality among the control room computers.

<br />

#### OPR1
* Client applications
* Main control system server
* Undulator (PGM beamline) command server

<br />

#### OPR2
Main data analysis computer.

<br />

#### OPR4
* Beam data server to beamlines
* Images for campus television

<br />

#### OPR7
* Client applications
* Archiving
* Beam data server to OPR4

<br />

#### OPR10
* Images for storage ring status web page
* Telephone operator warning system

<br />

### Installation steps

### BDE
The following database aliases must be defined:

```
Carga: C:\Arq\Controle\Carga
Conf: C:\Arq\Controle\BDADOS\CONFIGS\Maquina
Dics: C:\Arq\Controle\BDADOS\DICS
Logs: C:\Arq\Controle\BDADOS\LOGS
Misc: C:\Arq\Controle\BDADOS\MISC
Norm: C:\Arq\Controle\BDADOS\CONFIGS\Normal
 ```
The tables and configuration files must be installed in `C:\Arq\Controle\BDADOS`

<br />

#### Drivers and DLLs
The following files must be installed in the corresponding directories:

```
porttalk.sys: C:\Windows\System32\Drivers
locoIOXP.dll: C:\Windows\System
PSocketDLL.dll: C:\Windows\System
```

<br />

#### Registry
The Windows Registry must have the following entries with type `REG_SZ` under `HKEY_CURRENT_USER/IDPM/MODO`:

<br />

##### Main server

```
CONEXAO_DPM: SEGURO
CONEXAO_REDE: LOCAL
ENDBASEPCI: <pciloco_base_address>
HANDSHAKE: TRUE
HANDSHAKE_REMOTO: FALSE
IP_SERVIDOR_LOCAL: <main_server_ip_address>
PCISLOCO: TRUE
TIMEOUT: TRUE
```

<br />

##### Remote servers

```
CONEXAO_DPM: ESPIAO
CONEXAO_RAPIDA: TRUE
CONEXAO_REDE: REMOTO
ENDBASEPCI: <pciloco_base_address>
HANDSHAKE: TRUE
HANDSHAKE_REMOTO: FALSE
IP_SERVIDOR_LOCAL: <main_server_ip_address>
LOCOUSAPCI: TRUE
TIMEOUT: TRUE
```

<br />

#### Applications
Applications must be installed in `C:\Arq\Controle\Projetos` (See [[FAC:UVX high level application list]][link].)

<br />

## Configuration
The control system network and device configuration for the high level applications is kept in `C:\Arq\Controle\BDADOS\CONFIGS\Rede`. After changes to the files, the `Config` program must be run to generate the database tables used by the applications.

There are software limits on the maximum number of bytes that can be used for input and output, and also for the maximum number of network nodes. These limits are defined in `C:\Arq\Controle\Projetos\Placas\Datplaca.pas` and `C:\Arq\Controle\Projetos\DLL_ServidorDPM\Dll_Psocket\USocket.pas` and, in case of changes, the control system applications dependent on them must be recompiled.

<br />

## Development
To compile the UVX control system high level applications, the appropriate version of Delphi is needed, with some additional packages. The sections below describe differences among the different Delphi versions used and packages required by multiple applications; some of them might require specific packages that can be found in each project directory.

<br />

### Delphi
There are two parallel versions of the UVX control system high applications kept up-to-date; one is the classic Delphi 3 and 5, and the other the Delphi 2009 . When using the latter, some differences must be kept in mind.

<br />

#### Delphi 2009
The high level applications repositories in lnls82-linux are located in `RepositoriosD2009W7`. Some differences from the other versions are:
* The `*Socket` components from Delphi 3 and 5 are not available; the declaration, initialisation and the procedures associated with its events must be added programmatically.
* The `Real` numeric type is 8 bytes long, in contrasts with the 6 bytes length in Delphi 3. In particular, this type is user by the archiving application `Registro` and the difference leads to incompatible archive files.
* `Porttalk` cannot be used on Windows 7 64-bit machines.

Each time you open the IDE on the FAC6 computer, rename the file `C:\Users\maquina\AppData\Local\Temp\EditorLineEnds.ttr` to anything else. While the file keeps its original name, opening the IDE again will fail.

<br />

### Packages
Multiple high level applications require the `FISAC` and `LOCO` packages. These are available for installation in the lnls82-linux repositories.

<br />

## Archiving
The UVX control system archiving system stores the values of a subset of the control system variables at three different rates. Data can be loaded, visualised and analysed in Igor Pro with the ANDA scripts.

<br />

### System components
#### Registro
Registro is the application running on OPR7 with the responsibility of saving the varible data in binary form to files in the `C:\Arq\Anonimos` directory. It also creates the variable header files (`CAB*`) and generates entries in the `IndReg` table in OPR2, assocating each archive file with the corresponding header. Every full hour, Registro copies the last `STOT` file, and at 00:00 it copies the `TOT` file to OPR2.

<br />

#### ANDA
ANDA is a set of Igor Pro scripts that retrieve data from the archive and supply tools for analysis and visualisation of data. It is installed by copying the `ANDA` folder to the Igor Pro installation `Igor Procedures` directory. The paths used by ANDA are defined in `C:\Arq\Medidas\Estabilidade\MacrosTemplates\Caminhos.txt`; look at the OPR2 and FAC6 versions of the file for examples.

When installing ANDA on a 64-bit Windows machine, import the Registry entries from FAC6 (available at `C:\Arq`).

<br />

#### RegAn
RegAn is the application that loads and converts the binary data from the archive files into text data that can be loaded by Igor Pro. It is available at the high level applications repository.

<br />

### Archiving periods
* `TOT*` files contain data with a 30s period.
* `STOT*` files contain data with a 1s period.
* The `Reg_Veloz.dat` file contains data with a 0.25s-spaced, and is regularly overwritten.

<br />

### Changing the set of archived variables
The software limit on the number of variables that can be archived by the current version of Registro is defined in the file `Registro\DatRegTot.pas`. Under that limit, variables may be added or removed from archiving by editing the procedures `PrepCab` and `MontaReg` in `Registro\URegistro.pas`; after a change, the program must be recompiled, and the name of the archive header file bust be updated in the `IndReg` table in OPR2.
