---
title: Beam 2
description: 
published: 1
date: 2024-02-29T14:17:12.637Z
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
