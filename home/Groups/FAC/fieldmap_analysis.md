# FAC: Fieldmap analysis

Field specification of every 3D nominal model of magnets is checked. This is accomplished by having its 3D-field map sampled on the mid-plane (at y = 0 mm) and analyzed. It can be demonstrated that knowledge of the 3D magnetic field on any plane, and on the mid-plane in particular, is enough for the reconstruction of the 3D field over the entire gap region. Apart from the discreteness of the fieldmap grid on the xz plane, numerical trajectories with arbitrary precision can be computed using standard Runge-Kutta integration algorithms. Multipoles around these trajectories can then be calculated and compared to specifications.

## 3D field extrapolation from the mid-plane

Maxwell equations for $\vec{B} = (B_x,B_y,B_z)$ can be solved in the magnet gap by expansion of the field components in power series around the midplane, $y = 0$:

$B_x(x,y,z) = {B_x}^(0)(x,z) + B_x^{(1)}(x,z) \; y + B_x^{(2)}(x,z) \; y^2 + \cdots \\
B_y(x,y,z) = B_y^{(0)}(x,z) + B_y^{(1)}(x,z) \; y + B_y^{(2)}(x,z) \; y^2 + \cdots \\
B_z(x,y,z) = B_z^{(0)}(x,z) + B_z^{(1)}(x,z) \; y + B_z^{(2)}(x,z) \; y^2 + \cdots \\$

where $B_x^{(0)}$, $B_y^{(0)}$ and $B_z^{(0)}$ are the three-components of the 3D fieldmap of the magnet on the mid-plane. The rotational of $\vec{B}$ in the source-free gap gives the following recursion relation:

$\frac{\partial B_x}{\partial y} - \frac{\partial B_y}{\partial x} = 0 \rightarrow B_x^{(n+1)} = \frac{\partial B_y^{(n)}}{\partial x} \\
\frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z} = 0 \rightarrow B_z^{(n+1)} = \frac{\partial B_y^{(n)}}{\partial z}$

whereas the divergence-free equation yields

$\frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = 0  \rightarrow B_y^{(n+1)} = - \left( \frac{\partial Bx^{(n)}}{\partial x} + \frac{\partial B_z^{(n)}}{\partial z} \right)$

this set of three equations allows us to reconstruct the 3D magnetic field off the midplane, if necessary, provided the $xz$ grid is fine enough for the calculation of required partial derivatives.

##  Mid-plane fieldmaps 

Fieldmaps of the 3D magnet models are usually generated with 1-mm spacing in the longitudinal $z$ direction and 0.5-mm spacing the horizontal or radial $x$ direction. As for range, horizontal and longitudinal maxima and minima depend on how fast the magnetic field falls down. Usually the longitudinal extend of the maps is such that the field has fallen to values much lower than 0.5 Gauss, or the typical magnitude earth's magentic field. Attention has to be paid also to guarantee that the integrated field outside the grid is negligible. The horizontal range is chosen in a way to allow multipoles to be calculated around the reference trajectory and to describe the whole field in the beam dynamics aperture. For dipoles the horizontal range has to be large to take into account the sagitta of the beam trajectory.

##  Analysis scripts 

There are four basic python scripts used to analyze fieldmaps: [fac-fma-rawfield.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-rawfield.py), [fac-fma-trajectory.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-trajectory.py), [fac-fma-multipoles.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-multipoles.py) and [fac-fma-model.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-model.py). Usually they are invoked in this order. In addition there is [fac-fma-profile.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-profile.py) that can be used to print and plot dipole segmented models. There is also a driving script called [fac-fma-analysis.py](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/fac-fma-analysis.py) which can be used to clean output files in the current directory ('clean' argument) and run ('run' argument) the other scripts in series. Its help describes all possibilities (completion can be used). These scripts are all driving routines to library objects and functions implemented in the [fieldmaptrack library](https://github.com/lnls-fac/code/tree/master/fieldmaptrack).

### fac-fma-rawfield.py

This script does basic analysis of the fieldmap. It is used to check for simple mistakes, such as the syntax of the ASCII file with the fieldmap, field polarity and order of magnitude. The script generates a text output called {{path|rawfield.out}} with information about the mid-plane grid spacings and maximum fields. It also generates PDF files with the field longitudinal and transversal roll-offs. By default, if no filename is passed as argument, the script will read an input file called {{path|rawfield.in}} in the current directory ([see example in link for help on input parameters](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/rawfield.in)).

### fac-fma-trajectory.py

Calculates a Runge-Kutta trajectory for an electron subject to a given fieldmap and a particular initial conditions. The algorithm used is a RK integrator of fourth order. The independent coordinate used is the electron path length $s$ and the spatial coordinates are the Cartesian coordinates $x$ (horizontal/radial), $y$ (vertical) and $z$ (local longitudinal), corresponding to the fieldmap coordinate system. The right-hand rule $\hat{z} = \hat{x} \times \hat{y}$ applies in this system. As for ''momenta'', the dependent coordinates chosen are the linear ''momenta'' normalized by the nominal momentum: 

$x' \equiv \frac{p_x}{p_0} = \frac{1}{\beta c} \frac{dx}{dt} = \frac{dx}{ds} \\
y' \equiv \frac{p_y}{p_0} = \frac{1}{\beta c} \frac{dy}{dt} = \frac{dy}{ds} \\
z' \equiv \frac{p_z}{p_0} = \frac{1}{\beta c} \frac{dz}{dt} = \frac{dz}{ds}$

The exact equations of motion in these coordinates are as follows,

$\frac{dx'}{ds} = - \frac{1}{\beta |B\rho|} \left( y' B_z - z' B_y \right) \\
\frac{dy'}{ds} = - \frac{1}{\beta |B\rho|} \left( z' B_x - x' B_y \right) \\
\frac{dz'}{ds} = - \frac{1}{\beta |B\rho|} \left( x' B_y - y' B_x \right)$

With these variables the deflection angle $\theta$ of the trajectory from $s_1$ to $s_2$ is given by

$\theta = \left. \arctan  \left( \frac{dx}{dz} \right) \right|_{s_1}^{s_2} = \left. \arctan  \left( \frac{x'}{z'} \right) \right|_{s_1}^{s_2}.$

The script reads an input file called `trajectory.in` ([see example in link for help on input parameters](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/trajectory.in)) and generates an output text file called `trajectory.out` with results of analysis. An important information stored in this file is the value of the parameter ''rx position of reference point''. This is the horizontal coordinate of the intersection point of the two tangential straight lines, one upstream and the other downstream the trajectory. Since symmetry longitudinal symmetry is always assumed for the magnets, this point lies on the center line of the magnet (rz = 0). This reference point can be used for the fiducialization of the magnet. A file called `field_on_trajectory.txt` is generated in the current directory.

### fac-fma-multipoles.py

Calculates multipoles around a given reference trajectory. At each point along the trajectory a perpendicular line on the mid-plane is calculated and the field is interpolated on a grid of points on this line. Multipoles of specified orders are then fitted to the interpolated field. These multipoles, as functions of the arc length $s$, are then stored in an output file called `multipoles.txt`. An output file `multipoles.out` is also generated with a summary which includes the relative multipoles at a particular radial position $x = r_0$. These relative multipoles serve as input for generating random machines with multipolar errors. PDF files are automatically generated with multipole profiles, one for each fitted monomial. Finally, a plot of the residual field profile (without the nominal contribution) is generated both by integrating the fitted multipoles around the trajectory and by integrating the field in paralel trajectories. The match between the two profiles should indicate the goodness of the multipoles fit. The input file to the script in called `multipoles.in` ([see example in link for help on input parameters](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/multipoles.in)).

### fac-fma-model.py

Generates a segmented model of the magnet by integrating multipoles in each model slice. The segmented model is defined in the input file `model.in` ([see example in link for help on input parameters](https://github.com/lnls-fac/code/blob/master/scripts/fieldmap_analysis/model.in)). The output file `model.out` contains the segmented model and its normalized multipoles, each line corresponding to a slice in the model. The last slice contains the normalized multipoles integrated from the beginning of the slice to the end of the trajectory, divided by the length of the slice. In other words, whatever leaks out the model length is integrated back into the last model slice.

### fac-fma-profile.py

Opens a dialog box with which the user can select a directory containing a `analysis.txt` and a `multipoles.txt` files generated in a fieldmap analysis and that are used to print and plot segmented models.

### fac-fma-analysis.py

Is a drive script with which all previous scripts can either be run separately in order (e.g., `fac-fma-analysis.py rawfield`) or in series `fac-fma-analysis.py run`. Other options such as `help`, for example, are available. Bash completion for `fma-analysis.py` is implemented and can be used to list all its command options.