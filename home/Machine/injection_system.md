---
title: Injection System
description: 
published: 1
date: 2024-03-05T15:35:25.416Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:21.285Z
---

# Machine: Injection System

<br />

## Introduction

The Sirius injection system is composed of a 150 MeV Linac, a full energy 3 GeV synchrotron booster operating in top-up mode and 2 transport lines, one from the Linac to the Booster (LTB) and another from the Booster to the Storage Ring (BTS). The booster and the storage ring are concentric and share the same tunnel. Their injection sections are placed close together to restrict the 'dirty' area in terms of radiation. A general layout of the Sirius injection system is shown in Figure 1. 

![LAYOUT INJECTION SYSTEM](/img/machine/injection_system/layout_inject_system.svg)

**Figure 1**: Layout of the Sirius injection system with a 150 MeV Linac and a full energy 3 GeV booster in the same tunnel as the storage ring. The booster and storage ring injection sections are placed close together to restrict the 'dirty' area in terms of radiation.

<br />

## Booster

### Linear Optics

The booster lattice consists of 50 modified FODO cells with combined-function magnets suitable to provide low emittance. The main difference from other booster designs is that the Sirius booster contains only arc sections: no long dispersion-free straight sections are provided. This means that injection and extraction, as well as the Petra 5-cell RF cavity, are located in these dispersive straight sections. With this concept a very high lattice symmetry for the booster is obtained and only a few magnet families are necessary. A high lattice symmetry is not only beneficial for beam dynamics but also to maximize the radial distance between the storage ring and the booster beam centers, minimizing the variations in the size of the corridor between the two concentric rings.

The lattice is composed of three main families of magnets: combined function dipoles (BD), with defocusing quadrupole and sextupole field components, focusing quadrupoles (QF) and focusing sextupoles (SF). Together, they define the working point and set the chromaticities to +0.5 in both planes. The achieved natural emittance at the extraction energy of 3 GeV is very low, which is essential to provide a clean injection process into the storage ring with the nonlinear kicker injection process.

The families of focusing quadrupoles QF and the defocusing quadrupolar component in the dipoles BD set the nominal horizontal and vertical tunes. In order to allow for flexibility in tune adjustment, an extra family of weak corrector quadrupoles QD is added to the lattice. A QD quadrupole is placed every two dipoles, right next to it. In the same way, the chromaticities are set to +0.5 in both planes by the family of sextupoles SF and the defocusing sextupolar component in the dipoles BD; and to allow flexibility for chromaticity adjustment, an extra family of corrector sextupoles SD is introduced. A sextupole corrector SD is placed every five dipoles in the lattice. There are 2 kinds of straight sections connecting the dipoles: odd sections contain orbit correctors and even sections contain quadrupoles QD and sextupoles SF. All sections contain quadrupoles QF and BPMs. Ten sextupoles SD are distributed in odd and even sectors. A schematic diagram of the Booster straight sections is shown in Figure 3 

The booster main parameters are summarized in Table 1 and Table 2, and the optical functions are shown in Figure 2. 

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
| Momentum compaction factor | 7.19×10⁻⁴ |  |
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

#### Dipoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Name | DipB |  |
| Number | 50 |  |
| Length | 1.221 | m |
| Dipole field (min/max) | 0.0515 / 1.030 | T |
| Bending radius | 9.716 | m |
| Integrated* quadrupole grad. (min/max) | 0.12 / 2.48 | T |
| Integrated* sextupole grad., ∫B"/2.ds, (min/max) | 1.28 / 25.63 | TÂ·m-1 |

**Table 2**: Sirius booster dipoles main parameters. 

*integration along particle trajectory. 

#### QF Quadrupoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Name | QF |  |
| Number | 50 |  |
| Effective magnetic length | 0.228 | m |
| Maximum gradient | -18.7 | TÂ·m-1 |

**Table 3**: Sirius booster QF quadrupoles main parameters. 

<br />

#### QD Quadrupoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Name | QD |  |
| Number | 25 |  |
| Effective magnetic length | 0.100 | m |
| Maximum gradient | ± 5.3 | TÂ·m-1 |

**Table 4**: Sirius booster QD quadrupoles main parameters. 

<br />

#### QS (skew) Quadrupoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Name | QS |  |
| Number | 1 |  |
| Effective magnetic length | 0.100 | m |
| Maximum gradient | ± 1.6 | TÂ·m-1 |

**Table 5**: Sirius booster QS quadrupoles main parameters. 

<br />

#### Sextupoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Names | SF and SD |  |
| Number (SF + SD) | (25 +10) |  |
| Effective magnetic length | 0.105 | m |
| Max. integrated gradient, ∫B"/2.ds | 200.14 | TÂ·m-2 |

**Table 6**: Sirius booster sextupoles main parameters. 

![BOOSTER TWISS](/img/machine/injection_system/bo_twiss.svg)

**Figure 2**: Twiss functions for V02.

![BOOSTER STRAIGHT SECTIONS](/img/machine/injection_system/bo_straight_sections.png)

**Figure 3**: Booster straight sections. All 50 sections contain a QF in the center and a BPM in the Upstream part. Odd sections contain correctors CH and CV in the Upstream part, and Even sections contain SF (Upstream) and QD (Downstream). Section 49, where extraction septa are located, is an exception with CH in the Downstream part. The 10 sextupoles SD are distributed in Odd and Even sections.


### Tune correction

Tune correction in the Sirius Booster will be performed with QF and QD families: 

$$
\begin{bmatrix} \nu_x\\ \nu_y \end{bmatrix} = 
\begin{bmatrix} 19.204\\7.314 \end{bmatrix}+
\begin{bmatrix} 92.6900 &   4.1213 \\-21.1086 & -39.2987\end{bmatrix} \times
\begin{bmatrix}Q_F-0.377 \\Q_D+0.001\end{bmatrix}
$$

where $\nu$ is the tune and $Q [m^{-1}]$ is the integrated quadrupole strength.

<br />

### Chromaticity Correction

Chromaticity correction in the Sirius Booster will be performed with SF and SD families. 

$$
\begin{bmatrix} \xi_x\\ \xi_y \end{bmatrix} = 
\begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} +
\begin{bmatrix} 30.1642  &  0.2808 \\ -8.1027  & -2.7899 \end{bmatrix} \times
\begin{bmatrix} S_F - 1.189\\ S_D - 0.742 \end{bmatrix}
$$

where $\xi$ is the chromaticity and $S [m^{-2}]$ is the integrated sextupole strength. From the above equation, we notice the chromaticity is corrected to 0.5 in both planes when $S_F$ and $S_D$ are equal to 1.189 and 0.742, respectively. 

To specify the maximum SD integrated strength, we considered, among others, the effect of a systematic error of 12% in the sextupolar component of the dipoles and a range of variation of chromaticity of [0.5,4.0] in both planes.

<br />

### Error Tolerance Specifications 

Assumed multipole errors for Booster dipoles, quadrupoles and sextupoles are shown in Table 3, Table 4 and Table 5 

<br />

#### Booster Magnets Multipole Errors

##### Dipoles @r = 17.5 mm

|  Multipole error | Systematic <br />Normal| Random <br />Normal | Random <br />Skew|
| --- | --- | --- |--- |
| B2/B0 (sextupole) | - | 5.5×10⁻⁴ * | 1.0×10⁻⁴ |
| B3/B0 (octupole) | +4.0×10⁻⁵ | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B4/B0 (decapole) | -3.6×10⁻⁴ | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B5/B0 (12-pole) | +2.7×10⁻⁵ | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B6/B0 (14-pole) | -1.3×10⁻⁴ | 4.0×10⁻⁴ | 1.0×10⁻⁴ |

**Table 7**: Booster dipole multipole errors specification. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

*This spec is replicated in the dipole alignment and rotation errors table. Actual designed dipole model shows numbers are that in accordance with these specs. (see fieldmap analysis) 

##### Quadrupoles @r = 17.5 mm

|  Multipole error | Systematic¹ | <br />Random <br />Normal | <br />Random <br />Skew|
| --- | --- | --- | --- |
| B2/B1 (sextupole) | -- | 7.0×10⁻⁴ | 1.0×10⁻³ |
| B3/B1 (octupole) | -- | 4.0×10⁻⁴ | 5.0×10⁻⁴ |
| B4/B1 (decapole) | -- | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B5/B1 (12-pole) | -1.0×10⁻³ | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B6/B1 (14-pole) | -- | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B7/B1 (16-pole) | -- | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B8/B1 (18-pole) | -- | 4.0×10⁻⁴ | 1.0×10⁻⁴ |
| B9/B1 (20-pole) | +1.1×10⁻³ | -- | -- |
| B13/B1 (28-pole) | +8.0×10⁻⁵ | -- | -- |

**Table 8**: Booster QF quadrupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

¹ Multipoles of prototype magnets measured with radial rotating coils 

<br />

##### Sextupoles @r = 17.5 mm

|  Multipole error | Systematic¹ <br />Normal| Random <br />Normal | Random <br />Skew|
| --- | --- | --- | --- |
| B3/B2 (octupole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B4/B2 (decapole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B5/B2 (12-pole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B6/B2 (14-pole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B7/B2 (16-pole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B8/B2 (18-pole) | -2.7×10⁻² | 4.0×10-⁴ | 1.0×10-⁴ |
| B9/B2 (20-pole) | -- | 4.0×10-⁴ | 1.0×10-⁴ |
| B14/B2 (30-pole) | -1.4×10-2 | -- | -- |

**Table 9**: Booster sextupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.  

¹ Relative multipoles calculated around the Runge-Kutta trajectory for the latest sextupole model-03 fieldmap at 3 GeV 

<br />

#### Booster Magnets Alignment and Excitation Errors

| Parameter | Dipoles | Quadrupoles | Sextupoles | BPMs | Unit |
| --- | --- | --- | --- |--- |--- |
| Transverse position, x, y | 160 | 160 | 160 | 300 | Î¼m |
| Rotation around longitudinal axis | 0.8 | 0.8 | 0.8 | -- | mrad |
| Excitation error (static or low frequency) | 0.15 | 0.3 | 0.3 | -- |  % |
| Dipole Gradient Error | 2.4 | -- | -- | -- |  %  |

**Table 10**: Maximum absolute value of random alignment and excitation errors for the Booster. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### Booster Magnets High Frequency Errors

| Parameter | Value | Unit |
| --- | --- | --- |
| Girder vibration rms amplitude | 500 | nm |
| Power supply ripple | |  |
| Tracking error | 100 | ppm |

**Table 11**: Booster magnets high frequency errors. 

<br />

### Closed orbit correction system

The specification for the closed orbit correction system for the Sirius booster is in Table 12 and its distribution along the ring is shown in Figure 4. To calculate corrector kicks and estimate residual orbit displacements, we have simulated static orbit distortions due to random alignment and excitation errors in all magnets in the lattice (see Table 10). These are relaxed error tolerances, we expect better results for the real machine. The implicit safety margin that is assumed should account for the dynamic effects during energy ramping that were not taken into account in these calculations. The closed orbit before correction is shown in Figure 5 and the residual closed orbit distortion after correction is shown in Figure 6. The corrector strengths are listed in Table 13

![BOOSTER LATTICE](/img/machine/injection_system/bo_lattice.svg)

**Figure 4**: Booster lattice

| Parameter | Value | Unit |
| --- | --- | --- |
| Number of BPMs | 50 |  |
| Number of horizontal dipole correctors | 25 |  |
| Number of vertical dipole correctors | 25 |  |
| Maximum horizontal dipole corrector strength | 310 | Î¼rad |
| Maximum vertical dipole corrector strength | 310 | Î¼rad

**Table 12**: Parameters of the global closed orbit and coupling correction system for the Booster. 

![BOOSTER UNCORR COD](/img/machine/injection_system/sr_bo_cod_uncorrected.svg)

**Figure 5**: Horizontal (blue) and vertical (red) uncorrected closed orbit for 20 random booster machines. The bold curves represent one rms value.

![BOOSTER CORR COD](/img/machine/injection_system/sr_bo_cod_corrected.svg)

**Figure 6**: Horizontal (blue) and vertical (red) corrected closed orbit for 20 random booster machines. The bold curves represent one rms value.

| Parameter | Horizontal | Vertical | Unit |
| --- | --- | --- | --- |
| COD rms | 238 | 380 | µm |
| COD rms @ BPMs | 247 | 284 | µm |
| Rms corrector strength | 60 | 89 | µrad |
| Max. corrector strength | 186 | 253 | µrad |

**Table 13**: Statistics of orbit correction in the Booster for 20 random machines. 

<br />

### Aperture requirements

The physical aperture requirements for the booster are defined by the injected Linac beam size and energy variation from pulse to pulse, by the closed orbit distortions and by a tolerance for beam oscillations after injection. During acceleration the beam size shrinks as well as the oscillations due to mismatched energy, position and angle of the injected beam.

The beam stay clear (half-aperture) was defined by the following formulae:

$Ax = 4 \sqrt{\beta _x \epsilon _x (170 nm.rad) + (\eta _x \sigma _{\delta} (0.5 \%))²} + x_COD(1mm) + x_{osc}(4.5mm) + \eta_x \delta_{osc} (1.5\%) = 17.5 mm$ at quadrupoles

$Ay = 4 \sqrt{\beta_y \epsilon_y(170 nm.rad)} \qquad\qquad\qquad\quad + y_{COD}(1mm) + y_{osc}(1.5mm) \qquad\qquad\qquad\,\, = 11.7 mm$ at dipoles

The resulting requirements are illustrated in Figure 7. 

![BOOSTER APERTURE REQS](/img/machine/injection_system/bo_aperture_reqs.png)

**Figure 7**: The half-aperture requirements for the Booster are based on error tolerances for the injected beam at 120 MeV. Allowances in both planes (horizontal and vertical) have been set for orbit distortions and residual beam oscillations due to errors in meeting the on-axis injection conditions. In the horizontal plane, an extra allowance is set for a Linac beam energy mismatch.

The booster vacuum chambers will be made of 1 mm thick stainless steel cylindrical tubes with inner diameter of 23.4 mm at the dipoles and 36 mm at the straight sections. 

<br />

### Dynamic aperture

The chromaticity correction sextupoles, multipole components in dipoles and quadrupoles, and alignment errors reduce the dynamic aperture to about ±12 mm in the horizontal and ±4 mm in the vertical plane at the injection point. This is sufficiently large for an efficient on-axis injection and for beam lifetime. Figure 8, Figure 9 and Figure 10 show the dynamic and momentum apertures for 20 machines with random multipole, alignment and excitation errors in all magnets. 

![BOOSTER MULTICOD TUNE DAXY](/img/machine/injection_system/bo_multi_cod_tune_daxy.png)

**Figure 8**: On-momentum dynamic aperture at the center of quadrupole QF for 20 machines with alignment and multipole errors, orbit and tune corrections. The color scale represents the percentage of machines in which a given point of the grid is stable. For these calculations, the following configuration was used: 6D tracking with Trackcpp; 5000 turns for on-momentum and off-momentum apertures; The vacuum chamber physical aperture (17.5x17.5 mm² in the straights and 12x12 mm² in the dipoles) is considered along the ring.

![BOOSTER MULTICOD TUNE DAEX](/img/machine/injection_system/bo_multi_cod_tune_daex.png)

**Figure 9**: Off-momentum dynamic aperture at the center of quadrupole QF for 20 machines with alignment and multipole errors, orbit and tune corrections. The color scale represents the percentage of machines in which a given point of the grid is stable. For these calculations, the following configuration was used: 6D tracking with Trackcpp; 3500 turns for on-momentum and off-momentum apertures; The vacuum chamber physical aperture (17.5x17.5 mm² in the straights and 12x12 mm² in the dipoles) is considered along the ring.

![MA BOOSTER MULTICOD](/img/machine/injection_system/bo_multi_cod_tune_Tous_LT.svg)

**Figure 10**: Momentum aperture for 1/10 of the Booster for 20 machines with alignment and multipole errors, orbit and tune corrections. For this calculation, the following configuration was used: 6D tracking with Trackcpp; 2000 turns; The vacuum chamber physical aperture (17.5x17.5 mm² in the straights and 12x12 mm² in the dipoles) is considered along the ring. Black lines represent the loss rate.

<br />

### Booster injection

The 150 MeV electron beam from the Linac is injected on axis into the booster. The injection septum and the on-axis injection kicker are shown in Figure 43, the horizontal trajectory of the injected beam in Figure 12 and a cross section at the injection point in Figure 13. The injection point at the booster is defined at the physical end of the injection septum. 

![BOOSTER INJECTION SECTION LAYOUT](/img/machine/injection_system/bo_inject_sec_layout.svg)

**Figure 11**: Booster injection section layout.

![BOOSTER INJECTION TRAJECTORY](/img/machine/injection_system/bo_inject_trajectory.png)

**Figure 12**: Trajectory of the injected beam from the Linac in the horizontal plane. The solid red curve represents the injected beam centroid and the dashed curves represent ±3σx beam envelope.

![BOOSTER INJECTION XY](/img/machine/injection_system/bo_injection_xy.svg)

**Figure 13**: Schematic representation of the transverse cross section at booster injection point. Incoming beam from TB is moving towards the viewer.

<br />

### Booster extraction

Two kickers are used to extract the beam from the booster. They deflect the beam towards the extraction septum, passing through a defocusing dipole and a tune corrector quadrupole along the way. The nominal strength for this quadrupole is zero, it will only be used for small tune corrections. The arrangement of the booster extraction system elements is shown in Figure 14. 

![BOOSTER EXTRACTION LAYOUT](/img/machine/injection_system/bo_extract_layout.svg)

**Figure 14**: Booster extraction layout.

The extracted beam horizontal trajectory is shown in Figure 15. Due to the large amplitude of the extracted beam, the horizontal size of the dipole vacuum chamber next to the septum will have to be increased. The beam arrives at the septum with an amplitude of x=22 mm and angle of x'=5.0 mrad. This amplitude considers: 

| Element | Value | Unit |
| --- | --- | --- |
| half-aperture for stored beam | 18.0 | mm |
| vacuum chamber thickness | 1.0 | mm |
| septum thickness | 3.3 | mm |
| half-aperture for extracted beam (4σ) | 1.0 | mm |
| **Total** | **23.3** | **mm** |

**Table 14**: Booster extraction apertures. 

![BOOSTER EXTRACTION TRAJECTORY](/img/machine/injection_system/bo_extract_trajectory.jpg)

**Figure 15**: Trajectory of the extracted beam from the booster in the horizontal plane. The solid red curve represents the extracted beam trajectory calculated by the linear model and the dashed curves represent ±4σx beam envelope. The green curve is the horizontal beam stay clear. Due to the large amplitude of the extracted beam at the dipole, the beam trajectory has also been calculated by Runge-Kutta integration using the simulated dipole field map (dark blue curve).

![BOOSTER EXTRACTION XY](/img/machine/injection_system/bo_extract_xy.svg)

**Figure 16**: Schematic representation of transverse cross section at booster extraction point.

<br />

### Booster RF system

Table:Booster RF parameters shows the design parameters of the RF system for the booster. The value of the Peak RF voltage presented in the table was calculated assuming the energy spread of the beam could be 90% larger than the expected value, also present in the table, and the momentum compaction could be 30% higher than the value in the table. These are very pessimistic scenarios for the system design, being the nominal 

| Parameter | Value | Unit |
| --- | --- | --- |
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
| Linac to Booster phase stability @500MHz | 5.0 | ° |

**Table 15**: Parameters used to design the booster RF system. 

<br />

### Booster straight sections allocation
| Sector | U (upstream of QF) | D (downstream of QF) |
| --- | --- | --- |
| 01 | InjSept | InjKckr, Scrn-1, Scrn-2 |
| 02 | Scrn | QS, TuneShkr |
| 03 | | `chicane` |
| 04 | TunePkup | GSL |
| 05 | | P5Cav |
| 06 | |  |
| 07 | |  |
| 08 | | `chicane` |
| 09 | |  |
| 10 | |  |
| 11 | |  |
| 12 | |  |
| 13 | | `chicane` |
| 14 | |  |
| 15 | |  |
| 16 | |  |
| 17 | |  |
| 18 | | `chicane` |
| 19 | |  |
| 20 | |  |
| 21 | |  |
| 22 | |  |
| 23 | | `chicane` |
| 24 | |  |
| 25 | |  |
| 26 | |  |
| 27 | |  |
| 28 | | `chicane` |
| 29 | |  |
| 30 | |  |
| 31 | |  |
| 32 | |  |
| 33 | | `chicane` |
| 34 | |  |
| 35 | | DCCT |
| 36 | |  |
| 37 | |  |
| 38 | | `chicane` |
| 39 | |  |
| 40 | |  |
| 41 | |  |
| 42 | |  |
| 43 | | `chicane` |
| 44 | |  |
| 45 | |  |
| 46 | |  |
| 47 | | `chicane` |
| 48 | | EjeKckr |
| 49 | EjeSeptF |  |
| 50 | | 

**Table 16**: Booster straight sections allocation 

QS = Skew Quadrupole
GSL = Generic Stripline
TunePkup = Tune Pickup
TuneShkr = Tune Shaker
InjKckr = Injection Kicker
InjSept = Injection Septum
EjeKckr = Ejection Kicker
Scrn = Fluorescent Screen 

<br />

## Linac 

The Sirius 150 MeV Linac is a 'turn-key' system provided by SSRF/SINAP. The Linac design parameters are specified in Table 17. 

| Parameter | Multi-bunch | Single-bunch | Unit |
| --- | --- | --- | --- |
| Energy | 150 | 150 | MeV |
| Frequency (e-gun and SHB) | 499.664 | 499.664 | MHz |
| Frequency (accelerating structures) | 2997.948 | 2997.948 | MHz |
| Normalized emittance | ≤ 50 | ≤ 50 | Ï€Â·mmÂ·mrad |
| Relative energy spread (rms) | ≤ 0.5 | ≤ 0.5 |  % |
| Pulse to pulse energy variation | ≤ 0.25 | ≤ 0.25 |  % |
| Pulse to pulse beam position variation | ≤ 0.20 | ≤ 0.20 | mm |
| Pulse to pulse jitter | ≤ 100 | ≤ 100 | ps |
| Pulse charge | ≥ 3 | ≥ 1 | nC |
| Pulse duration | 150 to 300 | ≤ 1 | ns |
| Repetition rate | 2 | 2 | Hz |

**Table 17**: Main parameters of Sirius Linac in multi-bunch and single-bunch operation modes. 

![LINAC LAYOUT](/img/machine/injection_system/li_layout.png)

**Figure 17**: General layout of Sirius 150 MeV Linac.

![LINAC LAYOUT2](/img/machine/injection_system/li_layout2.png)

**Figure 18**: Linac layout in detail.

![LINAC SCHEME](/img/machine/injection_system/li_scheme.png)

**Figure 19**: Schematic diagram of Sirius 150 MeV Linac.

<br />

### Linac pictures during FAT at SSRF

![LINAC SSRF1](/img/machine/injection_system/li_ssrf1.png) ![LINAC SSRF2](/img/machine/injection_system/li_ssrf2.png)

![LINAC SSRF3](/img/machine/injection_system/li_ssrf3.png) ![LINAC SSRF4](/img/machine/injection_system/li_ssrf4.png)

**Figures 20, 21, 22 and 23**: Pictures at SSRF

<br />

## Linac to booster transport line (LTB) 

The Linac-to-Booster transport line (LTB - naming initials TB), transports the 150 MeV electron beam from the end of the Linac (by definition, just after the last accelerating section) to the booster injection point, just after the injection septum. A general view of the LTB transport line is shown in Figure 24. A schematic diagram of the LTB elements with their names is shown in Figure 25. The main parameters are shown in Table 18. 

![LTB INJECTION LAYOUT](/img/machine/injection_system/ltb_inject_layout.svg)

**Figure 24**: Overview of the LTB transfer line.

![LTB DETAIL](/img/machine/injection_system/ltb_detail.png)

**Figure 25**: LTB transfer line in detail

| Parameter | Value | Unit |
| --- | --- | --- |
| Nominal energy | 150.0 | MeV |
| Lattice version | V02 |  |
| Total length including septum | 21.2475 | m |

**Table 18**: Main parameters of the LTB transfer line. 

<br />

### LTB Lattice

The LTB lattice is composed of two chromatic sections separated by an achromatic section. In the first chromatic section just after the Linac the dispersion function is negative, created by two negative deflection dipoles. The first dipole is also a beam energy spectrometer for the Linac. An energy slit is placed in this section at the position where the energy resolution is maximum, i.e., where the relation ηx/βx is maximum. In the achromatic section, the LTB line goes through a shielding wall separating the Linac from the storage ring tunnel. In the last chromatic section the dispersion is positive and the optical functions are matched to the Booster's functions. The beam is injected on-axis into the Booster. 

Since the optical functions at the Linac exit are not precisely known, we have considered 6 different initial condition modes (M1, ... , M6) for the transport line and looked for solutions that are flexible enough to accommodate all modes. The initial Twiss functions for the modes are shown in Table 19, where several different combinations of initial αx and αy are covered. The corresponding optical functions are shown in Table 16. 

![TABLE LTB TWISS](/img/machine/injection_system/tab_twiss_ltb.png)

**Table 19**: Initial Twiss functions for the LTB transfer line modes, and matching parameters at booster injection point.

![TABLE TWISS LTB](/img/machine/injection_system/tab_ltb_twiss_M4.svg)

**Table 20**: Optical functions along the LTB transfer line for 6 different initial condition modes. 

<br />

### LTB Beam Size and Aperture Requirement

The figures below show the horizontal and vertical beam sizes along LTB for the different modes M1 to M6. The beam parameters at the Linac end are: emittance: εx = εy = 170 nm.rad; rms energy spread: δ=0.5%. 

![LTB BEAMSIZE HOR](/img/machine/injection_system/ltb_beamsize_hor.png)

**Figure 26**: Horizontal beam size along LTB transfer line for various operation modes. Different operation modes correspond to different initial conditions for the optical functions at the Linac end. The beam sizes are calculated for the following parameters: beam energy=150 MeV; emittance: εx = εy = 170 nm.rad; rms energy spread: δ=0.5%.

![LTB BEAMSIZE VERT](/img/machine/injection_system/ltb_beamsize_vert.png)

**Figure 27**: Vertical beam size along LTB transfer line for various operation modes. Different operation modes correspond to different initial conditions for the optical functions at the Linac end. The beam sizes are calculated for the following parameters: beam energy=150 MeV; emittance: εx = εy = 170 nm.rad; rms energy spread: δ=0.5%.

The aperture requirements and BSC for the LTB transport line are calculated considering a clearance for residual orbit distortion and trajectory variations due to pulse to pulse differences in beam energy and launching conditions (position and angle) as described in Table 21. 

| Parameter | Value | Unit |
| --- | --- | --- |
|Max. orbit distortion along LTB (H and V) | ± 1 | mm |
| Linac pulse to pulse energy variation | 0.4 |  % |
| Linac pulse to pulse beam centroid position/angle variation (H and V) | 40 | nm.rad |
| LTB vacuum chamber inner aperture (full) at quadrupoles (H / V) | 36.1 / 36.1 | mm |
| LTB vacuum chamber inner aperture (full) at dipoles (H / V) | 23.4 / 23.4 | mm |
| Number of beam sigmas that fit in the aperture (H / V) | ± 3.3 / ± 4.6 | |

**Table 21**: Parameters for LTB transfer line aperture and BSC calculations. 

The calculated horizontal and vertical BSC for LTB transport line modes are shown in the figures below. 

![LTB BSCH](/img/machine/injection_system/ltb_bsch.png)

**Figure 28**: Horizontal beam stay clear (BSC) for LTB transfer line. The BSC can accommodate the residual orbit distortion and trajectory variations due to pulse to pulse differences in beam energy and launching conditions (position and angle) described in Table 18. The vacuum chamber inner half-aperture is represented by the solid black curve.

![LTB BSCV](/img/machine/injection_system/ltb_bscv.png)

**Figure 29**: Vertical beam stay clear (BSC) for LTB transfer line. The BSC can accommodate the residual orbit distortion and trajectory variations due to pulse to pulse differences in launching conditions (position and angle) described in Table 18. The vacuum chamber inner half-aperture is represented by the solid black curve.

<br />

### LTB Orbit Correction

The LTB orbit correction parameters are shown in Table 19 and the magnet alignment and excitation error tolerances assumed for orbit correction studies in the LTB transport line are shown in Table 20. The trajectory correction statistics are shown in Table 25 and the orbits before and after correction for all modes are shown in Table 26. The correction system uses a beam position measurement station with integrated fluorescent screens and striplines. The injection septum is used as corrector to adjust horizontal position and angle at the booster injection point. 

| Parameter | Value | Unit |
| --- | --- | --- |
| Number of beam position measurement stations | 6 |  |
| Number of horizontal correctors | 6 |  |
| Number of vertical correctors | 6 |  |
| Maximum corrector strength | ± 2.5 | mrad |

**Table 22**: Parameters for LTB transfer line orbit correction. 

<br />

#### Errors for LTB transfer line orbit correction simulation. 

A uniform random error distribution is assumed. 

| Error | Range | Unit |
| --- | --- | --- |
| X alignment | ±0.3 | mm |
| Y alignment | ±0.3 | mm |
| Roll angle | ±0.4 | mrad |
| Relative field error | ±0.1 |  %  |

**Table 23**:  Type of error (applied to all magnets) 

| Error | Range | Unit |
| --- | --- | --- |
| X alignment | ±0.5 | mm |
| Y alignment | ±0.5 | mm  |

**Table 24**:  BPM alignment error 

| Error | Range | Unit |
| --- | --- | --- |
| x | ±0.4 | mm |
| θx | ±0.1 | mrad |
| y | ±0.4 | mm |
| θy | ±0.1 | mrad |
| dp/p | ±0.5 |  %  |

**Table 25**:  Error in beam launching conditions 

<br />

#### Orbit correction statistics

Over 100 random seeds for LTB transfer line modes M1 to M6 were used.

| Element | Before | After |
| --- | --- | --- |
| Max. rms H orbit | 2.1 ± 0.14 | 0.53 ± 0.02 |
| Max. rms V orbit | 1.6 ± 0.29 | 0.40 ± 0.02 |
| Max. rms H orbit @ BPMs | 1.6 ± 0.09 | 0.31 ± 0.01 |
| Max. rms V orbit @ BPMs | 1.5 ± 0.27 | 0.31 ± 0.004 |
| Average H peak-to-peak | 3.8 ± 0.26 | 1.17 ± 0.02 |
| Average V peak-to-peak | 1.8 ± 0.23 | 0.87 ± 0.02  |

**Table 26**:  Orbit in mm 

| Element | Before | After |
| --- | --- | --- |
|  | rms | max |
| CH | 0.63 ± 0.03 | 1.88 ± 0.12 |
| CV | 0.38 ± 0.013 | 1.85 ± 0.13 |
| septum | 2.27 ± 0.13 | 5.9 ± 0.3 |

**Table 27**:  Corrector strength in mrad 

![TABLE LTB ORBIT](/img/machine/injection_system/tab_M4_Orbit.svg)

**Table 28**: Orbit along the LTB transfer line for modes M1 to M6. For each mode, 100 random machines are simulated with errors given in Table xx??. The bold solid curves represent one sigma of the orbit distribution. 


### LTB Diagnostic Elements 
The LTB diagnostics elements are summarized in Table 29. 

| Measurement | Probe type | Resolution |
| --- | --- | --- |
| Bunch waveform (micro & macro bunch) | Stripline BPM | 1% peak value |
| Bunch charge | ICT | 2.0 % |
| Position | Stripline BPM | 0.2 mm |
| Fluorescent screen | 0.5 mm |
| Profile | Fluorescent screen | 0.5 mm |
| Energy slit / collimation | Beam scraper | 0.1 mm |

**Table 29**: LTB diagnostics elements.

![LTB DIAGNOSTICS](/img/machine/injection_system/ltb_diagnostics.png)

**Figure 30**: Schematic layout of LTB diagnostic elements.

<br />

#### LTB Horizontal/Vertical Scrapers

A horizontal scraper with a pair of blades will be used in the LTB line as energy slit, to select the portion of the beam coming from the Linac that is within the Booster energy acceptance at injection energy. For this purpose it is installed at a high dispersion and low horizontal betatron function place. An identical scraper will also be installed in the vertical plane, at a high vertical betatron function place, to reduce particle losses at the septum or in the Booster. 

Specifications for the LTB horizontal and vertical scrapers are given in Table 30. 

| Parameter | Value | Unit |
| --- | --- | --- |
| Quantity of scrapers | 2 | (1 horizontal + 1 vertical) |
| Number of blades per scraper * | 2 |  |
| Blade position resolution (transverse) | 10 | μm |
| Position accuracy | 100 | μm |
| Position repeatability | 50 | μm |
| Motion range per blade ** | 20 | mm |

**Table 30**: Specifications for LTB transfer line scrapers. 

*Blades with independent movement 

**Vacuum chamber diameter ∅=36 mm 

<br />

#### LTB Beam Position Measurement Stations

Beam position measurement stations combining a stripline BPM and a fluorescent screen will be used in the LTB line to measure the beam position. The specifications for the stripline BPMs are shown in Table 31 and for the fluorescent screens in Table 32. 

| Parameter | Value | Unit |
| --- | --- | --- |
| Quantity | 6 |  |
| Dynamic range | 50 | dB |
| Alignment accuracy | 0.5 | mm |
| Measurement accuracy | 0.2 | mm |
| Resolution @ 1 nC | 100 | μm |
| Measurement range (radius) | ± 5 | mm  |

**Table 31**: Specifications for LTB transfer line stripline BPMs. 

| Parameter | Value | Unit |
| --- | --- | --- |
| Quantity | 6 |  |
| Spatial resolution (transverse) | 0.2 | mm |
| Mechanical positioning accuracy | 0.2 | mm |
| Mechanical positioning repeatability | 0.1 | mm |

**Table 32**: Specifications for LTB transfer line fluorescent screens. 

<br />

#### LTB ICTs

Two Integrating Current Transformers (ICTs) will be installed at the LTB extremities allowing measurements of its transmission efficiency. The first ICT is being purchased as part of the Linac. The specifications for the LTB ICTs are shown in Table 33. 

Model: ID 34.9 - Bergoz CF4.5"-34.9-40/1.1

| Parameter | Value | Unit |
| --- | --- | --- |
| Quantity | 3 | (1 from Linac + 2) |
| Dynamic range | 50 | dB |
| Resolution | 2 |  % |

**Table 33**: Specifications for LTB transfer line ICTs. 

<br />

## Booster to storage ring transport line (BTS) 

The main function of the booster-to-storage ring transport line (BTS - with naming initials TS), is to transport the 3.0 GeV electron beam from the booster synchrotron to the storage ring (SR). The geometric requirements for this line are determined by the lattice of the two accelerators located in the same machine tunnel. Since the BTS line traverses the machine tunnel, a long element-free drift section is required to facilitate the passage of people and equipment through this region. To save costs, the BTS line uses the same quadrupoles as the storage ring and same dipoles and correctors as the booster. The booster dipole is scaled to a lower value as compared to the booster peak value, so that it can be set to DC operation without overheating the coils. 

A general view of the BTS transport line is shown in Figure 30. A schematic diagram of the BTS elements with their names is shown in Figure 31. The main parameters are shown in Table 29. 

![BTS INJECTION LAYOUT](/img/machine/injection_system/bts_inject_layout.svg)

**Figure 30**: Overview of the TS transfer line.

![TRANSFER LINE DETAIL](/img/machine/injection_system/tl_detail.png)

**Figure 31**: TS transfer line in detail.

| Parameter | Value | Unit |
| --- | --- | --- |
| Operation energy | 3.0 | GeV |
| Lattice version | V03 |  |
| Total length including septa | 26.89 | m |
| Number of dipoles | 3 |  |
| Number of quadrupoles | 8 |  |
| Number of horizontal correctors (CH + septa) | 4 + 2 |  |
| Number of vertical correctors | 6 |  |

**Table 34**: Main parameters of the BTS transfer line. 

<br />

### BTS Lattice

The BTS lattice is designed with the same magnetic elements of the Booster (dipoles and correctors) and of the Storage Ring (quadrupoles Q14 and Q20). We define the BTS transport line from the Booster extraction septum to the Storage Ring thin injection septum, with both septa included.

The BTS initial optical conditions are matched to the Booster parameters at the extraction point, but the final conditions are mismatched to optimize the injection efficiency into the storage ring with a nonlinear kicker (NLK). The 2 modes M1 and M2 are optimized for different positions of the injected beam at the NLK. Mode M1 assumes the beam is injected at x=-8.0 mm, close to the NLK field maximum, and mode M2 assumes the beam is injected at x=-5.3 mm, where the NLK field has a slope. We expect to inject the beam close to the NLK field maximum, but, for safety, in case the dynamic aperture is not sufficiently large in the beginning, we have studied the possibility of injecting the beam closer to the storage ring axis.

In addition to usual requirements for beam transmission, the BTS transport line optics also requires a free space to allow people and equipment to pass by bending below the beam pipe.

The parameters of the injected beam at the booster extraction point, SR injection point and NLK for the 2 modes are shown in Table 31 and the corresponding optical functions are shown in Figure 32. 

| Parameter |  Booster extraction point |  Storage Ring injection point <br />M1 | Storage Ring injection point <br />M2 | NLK <br />M1 | NLK <br />M2 | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| βx | 9.321 | 7.803 | 11.649 | 4.0 | 5.0 | m |
| αx | -2.647 | 0.975 | 1.305 | 0.0 | 0.4 |  |
| βy | 12.881 | 4.902 | 4.902 | 6.66 | 6.66 | m |
| αy | 2.00 | 0.186 | 0.186 | -0.637 | -0.637 |  |
| ηx | 0.231 | 0.0 | 0.0 | 0.0 | 0.0 | m |
| η'x | 0.069 | 0.0 | 0.0 | 0.0 | 0.0 | |

**Table 35**: Beam parameters at the booster extraction point and storage ring injection point optimized for injection with NLK. 

![TRANSFER LINE TWISS M1M2](/img/machine/injection_system/tl_twiss_m1m2.svg)

**Figure 32**: Optical functions along the BTS transfer line for operation modes M1 and M2.

The considerations for the extracted beam amplitude at the booster extraction septum are described in Table 14, and the considerations for the injected beam aperture at the storage ring injection point (end of thin septum), in Table 36. 

| Element | Value | Unit |
| --- | --- | --- |
| half-aperture for stored beam | 18.0 | mm |
| vacuum chamber thickness | 1.0 | mm |
| septum thickness | 3.3 | mm |
| half-aperture for extracted beam (4σ) | 1.0 | mm |
| **Total** | **23.3** | **mm** |

**Table 14**: Booster extraction apertures. 

| Element | Value | Unit |
| --- | --- | --- |
| half-aperture for stored beam | 12.0 | mm |
| vacuum chamber thickness | 1.0 | mm |
| septum thickness | 3.35 | mm |
| half-aperture for extracted beam (4σ) | 1.0 | mm |
| **Total** | **23.3** | **mm** |

**Table 36**: Storage ring injection apertures. 

<br />

### BTS Beam Size and Aperture Requirement

The figures below show the horizontal and vertical beam sizes along BTS for the modes M1 and M2. 

![BTS BEAM SIZE HOR](/img/machine/injection_system/bts_beam_size_H.png)

**Figure 33**: Horizontal beam size along the BTS transfer line for modes M1 and M2 assuming the booster parameters for emittance, ε=3.47 nm.rad, energy spread, σε=0.087%, and emittance coupling, κ=1%.

![BTS BEAM SIZE VERT](/img/machine/injection_system/bts_beam_size_V.png)

**Figure 34**: Vertical beam size along the BTS transfer line for modes M1 and M2 assuming the booster parameters for emittance, ε=3.47 nm.rad, energy spread, σε=0.087%, and emittance coupling, κ=1%.

The aperture requirements and beam stay clear (BSC) for the BTS transport line are calculated considering a clearance for residual orbit distortion and trajectory variations due to pulse to pulse differences in beam energy and launching conditions (position and angle) as described in Table 37 

| Parameter | Value | Unit |
| --- | --- | --- |
| Max. orbit distortion along LTB (H and V) | ± 1 | mm |
| Booster pulse to pulse energy variation | 0.1 |  % |
| Booster pulse to pulse beam centroid position/angle variation (H and V) | 0.4 | nm.rad |
| BTS vacuum chamber inner aperture (full) at quadrupoles (H / V) | 23.4 / 23.4 | mm |
| BTS vacuum chamber inner aperture (full) at dipoles (H / V) | 23.4 / 23.4 | mm |

**Table 37**: Parameters for BTS transfer line aperture and BSC calculations. 

The calculated horizontal and vertical BSC for BTS transport line modes are shown in the figures below. 

![TS BSC HOR](/img/machine/injection_system/ts_bsch.png)

**Figure 35**: Horizontal beam stay clear (BSC) for BTS transfer line. The BSC can accommodate residual orbit distortion and trajectory variations due to pulse to pulse differences in beam launching conditions described in Table 37. The vacuum chamber inner half-aperture is represented by the solid black curve.

![TS BSC VERT](/img/machine/injection_system/ts_bscv.png)

**Figure 36**: Vertical beam stay clear (BSC) for BTS transfer line. The BSC can accommodate residual orbit distortion and trajectory variations due to pulse to pulse differences in beam launching conditions described in Table 37. The vacuum chamber inner half-aperture is represented by the solid black curve.

<br />

### BTS Orbit Correction

The BTS transport line orbit correction main parameters are shown in Table 38. The specification of error tolerances takes into consideration the maximum Booster corrector strength at 3 GeV, since the same correctors are used. The tolerances are shown in Tables 39, 40, 41 and the correction statistics in Tables 42, 43. The orbits before and after correction for all modes are shown in Table 36. The correction system uses the same beam position measurement station with integrated fluorescent screens and striplines. The Booster extraction septum is used as a horizontal corrector as well as the storage ring injection septa, that are used to adjust horizontal position and angle at the storage ring injection point. 

| Parameter | Value | Unit |
| --- | --- | --- |
| Number of beam position measurement stations | 5 |  |
| Number of horizontal correctors | 4 |  |
| Number of septa used as horizontal corrector | 2 |  |
| Number of vertical correctors | 6 |  |
| Maximum corrector strength | ±0.35 | mrad |

**Table 38**: Parameters for BTS transfer line orbit correction. 

<br />

#### Maximum absolute random errors for BTS transfer line orbit correction simulation

A Gaussian distribution with cutoff in ±1σ is assumed. 

| Error | Value | Unit |
| --- | --- | --- |
| X alignment | 0.16 | mm |
| Y alignment | 0.16 | mm |
| Roll angle | 0.5 | mrad |
| Relative field error | 0.1 |  %  |

**Table 39**: Magnets 

| Error | Value | Unit |
| --- | --- | --- |
| X alignment | 0.2 | mm |
| Y alignment | 0.2 | mm  |

**Table 40**: BPMs 

| Error | Value | Unit |
| --- | --- | --- |
| x | 0.2 | mm |
| θx | 0.1 | mrad |
| y | 0.2 | mm |
| θy | 0.1 | mrad |
| dp/p | 0.2 |  %  |

**Table 41**: Beam launching conditions 

<br />

#### Orbit correction statistics

Over 100 random seeds for BTS transfer line. were used.

| Element | Before | After |
| --- | --- | --- |
| Max. rms H orbit | 0.86 | 0.17 |
| Max. rms V orbit | 0.92 | 0.18 |
| Max. rms H orbit @ BPMs | 0.79 | 0.11 |
| Max. rms V orbit @ BPMs | 0.78 | 0.12 |
| Average H peak-to-peak | 1.4 | 0.4 |
| Average V peak-to-peak | 1.4 | 0.4  |

**Table 42**:  Orbit in mm 

| Element | Before | After |
| --- | --- | --- |
|  | rms | max |
| CH | 0.10 | 0.37 |
| CV | 0.10 | 0.29 |
| septa | 0.20 | 0.54 |

**Table 43**:  Corrector strength in mrad 

![TS ORBIT](/img/machine/injection_system/ts_orbit.svg)

**Figure 37**: Orbit along the BTS transfer line for modes M1 and M2. For each mode, 100 random machines are simulated with errors given in Tables 39, 40, 41. The bold solid curves represent one sigma of the orbit distribution. 

<br />

### BTS Diagnostics Elements
![TS DIAGNOSTICS](/img/machine/injection_system/ts_diagnostics.png)

**Figure 38**: Schematic layout of BTS diagnostic elements.

<br />

## Injection into the Storage Ring 
The injection point in the storage ring is, by definition, the physical end of the thin septum. 

![SIRIUS RING INJECTION](/img/machine/injection_system/ring_inject.svg)

**Figure 39**: Layout of the storage ring injection straight section.

![RING TRANSVERSE CROSS SECTION](/img/machine/injection_system/ring_transverse_cross.svg)

**Figure 40**: Schematic representation of the transverse cross section at the storage ring injection point.

<br />

### Injection with Nonlinear Kicker (InjNLKckr)
![NONLINEAR INJECTION RING](/img/machine/injection_system/nonlin_kick_inject_ring.png)

**Figure 41**: Injection into the storage ring using a Nonlinear Kicker. The trajectory of the injected beam centroid in the horizontal plane is shown in solid red curve. The dashed curves represent ±3σx beam envelope.

![MAGNET PHASE](/img/machine/injection_system/magnet_phase.png)

**Figure 42**: Phase space at the Pulsed Multipole Magnet (PMM) position. The green curve represents the injected beam (±4σx) inside the storage ring acceptance (red curve) after the PMM non-linear kick. The black curve is plotted against the right axis and represents the magnetic field of the PMM.

<br />

### On-axis injection (InjDpKckr)
![ON AXIS INJECTION](/img/machine/injection_system/onaxis_inject_ring.png)

**Figure 43**: On-axis injection into the storage ring with a on-axis dipole kicker. The trajectory of the injected beam centroid in the horizontal plane is shown in solid red curve. The dashed curves represent ±3σx beam envelope.

<br />

## Pulsed Magnets Parameters 

### General layout
![BOOSTER INJECTION SECTION LAYOUT](/img/machine/injection_system/bo_inject_sec_layout.svg)

**Figure 44**: Booster injection section layout.

![BOOSTER EXTRACTION LAYOUT](/img/machine/injection_system/bo_extract_layout.svg)

**Figure 45**: Booster extraction layout.

![SIRIUS RING INJECTION](/img/machine/injection_system/ring_inject.svg)

**Figure 46**: Layout of the storage ring injection straight section.

<br />

### Septa

| Septum | Booster <br />Injection | Booster <br />Extraction Thin | Booster <br />Extraction Thick | Storage Ring <br />Injection Thick | Injection Thin | Unit |
| --- | --- | --- | --- | --- | --- | --- |
| Number | 1 | 1 | 1 | 2 | 1 |  |
| Arc length | 0.500 | 0.577 | 0.577 | 0.577 | 0.500 | m |
| Nominal deflection [Â°]| +21.75 | -3.60 | -3.60 | +3.60 | +3.12 | Â° |
| Nominal deflection [mrad]| +379.61 | -62.83 | -62.83 | +62.83 | +54.42 | mrad |
| Maximum deflection | 400.0 | 68.0 | 68.0 | 60.0 | 60.0 | mrad |
| Nominal magnetic field | 0.380 | -1.089 | -1.089 | 1.089 | 1.089 | T |
| Nominal beam trajectory radius | 1.317 | -9.188 | -9.188 | 9.188 | 9.188 | m |
| Magnet shape radius | 1.350 | -12.500 | 12.500 | 12.500 | 12.500 | m |
| Sagitta | 23.7 | 4.5 | 4.5 | 4.5 | 3.4 | mm |
| Horizontal Beam Stay Clear (full) | ≥ 22 | ≥ 9 | ≥ 9 | ≥ 9 | ≥ 9 | mm |
| Vertical Beam Stay Clear (full) | ≥ 16 | ≥ 8 | ≥ 8 | ≥ 7 | ≥ 7 | mm |
| Septum thickness † | 3 | 3 | 3 | 2.5 | 2.5 | mm |
| Amplitude reproducibility (rms) | ≤ 0.07 | ≤ 0.006 | ≤ 0.006 | ≤ 0.017 | ≤ 0.017 |  % |
| Flat top (rms) | ≤ 0.07 | ≤ 0.006 | ≤ 0.006 | ≤ 0.017 | ≤ 0.017 |  % |
| Flat top width | 150 | 150 | 150 | 150 | 150 | ns |
| Minimum half-sine pulse duration to satisfy flat-top | ≥ 6.2 | ≥ 21 | ≥ 21 | ≥ 12.6 | ≥ 12.6 | μs |
| Integrated leak field | ≤ 50 | ≤ 200 | ≤ 200 | ≤ 3.7 | ≤ 3.7 | G.cm |

**Table 44**: Main parameters for Sirius septa. 

† See Booster extraction apertures and SI injection apertures

<br />

### Kickers

| Kicker | Booster <br />Injection | Booster <br />Extraction | Storage Ring <br /> DpKckr (On-axis) | Storage Ring <br /> NLKckr | Unit |
| --- | --- | --- | --- | --- | --- |
| Beam energy | 0.15 | 3.0 | 3.0 | 3.0 | GeV |
| Number | 1 | 1 | 1 | 1 |  |
| Length | 0.5 | 0.5 | 0.5 | 0.47 | m |
| Nominal deflection | 19.34 | 2.52 | 6.1 | 2.9 (@x=-8 mm) | mrad |
| Maximum deflection | 23.4 | 2.9 | 6.7 | 3.4 (@x=-6 mm) | mrad |
| Nominal integrated field | 0.010 | 0.025 | 0.061 | 0.029 (@x=-8 mm) | T.m |
| Maximum integrated field | 0.012 | 0.029 | 0.067 | 0.034 (@x=-6 mm) | T.m |
| Horizontal Beam Stay Clear (full) | ≥ 36 | ≥ 36 | ≥ 24 | ≥ 24 | mm |
| Vertical Beam Stay Clear (full) | ≥ 15 | ≥ 15 | ≥ 9 | ≥ 9 | mm |
| Amplitude reproducibility (rms) | ≤ 0.31 | ≤ 0.37 | ≤ 0.33 | ≤ 0.7 |  % |
| Flat top (peak-to-peak) | ≤ 0.62 | ≤ 0.74 | ≤ 0.66 | ≤ 1.4 |  % |
| Flat top width | 150 | 150 | 150 | 150 | ns |
| Rise time | - | ≤ 1.5 | - | - | μs |
| Fall time | ≤ 1.5 | - | ≤ 1.5 | ≤ 1.5 | μs |
| Minimum half-sine pulse duration to satisfy flat-top | ≥ 3.0 | ≥ 2.7 | ≥ 2.9 | ≥ 2.0 | μs |
| Tolerance for integrated dipole field at center ¹ | - | - | - | < 3.7 | G.cm |
| Tolerance for integrated quadrupole gradient at center ² | - | - | - | < 0.12 | T | 

**Table 45**: Main parameters for Sirius kickers. 

¹ For horizontal stored beam centroid oscillation < 10% of beam size. 

² For horizontal stored beam size oscillation < 10%. 

<br /> 

### Assumptions for aperture requirements and tolerance calculations 

#### Aperture requirements

| Septum | Unit | Booster Injection <br />Horizontal | Booster Injection <br />Vertical | Booster Extraction <br />Horizontal | Booster Extraction <br />Vertical | Storage Ring Injection <br />Horizontal | Storage Ring Injection <br />Vertical |
| --- | --- | --- | --- | --- | --- | --- | --- |
| beam size, ±3σ | mm | ±6.3 | ±4.0 | ±1.0 | ±1.0 | ±1.0 | ±0.5 |
| orbit distortion | mm | ±1.0 | ±1.0 | ±1.5 | ±1.0 | ±1.5 | ±1.0 |
| tolerance for vacuum chamber | mm | ±1.0 | ±1.0 | ±1.0 | ±1.0 | ±1.0 | ±1.0 |
| position/angle variation | mm | ±2.0 | ±2.0 | ±1.0 | ±1.0 | ±1.0 | ±1.0 |
| energy variation | mm | ±0.7 | - | - | - | - | - |
| **Total** | mm | ±11.0 | ±8.0 | ±4.5 | ±4.0 | ±4.5 | ±3.5 |
| **Total Full Size** | mm | 22 | 16.0 | 9.0 | 8.0 | 9.0 | 7.0 |

**Table 46**: Beam aperture requirement considerations for Sirius septa. 

<br />

#### Flat-top and pulse-to-pulse reproducibility
The requirements for the 3 GeV kickers and septa flat-top and pulse-to-pulse reproducibility were determined based on the NLK injection efficiency in the storage ring. The injected beam position and angle stability at the NLK are required to be within Δx < 150 μm and Δx' < 50 μrad. Random variations in the injected beam position and angle at the NLK are supposed to be caused by uncorrelated random variations in:

1) Booster extraction kickers

2) Booster extraction septa

3) Storage ring thick injection septum

4) Storage ring thin injection septum

5) Storage ring NLKckr

6) BTS transport line magnet vibrations and ripple

If we suppose these effects add in quadrature and have the same weight, the tolerance for each contribution becomes: 

$\Delta x < 60 \mu m {\;} {\;} {\;} and {\;} {\;} {\;} \Delta x' < 20 \mu rad$

1) Booster extraction kickers (bek): A variation in the bek kick (same kick in both kickers) affects the position and angle at the NLK according to: 

$\Delta x [mm] = 11.1 \Delta \theta _{bek} [mrad] and \Delta x' = 3.4 \Delta \theta _{bek} {\;} {\;}$ , thus 

$\Delta \theta _{bek} < 5.4 \mu rad  or  \Delta \theta _{bek} / \theta _{bek} < 0.3%$

2) Booster extraction septa (bes): A variation in the bes kick (same kick in both septa) affects the position and angle at the NLK according to: 

$\Delta x [mm] = 13.9 \Delta \theta _{bes} [mrad] {\;} {\;} {\;} and {\;} {\;} {\;} \Delta x' = 0.5 \Delta \theta _{bes} {\;} {\;}$ , thus

$\Delta \theta _{bes} < 4.3 \mu rad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{bes} / \theta _{bes} < 0.006\%$ 

3) Storage ring thick injection septum (stk): A variation in the stk kick affects the position and angle at the NLK according to: 

$\Delta x [mm] = 5.3 \Delta \theta _{stk} [mrad] {\;} {\;} {\;} and {\;} {\;} {\;} \Delta x' = \Delta \theta _{stk} {\;} {\;}$ , thus

${\;} {\;} \Delta \theta _{stk} < 11.4 \mu rad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{stk} / \theta _{stk} < 0.01\%$ 

4) Storage ring thin injection septum (stn): A variation in the stn kick affects the position and angle at the NLK according to: 

$\Delta x [mm] = 3.7 \Delta \theta _{stn} [mrad] {\;} {\;} {\;} and {\;} {\;} {\;} \Delta x' = \Delta \theta _{stn} {\;} {\;}$ , thus

${\;} {\;} \Delta \theta _{stn} < 16.2 \mu rad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{stn} / \theta _{stn} < 0.019\%$ 

<br />
5) Storage ring NLKckr (pmm): 

$\Delta \theta _{pmm} < 20 \mu rad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{pmm} / \theta _{pmm} < 0.7\%$

For the other pulsed magnets:

1) Storage ring on-axis injection kicker (sik): The tolerance is calculated by requiring that the injected beam oscillation amplitude be limited to $\Delta x _{max}$ < 0.5 mm along the storage ring horizontal plane. The trajectory of the electron beam after a residual kick at sik is: 

$\Delta x (s) = \Delta \theta _{sik} [\beta _{x , sik} \beta _{x , max}] ^{1/2} sin(\Delta \varphi)$

$\Delta x _{max}$ is limited if

${\Delta \theta _{sik} < \Delta x _{max} / [\beta _{x , sik} \beta _{x , max}] ^{1/2}}$

Using $\beta _{x , sik}=18.6$ m and $\beta _{x , max}=19.3$ m, we have 

$\Delta \theta _{sik} < 26.4 \Delta x _{max} [\mu rad] {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{sik} / \theta _{sik} < 0.33\%$

2) Booster on-axis injection kicker (bik): The tolerance can be calculated in a similar way, by requiring that the injected beam oscillation amplitude be limited to Δxmax < 1.5 mm along the booster horizontal plane. When specifying the booster aperture, an allowance of 4.5 mm was considered for beam oscillations after injection. For the booster $\beta _{x , bik}=17.9$ m and βx,max=23.2 m, so we have 

$\Delta \theta _{bik} < 0.074 mrad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{bik} / \theta _{bik} < 0.31\%$

3) Booster injection septum (bis): A variation in the bis kick affects the position and angle at the injection kicker (bik) according to: 

$\Delta x [mm] = 1.85 \Delta \theta _{bis} [mrad] {\;} {\;} {\;} and {\;} {\;} {\;} \Delta x' = 0.2 \Delta \theta _{bis} {\;} {\;} {\;},$

if we require Δx < 0.5 mm at the booster injection kicker, we have: 

$\Delta \theta _{bis} < 0.27 mrad {\;} {\;} {\;} or {\;} {\;} {\;} \Delta \theta _{bis} / \theta _{bis} < 0.07\%$

<br />

#### Leakage field

To calculate the allowed **storage ring injection septa** leakage field at the stored beam position in the storage ring, we have assumed that the oscillations caused by the perturbation be limited to 10% of the beam size. The beam trajectory after a kick is given by: 

${\Delta x (s) = \Delta \theta _0 [\beta _0 \beta (s)] ^{1/2} sin[\varphi (s) - \varphi _0] < 0.1 \sigma _x (s) = 0.1 [\epsilon _x \beta (s)] ^{1/2}}$

and as a worst-case estimate we take sin[φ(s)-φ0]=1, and the residual kick at the stored beam position should satisfy:

$\Delta \theta _0 < 0.1 [\epsilon _x /\beta _0] ^{1/2}$ <br /> for $\epsilon _x = 0.27 nm.rad {\;} {\;} {\;} and {\;} {\;} {\;} \beta _0 = 20 m$, we have $\Delta \theta _0 < 0.37 \mu rad, {\;} {\;} {\;} or {\;} {\;} {\;} \int B .dl < 3.7 G.cm{\;} {\;}$ at ${\;} {\;}E = 3 GeV.$

<br />
For the **booster extraction septum**, we set the allowed leakage field so that the orbit distortion amplitude is limited to 0.3 mm. 

$\Delta x (s) = \Delta \theta _0 [\beta _0 /\beta (s)] ^{1/2} sin[\varphi (s) - \varphi _0] < 1.5 mm {\;} {\;} {\;} ,$ then <br /> for $\beta _{x , max} = 23.2 m {\;} {\;} {\;} and {\;} {\;} {\;} \beta _0 = 9.2 m$, we have $\Delta \theta _0 < 20 \mu rad, {\;} {\;} {\;} or {\;} {\;} {\;} \int B .dl < 200 G.cm{\;} {\;}$ at ${\;} {\;}E = 3 GeV.$

<br />
For the **booster injection septum**, we set the allowed leakage field so that the orbit distortion amplitude is limited to 1.5 mm. 

$\Delta x (s) = \Delta \theta _0 [\beta _0 /\beta (s)] ^{1/2} sin[\varphi (s) - \varphi _0] < 1.5 mm {\;} {\;} {\;} ,$ then <br /> for $\beta _{x , max} = 23.2 m {\;} {\;} {\;} and {\;} {\;} {\;} \beta _0 = 9.2 m$, we have $\Delta \theta _0 < 0.1 mrad, {\;} {\;} {\;} or {\;} {\;} {\;} \int B .dl < 50 G.cm{\;} {\;}$ at ${\;} {\;}E = 150 MeV.$

<br />

#### Half-sine pulse duration

If we define the pulse amplitude by 

$A = A_0 cos(\pi t/T)$

then the half-sine pulse duration T required for a flat-top dA/A0 in the time range 2t0 << T is given by 

$T = \pi t_0 * (2 dA/A_0) ^{1/2}$

![SEPTUM PULSE DURATION](/img/machine/injection_system/septum_pulse_duration.svg)

**Figure 43**: Septum pulse.
