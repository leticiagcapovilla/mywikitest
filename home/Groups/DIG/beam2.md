---
title: Beam 2
description: 
published: 1
date: 2024-02-29T15:15:47.355Z
tags: 
editor: markdown
dateCreated: 2024-02-29T14:16:28.261Z
---

# DIG: Beam Position Calculation

See also: [Beam Diagnostics and Feedback System][link] and [DIG Group Page][link]

## General

  Due to beam high speed, an efficient and fast measurement is required, allowing the control of the beam position. This is done by combining a hardware implementation using FPGA with an efficient calculation algorithm. Through simulations it is possible to compare different algorithms, finding the one that best suits the needs of the machine operation. The coordinate system used is in accordance with all the other conventions, as seen on [Coordinate System and Conventions][link].

### Simulation Algorithm

Data acquisition is made through four antennas arranged on the edges of the vacuum chamber, as shown in Figure 1. These antennas are responsible for measuring the current density induced by the electron beam, and for a situation where the beam passes through the centre of the chamber, the induced values are equal. If there is a displacement, the induced intensity on each antenna would be different, allowing to estimate the xy displacement using these values. To make a comparison between different calculation algorithms, the following steps have been taken:

1.  Definition of the points x and y, representing the coordinates where the beam would pass.

2.  Using a script provided earlier, the excitations at the antennas A, B, C and D are calculated for each one of the coordinates previously defined.

3.  Excitations are used in the algorithms, obtaining the respective positions x' and y'.

![Chamber_ilu.png](/img/groups/dig/beam_pos_calc/Chamber_ilu.png)

**Figure 1**: Vacuum chamber ilustration.

### "K" Compensation

After the calculation of the beam positions, a considerable discrepancy between the real value and the obtained one is usually observed. This difference can be reduced by the multiplication of the latter by a factor "K", obtained according to the methods described below.

#### Constant "K"

The "K" value is a constant obtained through the first-degree linear interpolation of the measures of the central region of the chamber. The "K" is calculated as the inverse of the angular coefficient obtained, so that values at this region have the measured value (horizontal axis) equivalent to the actual values (vertical axis) as seen in Figure 2.

![](/img/groups/dig/beam_pos_calc/K_calc_demo.png)

**Figure 2**: Comparison of pure and compensated measures.

#### Variable "K"

Another way to compensate the measures is to consider a polynomial $K(x,y)$, which apply a different correction factor for each point in space. In this case, a few iterations are made to converge the measure to a value close to the real one, as seen on the equations below: 

$x_{n+1} = Method * K_x(x_n, y_n)$

$y_{n+1} = Method * K_y(x_n, y_n)$

The variable $Method$ stands for any calculation equation being used to calculate the coordinates.

### Line Gain Differences

Although the physical construction and installation of equipments is made seeking to minimize the differences between the measurements on each antenna, small imperfections in them result in different gains in measures. One way to minimize this is to conduct a switching between opposing antennas, so that a signals passes through one equipment line (having a respective gain, "T1" for example) and then through the opposite line ( having a gain "T2", for instance). In this way, through further processing is possible to take a mean value of the switched signal, obtaining a signal close to the pure ones, without the distortions caused by different gains from each equipment line, as seen in Figure 3.

![](/img/groups/dig/beam_pos_calc/B_gain_ilu.png)

**Figure 3**: Signals of antennas A and B after the switching, and their respective mean values.

## Methods

### Delta/Sigma $(&Delta;/&Sigma;)$

#### Model

The $x$ and $y$ values are calculated using the following formulae:

$x= \frac{(a+d)-(b+c)}{a+b+c+d} \cdot K_x$

$y= \frac{(a+b)-(c+d)}{a+b+c+d} \cdot K_y$

After the $Kx$ calibration process, the output curve is as observed on Figure 4. Using the system symmetry, is possible to consider $K_y = K_x$.

![](/img/groups/dig/beam_pos_calc/1_1.png)

**Figure 4**: Calibration curve of the Delta/Sigma Method.

#### Line Gain

Considering the gains $T_1$,$T_2$,$T_3$ and $T_4$ for the lines of antennas A, B, C and D respectively, and calculating the mean values as the geometric mean, the $x$ equation would be:

$$
x= \frac{(a+d)-(b+c)}{a+b+c+d} \cdot K_x
$$

$$
=\frac{(\sqrt{A^2 \cdot {\color{red}T_1 \cdot T_2}}+\sqrt{D^2 \cdot {\color{blue}T_3 \cdot T_4}})-(\sqrt{B^2 \cdot {\color{blue}T_3 \cdot T_4}}+\sqrt{C^2 \cdot {\color{red}T_1 \cdot T_2}})}{\sqrt{A^2 \cdot {\color{red}T_1 \cdot T_2}}+\sqrt{B^2 \cdot {\color{blue}T_3 \cdot T_4}}+\sqrt{C^2 \cdot {\color{red}T_1 \cdot T_2}}+\sqrt{D^2 \cdot {\color{blue}T_3 \cdot T_4}}} \cdot K_x
$$

$$
=\frac{\sqrt{\color{red}T_1 \cdot T_2} \cdot (A-C) + \sqrt{\color{blue}T_3 \cdot T_4} \cdot (D-B)}{\sqrt{\color{red}T_1 \cdot T_2} \cdot (A+C) + \sqrt{\color{blue}T_3 \cdot T_4} \cdot (D+B)} \cdot K_x
$$

It is important to observe that the terms $\sqrt{T_1 \cdot T_2}$ and $\sqrt{T_3 \cdot T_4}$ were not cancelled, and further processing is required to compensate these in order to reduce its interference on the measuring process. If a arithmetic mean had been used, a similar situation would have happened, as the values would not have been cancelled as well.

#### Real and Calculated Values

Choosing a matrix of coordinates $x$ and $y$ in a 5 mm square representing positing where the beam would pass, a corresponding matrix of the points seen by the algorithm is shown in Figure 5.

![](/img/groups/dig/beam_pos_calc/1_2.png) ![](/img/groups/dig/beam_pos_calc/1_3.png)

**Figure 5**: Real and calculated coordinates for the Delta/Sigma Method.

#### Contour Plot Inaccuracy

A contour plot was made to show the inaccuracy variation on the considered area, as seen on Figure 6. The result was based on the difference between the distances to the origin, according to the following equation:

$Inaccuracy = \sqrt{(x')^2 + (y')^2} - \sqrt{x^2 + y^2}$ 

Considering $x$ and $y$ as the real positions and $x'$ and $y'$ as the calculated ones.

![](/img/groups/dig/beam_pos_calc/1_4.png)

**Figure 6**: Inaccuracy contour plot of the Delta/Sigma Method.

#### Advantagens vs. Disadvantages

* Cheap processing
* Doesn't eliminate line gain
* Low Accuracy

----

### Pi/Pi ($&Pi;/&Pi;$)

#### Model

The $x$ and $y$ values are calculated using the following formulae:

$x=log\left(\frac{a}{c}\right) \cdot K_x$

$y=log\left(\frac{b}{d}\right) \cdot K_y$

After the $Kx$ calibration process, the output curve is as observed on Figure 7. Using the system symmetry, is possible to consider $K_y = K_x$.

![](/img/groups/dig/beam_pos_calc/2_1.png)

**Figure 7**: Calibration curve of the Pi/Pi Method.

#### Line Gain

Considering the gains $T_1$,$T_2$,$T_3$ and $T_4$ for the lines of antennas A, B, C and D respectively, and calculating the mean values as the geometric mean, the $x$ equation would be:

$$
x=log\left(\frac{a \cdot d}{b \cdot c}\right) \cdot K_x
$$

$$
=log\left(\frac{\sqrt{A^2 \cdot {\color{red}T_1 \cdot T_2}} \cdot \sqrt{D^2 \cdot {\color{blue}T_3 \cdot T_4}}}{\sqrt{B^2 \cdot {\color{blue}T_3 \cdot T_4}} \cdot \sqrt{C^2 \cdot {\color{red}T_1 \cdot T_2}}}\right) \cdot K_x
$$

$$
=log \left( \left( \frac{\cancel{\sqrt{\color{red}T_1 \cdot T_2}} \cdot \cancel{\sqrt{\color{blue}T_3 \cdot T_4}}}{\cancel{\sqrt{\color{blue}T_3 \cdot T_4}} \cdot \cancel{\sqrt{\color{red}T_1 \cdot T_2}}} \right) \cdot \left( \frac{\sqrt{A²} \cdot \sqrt{B²}}{\sqrt{B²} \cdot \sqrt{C²}} \right) \right) \cdot K_x
$$

$$
=log\left(\frac{A \cdot D}{B \cdot C}\right) \cdot K_x
$$

In this case, the gains $T_1$,$T_2$,$T_3$ and $T_4$ were mathematically cancelled, reducing processing effort as a compensation is not required anymore. The second part of the equation (B and D) was omitted for a better visualization and is similar to the cancellation done using A and C. If a arithmetic mean had been used, the result would have been the same, and the gains would have been cancelled.

#### No Iteration

##### "K" Calculation

If $Kx$ is consider as a constant value resulting from the calibration process done so far, the resulting curve would be as shown in <xr id="fig:4_1"/>, and $K_y = K_x$ by the system symmetry.

![](/img/groups/dig/beam_pos_calc/4_1.png)

**Figure 10**: Calibration curve of the Partial Delta/Sigma Method (No iteration).

##### Real and Calculated Values

Choosing a matrix of coordinates $x$ and $y$ in a 5 mm square representing positing where the beam would pass, a corresponding matrix of the points seen by the algorithm is shown in Figure 11. 

![](/img/groups/dig/beam_pos_calc/4_2.png) ![](/img/groups/dig/beam_pos_calc/4_3.png)

**Figure 11**: Real and calculated coordinates for the Partial Delta/Sigma (No iteration) Method.

##### Contour Plot Inaccuracy

A contour plot was made to show the inaccuracy variation on the considered area, as seen on Figure 12. The result was based on the difference between the distances to the origin, according to the following equation:

${Inaccuracy = \sqrt{(x')^2 + (y')^2} - \sqrt{x^2 + y^2}}$ 

Considering $x$ and $y$ as the real positions and $x'$ and $y'$ as the calculated ones.

![](/img/groups/dig/beam_pos_calc/4_4.png)

**Figure 12**: Inaccuracy contour plot of the Partial Delta/Sigma (No iteration) Method.

##### Advantagens vs. Disadvantages

* Cheap processing
* Line gain compensation
* Low accuracy


#### Using 5 Iterations

##### "K" Polynom

Another approach to compensate the differences between real and calculated values is to use a function that has different gains depending on its position, and not a constant one as done so far. This can be done using the following strategy:

$x_{n+1} = K_x\left ( x_n,y_n \right ) \cdot Method$
	
$y_{n+1} = K_y\left ( x_n,y_n \right ) \cdot Method$

It is important to realise that the more iterations are done, the more the calculated value approximates the real one. For this case, the polynoms are calculated using the following equations:

$K_x\left ( x_0,y_0 \right ) = a_0 + a_1 \cdot y_0^2 + a_2 \cdot y_0^4 + a_3 \cdot x_0^2 + a_4 \cdot x_0^2 \cdot y_0^2 + a_5 \cdot x_0^4$
	
$K_y\left ( x_0,y_0 \right ) = b_0 + b_1 \cdot y_0^2 + b_2 \cdot y_0^4 + b_3 \cdot x_0^2 + b_4 \cdot x_0^2 \cdot y_0^2 + b_5 \cdot x_0^4$

The coefficients were calibrated using a non-linear regression algorithm using the simulation data.

##### Real and Calculated Values

Choosing a matrix of coordinates $x$ and $y$ in a 5 mm square representing positing where the beam would pass, a corresponding matrix of the points seen by the algorithm is shown in Figure 13. 

![](/img/groups/dig/beam_pos_calc/5_2.png) ![](/img/groups/dig/beam_pos_calc/5_3.png)

**Figure 13**: Real and calculated coordinates for the Partial Delta/Sigma (5 iterations) Method.

##### Contour Plot Inaccuracy

A contour plot was made to show the inaccuracy variation on the considered area, as seen on Figure 14. The result was based on the difference between the distances to the origin, according to the following equation:

${Inaccuracy = \sqrt{(x')^2 + (y')^2} - \sqrt{x^2 + y^2}}$

Considering $x$ and $y$ as the real positions and $x'$ and $y'$ as the calculated ones.

![](/img/groups/dig/beam_pos_calc/5_4.png)