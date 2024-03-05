---
title: Power Supplies
description: 
published: 1
date: 2024-03-05T16:39:08.595Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:36.912Z
---

# Machine: Power Supplies 

<br />

## Introduction

The Power Supplies (PS) are used to feed the magnets of all accelerators and transport lines, working as current sources. Due to their parameters, the PS were divided in three families: 1. Low Power Supplies (FBP): bipolar PS, with output up to 10A/10V, used to feed steering magnets, skew quadrupoles, quadrupole trim coils, etc. 2. High Power Supplies (FAP): unipolar PS, with ouput up to 350A/460V, used to feed Dipoles, Quadrupoles and Sextupoles of Storage Ring and other magnets. 3. AC Power Supplies (FAC): bipolar PS which will follow a 2-Hz reference, with output up to 1.1kA/800V, used to feed Dipoles, Quadrupoles and Sextupoles of Booster. All the PS will be controlled by the same digital hardware, called Digital Regulation System (DRS), but with different firmwares. The main parameters of the Sirius storage ring power supplies are shown in Table 1.

| Magnet kind | Dipole B1 | Dipole B2 | Quadrupole Q30  (QFB, QFP) | Quadrupole Q20  (QFA, Q1, Q2, Q3, Q4) | Quadrupole Q14  (QDA, QDB1, QDB2, QDP1, QDP2) | Sextupoles |
| --- | --- | --- | --- | --- | --- | --- |
| Magnet quantity | 40 | 40 | 30 | 170 | 70 | 280 |
| Magnet resistance \\\[mohm\\\] | 21.47 | 30.26 | 46.94 | 36.33 | 29.97 | 35.22 |
| Magnet inductance \\\[mH\\\] | 8.2 | 12.4 | 18.0 | 12.5 | 9.2 | 4.6 |
| Magnet time constant \\\[ms\\\] | 382 | 410 | 383 | 344 | 307 | 131 |

**Table 1**: Sirius SI main PS parameters.

<br />

## General Tables

1. A general table with power supply parameters can be [accessed here](https://cnpemcamp.sharepoint.com/:x:/s/ELP/EaXHkq-swT5Fh3xcsyfzOZYBXkQeKtMJdefVicC7ixPrGA?e=kfB2EK) (available only through CNPEM Office-365 login)

2. Power supply communications architecture can be [accessed here](https://cnpemcamp.sharepoint.com/:b:/s/ELP/EX-JCc1IeEJIlHcrdO8KM8oB-ubBj70SJ_vJrMppO3eNqg?e=fhZDea) (available only through CNPEM Office-365 login)

3. Device names of beaglebone black units used for power supply control can be [accessed here](https://docs.google.com/spreadsheets/d/11s11bqsI3l0wYF6fTtViMb_c2Ei8N1JVJgPSj-4318M/edit#gid=0) (available only through CNPEM Office-365 login)

4. Control system static table relating power supplies with their DC-Links can be [accessed here](http://10.0.38.42/control-system-constants/pwrsupply/bsmp-dclink.txt)

<br />

## Digital Regulation System (DRS) Specifications

1. BSMP specification of power supplies can be [accessed here](https://cnpemcamp.sharepoint.com/:x:/s/sei/EdwpNtZ1QItBlvEjc5j_REcBspYu9GkjKm64YNPe8026_Q?e=FDM0L6) (available only through CNPEM Office-365 login)

2. BSMP documentation can be [accessed here](https://github.com/lnls-sirius/libbsmp/blob/master/doc/protocol_v2-30_en_US.pdf)

3. Parameters bank specification from UDC firmware can be [accessed here](https://cnpemcamp.sharepoint.com/:x:/s/sei/EVsxmc1S2ylMhxGyE5-5oCoBq9jJeH2PzsrV10rLivgQUA?e=J6a0Vn) (available only through CNPEM Office-365 login)

4. Control electronics inventory and gain for each HRADC BNC monitors can be [accessed here](https://cnpemcamp.sharepoint.com/:x:/s/sei/EaAeezMA8i1Hm8MHQzqVaEABG2J15RDl3fdHqNfVvZBn6w?e=6b1BKl) (available only through CNPEM Office-365 login)

5. [[ELP:Table of memory addresses for power supplies Scope Source]]

## Operation Manuals

## PSCommands (Test, Turn On and Turn Off procedures)

## The Digital Regulation System (DRS)

## Low Power Power Supplies (FBP)

## High Power Power Supplies (FAP) ELP:List of front panel interlocks for FAP power supply modules

## AC Power Supplies (FAC)

ELP:List of front panel interlocks for FAC output stage power supply modules

ELP:List of front panel interlocks for FAC input stage power supply modules

ELP:List of front panel interlocks for FAC command rack power supply modules