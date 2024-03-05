---
title: Storage Ring
description: 
published: 1
date: 2024-03-05T15:02:07.819Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:48.087Z
---

# Machine: Storage Ring

## Introduction
Sirius is a 3 GeV synchrotron light source that is being built by the Brazilian Synchrotron Light Laboratory (LNLS). The storage ring uses the multi-bend-achromat design approach (5BA in this case) to achieve a very low beam emittance of 0.25 nmÂ·rad. The 518 m circumference contains 20 straight sections of alternating 6.5 and 7.5 meters in length, to be used for insertion devices as well as injection and RF systems. The central dipole of the 5BA cell is a permanent magnet with transverse and longitudinal field gradients to reduce the emittance and provide a hard X-ray radiation source. The thin high field section at its center of approximately 3.2 T provides radiation with critical energy of 19 keV with a modest contribution to the total energy loss. The other low field dipoles (0.56 T), responsible for the main beam deflection, will be electromagnetic. Many challenges are associated with this kind of lattice, including both in beam dynamics and accelerator engineering, that require R&D on new techniques.

The Sirius 5BA lattice design comprises a 5-fold symmetric configuration with alternating high and low horizontal betatron functions that has been optimized in the presence of nonlinear and perturbation effects. Most of the subsystems components are presently either under production or prototyping phase and the Sirius site is already being prepared. The earthwork is concluded and the building construction has started at the end of 2014.

Links below point to drawings with family names of lattice elements for each accelerator section

* [AS - Accelerator System drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-AS.pdf) PDF file [(sectors split in PDF files)](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings)
* [SI - Storage Ring drawing]((https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-SI.pdf)) PDF file
* [TS - Booster to Storage Ring transport line drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-TS.pdf) PDF file
* [BO - Booster drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-BO.pdf) PDF file
* [TB - Linac to Booster transport line drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-TB.pdf) PDF file
* [LI - Linac drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-LI.pdf) PDF file

## General Layout
Sirius will be comprised of an injection system and a 3 GeV electron storage ring. The injection system is composed of a 150 MeV linear accelerator (LINAC) and a full energy booster ring, providing top-up electron filling to the main storage ring. The booster and the storage ring will be concentric and will share the same tunnel. 

![SIRIUS LAYOUT](/img/machine/storage_ring/sr_sirius_layout.jpg)

**Figure 1**: Layout of the Sirius accelerator complex. The experimental hall will be able to accommodate beamlines up to 100 m in length. The requirement for longer beamlines (up to 450 m) is also anticipated and the possibility of a future extension of the building is left open.


## Lattice and basic parameters 

### Design parameters
Several different types of magnetic lattices have been studied for Sirius over the past few years. The final choice is a 20-cell five-bend-achromat (5BA) with natural emittance of 0.25 nmÂ·rad at 3 GeV. The circumference is 518.4 m and there are 20 dispersion-free straight sections of alternating 7.5-m and 6.5-m in length for insertion devices and machine utilities (see Figure 2). Among the lattices studied, this lattice showed the best compromise in terms of low emittance and large number of insertion device straight sections for a given constraint in the ring circumference. In addition, the lattice optics, that showed signs of good nonlinear behavior since the beginning, was indeed optimized to a robust dynamic aperture and momentum acceptance, allowing for conventional off-axis injection and large beam lifetime of about 10 hours with realistic error tolerances and insertion device effects. The nonlinear optimization is a continuous process that is still ongoing but already shows excellent results.

The low emittance is mainly achieved with the MBA approach, with M equal to 5. Besides the total number, other dipole magnet parameters have also been optimized to reduce the emittance: transverse field gradient is added to increase the horizontal damping partition number as well as to match the optics, low bending field and achromatic condition in the straight sections are used to enhance the effect of insertion devices on emittance reduction, different dipole lengths in the cell are used to minimize the weight of the end dipoles, where the dispersion function is matched to the achromatic condition and not to minimum emittance condition, and a simple longitudinal field gradient is introduced in the center dipole. This longitudinal field gradient is created by sandwiching a thin high-field permanent magnet dipole of 3.2 Tesla in the center of the low field main deflection dipole of 0.56 Tesla. In addition to reducing the emittance, these thin dipoles will also produce hard x-rays of critical photon energy of 19.2 keV, and thus usable flux up to about 115 keV, in just a small horizontal angular fan, keeping the overall dipole radiation power at low level. The option for a relatively low dipole field also favors a smaller beam energy spread.

Figure 2 shows a schematic drawing of one Sirius 5BA achromatic cell with the central BC dipole composed of a high field (HF) slice sandwiched by two low field (LF) sectors. The total deflection per cell is 18°, composed by the deflections of 2.76 Â°, 4.10 Â°, 4.30 Â°, respectively by B1, B2 and BC. The 2 types of straight sections are shown to the left (7-m) and right (6-m). 

![SR LAYOUT1](/img/machine/storage_ring/sr_ring_layout1.png)

**Figure 2**: Layout of the Sirius modified 5BA periods. The superbend BC in the cell center has peak magnetic field of 3.2 Tesla. There are 2 types of straight sections, with quadrupole doublet for high-beta straight sections (A) and quadrupole triplet for low-beta straight sections (B and P). A superperiod is composed of one high-beta and 3 low beta sections: A-B-P-B. The B and P low-beta sections are identical as far as first order optics is concerned; they differ in second order optics, i.e., the sextupoles are different. The quadrupoles in the P sectors can be independently adjusted to restore a 5-fold symmetric optics.

The lattice has alternating high horizontal beta in 7.5 m long straight sections and low horizontal beta in 6.5 m long straight sections for insertion devices. A quadrupole doublet is used to match the arcs to the high horizontal beta sections and a quadrupole triplet is used in the low horizontal beta ones. The optics thus has symmetry 5, as shown in Figure 3. The vertical beta function in the straight sections is always low to minimize the impact of the insertion devices.

In the arc sections the dispersion function reaches a maximum of 8 cm. A pair of quadrupoles between the dipoles is used to focus the beam in the horizontal plane whereas in the vertical plane only the dipole field gradient and edge focusing are used. 

![LATTICE FUNCS](/img/machine/storage_ring/lattice_func.svg)

**Figure 3**: The lattice functions for one 5BA cell with 1/2 high beta straight to the left and 1/2 low beta straight to the right. One machine period consists of one high beta and three low beta straights.

 The main parameters of the Sirius storage ring are shown in the tables below. 

#### Beam

| Parameter | Value | Unit |
| --- | --- | --- |
| Energy (top up) | 3 | GeV |
| Gamma factor | 5871 |  |
| Current | 350 | mA |

#### Lattice

| Parameter | Value | Unit |
| --- | --- | --- |
| Version | V25.01 |  |
| Type | 5BA |  |
| Circumference | 518.3899 | m |
| Revolution period | 1.729 | Î¼s |
| Revolution frequency | 0.5783 | MHz |
| Long straight sections | 5 7.5 | m |
| Short straight sections | 15 6.5 | m |
| Beam plane height | 1400 | mm |

#### Optics

| Parameter | Value | Unit |
| --- | --- | --- |
| Mode | S05.01 |  |
| Linear momentum compaction | 1.645×10⁻⁴ |  |
| Transverse coupling | 1.0 |  % |

| Parameter | Horizontal | Vertical| Unit |
| --- | --- | --- | --- |
| Betatron tunes | 49.0962 | 14.1520 |  |
| Natural chromaticies | -118.9 | -81.2 |  |
| Beta @ center of SS-A | 17.2 | 3.6 | m |
| Beta @ center of SS-B | 1.5 | 1.4 | m |
| Beta @ center of BC | 0.3 | 5.4 | m |
| Beam size @ center of SS-A | 65.3 | 3.0 | Î¼m |
| Beam size @ center of SS-B | 19.3 | 1.9 | Î¼m |
| Beam size @ center of BC | 9.2 | 3.6 | Î¼m |
| Beam divergence @ center of SS-A | 3.8 | 0.8 | Î¼rad |
| Beam divergence @ center of SS-B | 12.9 | 1.3 | Î¼rad |
| Beam divergence @ center of BC | 27.1 | 0.7 | Î¼rad |

#### Equilibrium Parameters

| Parameter | Value | Unit |
| --- | --- | --- |
| Natural emittance | 0.250 | nmÂ·rad |
| Natural energy spread | 0.084 |  % |
| Natural bunch length | 2.5 (8.2) | mm (ps) |
| Energy loss per turn from dipoles | 471.0 | keV |
| Energy loss per turn from IDs | 400.0 | keV |
| Total Energy loss per turn | 871.0 | keV |
| Radiation power from dipoles | 235.5 | kW |
| Radiation power from IDS | 200.0 | kW |
| Total radiation power | 435.5 | kW |


| Parameter | Horizontal | Vertical | Longitudinal | Unit |
| --- | --- | --- | --- | --- |
| Damping partition number | 1.30 | 1.00 | 1.70 |  |
| Damping time (dipoles only) | 16.92 | 22.03 | 12.97 | ms |

#### RF Parameters (with IDs)

| Parameter | Value | Unit |
| --- | --- | --- |
| Frequency | 499.6638 | MHz |
| Harmonic number | 864 |  |
| Cavity peak voltage | 3.0 | MV |
| Synchronous phase | 163.1 | Â° |
| Synchrotron tune | 4.7×10⁻³ |  |
| Synchrotron frequency | 2.69 | kHz |
| Energy acceptance | 5.1 |  % |

#### Low Field Dipoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Magnetic field | 0.5642 | T |
| Bending radius | 17.738 | m |
| Critical energy | 3.38 | keV |


| Parameter | B1 | B2 | BC_LF | Unit |
| --- | --- | --- | --- | --- |
| Number of dipoles | 40 | 40 | 40 |  |
| Hard-edge length of dipoles | 0.8530 | 1.2630 | 0.4020 | m |
| Deflection angle | 2.76 | 4.10 | 1.58 | Â° |

#### High Field Dipoles

| Parameter | Value | Unit |
| --- | --- | --- |
| Magnetic peak field | 3.2 | T |
| Bending radius @ peak | 3.127 | m |
| Critical energy @ peak | 19.15 | keV |


| Parameter | BC_HF | Unit |
| --- | --- | --- |
| Number of dipoles | 20 |  |
| Deflection angle | 1.14 | Â° |

**Table 1**: Sirius SR main parameters. 

### Measured parameters
Linear optics measurements can be performed by manipulating the stored beam. The dispersion function can be measured at BPMs by changing the RF frequency and measuring the corresponding variation in the closed orbit. The beta functions at quadrupole can be obtained by changing a quadrupole strength individually and measuring the corresponding variation in the betatron tune. Another method of measuring the beta functions is exciting betatron oscillations with a pinger and reading the turn-by-turn (TbT) beam positions over many turns with BPMs. Applying Principal Component Analysis (PCA) in the TbT data, it is possible to obtain the beta functions at BPMs. The lattice model can be calibrated to fit the measured orbit response matrix, which may provide information regarding the linear optics in the actual storage ring. The method of model calibration with orbit response matrix is called LOCO (Linear Optics from Closed Orbits). With the results obtained by performing the aforementioned beam-based measurements, one can characterize the machine linear optics and basic parameters and compare with the design values.

Based on the measurements performed in Sirius storage ring during the machine studies, the status of Sirius lattice parameters in March 2021 is:

* Energy (based on excitation curve of B1B2 dipoles): 2.99 GeV
* Horizontal Emittance: nominal (0.25 nmÂ·rad)
* Betatron coupling (minimum tune separation): 1%
* Energy Spread: nominal (0.084 %)
* Horizontal and vertical beta functions at straight sections: nominal (check Table 1) within 2% of relative error (std).
* Horizontal dispersion function and its derivative at center of straight sections: nominal (zero) within 1mm and 0.3mrad of error (std), respectively.
* Vertical dispersion function and its derivative at center of at straight sections, check Table 2.

| | 01SA | 02SB | 03SP | 04SB | 05SA | 06SB | 07SP | 08SB | 09SA | 10SB | 11SP | 12SB | 13SA | 14SB | 15SP | 16SB | 17SA | 18SB | 19SP | 20SB |
| --- | --- | --- |--- | --- | --- |--- | --- | --- |--- | --- | --- |--- | --- | --- |--- | --- | --- |--- | --- | --- |
| [mm] | 0.8 | 0.7 | -1.1 | -0.2 | 1.6 | -0.0 | -2.0 | 0.1 | 3.3 | 0.1 | -0.7 | -0.3 | -0.1 | 0.3 | 0.1 | -0.4 | -0.1 | 0.7 | 0.9 | 0.0 |
| [mrad] | -0.2 | 0.3 | 0.1 | -0.4 | -0.3 | 0.6 | 0.1 | -1.7 | -0.2 | 0.4 | 0.2 | 0.2 | -0.1 | 0.0 | 0.3 | 0.1 | -0.1 | 0.1 | -0.5 | 0.0 |

**Table 2**: Vertical dispersion function and its derivative at center of straight sections 


## Beam stay clear 
The beam stay clear (BSC) is defined here as the free aperture required for the beam as measured from its central orbit. In linear approximation, the BSC is symmetric about this orbit.

We have considered two contributions for the BSC requirement:

1) To allow betatron oscillations for on-energy particles: 

$BSC_b (s)=\sqrt{\frac{\beta(s)}{\beta ^*}BSC_b^*}$

where $BSC_b$ and $\beta ^*$ are respectively the physical aperture and value of betatron function at the acceptance restricting point.

$BSC_e (s)=(\sqrt{\beta(s) \mathcal{H} ^* + \eta (s)}) \delta ^*$

2) To allow betatron oscillations for particles after Touschek scattering in which the energy deviation goes up to the energy acceptance: 

where $\mathcal{H} ^*$ is the maximum value of $\mathcal{H} (s) = \gamma \eta ² + 2 \alpha \eta \eta' + \beta \eta'²$, and $\delta ^*$ is the energy acceptance. 

For the vertical plane we have contributions from 1) only: 

$BSCV (s) = BSC_b^y (s)$

whereas for the horizontal plane we have contributions from 1) and 2): 

$BSCH (s) = max (BSC_b^x (s), BSC_e^x (s))$

![BEAM SC](/img/machine/storage_ring/beam_stay_clear.svg)

**Figure 4**: Beam-stay-clear for Sirius. The vertical acceptance is limited by a 2-m long in-vacuum undulator with 4.5 mm full gap installed at the center of the low beta straight section. The horizontal acceptance is limited by the vacuum chamber (12 mm inner radius) at the high beta section.


### Beam stay clear at ID straight sections
The values of the beta functions and beam-stay-clear presented in this table are considered to be the specification values for SIRIUS beam-stay-clear. For this reason, the beta function shown here may be different from other tables, which will be in accordance with the latest storage ring model. 

| Straight Type | $\beta_x$ [m] | BSCx [mm] | $\beta_y$ [m] | BSCy [mm] |
| --- | --- | --- | --- | --- |
| SA | 17.78 | ±11.54 | 3.57 | ±2.84 |
| SB | 1.36 | ±3.20 | 1.60 | ±1.90 |
| SP | 1.36 | ±3.20 | 1.60 | ±1.90 |

**Table 3**: Beam Stay Clear at the center of Sirius straight sections. 

From the table above is possible to calculate the Beam Stay Clear at a position away from the center of the straight section, remembering that: 

$BSC (s) = \sqrt{\frac{\beta(s)}{\beta _0}BSC_0}$ and $\beta (s) = \beta _0 + \frac{s²}{\beta _0}$

where $\beta _0$ is the value of the betatron function at the center of the straight. 

![BSC TYPES STRAIGHT SEC](/img/machine/storage_ring/types_straight_sec.svg)

**Figure 5**: Beam-stay-clear for Sirius at all three types of straight sections.


### Nonlinear beam stay clear from tracking

![NONLIN BSC](/img/machine/storage_ring/nonlinear_beam_sc.svg)

**Figure 6**: Beam-stay-clear calculated from tracking simulations including nonlinear elements for SI.V14.C03. Note the asymmetry introduced by the optimization method, in which the negative side of the dynamic aperture is maximized at the high $\beta_x$ straight sections to improve the injection process.

## Error tolerance specifications 
After optimization of the bare lattice, errors are introduced in the model to study their influence on the beam stability and quality. This is accomplished with the flexible [AcceleratorToolbox (AT)](http://10.39.50.85:3000/en/home/Groups/FAC/matlab_at) in MATLAB. Aftwerwards these imperfect machine models are exported as flat-lattice files and used in a home-developed tracking code based on AT/TracyIII for performance optimization. From these tracking simulations, which are presented in the subsequent sections, the following error tolerance specifications were determined to be acceptable: 

### Multipole errors
We have simulated higher-order systematic and random multipole errors in all dipoles, quadrupoles, sextupoles and corrector magnets. The systematic multipole components for these magnets are taken from approved 3D magnetic models. Normal and skew random errors were chosen such that, at x = 12 mm from the reference orbit, their total residual fields deviate 100 and 30 ppm from their nominal values, respectively. Table 4, Table 3, Table 7, Table 6 shows the sets of systematic and random multipole errors used in the tracking simulations. The effects of higher-order multipoles associated with insertion device modeling are introduced separately in the form of non-linear kick maps for each device. 

|  Multipole error | Q14 <br />Systematic<br /> Normal<br />| Q20 <br />Systematic<br /> Normal<br /> | Q30 <br />Systematic<br />Normal<br /> | <br />Random <br />Normal | <br />Random <br />Skew|
| --- | --- | --- | --- |--- |--- |
| B2/B1 (sextupole) | | | | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B3/B1 (octupole) | | | | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B4/B1 (decapole) | | | | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B5/B1 (12-pole) | -3.9×10⁻⁴ | -4.1×10⁻⁴ | -4.3×10⁻⁴ | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B9/B1 (20-pole) | +1.7×10⁻³ | +1.7×10⁻³ | +1.8×10⁻³ | |  |
| B13/B1 (20-pole) | -8.0×10⁻⁴ | -7.7×10⁻⁴ | -8.1×10⁻⁴ | |  |
| B17/B1 (20-pole) | +8.5×10⁻⁵ | +5.9×10⁻⁵ | +7.2×10⁻⁵ | | | 

**Table 4**: Storage ring quadrupole multipole errors. Contribution of multipolar components relative to main quadrupolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

|  Multipole error | Systematic <br />Normal| Random <br />Normal | Random <br />Skew|
| --- | --- | --- |--- |
| B2/B0 (sextupole) | 1.5×10⁻⁴ | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B3/B0 (octupole) | -7.2×10⁻⁵ | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B4/B0 (decapole) | -5.6×10⁻⁴ | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B5/B0 (12-pole) | 6.7×10⁻⁵ | 1.5×10⁻⁴ | 0.5×10⁻⁴ |
| B6/B0 (14-pole) | 3.8×10⁻⁴ | - | - 

**Table 5**: Storage ring dipole multipole errors. Contribution of multipolar components relative to main dipolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

| Systematic multipole error | CHS (normal) | CVS (skew) | QS (skew) |
| --- | --- | --- |--- |
| B3/B0 (decapole) | | | -5.8×10⁻¹ |
| B4/B0 (decapole) | +3.1×10⁻¹ | -2.9×10⁻¹ |  |
| B6/B0 (14-pole) | +3.3×10⁻² | -3.5×10⁻³ |  |
| B7/B0 (16-pole) | | | +2.7×10⁻² |
| B8/B0 (18-pole) | -4.8×10⁻² | +5.5×10⁻² |  |
| B9/B0 (20-pole) | | | +8.0×10⁻² |
| B10/B0 (22-pole) | +1.4×10⁻² | -1.1×10⁻² |  |
| B13/B0 (28-pole) | | | +2.4×10⁻³ |

**Table 6**: Storage ring horizontal, vertical and skew corrector magnets systematic multipole errors. Contribution of multipolar components relative to main field at x = 12 mm. 

|  Multipole error | Systematic <br />Normal| Random <br />Normal | Random <br />Skew|
| --- | --- | --- | --- |
| B3/B2 (octupole) | | 7.0×10⁻⁴ | 5.0×10⁻⁴ |
| B4/B2 (decapole) | -7.0×10⁻⁵ | 5.0×10⁻⁴ | 5.0×10⁻⁴ |
| B5/B2 (12-pole) | | 4.0×10⁻⁴ | 5.0×10⁻⁵ |
| B6/B2 (14-pole) | -1.4×10⁻⁴ | 2.0×10⁻⁴ | 5.0×10⁻⁵ |
| B8/B2 (18-pole) | -2.4×10⁻³ | |  |
| B14/B2 (30-pole) | +1.4×10⁻³ | | 

**Table 7**: Storage ring sextupole multipole errors. Contribution of multipolar components relative to main sextupolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

¹ These spec values have been updated in 2018-04-23 after rotating coil measurements. They have been validated by beam dynamics calculations.


### Alignment and excitation errors
Tracking calculations have shown that the misalignment errors of the magnets are the dominating source of dynamical aperture reduction. We performed a statistical study using simulated machines with random Gaussian misalignments of all their magnets. Standard deviations of 30, 40 and 50 μm were tested with acceptance cutoff at 1-σ. Table 8 shows the final specifications for misalignment, rotation and excitation lattice errors. The nominal tolerance for the misalignment error being considered is 40 μm. 

| | Dipole Unit Blocks | Quadrupoles | Sextupoles | Girders | BPMs |  |
 --- | --- | --- | --- | --- | --- | --- |
| Transverse position, x, y| 40 | 40 | 40 | 80 | 20 | Î¼m |
| Rotation around longitudinal axis | 0.30 | 0.30 | 0.30 | 0.30 | -- | mrad |
| Strength error (static or low frequency) | 0.05 | 0.05 | 0.05 | -- | -- |  % |
| Dipole Gradient error | 0.1 | -- | -- | -- | -- |  % |

**Table 8**: Maximum absolute value of random alignment and excitation errors. The errors are generated with a Gaussian distribution truncated at ±1σ. 


### High frequency errors
We analyzed the effect of high frequency (> 1 kHz) magnet vibration and power supply ripple errors on the beam stability. These high frequency perturbations cannot be compensated by the presently available fast feedback systems and thus, in this case, the amplitude of the perturbations must be limited at the source. To estimate the effects of these perturbations we resort to the definition of the orbit amplification factor. The expected rms value for the orbit distortion at any observation point due to a Gaussian distribution of quadrupole misalignments with standard deviation $\sigma _{quad}$ is given by

$$
{\sqrt{\langle \mathcal{u}² (s_0) \rangle} = A_{\mathcal{u}} \sigma_{quad} = \sqrt{\beta_{\mathcal{u}} (s_0)} {\space} \overline{A}_{\mathcal{u}} \sigma_{quad}}
$$

where represents either x or y and $A_{\mathcal{u}}$ is the corresponding orbit amplification factor. We can define an orbit amplification factor $\overline{A}_{\mathcal{u}}$ normalized to $\sqrt{\beta _{\mathcal{u}} (s_0)}$ at the observation point: 

$$
{\overline{A}_{\mathcal{u}} = \frac{A_{\mathcal{u}}}{\sqrt{\beta _{\mathcal{u}} (s_0)}} = \frac{1}{2 \sqrt{2} sin(\pi \nu _{\mathcal{u}})} (\sum_{i=1}^{all quads}(KL)_i ^2 \beta _{\mathcal{u}}(s_i))^{1/2}}
$$

The tolerance for these high frequency vibration amplitudes that cannot be compensated by the feedback system is related to the orbit stability goal (usually 10% of beam size) in the vertical plane by: 

$$
\Delta \mathcal{y} _{quad,vibration} < 0.1 \frac{\sqrt{\epsilon _y}}{\overline{A}_y}
$$

where $\epsilon _y = \epsilon _0 \kappa / (1 + \kappa)$ is the vertical emittance expressed as a function of the coupling factor $\kappa$ and the natural emittance $\epsilon _0$. Using the expressions above the tolerances for uncorrelated high frequency errors have been determined as shown in Table 9.

| | Dipoles | Quadrupoles | Sextupoles |  |
 --- | --- | --- | --- |--- |
| Power supply ripple | 20 | 20 | 20 | ppm |
| Vibration rms amplitude | 6 | 6 | 6 | nm |

**Table 8**: Standard deviation for ripple and vibration errors. 


## Closed-orbit correction and coupling control
The Sirius closed-orbit correction system will consist of a Slow Orbit Feedback (SOFB) and a Fast Orbit Feedback (FOFB) systems. The SOFB system will make use of all 160 BPMs, and of 120 horizontal and 160 vertical slow correctors located in sextupole magnets. Only a vertical corrector close to BC dipole will not be combined to a sextupole. On the other hand, the FOFB system uses 80 horizontal and 80 vertical air coils located upstream and downstream of each of the 18 ID straight sections and 20 superbend sources. A subset of BPMs, the ones on either side of the radiation sources, will be used for local compensation of fast perturbations. These fast corrector coils will be placed at special sections with 0.3 mm thick stainless steel vacuum chambers. Both feedback systems will run at the same time, the SOFB system compensating for long term perturbations using a global correction algorithm based on SVD; and the FOFB system compensating for short term perturbations based on a local correction scheme. Tests performed at other laboratories like Soleil show that it is possible to have both systems working simultaneously without dead bands and without having them fighting each other. The implementation has to be such that the FOFB system does not correct around the golden orbit, but around the SOFB residual closed orbit, which is updated before each step of the SOFB; and the SOFB feedback corrects both for the orbit distortion read on BPMs and the orbit reconstructed by unloading the DC part of the fast correctors avoiding their saturation.

For coupling correction and control, independently powered skew quadrupole correctors are provided. They consist of additional coil windings in the sextupole families SF1J and SF1K (dispersive skews),and SDA and SDB (non-dispersive skews). The dispersive skew quadrupoles SF1 will be used to minimize the vertical dispersion created by alignments errors, and the non-dispersive ones will be used to correct coupling by minimizing the off-diagonal elements in the orbit response-matrix. This results typically in 0.02% residual emittance coupling in simulations. After this correction, the vertical beam size can be increased by controlling the overall coupling using the non-dispersive skews. For beam size and lifetime calculation purposes we consider setting the emittance coupling to 1%. 

Figure 7 shows the distribution of correctors and BPMs in one superperiod of the storage ring for the closed-orbit and coupling correction systems, and Tables 9 and 10 shows some parameters for the elements used in these systems. The tolerances for alignment and excitation errors used in the simulations are shown in Table 8. 

![SR LAYOUT2](/img/machine/storage_ring/sr_ring_layout2.png)

**Figure 7**: Distribution of corrector magnets and BPMs for the global and local closed-orbit correction system. Skew quadrupoles (QS) are implemented as additional coil windings in the sextupole families SFA0, SDB0, SDP0, SDx2(C1), SDx3(C3) while slow horizontal and vertical orbit correctors (CH and CV) are implemented in SDA0, SFB0, SFP0, SDx1, SFx2 and SDA0, SFB0, SFP0, SDx1, SDx3, SFx2(C3) families respectively. An additional skew corrector QS is implemented as an extra coil in the fast corrector next to BC, and a stand-alone vertical corrector CV is placed before dipole BC. Fast correctors (FCH and FCV) are located at special sections with 0.3 mm thick stainless steel vacuum chambers.

| Parameter | Value | Unit |
| --- | --- | --- |
| Number of BPMs | 160 |  |
| Number of skew quadrupoles | 80 (+ 10 QS in fast corrector)* |  |
| Skew quadrupole maximum integrated strength | 0.100 | T  |


| Parameter | Horizontal v. | Vertical v. | Unit |
| --- | --- | --- | --- |
| Number of slow dipole correctors | 120 | 160** |  |
| Maximum slow dipole corrector strength | 300 | 300 | Î¼rad |
| Number of fast dipole correctors | 80 | 80 |  |
| Maximum fast dipole corrector strength | 30 | 30 | Î¼rad |

**Tables 9 and 10**: Parameters of the closed orbit and coupling correction system. 

*80 skew quadrupoles are implemented as additional coils in sextupole magnets and 20 in fast correctors.

**140 vertical corrector are implemented as additional coils in sextupole magnets and 20 vertical correctors are separated magnets. 

The simulations show that the set of errors considered in Table 7, if uncorrected, result in large orbit distortions that cause many of the generated random machines to be unstable. To avoid these unstable machines, the orbit is initially corrected with the sextupoles turned off. Then, with a small residual orbit distortion, the sextupoles can be turned on again in steps without inducing instabilities. At each step, the orbit is further corrected iteratively until convergence.

Figure 8 shows the closed orbit for the simulated random machines without correction and with the sextupoles turned off. Figure 9 shows the residual orbit after global correction with respect to the ideal orbit, that is defined by the absolute zero of the reference system, including errors in the BPM offsets and considering that they are fixed to the girders; and Figure 10 shows the residual orbit with no BPM offset errors and no girder alignment errors. In this case the BPMs are centered around the ideal orbit. Tables 11 and 12 present the statistics of the orbit correction for 20 random machines.

![ORBIT BEFORE CORRECTION](/img/machine/storage_ring/uncorrected_hor_vert.svg)

**Figure 8**: Horizontal (blue) and vertical (red) uncorrected closed orbit for 20 random machines with sextupoles off. Bold curves represent one rms value.

![ORBIT AFTER CORRECTION](/img/machine/storage_ring/corrected_hor_vert.svg)

**Figure 9**: Horizontal (blue) and vertical (red) corrected closed orbit for 20 random machines with respect to the ideal orbit defined by the absolute zero of the reference system, including errors in the BPM offsets and considering that BPMs are fixed to the girders. Bold curves represent one rms value.

![BPM ORBIT CORRECTION](/img/machine/storage_ring/bpm_corr_hor_vert.svg)

**Figure 10**: Horizontal (blue) and vertical (red) corrected closed orbit for 20 random machines with no BPM offset errors and no girder alignment errors. In this case the BPMs are centered around the ideal closed orbit. Bold curves represent one rms value.

![FOFB CORRECTION](/img/machine/storage_ring/fofb.svg)

**Figure 11**: Fast orbit feedback. Correction with 80 BPMs, 80 FCH (fast horizontal) and 80 FCV (fast vertical corrector). The 80 BPMs are enclosing the 40 source points, 20 IDs and 20 BCs.


#### Orbit

| Parameter | before correction (mm)  | after correction (μm) <br /> wrt to ideal orbit <br /> | after correction (μm) <br /> wrt to BPMs <br />  |
| --- | --- | --- |--- |
| rms H orbit | 7.8 | 44 | - |
| rms V orbit | 7.7 | 59 | - |
| rms H orbit @ BPMs | 11 | 50 | 20 |
| rms V orbit @ BPMs | 5.7 | 49 | 22 

#### Correctors

| Parameter | H (μrad) | V (μrad) |
| --- | --- | --- |
| rms corrector strength | 52 | 78 |
| Max. corrector strength | 147 ± 26 | 264 ± 47 

**Tables 11 and 12**: Orbit correction statistics over 20 random seeds for the storage ring.


## Dynamic and momentum aperture 
For Sirius, the target dynamic aperture to assure a safe and high efficiency injection process is about 8 mm in the inner horizontal side of the ring at injection point. As for the momentum aperture, the goal is to reach a beam lifetime around 10 hours. 

### Bare lattice
The bare lattice is the lattice that contains only sextupoles as non-linear elements and that does not include misalignment or multipoles errors. Figure 12 and Figure 13 shows diffusion and frequency maps and Figure 14 shows the phase space for the best result obtained up to now. It should be mentioned that this is an ongoing optimization work. 

![DIFF MAP LONG](/img/machine/storage_ring/dif_map1.png)

**Figure 12**: Diffusion map (bottom) and corresponding frequency map (top) for Sirius at the center of the long straight section. Particles were tracked for 1032 turns [with AT](http://10.39.50.85:3000/en/home/Groups/FAC/matlab_at) for the bare lattice. On-momentum particles with transverse distribution x-z are shown.


![DIFF MAP 7MM](/img/machine/storage_ring/dif_map2.png)

**Figure 13**: Diffusion map (bottom) and corresponding frequency map (top) for Sirius at the center of the 7-m straight section. Particles were tracked for 1032 turns [with AT](http://10.39.50.85:3000/en/home/Groups/FAC/matlab_at) for the bare lattice. Coordinate-momentum distribution (x-dp) at initial vertical coordinate z=0.5 mm is shown.

![STORAGE RING PHASE](/img/machine/storage_ring/ring_phase.svg)

**Figure 14**: Sirius storage ring SI.V14.C03 phase space. Particles tracked for 500 turns, using AT. Blue/red dots refers to on-momentum horizontal/vertical scan of initial positions while keeping the vertical/horizontal initial position fixed at 0.1mm. Cyan dots refer to momentum scan up to $\pm$ 5% keeping transverse initial positions at 0.1mm.

### Multipole, excitation and alignment errors

![ONOFF MOMENTUM1](/img/machine/storage_ring/on_off_momentum1.png)

**Figure 15**: On-momentum (left) off-momentum (right) dynamic apertures at the center of the 7-m straight section for 20 machines with alignment and multipole errors, orbit, tune and coupling corrections. The color scale represents the percentage of machines in which a given point of the grid is stable. For these calculations, the following configuration was used: 6D tracking with [Trackcpp](/home/Groups/FAC/trackcpp); 5000 turns for on-momentum particles and 3500 turns for off-momentum apertures; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring.

![MOMENTUM APERTURE1](/img/machine/storage_ring/momentum_aperture1.svg)

**Figure 16**: Momentum aperture for one superperiod of the ring for 20 machines with alignment and multipole errors, orbit, tune and coupling corrections. For this calculation, the following configuration was used: 6D tracking with [Trackcpp](/home/Groups/FAC/trackcpp); 2000 turns; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring. Black lines represent the normalized loss rate for each machine, showing the dipoles as the main source of particle loss due to Touschek scattering.


### Optics symmetrization

Optics symmetrization consists in using individual quadrupoles to correct for the β-beating introduced by orbit errors in sextupoles and excitation errors in quadrupoles. 

![ONOFF MOMENTUM2](/img/machine/storage_ring/on_off_momentum2.png)

**Figure 17**: On-momentum (left) off-momentum (right) dynamic apertures at the center of the 7-m straight section for 20 machines with alignment and multipole errors, orbit, tune, coupling and optics corrections. The color scale represents the percentage of machines in which a given point of the grid is stable. For these calculations, the following configuration was used: 6D tracking with Trackcpp; 5000 turns for on-momentum particles and 3500 turns for off-momentum apertures; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring.

![MOMENTUM APERTURE2](/img/machine/storage_ring/momentum_aperture2.svg)

**Figure 18**: Momentum aperture for one superperiod of the ring for 20 machines with alignment and multipole errors, orbit, tune, coupling and optics corrections. For this calculation, the following configuration was used: 6D tracking with Trackcpp; 2000 turns; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring. Black lines represent the normalized loss rate for each machine, showing the dipoles as the main source of particle loss due to Touschek scattering.

![DAXY](/img/machine/storage_ring/daxy.svg)

**Figure 19**: On-momentum Dynamic Aperture increase due to symmetrization of the optic functions. Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

![DAEX](/img/machine/storage_ring/daex.svg)

**Figure 20**: Off-momentum dynamic Aperture increase due to symmetrization of the linear optics. Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

![MOMENTUM APERTURE3](/img/machine/storage_ring/momentum_aperture3.svg)

**Figure 21**: Momentum Aperture increase due to symmetrization of the linear optics. Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

### Impact of insertion devices

Insertion devices change the beam equilibrium properties through modifications of radiation integrals due to their alternating field (???). They also introduce focusing in the beam dynamics due to their intrinsic field roll-offs. This additional focusing is mitigated with appropriate tweaking of the lattice quadrupole magnets, specially the flanking ones. All quadrupole families are re-tuned in order to restore the optics symmetries, original tunes, and dispersion-free straights that the lattice had before the introduction of the IDs.


The list of IDs for Sirius is still being studied and developed. The devices planned to be used at this point are described in ???. ??? shows the impact of these devices on the equilibrium parameters of the beam.

Traditional elliptically polarizing undulators have strong horizontal field roll-offs when the light produced is vertically polarized. These roll-offs would have a prohibitive detrimental effect on the beam dynamics if the ID was allowed in without active compensations. Active compensation of these intrinsic roll-offs are being studied. Double helical superconductor undulators are also being studied and may provide an alternative to the traditional EPUs. 

#### plots below are out-of-date 

![daxy_effects_ids.svg](/img/machine/storage_ring/daxy_effects_ids.svg)

**Figure 22**: Effect of the IDs on the on-momentum dynamical aperture (red lines) as compared to the lattice without IDs (blue lines). Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

![daex_effects_ids](/img/machine/storage_ring/daex_effects_ids.svg)

**Figure 23**: Effect of the IDs on the off-momentum dynamical aperture (red lines) as compared to the lattice without IDs (blue lines). Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

![ma_effects_ids](/img/machine/storage_ring/ma_effects_ids.svg)

**Figure 24**: Momentum Aperture reduction due to IDs (red lines). Solid lines represent the average aperture of 20 machines with random multipole, alignment and excitation errors and dashed lines the average plus or minus one rms.

With additional optics symmetrization the dynamical and momentum apertures are as in Figure 25 and Figure 26 

![ONOFF MOMENTUM3](/img/machine/storage_ring/on_off_momentum3.png)

**Figure 25**: On-momentum (left) off-momentum (right) dynamic apertures at the center of the 7-m straight section for 20 machines with the IDS for phase2 and alignment and multipole errors, orbit, tune, coupling and optics corrections. The color scale represents the percentage of machines in which a given point of the grid is stable. For these calculations, the following configuration was used: 6D tracking with Trackcpp; 5000 turns for on-momentum particles and 3500 turns for off-momentum apertures; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring.

![MA SUPERPERIOD](/img/machine/storage_ring/ma_superperiod.svg)

**Figure 26**: Momentum aperture for one superperiod of the ring for 20 machines with the IDS for phase 2 plus alignment and multipole errors, orbit, tune, coupling and optics corrections. For this calculation, the following configuration was used: 6D tracking with Trackcpp; 2000 turns; The vacuum chamber physical aperture (12x12 mm²) and the IDS at minimum gap aperture (12x2.25 mm² at low beta straight sections and 12x4 mm² at high beta straight sections) are considered along the ring.

## Operation Phases

In this section the operation phases for Sirius from commissioning to maximum current and full insertion devices usage are described. The parameters for each phase, shown in Table 13, will be used in the following sections to estimate beam lifetime and instability thresholds and also to make an assessment of the operation conditions of the storage ring. In the commissioning phase (Phase 0) the energy loss is due only to dipoles and no insertion device is restricting the vertical acceptance of the machine. The RF voltage is provided by two super conducting cavities (SC) and the target stored current is 100 mA, distributed in a uniform-filling pattern. In the initial users mode (Phase 1), the first 12 beamlines described in the next section are included. The IDs for these beam lines include four in-vacuum undulators with 4.5 mm minimum gap (IVU19), two in-vacuum undulators with 8.0 mm minimum gap (IVU25) and four EPUs. All those insertion devices add about 145 keV to the energy loss/turn and cause a reduction in the natural emittance from 0.24 to 0.20 nm rad. The same RF cavities and stored current of the commissioning phase are assumed. The IDs for the final scenario (Phase 2) are not defined yet and it is therefore more difficult to estimate their impact on the beam parameters. It was then considered filling all low-beta sections with IVUs and the high-beta ones with EPUs, adding another 230 keV to the energy loss/turn. For the purpose of lifetime calculation and machine subsystems design, such as vacuum and RF, a maximum current of 500 mA is being considered. In this case, to have a reasonable lifetime, it is necessary a third-harmonic cavity (3HC) to flatten the potential in the RF bucket. This is essential both to increase the bunch length and the synchrotron tune spread. The former improves beam lifetime by reducing the charge density, and the latter increases beam stability by adding Landau damping. A factor of about five increase in bunch length can be achieved for a uniform bunch filling pattern. 

| Parameter | Phase 0 <br />(commissioning)| Phase 1 <br />(initial user mode)| Phase 2 <br />(final user mode)|
| --- | --- | --- | --- | --- |
| Maximum total current | 100 | 100 | 350 | mA |
| Current/bunch (uniform fill) | 0.116 | 0.116 | 0.405 | mA |
| Single bunch current | - | - | 2 | mA |
| RF Cavities | 1 NC (Petra 7-cell) | 2 SC | 2 SC + 3HC |  |
| Natural emittance* | 0.25 | 0.21 | 0.15 | nm rad |
| Coupling | 3 | 3 | 3 |  % |
| IDs | - | 6 IVUs, 2 EPUs | 12 IVUs, 8 EPUs |  |
| Natural energy spread* | 0.085 | 0.084 | 0.083 |  % |
| Natural bunch length* | 2.4 | 2.3 | 11.6 | mm |

*considering the zero current case only. 

**Table 13**: Sirius operation phases for beam lifetime and instability threshold calculations. 


## Intra-beam Scattering (IBS)

Given the scenarios presented in the previous section it is important to calculate the effect of intra-beam scattering (IBS) on the beam, since it can spoil the emittance and the storage ring performance. Another similar effect that cause beam blow-up is the microwave instability, which acts mostly in the longitudinal plane, causing an additional dilution of the density in the longitudinal phase space. Both effects can be harmful especially when operating in a hybrid fill mode, where a high current single-bunch is filled in the center of a small gap of empty buckets (about 5 to 10% of the total circumference), for time resolved experiments. To estimate the final parameters of the single bunch distribution, such as the emittance and energy spread, we iterated the calculation of IBS growth times using CIMP (Completely Integrated Modified Piwinski) and Bane formalisms. Some results are shown in Table 14. For the single bunch case in Phase 2, the IBS calculations are extended for single bunch currents up to 3 mA for Phase 2 are in Figure 27 to Figure 30. 

| Parameter | Phase 0 <br />(commissioning)| Phase 1 <br />(initial user mode)| Phase 2 <br />(final user mode)| Phase 2 <br />(high current)| Phase 2<br />(single bunch) |  |
| --- | --- | --- | --- | --- | --- | --- |
| Maximum total current | 100 | 100 | 350 | 500 | 2 | mA |
| Current/bunch (uniform fill) | 0.116 | 0.116 | 0.405 | 0.579 | - | mA |
| Horizontal emittance | 0.266 | 0.217 | 0.168 | 0.174 | 0.210 | nm rad |
| Vertical emittance | 7.76 | 6.32 | 4.89 | 5.07 | 6.14 | pm rad |
| Energy spread | 0.088 | 0.087 | 0.085 | 0.086 | 0.091 |  % |
| Bunch length | 2.5 | 2.4 | 12.0 | 12.1 | 12.8 | mm |

**Table 14**: IBS effects (CIMP formalism) on the bunch emittances in Sirius.

![ibs_effect1.png](/img/machine/storage_ring/ibs_effect1.png)

**Figure 27**: IBS effect (CIMP and Bane formalisms) on horizontal emittance as a function of current per bunch. Calculation for Phase 1 (no 3HC) and Phase 2 (with 3HC).

![ibs_effect2.png](/img/machine/storage_ring/ibs_effect2.png)

**Figure 28**: IBS effect (CIMP and Bane formalism) on vertical emittance as a function of current per bunch. Calculation for Phase 1 (no 3HC) and Phase 2 (with 3HC).

![ibs_effect3.png](/img/machine/storage_ring/ibs_effect3.png)

**Figure 29**: IBS effect (CIMP and Bane formalisms) on energy spread as a function of current per bunch. Calculation for Phase 1 (no 3HC) and Phase 2 (with 3HC).

![ibs_effect4.png](/img/machine/storage_ring/ibs_effect4.png)

**Figure 30**: IBS effect (CIMP and Bane formalisms) on bunch length as a function of current per bunch. Calculation for Phase 1 (no 3HC) and Phase 2 (with 3HC).

## Lifetime

The beam lifetime is also a key performance parameter for a light source. Various processes can lead to the loss of electrons from the beam; the most important ones are the collisions with residual gas molecules (gas scattering lifetime) and between two electrons with large momentum transfer (Touschek lifetime). Given the very low emittance of the machine, care has been taken to include IBS effects (using Bane model) in the calculations. For the elastic and inelastic lifetimes, a simulated pressure profile assuming accumulated charge of 10000Ah was used. Concerning Touschek lifetime, it is import to note that the natural emittance of Sirius is already in the regime where there is an exponential increase in Touschek lifetime towards lower emittances, as can be seen in Figure 32. From the plot it is clear that the inclusion of IDs in the machine, further reducing the emittance, is beneficial for the lifetime. In this regime the lifetime also shows a strong dependence on the energy acceptance. It is thus very important to optimize the lattice to have the largest possible energy acceptance. Table 15 shows results from lifetime calculations for uniform fill for different scenarios. For all cases the total lifetime is between 8 and 11 h. For Sirius there are users also interested in time-resolved experiments and thus an estimate for single bunch lifetime is needed. Calculations of lifetime for a single bunch were performed using parameters from Phase 1 and 2 and are included in Table 15 and show in Figure 31. 

| Parameter | Phase 0 <br />(commissioning)| Phase 1 <br />(initial user mode)| Phase 2 <br />(final user mode)| Phase 2 <br />(high current)| Phase 2 <br />(single bunch)|  |
| --- | --- | --- | --- | --- | --- | --- |
| Maximum total current | 100 | 100 | 350 | 500 | 2 | mA |
| Current/bunch (uniform fill) | 0.116 | 0.116 | 0.405 | 0.579 | - | mA |
| Touschek Lifetime | 18.05 | 15.87 | 20.63 | 14.82 | 4.98 | hours |
| Elastic Lifetime | 68.25 | 33.67 | 33.67 | 33.67 | 33.67 | hours |
| Inelastic Lifetime | 42.25 | 42.25 | 42.25 | 42.25 | 42.25 | hours |
| Total Lifetime | 10.67 | 8.59 | 9.82 | 8.27 | 3.92 | hours |

**Table 15**: Lifetime for Sirius. (IDs errors and symmetrization not taken into account) 

![TOTAL BEAM LIFE](/img/machine/storage_ring/total_beam_life.png)

**Figure 31**: Total beam lifetime for Phase 1 and Phase 2. On both cases the presence or not of a 3HC and the IBS effects are taken into account.

![VARIATION TOUSCHEK LIFETIME](/img/machine/storage_ring/var_touschek_life.png)

**Figure 32**: Variation of the Touschek lifetime component as a function of horizontal emittance (keeping all other factors, like vertical emittance and energy spread, constant) for Phase 1, Phase 2 with 350 mA (in final user mode) and 500 mA (high current case) scenarios. IBS effects are not considered in this calculation.


## Impedance budget and instabilities 

### Impedance budget

The beam-environment interaction can be described by the impedance concept, where each structure is modelled by a frequency dependent complex function. The Sirius impedance budget may be divided into two types: the resistive wall and the geometric impedances. The first kind was estimated using analytical formulas and the second with 2 and 3D numerical codes. See [Impedance Budget](/home/Machine/impedance_budget) for more details regarding the modelling of each component. Figure 35, Figure 33 and Figure 34 shows the impedance budget used so far for instability thresholds calculation for phase 2 and Table 16 shows the summary of its effect on the beam. 


| Element | $K_{loss}$  <br />[mV/pC] | P  <br />[mW] | Quantity | Total $K_{loss}$  <br />[mV/pC] | Total P  <br />[W] | $\beta _x K_x$  <br />[kV/pC] | $\beta _y K_y$  <br />[kV/pC] |
| --- | --- | --- | --- | --- | --- | --- | --- |
|IVUs @ low betax | 8.64 | 2120 | 8 | 69.1 | 16.9 | -44.6 | -89.3 |
| IVUs @ high betax | 4.98 | 1220 | 4 | 19.9 | 4.89 | -41.9 | -17.1 |
| EPUs | 4.37 | 1070 | 8 | 34.9 | 8.57 | -11.6 | -5.21 |
| Fast Correctors | 0.50 | 122 | 80 | 39.9 | 9.79 | -10.8 | -17 |
| Ferrite Kickers | -- | -- | 1 | 1.21 | 0.296 | -10.2 | -5.38 |
| PMM | -- | -- | 1 | 1.21 | 0.296 | -5.57 | -4.33 |
| Wall with NEG | -- | -- | 1 | 0429 | 105 | -33.2 | -50.7 |
| Broad Band | -- | -- | 1 | 2860 | 701 | -22.7 | -35.7 |
| Total | - | - | - | 3450 | 847 | -181 | -225 |

**Table 16**: Summary of the Effects of the impedance budget on the beam for phase 2. 

![HOR IMPEDANCE PHASE2](/img/machine/storage_ring/hor_imped_pha2.svg)

**Figure 33**: Horizontal Impedance for phase 2. Dashed lines represent negative data.

![VERT IMPEDANCE PHASE2](/img/machine/storage_ring/vert_imped_pha2.svg)

**Figure 34**: Vertical Impedance for phase 2. Dashed lines represent negative data.

![LONGIT IMPEDANCE PHASE2](/img/machine/storage_ring/longit_imped_pha2.svg)

**Figure 35**: Longitudinal Impedance for phase 2. Dashed lines represent negative data.

### Collective Instabilities
With the impedance budget presented above, collective instability thresholds for Sirius have been calculated for the various operation scenarios described in Operation Phases, for coupled bunch and single bunch effects.

Regarding the coupled bunch (CB) instabilities, the transverse planes will be unstable, due to resistive wall instability (see Table 17) and the longitudinal plane will be stable, given that there is no narrow band impedances in our model. the instabilities in the tansverse plane could be controlled by increasing the chromaticity, because of the strong head-tail damping of the azimuthal mode zero (see Figure 36 and Figure 37). However, this behaviour depends strongly on the strength of the broadband impedance and for the sake of safety a transverse feedback system will be installed in the machine from the beginning. 

| Parameter | Commissioning <br />Horizontal |  Commissioning <br />Vertical |  Phase 1 <br />Horizontal |  Phase 1 <br />Vertical |  Phase 2 <br />Horizontal |  Phase 2 <br />Vertical |
| --- | --- | --- | --- | --- | --- | --- |
| Threshold @ ξx,y=0 [mA] | 15.6 | 22.6 | 9.5 | 18.5 | 23 | 18.5 |
| Growth Time [ms] | 3.5 | 3.8 | 1.22 | 2.77 | 0.68 | 0.65 |
| Most Unstable CB mode | 815 | 850 | 815 | 850 | 815 | 850 |
| Minimum Chromaticity to Damp | 1.22 | 1.56 | 1.3 | 1.1 | 0.82 | 0.72 |

**Table 17**: Parameters for the coupled bunch instabilities in Sirius. 

![HOR BUNCH INSTABILITIES](/img/machine/storage_ring/hor_coup_bunch.svg)

**Figure 36**: Horizontal Coupled Bunch Instabilities for phase 2.

![VERT BUNCH INSTABILITIES](/img/machine/storage_ring/vert_coup_bunch.svg)

**Figure 37**: Vertical Coupled Bunch Instabilities for phase 2.

Table 18 shows the current thresholds for single bunch instabilities. Even for Phase 1 which presents the lowest thresholds (see Figure 38, Figure 39 and Figure 40), the operation current is well below the thresholds calculated for all three planes. For Phase 2, because of the third harmonic cavity, the bunches will not be Gaussian anymore which breaks the assumptions made in the theoretical models we have used for instability calculations. However, the operational current per bunch for this phase is still well below the calculated thresholds, resulting in a large safety margin. 

#### Current threshold [mA] 

| Mode Coupling | Commissioning | Phase 1 | Phase 2 |
| --- | --- | --- | --- |
| Vertical | 1.4 | 1.1 | 1.9 |
| Horizontal | 2.2 | 1.7 | 2.9 |
| Longitudinal | 3.0 | 2.6 | >> 4 |

**Table 18**: Current Thresholds for Single Bunch Instabilities in Sirius. 

![HOR COUP INSTABILITY](/img/machine/storage_ring/hor_coup_mode.svg)

**Figure 38**: Horizontal Mode Coupling Instability at zero chromaticity for Phase 1. Calculated using 9 azimuthal and 13 radial modes.

![VERT COUP INSTABILITY](/img/machine/storage_ring/vert_coup_mode.svg)

**Figure 39**: Vertical Mode Coupling Instability at zero chromaticity for Phase 1. Calculated using 9 azimuthal and 13 radial modes.

![LONGIT COUP INSTABILITY](/img/machine/storage_ring/longit_coup_mode.svg)

**Figure 40**: Longitudinal Mode Coupling Instability for Phase 1. Calculated using 33 azimuthal and 51 radial modes.

A hybrid filling pattern with an empty gap and a high current single bunch for time resolved experiments is planned for Sirius. In this mode, the bunch lengthening provided by the harmonic cavity can be smaller and non-uniform. For the single bunch in the middle of the gap, even with optimum lengthening, the threshold current for mode coupling (see Table 18, Phase 2) is already below the nominal value of 2 mA. A tracking code that includes the effects of the harmonic cavity with uniform and non-uniform filling as well as broadband impedances is being developed to study the hybrid filling mode more carefully. 

## Diagnostic Beamlines 
Here is a summary of the main features and specifications of each diagnostic beam line for the Storage ring in the Sirius project. 

### General Idea
Since Sirius will be a project mainly devoted to the production of soft and hard x-rays and due to the strong focusing nature of its lattice, the apertures available for beam lines are small. Bearing this in mind and the development of diagnostics equipment in the later years the natural choice is to use x-ray to image the beam in the diagnostic beamlines, and not vis-UV or visible radiation. Another issue is that on the new low emittance machines, impedances can represent a limiting factor and introducing vacuum chamber tapers, steps or strange geometries has to be a well thought process not to impact on the instability limits. Using x-rays to image the beam doesn't change the vacuum chamber current project and thus don't imply changes in the impedances on the overall machine. Also, making the design of the beam lines compatible with the overall machine design won't limit the number of diagnostic beamlines that can be built, if in the future this need arrises. For quick longitudinal profile measurements and filling pattern determination a streak camera and a BPM or Fast Current Transformer (FCT) will be used, thus a visible beaming is needed, however this line doesn't need extreme resolution for the vertical profiles and can use the available aperture in the machine without further modification on the vacuum chamber projects. Here is a summary of all the measurements that should be possible with the diagnostic beamlines:

* Beam size and thus emittance in transverse plane (horizontal and vertical);
* Energy spread (and for that it is necessary to have 2 beam lines, one with zero and one with significant dispersion -> B1 and B2 beam lines);
* Bunch length and longitudinal profiles (using visible light + streak camera);
* Filling pattern (visible diagnostics);
* Transverse turn-by-turn mode (for injection studies, instabilities, etc.) by using a fast camera with enhanced sensitivity in any on of the beam lines measuring transverse sizes ([1], [2] and [3]).

### Available sources points
There will be three possible sources available for diagnostics, light from B1 and B2 and also BC. Given the actual lattice the beam sizes in each of those sources are: 

| Source | $\beta _x [m]$ | $\beta _y [m]$ | $\alpha _x [rad]$ | $\alpha _y [rad]$ | $\gamma _x [1/m]$ | $\gamma _y [1/m]$ | $\eta _x [mm]$ | $\eta ' _x [mrad]$ | $\sigma _{x,b} [\mu m]$ | $\sigma _x [\mu m]$ | $\sigma _y [\mu m]$ | $\sigma' _{x,b} [\mu rad]$ | $\sigma' _x [\mu rad]$ | $\sigma' _y [\mu rad]$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | 1.7 | 26.8 | 2.9 | -6.6 | 5.7 | 1.6 | 0.1 | 3.2 | 20.3 | 20.3 | 8.2 | 37.6 | 37.7 | 2.0 |
| B2 | 1.6 | 24.5 | 2.4 | -7.6 | 4.1 | 2.4 | 28.1 | -41.8 | 20.0 | 32.2 | 7.8 | 31.8 | 49.3 | 2.4 |

**Table 19**: Sources, optical functions and beam sizes (at the source point), considering 1% coupling ($\kappa$), $\epsilon _0 = 251$ pmrad and $\sigma _{\delta}$ = 0.09%.

where ${\alpha = -\frac{1}{2} \frac{d \beta}{ds'}, {\;} {\;} \gamma = \frac{1 + \alpha ²}{\beta}, {\;} {\;} \sigma _{\beta} = \sqrt{\epsilon \beta}, {\;} {\;} \sigma = \sqrt{\sigma _{\beta}  ²+ \eta² \sigma _{\delta '} ²}, {\;} {\;} \sigma ' _{beta} = \sqrt{\epsilon \gamma}, {\;} {\;} \sigma ' = \sqrt{\sigma '² _{\beta} + \eta '² \sigma ² _{\delta}}, {\;} {\;} \epsilon _x = \frac{\epsilon _0}{1 + \kappa} {\;} {\;} and {\;} {\;} \epsilon _y = \frac{\epsilon _0 \kappa}{1 + \kappa}}$

The beam line coming from dipole B2 requires some modification on the vacuum chamber design, so the allocation for this beam line should be done well in advance in the project. According to ray tracing it is possible to extract light from this dipole, as long as the vertical corrector that comes right after it is removed in order to give space for a new pumping station. Due to limitations in the vacuum tube mechanics it is not possible to extract light from the very beginning of B2 (like it will be for B1) and the beam line will take light from 19 up to 27 mrad inside the dipole, as show in Figure 41. For dipole B1 it is possible to extract radiation from 0 up to 6 mrad inside the element.

The available source points around the storage ring are (so far): the B1 and B2 dipoles after the injection section (sector 01) and the same dipoles in the RF section (sector 03). In the case of the BC anyone, that is not allocated for a beam line form the beginning, is a possible source. 

![EXTRACTION PATH](/img/machine/storage_ring/extract_path.jpg)

**Figure 41**: Figure show the extraction path from dipole B2. The yellow line is the extraction of light from the beginning of the dipole, which cannot be realised due to mechanical constraints in the vacuum chamber production. The available extration point is them moved 19 mrad into the dipole and is represented by the green line in the picture. According to preliminary ray-tracing, this beamline won't colide with any magnet.

### Techniques and limutations 
In this section we describe a few techniques that can be used to measure the beam sizes in the Storage ring in Sirius. 

#### Pinholes
This is the most classical way for measuring beam sizes. The beam line would be composed of: a cooled monochromator followed by a set of attenuators and filters, a pinhole with array with 10, 15, 20 and 25 µm pinholes (explanation to follow), a phosphor screen and a CCD camera with pixel size of the order of 4 µm (of-the-shelf component, to reduce costs). The total magnification would be around 5 for B1 and 4.5 for B2. The image formed on the camera is the convolution of the source profile and the point spread function (PSF) of the system, i.e., the beamline. Consequently, the convolved PSF determines the smallest image size measurable by the imaging system. To calculate the PSF of the system we will, in a first approximation, assume to be in the far-field region. This is true when the distance between the pinhole and the screen in which the light is observed is significantly greater than A²/λ, where λ is the wavelength and A is the pinhole diameter. In the regime in which Fraunhofer optics are valid, the PSF can be approximated by a Gaussian function and in this case the rms Gaussian size of the image of the electron beam Σ fulfills: 

$\Sigma ² = S ² + \Sigma _0 ² + \Sigma _1 ²$

where S is the rms size of the image of the photon beam at a distance d from the pinhole, Σ0² is the point spread function of the system and Σ1² accounts for effects of blurring caused by the phosphor screen and also the CCD camera resolution. For monochromatic radiation the pinhole contribution to the PSF can be further decomposed into two contributions: 

${\Sigma _0 ² = S²_{aperture} + S²_{diff}}$

$S_{aperture}$ is the geometrical projection of the pinhole opening. A point source of light illuminating a hole at a distance d, will project a spot of light on the scintillator screen. The size of this spot is A(D+d)/d, where A is the pinhole diameter and D is the distance from the pinhole to the screen. The camera geometric magnification is M=D/d, and the corresponding rms size of this contribution to the total measured beam size is: 

${S_{aperture} = \frac{A}{\sqrt{12}} \frac{D + d}{d}}$

where the factor √12 is due to the conversion of the width of the rectangular profile to an rms value. S accounts for the pinhole diffraction, which in the regime of Fraunhofer diffraction is described by a Bessel function of first order, for a circular pinhole. If the Bessel function of first order is approximated by a Gaussian function, the rms size of the diffraction contribution to the total beam size is: 

${S_{diff} = 0.42 \frac{\lambda D}{A}}$

Thus, pinholes with large apertures will lead to image blurring due to geometrical shadowing while pinholes with small apertures have strong diffraction effects. The total contribution from the pinholes to the PSF as a function of the photon energy for the different pinhole apertures is shown in Figure 42 as well as a plot of the optimum aperture as a function of photon energy in Figure 43. For Sirius we considered that the pinholes are 3.5 m away from the source and that the beam line has a magnification of 5 for a beam line in dipole B1. From the plots we can see that there is no gain in having pinholes smaller than 10 µm and having an array with 10, 15 and 20 µm pinholes would cover the optimum size for a broad range of wavelengths. In Figure 44 is the result from a SRW simulation for the pinholes in Sirius, notice that for most cases the Fraunhoffer approximation is still valid and the diffraction pattern can be fitted by a Gaussian. 

![CONTRIBUTION SPREAD FUNC](/img/machine/storage_ring/contrib_spread.png)

**Figure 42**: Contribution to the point spread function for the pinholes as a function of photon energy (calculated and simulated in SRW). The distance source-pinhole was kept fixed at 3.5 m and the beam line magnification is 5.

![var_psf.png](/img/machine/storage_ring/var_psf.png)

**Figure 43**: Variation of the PSF as a function os pinhole size. The distance source-pinhole was kept fixed at 3.5 m and the beamline magnification is 5.

![srw_sim.png](/img/machine/storage_ring/srw_sim.png)

**Figure 44**: SRW simulations for the pinholes in Sirius, up to 50 keV the diffraction can be nicely approximated by a gaussian. The distance source-pinhole was kept fixed at 5 m and the beamline magnification is 5.

The imaging system contribution to the PSF (Σ1) can be further decomposed into two contributions; S accounts for the blurring of the final image due to the thickness and grain size of the phosphor screen (≈ 6- 10 µm), and $S_{CCD}$ is the rms spatial resolution of the camera, which can be approximated by the pixel size divided by the magnification. The pixel size of a standard CCD camera is 4.65 µm thus $S_{CCD}$ ≈ 1 μm. Gathering those two contributions we have that Σ1 ≈ 6 μm (on average). Putting together all the contributions the total point spread function of the system as a function of pinhole size and photon energy is given in the Table 19. So form this table we can see that it is a viable technique for measuring horizontal beam sizes ≥ 20 µm, however for vertical beam sizes it is not optimum since the PSF is of the same size as the beam height for Sirius. 

#### PSF ($\mu m$)

| Pinhole Size | 20 keV | 30 keV | 40 keV | 50 keV |
| --- | --- | --- | --- | --- |
| 10 µm | 10.7 | 8.6 | 7.6 | 7.1 |
| 15 µm | 8.6 | 7.3 | 6.8 | 6.4 |
| 20 µm | 7.7 | 6.9 | 6.9 | 8.9 |

**Table 20**: Total PSF at the source point for the B1 case.


#### Toroidal Mirror
Given the results for the pinhole it is possible to notice that a accurate measurement of for the vertical beam size is not possible. In order to b able to measure vertical and horizontal beam size we are now studying the use of a toroidal X-ray mirror. The optics is much like the one used in the SAX beam line in the current machine, the UVX. A series of calculations using SHADOW are begin done to evaluate this possibility. 

### Bunch length and Filling pattern measurements
In order to measure the bunch length the idea is to move the streak camera from the old light source (UVX) to the new one. The streak camera is a Hammamatsu with dual sweep unit running at a frequency of 1/4th of the RF frequency. In the old machine the RF frequency is 476.066 MHZ and thus the sincroscran frequency is about 119 MHz. It will be necessary to ship the unit to Japan in order to have the frequency changed to accommodate the 500 MHz, which is the nominal RF frequency from Sirius. The principle of operation of the streak camera is explained in Figure 45 , bellow. 

![STREAK CAM OPERATION](/img/machine/storage_ring/streak_cam_schema.png)

**Figure 45**: Operation schematics for the streak camera.

The Sirius Storage ring will have 864 buckets that will be filled evenly or with a gap (in case problems with ion trapping show up). At the beginning of its operation no special filling patter is considered, however it is expected that with time and the increasing number of very specialized beam lines a number of requests may arise. One possibility is the use o a long train of uniform bunches followed by a gap with a high current single bunch in the middle, used specifically for time-resolved experiments. In this case a good control of the filling pattern throughout a shift in needed. The Filling pattern system involves not only timing and diagnostics but also, injection/extraction and control and from start the plan is to implements a system that can implement arbitrary fillings in the machine and keep it, via filling pattern feedback, for long runs.

Since the frequency of the whole acceleration chain is based on 500 MHZ (the Linac as an harmonic of it), in order to be able to measure distinguish between consecutive bunches (without the need of reconstructing the longitudinal time structure, for that the idea is to use streak camera) the monitor used have to have a bandwidth of at least 500 MHz. In Sirius the monitor planned to be used are: 

* LINAC: a wall current monitor (check the TDR);
* Transport Lines and Booster: A commercial of-the-shelf Bergoz Fast Current Transformer (FCT) directly mounted on the vacuum chamber with ceramic break and RF shielding. According to branch measurements in NSLS-II it can reach ~ 1 GHz bandwidth (with a rise and fall time of about 200 ps) which is enough to extract the bunch-by-bunch information.
* Storage ring: A dedicated BMP to measure filling pattern The expected bandwidth is expected to be on the range of 10 to 20 GHz and for 100 mA stored it is expected to create a signal of X dBm on a 50 Ohm load, which is strong enough to perform measurements.

In order to digitize and process the data from the filling pattern monitors it is necessary a minimum sampling rate of ~ 1 GS/s (for 500 MHZ signals). Since the bunch length in the booster and storage ring are about 40 ps and 10 ps (or ~40 with a 3rd Harmonic Cavity) respectively and given the bandwidth of the monitors in each machine, the actually measured signal will the broadened to ~ 1 ns in the case of the Booster and to ~ 100 ps for the Storage Ring. In order to be able to measure both signals a digitizer capable of 4GS/s for the booster should be enough (4 sample points for each bunch) but for the storage ring a much better one is needed for the storage ring, with at least 10 times the capability, i.e., 40 GS/s. In the case of the booster and transport lines those equipment are ready available (either scopes of High-Speed Digitizers) and for the storage reign special oscilloscopes are also available in the market, however they are high-end equipment. Either way, digitizer or oscilloscopes, both are able to communicate with EPCIS and an interface with the control system should not be an issue. 


## Injection into the Storage Ring 
The injection point in the storage ring is, by definition, the physical end of the thin septum. 

![RING INJECTION](/img/machine/storage_ring/ring_inject.svg)

**Figure 46**: Layout of the storage ring injection straight section.

![TRASNVERSE SECTION](/img/machine/storage_ring/ring_transverse_cross.svg)

**Figure 47**: Schematic representation of the transverse cross section at the storage ring injection point.

### Injection with Nonlinear Kicker (InjNLKckr)

![NONLINEAR INJECTION RING](/img/machine/storage_ring/nonlin_kick_inject_ring.png)

**Figure 48**: Injection into the storage ring using a Nonlinear Kicker. The trajectory of the injected beam centroid in the horizontal plane is shown in solid red curve. The dashed curves represent ±3σx beam envelope.

![MAGNET PHASE](/img/machine/storage_ring/magnet_phase.png)

**Figure 49**: Phase space at the Pulsed Multipole Magnet (PMM) position. The green curve represents the injected beam (±4σx) inside the storage ring acceptance (red curve) after the PMM non-linear kick. The black curve is plotted against the right axis and represents the magnetic field of the PMM.


### On-axis injection (InjDpKckr)

![ON AXIS INJECTION](/img/machine/storage_ring/onaxis_inject_ring.png)

**Figure 50**: On-axis injection into the storage ring with a on-axis dipole kicker. The trajectory of the injected beam centroid in the horizontal plane is shown in solid red curve. The dashed curves represent ±3σx beam envelope.

## Straight sections allocation

|Sector |  | Long Straight (SA, SB, SP) | M2 | B2 | BC | C4 Straight |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | SA | TuneShkrH ScrapH ScrapV InjDpKckr InjNLKckr | | CARCARÁ (B1) | |  |
| 02 | SB | (Petra7) {3HCav} | | | |  |
| 03 | SP | {2 x SRFCav} | | | |  |
| 04 | SB | TIMBÓ | | | HIBISCO |  |
| 05 | SA | SIBIPIRUNA | | | |  |
| 06 | SB | CARNAÚBA (APU22) > {VPU29} | | | |  |
| 07 | SP | CATERETÊ (APU22) > {VPU29} | | IMBUIA | |  |
| 08 | SB | EMA (APU22) > {IVU18} | | | |  |
| 09 | SA | MANACÁ APU22 > {2 x APU22} | | | |  |
| 10 | SB | SABIÁ (EPU50_UVX) > {2 x DU52} | | | MOGNO |  |
| 11 | SP | IPÊ (APU58) > {APPLE-II} | | | |  |
| 12 | SB | -- | | | |  |
| 13 | SA | -- | | SAPÊ | QUATI | DCCT |
| 14 | SB | PAINEIRA (W180_UVX) > {IVU18} | | | JATOBÁ | DCCT |
| 15 | SP | -- | | | | GBPM |
| 16 | SB | -- BbBKckrL | BbBPkup | | | BbBKckrV |
| 17 | SA | SAPUCAIA (PAPU50) > {2 x APU22} BbBKckrH | | CEDRO | | TunePkupV |
| 18 | SB | -- TunePkupH | | | | TuneShkrV |
| 19 | SP | -- GSL15 | | | | PingV |
| 20 | SB | -- GSL07 | | | | 

**Table 21**: Allocation of Beamlines and Diagnostics Equipments in the Storage Ring

BbBKckrH  : H BbB (Bunch-by-Bunch) Kicker
BbBKckrV  : V BbB Kicker 
BbBKckrL  : L BbB Kicker 
BbBPkup   : BbB Pickup
TuneShkrH : H Tune Shaker
TuneShkrV : V Tune Shaker
TunePkupH : H Tune Pickup
TunePkupV : V Tune Pickup
GBPM      : Extra BPM
GSL07     : Generic Stripline (λ/8)
GSL15     : Generic Stripline (λ/4)
InjDpKckr : Dipole Kicker for on-axis injection
InjNLKckr : Nonlinear Kicker
SRFCav    : Superconducting RF Cavity
3HCav     : 3rd Harmonic Cavity
DCCT      : DC Current Transformer
PingH     : Horizontal Pinger
PingV     : Vertical Pinger
