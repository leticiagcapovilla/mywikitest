---
title: Beam 2
description: 
published: 1
date: 2024-02-29T14:16:28.261Z
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