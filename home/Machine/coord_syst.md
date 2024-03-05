---
title: Coordinate System and Conventions
description: 
published: 1
date: 2024-03-05T15:41:30.312Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:12.126Z
---

# Machine: Coordinate System and Conventions

<br />

## Machine Coordinate System

The stored electrons in Sirius will be circulating in clockwise direction (as seen from the top). The motion of an electron is described in terms of coordinates related to the machine ideal orbit. Any position is specified in an orthogonal, right-handed coordinate system $(x,y, z)$ that follows the ideal particle traveling along the ideal path. $s$ is the coordinate along the ideal orbit and $\hat{s}$ points in the direction of the particle velocity, that is tangent to the ideal orbit. The transverse coordinates $x$ and $y$ measure the horizontal and vertical deviations from the ideal orbit, with $\hat{x}$ pointing to the outside of the ring and $\hat{y}$ pointing upward. See Figure 1. The vectorial cross product $\hat{s} = \hat{x} \times \hat{y}$ holds.

The direction of $B_y$ for different kinds of magnets in the Sirius coordinate system are shown in Figure 2, where the term 'focusing' refers, by convention, to the plane of the orbit. The direction of the electron velocity is given by $\hat{s}$.

![](/img/machine/coord_systs_and_conventions/ideal_orbit.svg)

**Figure 1**: Coordinate system for Sirius. Top view.

![](/img/machine/coord_systs_and_conventions/magnets_direction.svg)

**Figure 2**: $B_y$ direction for different kinds of magnets for electrons circulating clockwise. $\hat{x}$ points to the outside of the storage ring.

<br />

## BPM Coordinate System

![](/img/machine/coord_systs_and_conventions/45bpm_coord.png)

**Figure 3**: 45 degree Rotated BPM Coordinate System.

![](/img/machine/coord_systs_and_conventions/crossbpm_coord.png)

**Figure 4**: Cross BPM Coordinate System.      

The Beam Position Monitors Coordinate System is as shown on Figure 3. The antennas A, B, C and D are displayed, along with the beam direction (going outside of the figure). For further information, see [DIG:Beam Position Calculation.](/home/Groups/DIG/beam_position_calc)

| | Direction | Origin | + |
| --- | --- | --- | --- |
| x-axis | Horizontal, perpendicular to beam prolongation | Centre of beam | To the left, outward the storage ring |
| y-axis | Vertical, perpendicular to beam prolongation | Centre of beam | Upwards 

<br />

## Beamline Coordinate System

![](img/beamline_coord.png)

**Figure 5**: Beamline coordinate system and rotation around axis.    

| | Direction | Origin | + | Rotation around the axis |
| --- | --- | --- | --- | --- |
| z-axis | along beam propagation | source point | in the beam direction | roll |
| x-axis | horizontal, perpendicular to beam prolongation | center of beam | to the left, outward, opposite to storage ring | pitch (equal to Bragg rotation) |
| y-axis | vertical, perpendicular to beam prolongation | floor of experimental hall | upwards | yaw 