# FAC: Segmented and Rectangular Sirius Dipole Models

<br>

## Introduction

AT this point the Sirius dipoles are supposed to be rectangular but with curved poles. We have studied feasibility of different dipole models for the Sirius storage ring. The first model studied is that of a rectangular dipole in which the pole is also rectangular, that is, with constant field and gradient in the rectangular coordinate system. In this case the field varies along the trajectory of the beam. We analyzed the impact of this varying field on the beam optics and equilibrium parameters in order to ascertain the feasibility of the model. The second model studied was that of breaking Sirius dipoles into a composition of basic segments: B1 dipoles would be made of two identical segments, B2 dipoles would be made of three segments and B3 dipoles are made of a single segment. In this case we analyzed the impact of independent alignment of the segments on the alignment tolerance, due to the impact on the beam optics.

<br>

### Rectangular-pole dipole model

It has been argued that extra machining required in a dipole with curved poles represent a difficulty not worth pursuing in order to minimize the extent of the good-field region. It also probably represents additional costs in manufacturing. One possible alternative model would be of a rectangular dipole with rectangular poles. Fine machining of its poles would be simpler and could be cheaper. But the substitution of the current dipole model - rectangular with curved poles - to this model with rectangular poles will change the beam optics and equilibrium parameters, such as tunes, natural emittance and so on. We have calculated these changes.

To take into account the impact of this model we performed a Runge-Kutta integration of the trajectory in the presence of a hard-edge field with an explicit analytical expression:

$$
B_y(x) = B_0 + G x
$$

The nominal field gradient $G$ of 7.8054 T.m⁻¹ was fixed and used. The dipolar field $B_0$ was searched for the RK trajectory to give the nominal deflection angle of the dipole. We also kept the original hard-edge lengths of the dipoles. These analyses were made using adaptations of the fieldmap analysis scripts (see [Fieldmap analysis](/Machine/Groups/FAC/fieldmap_analysis)). 

The vertical field component on the RK trajectories for these models are depicted on Figure 1.


|![](/img/groups/fac/sirius_dipole_models/Fac_sirius_dipole_models.svg)|
|-|
|**Figure 1**:  Field along trajectory for B1, B2 and B3 dipoles with rectangular poles.|

From these field profiles segmented AT models have been created to study the changes in the beam optics. Below is a listing with the segmentated model for all three types of dipoles. 

**B1 AT dipole model**

```
dip_nam = 'B1';
dip_len = 0.828080;
dip_ang = 2.766540 * (pi/180);
dip_K   = -0.78;
dip_S   =  0.0;
h01 = rbend_sirius(dip_nam, dip_len/20, 0.0518771353 * dip_ang, 1*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h02 = rbend_sirius(dip_nam, dip_len/20, 0.0512879975 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h03 = rbend_sirius(dip_nam, dip_len/20, 0.0507573445 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h04 = rbend_sirius(dip_nam, dip_len/20, 0.0502945581 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h05 = rbend_sirius(dip_nam, dip_len/20, 0.0498990223 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h06 = rbend_sirius(dip_nam, dip_len/20, 0.0495702105 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h07 = rbend_sirius(dip_nam, dip_len/20, 0.0493076850 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h08 = rbend_sirius(dip_nam, dip_len/20, 0.0491110961 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h09 = rbend_sirius(dip_nam, dip_len/20, 0.0489801821 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h10 = rbend_sirius(dip_nam, dip_len/20, 0.0489147687 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h11 = rbend_sirius(dip_nam, dip_len/20, 0.0489147687 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h12 = rbend_sirius(dip_nam, dip_len/20, 0.0489801821 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h13 = rbend_sirius(dip_nam, dip_len/20, 0.0491110961 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h14 = rbend_sirius(dip_nam, dip_len/20, 0.0493076850 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h15 = rbend_sirius(dip_nam, dip_len/20, 0.0495702105 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h16 = rbend_sirius(dip_nam, dip_len/20, 0.0498990223 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h17 = rbend_sirius(dip_nam, dip_len/20, 0.0502945581 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h18 = rbend_sirius(dip_nam, dip_len/20, 0.0507573445 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h19 = rbend_sirius(dip_nam, dip_len/20, 0.0512879975 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h20 = rbend_sirius(dip_nam, dip_len/20, 0.0518771353 * dip_ang, 0*dip_ang/2, 1*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
B1  =  [h01, h02, h03, h04, h05, h06, h07, h08, h09, h10, mb1, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, ];
```

**B2 AT dipole model**

```
dip_nam = 'B2';
dip_len = 1.228262;
dip_ang = 4.103510 * (pi/180);
dip_K   = -0.78;
dip_S   =  0.0;
h01 = rbend_sirius(dip_nam, dip_len/20, 0.0541002838 * dip_ang, 1*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h02 = rbend_sirius(dip_nam, dip_len/20, 0.0527884286 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h03 = rbend_sirius(dip_nam, dip_len/20, 0.0516318352 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h04 = rbend_sirius(dip_nam, dip_len/20, 0.0506271179 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h05 = rbend_sirius(dip_nam, dip_len/20, 0.0497713347 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h06 = rbend_sirius(dip_nam, dip_len/20, 0.0490619790 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h07 = rbend_sirius(dip_nam, dip_len/20, 0.0484969728 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h08 = rbend_sirius(dip_nam, dip_len/20, 0.0480746606 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h09 = rbend_sirius(dip_nam, dip_len/20, 0.0477938048 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h10 = rbend_sirius(dip_nam, dip_len/20, 0.0476535824 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h11 = rbend_sirius(dip_nam, dip_len/20, 0.0476535824 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h12 = rbend_sirius(dip_nam, dip_len/20, 0.0477938048 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h13 = rbend_sirius(dip_nam, dip_len/20, 0.0480746606 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h14 = rbend_sirius(dip_nam, dip_len/20, 0.0484969728 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h15 = rbend_sirius(dip_nam, dip_len/20, 0.0490619790 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h16 = rbend_sirius(dip_nam, dip_len/20, 0.0497713347 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h17 = rbend_sirius(dip_nam, dip_len/20, 0.0506271179 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h18 = rbend_sirius(dip_nam, dip_len/20, 0.0516318352 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h19 = rbend_sirius(dip_nam, dip_len/20, 0.0527884286 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h20 = rbend_sirius(dip_nam, dip_len/20, 0.0541002838 * dip_ang, 0*dip_ang/2, 1*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
B2  =  [h01, h02, h03, h04, h05, h06, h07, h08, h09, h10, mb2, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, ];
```
 
**B3 AT dipole model**

```
dip_nam = 'B3';
dip_len = 0.428011;
dip_ang = 1.429950 * (pi/180);
dip_K   = -0.78;
dip_S   =  0.0;
h01 = rbend_sirius(dip_nam, dip_len/20, 0.0505073397 * dip_ang, 1*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h02 = rbend_sirius(dip_nam, dip_len/20, 0.0503471250 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h03 = rbend_sirius(dip_nam, dip_len/20, 0.0502045375 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h04 = rbend_sirius(dip_nam, dip_len/20, 0.0500798842 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h05 = rbend_sirius(dip_nam, dip_len/20, 0.0499731207 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h06 = rbend_sirius(dip_nam, dip_len/20, 0.0498842091 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h07 = rbend_sirius(dip_nam, dip_len/20, 0.0498131177 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h08 = rbend_sirius(dip_nam, dip_len/20, 0.0497598213 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h09 = rbend_sirius(dip_nam, dip_len/20, 0.0497243009 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h10 = rbend_sirius(dip_nam, dip_len/20, 0.0497065439 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h11 = rbend_sirius(dip_nam, dip_len/20, 0.0497065439 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h12 = rbend_sirius(dip_nam, dip_len/20, 0.0497243009 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h13 = rbend_sirius(dip_nam, dip_len/20, 0.0497598213 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h14 = rbend_sirius(dip_nam, dip_len/20, 0.0498131177 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h15 = rbend_sirius(dip_nam, dip_len/20, 0.0498842091 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h16 = rbend_sirius(dip_nam, dip_len/20, 0.0499731207 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h17 = rbend_sirius(dip_nam, dip_len/20, 0.0500798842 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h18 = rbend_sirius(dip_nam, dip_len/20, 0.0502045375 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h19 = rbend_sirius(dip_nam, dip_len/20, 0.0503471250 * dip_ang, 0*dip_ang/2, 0*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
h20 = rbend_sirius(dip_nam, dip_len/20, 0.0505073397 * dip_ang, 0*dip_ang/2, 1*dip_ang/2, 0, 0, 0, [0 0 0], [0 dip_K dip_S], bend_pass_method);
B3  =  [h01, h02, h03, h04, h05, h06, h07, h08, h09, h10, mb3, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, ];
```

Calculations on AT shows that the changes from going to hard-edge models to these segmented models are very small and could be accommodated in a new lattice optimization. Horizontal tune change is negligible whereas vertical tunes changes is small, of the order of 0.03. Dispersion function changes around 0.3/0.5 mm and natural emittance increases by 1%. From the points of view of the linear optics these rectangular-pole models are fine. It remains to be seen whether multipole specifications can really be met with rather large good-field regions which are intrinsic to these dipole models.

**Table 1**: Main effects of the rectangular dipoles on Sirius Parameters.

|Parameter| Variation |
|-|-|
|Horizontal Tune| 2×10-3|  |
|Vertical Tune| 3×10-2|  |
|Dispersion Function @Straight Sections| 0.3/0.5| mm |
|Equilibrium Emittance| 1|  % |

<br>

### Segmented dipole model

The second alternative consists in making only one kind of rectangular magnetic core for all the dipoles and grouping different numbers of these blocks to form the three families of dipoles, being B1 formed by two segments, B2 by three, and B3 by one. However, there would be only one coil per magnet to save space in the lattice and to place the segments inside a magnet closer to each other, minimizing variations of the bending field between them. One important aspect of these segmented dipoles is that the cores would be aligned tilted in relation to each other, to maximize the homogeneity of the bending field along the curved reference trajectory of the electrons.

Our model of such dipoles assumed no variations of the field between segments in the dipoles and no variation of the field along each segment. While the latter assumption is well justified by the small sagita of each block, the first must be revised as soon as the magnetic and mechanic design of the magnets become available, because it depends very strongly on the separation between the segments. The main effect of this model on the beam dynamics is the different edge focusing due to the difference in the edge angle in relation to the conventional rectangular dipole. In the rectangular model the edge angle is half the deflection angle of the whole magnet, while in the segmented dipole, it is equal to half of the angle of one block, which reduces the edge angle of the B2 and B3 dipoles by a factor of three and two, respectively. With this difference in the vertical focusing the optics must be adjusted to restore optical functions. In this process the dipoles gradient was changed from 0.7800 m<sup>-2</sup> to 0.7848 m<sup>-2</sup> but no variations in the equilibrium values, tunes and maximum betatron functions were observed.

Another effect of this segmented model of the dipoles in the beam dynamics is related to the magnet tolerances. In this configuration the blocks which constitutes a given magnet have uncorrelated alignment, rotation and excitation errors, which could change the residual closed orbit and betabeating of the machine, leading to tighter or relaxed tolerances. <xr id="fig:cod"/> and <xr id="fig:betabeat"/> compare the effect of correlated and uncorrelated errors in the dipole blocks, simulating  and <xr id="tab:comp_correlated_and_uncorrelated"/> shows the statistics of the residual orbit and betabeating for both configurations. We notice the results with uncorrelated errors have smaller residual closed orbit in the vertical plane and smaller betabeating in both planes, which does not invalidates the possibility of breaking the dipoles.


|![](/img/groups/fac/sirius_dipole_models/Sirius_SR_segmented_model_dip_correlated_errors_betabeat.svg)|
|-|
|**Figure 2**: Residual closed orbit after correction for one superperiod of the storage ring with and without correlated errors in the dipole segments.|


|![](/img/groups/fac/sirius_dipole_models/Sirius_SR_segmented_model_dip_correlated_errors_betabeat.svg)|
|-|
|**Figure 3**: Residual betabeting after orbit correction for one superperiod of the storage ring with and without correlated errors in the dipole segments.|


**Uncorrelated - COD**

Individual Machine Statistics: 

|   i |   codx[um]    |   cody[um]    | max. kick [urad] |
|-|-|-|-|
|     | (max)  (std)  | (max)  (std)  |   x     y    |
| 001 |  26.33   6.11 |  50.81  11.24 |  85.38  59.44  |
| 002 |  36.90   7.30 |  73.34  11.84 |  83.89  62.66  |
| 003 |  31.47   7.31 |  71.09  11.88 |  96.88  67.43  |
| 004 |  31.41   6.02 |  49.89  11.65 |  70.32  52.47  |
| 005 |  28.04   7.37 |  59.09  12.08 |  81.41  73.71  |
| 006 |  30.68   7.34 |  70.03  11.36 |  67.07  66.39  |
| 007 |  30.64   7.00 |  52.82  11.00 |  88.75  59.48  |
| 008 |  28.15   7.21 |  75.81  12.05 |  75.14  55.68  |
| 009 |  27.97   6.51 |  59.98  13.73 |  73.95  51.23  |
| 010 |  29.83   7.02 |  60.78  10.51 |  79.10  50.24  |
| 011 |  26.60   7.05 |  53.75  12.85 |  73.53  68.43  |
| 012 |  24.55   6.67 |  67.03  11.64 |  73.67  62.83  |
| 013 |  31.35   7.73 |  66.95  11.90 |  82.12  46.79  |
| 014 |  29.35   6.59 |  53.92  11.16 |  77.46  68.42  |
| 015 |  28.88   6.68 |  52.78  11.81 |  82.00  70.22  |
| 016 |  23.58   6.61 |  51.51  11.72 |  72.12  51.07  |
| 017 |  31.16   7.18 |  59.60  11.21 |  71.86  55.44  |
| 018 |  26.18   6.86 |  71.50  14.60 |  80.56  51.66  |
| 019 |  29.93   7.18 |  69.42  10.59 |  74.60  53.28  |
| 020 |  32.53   7.17 |  52.27  11.26 |  80.37  61.70  |


Estimative of emsemble properties:

std (kickx, kicky) [urad]: (26.034, 22.539)
max (kickx, kicky) [urad]: (96.884, 73.714)
max(<x(s)^2>_E-<x(s)>_E^2) cod: 18.086 um @ s = 29.25 (hcm)
max(<y(s)^2>_E-<y(s)>_E^2) cod: 34.017 um @ s = 16.54 (mb2)
rms corrected cod @ all  (x,y) [um]: (6.963, 11.848)
rms corrected cod @ bpms (x,y) [um]: (2.721, 6.012)


**Correlated - COD**

Individual Machine Statistics: 

|  i |   codx[um]    |   cody[um]    | max. kick [urad] |
|-|-|-|-|
|    | (max)  (std)  | (max)  (std)  |   x     y    |
|001 |  29.67   7.42 |  75.62  13.22 |  78.81  82.38  |
|002 |  29.79   6.89 |  59.91  12.29 |  79.11  86.44  |
|003 |  28.49   6.65 |  94.82  15.22 |  70.10  71.67  |
|004 |  30.28   7.80 |  54.67  12.16 |  85.30  68.18  |
|005 |  30.58   7.93 |  70.60  11.77 |  94.13  65.70  |
|006 |  32.25   8.44 |  58.36  13.42 |  81.97  72.60  |
|007 |  29.39   7.30 |  51.26  12.43 |  79.37  67.16  |
|008 |  29.26   7.44 |  74.46  12.31 |  66.69  74.33  |
|009 |  29.56   7.43 |  74.74  12.07 |  74.17  74.90  |
|010 |  32.73   7.39 |  76.67  14.14 |  80.12  64.87  |
|011 |  29.51   7.28 |  76.67  13.80 |  64.45  75.87  |
|012 |  36.85   7.51 |  83.66  15.26 |  75.85  70.72  |
|013 |  30.06   7.22 |  81.23  15.35 |  71.14  63.49  |
|014 |  30.06   7.75 |  95.28  13.95 |  86.15  94.42  |
|015 |  27.13   7.65 |  58.25  12.00 |  78.01  64.69  |
|016 |  33.01   7.53 |  70.87  13.79 |  77.55  77.19  |
|017 |  32.83   7.72 |  59.04  13.29 |  91.39  65.53  |
|018 |  31.86   8.01 |  78.69  14.15 |  86.62  83.95  |
|019 |  28.93   7.61 |  55.38  11.62 |  88.58  73.84  |
|020 |  34.13   7.46 |  43.10  10.53 |  81.38  63.80  |

Estimative of emsemble properties:

std (kickx, kicky) [urad]: (27.144, 26.839)
max (kickx, kicky) [urad]: (94.127, 94.422)
max(<x(s)^2>_E-<x(s)>_E^2) cod: 18.452 um @ s = 34.26 (hcm)
max(<y(s)^2>_E-<y(s)>_E^2) cod: 43.881 um @ s = 16.95 (b2)
rms corrected cod @ all  (x,y) [um]: (7.536, 13.210)
rms corrected cod @ bpms (x,y) [um]: (2.794, 6.793)


**Uncorrelated - BetaBeat**

Individual Machine Statistics: 

|  i | dbetax [%]   | dbetay [%]    |
|-|-|-|
|    | (max)  (std)  | (max)  (std)   |
|001 |   8.72   1.67 |  10.87   2.51  |
|002 |  27.32   6.81 |  17.38   4.15  |
|003 |   9.57   2.29 |  16.46   4.22  |
|004 |  17.27   4.20 |  15.29   4.21  |
|005 |  13.56   2.78 |   9.88   1.91  |
|006 |   7.25   1.64 |  13.23   3.13  |
|007 |  17.54   4.22 |  17.92   4.14  |
|008 |  14.66   3.30 |  19.18   4.82  |
|009 |   8.92   1.93 |  17.35   4.03  |
|010 |  11.02   2.30 |  21.14   4.75  |
|011 |  10.69   2.72 |  20.60   4.41  |
|012 |  17.28   3.72 |  14.92   2.61  |
|013 |  13.42   3.22 |  12.46   2.93  |
|014 |  12.84   3.34 |  15.90   3.14  |
|015 |   8.72   1.83 |  16.45   3.65  |
|016 |  11.22   2.70 |  20.12   3.99  |
|017 |  20.30   4.75 |  15.16   3.27  |
|018 |  17.51   3.83 |  10.11   2.16  |
|019 |   8.20   1.96 |  11.54   2.33  |
|020 |   8.98   1.78 |  15.20   2.79  

Estimative of emsemble properties:

std (dbetax, dbetay) [%]: (4.289, 3.783)
max (dbetax, dbetay) [%]: (27.316, 21.145)


**Correlated - BetaBeat**

Individual Machine Statistics: 

|  i | dbetax [%]   | dbetay [%]    |
|-|-|-|
|    | (max)  (std)  | (max)  (std)   |
|001 |   8.48   1.71 |  11.53   2.68  |
|002 |  13.34   2.70 |  11.11   2.56  |
|003 |   9.45   2.12 |  12.93   3.21  |
|004 |  17.39   3.82 |  13.91   2.50  |
|005 |  17.65   4.33 |  14.46   3.56  |
|006 |   9.81   1.97 |  14.94   3.74  |
|007 |  11.32   2.72 |  18.94   4.85  |
|008 |  24.86   5.93 |  10.59   2.20  |
|009 |  16.13   3.81 |  12.84   2.98  |
|010 |  14.92   3.30 |  18.82   2.47  |
|011 |  20.44   4.92 |  16.12   3.28  |
|012 |   9.80   1.87 |  35.24   8.65  |
|013 |  19.82   4.84 |  23.22   4.26  |
|014 |  15.07   3.16 |  16.57   4.17  |
|015 |  32.54   8.17 |  10.47   2.97  |
|016 |   7.81   1.44 |  13.16   2.94  |
|017 |   6.22   1.38 |  13.72   2.37  |
|018 |  13.94   2.68 |  14.83   3.58  |
|019 |   9.19   1.99 |  15.14   3.12  |
|020 |  20.80   4.89 |  18.78   4.36  |

 Estimative of emsemble properties:

std (dbetax, dbetay) [%]: (5.116, 4.321)
max (dbetax, dbetay) [%]: (32.539, 35.237)