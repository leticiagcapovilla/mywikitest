---
title: Stream-IOC
description: 
published: 1
date: 2024-06-06T16:06:22.923Z
tags: 
editor: markdown
dateCreated: 2024-06-06T16:05:11.751Z
---

# CON: Stream-IOC

<br>

## Introduction

Stream-IOC is an EPICS IOC application based on StreamDevice developed by [LNLS Controls Group](/Machine/Groups/CON). It consists of StreamDevice 2.7.7, packaged with proper database definition and protocol files for integrating into the control system several devices intended to be used in Sirius.

<br>

## Current supported devices

* Agilent 4UHV Ion Pump Controller
* Berthold Technologies LB 6420
* [MBTemp](/Machine/Groups/CON/mbtemp)
* [DCM SE-10](https://dcmtech.com.br/equipamentos-e-sistemas-para-monitorar-temperatura-e-umidade/se-10-monitor-de-ambientes-com-acionamento-de-cargas/){target=_blank}
* [CountingPRU](/Machine/Groups/CON/pruserial485)
* [NTP time servers](/Machine/Groups/CON/ntp)
* [SPIxCONV](/Machine/Groups/CON/spixconv)
* Thermo Fisher Probes FTH 6020
* ELSE Nuclear SATURN 5702

<br>

## Devices that will be supported in the future

* Sirius pulsed magnets controller unit

<br>

## External links

Stream-IOC source code and manual are available at [https://github.com/lnls-sirius/stream-ioc](https://github.com/lnls-sirius/stream-ioc){target=_blank}.

More information about StreamDevice EPICS module can be found on [its official web site](http://epics.web.psi.ch/software/streamdevice/){target=_blank}.
