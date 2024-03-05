---
title: Booster
description: 
published: 1
date: 2024-03-05T14:30:12.816Z
tags: 
editor: markdown
dateCreated: 2024-03-05T14:05:18.596Z
---

# Machine: Booster parameters

## Tables

### Major parameters

| Parameter | Value | Unit |
| --- | --- | ---|
| Lattice version | V03 |  |
| Beam extraction energy | 3.0 | GeV |
| Beam injection energy | 0.150 | GeV |
| Beam current | 2.0 | mA |
| Circumference | 496.800 | m |
| Revolution frequency | 0.603 | MHz |
| Revolution period | 1.657 | Î¼s |
| Cycling frequency | 2 | Hz |
| Betatron tune, horizontal | 19.204 |  |
| Betatron tune, vertical | 7.314 |  |
| Momentum compaction factor | 7.19×10-4 |  |
| Natural chromaticity, horizontal | -33.70 |  |
| Natural chromaticity, vertical | -13.95 |  |
| Natural emittance | 3.47 | nm⋅rad |
| Natural energy spread | 0.087 |  % |
| Damping time, horizontal | 11.3 | ms |
| Damping time, vertical | 13.8 | ms |
| Damping time, longitudinal | 7.7 | ms |
| RF frequency | 499.654 | MHz |
| Harmonic number | 828 | 

**Table 1**: Major Sirius BO main parameters.

### RF parameters

| Parameter | Value | Unit |
| --- | --- | ---|
| Beam energy | 3.0 | GeV |
| Beam current | 2.0 | mA |
| Energy loss/turn | 721.3 | keV |
| SR power | 1.44 | kW |
| Cavity type | PETRA 5-cell |  |
| Peak RF voltage | 1.05 | MV |
| Total scaled shunt impedance | 15 | MÃŽÂ© |
| Maximum RF power needed | 45.0 | kW |
| Energy spread | 0.0874 |  % |
| RF frequency | 499.654 | MHz |
| RF wavelength | 0.6000 | m |
| Harmonic number | 828 |  |
| Momentum compation factor | 7.19×10-4 |  |
| Overvoltage | 1.456 |  |
| Synchronous phase | 136.6 | Â° |
| Synchrotron tune | 0.0044 |  |
| Synchrotron frequency | 2.67 | kHz |
| Natural bunch length | 11.25 | mm |
| Natural bunch length | 37.53 | ps |
| Energy acceptance | 0.79 |  % |
| Quantum lifetime | 4267 | s |
| Linac to Booster phase stability @500MHz | 5.0 | ° 

**Table 2**: Parameters used to design the booster RF system. 

### Global closed orbit and coupling correction system

| Parameter | Value | Unit |
| --- | --- | ---|
| Number of BPMs | 50 |  |
| Number of horizontal dipole correctors | 25 |  |
| Number of vertical dipole correctors | 25 |  |
| Maximum horizontal dipole corrector strength | 310 | Î¼rad |
| Maximum vertical dipole corrector strength | 310 | Î¼rad

**Table 3**: Parameters of the global closed orbit and coupling correction system for the Booster.  

### Alignment and excitation errors

| Parameter | Dipoles | Quadrupoles | Sextupoles | BPMs | Unit |
| --- | --- | --- | --- | ---|
| Transverse position, x, y| 160 | 160 | 160 | 300 | Î¼m |
| Rotation around longitudinal axis | 0.8 | 0.8 | 0.8 | -- | mrad |
| Excitation error (static or low frequency) | 0.15 | 0.3 | 0.3 | -- |  % |
| Dipole Gradient Error | 2.4 | -- | -- | -- |  % 

**Table 4**: Maximum absolute value of random alignment and excitation errors for the Booster. The errors are generated with a Gaussian distribution truncated at ±1σ.

### 1.5 Orbit correction statistics

| Parameter | Horizontal | Vertical | Unit |
| --- | --- | --- | --- |
| COD rms | 238 | 380 | µm |
| COD rms @ BPMs | 247 | 284 | µm |
| Rms corrector strength | 60 | 89 | µrad |
| Max. corrector strength | 186 | 253 | µrad

**Table 5**: Statistics of orbit correction in the Booster for 20 random machines. 

### 1.6 Straight sections allocation

| Sector | U (upstream of QF) | D (downstream of QF) |
| --- | --- | --- |
| 01 | InjSept | InjKckr, Scrn-1, Scrn-2 |
| 02 | Scrn | QS, TuneShkr |
| 03 | | chicane |
| 04 | TunePkup | GSL |
| 05 | | P5Cav |
| 06 | |  |
| 07 | |  |
| 08 | | chicane |
| 09 | |  |
| 10 | |  |
| 11 | |  |
| 12 | |  |
| 13 | | chicane |
| 14 | |  |
| 15 | |  |
| 16 | |  |
| 17 | |  |
| 18 | | chicane |
| 19 | |  |
| 20 | |  |
| 21 | |  |
| 22 | |  |
| 23 | | chicane |
| 24 | |  |
| 25 | |  |
| 26 | |  |
| 27 | |  |
| 28 | | chicane |
| 29 | |  |
| 30 | |  |
| 31 | |  |
| 32 | |  |
| 33 | | chicane |
| 34 | |  |
| 35 | | DCCT |
| 36 | |  |
| 37 | |  |
| 38 | | chicane |
| 39 | |  |
| 40 | |  |
| 41 | |  |
| 42 | |  |
| 43 | | chicane |
| 44 | |  |
| 45 | |  |
| 46 | |  |
| 47 | | chicane |
| 48 | | EjeKckr |
| 49 | EjeSeptF |  |
| 50 | | 


QS = Skew Quadrupole

GSL = Generic Stripline

TunePkup = Tune Pickup

TuneShkr = Tune Shaker

InjKckr = Injection Kicker

InjSept = Injection Septum

EjeKckr = Ejection Kicker

Scrn = Fluorescent Screen 

### 1.7 Booster RF cavity

| Parameter | Value | Unit |
| --- | --- | ---|
| Number of cells | 5 |  |
| Fundamental frequency | 499.654 | MHz |
| Maximum gap voltage | 1.5 | MV |
| Nominal gap voltage | 1.1 | MV |
| Tuning range | ±0.2 | MHz |
| Minimum unloaded Q | 29,000 |  |
| Minimum R/Q | 370 | Ω/m |
| Minimum shunt impedance | 15 | MΩ |
| Dissipated cavity power @1.1MV | 33 | kW |
| Coupling factor | 1.04 |  |
| Operating temperature | 30 | °C |
| Detuning due to plunger position | 20 | kHz/mm |
| Total length between flanges | 1,800 | mm |
| Beam tube aperture | 120 | mm |
| Beam height | 1,400 | mm 

**Table 6**: Parameters of the Booster RF cavity. 
