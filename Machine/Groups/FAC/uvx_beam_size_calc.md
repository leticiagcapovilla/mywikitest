---
title: UVX beam size calculation
description: 
published: 1
date: 2024-03-19T19:34:56.209Z
tags: 
editor: markdown
dateCreated: 2024-03-19T19:34:27.607Z
---

# FAC: UVX beam size calculation

The UVX beam size calculation system, located at the DFX beamline, consists of an Ethernet camera connected to a desktop computer running the Dimfei Delphi application. Dimfei uses DLLs to communicate with the camera and perform the beam size calculation.

## Camera

A [Basler](http://www.baslerweb.com/en) scA640-70gm camera is used for beam image acquisition, with the X-rays coming from a pinhole array converted into visible light by a film.

<br />

## Software

### Dimfei

The Dimfei Delphi application runs on DFX1 and is the user interface to the beam size calculation system. It can be used for changing the camera and calculation parameters, and depends on the DLLs described below for these tasks.

<br />

### DLLs

The DLLs used by Dimfei are written in C++ and the source code is available in the dimfei repository.

<br />

#### imgacq

Image acquisition from the Basler camera, using the Basler SDK.

<br />

#### dimfei

Beam size calculation using 2D Gaussian fit with [Levenberg-Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm).

<br />

## Installation and configuration

The [Basler](http://www.baslerweb.com/en) SDK is required to use the camera. To install the `Dimfei` application, copy the Dimfei directory from the dimfei repository to `C:\Arq\Controle\Projetos\Tandem` and copy the imgacq and dimfei DLLs to it.

When installing in a new computer or after hardware changes, it might be necessary to change some constant values and recompile the Dimfei Delphi application (see instructions below on how to set up the development environment):

- In `Obturador.pas`, `CONST_ENDBASE` must be set to the shutter card base address.
- In `ComDimfeiIDPM.pas`, `DFX1_IP` and `OPR1_IP` must be set to the DFX1 and OPR1 IP addresses, respectively.

<br />

## Development

To be able to compile the Dimfei application, use the [same configurations][link] as for the UVX control system high level applications in general. The source code for the DLLs is supplied as Visual Studio solutions, and some additional requirements must be fulfilled:

- acqimg depends on the Basler SDK.
- dimfei depends on [LAPACKE](http://www.netlib.org/lapack/index.html#_lapack_for_windows).