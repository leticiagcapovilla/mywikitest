---
title: Magnets
description: 
published: 1
date: 2024-03-05T16:02:36.200Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:29.287Z
---

# Machine: Magnets

<br />

## Storage Ring Magnets

At this point all magnets have been designed, simulated and approved. A few prototype magnets (quadrupoles) have been measured mechanical and magnetically. Overall magnetic measurements with rotating coil and Hall probe systems are still pending.

<br />

### Storage Ring Dipoles

Dipoles in Sirius are of three distinct families: B1, B2 and BC. The first two, B1 and B2, are electromagnetic dipoles, whereas BC is a NdFeB permanent magnet dipole made of a thin 3.2 T slice sandwiched between two low field sector dipoles.

<br />

#### SI Dipole Magnet Specifications

##### Main Parameters

Main parameters for the electromagnetic dipoles B1 and B2 are shown in Table 1, and for the permanent magnet superbend BC in Table 2.

|Parameters| B1| B2| Units |
| --- | --- | --- | --- |
|Excitation| monopolar power supply| monopolar power supply| - |
|Number of magnets| 40| 40| - |
|Deflection angle| 2.7553| 4.0964| Â° |
|Magnetic length| 0.853| 1.263| m |
|Physical length| 0.807| 1.21239| m |
|Integrated quadrupole strength¹| -0.6461| -0.9588| m⁻¹ |
|Integrated sextupole strength¹| 0.0| 0.0| m⁻² |
|Full central gap²| 24.0| 24.0| mm |
|Hardedge bending radius| 17.7379| 17.6654| m |
|Hardedge quadrupole strength| -0.7574| -0.7591| m⁻² |
|Hardedge sextupole strength| 0.0| 0.0| m⁻³ |
|Hardedge sagitta| 5.127| 11.286| mm |
|Integrated field¹| -0.48| -0.72| TÂ·m |
|Integrated quadrupole gradient¹| 6.4652| 9.5946| T |
|Integrated sextupole gradient¹| 0.0| 0.0| TÂ·m⁻¹ |
|Hardedge field| -0.5642| -0.5665| T |
|Hardedge quadrupole gradient| 7.5794| 7.5967| TÂ·m⁻¹ |
|Hardedge sextupole gradient| 0.0| 0.0| TÂ·m⁻² |
|Quadrupole flexibility| 10.0| 10.0|  %  |

**Table 1**: Storage ring dipoles B1 and B2 main parameters. A parallel face, curved dipole is assumed (constant B and dB/dx along trajectory).

¹ On the Runge-Kutta trajectory.

² Full gap at the horizontal central position, where Runge-Kutta beam trajectory is centered.

| Parameters | BC | Unit |
| --- | --- | --- |
|Excitation| permanent NdFeB magnets| - |
|Number of magnets| 20| - |
|Magnet length| 0.828| m |
|Magnetic arc length| 0.920| m |
|Deflection angle| 4.2966| Â° |
|Peak field| 3.20| T |
|Full gap at peak field| 10.20| mm |
|Bending radius at peak field| 3.1272| m |
|Critical energy at peak field| 19.2| keV |
|Integrated field| -0.75042| TÂ·m |
|Integrated gradient| 6.2511| T  |

**Table 2**: Storage ring BC dipole main parameters.

<br />

##### Electric parameters

|Parameters |B1| B2| Unit |
| --- | --- | --- | --- |
|Main coil current| 394.10| 394.10| A |
|Main coil number of turns| 24| 24| - |
|Stored magnetic energy| 677.32| 1003.66| J |
|Magnet inductance| 8.72| 12.92| mH |

**Table 3**: Storage ring dipoles B1 and B2 electric parameters

<br />

##### Multipole Errors

| Multipole error| Systematic Normal| Random Normal | Random Skew |
| --- | --- | --- | --- |
|B2/B0 (sextupole)| 1.5×10⁻⁴| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B3/B0 (octupole)| -7.2×10⁻⁵| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B4/B0 (decapole)| -5.6×10⁻⁴| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B5/B0 (12-pole)| 6.7×10⁻⁵| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B6/B0 (14-pole)| 3.8×10⁻⁴| -| -  |

**Table 4**: Storage ring dipole multipole errors. Contribution of multipolar components relative to main dipolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

<br />

##### Alignment and Excitation Errors

|Parameters |Dipole Unit Blocks| Girders| Unit |
| --- | --- | --- | --- |
|Transverse position, x, y| 40| 80| Î¼m |
|Rotation around longitudinal axis| 0.30| 0.30| mrad |
|Strength error (static or low frequency)| 0.05| --|  % |
|Dipole Gradient error| 0.1| --|  %  |

**Table 5**: Maximum absolute value of random alignment and excitation errors for Storage Ring Dipoles. The errors are generated with a Gaussian distribution truncated at ±1σ.

<br />

####  SI Dipole Magnet 3D Models

##### BC

The BC dipoles in the Sirius storage ring is composed of a central high field slice with 1.1395 Â° of deflection and two flanking low field sectors with 1.57855 Â°. There is a control gap in the back of the dipole that can be used to adjust the magnetic field. Additionally, the low field poles can be moved transversely to adjust the integrated field and the pole between the low and high field sectors can be rotated about the longitudinal axis to correct the integrated quadrupole gradient.

![](/img/machine/magnets/SI_magnet_dipole_BC_drawing.png)

**Figure 1**: 3D drawing of the BC dipole model.

![](/img/machine/magnets/SI_magnet_dipole_BC_field.png)

**Figure 2**: Field of the BC dipole half model.

<br />

###### Fieldmap Analysis

Nominally BC dipoles should deflect the beam in 4.2966 Â°. A 3D model of BC has been [analyzed](/home/Groups/FAC/fieldmap_analysis) and approved. Fieldmap corresponding to one value for the control gap has been considered, namely 3.2 mm. A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-dipoles-bc/tree/master/links-official).

<br />

###### Segmented Model

In order to take into account the s-dependent field profile of the BC dipoles a symmetric model was created with 15 segments at each side of the magnet. Their segmentation points were chosen in a way to minimize the difference between integrals of the squared profile between for the model and the field on the Runge-Kutta trajectory.

![](/img/machine/magnets/segmented_model_BC_Anel.svg)

**Figure 3**: Field profile of segmented BC dipole model. Red curve corresponds to the field on Runge-Kutta trajectory.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0010| 0.018| -3.231| -0.001| -27.800 |
|02| 0.0040| 0.072| -3.153| -0.005| -24.800 |
|03| 0.0050| 0.080| -2.805| -0.021| -17.800 |
|04| 0.0050| 0.068| -2.371| -0.027| -11.000 |
|05| 0.0050| 0.058| -2.040| -0.027| -7.650 |
|06| 0.0100| 0.096| -1.672| -0.026| -5.620 |
|07| 0.0100| 0.074| -1.289| -0.026| -3.920 |
|08| 0.0100| 0.056| -0.980| -0.025| -2.380 |
|09| 0.0100| 0.044| -0.772| -0.021| -1.030 |
|10| 0.0320| 0.116| -0.631| -0.023| +0.903 |
|11| 0.0320| 0.097| -0.528| -0.148| +0.286 |
|12| 0.1600| 0.625| -0.682| -0.888| +0.341 |
|13| 0.1600| 0.628| -0.686| -0.903| +0.177 |
|14| 0.0120| 0.043| -0.622| -0.874| +0.068 |
|15| 0.0140| 0.033| -0.418| -0.434| -2.100 |
|16| 0.0160| 0.019| -0.212| -0.107| -2.050 |
|17| 0.0350| 0.020| -0.099| -0.019| -1.180  |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 6**: SI BC dipole segmented model.

<br />

##### B1

![](/img/machine/magnets/SI_magnet_dipole_B1_drawing.png)

**Figure 4**: 3D drawing of the B1 dipole model.

![](/img/machine/magnets/SI_magnet_dipole_B1_field.png)

**Figure 5**: Field of the B1 dipole half model.

<br />

###### Fieldmap Analysis

Nominally B1 dipoles should deflect the beam in 2.7553 Â°. So far a preliminary 3D model of B1 has been analyzed and approved. Field map corresponding to the nominal excited field has been considered. The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-dipoles-b1/tree/master/links-official/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [accessed this folder](https://github.com/lnls-ima/si-dipoles-b1/tree/master/links-official). 

<br />

###### Segmented Model

In order to take into account the s-dependent field profile of the B1 dipoles a symmetric model was created with 15 segments at each side of the magnet. Their segmentation points were chosen in a way to minimize the difference between integrals of the squared profile between for the model and the field on the Runge-Kutta trajectory. 

![](/img/machine/magnets/segmented_model_B1.svg)

**Figure 6**: Field profile of segmented B1 dipole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0020| 0.006| -0.562| -0.753| -0.297 |
|02| 0.0030| 0.010| -0.562| -0.756| -0.245 |
|03| 0.0050| 0.016| -0.564| -0.762| -0.117 |
|04| 0.0050| 0.016| -0.566| -0.770| -0.015 |
|05| 0.0050| 0.016| -0.567| -0.774| +0.004 |
|06| 0.0100| 0.033| -0.568| -0.775| -0.003 |
|07| 0.0400| 0.130| -0.567| -0.774| +0.019 |
|08| 0.1500| 0.483| -0.563| -0.773| +0.055 |
|09| 0.1000| 0.322| -0.563| -0.773| +0.076 |
|10| 0.0500| 0.162| -0.565| -0.774| +0.008 |
|11| 0.0340| 0.105| -0.540| -0.777| -0.159 |
|12| 0.0160| 0.033| -0.363| -0.428| -2.230 |
|13| 0.0400| 0.033| -0.143| -0.085| -1.960 |
|14| 0.0400| 0.008| -0.034| -0.009| -0.428 |
|15| 0.0500| 0.005| -0.016| -0.001| -0.102 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 7**: SI B1 dipole segmented model.

<br />

##### B2

![](/img/machine/magnets/SI_magnet_dipole_B2_drawing.png)

**Figure 7**: 3D drawing of the B2 dipole model.

![](/img/machine/magnets/SI_magnet_dipole_B2_field.png)

**Figure 8**: Field of the B2 dipole half model.

<br />

###### Fieldmap Analysis

Nominally B1 dipoles should deflect the beam in 4.0964 Â°. So far a preliminary 3D model of B2 has been analyzed and approved. Field map corresponding to the nominal excited field has been considered. The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-dipoles-b2/tree/master/links-official/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [accessed this folder](https://github.com/lnls-ima/si-dipoles-b2/tree/master/links-official).

<br />

###### Segmented Model

In order to take into account the s-dependent field profile of the B2 dipoles a symmetric model was created with 17 segments at each side of the magnet. Their segmentation points were chosen in a way to minimize the difference between integrals of the squared profile between for the model and the field on the Runge-Kutta trajectory.

![](/img/machine/magnets/segmented_model_B2.svg)

**Figure 9**: Field profile of segmented B2 dipole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1250| 0.405| -0.566| -0.774| +0.045 |
|02| 0.0550| 0.179| -0.569| -0.774| +0.028 |
|03| 0.0100| 0.033| -0.570| -0.774| +0.018 |
|04| 0.0050| 0.016| -0.568| -0.767| -0.019 |
|05| 0.0050| 0.016| -0.566| -0.759| -0.150 |
|06| 0.0050| 0.016| -0.565| -0.753| -0.268 |
|07| 0.0050| 0.016| -0.566| -0.756| -0.195 |
|08| 0.0100| 0.033| -0.568| -0.768| -0.011 |
|09| 0.0100| 0.033| -0.570| -0.774| +0.022 |
|10| 0.1750| 0.568| -0.567| -0.773| +0.081 |
|11| 0.1750| 0.567| -0.566| -0.773| +0.107 |
|12| 0.0200| 0.063| -0.553| -0.791| -0.030 |
|13| 0.0100| 0.028| -0.480| -0.682| -0.204 |
|14| 0.0150| 0.030| -0.345| -0.361| -2.440 |
|15| 0.0200| 0.022| -0.192| -0.108| -2.480 |
|16| 0.0300| 0.014| -0.084| -0.026| -1.220 |
|17| 0.0320| 0.005| -0.029| -0.005| -0.359 |
|18| 0.0325| 0.004| -0.022| -0.001| -0.149 |

* K=B'/(Bρ), S=B"/(2Bρ)

**Table 8**: SI B2 dipole segmented model.

<br />

#### SI Dipole Magnet Measurements

A summary of magnet field measurements of SI BC dipole. The Hall probe measurement files can be found at [this folder](https://github.com/lnls-ima/si-dipoles-bc/tree/master/model-13/measurement/magnetic/hallprobe).

<br />

##### BC

Analysis of BC hallprobe measurements. The analysis results can be found at [this folder](https://github.com/lnls-ima/si-dipoles-bc/tree/master/model-13/analysis/hallprobe/production) with subfolders x0-0p0079mm which contains results based on Runge-Kutta trajectory and x0-0p0079mm-reftraj holds the results based on reference trajectory. The initial x coordinate used was + 79um. The reference point is 7.703087 mm for reference trajectory.

<br />

###### Summary

* rx position of reference point:     +7.703087 mm
* initial rx position of trajectory:  +0.079092 mm

**Deflection Angle [deg]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| BC | +2.14829 | ± 0.00016 | 0.00060 |
| Diff | -0.00048 | ± 0.00743 | 0.02801 |

**KL [1/m]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| BC | -0.3127 | ± 0.0002 | 0.0008 |
| Diff | -0.0554 | ± 0.0595 |  0.2446  |

**SL [1/m²]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| BC | -0.35 | ± 0.074  | 0.24 |
| Diff | 21.05 | ± 16.75 | 54.60 |


The values used to calculate the difference to model were:

Deflection angle: 2.1483 deg

KL: - 0.31267 1/m

SL: -0.35037 1/m²

<br />

###### Deflection Angle

![](/img/machine/magnets/si-dipoles-bc-deflection-angle.svg)

**Figure 10**: Deflection angle calculated with reference trajectory, initial point at x = +79 um and the reference point is 7.703087mm.

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-dipoles-bc-integrated-quadrupole.svg)

**Figure 11**: Integrated quadrupole calculated with reference trajectory, initial point at x = +79 um and the reference point is 7.703087mm.

<br />

###### Integrated Sextupole

![](/img/machine/magnets/si-dipoles-bc-integrated-sextupole.svg)

**Figure 12**: Integrated sextupole calculated with reference trajectory, initial point at x = +79 um and the reference point is 7.703087mm.

<br />

##### B1

Analysis of B1 hallprobe measurements. The analysis results can be found at [this folder](https://github.com/lnls-ima/si-dipoles-b1/tree/master/model-09/analysis/hallprobe/production) with subfolders x0-8p527mm which contains results based on Runge-Kutta trajectory and x0-8p527mm-reftraj holds the results based on reference trajectory. The initial point of reference trajectory is 8.5270 mm and reference point is 13.6929 mm.

<br />

###### Summary

* rx position of reference point:     +13.692930 mm
* initial rx position of trajectory:  +8.527000 mm

**Deflection Angle [deg]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B1 | +1.37760 | ± 0.00029 | 0.00103 |
| Diff | -0.00354 | ± 0.02085 | 0.07471 |

**KL [1/m]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B1 | -0.3228 | ± 0.0002 | 0.0007 |
| Diff | +0.0393 | ± 0.0623 | 0.2133 |

**SL [1/m²]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B1 | -0.096 | ± 0.015 | 0.056 |
| Diff | +11.08 | ± 13.95 | 52.17 |

The values used to calculate the difference to model were: 

Deflection angle: 1.37765 deg

KL: -0.32289 1/m
SL: -0.10763 1/m²

<br />

###### Deflection Angle

![](/img/machine/magnets/si-dipoles-b1-deflection-angle.svg)

**Figure 13**: Deflection angle at current 403.6 A calculated with reference trajectory, initial point at x = 8.527 mm and reference point is 13.6929 mm.

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-dipoles-b1-integrated-quadrupole.svg)

**Figure 14**: Integrated gradient at current 403.6 A calculated with reference trajectory, initial point at x = 8.527 mm and reference point is 13.6929 mm.

<br />

###### Integrated Sextupole

![](/img/machine/magnets/si-dipoles-b1-integrated-sextupole.svg)

**Figure 15**: Integrated sextupole at current 403.6 A calculated with reference trajectory, initial point at x = 8.527 mm and reference point is 13.6929 mm.

<br />

##### B2

Analysis of B2 hallprobe measurements. The analysis results can be found at [this folder](https://github.com/lnls-ima/si-dipoles-b2/tree/master/model-08/analysis/hallprobe/production) with subfolders x0-8p153mm which contains results based on Runge-Kutta trajectory and x0-8p153mm-reftraj holds the results based on reference trajectory. The initial point of reference trajectory is 8.1530 mm and reference point is 19.4278 mm. 

<br />

###### Summary

* rx position of reference point:     +19.427847 mm
* initial rx position of trajectory:  +8.153000 mm

**Deflection Angle [deg]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B2 | +2.04820 | ± 0.00045 | 0.00146 |
| Diff | -0.00011 | ± 0.02175 | 0.07151 |

**KL [1/m]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B2 | -0.4794 | ± 0.0003 | 0.0011 |
| Diff | +0.0841 | ± 0.0596 | 0.2288 |

**SL [1/m²]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| B2 | -0.096 | ± 0.011 | 0.058 |
| Diff | +2.388 | ± 11.45 | 58.42 |

The values used to calculate the difference to model were: 

Deflection angle: 2.0482 deg

KL: -0.47982 1/m

SL: -0.09868 1/m²

<br />

###### Deflection Angle

![](/img/machine/magnets/si-dipoles-b2-deflection-angle.svg)

**Figure 16**: Deflection angle at current 401.8 A calculated with reference trajectory and initial point at x = 8.153 mm and reference point is 19.4278 mm.

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-dipoles-b2-integrated-quadrupole.svg)

**Figure 17**:  Integrated gradient at current 401.8 A calculated with reference trajectory and initial point at x = 8.153 mm and reference point is 19.4278 mm.

<br />

###### Integrated Sextupole

![](/img/machine/magnets/si-dipoles-b2-integrated-sextupole.svg)

**Figure 18**:  Integrated sextupole at current 401.8 A calculated with reference trajectory and initial point at x = 8.153 mm and reference point is 19.4278 mm.

<br />

#### SI Dipole Magnet Sorting

<!-- The order used was the result G286I010 of optimization run0. -->
<!-- Results can be found in data repository of si.v24.01 inside the folder dipoles_sorting. -->

<br />

##### B1 Installation Order

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-B1| B1-025 |
|SI-01C4:MA-B1| B1-040 |
|SI-02C1:MA-B1| B1-003 |
|SI-02C4:MA-B1| B1-031 |
|SI-03C1:MA-B1| B1-029 |
|SI-03C4:MA-B1| B1-038 |
|SI-04C1:MA-B1| B1-004 |
|SI-04C4:MA-B1| B1-005 |
|SI-05C1:MA-B1| B1-024 |
|SI-05C4:MA-B1| B1-016 |
|SI-06C1:MA-B1| B1-012 |
|SI-06C4:MA-B1| B1-030 |
|SI-07C1:MA-B1| B1-018 |
|SI-07C4:MA-B1| B1-011 |
|SI-08C1:MA-B1| B1-033 |
|SI-08C4:MA-B1| B1-013 |
|SI-09C1:MA-B1| B1-015 |
|SI-09C4:MA-B1| B1-042 |
|SI-10C1:MA-B1| B1-021 |
|SI-10C4:MA-B1| B1-019 |
|SI-11C1:MA-B1| B1-043 |
|SI-11C4:MA-B1| B1-009 |
|SI-12C1:MA-B1| B1-036 |
|SI-12C4:MA-B1| B1-034 |
|SI-13C1:MA-B1| B1-020 |
|SI-13C4:MA-B1| B1-010 |
|SI-14C1:MA-B1| B1-027 |
|SI-14C4:MA-B1| B1-002 |
|SI-15C1:MA-B1| B1-023 |
|SI-15C4:MA-B1| B1-014 |
|SI-16C1:MA-B1| B1-035 |
|SI-16C4:MA-B1| B1-032 |
|SI-17C1:MA-B1| B1-039 |
|SI-17C4:MA-B1| B1-017 |
|SI-18C1:MA-B1| B1-028 |
|SI-18C4:MA-B1| B1-037 |
|SI-19C1:MA-B1| B1-006 |
|SI-19C4:MA-B1| B1-046 |
|SI-20C1:MA-B1| B1-041 |
|SI-20C4:MA-B1| B1-026  |

**Not Used**
 
| Magnet Name| Magnet Serial ID |
| --- | --- |
|---| B1-022  |

**Table 9**: Storage Ring Dipoles B1 Installation. 

<br />

##### B2 Installation Order

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C2:MA-B2| B2-002 |
|SI-01C3:MA-B2| B2-001 |
|SI-02C2:MA-B2| B2-010 |
|SI-02C3:MA-B2| B2-011 |
|SI-03C2:MA-B2| B2-017 |
|SI-03C3:MA-B2| B2-014 |
|SI-04C2:MA-B2| B2-032 |
|SI-04C3:MA-B2| B2-043 |
|SI-05C2:MA-B2| B2-022 |
|SI-05C3:MA-B2| B2-045 |
|SI-06C2:MA-B2| B2-004 |
|SI-06C3:MA-B2| B2-015 |
|SI-07C2:MA-B2| B2-023 |
|SI-07C3:MA-B2| B2-037 |
|SI-08C2:MA-B2| B2-008 |
|SI-08C3:MA-B2| B2-013 |
|SI-09C2:MA-B2| B2-019 |
|SI-09C3:MA-B2| B2-030 |
|SI-10C2:MA-B2| B2-033 |
|SI-10C3:MA-B2| B2-007 |
|SI-11C2:MA-B2| B2-042 |
|SI-11C3:MA-B2| B2-016 |
|SI-12C2:MA-B2| B2-034 |
|SI-12C3:MA-B2| B2-018 |
|SI-13C2:MA-B2| B2-036 |
|SI-13C3:MA-B2| B2-038 |
|SI-14C2:MA-B2| B2-021 |
|SI-14C3:MA-B2| B2-005 |
|SI-15C2:MA-B2| B2-006 |
|SI-15C3:MA-B2| B2-029 |
|SI-16C2:MA-B2| B2-003 |
|SI-16C3:MA-B2| B2-027 |
|SI-17C2:MA-B2| B2-040 |
|SI-17C3:MA-B2| B2-044 |
|SI-18C2:MA-B2| B2-031 |
|SI-18C3:MA-B2| B2-028 |
|SI-19C2:MA-B2| B2-026 |
|SI-19C3:MA-B2| B2-025 |
|SI-20C2:MA-B2| B2-046 |
|SI-20C3:MA-B2| B2-009  |

**Not Used**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|---| B2-024  |

**Table 10**: Storage Ring Dipoles B2 Installation.

<br />

### Storage Ring Quadrupoles

There will be three types of quadrupole magnets in the Sirius lattice: Q14, Q20 and Q30, labeled as such according to their hard-edge lengths in simulations. Magnets from families QDA, QDB1, QDB2, QDP1 and QDP2 will be of type Q14; magnets from families QFA, Q1, Q2, Q3 and Q4  will be of type Q20; and magnets from families QFB and QFP will be of type Q30.

<br />

#### SI Quadrupole Magnet Specifications

##### Main Parameters

Table 11 lists main specifications for the quadrupoles.

|| Q14| Q20| Q30| units |
| --- | --- | --- | --- | --- |
|Number of magnets| 70| 170| 30|  |
|Magnetic length 1| 0.140| 0.200| 0.300| m |
|Maximum strength 1| 3.72| 4.54| 4.54| m⁻² |
|Bore diameter| 28| 28| 28| mm |
|Field flexibility for individual quadrupole 2| ± 10| ± 5| ± 5|  % |
|Maximum integrated strength 3| 0.5208| 0.908| 1.362| m⁻¹ |
|Maximum integrated field gradient 3| 5.21| 9.09| 13.63| T |
|Maximum field gradient 3| 37.23| 45.43| 45.43| TÂ·m⁻¹ |
|Maximum field at pole tip 3| 0.52| 0.64| 0.64| T  |

¹ Maximum values required for excitation with the main coils only.

² Obtained with trim coils.

³ Derived parameters from base specification parameters.

**Table 11**: Storage ring quadrupole magnets specification

<br />

##### Electric parameters

| | Q14| Q20| Q30| units |
| --- | --- | --- | --- | --- |
|Main coil current| 146.60| 154.66| 153.80| A |
|Main coil number of turns| 20.00| 23.25| 23.25|  |
|Maximum trim coil current| 10.00| 10.00| 10.00| A |
|Trim coil number of turns| 28.00| 18.00| 18.00|  |
|Stored magnetic energy| 72.45| 140.33| 211.01| J |
|Magnet inductance| 6.74| 11.73| 17.84| mH  |

**Table 12**: Storage ring quadrupole electric parameters 		

<br />

##### Multipole Errors

| Multipole error| Q14 <br />Systematic <br />Normal| Q20 <br />Systematic <br />Normal| Q30 <br />Systematic <br />Normal| Random Normal | Random Skew|
| --- | --- | --- | --- | --- | --- |
|B2/B1 (sextupole)| 	|	|	| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B3/B1 (octupole)| 	|	|	| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B4/B1 (decapole)| 	|	|	| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B5/B1 (12-pole)| -3.9×10⁻⁴| -4.1×10⁻⁴| -4.3×10⁻⁴| 1.5×10⁻⁴| 0.5×10⁻⁴ |
|B9/B1 (20-pole)| +1.7×10⁻³| +1.7×10⁻³| +1.8×10⁻³| 	 |
|B13/B1 (20-pole)| -8.0×10⁻⁴| -7.7×10⁻⁴| -8.1×10⁻⁴| 	 |
|B17/B1 (20-pole)| +8.5×10⁻⁵| +5.9×10⁻⁵| +7.2×10⁻⁵| 	 |		

**Table 13**: Storage ring quadrupole multipole errors. Contribution of multipolar components relative to main quadrupolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

<br />

##### Alignment and Excitation Errors

|| Quadrupoles|  |
| --- | --- | --- |
|Transverse position, ,| 40| Î¼m |
|Rotation around longitudinal axis| 0.30| mrad |
|Strength error (static or low frequency)| 0.05|  % |

**Table 14**: Maximum absolute value of random alignment and excitation errors for the Storage Ring Quadrupoles. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### SI Quadrupole Magnet 3D Models

All three types of quadrupoles models, namely Q14, Q20 and Q30 quadrupoles, have been designed, analyzed and approved.

![](/img/machine/magnets/SI_magnet_q14_drawing.png)

**Figure 19**: 3D drawing of the Q14 quadrupole model.

![](/img/machine/magnets/SI_magnet_q14_field.png)

**Figure 20**: Field of the Q14 quadrupole model.

![](/img/machine/magnets/SI_magnet_q20_drawing.png)

**Figure 21**: 3D drawing of the Q20 quadrupole model.

![](/img/machine/magnets/SI_magnet_q20_field.png)

**Figure 22**: Field of the Q20 quadrupole model.

![](/img/machine/magnets/SI_magnet_q30_drawing.png)

**Figure 23**: 3D drawing of the Q30 quadrupole model.

![](/img/machine/magnets/SI_magnet_q30_field.png)

**Figure 24**: Field of the Q30 quadrupole model.

<br />

##### Fieldmap Analysis

**Q14**

The 3D magnetic model of Q14 has been analyzed and approved, corresponding to maximum quadrupole strength, both family and trim coils excited. Analysis data for the latest model fieldmap can be [accessed here](https://github.com/lnls-ima/si-quadrupoles-q14/tree/master/links-official). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-quadrupoles-q14/tree/master/links-official). 

**Q20**

The 3D magnetic model of Q20 has been analyzed and approved, corresponding to maximum quadrupole strength, both family and trim coils excited. Analysis data for the latest model fieldmap can be [accessed here](https://github.com/lnls-ima/si-quadrupoles-q20/tree/master/links-official). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-quadrupoles-q20/tree/master/links-official). 

**Q30**

The 3D magnetic model of Q30 has been analyzed and approved, corresponding to maximum quadrupole strength, both family and trim coils excited. Analysis data for the latest model fieldmap can be [accessed here](https://github.com/lnls-ima/si-quadrupoles-q30/tree/master/links-official). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-quadrupoles-q30/tree/master/links-official). 

**Table 15**: brings the main fieldmap analysis results.

|| Q14| Q20| Q30| units |
| --- | --- | --- | --- | --- |
|Physical length 1| 0.1255| 0.1865| 0.2890| m |
|Magnetic length 2| 0.1401| 0.2001| 0.3003| m |
|Maximum main coil current| 160 / 3040| 150 / 3600| 150 / 3600| A / A.turns |
|Maximum trim coil current| 10 / 180| 10 / 180| 10 / 180| A / A.turns |
|Maximum integrated field gradient| 5.730| 9.611| 14.44| T |
|Relative multipole (n=5) 3| -2.7×10⁻⁴| -3.2×10⁻⁴| -4.4×10⁻⁴|  |
|Relative multipole (n=9) 3| +1.5×10⁻³| +1.7×10⁻³| +1.8×10⁻³|  |
|Relative multipole (n=13) 3| -6.3×10⁻⁴| -6.5×10⁻⁴| -6.7×10⁻⁴|  |	

¹ with end plates but without coils.

² integrated gradient divided by gradient at longitudinal center.

³ normal integrated multipoles divided by integrated quadrupole at x = 11.7 mm.

**Table 15**: Storage ring quadrupole magnet 3D-model parameters 

<br />

##### Segmented Model

Currently the hard-edge approximation is being used to model all quadrupoles for beam dynamics calculations purposes.

![](/img/machine/magnets/segmented_model_Q14.svg)

**Figure 25**: Quadrupole strength profile of Q14. Red curve corresponds to the strength on Runge-Kutta trajectory.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0700| 0.000| -0.000e+00| -4.090e+00| -0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 16**: SI quadrupole Q14 half segmented model (maximum strength).

![](/img/machine/magnets/segmented_model_Q20.svg)

**Figure 26**: Quadrupole strength profile of Q20. Red curve corresponds to the strength on Runge-Kutta trajectory.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1000| 0.000| -0.000e+00| -4.800e+00| -0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 17**: SI quadrupole Q20 half segmented model (maximum strength). 

![](/img/machine/magnets/segmented_model_Q30.svg)

**Figure 27**: Quadrupole strength profile of Q30. Red curve corresponds to the strength on Runge-Kutta trajectory.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1500| 0.000| -0.000e+00| -4.810e+00| -0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 18**: SI quadrupole Q30 half segmented model (maximum strength).

<br />

#### SI Quadrupole Magnet Measurements

A summary of magnet field measurements of SI quadrupoles.

<br />

##### Q14

###### Summary

**IntQuad [T]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | +5.2405 | ± 0.0024 | 0.0074 | 
| QDB1  | +5.2373 | ± 0.0030 | 0.0125 |
| QDB2  | +5.2338 | ± 0.0013 | 0.0044 |
| QDP1  | +5.2365 | ± 0.0021 | 0.0070 |
| QDP2  | +5.2365 | ± 0.0012 | 0.0042 |

**XCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | -0.1 | ± 5.4 | 20.3 | 
| QDB1  | +2.0 | ± 5.7 | 24.9 |
| QDB2  | +0.1 | ± 7.3 | 28.0 |
| QDP1  | +4.7 | ± 5.5 | 17.8 |
| QDP2  | -2.1 | ± 5.4 | 15.6 |

**YCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | +5.6 | ± 4.3 | 13.4 | 
| QDB1  | +3.5 | ± 5.2 | 24.6 |
| QDB2  | +3.4 | ± 4.2 | 15.6 |
| QDP1  | +3.6 | ± 3.2 | 11.4 |
| QDP2  | +4.5 | ± 5.3 | 17.9 |

**RollError [mrad]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | -0.4 | ± 0.1 | 0.2 | 
| QDB1  | -0.3 | ± 0.1 | 0.4 |
| QDB2  | -0.3 | ± 0.1 | 0.6 |
| QDP1  | -0.4 | ± 0.1 | 0.2 |
| QDP2  | -0.4 | ± 0.1 | 0.3 |

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-quadrupoles-q14-integrated-quadrupole.svg)

**Figure 28**: Integrated quadrupole strengths of Q14 magnets.

<br />

###### Horizontal Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q14-xcenter.svg)

**Figure 29**: Horizontal magnet center of Q14 magnets.

<br />

###### Vertical Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q14-ycenter.svg)

**Figure 30**: Vertical magnet center of Q14 magnets.

<br />

###### Roll-Angle Error

![](/img/machine/magnets/si-quadrupoles-q14-rollerror.svg)

**Figure 31**: Roll angle error of Q14 magnets.

<br />

##### Q20

###### Summary

**IntQuad [T]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFA   | -9.0805 | ± 0.0047 | 0.0173 | 
| Q1  | -9.0995 | ± 0.0071 | 0.0278 |
| Q2  | -9.0855 | ± 0.0042 | 0.0160 |
| Q3  | -9.0883 | ± 0.0057 | 0.0235 |
| Q4  | -9.0790 | ± 0.0059 | 0.0236 |

**XCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFA   | +8.4 | ± 3.0 | 10.2 | 
| Q1  | +5.7 | ± 6.6 | 30.4 |
| Q2  | +7.1 | ± 5.1 | 22.0 |
| Q3  | +6.5 | ± 5.9 | 25.5 |
| Q4  | +7.8 | ± 5.5 | 26.2 |

**YCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | +6.8 | ± 5.6 | 16.0 | 
| QDB1  | +3.8 | ± 5.0 | 22.4 |
| QDB2  | +4.0 | ± 5.5 | 28.5 |
| QDP1  | +4.0 | ± 6.6 | 31.4 |
| QDP2  | +3.5 | ± 4.4 | 20.8 |

**RollError [mrad]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QDA   | +0.0 | ± 0.1 | 0.4 | 
| QDB1  | +0.1 | ± 0.1 | 0.5 |
| QDB2  | +0.1 | ± 0.1 | 0.4 |
| QDP1  | +0.0 | ± 0.1 | 0.3 |
| QDP2  | +0.1 | ± 0.1 | 0.4 |

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-quadrupoles-q20-integrated-quadrupole.svg)

**Figure 32**: Integrated quadrupole strengths of Q20 magnets.

<br />

###### Horizontal Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q20-xcenter.svg)

**Figure 33**: Horizontal magnet center of Q20 magnets.

<br />

###### Vertical Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q20-ycenter.svg)

**Figure 34**: Vertical magnet center of Q20 magnets.

###### Roll-Angle Error

![](/img/machine/magnets/si-quadrupoles-q20-rollerror.svg)

**Figure 35**: Roll angle error of Q20 magnets.

##### Q30

###### Summary

**IntQuad [T]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFB | -13.6385 | ± 0.0050 | 0.0215 | 
| QFP | -13.6295 | ± 0.0038 | 0.0127 |

**XCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFB | +0.6 | ± 7.1 | 28.9 | 
| QFP | -4.2 | ± 5.1 | 18.8 |

**YCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFB | -1.8 | ± 4.5 | 18.0 | 
| QFP | -2.8 | ± 4.0 | 13.2 |

**RollError [mrad]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| QFB | -0.3 | ± 0.05 | 0.2 | 
| QFP | -0.2 | ± 0.1 | 0.3 |

<br />

###### Integrated Quadrupole

![](/img/machine/magnets/si-quadrupoles-q30-integrated-quadrupole.svg)

**Figure 36**: Integrated quadrupole strengths of Q30 magnets.

<br />

###### Horizontal Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q30-xcenter.svg)

**Figure 37**: Horizontal magnet center of Q30 magnets.

<br />

###### Vertical Magnetic Center

![](/img/machine/magnets/si-quadrupoles-q30-ycenter.svg)

**Figure 38**: Vertical magnet center of Q30 magnets.

<br />

###### Roll-Angle Error

![](/img/machine/magnets/si-quadrupoles-q30-rollerror.svg)

**Figure 39**: Roll angle error of Q30 magnets.

<br />

#### SI Quadrupole Magnet Sorting

##### Q14 Installation Order

**QDA**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01M2:MA-QDA| Q14-081 |
|SI-05M1:MA-QDA| Q14-077 |
|SI-05M2:MA-QDA| Q14-028 |
|SI-09M1:MA-QDA| Q14-059 |
|SI-09M2:MA-QDA| Q14-062 |
|SI-13M1:MA-QDA| Q14-058 |
|SI-13M2:MA-QDA| Q14-040 |
|SI-17M1:MA-QDA| Q14-034 |
|SI-17M2:MA-QDA| Q14-068 |
|SI-01M1:MA-QDA| Q14-018  |

**QDB1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02M1:MA-QDB1| Q14-010 |
|SI-02M2:MA-QDB1| Q14-017 |
|SI-04M1:MA-QDB1| Q14-011 |
|SI-04M2:MA-QDB1| Q14-008 |
|SI-06M1:MA-QDB1| Q14-023 |
|SI-06M2:MA-QDB1| Q14-035 |
|SI-08M1:MA-QDB1| Q14-048 |
|SI-08M2:MA-QDB1| Q14-075 |
|SI-10M1:MA-QDB1| Q14-021 |
|SI-10M2:MA-QDB1| Q14-055 |
|SI-12M1:MA-QDB1| Q14-014 |
|SI-12M2:MA-QDB1| Q14-033 |
|SI-14M1:MA-QDB1| Q14-026 |
|SI-14M2:MA-QDB1| Q14-067 |
|SI-16M1:MA-QDB1| Q14-057 |
|SI-16M2:MA-QDB1| Q14-027 |
|SI-18M1:MA-QDB1| Q14-079 |
|SI-18M2:MA-QDB1| Q14-009 |
|SI-20M1:MA-QDB1| Q14-025 |
|SI-20M2:MA-QDB1| Q14-053  |

**QDB2**

| Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02M1:MA-QDB2| Q14-039 |
|SI-02M2:MA-QDB2| Q14-050 |
|SI-04M1:MA-QDB2| Q14-038 |
|SI-04M2:MA-QDB2| Q14-020 |
|SI-06M1:MA-QDB2| Q14-045 |
|SI-06M2:MA-QDB2| Q14-047 |
|SI-08M1:MA-QDB2| Q14-064 |
|SI-08M2:MA-QDB2| Q14-046 |
|SI-10M1:MA-QDB2| Q14-032 |
|SI-10M2:MA-QDB2| Q14-030 |
|SI-12M1:MA-QDB2| Q14-065 |
|SI-12M2:MA-QDB2| Q14-056 |
|SI-14M1:MA-QDB2| Q14-049 |
|SI-14M2:MA-QDB2| Q14-054 |
|SI-16M1:MA-QDB2| Q14-063 |
|SI-16M2:MA-QDB2| Q14-004 |
|SI-18M1:MA-QDB2| Q14-015 |
|SI-18M2:MA-QDB2| Q14-066 |
|SI-20M1:MA-QDB2| Q14-060 |
|SI-20M2:MA-QDB2| Q14-052  |

**QDP1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-03M1:MA-QDP1| Q14-069 |
|SI-03M2:MA-QDP1| Q14-072 |
|SI-07M1:MA-QDP1| Q14-019 |
|SI-07M2:MA-QDP1| Q14-031 |
|SI-11M1:MA-QDP1| Q14-041 |
|SI-11M2:MA-QDP1| Q14-070 |
|SI-15M1:MA-QDP1| Q14-051 |
|SI-15M2:MA-QDP1| Q14-042 |
|SI-19M1:MA-QDP1| Q14-029 |
|SI-19M2:MA-QDP1| Q14-061  |

**QDP2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-03M1:MA-QDP2| Q14-012 |
|SI-03M2:MA-QDP2| Q14-005 |
|SI-07M1:MA-QDP2| Q14-078 |
|SI-07M2:MA-QDP2| Q14-071 |
|SI-11M1:MA-QDP2| Q14-007 |
|SI-11M2:MA-QDP2| Q14-006 |
|SI-15M1:MA-QDP2| Q14-073 |
|SI-15M2:MA-QDP2| Q14-016 |
|SI-19M1:MA-QDP2| Q14-037 |
|SI-19M2:MA-QDP2| Q14-002  |

**Not Used**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|---| Q14-044 |
|---| Q14-074 |
|---| Q14-043 |
|---| Q14-013 |
|---| Q14-024 |
|---| Q14-076 |
|---| Q14-080 |
|---| Q14-036  |

**Table 19**: Storage Ring Quadrupoles Q14 Installation. 

<br />

##### Q20 Installation Order

**QFA**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01M2:MA-QFA| Q20-076 |
|SI-05M1:MA-QFA| Q20-079 |
|SI-05M2:MA-QFA| Q20-176 |
|SI-09M1:MA-QFA| Q20-074 |
|SI-09M2:MA-QFA| Q20-101 |
|SI-13M1:MA-QFA| Q20-162 |
|SI-13M2:MA-QFA| Q20-155 |
|SI-17M1:MA-QFA| Q20-095 |
|SI-17M2:MA-QFA| Q20-071 |
|SI-01M1:MA-QFA| Q20-049  |

**Q1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-Q1| Q20-030 |
|SI-01C4:MA-Q1| Q20-132 |
|SI-02C1:MA-Q1| Q20-013 |
|SI-02C4:MA-Q1| Q20-014 |
|SI-03C1:MA-Q1| Q20-027 |
|SI-03C4:MA-Q1| Q20-008 |
|SI-04C1:MA-Q1| Q20-029 |
|SI-04C4:MA-Q1| Q20-023 |
|SI-05C1:MA-Q1| Q20-149 |
|SI-05C4:MA-Q1| Q20-028 |
|SI-06C1:MA-Q1| Q20-036 |
|SI-06C4:MA-Q1| Q20-033 |
|SI-07C1:MA-Q1| Q20-020 |
|SI-07C4:MA-Q1| Q20-015 |
|SI-08C1:MA-Q1| Q20-125 |
|SI-08C4:MA-Q1| Q20-153 |
|SI-09C1:MA-Q1| Q20-025 |
|SI-09C4:MA-Q1| Q20-067 |
|SI-10C1:MA-Q1| Q20-035 |
|SI-10C4:MA-Q1| Q20-141 |
|SI-11C1:MA-Q1| Q20-119 |
|SI-11C4:MA-Q1| Q20-012 |
|SI-12C1:MA-Q1| Q20-111 |
|SI-12C4:MA-Q1| Q20-006 |
|SI-13C1:MA-Q1| Q20-164 |
|SI-13C4:MA-Q1| Q20-024 |
|SI-14C1:MA-Q1| Q20-010 |
|SI-14C4:MA-Q1| Q20-032 |
|SI-15C1:MA-Q1| Q20-011 |
|SI-15C4:MA-Q1| Q20-005 |
|SI-16C1:MA-Q1| Q20-039 |
|SI-16C4:MA-Q1| Q20-109 |
|SI-17C1:MA-Q1| Q20-016 |
|SI-17C4:MA-Q1| Q20-009 |
|SI-18C1:MA-Q1| Q20-026 |
|SI-18C4:MA-Q1| Q20-037 |
|SI-19C1:MA-Q1| Q20-038 |
|SI-19C4:MA-Q1| Q20-017 |
|SI-20C1:MA-Q1| Q20-007 |
|SI-20C4:MA-Q1| Q20-021  | 

**Q2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-Q2| Q20-096 |
|SI-01C4:MA-Q2| Q20-034 |
|SI-02C1:MA-Q2| Q20-092 |
|SI-02C4:MA-Q2| Q20-122 |
|SI-03C1:MA-Q2| Q20-136 |
|SI-03C4:MA-Q2| Q20-174 |
|SI-04C1:MA-Q2| Q20-056 |
|SI-04C4:MA-Q2| Q20-059 |
|SI-05C1:MA-Q2| Q20-128 |
|SI-05C4:MA-Q2| Q20-115 |
|SI-06C1:MA-Q2| Q20-126 |
|SI-06C4:MA-Q2| Q20-158 |
|SI-07C1:MA-Q2| Q20-073 |
|SI-07C4:MA-Q2| Q20-087 |
|SI-08C1:MA-Q2| Q20-137 |
|SI-08C4:MA-Q2| Q20-082 |
|SI-09C1:MA-Q2| Q20-050 |
|SI-09C4:MA-Q2| Q20-117 |
|SI-10C1:MA-Q2| Q20-105 |
|SI-10C4:MA-Q2| Q20-124 |
|SI-11C1:MA-Q2| Q20-120 |
|SI-11C4:MA-Q2| Q20-118 |
|SI-12C1:MA-Q2| Q20-134 |
|SI-12C4:MA-Q2| Q20-135 |
|SI-13C1:MA-Q2| Q20-068 |
|SI-13C4:MA-Q2| Q20-098 |
|SI-14C1:MA-Q2| Q20-072 |
|SI-14C4:MA-Q2| Q20-175 |
|SI-15C1:MA-Q2| Q20-178 |
|SI-15C4:MA-Q2| Q20-104 |
|SI-16C1:MA-Q2| Q20-046 |
|SI-16C4:MA-Q2| Q20-154 |
|SI-17C1:MA-Q2| Q20-167 |
|SI-17C4:MA-Q2| Q20-094 |
|SI-18C1:MA-Q2| Q20-062 |
|SI-18C4:MA-Q2| Q20-102 |
|SI-19C1:MA-Q2| Q20-131 |
|SI-19C4:MA-Q2| Q20-138 |
|SI-20C1:MA-Q2| Q20-065 |
|SI-20C4:MA-Q2| Q20-152  |

**Q3**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C2:MA-Q3| Q20-066 |
|SI-01C3:MA-Q3| Q20-061 |
|SI-02C2:MA-Q3| Q20-091 |
|SI-02C3:MA-Q3| Q20-004 |
|SI-03C2:MA-Q3| Q20-147 |
|SI-03C3:MA-Q3| Q20-114 |
|SI-04C2:MA-Q3| Q20-112 |
|SI-04C3:MA-Q3| Q20-165 |
|SI-05C2:MA-Q3| Q20-107 |
|SI-05C3:MA-Q3| Q20-019 |
|SI-06C2:MA-Q3| Q20-179 |
|SI-06C3:MA-Q3| Q20-106 |
|SI-07C2:MA-Q3| Q20-148 |
|SI-07C3:MA-Q3| Q20-108 |
|SI-08C2:MA-Q3| Q20-070 |
|SI-08C3:MA-Q3| Q20-159 |
|SI-09C2:MA-Q3| Q20-121 |
|SI-09C3:MA-Q3| Q20-045 |
|SI-10C2:MA-Q3| Q20-042 |
|SI-10C3:MA-Q3| Q20-130 |
|SI-11C2:MA-Q3| Q20-161 |
|SI-11C3:MA-Q3| Q20-075 |
|SI-12C2:MA-Q3| Q20-127 |
|SI-12C3:MA-Q3| Q20-022 |
|SI-13C2:MA-Q3| Q20-145 |
|SI-13C3:MA-Q3| Q20-133 |
|SI-14C2:MA-Q3| Q20-172 |
|SI-14C3:MA-Q3| Q20-129 |
|SI-15C2:MA-Q3| Q20-018 |
|SI-15C3:MA-Q3| Q20-142 |
|SI-16C2:MA-Q3| Q20-139 |
|SI-16C3:MA-Q3| Q20-113 |
|SI-17C2:MA-Q3| Q20-140 |
|SI-17C3:MA-Q3| Q20-170 |
|SI-18C2:MA-Q3| Q20-110 |
|SI-18C3:MA-Q3| Q20-044 |
|SI-19C2:MA-Q3| Q20-086 |
|SI-19C3:MA-Q3| Q20-177 |
|SI-20C2:MA-Q3| Q20-031 |
|SI-20C3:MA-Q3| Q20-064  |

**Q4**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C2:MA-Q4| Q20-081 |
|SI-01C3:MA-Q4| Q20-097 |
|SI-02C2:MA-Q4| Q20-051 |
|SI-02C3:MA-Q4| Q20-168 |
|SI-03C2:MA-Q4| Q20-166 |
|SI-03C3:MA-Q4| Q20-043 |
|SI-04C2:MA-Q4| Q20-080 |
|SI-04C3:MA-Q4| Q20-047 |
|SI-05C2:MA-Q4| Q20-163 |
|SI-05C3:MA-Q4| Q20-048 |
|SI-06C2:MA-Q4| Q20-103 |
|SI-06C3:MA-Q4| Q20-116 |
|SI-07C2:MA-Q4| Q20-089 |
|SI-07C3:MA-Q4| Q20-077 |
|SI-08C2:MA-Q4| Q20-093 |
|SI-08C3:MA-Q4| Q20-063 |
|SI-09C2:MA-Q4| Q20-100 |
|SI-09C3:MA-Q4| Q20-054 |
|SI-10C2:MA-Q4| Q20-156 |
|SI-10C3:MA-Q4| Q20-169 |
|SI-11C2:MA-Q4| Q20-057 |
|SI-11C3:MA-Q4| Q20-058 |
|SI-12C2:MA-Q4| Q20-090 |
|SI-12C3:MA-Q4| Q20-150 |
|SI-13C2:MA-Q4| Q20-144 |
|SI-13C3:MA-Q4| Q20-085 |
|SI-14C2:MA-Q4| Q20-052 |
|SI-14C3:MA-Q4| Q20-069 |
|SI-15C2:MA-Q4| Q20-123 |
|SI-15C3:MA-Q4| Q20-084 |
|SI-16C2:MA-Q4| Q20-143 |
|SI-16C3:MA-Q4| Q20-171 |
|SI-17C2:MA-Q4| Q20-053 |
|SI-17C3:MA-Q4| Q20-157 |
|SI-18C2:MA-Q4| Q20-078 |
|SI-18C3:MA-Q4| Q20-146 |
|SI-19C2:MA-Q4| Q20-060 |
|SI-19C3:MA-Q4| Q20-160 |
|SI-20C2:MA-Q4| Q20-173 |
|SI-20C3:MA-Q4| Q20-083  |

**Not Used**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|---| Q20-041 |
|---| Q20-088 |
|---| Q20-040 |
|---| Q20-055 |
|---| Q20-099  |

**Table 20**: Storage Ring Quadrupoles Q20 Installation.

<br />

##### Q30 Installation Order

**QFB**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02M1:MA-QFB| Q30-016 |
|SI-02M2:MA-QFB| Q30-032 |
|SI-04M1:MA-QFB| Q30-010 |
|SI-04M2:MA-QFB| Q30-019 |
|SI-06M1:MA-QFB| Q30-008 |
|SI-06M2:MA-QFB| Q30-036 |
|SI-08M1:MA-QFB| Q30-011 |
|SI-08M2:MA-QFB| Q30-035 |
|SI-10M1:MA-QFB| Q30-009 |
|SI-10M2:MA-QFB| Q30-020 |
|SI-12M1:MA-QFB| Q30-029 |
|SI-12M2:MA-QFB| Q30-014 |
|SI-14M1:MA-QFB| Q30-013 |
|SI-14M2:MA-QFB| Q30-024 |
|SI-16M1:MA-QFB| Q30-005 |
|SI-16M2:MA-QFB| Q30-021 |
|SI-18M1:MA-QFB| Q30-025 |
|SI-18M2:MA-QFB| Q30-030 |
|SI-20M1:MA-QFB| Q30-023 |
|SI-20M2:MA-QFB| Q30-022  |

**QFP**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-03M1:MA-QFP| Q30-033 |
|SI-03M2:MA-QFP| Q30-027 |
|SI-07M1:MA-QFP| Q30-017 |
|SI-07M2:MA-QFP| Q30-006 |
|SI-11M1:MA-QFP| Q30-026 |
|SI-11M2:MA-QFP| Q30-034 |
|SI-15M1:MA-QFP| Q30-015 |
|SI-15M2:MA-QFP| Q30-031 |
|SI-19M1:MA-QFP| Q30-007 |
|SI-19M2:MA-QFP| Q30-004  | 

**Not Used**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|---| Q30-018 |
|---| Q30-012 |
|---| Q30-028  |

**Table 21**: Storage Ring Quadrupoles Q30 Installation. 

<br />

### Storage Ring Sextupoles, Slow Orbit Correctors and Skew Quadrupoles

Sextupole magnets in Sirius are designed to be multifunctional: apart from providing sextupolar field for chromaticity correction and dynamical aperture optimization, they also provide horizontal and vertical slow dipolar correctors for steering the beam orbit, as well as skew quadrupolar field to correct linear coupling introduced by lattice errors. These functions are implemented as additional excitations coils in the magnets. A sextupole magnet with excitation coils for vertical and/or horizontal dipolar fields does not have coils for skew quadrupolar fields, and vice-versa.

<br />

#### SI Sextupole Magnet Specifications

##### Main Parameters

Table 22 lists main specifications for the strength of the sextupole magnets.

| Parameter | Value | Unit |
| --- | --- | --- |
|Number of magnets| 280|  |
|Magnetic length| 0.15| m |
|Bore diameter| 28| mm |
|Maximum sextupolar strength| 240| m-3 |
|Maximum integrated sextupolar strength, ∫S.ds| 36| m-2 |
|Maximum integrated sextupolar field gradient, ∫B"/2.ds| 360.2| TÂ·m-1 |
|Maximum sextupole field gradient| 2402| TÂ·m-2 |
|Maximum sextupolar field at pole tip| 0.47| T  |

**Table 22**: Storage ring sextupole strength specifications. 

Table 23 lists main specifications for the orbit-corrector in the sextupole magnets.

|Coils| CH| CV|  |
| --- | --- | --- | --- |
|Number of correctors| 120| 160|  |
|Sextupole families with correctors| SDA0, SFB0, SFP0, SDx1, SFx2| SDA0, SFB0, SFP0, SDx1, SDx3, SFx2(C3)|  |
|Maximum kick angle| 390| 405| Î¼rad |
|Maximum integrated dipolar field| 0.00390| 0.00405| TÂ·m |
|Maximum dipolar field| 0.0260| 0.0270| T  |

**Table 23**: Storage ring orbit corrector specifications. 

Table 24 lists main specifications for the skew quadrupoles in the sextupole magnets.

|Coil| QS|  |
| --- | --- | --- |
|Number| 80 (+ 10 QS in fast corrector)|  |
|Sextupole families with skew quadrupoles| SFA0, SDB0, SDP0, SDx2(C1), SDx3(C3)|  |
|Maximum skew quadrupolar strength ¹| 0.0667| m⁻² |
|Maximum integrated skew quadrupolar strength| 0.0100| m⁻¹ |
|Maximum integrated skew quadrupolar gradient| 0.100| T |

**Table 24**: Storage ring skew quadrupole specifications. 

¹ Maximum value needed to correct linear coupling introduced by magnet alignment errors. Coupling introduced by IDs will be corrected using local skew quadrupoles. 

<br />

##### Electric parameters

|| S15| units |
| --- | --- | --- |
|Main coil current| 158.48| A |
|Main coil number of turns| 11.25|  |
|Maximum CH coil current| 10.00| A |
|CH coil number of turns| 14 / 28|  |
|Maximum CV coil current| 10.00| A |
|CV coil number of turns| 28|  |
|QS coil current ¹| 4.30| A |
|QS coil number of turns| 28|  |
|Stored magnetic energy| 61.57| J |
|Magnet inductance| 4.90| mH |

**Table 25**: Storage ring sextupole electric parameters 

¹ Value required to reach the specified skew quadrupolar strength. 

<br />

##### Multipole Errors

Multipole errors from sextupolar excitation

|Multipole error| Systematic <br />(normal)| Random <br />Normal| Random <br />Skew |
| --- | --- | --- | --- |
|B3/B2 (octupole)| |	7.0×10⁻⁴| 5.0×10⁻⁴ |
|B4/B2 (decapole)| -7.0×10⁻⁵| 5.0×10⁻⁴| 5.0×10⁻⁴ |
|B5/B2 (12-pole)| |	4.0×10⁻⁴| 5.0×10⁻⁵ |
|B6/B2 (14-pole)| -1.4×10⁻⁴| 2.0×10⁻⁴| 5.0×10⁻⁵ |
|B8/B2 (18-pole)| -2.4×10⁻³| 	 |
|B14/B2 (30-pole)| +1.4×10⁻³|  |	

**Table 26**: Storage ring sextupole multipole errors. Contribution of multipolar components relative to main sextupolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

Multipole errors from slow horizontal corrector excitation

|Multipole error| Systematic <br />(normal)| Random <br />Normal| Random <br />Skew |
| --- | --- | --- | --- |
|B4/B0 (decapole)| +3.1×10-1| | |
|B6/B0 (14-pole)| +3.3×10⁻²| | |
|B8/B0 (18-pole)| -4.8×10⁻²| | |
|B10/B0 (22-pole)| +1.4×10⁻²| | |		

**Table 27**: Storage ring horizontal corrector magnet multipole errors. Contribution of multipolar components relative to main dipolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

Multipole errors from slow vertical corrector excitation

|Multipole error| Systematic <br />(normal)| Random <br />Normal| Random <br />Skew |
| --- | --- | --- | --- |
|B4/B0 (decapole)| -2.9×10-1| | |
|B6/B0 (14-pole)| -3.5×10⁻³| | |
|B8/B0 (18-pole)| +5.5×10⁻²| | |
|B10/B0 (22-pole)| -1.1×10⁻²| | |		

**Table 28**: Storage ring vertical corrector magnet multipole errors. Contribution of multipolar components relative to main dipolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ.

Multipole errors from skew quadrupole excitation

|Multipole error| Systematic <br />(normal)| Random <br />Normal| Random <br />Skew |
| --- | --- | --- | --- |
|B3/B1 (octupole)| -5.8×10-1| | |
|B7/B1 (16-pole)| +2.7×10⁻³| | |
|B9/B1 (20-pole)| +8.0×10⁻³| | |
|B13/B1 (28-pole)| +2.4×10⁻³| | |	

**Table 29**: Storage ring skew quadrupoles multipole errors. Contribution of multipolar components relative to main quadrupolar field at x = 12 mm. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

<br />

##### Alignment and Excitation Errors

|| Sextupoles|  |
| --- | --- | --- |
|Transverse position, x, y| 40| Î¼m |
|Rotation around longitudinal axis| 0.30| mrad |
|Strength error (static or low frequency)| 0.05|  %  |

**Table 30**: Maximum absolute value of random alignment and excitation errors for the Storage Ring Sextupoles. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### SI Sextupole Magnet 3D Models

![](/img/machine/magnets/SI_magnet_sextupole_drawing.png)

**Figure 40**: 3D drawing of the sextupole (with dipolar field coils) quadrupole model.

![](/img/machine/magnets/SI_magnet_sextupole_field.png)

**Figure 41**: Field of the quadrupole (with dipolar field coils) half model.

<br />

##### Fieldmap Analysis

A 3D model of multifunctional sextupole magnet has been [[FAC:Fieldmap analysis|analyzed]] and approved. Fieldmap analysis for each function has been performed with maximum excitation currents, when residual multipoles are expected to be worse. For the analysis of horizontal and vertical orbit corrector fields, as well as for the skew quadrupole corrector field, the sextupolar function was also excited in order to guarantee fast convergence of the magnetic solution.

**Sextupolar function**

The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx).

**Sextupolar+Horizontal functions**

The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-ch/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-ch).

**Sextupolar+Vertical functions**

The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-cv/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-cv).

**Sextupolar+Skew functions**

The latest analyzed fieldmap can be [accessed here](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-qs/fieldmap-file.txt). A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-sextupoles-s15/tree/master/links-official-sx-qs).

<br />

##### Segmented Model

Currently the hard-edge approximation is being used to model sextupoles for beam dynamics calculations purposes. 

![](/img/machine/magnets/segmented_model_S.svg)

**Figure 42**: Strength profile of SI sextupole model

Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0750| 0.000| -0.000e+00| +0.000e+00| +2.470e+02 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 31**: SI sextupole half segmented model (maximum strength). 

<br />

#### SI Sextupole Magnet Measurements

A summary of magnet field measurements of SI S15 sextupoles.

<br />

##### Summary

**IntSext [(T/m)/A]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| SDA0 | -2.2551 | ± 0.00060 | 0.00166 |
| SFA0 | -2.2555 | ± 0.00038 | 0.00128 |
| SDB0 | -2.2514 | ± 0.00065 | 0.00226 |
| SFB0 | -2.2488 | ± 0.00079 | 0.00302 |
| SDP0 | -2.2525 | ± 0.00014 | 0.00046 |
| SFP0 | -2.2543 | ± 0.00033 | 0.00120 |
| SDA1 | -2.2467 | ± 0.00033 | 0.00111 |
| SFA1 | -2.2332 | ± 0.00035 | 0.00126 |
| SDB1 | -2.2545 | ± 0.00053 | 0.00181 |
| SFB1 | -2.2003 | ± 0.00105 | 0.00449 |
| SDP1 | -2.2550 | ± 0.00042 | 0.00125 |
| SFP1 | -2.2030 | ± 0.00029 | 0.00102 |
| SDA2 | -2.2584 | ± 0.00113 | 0.00301 |
| SFA2 | -2.2481 | ± 0.00044 | 0.00137 |
| SDB2 | -2.2532 | ± 0.00100 | 0.00498 |
| SFB2 | -2.2324 | ± 0.00079 | 0.00306 |
| SDP2 | -2.2523 | ± 0.00032 | 0.00115 |
| SFP2 | -2.2306 | ± 0.00048 | 0.00169 |
| SDA3 | -2.2494 | ± 0.00064 | 0.00202 |
| SDB3 | -2.2446 | ± 0.00060 | 0.00199 |
| SDP3 | -2.2484 | ± 0.00038 | 0.00134 |

**XCenter [um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| SDA0 | +11.2 | ± 7.5 |  27.8 
| SFA0 | +15.3 | ± 5.0 |  16.6 
| SDB0 | +14.5 | ± 6.0 |  26.1 
| SFB0 | +20.3 | ± 7.8 |  27.7 
| SDP0 | +12.1 | ± 4.9 |  15.1 
| SFP0 | +16.1 | ± 6.9 |  24.1 
| SDA1 | +10.2 | ± 6.2 |  21.1 
| SFA1 | +11.9 | ± 2.9 |  10.6 
| SDB1 | +11.3 | ± 5.3 |  20.4 
| SFB1 | +18.6 | ± 5.2 |  17.9 
| SDP1 | +13.7 | ± 6.3 |  20.3 
| SFP1 | +12.6 | ± 3.8 |  12.7 
| SDA2 | +11.6 | ± 5.2 |  17.6 
| SFA2 |  +9.7 | ± 6.5 |  23.5 
| SDB2 | +13.4 | ± 5.4 |  25.0 
| SFB2 | +15.5 | ± 7.1 |  25.8 
| SDP2 | +19.7 | ± 6.1 |  16.8 
| SFP2 | +14.0 | ± 4.4 |  14.6 
| SDA3 | +16.3 | ± 2.9 |   9.1 
| SDB3 | +14.6 | ± 6.4 |  23.1 
| SDP3 | +11.3 | ± 5.2 |  18.0 


**YCenter[um]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| SDA0 | +27.2 | ± 6.3 |  21.0 
| SFA0 | +22.6 | ± 4.1 |  12.5 
| SDB0 | +22.7 | ± 4.6 |  18.3 
| SFB0 | +27.8 | ± 4.9 |  24.9 
| SDP0 | +25.2 | ± 4.6 |  13.7 
| SFP0 | +23.6 | ± 5.6 |  17.9 
| SDA1 | +25.6 | ± 4.8 |  14.9 
| SFA1 | +23.0 | ± 4.3 |  13.8 
| SDB1 | +26.0 | ± 4.3 |  14.4 
| SFB1 | +25.5 | ± 3.6 |  14.2 
| SDP1 | +23.7 | ± 5.5 |  17.0 
| SFP1 | +25.9 | ± 3.5 |  13.4 
| SDA2 | +24.0 | ± 3.9 |  12.2 
| SFA2 | +25.1 | ± 3.5 |  11.8 
| SDB2 | +24.4 | ± 4.1 |  17.1 
| SFB2 | +27.8 | ± 3.9 |  14.4 
| SDP2 | +28.2 | ± 4.3 |  16.2 
| SFP2 | +25.8 | ± 2.8 |   7.8 
| SDA3 | +25.2 | ± 3.1 |  10.3 
| SDB3 | +24.7 | ± 4.1 |  15.0 
| SDP3 | +22.0 | ± 2.8 |  11.2 


**RollError [mrad]**

| Parameters | Avg | ± Std | MaxMin |
| --- | --- | --- | --- |
| SDA0 | -0.022 | ± 0.051 |  0.157 |
| SFA0 | +0.173 | ± 0.076 |  0.266 |
| SDB0 | +0.165 | ± 0.037 |  0.145 |
| SFB0 | +0.059 | ± 0.058 |  0.239 |
| SDP0 | +0.074 | ± 0.032 |  0.096 |
| SFP0 | +0.160 | ± 0.050 |  0.193 |
| SDA1 | +0.175 | ± 0.022 |  0.081 |
| SFA1 | +0.116 | ± 0.023 |  0.069 |
| SDB1 | +0.021 | ± 0.038 |  0.136 |
| SFB1 | +0.008 | ± 0.080 |  0.325 |
| SDP1 | +0.276 | ± 0.035 |  0.108 |
| SFP1 | +0.051 | ± 0.044 |  0.124 |
| SDA2 | +0.091 | ± 0.069 |  0.254 |
| SFA2 | +0.068 | ± 0.027 |  0.090 |
| SDB2 | +0.235 | ± 0.110 |  0.544 |
| SFB2 | -0.081 | ± 0.066 |  0.268 |
| SDP2 | +0.086 | ± 0.042 |  0.132 |
| SFP2 | -0.011 | ± 0.030 |  0.100 |
| SDA3 | +0.233 | ± 0.059 |  0.217 |
| SDB3 | +0.220 | ± 0.052 |  0.231 |
| SDP3 | +0.215 | ± 0.034 |  0.094 |

<br />

##### Integrated Sextupole

![](/img/machine/magnets/si-sextupoles-s15-integrated-sextupole.svg)

**Figure 43**:  Integrated sextupole strengths of S15 magnets.

<br />

##### Horizontal Magnetic Center

![](/img/machine/magnets/si-sextupoles-s15-xcenter.svg)

**Figure 44**: Horizontal magnet center of S15 magnets.

##### Vertical Magnetic Ce
<br />
nter

![](/img/machine/magnets/si-sextupoles-s15-ycenter.svg)

**Figure 45**: Vertical magnet center of S15 magnets.

<br />

##### Roll-Angle Error

![](/img/machine/magnets/si-sextupoles-s15-rollerror.svg)

**Figure 46**: Roll angle error of S15 magnets.

<br />

#### SI Sextupole Magnet Sorting

**SDA0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01M2:MA-SDA0| S15-004 |
|SI-05M1:MA-SDA0| S15-007 |
|SI-05M2:MA-SDA0| S15-270 |
|SI-09M1:MA-SDA0| S15-240 |
|SI-09M2:MA-SDA0| S15-283 |
|SI-13M1:MA-SDA0| S15-122 |
|SI-13M2:MA-SDA0| S15-184 |
|SI-17M1:MA-SDA0| S15-273 |
|SI-17M2:MA-SDA0| S15-118 |
|SI-01M1:MA-SDA0| S15-261  |

**SFA0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01M2:MA-SFA0| S15-278 |
|SI-05M1:MA-SFA0| S15-246 |
|SI-05M2:MA-SFA0| S15-276 |
|SI-09M1:MA-SFA0| S15-009 |
|SI-09M2:MA-SFA0| S15-015 |
|SI-13M1:MA-SFA0| S15-279 |
|SI-13M2:MA-SFA0| S15-033 |
|SI-17M1:MA-SFA0| S15-016 |
|SI-17M2:MA-SFA0| S15-010 |
|SI-01M1:MA-SFA0| S15-172  |

**SDB0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02M1:MA-SDB0| S15-159 |
|SI-02M2:MA-SDB0| S15-119 |
|SI-04M1:MA-SDB0| S15-132 |
|SI-04M2:MA-SDB0| S15-101 |
|SI-06M1:MA-SDB0| S15-026 |
|SI-06M2:MA-SDB0| S15-085 |
|SI-08M1:MA-SDB0| S15-259 |
|SI-08M2:MA-SDB0| S15-264 |
|SI-10M1:MA-SDB0| S15-154 |
|SI-10M2:MA-SDB0| S15-131 |
|SI-12M1:MA-SDB0| S15-241 |
|SI-12M2:MA-SDB0| S15-108 |
|SI-14M1:MA-SDB0| S15-086 |
|SI-14M2:MA-SDB0| S15-114 |
|SI-16M1:MA-SDB0| S15-213 |
|SI-16M2:MA-SDB0| S15-106 |
|SI-18M1:MA-SDB0| S15-157 |
|SI-18M2:MA-SDB0| S15-023 |
|SI-20M1:MA-SDB0| S15-045 |
|SI-20M2:MA-SDB0| S15-239  |

**SFB0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02M1:MA-SFB0| S15-076 |
|SI-02M2:MA-SFB0| S15-133 |
|SI-04M1:MA-SFB0| S15-152 |
|SI-04M2:MA-SFB0| S15-082 |
|SI-06M1:MA-SFB0| S15-074 |
|SI-06M2:MA-SFB0| S15-163 |
|SI-08M1:MA-SFB0| S15-103 |
|SI-08M2:MA-SFB0| S15-075 |
|SI-10M1:MA-SFB0| S15-072 |
|SI-10M2:MA-SFB0| S15-208 |
|SI-12M1:MA-SFB0| S15-039 |
|SI-12M2:MA-SFB0| S15-048 |
|SI-14M1:MA-SFB0| S15-070 |
|SI-14M2:MA-SFB0| S15-053 |
|SI-16M1:MA-SFB0| S15-038 |
|SI-16M2:MA-SFB0| S15-151 |
|SI-18M1:MA-SFB0| S15-077 |
|SI-18M2:MA-SFB0| S15-013 |
|SI-20M1:MA-SFB0| S15-056 |
|SI-20M2:MA-SFB0| S15-073  |

**SDP0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-03M1:MA-SDP0| S15-041 |
|SI-03M2:MA-SDP0| S15-110 |
|SI-07M1:MA-SDP0| S15-113 |
|SI-07M2:MA-SDP0| S15-269 |
|SI-11M1:MA-SDP0| S15-230 |
|SI-11M2:MA-SDP0| S15-147 |
|SI-15M1:MA-SDP0| S15-143 |
|SI-15M2:MA-SDP0| S15-193 |
|SI-19M1:MA-SDP0| S15-232 |
|SI-19M2:MA-SDP0| S15-187  |

**SFP0**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-03M1:MA-SFP0| S15-249 |
|SI-03M2:MA-SFP0| S15-221 |
|SI-07M1:MA-SFP0| S15-238 |
|SI-07M2:MA-SFP0| S15-044 |
|SI-11M1:MA-SFP0| S15-274 |
|SI-11M2:MA-SFP0| S15-135 |
|SI-15M1:MA-SFP0| S15-043 |
|SI-15M2:MA-SFP0| S15-040 |
|SI-19M1:MA-SFP0| S15-258 |
|SI-19M2:MA-SFP0| S15-093  |

**SDA1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-SDA1| S15-138 |
|SI-04C4:MA-SDA1| S15-120 |
|SI-05C1:MA-SDA1| S15-195 |
|SI-08C4:MA-SDA1| S15-212 |
|SI-09C1:MA-SDA1| S15-207 |
|SI-12C4:MA-SDA1| S15-164 |
|SI-13C1:MA-SDA1| S15-100 |
|SI-16C4:MA-SDA1| S15-141 |
|SI-17C1:MA-SDA1| S15-223 |
|SI-20C4:MA-SDA1| S15-112  |

**SFA1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-SFA1| S15-142 |
|SI-04C4:MA-SFA1| S15-219 |
|SI-05C1:MA-SFA1| S15-102 |
|SI-08C4:MA-SFA1| S15-286 |
|SI-09C1:MA-SFA1| S15-236 |
|SI-12C4:MA-SFA1| S15-266 |
|SI-13C1:MA-SFA1| S15-265 |
|SI-16C4:MA-SFA1| S15-272 |
|SI-17C1:MA-SFA1| S15-098 |
|SI-20C4:MA-SFA1| S15-105  |

**SDB1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C4:MA-SDB1| S15-168 |
|SI-02C1:MA-SDB1| S15-181 |
|SI-03C4:MA-SDB1| S15-174 |
|SI-04C1:MA-SDB1| S15-128 |
|SI-05C4:MA-SDB1| S15-146 |
|SI-06C1:MA-SDB1| S15-268 |
|SI-07C4:MA-SDB1| S15-139 |
|SI-08C1:MA-SDB1| S15-202 |
|SI-09C4:MA-SDB1| S15-244 |
|SI-10C1:MA-SDB1| S15-242 |
|SI-11C4:MA-SDB1| S15-149 |
|SI-12C1:MA-SDB1| S15-124 |
|SI-13C4:MA-SDB1| S15-107 |
|SI-14C1:MA-SDB1| S15-189 |
|SI-15C4:MA-SDB1| S15-188 |
|SI-16C1:MA-SDB1| S15-177 |
|SI-17C4:MA-SDB1| S15-186 |
|SI-18C1:MA-SDB1| S15-126 |
|SI-19C4:MA-SDB1| S15-123 |
|SI-20C1:MA-SDB1| S15-170  |

**SFB1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C4:MA-SFB1| S15-104 |
|SI-02C1:MA-SFB1| S15-080 |
|SI-03C4:MA-SFB1| S15-061 |
|SI-04C1:MA-SFB1| S15-067 |
|SI-05C4:MA-SFB1| S15-068 |
|SI-06C1:MA-SFB1| S15-034 |
|SI-07C4:MA-SFB1| S15-060 |
|SI-08C1:MA-SFB1| S15-081 |
|SI-09C4:MA-SFB1| S15-156 |
|SI-10C1:MA-SFB1| S15-257 |
|SI-11C4:MA-SFB1| S15-234 |
|SI-12C1:MA-SFB1| S15-182 |
|SI-13C4:MA-SFB1| S15-233 |
|SI-14C1:MA-SFB1| S15-169 |
|SI-15C4:MA-SFB1| S15-059 |
|SI-16C1:MA-SFB1| S15-275 |
|SI-17C4:MA-SFB1| S15-153 |
|SI-18C1:MA-SFB1| S15-052 |
|SI-19C4:MA-SFB1| S15-071 |
|SI-20C1:MA-SFB1| S15-065  |

**SDP1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02C4:MA-SDP1| S15-092 |
|SI-03C1:MA-SDP1| S15-017 |
|SI-06C4:MA-SDP1| S15-175 |
|SI-07C1:MA-SDP1| S15-271 |
|SI-10C4:MA-SDP1| S15-020 |
|SI-11C1:MA-SDP1| S15-050 |
|SI-14C4:MA-SDP1| S15-109 |
|SI-15C1:MA-SDP1| S15-012 |
|SI-18C4:MA-SDP1| S15-155 |
|SI-19C1:MA-SDP1| S15-227  |

**SFP1**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02C4:MA-SFP1| S15-063 |
|SI-03C1:MA-SFP1| S15-260 |
|SI-06C4:MA-SFP1| S15-180 |
|SI-07C1:MA-SFP1| S15-176 |
|SI-10C4:MA-SFP1| S15-250 |
|SI-11C1:MA-SFP1| S15-209 |
|SI-14C4:MA-SFP1| S15-165 |
|SI-15C1:MA-SFP1| S15-253 |
|SI-18C4:MA-SFP1| S15-229 |
|SI-19C1:MA-SFP1| S15-251  |

**SDA2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C1:MA-SDA2| S15-248 |
|SI-04C4:MA-SDA2| S15-277 |
|SI-05C1:MA-SDA2| S15-245 |
|SI-08C4:MA-SDA2| S15-029 |
|SI-09C1:MA-SDA2| S15-256 |
|SI-12C4:MA-SDA2| S15-167 |
|SI-13C1:MA-SDA2| S15-031 |
|SI-16C4:MA-SDA2| S15-263 |
|SI-17C1:MA-SDA2| S15-166 |
|SI-20C4:MA-SDA2| S15-032  |

**SFA2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C2:MA-SFA2| S15-282 |
|SI-04C3:MA-SFA2| S15-117 |
|SI-05C2:MA-SFA2| S15-021 |
|SI-08C3:MA-SFA2| S15-145 |
|SI-09C2:MA-SFA2| S15-220 |
|SI-12C3:MA-SFA2| S15-243 |
|SI-13C2:MA-SFA2| S15-171 |
|SI-16C3:MA-SFA2| S15-280 |
|SI-17C2:MA-SFA2| S15-281 |
|SI-20C3:MA-SFA2| S15-005  |

**SDB2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C4:MA-SDB2| S15-197 |
|SI-02C1:MA-SDB2| S15-247 |
|SI-03C4:MA-SDB2| S15-218 |
|SI-04C1:MA-SDB2| S15-099 |
|SI-05C4:MA-SDB2| S15-211 |
|SI-06C1:MA-SDB2| S15-006 |
|SI-07C4:MA-SDB2| S15-235 |
|SI-08C1:MA-SDB2| S15-130 |
|SI-09C4:MA-SDB2| S15-226 |
|SI-10C1:MA-SDB2| S15-254 |
|SI-11C4:MA-SDB2| S15-162 |
|SI-12C1:MA-SDB2| S15-206 |
|SI-13C4:MA-SDB2| S15-096 |
|SI-14C1:MA-SDB2| S15-224 |
|SI-15C4:MA-SDB2| S15-140 |
|SI-16C1:MA-SDB2| S15-225 |
|SI-17C4:MA-SDB2| S15-129 |
|SI-18C1:MA-SDB2| S15-027 |
|SI-19C4:MA-SDB2| S15-222 |
|SI-20C1:MA-SDB2| S15-203  |

**SFB2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C3:MA-SFB2| S15-121 |
|SI-02C2:MA-SFB2| S15-190 |
|SI-03C3:MA-SFB2| S15-192 |
|SI-04C2:MA-SFB2| S15-087 |
|SI-05C3:MA-SFB2| S15-210 |
|SI-06C2:MA-SFB2| S15-231 |
|SI-07C3:MA-SFB2| S15-158 |
|SI-08C2:MA-SFB2| S15-115 |
|SI-09C3:MA-SFB2| S15-008 |
|SI-10C2:MA-SFB2| S15-160 |
|SI-11C3:MA-SFB2| S15-019 |
|SI-12C2:MA-SFB2| S15-267 |
|SI-13C3:MA-SFB2| S15-078 |
|SI-14C2:MA-SFB2| S15-030 |
|SI-15C3:MA-SFB2| S15-090 |
|SI-16C2:MA-SFB2| S15-116 |
|SI-17C3:MA-SFB2| S15-018 |
|SI-18C2:MA-SFB2| S15-097 |
|SI-19C3:MA-SFB2| S15-179 |
|SI-20C2:MA-SFB2| S15-185  |

**SDP2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02C4:MA-SDP2| S15-252 |
|SI-03C1:MA-SDP2| S15-199 |
|SI-06C4:MA-SDP2| S15-088 |
|SI-07C1:MA-SDP2| S15-024 |
|SI-10C4:MA-SDP2| S15-079 |
|SI-11C1:MA-SDP2| S15-191 |
|SI-14C4:MA-SDP2| S15-025 |
|SI-15C1:MA-SDP2| S15-014 |
|SI-18C4:MA-SDP2| S15-161 |
|SI-19C1:MA-SDP2| S15-028  |

**SFP2**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02C3:MA-SFP2| S15-062 |
|SI-03C2:MA-SFP2| S15-049 |
|SI-06C3:MA-SFP2| S15-194 |
|SI-07C2:MA-SFP2| S15-064 |
|SI-10C3:MA-SFP2| S15-237 |
|SI-11C2:MA-SFP2| S15-127 |
|SI-14C3:MA-SFP2| S15-057 |
|SI-15C2:MA-SFP2| S15-173 |
|SI-18C3:MA-SFP2| S15-089 |
|SI-19C2:MA-SFP2| S15-054  |

**SDA3**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C2:MA-SDA3| S15-217 |
|SI-04C3:MA-SDA3| S15-215 |
|SI-05C2:MA-SDA3| S15-035 |
|SI-08C3:MA-SDA3| S15-144 |
|SI-09C2:MA-SDA3| S15-216 |
|SI-12C3:MA-SDA3| S15-214 |
|SI-13C2:MA-SDA3| S15-204 |
|SI-16C3:MA-SDA3| S15-036 |
|SI-17C2:MA-SDA3| S15-051 |
|SI-20C3:MA-SDA3| S15-022  |

**SDB3**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-01C3:MA-SDB3| S15-084 |
|SI-02C2:MA-SDB3| S15-111 |
|SI-03C3:MA-SDB3| S15-228 |
|SI-04C2:MA-SDB3| S15-150 |
|SI-05C3:MA-SDB3| S15-198 |
|SI-06C2:MA-SDB3| S15-201 |
|SI-07C3:MA-SDB3| S15-196 |
|SI-08C2:MA-SDB3| S15-125 |
|SI-09C3:MA-SDB3| S15-183 |
|SI-10C2:MA-SDB3| S15-205 |
|SI-11C3:MA-SDB3| S15-047 |
|SI-12C2:MA-SDB3| S15-200 |
|SI-13C3:MA-SDB3| S15-037 |
|SI-14C2:MA-SDB3| S15-148 |
|SI-15C3:MA-SDB3| S15-058 |
|SI-16C2:MA-SDB3| S15-178 |
|SI-17C3:MA-SDB3| S15-255 |
|SI-18C2:MA-SDB3| S15-134 |
|SI-19C3:MA-SDB3| S15-083 |
|SI-20C2:MA-SDB3| S15-046  |

**SDP3**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|SI-02C3:MA-SDP3| S15-042 |
|SI-03C2:MA-SDP3| S15-095 |
|SI-06C3:MA-SDP3| S15-055 |
|SI-07C2:MA-SDP3| S15-094 |
|SI-10C3:MA-SDP3| S15-011 |
|SI-11C2:MA-SDP3| S15-262 |
|SI-14C3:MA-SDP3| S15-136 |
|SI-15C2:MA-SDP3| S15-284 |
|SI-18C3:MA-SDP3| S15-137 |
|SI-19C2:MA-SDP3| S15-285  |

**Not Used**

|Magnet Name| Magnet Serial ID |
| --- | --- |
|---| S15-091  |

**Table 32**: Storage Ring Sextupoles Installation.

<br />

### Storage Ring Vertical Corrector Magnets

Apart from slow horizontal and vertical slow orbit correctors implemented as additional coils in sextupole magnets, there will be 20 vertical corrector magnets located in C2 dispersion sections. These magnets will be identical to the ones used in the Booster. 

<br />

### Storage Ring Fast Orbit Correctors

Sirius storage ring is planned to have 80 horizontal and 80 vertical fast orbit correctors, as well as 10 skew quadrupole correctors. There will be two types of fast correctors: FC1 magnets with iron poles resembling skew quadrupoles, where horizontal, vertical and skew correctors are implemented as independent coils, and FC2 magnets, which are CF1 magnets rotated 45 degrees with no skew corrector coils. FC2 magnets are installed in odd-numbered C2 sectors to allow for synchrotron light of B2 dipoles to go to diagnostics beamlines. Fast correctors will sit on top of stainless steel vacuum chambers coated with a thin copper inner layer.

<br />

#### SI Fast Correctors Specifications

##### Main Parameters

| |Horizontal| Vertical| Skew |
| --- | --- | --- | --- |
|Number of fast correctors| 80| 80| 10 ¹ |
|Maximum fast corrector strength| 30 Î¼rad| 30 Î¼rad| 0.1 T ² |

¹ located at even C2 sectors.

² based on a 2.6%(2.3%) coupling value when one skew magnet is turned on in a straight high(low)-beta straight section. 

**Table 33**: Storage Ring fast orbit correctors.

<br />

##### Multipole Errors

The impact on the beam dynamics of residual multipole errors for the fast corrector magnets has been analyzed from fieldmaps of current models. The impact is very small and the current magnet models have been accepted. Magnetic measurements for prototypes are yet to be taken and analyzed. 

<br />

####  SI Fast Correctors Magnet 3D Models

![](/img/machine/magnets/SI_magnet_fast_corrector_drawing.png)

**Figure 47**: 3D drawing of the fast corrector model.

![](/img/machine/magnets/SI_magnet_fast_corrector_field.png)

**Figure 48**: Field of the fast corrector model.

<br />

###### Fieldmap Analysis

A 3D model of multifunctional sextupole magnet has been analyzed and approved. Fieldmap analysis for each function has been performed with maximum excitation currents, when residual multipoles are expected to be worse. For the analysis of horizontal and vertical orbit corrector fields, as well as for the skew quadrupole corrector field, the sextupolar function was also excited in order to guarantee fast convergence of the magnetic solution.

**FC1 Horizontal correction function**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-fast-correctors/tree/master/links-official-FC1-fch).

**FC1 Vertical correction function**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-fast-correctors/tree/master/links-official-FC1-fcv).

**FC1 Skew quadrupole function**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-fast-correctors/tree/master/links-official-FC1-qs).

**FC2 Horizontal correction function**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-fast-correctors/tree/master/links-official-FC2-fch).

**FC2 Vertical correction function**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/si-fast-correctors/tree/master/links-official-FC2-fcv). 

<br />

###### Segmented Model

A hardedge model is being used for fast correctors. 

<br />

#### SI Fast Correctors Magnet Measurements

Not available yet.

<br />

### Storage Ring Magnet Families

The storage ring magnets are grouped into families. The tables below list the storage ring families with their individual magnets.

#### Storage Ring Dipole Families

|| SI-Fam:PS-B1B2-1| SI-Fam:PS-B1B2-2| SI-Fam:MA-QB1B2 |
| --- | --- | --- | --- |
|1| SI-01C1:MA-B1| SI-01C1:MA-B1| SI-01C1:MA-B1 |
|2| SI-01C2:MA-B2| SI-01C2:MA-B2| SI-01C2:MA-B2 |
|3| SI-01C3:MA-B2| SI-01C3:MA-B2| SI-01C3:MA-B2 |
|4| SI-01C4:MA-B1| SI-01C4:MA-B1| SI-01C4:MA-B1 |
|5| SI-02C1:MA-B1| SI-02C1:MA-B1| SI-02C1:MA-B1 |
|6| SI-02C2:MA-B2| SI-02C2:MA-B2| SI-02C2:MA-B2 |
|7| SI-02C3:MA-B2| SI-02C3:MA-B2| SI-02C3:MA-B2 |
|8| SI-02C4:MA-B1| SI-02C4:MA-B1| SI-02C4:MA-B1 |
|9| SI-03C1:MA-B1| SI-03C1:MA-B1| SI-03C1:MA-B1 |
|10| SI-03C2:MA-B2| SI-03C2:MA-B2| SI-03C2:MA-B2 |
|11| SI-03C3:MA-B2| SI-03C3:MA-B2| SI-03C3:MA-B2 |
|12| SI-03C4:MA-B1| SI-03C4:MA-B1| SI-03C4:MA-B1 |
|13| SI-04C1:MA-B1| SI-04C1:MA-B1| SI-04C1:MA-B1 |
|14| SI-04C2:MA-B2| SI-04C2:MA-B2| SI-04C2:MA-B2 |
|15| SI-04C3:MA-B2| SI-04C3:MA-B2| SI-04C3:MA-B2 |
|16| SI-04C4:MA-B1| SI-04C4:MA-B1| SI-04C4:MA-B1 |
|17| SI-05C1:MA-B1| SI-05C1:MA-B1| SI-05C1:MA-B1 |
|18| SI-05C2:MA-B2| SI-05C2:MA-B2| SI-05C2:MA-B2 |
|19| SI-05C3:MA-B2| SI-05C3:MA-B2| SI-05C3:MA-B2 |
|20| SI-05C4:MA-B1| SI-05C4:MA-B1| SI-05C4:MA-B1 |
|21| SI-06C1:MA-B1| SI-06C1:MA-B1| SI-06C1:MA-B1 |
|22| SI-06C2:MA-B2| SI-06C2:MA-B2| SI-06C2:MA-B2 |
|23| SI-06C3:MA-B2| SI-06C3:MA-B2| SI-06C3:MA-B2 |
|24| SI-06C4:MA-B1| SI-06C4:MA-B1| SI-06C4:MA-B1 |
|25| SI-07C1:MA-B1| SI-07C1:MA-B1| SI-07C1:MA-B1 |
|26| SI-07C2:MA-B2| SI-07C2:MA-B2| SI-07C2:MA-B2 |
|27| SI-07C3:MA-B2| SI-07C3:MA-B2| SI-07C3:MA-B2 |
|28| SI-07C4:MA-B1| SI-07C4:MA-B1| SI-07C4:MA-B1 |
|29| SI-08C1:MA-B1| SI-08C1:MA-B1| SI-08C1:MA-B1 |
|30| SI-08C2:MA-B2| SI-08C2:MA-B2| SI-08C2:MA-B2 |
|31| SI-08C3:MA-B2| SI-08C3:MA-B2| SI-08C3:MA-B2 |
|32| SI-08C4:MA-B1| SI-08C4:MA-B1| SI-08C4:MA-B1 |
|33| SI-09C1:MA-B1| SI-09C1:MA-B1| SI-09C1:MA-B1 |
|34| SI-09C2:MA-B2| SI-09C2:MA-B2| SI-09C2:MA-B2 |
|35| SI-09C3:MA-B2| SI-09C3:MA-B2| SI-09C3:MA-B2 |
|36| SI-09C4:MA-B1| SI-09C4:MA-B1| SI-09C4:MA-B1 |
|37| SI-10C1:MA-B1| SI-10C1:MA-B1| SI-10C1:MA-B1 |
|38| SI-10C2:MA-B2| SI-10C2:MA-B2| SI-10C2:MA-B2 |
|39| SI-10C3:MA-B2| SI-10C3:MA-B2| SI-10C3:MA-B2 |
|40| SI-10C4:MA-B1| SI-10C4:MA-B1| SI-10C4:MA-B1 |
|41| SI-11C1:MA-B1| SI-11C1:MA-B1| SI-11C1:MA-B1 |
|42| SI-11C2:MA-B2| SI-11C2:MA-B2| SI-11C2:MA-B2 |
|43| SI-11C3:MA-B2| SI-11C3:MA-B2| SI-11C3:MA-B2 |
|44| SI-11C4:MA-B1| SI-11C4:MA-B1| SI-11C4:MA-B1 |
|45| SI-12C1:MA-B1| SI-12C1:MA-B1| SI-12C1:MA-B1 |
|46| SI-12C2:MA-B2| SI-12C2:MA-B2| SI-12C2:MA-B2 |
|47| SI-12C3:MA-B2| SI-12C3:MA-B2| SI-12C3:MA-B2 |
|48| SI-12C4:MA-B1| SI-12C4:MA-B1| SI-12C4:MA-B1 |
|49| SI-13C1:MA-B1| SI-13C1:MA-B1| SI-13C1:MA-B1 |
|50| SI-13C2:MA-B2| SI-13C2:MA-B2| SI-13C2:MA-B2 |
|51| SI-13C3:MA-B2| SI-13C3:MA-B2| SI-13C3:MA-B2 |
|52| SI-13C4:MA-B1| SI-13C4:MA-B1| SI-13C4:MA-B1 |
|53| SI-14C1:MA-B1| SI-14C1:MA-B1| SI-14C1:MA-B1 |
|54| SI-14C2:MA-B2| SI-14C2:MA-B2| SI-14C2:MA-B2 |
|55| SI-14C3:MA-B2| SI-14C3:MA-B2| SI-14C3:MA-B2 |
|56| SI-14C4:MA-B1| SI-14C4:MA-B1| SI-14C4:MA-B1 |
|57| SI-15C1:MA-B1| SI-15C1:MA-B1| SI-15C1:MA-B1 |
|58| SI-15C2:MA-B2| SI-15C2:MA-B2| SI-15C2:MA-B2 |
|59| SI-15C3:MA-B2| SI-15C3:MA-B2| SI-15C3:MA-B2 |
|60| SI-15C4:MA-B1| SI-15C4:MA-B1| SI-15C4:MA-B1 |
|61| SI-16C1:MA-B1| SI-16C1:MA-B1| SI-16C1:MA-B1 |
|62| SI-16C2:MA-B2| SI-16C2:MA-B2| SI-16C2:MA-B2 |
|63| SI-16C3:MA-B2| SI-16C3:MA-B2| SI-16C3:MA-B2 |
|64| SI-16C4:MA-B1| SI-16C4:MA-B1| SI-16C4:MA-B1 |
|65| SI-17C1:MA-B1| SI-17C1:MA-B1| SI-17C1:MA-B1 |
|66| SI-17C2:MA-B2| SI-17C2:MA-B2| SI-17C2:MA-B2 |
|67| SI-17C3:MA-B2| SI-17C3:MA-B2| SI-17C3:MA-B2 |
|68| SI-17C4:MA-B1| SI-17C4:MA-B1| SI-17C4:MA-B1 |
|69| SI-18C1:MA-B1| SI-18C1:MA-B1| SI-18C1:MA-B1 |
|70| SI-18C2:MA-B2| SI-18C2:MA-B2| SI-18C2:MA-B2 |
|71| SI-18C3:MA-B2| SI-18C3:MA-B2| SI-18C3:MA-B2 |
|72| SI-18C4:MA-B1| SI-18C4:MA-B1| SI-18C4:MA-B1 |
|73| SI-19C1:MA-B1| SI-19C1:MA-B1| SI-19C1:MA-B1 |
|74| SI-19C2:MA-B2| SI-19C2:MA-B2| SI-19C2:MA-B2 |
|75| SI-19C3:MA-B2| SI-19C3:MA-B2| SI-19C3:MA-B2 |
|76| SI-19C4:MA-B1| SI-19C4:MA-B1| SI-19C4:MA-B1 |
|77| SI-20C1:MA-B1| SI-20C1:MA-B1| SI-20C1:MA-B1 |
|78| SI-20C2:MA-B2| SI-20C2:MA-B2| SI-20C2:MA-B2 |
|79| SI-20C3:MA-B2| SI-20C3:MA-B2| SI-20C3:MA-B2 |
|80| SI-20C4:MA-B1| SI-20C4:MA-B1| SI-20C4:MA-B1 |

**Table 34**: Storage Ring Dipole Families (including transverse gradient variation with QB1B2) 

<br />

#### Storage Ring Quadrupole Families

|| SI-Fam:MA-Q1| SI-Fam:MA-Q2| SI-Fam:MA-Q3| SI-Fam:MA-Q4 |
| --- | --- | --- | --- | --- |
|1| SI-01C1:MA-Q1| SI-01C1:MA-Q2| SI-01C2:MA-Q3| SI-01C2:MA-Q4 |
|2| SI-01C4:MA-Q1| SI-01C4:MA-Q2| SI-01C3:MA-Q3| SI-01C3:MA-Q4 |
|3| SI-02C1:MA-Q1| SI-02C1:MA-Q2| SI-02C2:MA-Q3| SI-02C2:MA-Q4 |
|4| SI-02C4:MA-Q1| SI-02C4:MA-Q2| SI-02C3:MA-Q3| SI-02C3:MA-Q4 |
|5| SI-03C1:MA-Q1| SI-03C1:MA-Q2| SI-03C2:MA-Q3| SI-03C2:MA-Q4 |
|6| SI-03C4:MA-Q1| SI-03C4:MA-Q2| SI-03C3:MA-Q3| SI-03C3:MA-Q4 |
|7| SI-04C1:MA-Q1| SI-04C1:MA-Q2| SI-04C2:MA-Q3| SI-04C2:MA-Q4 |
|8| SI-04C4:MA-Q1| SI-04C4:MA-Q2| SI-04C3:MA-Q3| SI-04C3:MA-Q4 |
|9| SI-05C1:MA-Q1| SI-05C1:MA-Q2| SI-05C2:MA-Q3| SI-05C2:MA-Q4 |
|10| SI-05C4:MA-Q1| SI-05C4:MA-Q2| SI-05C3:MA-Q3| SI-05C3:MA-Q4 |
|11| SI-06C1:MA-Q1| SI-06C1:MA-Q2| SI-06C2:MA-Q3| SI-06C2:MA-Q4 |
|12| SI-06C4:MA-Q1| SI-06C4:MA-Q2| SI-06C3:MA-Q3| SI-06C3:MA-Q4 |
|13| SI-07C1:MA-Q1| SI-07C1:MA-Q2| SI-07C2:MA-Q3| SI-07C2:MA-Q4 |
|14| SI-07C4:MA-Q1| SI-07C4:MA-Q2| SI-07C3:MA-Q3| SI-07C3:MA-Q4 |
|15| SI-08C1:MA-Q1| SI-08C1:MA-Q2| SI-08C2:MA-Q3| SI-08C2:MA-Q4 |
|16| SI-08C4:MA-Q1| SI-08C4:MA-Q2| SI-08C3:MA-Q3| SI-08C3:MA-Q4 |
|17| SI-09C1:MA-Q1| SI-09C1:MA-Q2| SI-09C2:MA-Q3| SI-09C2:MA-Q4 |
|18| SI-09C4:MA-Q1| SI-09C4:MA-Q2| SI-09C3:MA-Q3| SI-09C3:MA-Q4 |
|19| SI-10C1:MA-Q1| SI-10C1:MA-Q2| SI-10C2:MA-Q3| SI-10C2:MA-Q4 |
|20| SI-10C4:MA-Q1| SI-10C4:MA-Q2| SI-10C3:MA-Q3| SI-10C3:MA-Q4 |
|21| SI-11C1:MA-Q1| SI-11C1:MA-Q2| SI-11C2:MA-Q3| SI-11C2:MA-Q4 |
|22| SI-11C4:MA-Q1| SI-11C4:MA-Q2| SI-11C3:MA-Q3| SI-11C3:MA-Q4 |
|23| SI-12C1:MA-Q1| SI-12C1:MA-Q2| SI-12C2:MA-Q3| SI-12C2:MA-Q4 |
|24| SI-12C4:MA-Q1| SI-12C4:MA-Q2| SI-12C3:MA-Q3| SI-12C3:MA-Q4 |
|25| SI-13C1:MA-Q1| SI-13C1:MA-Q2| SI-13C2:MA-Q3| SI-13C2:MA-Q4 |
|26| SI-13C4:MA-Q1| SI-13C4:MA-Q2| SI-13C3:MA-Q3| SI-13C3:MA-Q4 |
|27| SI-14C1:MA-Q1| SI-14C1:MA-Q2| SI-14C2:MA-Q3| SI-14C2:MA-Q4 |
|28| SI-14C4:MA-Q1| SI-14C4:MA-Q2| SI-14C3:MA-Q3| SI-14C3:MA-Q4 |
|29| SI-15C1:MA-Q1| SI-15C1:MA-Q2| SI-15C2:MA-Q3| SI-15C2:MA-Q4 |
|30| SI-15C4:MA-Q1| SI-15C4:MA-Q2| SI-15C3:MA-Q3| SI-15C3:MA-Q4 |
|31| SI-16C1:MA-Q1| SI-16C1:MA-Q2| SI-16C2:MA-Q3| SI-16C2:MA-Q4 |
|32| SI-16C4:MA-Q1| SI-16C4:MA-Q2| SI-16C3:MA-Q3| SI-16C3:MA-Q4 |
|33| SI-17C1:MA-Q1| SI-17C1:MA-Q2| SI-17C2:MA-Q3| SI-17C2:MA-Q4 |
|34| SI-17C4:MA-Q1| SI-17C4:MA-Q2| SI-17C3:MA-Q3| SI-17C3:MA-Q4 |
|35| SI-18C1:MA-Q1| SI-18C1:MA-Q2| SI-18C2:MA-Q3| SI-18C2:MA-Q4 |
|36| SI-18C4:MA-Q1| SI-18C4:MA-Q2| SI-18C3:MA-Q3| SI-18C3:MA-Q4 |
|37| SI-19C1:MA-Q1| SI-19C1:MA-Q2| SI-19C2:MA-Q3| SI-19C2:MA-Q4 |
|38| SI-19C4:MA-Q1| SI-19C4:MA-Q2| SI-19C3:MA-Q3| SI-19C3:MA-Q4 |
|39| SI-20C1:MA-Q1| SI-20C1:MA-Q2| SI-20C2:MA-Q3| SI-20C2:MA-Q4 |
|40| SI-20C4:MA-Q1| SI-20C4:MA-Q2| SI-20C3:MA-Q3| SI-20C3:MA-Q4  |

**Table 35**: Storage Ring Dispersive Quadrupole Families 

|| SI-Fam:MA-QFA| SI-Fam:MA-QDA| SI-Fam:MA-QFP| SI-Fam:MA-QDP1| SI-Fam:MA-QDP2| SI-Fam:MA-QFB| SI-Fam:MA-QDB1| SI-Fam:MA-QDB2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1| SI-01M1:MA-QFA| SI-01M1:MA-QDA| SI-03M1:MA-QFP| SI-03M1:MA-QDP1| SI-03M1:MA-QDP2| SI-02M1:MA-QFB| SI-02M1:MA-QDB1| SI-02M1:MA-QDB2 |
|2| SI-01M2:MA-QFA| SI-01M2:MA-QDA| SI-03M2:MA-QFP| SI-03M2:MA-QDP1| SI-03M2:MA-QDP2| SI-02M2:MA-QFB| SI-02M2:MA-QDB1| SI-02M2:MA-QDB2 |
|3| SI-05M1:MA-QFA| SI-05M1:MA-QDA| SI-07M1:MA-QFP| SI-07M1:MA-QDP1| SI-07M1:MA-QDP2| SI-04M1:MA-QFB| SI-04M1:MA-QDB1| SI-04M1:MA-QDB2 |
|4| SI-05M2:MA-QFA| SI-05M2:MA-QDA| SI-07M2:MA-QFP| SI-07M2:MA-QDP1| SI-07M2:MA-QDP2| SI-04M2:MA-QFB| SI-04M2:MA-QDB1| SI-04M2:MA-QDB2 |
|5| SI-09M1:MA-QFA| SI-09M1:MA-QDA| SI-11M1:MA-QFP| SI-11M1:MA-QDP1| SI-11M1:MA-QDP2| SI-06M1:MA-QFB| SI-06M1:MA-QDB1| SI-06M1:MA-QDB2 |
|6| SI-09M2:MA-QFA| SI-09M2:MA-QDA| SI-11M2:MA-QFP| SI-11M2:MA-QDP1| SI-11M2:MA-QDP2| SI-06M2:MA-QFB| SI-06M2:MA-QDB1| SI-06M2:MA-QDB2 |
|7| SI-13M1:MA-QFA| SI-13M1:MA-QDA| SI-15M1:MA-QFP| SI-15M1:MA-QDP1| SI-15M1:MA-QDP2| SI-08M1:MA-QFB| SI-08M1:MA-QDB1| SI-08M1:MA-QDB2 |
|8| SI-13M2:MA-QFA| SI-13M2:MA-QDA| SI-15M2:MA-QFP| SI-15M2:MA-QDP1| SI-15M2:MA-QDP2| SI-08M2:MA-QFB| SI-08M2:MA-QDB1| SI-08M2:MA-QDB2 |
|9| SI-17M1:MA-QFA| SI-17M1:MA-QDA| SI-19M1:MA-QFP| SI-19M1:MA-QDP1| SI-19M1:MA-QDP2| SI-10M1:MA-QFB| SI-10M1:MA-QDB1| SI-10M1:MA-QDB2 |
|10| SI-17M2:MA-QFA| SI-17M2:MA-QDA| SI-19M2:MA-QFP| SI-19M2:MA-QDP1| SI-19M2:MA-QDP2| SI-10M2:MA-QFB| SI-10M2:MA-QDB1| SI-10M2:MA-QDB2 |
|11| 	|	|	|	|	|SI-12M1:MA-QFB| SI-12M1:MA-QDB1| SI-12M1:MA-QDB2 |
|12| 	|	|	|	|	|SI-12M2:MA-QFB| SI-12M2:MA-QDB1| SI-12M2:MA-QDB2 |
|13| 	|	|	|	|	|SI-14M1:MA-QFB| SI-14M1:MA-QDB1| SI-14M1:MA-QDB2 |
|14| 	|	|	|	|	|SI-14M2:MA-QFB| SI-14M2:MA-QDB1| SI-14M2:MA-QDB2 |
|15| 	|	|	|	|	|SI-16M1:MA-QFB| SI-16M1:MA-QDB1| SI-16M1:MA-QDB2 |
|16| 	|	|	|	|	|SI-16M2:MA-QFB| SI-16M2:MA-QDB1| SI-16M2:MA-QDB2 |
|17| 	|	|	|	|	|SI-18M1:MA-QFB| SI-18M1:MA-QDB1| SI-18M1:MA-QDB2 |
|18| 	|	|	|	|	|SI-18M2:MA-QFB| SI-18M2:MA-QDB1| SI-18M2:MA-QDB2 |
|19| 	|	|	|	|	|SI-20M1:MA-QFB| SI-20M1:MA-QDB1| SI-20M1:MA-QDB2 |
|20| 	|	|	|	|	|SI-20M2:MA-QFB| SI-20M2:MA-QDB1| SI-20M2:MA-QDB2  |

**Table 36**: Storage Ring Non Dispersive Quadrupole Families 

<br />

#### Storage Ring Sextupole Families

|| SI-Fam:MA-SFA0| SI-Fam:MA-SFA1| SI-Fam:MA-SFA2| SI-Fam:MA-SDA0| SI-Fam:MA-SDA1| SI-Fam:MA-SDA2| SI-Fam:MA-SDA3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|1| SI-01M1:MA-SFA0| SI-01C1:MA-SFA1| SI-01C2:MA-SFA2| SI-01M1:MA-SDA0| SI-01C1:MA-SDA1| SI-01C1:MA-SDA2| SI-01C2:MA-SDA3 |
|2| SI-01M2:MA-SFA0| SI-04C4:MA-SFA1| SI-04C3:MA-SFA2| SI-01M2:MA-SDA0| SI-04C4:MA-SDA1| SI-04C4:MA-SDA2| SI-04C3:MA-SDA3 |
|3| SI-05M1:MA-SFA0| SI-05C1:MA-SFA1| SI-05C2:MA-SFA2| SI-05M1:MA-SDA0| SI-05C1:MA-SDA1| SI-05C1:MA-SDA2| SI-05C2:MA-SDA3 |
|4| SI-05M2:MA-SFA0| SI-08C4:MA-SFA1| SI-08C3:MA-SFA2| SI-05M2:MA-SDA0| SI-08C4:MA-SDA1| SI-08C4:MA-SDA2| SI-08C3:MA-SDA3 |
|5| SI-09M1:MA-SFA0| SI-09C1:MA-SFA1| SI-09C2:MA-SFA2| SI-09M1:MA-SDA0| SI-09C1:MA-SDA1| SI-09C1:MA-SDA2| SI-09C2:MA-SDA3 |
|6| SI-09M2:MA-SFA0| SI-12C4:MA-SFA1| SI-12C3:MA-SFA2| SI-09M2:MA-SDA0| SI-12C4:MA-SDA1| SI-12C4:MA-SDA2| SI-12C3:MA-SDA3 |
|7| SI-13M1:MA-SFA0| SI-13C1:MA-SFA1| SI-13C2:MA-SFA2| SI-13M1:MA-SDA0| SI-13C1:MA-SDA1| SI-13C1:MA-SDA2| SI-13C2:MA-SDA3 |
|8| SI-13M2:MA-SFA0| SI-16C4:MA-SFA1| SI-16C3:MA-SFA2| SI-13M2:MA-SDA0| SI-16C4:MA-SDA1| SI-16C4:MA-SDA2| SI-16C3:MA-SDA3 |
|9| SI-17M1:MA-SFA0| SI-17C1:MA-SFA1| SI-17C2:MA-SFA2| SI-17M1:MA-SDA0| SI-17C1:MA-SDA1| SI-17C1:MA-SDA2| SI-17C2:MA-SDA3 |
|10| SI-17M2:MA-SFA0| SI-20C4:MA-SFA1| SI-20C3:MA-SFA2| SI-17M2:MA-SDA0| SI-20C4:MA-SDA1| SI-20C4:MA-SDA2| SI-20C3:MA-SDA3 |

**Table 37**: Storage Ring Sextupole Families A 

|| SI-Fam:MA-SFB0| SI-Fam:MA-SFB1| SI-Fam:MA-SFB2| SI-Fam:MA-SDB0| SI-Fam:MA-SDB1| SI-Fam:MA-SDB2| SI-Fam:MA-SDB3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|1| SI-02M1:MA-SFB0| SI-01C4:MA-SFB1| SI-01C3:MA-SFB2| SI-02M1:MA-SDB0| SI-01C4:MA-SDB1| SI-01C4:MA-SDB2| SI-01C3:MA-SDB3 |
|2| SI-02M2:MA-SFB0| SI-02C1:MA-SFB1| SI-02C2:MA-SFB2| SI-02M2:MA-SDB0| SI-02C1:MA-SDB1| SI-02C1:MA-SDB2| SI-02C2:MA-SDB3 |
|3| SI-04M1:MA-SFB0| SI-03C4:MA-SFB1| SI-03C3:MA-SFB2| SI-04M1:MA-SDB0| SI-03C4:MA-SDB1| SI-03C4:MA-SDB2| SI-03C3:MA-SDB3 |
|4| SI-04M2:MA-SFB0| SI-04C1:MA-SFB1| SI-04C2:MA-SFB2| SI-04M2:MA-SDB0| SI-04C1:MA-SDB1| SI-04C1:MA-SDB2| SI-04C2:MA-SDB3 |
|5| SI-06M1:MA-SFB0| SI-05C4:MA-SFB1| SI-05C3:MA-SFB2| SI-06M1:MA-SDB0| SI-05C4:MA-SDB1| SI-05C4:MA-SDB2| SI-05C3:MA-SDB3 |
|6| SI-06M2:MA-SFB0| SI-06C1:MA-SFB1| SI-06C2:MA-SFB2| SI-06M2:MA-SDB0| SI-06C1:MA-SDB1| SI-06C1:MA-SDB2| SI-06C2:MA-SDB3 |
|7| SI-08M1:MA-SFB0| SI-07C4:MA-SFB1| SI-07C3:MA-SFB2| SI-08M1:MA-SDB0| SI-07C4:MA-SDB1| SI-07C4:MA-SDB2| SI-07C3:MA-SDB3 |
|8| SI-08M2:MA-SFB0| SI-08C1:MA-SFB1| SI-08C2:MA-SFB2| SI-08M2:MA-SDB0| SI-08C1:MA-SDB1| SI-08C1:MA-SDB2| SI-08C2:MA-SDB3 |
|9| SI-10M1:MA-SFB0| SI-09C4:MA-SFB1| SI-09C3:MA-SFB2| SI-10M1:MA-SDB0| SI-09C4:MA-SDB1| SI-09C4:MA-SDB2| SI-09C3:MA-SDB3 |
|10| SI-10M2:MA-SFB0| SI-10C1:MA-SFB1| SI-10C2:MA-SFB2| SI-10M2:MA-SDB0| SI-10C1:MA-SDB1| SI-10C1:MA-SDB2| SI-10C2:MA-SDB3 |
|11| SI-12M1:MA-SFB0| SI-11C4:MA-SFB1| SI-11C3:MA-SFB2| SI-12M1:MA-SDB0| SI-11C4:MA-SDB1| SI-11C4:MA-SDB2| SI-11C3:MA-SDB3 |
|12| SI-12M2:MA-SFB0| SI-12C1:MA-SFB1| SI-12C2:MA-SFB2| SI-12M2:MA-SDB0| SI-12C1:MA-SDB1| SI-12C1:MA-SDB2| SI-12C2:MA-SDB3 |
|13| SI-14M1:MA-SFB0| SI-13C4:MA-SFB1| SI-13C3:MA-SFB2| SI-14M1:MA-SDB0| SI-13C4:MA-SDB1| SI-13C4:MA-SDB2| SI-13C3:MA-SDB3 |
|14| SI-14M2:MA-SFB0| SI-14C1:MA-SFB1| SI-14C2:MA-SFB2| SI-14M2:MA-SDB0| SI-14C1:MA-SDB1| SI-14C1:MA-SDB2| SI-14C2:MA-SDB3 |
|15| SI-16M1:MA-SFB0| SI-15C4:MA-SFB1| SI-15C3:MA-SFB2| SI-16M1:MA-SDB0| SI-15C4:MA-SDB1| SI-15C4:MA-SDB2| SI-15C3:MA-SDB3 |
|16| SI-16M2:MA-SFB0| SI-16C1:MA-SFB1| SI-16C2:MA-SFB2| SI-16M2:MA-SDB0| SI-16C1:MA-SDB1| SI-16C1:MA-SDB2| SI-16C2:MA-SDB3 |
|17| SI-18M1:MA-SFB0| SI-17C4:MA-SFB1| SI-17C3:MA-SFB2| SI-18M1:MA-SDB0| SI-17C4:MA-SDB1| SI-17C4:MA-SDB2| SI-17C3:MA-SDB3 |
|18| SI-18M2:MA-SFB0| SI-18C1:MA-SFB1| SI-18C2:MA-SFB2| SI-18M2:MA-SDB0| SI-18C1:MA-SDB1| SI-18C1:MA-SDB2| SI-18C2:MA-SDB3 |
|19| SI-20M1:MA-SFB0| SI-19C4:MA-SFB1| SI-19C3:MA-SFB2| SI-20M1:MA-SDB0| SI-19C4:MA-SDB1| SI-19C4:MA-SDB2| SI-19C3:MA-SDB3 |
|20| SI-20M2:MA-SFB0| SI-20C1:MA-SFB1| SI-20C2:MA-SFB2| SI-20M2:MA-SDB0| SI-20C1:MA-SDB1| SI-20C1:MA-SDB2| SI-20C2:MA-SDB3  |

**Table 38**: Storage Ring Sextupole Families B 

|| SI-Fam:MA-SFP0| SI-Fam:MA-SFP1| SI-Fam:MA-SFP2| SI-Fam:MA-SDP0| SI-Fam:MA-SDP1| SI-Fam:MA-SDP2| SI-Fam:MA-SDP3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|1| SI-03M1:MA-SFP0| SI-02C4:MA-SFP1| SI-02C3:MA-SFP2| SI-03M1:MA-SDP0| SI-02C4:MA-SDP1| SI-02C4:MA-SDP2| SI-02C3:MA-SDP3 |
|2| SI-03M2:MA-SFP0| SI-03C1:MA-SFP1| SI-03C2:MA-SFP2| SI-03M2:MA-SDP0| SI-03C1:MA-SDP1| SI-03C1:MA-SDP2| SI-03C2:MA-SDP3 |
|3| SI-07M1:MA-SFP0| SI-06C4:MA-SFP1| SI-06C3:MA-SFP2| SI-07M1:MA-SDP0| SI-06C4:MA-SDP1| SI-06C4:MA-SDP2| SI-06C3:MA-SDP3 |
|4| SI-07M2:MA-SFP0| SI-07C1:MA-SFP1| SI-07C2:MA-SFP2| SI-07M2:MA-SDP0| SI-07C1:MA-SDP1| SI-07C1:MA-SDP2| SI-07C2:MA-SDP3 |
|5| SI-11M1:MA-SFP0| SI-10C4:MA-SFP1| SI-10C3:MA-SFP2| SI-11M1:MA-SDP0| SI-10C4:MA-SDP1| SI-10C4:MA-SDP2| SI-10C3:MA-SDP3 |
|6| SI-11M2:MA-SFP0| SI-11C1:MA-SFP1| SI-11C2:MA-SFP2| SI-11M2:MA-SDP0| SI-11C1:MA-SDP1| SI-11C1:MA-SDP2| SI-11C2:MA-SDP3 |
|7| SI-15M1:MA-SFP0| SI-14C4:MA-SFP1| SI-14C3:MA-SFP2| SI-15M1:MA-SDP0| SI-14C4:MA-SDP1| SI-14C4:MA-SDP2| SI-14C3:MA-SDP3 |
|8| SI-15M2:MA-SFP0| SI-15C1:MA-SFP1| SI-15C2:MA-SFP2| SI-15M2:MA-SDP0| SI-15C1:MA-SDP1| SI-15C1:MA-SDP2| SI-15C2:MA-SDP3 |
|9| SI-19M1:MA-SFP0| SI-18C4:MA-SFP1| SI-18C3:MA-SFP2| SI-19M1:MA-SDP0| SI-18C4:MA-SDP1| SI-18C4:MA-SDP2| SI-18C3:MA-SDP3 |
|10| SI-19M2:MA-SFP0| SI-19C1:MA-SFP1| SI-19C2:MA-SFP2| SI-19M2:MA-SDP0| SI-19C1:MA-SDP1| SI-19C1:MA-SDP2| SI-19C2:MA-SDP3 |

**Table 39**: Storage Ring Sextupole Families P

<br />

## Booster Magnets

### Booster Dipoles

There is only one type of dipole in the Booster. It is a multi-functional magnet with dipolar, defocusing quadrular and sextupolar functions.

<br />

#### BO Dipole Magnet Specifications

##### Main Parameters

| | BD| units |
| --- | --- | --- |
|Power supply type| monopolar¹|  |
|Number of magnets| 50|  |
|Deflection angle| 7.2| Â° |
|Magnetic length| 1.221| m |
|Physical length| 1.206| m |
|Integrated quadrupole strength²| -0.2477| m⁻¹ |
|Integrated sextupole strength²| -2.5610| m⁻² |
|Full central gap| 28.0| mm |
|Hardedge bending radius| 9.7164| m |
|Hardedge quadrupole strength| -0.2029| m⁻² |
|Hardedge sextupole strength| -2.0975| m⁻³ |
|Hardedge sagitta²| 18.836| mm |
|Good field region (GFR)| 6| mm |
|Homogeneity in GFR| 4/10000|  |
|Maximum integrated field³| -1.3204| TÂ·m  |

| | Injection| Extraction|  |
| --- | --- | --- | --- |
|Integrated field²| -0.0629| -1.2575| TÂ·m |
|Integrated quadrupole gradient²| 0.1239| 2.4788| T |
|Integrated sextupole gradient²| 1.2814| 25.6277| TÂ·m⁻¹ |
|Hardedge field| -0.0515| -1.0299| T |
|Hardedge quadrupole gradient| 0.1015| 2.0302| TÂ·m⁻¹ |
|Hardedge sextupole gradient| 1.0495| 20.9891| TÂ·m⁻² |

¹ Two monopolar power supplies will be used, each exciting alternate north and south pole coils of consecutive dipoles.

² On the Runge-Kutta trajectory.

³ The maximum integrated field is 5% higher than the integrated field at extraction energy. This is required by the adopted ramping curve. 

**Table 40**: Booster dipole main parameters 

<br />

##### Electric Parameters

|  | BD| units |
| --- | --- | --- |
|Main coil current| 1034.00| A |
|Main coil number of turns| 12|  |
|Stored magnetic energy| 2450.92| J |
|Magnet inductance| 4.58| mH |

**Table 41**: Booster dipole electric parameters 

<br />

##### Multipole Errors

Field analysis of the 3D model of the dipole shows very small residual multipoles. The larger systematic multipole values in Table 42, which do not compromise beam quality, are kept as specifications for measurements of the magnets in the future. Random multipole errors were chosen so that the rms multipolar contribution at r0 = 17.5 mm were 1/1000 of the nominal dipolar field. This contribution was then equally divided amoung the multipoles considered. On the other hand, normal sextupolar random 1σ value was set to 9 % of the maximum strength. All these values should be used as targets for the magnet modelling and measurements. Eventually the multipole values will be updated with measurement data and tested against beam dynamics simulations.

Dipoles @r = 17.5 mm

| Multipole error| Systematic| Random Normal | Random Skew |
| --- | --- | --- | --- |
|B2/B0 (sextupole)| --| 5.5×10⁻⁴ *| 1.0×10⁻⁴ |
|B3/B0 (octupole)| +4.0×10⁻⁴| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B4/B0 (decapole)| -3.6×10⁻⁴| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B5/B0 (12-pole)| +2.7×10⁻⁴| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B6/B0 (14-pole)| -1.3×10⁻⁴| 4.0×10⁻⁴| 1.0×10⁻⁴ |

**Table 42**: Booster dipole multipole errors specification. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

*This spec is replicated in the dipole alignment and rotation errors table

Actual designed dipole model shows numbers are that in accordance with these specs. (see [fieldmap analysis][link])

<br />

##### Alignment and Excitation Errors

|  | Dipoles|  |
| --- | --- | --- |
|Transverse position, ,| 160| Î¼m |
|Rotation around longitudinal axis| 0.8| mrad |
|Excitation error (static or low frequency)| 0.15|  % |
|Dipole Gradient Error| 2.4|  % |
|Dipole Sextupolar Error| 9|  %  |

**Table 43**: Maximum absolute value of random alignment and excitation errors for the Booster Dipoles. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### BO Dipole Magnet 3D Model

![](/img/machine/magnets/BO_magnet_dipole_drawing.png)

**Figure 49**: 3D drawing of the booster dipole model.

![](/img/machine/magnets/BO_magnet_dipole_field.png)

**Figure 50**: Field of the booster dipole model.

<br />

##### Fieldmap Analysis

Each dipole in the booster deflects the beam in 7.2 Â° nominally. A 3D magnetic model has been created and its [fieldmap analyzed][link] for a excitation current corresponding to 3.0 GeV. The model has been optimized in a way that the beam trajectory is roughly centered at the good-field region of the magnet, corresponding to the axis x = 0 mm. At the longitudinal center of the magnet the trajectory starts at x = 9.045 mm. The reference point, defined as the interception of the straight lines asymptotically tangent to the up and downstream trajectory branches, is located at x = 28.572 mm, at the longitudinal center of the magnet. Multipoles from fieldmap analysis are all very well within specifications. A summary of the analysis for extraction energy can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-dipoles/tree/master/links-official-3gev). As for low energy, the corresponding file can be found in [here](https://github.com/lnls-ima/bo-dipoles/tree/master/links-official-150mev). 

<br />

##### Segmented Model

In order to take into account the s-dependent field profile of the BO dipoles a symmetric model was created.

![](/img/machine/magnets/segmented_model_BD_Booster.svg)

**Figure 51**: Booster dipole By field on the trajectory calculated by Runge-Kutta integration and the adopted segmented model used in simulation codes. Only half dipole is shown in longitudinal direction. The slight variation in the flat region is caused by the curved trajectory in a straight magnet with transverse field gradient.

Table with segmented dipole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1960| 1.158| -1.032| -0.228| -1.990 |
|02| 0.1920| 1.143| -1.040| -0.212| -1.930 |
|03| 0.1820| 1.096| -1.052| -0.186| -1.920 |
|04| 0.0100| 0.051| -0.889| -0.249| -2.030 |
|05| 0.0100| 0.037| -0.641| -0.170| -1.470 |
|06| 0.0130| 0.033| -0.440| -0.062| -1.820 |
|07| 0.0170| 0.029| -0.299| -0.011| -1.970 |
|08| 0.0200| 0.022| -0.195| +0.005| -1.600 |
|09| 0.0300| 0.018| -0.107| +0.005| -0.930 |
|10| 0.0500| 0.012| -0.043| +0.002| -0.361 |

**Table 44**: Booster dipole segmented model.

<br />

#### BO Dipole Magnet Measurements

The magnetic measurement results for Booster dipoles at the extraction current, I= 991.63 A, are shown in Figure 52 , Figure 53 and Figure 54. The Hall probe measurement files can be found at [this folder](https://github.com/lnls-ima/bo-dipoles/tree/master/model-09/measurement/magnetic/hallprobe/production). The excitation curve measurement files can be found at [this folder](https://github.com/lnls-ima/bo-dipoles/tree/master/model-09/measurement/magnetic/hallprobe/excitation_curve).

![](/img/machine/magnets/BOMA_BD_int_field_992A.png)

**Figure 52**: Integrated field on the Runge-Kutta trajectory, calculated for the Hall probe measurements of the Booster dipoles at the extraction current (991.63 A).

![](/img/machine/magnets/BOMA_BD_int_quad_992A.png)

**Figure 53**: Integrated quadrupole gradient on the Runge-Kutta trajectory, calculated for the Hall probe measurements of the Booster dipoles at the extraction current (991.63 A).

![](/img/machine/magnets/BOMA_BD_int_sext_992A.png)

**Figure 54**: Integrated sextupole gradient on the Runge-Kutta trajectory, calculated for the Hall probe measurements of the Booster dipoles at the extraction current (991.63 A).

<br />

### Booster Quadrupoles

#### BO Quadrupole Magnets Specifications

##### Main Parameters

|| QF| QD| QS| units |
| --- | --- | --- | --- | --- |
|Power supply type| monopolar| bipolar| bipolar|  |
|Magnet model name| BQF| BQD| BQS|  |
|Number of magnets| 50| 25| 1|  |
|Maximum integrated strength ¹| 0.425| -0.052| 0.017| m⁻¹ |
|Magnetic length| 0.228| 0.100| 0.100| m |
|Physical length| 0.212| 0.085| 0.100| m |
|Maximum strength ¹| 1.865| -0.525| 0.168| m⁻² |
|Bore diameter| 40| 40| 40| mm |
|Maximum integrated field gradient ¹| -4.255| 0.525| 0.168| T |
|Maximum field gradient ¹| -18.664| 5.254| 1.600| TÂ·m⁻¹ |
|Maximum field at pole tip ¹| 0.373| 0.105| 0.032| T |

¹ The maximum field gradient is 5% higher than the field gradient at extraction energy. This is required by the adopted ramping curve. 

**Table 45**: Booster quadrupole main parameters 

<br />

##### Electric Parameters

|| QF| QD| QS| units |
| --- | --- | --- | --- | --- |
|Main coil current| 113.97| 30.42| 9.64| A |
|Main coil number of turns| 26.25| 27.50| 28.00|  |
|Stored magnetic energy| 59.34| 2.42| 0.22| J |
|Magnet inductance| 9.14| 5.22| 4.68| mH |

**Table 46**: Booster quadrupole electric parameters 

<br />

##### Multipole Errors

**Quadrupole QF**

quadrupoles @r = 17.5 mm

| Multipole error| Systematic¹| Random Normal| Random Skew |
| --- | --- | --- | --- |
| B2/B1 (sextupole)| --| 7.0×10⁻⁴| 1.0×10⁻³ |
|B3/B1 (octupole)| --| 4.0×10⁻⁴| 5.0×10⁻⁴ |
|B4/B1 (decapole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B5/B1 (12-pole)| -1.0×10⁻³| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B6/B1 (14-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B7/B1 (16-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B8/B1 (18-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B9/B1 (20-pole)| +1.1×10⁻³| --| -- |
|B13/B1 (28-pole)| +8.0×10⁻⁵| --| -- |

¹ Multipoles of prototype magnets measured with radial rotating coils 

**Table 47**: Booster QF quadrupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

**Quadrupole QD**

quadrupoles @r = 17.5 mm

| Multipole error| Systematic¹| Random Normal | Random Skew |
| --- | --- | --- | --- |
| B2/B1 (sextupole)| --| 7.0×10⁻⁴| 1.0×10⁻³ |
|B3/B1 (octupole)| --| 4.0×10⁻⁴| 5.0×10⁻⁴ |
|B4/B1 (decapole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B5/B1 (12-pole)| -4.7×10⁻³| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B6/B1 (14-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B7/B1 (16-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B8/B1 (18-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B9/B1 (20-pole)| +1.2×10⁻³| --| -- |
|B13/B1 (28-pole)| +5.4×10-7| --| -- |

¹ Relative multipoles calculated around the Runge-Kutta trajectory for the latest QD model-02 fieldmap at 3 GeV 

**Table 48**: Booster QD quadrupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

**Quadrupole QS**

quadrupoles @r = 17.5 mm

| Multipole error| Systematic¹| Random Normal | Random Skew |
| --- | --- | --- | --- |
|A3/A1 (octupole)| -1.1×10⁻³| --| -- |
|A5/A1 (12-pole)| +9.9×10⁻³| --| -- |
|A7/A1 (16-pole)| -8.7×10⁻³| --| -- |
|A9/A1 (20-pole)| +6.4×10⁻³| --| -- |

¹ Relative multipoles calculated around the Runge-Kutta trajectory for the latest QS model-01, fieldmap at 3 GeV 

**Table 49**: Booster QS quadrupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

<br />

##### Alignment and Excitation Errors

|| Quadrupoles|  |
| --- | --- | --- |
|Transverse position, x, y| 160| Î¼m |
|Rotation around longitudinal axis| 0.8| mrad |
|Excitation error (static or low frequency)| 0.3|  % |
|Tracking error| 100| ppm |

**Table 50**: Maximum absolute value of random alignment and excitation errors for the Booster Quadrupoles. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### BO Quadrupole 3D Models

![](/img/machine/magnets/BO_magnet_quadrupole_drawing.png)

**Figure 55**: 3D drawing of the QF booster quadrupole model.

![](/img/machine/magnets/BO_magnet_quadrupole_field.png)

**Figure 56**: Field of the booster QF quadrupole model.

![](/img/machine/magnets/BO_magnet_quadrupole_QD_drawing.png)

**Figure 57**: 3D drawing of the QD booster quadrupole model.

![](/img/machine/magnets/BO_magnet_quadrupole_QD_field.png)

**Figure 58**: Field of the booster QD quadrupole model.

![](/img/machine/magnets/BO_magnet_quadrupole_QS_drawing.png)

**Figure 59**: 3D drawing of the QS booster quadrupole model.

![](/img/machine/magnets/BO_magnet_quadrupole_QS_field.png)

**Figure 60**: Field of the booster QS quadrupole model.

<br />

##### Fieldmap Analysis

There will be two types of quadrupoles: QF and QD. QF quadrupoles are longer, 212-mm, whereas QD quadrupoles are shorter: 85-mm long. While QF magnets power supply is planed to be monopolar, the power supply for the QD family will be dipolar. 3D magnetic models for both QD and QF quadrupoles were analyzed. Nominal quadrupole field component in the booster dipoles provide most necessary defocusing for the optics and hence QD quadrupoles are installed in the lattice for optics correction purposes.

**QF at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qf/tree/master/links-official-3gev).

**QF at Injection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qf/tree/master/links-official-150mev).

**QD at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qd/tree/master/links-official-3gev).

**QD at Injection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qd/tree/master/links-official-150mev).

**QS at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qs/tree/master/links-official-3gev). 

<br />

##### Segmented Model

Currently booster quadrupoles are being modelled as a single segment within the hard-edge approximation.

![](/img/machine/magnets/segmented_model_QF.svg)

**Figure 61**: Booster QF quadrupole strength on the trajectory calculated by Runge-Kutta integration and the adopted hard-edge model used in simulation codes. Only half quadrupole is shown in longitudinal direction.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1140| 0.000| -0.000e+00| +1.870e+00| +0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 51**: BO QF quadrupole segmented model (maximum current). 

![](/img/machine/magnets/segmented_model_QD.svg)

**Figure 62**: Booster QD quadrupole strength on the trajectory calculated by Runge-Kutta integration and the adopted hard-edge model used in simulation codes. Only half quadrupole is shown in longitudinal direction.    

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0500| 0.000| -0.000e+00| -5.000e-01| -0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 52**: BO QD quadrupole segmented model (maximum current). 

![](/img/machine/magnets/segmented_model_QS.svg)

**Figure 63**: Booster QS quadrupole strength on the trajectory calculated by Runge-Kutta integration and the adopted hard-edge model used in simulation codes. Only half quadrupole is shown in longitudinal direction.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0500| 0.000| -0.000e+00| -1.680e-01| -0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 53**: BO QS quadrupole segmented model (maximum current). 

<br />

#### BO Quadrupole Magnet Measurements

The magnetic measurement results for Booster QF quadrupoles at high current, I=130 A, are shown in Figure 64 and Figure 65. The rotating coil measurement files can be found at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qf/tree/master/model-06/measurement/magnetic/rotcoil).

![](/img/machine/magnets/BOMA_BQF_align_130A.png)

**Figure 64**: Rotating coil measurements of the Booster QF quadrupoles at high current (130 A).

![](/img/machine/magnets/BOMA_BQF_excit_130A.png)

**Figure 65**: Rotating coil measurements of the Booster QF quadrupoles at high current (130 A).

The magnetic measurement results for Booster QD quadrupoles at high current, I=32 A, are shown in Figure 66 and Figure 67. The rotating coil measurement files can be found at [this folder](https://github.com/lnls-ima/bo-quadrupoles-qd/tree/master/model-02/measurement/magnetic/rotcoil).

![](/img/machine/magnets/BOMA_BQD_align_32A.png)

**Figure 66**: Rotating coil measurements of the Booster QD quadrupoles at high current (32 A).

![](/img/machine/magnets/BOMA_BQD_excit_32A.png)

**Figure 67**: Rotating coil measurements of the Booster QD quadrupoles at high current (32 A).

<br />

### Booster Sextupoles

#### BO Sextupole Magnet Specifications

##### Main Parameters

|  | SF| SD| units |
| --- | --- | --- | --- |
|Power supply type| monopolar| bipolar|  |
|Number of magnets| 25| 10|  |
|Maximum integrated strength ¹| 2.1| 2.1| m⁻² |
|Magnetic length| 0.105| 0.105| m |
|Physical length| 0.100| 0.100| m |
|Maximum strength ¹| 20.0| 20.0| m⁻³ |
|Bore diameter| 40| 40| mm |
|Maximum integrated field gradient ¹| 21.015| 21.015| TÂ·m⁻¹ |
|Maximum gradient ¹| 200.1| 200.1| TÂ·m⁻² |
|Maximum field at pole tip ¹| 0.080| 0.080| T |

¹ The maximum field gradient is 5% higher than the field gradient at extraction energy. This is required by the adopted ramping curve. 

**Table 54**: Booster sextupole main parameters 

<br />

##### Electric Parameters

| | BS| units |
| --- | --- | --- |
|Main coil current| 142.00| A |
|Main coil number of turns| 3.00|  |
|Stored magnetic energy| 0.98| J |
|Magnet inductance| 0.10| mH |

**Table 55**: Booster sextupole electric parameters

<br />

##### Multipole Errors

sextupoles @x = 17.5 mm

Multipole error| Systematic¹| Random Normal | Random Skew |
| --- | --- | --- | --- |
|B3/B2 (octupole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B4/B2 (decapole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B5/B2 (12-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B6/B2 (14-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B7/B2 (16-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B8/B2 (18-pole)| -2.7×10⁻²| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B9/B2 (20-pole)| --| 4.0×10⁻⁴| 1.0×10⁻⁴ |
|B14/B2 (30-pole)| -1.4×10⁻²| --| -- |

¹ Relative multipoles calculated around the Runge-Kutta trajectory for the latest sextupole model-03 fieldmap at 3 GeV 

**Table 56**: Booster sextupole multipole errors. Standard deviation for random multipole errors; simulations assume Gaussian distribution truncated at ±2σ. 

<br />

##### Alignment and Excitation Errors

|  | Sextupoles|  |
| --- | --- | --- |
|Transverse position, x, y| 160| Î¼m |
|Rotation around longitudinal axis| 0.8| mrad |
|Excitation error (static or low frequency)| 0.3|  %  |

**Table 57**: Maximum absolute value of random alignment and excitation errors for the Booster Sextupoles. The errors are generated with a Gaussian distribution truncated at ±1σ. 

<br />

#### BO Sextupole 3D Model

![](/img/machine/magnets/BO_magnet_sextupole_drawing.png)

**Figure 68**: 3D drawing of the booster sextupole model.

![](/img/machine/magnets/BO_magnet_sextupole_field.png)

**Figure 69**: Field of the booster sextupole model.

<br />

##### Fieldmap Analysis

There will be 25 focusing sextupoles (SF) and 10 defocusing sextupoles (SD) in the booster for chromaticity control. A 105-mm long 3D magnetic model for both SF and SD sextupoles was analyzed. SF family of magnets will be excited with a monopolar power supply whereas SD sextupoles family will be excited with a bipolar power supply. Analysis has been done for fieldmaps corresponding to injection and extraction energy currents. Since the magnetic field is very linear with the excitation current the two results are virtually identical with respect to field quality.

**SD/SF at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-sextupoles/tree/master/links-official-3gev).

**SD/SF at Injection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-sextupoles/tree/master/links-official-150mev). 

<br />

##### Segmented Model

Currently booster sextupoles are being modelled as a single segment within the hard-edge approximation. 

![](/img/machine/magnets/segmented_model_BO_S.svg)

**Figure 70**: Booster sextupole strength on the trajectory calculated by Runge-Kutta integration and the adopted hard-edge model used in simulation codes. Only half sextupole is shown in longitudinal direction.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0525| 0.000| -0.000e+00| +0.000e+00| +1.900e+01 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 58**: BO S sextupole segmented model (maximum current). 

<br />

#### BO Sextupole Magnet Measurements

The magnetic measurement results for Booster sextupoles at high current, I=150 A, are shown in Figure 71 and Figure 72. The rotating coil measurement files can be found at [this folder](https://github.com/lnls-ima/bo-sextupoles/tree/master/model-03/measurement/magnetic/rotcoil).

![](/img/machine/magnets/BOMA_BS_align_150A.png)

**Figure 71**: Rotating coil measurements of the Booster sextupoles at high current (150 A).

![](/img/machine/magnets/BOMA_BS_excit_150A.png)

**Figure 72**: Rotating coil measurements of the Booster sextupoles at high current (150 A).

<br />

### Booster Correctors

#### BO Corrector Magnets Specifications

##### Main parameters

|| CH| CV| units |
| --- | --- | --- | --- |
|Power supply type| bipolar| bipolar|  |
|Number of magnets| 25| 25|  |
|Maximum kick angle @ 3 GeV| 310| 310| Î¼rad |
|Magnetic length| 0.150| 0.150| m |
|Physical length| 0.112| 0.112| m |
|Central Gap| 43.0| 43.0| mm |
|Minimum Gap| 40.0| 40.0| mm |
|Maximum integrated field| 3.10×10⁻³| 3.10×10⁻³| TÂ·m |
|Maximum field| 2.07×10⁻²| 2.07×10⁻²| T  |

**Table 59**: Booster corrector main parameters 

<br />

##### Electric parameters

|| CH/CV| units |
| --- | --- | --- |
|Maximum main coil current| 9.35| A |
|Main coil number of turns| 38.50|  |
|Stored magnetic energy| 0.15| J |
|Magnet inductance| 3.37| mH |

**Table 60**: Booster corrector electric parameters 

<br />

##### Multipole Errors

The impact of residual multipole errors of reasonable correctors on the booster beam parameters is expected to be negligible and therefore no specification had been defined. The designed 3D model of these correctors showed acceptable multipole erros.

<br />

#### BO Corrector 3D Model

Orbit correctors for the booster use a single model for both horizontal and vertical deflections.

![](/img/machine/magnets/BO_magnet_corrector_drawing.png)

**Figure 73**: 3D drawing of the booster orbit correctors model.

![](/img/machine/magnets/BO_magnet_corrector_field.png)

**Figure 74**: Field of the booster orbit correctors model.

<br />

##### Fieldmap Analysis

There will be 25 horizontal and 25 vertical orbit correctors in the booster for orbit control. There will be one magnet model for both corrector types. Vertical corrector magnets are the same as horizontal correctors rotated by 90 degrees. The following are the [analysis][link]summaries created with [fma-analysis.py](https://github.com/lnls-fac/fieldmaptrack/blob/master/scripts/fma-analysis.py)

**CH at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-correctors/tree/master/links-official-ch-3gev).

**CV at Ejection Energy**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/bo-correctors/tree/master/links-official-cv-3gev). 

<br />

##### Segmented Model

Currently the hard-edge approximation is being used to model all booster correctors.

![](/img/machine/magnets/segmented_model_Corretora_Horizontal-Vertical_Booster.svg)

**Figure 75**:  Field profile of segmented booster correctors model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0750| 0.000| -2.121e-02| +3.400e-06| +1.940e-02 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 61**: BO correctors half segmented model (maximum strength). 

<br />

#### BO Corrector Magnet Measurements

The magnetic measurement results for Booster corrector at I=10 A are shown in Figure 76. The rotating coil measurement files can be found at [this folder](https://github.com/lnls-ima/bo-correctors/tree/master/model-02/measurement/magnetic/rotcoil).

![](/img/machine/magnets/BOMA_BC_excit_10A.png)

**Figure 76**: Rotating coil measurements of the Booster correctors at I=10 A.

<br />

### Booster Magnets Ramping Curve

For beam energy ramping in the Booster from 0.15 GeV to 3.0 GeV, the booster main magnetic elements will follow cycling curves with main parameters defined in Table 62. The cycling waveform shape will be a rounded triangle with rise time longer than fall time, as shown in Figure 77, a scaled universal curve where the extraction current at 3.0 GeV is set to 1 A. The maximum current is 5% higher than the extraction current. 

| Parameter | Value | Unit |
| --- | --- | --- |
|Cycling frequency| 2| Hz |
|Cycling period| 500| ms |
|Number of points per cycle| 2048|  |
|Uniform time interval between points| 244| μs |

**Table 62**: Booster magnets ramping curve parameters. 

![](/img/machine/magnets/BO_ramping_curve.png)

**Figure 77**: Scaled ramping curve for Booster magnets with extraction current set to 1 A. The top graph shows the current vs time where the maximum current is 5% higher than the current at extraction energy. The curve is defined by the points (+) with either linear or cubic interpolations between them. The bottom graph shows the time derivative of the current.

<br />

### Booster Magnets Installation

|Sector| Girder| Magnets| BS| BQF| BQS| BQD| BD| BC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|B01| LS-CENTRAL-003-UNI-0029| CORR-QUAD| --| BQF-042| --| --| --| BC-022 |
|LS-DIPOLO-002-UNI-0011| DIP| --| --| --| --| BD-010| -- |
|B02| LS-BSKEW-001-UNI-0001| SEXT-QUAD-QSKEW| BS-007| BQF-007| BQS-001| --| --| -- |
|LS-DIPOLO-002-UNI-0018| QUAD-DIP-SEXT| BS-035| --| --| BQD-002| BD-037| -- |
|B03| LS-BCH-001-UNI-0003| CORR| --| --| --| --| --| BC-027 |
|LS-CENTRAL-003-UNI-0022| CORR-QUAD| --| BQF-045| --| --| --| BC-021 |
|LS-DIPOLO-003-UNI-0022| DIP| --| --| --| --| BD-050| -- |
|B04| LS-CENTRAL-002-UNI-0016| SEXT-QUAD| BS-013| BQF-051| --| --| --| -- |
|LS-DIPOLO-003-UNI-0023| QUAD-DIP-CORR| --| --| --| BQD-007| BD-047| BC-062 |
|B05| LS-CENTRAL-006-UNI-0051| CORR-QUAD| --| BQF-043| --| --| --| BC-020 |
|LS-DIPOLO-004-UNI-0040| DIP| --| --| --| --| BD-044| -- |
|B06| LS-CENTRAL-002-UNI-0011| SEXT-QUAD| BS-014| BQF-024| --| --| --| -- |
|LS-DIPOLO-002-UNI-0012| QUAD-DIP-CORR| --| --| --| BQD-018| BD-008| BC-015 |
|B07| LS-CENTRAL-003-UNI-0027| CORR-QUAD| --| BQF-015| --| --| --| BC-037 |
|LS-DIPOLO-001-UNI-0003| DIP-SEXT| BS-034| --| --| --| BD-024| -- |
|B08| LS-CENTRAL-001-UNI-0001| SEXT-QUAD| BS-017| BQF-049| --| --| --| -- |
|LS-DIPOLO-003-UNI-0024| QUAD-DIP-CORR| --| --| --| BQD-017| BD-043| BC-060 |
|B09| LS-CENTRAL-005-UNI-0050| CORR-QUAD| --| BQF-016| --| --| --| BC-036 |
|LS-DIPOLO-004-UNI-0038| DIP| --| --| --| --| BD-026| -- |
|B10| LS-CENTRAL-002-UNI-0014| SEXT-QUAD| BS-016| BQF-034| --| --| --| -- |
|LS-DIPOLO-005-UNI-0041| QUAD-DIP-CORR| --| --| --| BQD-004| BD-027| BC-025 |
|B11| LS-CENTRAL-001-UNI-0005| CORR-QUAD| --| BQF-023| --| --| --| BC-040 |
|LS-DIPOLO-002-UNI-0020| DIP| --| --| --| --| BD-004| -- |
|B12| LS-CENTRAL-002-UNI-0015| SEXT-QUAD| BS-019| BQF-033| --| --| --| -- |
|LS-DIPOLO-001-UNI-0009| QUAD-DIP-SEXT| BS-039| --| --| BQD-006| BD-057| -- |
|B13| LS-BCH-001-UNI-0005| CORR| --| --| --| --| --| BC-024 |
|LS-CENTRAL-003-UNI-0024| CORR-QUAD| --| BQF-035| --| --| --| BC-035 |
|LS-DIPOLO-005-UNI-0050| DIP| --| --| --| --| BD-017| -- |
|B14| LS-CENTRAL-002-UNI-0017| SEXT-QUAD| BS-018| BQF-047| --| --| --| -- |
|LS-DIPOLO-001-UNI-0005| QUAD-DIP-CORR| --| --| --| BQD-024| BD-009| BC-047 |
|B15| LS-CENTRAL-005-UNI-0041| CORR-QUAD| --| BQF-037| --| --| --| BC-034 |
|LS-DIPOLO-003-UNI-0026| DIP| --| --| --| --| BD-028| -- |
|B16| LS-CENTRAL-002-UNI-0018| SEXT-QUAD| BS-020| BQF-053| --| --| --| -- |
|LS-DIPOLO-005-UNI-0043| QUAD-DIP-CORR| --| --| --| BQD-021| BD-041| BC-041 |
|B17| LS-CENTRAL-006-UNI-0052| CORR-QUAD| --| BQF-041| --| --| --| BC-033 |
|LS-DIPOLO-003-UNI-0027| DIP-SEXT| BS-043| --| --| --| BD-025| -- |
|B18| LS-CENTRAL-002-UNI-0013| SEXT-QUAD| BS-021| BQF-052| --| --| --| -- |
|LS-DIPOLO-003-UNI-0025| QUAD-DIP-CORR| --| --| --| BQD-016| BD-013| BC-044 |
|B19| LS-CENTRAL-004-UNI-0035| CORR-QUAD| --| BQF-011| --| --| --| BC-039 |
|LS-DIPOLO-001-UNI-0004| DIP| --| --| --| --| BD-031| -- |
|B20| LS-CENTRAL-001-UNI-0007| SEXT-QUAD| BS-022| BQF-032| --| --| --| -- |
|LS-DIPOLO-001-UNI-0008| QUAD-DIP-CORR| --| --| --| BQD-027| BD-054| BC-026 |
|B21| LS-CENTRAL-004-UNI-0031| CORR-QUAD| --| BQF-048| --| --| --| BC-013 |
|LS-DIPOLO-006-UNI-0051| DIP| --| --| --| --| BD-021| -- |
|B22| LS-CENTRAL-004-UNI-0034| SEXT-QUAD| BS-025| BQF-030| --| --| --| -- |
|LS-DIPOLO-002-UNI-0016| QUAD-DIP-SEXT| BS-037| --| --| BQD-014| BD-030| -- |
|B23| LS-BCH-001-UNI-0001| CORR| --| --| --| --| --| BC-019 |
|LS-CENTRAL-005-UNI-0045| CORR-QUAD| --| BQF-009| --| --| --| BC-010 |
|LS-DIPOLO-005-UNI-0045| DIP| --| --| --| --| BD-035| -- |
|B24| LS-CENTRAL-001-UNI-0003| SEXT-QUAD| BS-026| BQF-050| --| --| --| -- |
|LS-DIPOLO-004-UNI-0031| QUAD-DIP-CORR| --| --| --| BQD-012| BD-032| BC-059 |
|B25| LS-CENTRAL-002-UNI-0020| CORR-QUAD| --| BQF-025| --| --| --| BC-016 |
|LS-DIPOLO-005-UNI-0042| DIP| --| --| --| --| BD-007| -- |
|B26| LS-CENTRAL-001-UNI-0002| SEXT-QUAD| BS-029| BQF-040| --| --| --| -- |
|LS-DIPOLO-004-UNI-0035| QUAD-DIP-CORR| --| --| --| BQD-015| BD-018| BC-011 |
|B27| LS-CENTRAL-004-UNI-0040| CORR-QUAD| --| BQF-036| --| --| --| BC-009 |
|LS-DIPOLO-002-UNI-0013| DIP-SEXT| BS-042| --| --| --| BD-029| -- |
|B28| LS-CENTRAL-003-UNI-0028| SEXT-QUAD| BS-031| BQF-038| --| --| --| -- |
|LS-DIPOLO-003-UNI-0028| QUAD-DIP-CORR| --| --| --| BQD-026| BD-034| BC-029 |
|B29| LS-CENTRAL-005-UNI-0047| CORR-QUAD| --| BQF-056| --| --| --| BC-012 |
|LS-DIPOLO-006-UNI-0052| DIP| --| --| --| --| BD-014| -- |
|B30| LS-CENTRAL-001-UNI-0006| SEXT-QUAD| BS-023| BQF-031| --| --| --| -- |
|LS-DIPOLO-004-UNI-0032| QUAD-DIP-CORR| --| --| --| BQD-005| BD-052| BC-058 |
|B31| LS-CENTRAL-005-UNI-0042| CORR-QUAD| --| BQF-055| --| --| --| BC-053 |
|LS-DIPOLO-002-UNI-0019| DIP| --| --| --| --| BD-053| -- |
|B32| LS-CENTRAL-004-UNI-0038| SEXT-QUAD| BS-027| BQF-054| --| --| --| -- |
|LS-DIPOLO-001-UNI-0010| QUAD-DIP-SEXT| BS-036| --| --| BQD-009| BD-055| -- |
|B33| LS-BCH-001-UNI-0002| CORR| --| --| --| --| --| BC-018 |
|LS-CENTRAL-003-UNI-0021| CORR-QUAD| --| BQF-029| --| --| --| BC-054 |
|LS-DIPOLO-005-UNI-0047| DIP| --| --| --| --| BD-036| -- |
|B34| LS-CENTRAL-001-UNI-0009| SEXT-QUAD| BS-024| BQF-019| --| --| --| -- |
|LS-DIPOLO-003-UNI-0029| QUAD-DIP-CORR| --| --| --| BQD-011| BD-045| BC-014 |
|B35| LS-CENTRAL-003-UNI-0026| CORR-QUAD| --| BQF-028| --| --| --| BC-055 |
|LS-DIPOLO-001-UNI-0002| DIP| --| --| --| --| BD-046| -- |
|B36| LS-CENTRAL-002-UNI-0012| SEXT-QUAD| BS-015| BQF-020| --| --| --| -- |
|LS-DIPOLO-001-UNI-0006| QUAD-DIP-CORR| --| --| --| BQD-019| BD-022| BC-038 |
|B37| LS-CENTRAL-003-UNI-0023| CORR-QUAD| --| BQF-027| --| --| --| BC-049 |
|LS-DIPOLO-005-UNI-0048| DIP-SEXT| BS-040| --| --| --| BD-038| -- |
|B38| LS-CENTRAL-001-UNI-0010| SEXT-QUAD| BS-033| BQF-012| --| --| --| -- |
|LS-DIPOLO-005-UNI-0049| QUAD-DIP-CORR| --| --| --| BQD-022| BD-039| BC-048 |
|B39| LS-CENTRAL-004-UNI-0037| CORR-QUAD| --| BQF-046| --| --| --| BC-050 |
|LS-DIPOLO-004-UNI-0034| DIP| --| --| --| --| BD-042| -- |
|B40| LS-CENTRAL-005-UNI-0049| SEXT-QUAD| BS-030| BQF-022| --| --| --| -- |
|LS-DIPOLO-002-UNI-0015| QUAD-DIP-CORR| --| --| --| BQD-001| BD-016| BC-043 |
|B41| LS-CENTRAL-003-UNI-0030| CORR-QUAD| --| BQF-057| --| --| --| BC-051 |
|LS-DIPOLO-004-UNI-0036| DIP| --| --| --| --| BD-040| -- |
|B42| LS-CENTRAL-005-UNI-0044| SEXT-QUAD| BS-028| BQF-058| --| --| --| -- |
|LS-DIPOLO-002-UNI-0017| QUAD-DIP-SEXT| BS-041| --| --| BQD-023| BD-049| -- |
|B43| LS-BCH-001-UNI-0004| CORR| --| --| --| --| --| BC-028 |
|LS-CENTRAL-005-UNI-0043| CORR-QUAD| --| BQF-044| --| --| --| BC-056 |
|LS-DIPOLO-003-UNI-0030| DIP| --| --| --| --| BD-005| -- |
|B44| LS-CENTRAL-004-UNI-0033| SEXT-QUAD| BS-008| BQF-039| --| --| --| -- |
|LS-DIPOLO-004-UNI-0037| QUAD-DIP-CORR| --| --| --| BQD-010| BD-048| BC-057 |
|B45| LS-CENTRAL-005-UNI-0046| CORR-QUAD| --| BQF-018| --| --| --| BC-052 |
|LS-DIPOLO-001-UNI-0007| DIP| --| --| --| --| BD-023| -- |
|B46| LS-CENTRAL-003-UNI-0025| SEXT-QUAD| BS-010| BQF-014| --| --| --| -- |
|LS-DIPOLO-004-UNI-0039| QUAD-DIP-CORR| --| --| --| BQD-013| BD-051| BC-046 |
|B47| LS-CENTRAL-001-UNI-0008| CORR-QUAD| --| BQF-021| --| --| --| BC-017 |
|LS-DIPOLO-003-UNI-0021| DIP-SEXT| BS-038| --| --| --| BD-033| -- |
|B48| LS-CENTRAL-004-UNI-0032| SEXT-QUAD| BS-012| BQF-017| --| --| --| -- |
|LS-DIPOLO-005-UNI-0044| QUAD-DIP-CORR| --| --| --| BQD-003| BD-019| BC-045 |
|B49| LS-CENTRAL-002-UNI-0019| CORR-QUAD| --| BQF-026| --| --| --| BC-023 |
|LS-DIPOLO-005-UNI-0046| DIP| --| --| --| --| BD-011| -- |
|B50| LS-CENTRAL-004-UNI-0039| SEXT-QUAD| BS-032| BQF-013| --| --| --| -- |
|LS-DIPOLO-002-UNI-0014| QUAD-DIP-CORR| --| --| --| BQD-008| BD-020| BC-061  |

**Table 63**: Booster magnets installation. 

<br />

## TB Transfer Line Magnets

### TB Dipoles and septum

The TB dipoles and septum main parameters are shown in Table 64. 

|  | Spectrometer| Dipole| Septum|  |
| --- | --- | --- | --- | --- |
|Number| 1| 3| 1|  |
|Magnetic length| 0.450| 0.304| 0.500| m |
|Physical length| --| 0.2945| --| m |
|Deflection angle| 15.0| 15.0| 21.75| Â° |
|Hardedge bending radius| 1.719| 1.161| 1.317| m |
|Hardedge magnetic field| 0.291| 0.431| 0.380| T |
|Quadrupole gradient| 0| 0| 0| T/m |
|Hardedge sagitta| 14.7| 9.293| 23.7| mm |

**Table 64**: Main parameters for LTB transfer line dipoles.

|  | TB Dipole| units |
| --- | --- | --- |
|Main coil current| 254| A |
|Main coil number of turns| 23|  |
|Stored magnetic energy| 116.6| J |
|Magnet inductance| 3.7| mH |

**Table 65**: TB dipole electric parameters.

<br />

### TB Dipole Magnet 3D Model

![](/img/machine/magnets/TB_magnet_dipole_drawing.png)

**Figure 78**: 3D drawing of the TB dipole model.

![](/img/machine/magnets/TB_magnet_dipole_field.png)

**Figure 79**: Field of the TB dipole model.

<br />

#### Fieldmap Analysis

A 3D magnetic model has been created and its fieldmap analyzed. A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/tb-dipoles/tree/master/links-official).

#### Segmented Model

In order to take into account the s-dependent field profile of the TB dipoles a symmetric model was created.

![](/img/machine/magnets/segmented_model_TB_Dipole.svg)

**Figure 80**: TB dipole By field on the trajectory calculated by Runge-Kutta integration and the adopted segmented model used in simulation codes. Only half dipole is shown in longitudinal direction.

Table with segmented dipole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0800| 3.966| -0.433| -0.001| -0.074 |
|02| 0.0200| 0.990| -0.432| -0.021| -0.268 |
|03| 0.0200| 0.940| -0.410| -0.644| -4.760 |
|04| 0.0200| 0.645| -0.282| -1.630| -6.590 |
|05| 0.0200| 0.382| -0.167| -0.775| -13.400 |
|06| 0.0200| 0.244| -0.107| -0.374| -14.100 |
|07| 0.0300| 0.205| -0.060| -0.213| -9.210 |
|08| 0.0300| 0.129| -0.037| -0.138| -6.080 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 66**: TB dipole segmented model.

Constructed from simulated fieldmap at nominal energy

<br />

### TB Dipole Magnet Measurements

A summary of magnet field measurements will eventually be documented here.

<br />

### TB Quadrupoles

The quadrupoles in the TB transfer line (TB-QD) use the same yoke as the Booster 8.5 cm long quadrupoles BQD (effective length of 10 cm). A new set of coils is used to allow higher gradient with a 10 A power supply. In the first TB sector (just after the last Linac accelerating structure), there are 4 quadrupoles (a quadrupole triplet and a focus quadrupole) that will be purchased as part of the Linac. The TB quadrupoles main parameters are shown in Table 67 and their detailed configuration in Table 69.

|  | Part of Linac| TB|  |
| --- | --- | --- | --- |
|Model name| Linac| BQD|  |
|Number| 4| 10|  |
|Physical length| 0.050 / 0.100| 0.085| m |
|Magnetic length| --| 0.100| m |
|Maximum field gradient| 10.0| 8.000| TÂ·m⁻¹ |
|Bore diameter| 40.0| 40.0| mm |
|Maximum field at pole tip| 0.2| 0.16| T  |

**Table 67**: Main parameters for LTB transfer line quadrupoles.

|  | TB Quadrupole| units |
| --- | --- | --- |
|Main coil current| 10.00| A |
|Main coil number of turns| 140|  |
|Stored magnetic energy| 5.62| J |
|Magnet inductance| 112.4| mH |

**Table 68**: TB quadrupole electric parameters.

dB/dx [T/m] @ E=150 MeV

|Quadrupole| Eff. Length [m]|M1| M2| M3| M4| M5| M6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|QD1| 0.100| -8.42| --| --| --| --| -- |
|QF1| 0.100| 13.15| --| --| --| --| -- |
|QD2A| 0.100| -5.00| --| --| --| --| -- |
|QF2A| 0.100| 6.78| --| --| --| --| -- |
|QF2B| 0.100| 2.90| --| --| --| --| -- |
|QD2B| 0.100| -2.98| --| --| --| --| -- |
|QF3| 0.100| 7.96| --| --| --| --| -- |
|QD3| 0.100| -2.01| --| --| --| --| -- |
|QF4| 0.100| 11.53| --| --| --| --| -- |
|QD4| 0.100| -7.08| --| --| --| --| -- |

**Table 69**: Quadrupole configuration for TB transfer line modes.

<br />

### TB Quadrupole Magnet 3D Model

![](/img/machine/magnets/TB_magnet_quadrupole_drawing.png)

**Figure 81**: 3D drawing of the TB quadrupole model.

![](/img/machine/magnets/TB_magnet_quadrupole_field.png)

**Figure 82**: Field of the TB quadrupole model.

<br />

#### Fieldmap Analysis

A 3D magnetic model has been created and its fieldmap analyzed. A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/tb-quadrupoles/tree/master/links-official). 

<br />

#### Segmented Model

In order to take into account the s-dependent field profile of the TB quadrupoles a symmetric model was created.

![](/img/machine/magnets/segmented_model_TB_Quadrupole.svg)

**Figure 83**: TB quadrupole By field on the trajectory calculated by Runge-Kutta integration and the adopted segmented model used in simulation codes. Only half quadrupole is shown in longitudinal direction.

Table with segmented quadrupole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0500| 0.000| -0.000e+00| +1.600e+01| +0.000e+00 |

*K=B'/(Bρ), S=B"/(2Bρ)

Constructed from simulated fieldmap at maximum excitation current.

**Table 70**: TB quadrupole segmented model.

<br />

### TB Quadrupole Magnet Measurements

A summary of magnet field measurements will eventually be documented here.

<br />

### TB Correctors

The main TB corrector parameters are shown in Table 71.

<br />

#### TB Corrector Magnet Specifications

##### Main Parameters

|Type of corrector| Number| Max. θ (mrad)| ∫B.ds [T.m] @ E=150 MeV |
| --- | --- | --- | --- |
|Septum| 1| ± 6.8| ± 3.4E-03 |
|CH| 5| ± 2.5| ± 1.25E-03 |
|CV| 6| ± 2.5| ± 1.25E-03  |

**Table 71**: Main parameters for LTB transfer line correctors. 

<br />

#### TB Corrector Magnet 3D Model

![](/img/machine/magnets/TB_magnet_corrector_drawing.png)

**Figure 84**: 3D drawing of the TB corrector model.

![](/img/machine/magnets/TB_magnet_corrector_field.png)

**Figure 85**: Field of the TB corrector model with its CH coils excited.

<br />

##### Fieldmap Analysis

**CH**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/tb-correctors/tree/master/links-official-ch).

**CV**

A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/tb-correctors/tree/master/links-official-cv). 

<br />

##### Segmented Model

Currently the hard-edge approximation is being used to model TB correctors.

![](/img/machine/magnets/TB_segmented_model_corrector.svg)

**Figure 86**:  TB corrector By field on the trajectory calculated by Runge-Kutta integration and the adopted segmented model used in simulation codes. Only half of corrector is shown in longitudinal direction.

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.0405| 0.000| -1.916e-02| -4.400e-06| -4.840e+01 |

*K=B'/(Bρ), S=B"/(2Bρ) 

**Table 72**: TB corrector half segmented model (maximum strength). 

<br />

#### TB Corrector Magnet Measurements

## TS Transfer Line Magnets

### TS Dipoles and septa

The TS dipoles and septum main parameters are shown in Table 73.

The TS dipoles are mechanically the same as the Booster dipoles but the deflection angle has been reduced from +7.2 Â° (Booster) to +5.012 Â° (TS). This is necessary to avoid overheating of the coils since BTS dipoles will operate in DC regime while Booster dipoles operate in CW mode.

|  | Dipoles| Thin ext. septum| Thick ext. septum| Thick inj. septum| Thin inj. septum|  |
| --- | --- | --- | --- | --- | --- | --- |
|Number| 3| 1| 1| 2| 1|  |
|Magnetic length| 1.216| 0.577| 0.577| 0.577| 0.500| m |
|Physical length| 1.206| --| --| --| --| m |
|Deflection angle| +5.012| -3.600| -3.600| +3.600| +3.118| Â° |
|Hardedge bending radius| 13.902| -9.188| -9.188| 9.188| 9.188| m |
|Integrated magnetic field| 0.875| -0.629| -0.629| 0.629| 0.545| TÂ·m |
|Integrated quadrupole strength| -0.169| -| -| -| -| m⁻¹ |
|Hardedge sagitta| 13.40| 4.53| 4.53| 4.53| 3.40| mm  |

**Table 73**: Main parameters for BTS septa and dipoles.

|  | TS Dipole| units |
| --- | --- | --- |
|Main coil current| 680.10| A |
|Main coil number of turns| 12|  |
|Stored magnetic energy| 1075.88| J |
|Magnet inductance| 4.65| mH  |

**Table 74**: TS dipole electric parameters.

<br />

#### TS Dipole Magnet 3D Model

Same model as for BO dipoles.

![](/img/machine/magnets/BO_magnet_dipole_drawing.png)

**Figure 87**: 3D drawing of the booster dipole model.

![](/img/machine/magnets/BO_magnet_dipole_field.png)

**Figure 88**: Field of the booster dipole model.

<br />

#### Fieldmap Analysis

A 3D magnetic model has been created and its [fieldmap analyzed][link] A summary of the analysis can be found in analysis.txt at [this folder](https://github.com/lnls-ima/ts-dipoles/tree/master/links-official). 

<br />

#### Segmented Model

![](/img/machine/magnets/segmented_model_TS_Dipole.svg)

**Figure 89**: TS dipole By field on the trajectory calculated by Runge-Kutta integration and the adopted segmented model used in simulation codes. Only half dipole is shown in longitudinal direction.

Table with segmented dipole model

|Segment#| Length [m]| Deflection [deg.]| Field [T]| K [m⁻²] *| S [m⁻³] * |
| --- | --- | --- | --- | --- | --- |
|01| 0.1960| 0.808| -0.720| -0.151| -1.350 |
|02| 0.1920| 0.796| -0.724| -0.144| -1.330 |
|03| 0.1820| 0.761| -0.730| -0.132| -1.320 |
|04| 0.0100| 0.035| -0.618| -0.158| -1.140 |
|05| 0.0100| 0.025| -0.445| -0.100| -0.858 |
|06| 0.0130| 0.023| -0.306| -0.036| -1.100 |
|07| 0.0170| 0.020| -0.208| -0.007| -1.240 |
|08| 0.0200| 0.016| -0.136| +0.002| -1.040 |
|09| 0.0300| 0.013| -0.074| +0.002| -0.616 |
|10| 0.0500| 0.009| -0.030| +0.001| -0.243 |

*K=B'/(Bρ), S=B"/(2Bρ)

**Table 75**: TS dipole segmented model.

<br />

### TS Quadrupoles

Table 76 lists main specifications for TS quadrupoles (same as the storage ring quadrupoles) and Table 77 their detailed configuration.

|Magnet model name| Q14| Q20|  |
| --- | --- | --- | --- |
|Number| 5| 3|  |
|Quadrupoles| QF1A,QF1B,QD2,QD4A,QD4B| QF2,QF3,QF4|  |
|Maximum gradient| 37.23| 45.43| TÂ·m⁻¹ |
|Bore diameter| 28| 28| mm |
|Maximum field at pole tip| 0.52| 0.64| T  |

**Table 76**: Main parameters for TS transfer line quadrupoles.

dB/dx [T/m] @ E=3 GeV

| Quadrupole| Length [m]| M1| M2 |
| --- | --- | --- | --- |
|QF1A| 0.14| 16.4| 17.6 |
|QF1B| 0.14| 12.6| 15 |
|QD2| 0.14| -34| -34.1 |
|QF2| 0.2| 26.9| 27.1 |
|QF3| 0.2| 32.7| 31.5 |
|QD4A| 0.14| -33.4| -32.1 |
|QF4| 0.2| 40.8| 40.5 |
|QD4B| 0.14| -17| -17.7 |

**Table 77**: BTS transfer line quadrupole configuration for modes M1 and M2

<br />

### TS Correctors

Table 78 lists main specifications for TS correctors

| Parameter | Value | Unit |
| --- | --- | --- |
|Length| 0.1| m |
|Number of horizontal correctors| 4|  |
|Number of septa used as horizontal correctors| 2|  |
|Number of vertical correctors| 6|  |
|Maximum strength| ±0.35| mrad |
|Maximum field (E=3 GeV)| ± 3.50E-03| T.m  |

**Table 78**: Main parameters for BTS transfer line correctors.

<br />

## Magnet Colors

| Magnet type | color |
| --- | --- |
|dipoles| RAL 5012 |
|quadrupoles| RAL 2008 |
|sextupoles| RAL 6021 |
|correctors| N6,5 Munsell |
|coils|  |
|girders| RAL 9010 |
|pulsed magnets| RAL 3000  |

**Table 79**: Magnet colors
