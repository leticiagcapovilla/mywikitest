---
title: High Level Applications Visual Style Guide
description: 
published: 1
date: 2024-03-05T21:39:20.590Z
tags: 
editor: markdown
dateCreated: 2024-03-05T21:32:40.665Z
---

# Machine: High Level Applications Visual Style Guide

The visual style guide for Sirius defines guidelines for building graphical user interfaces.
Colours and Fonts

For CS-Studio screens, two files have been created for default colours and fonts. They are located in the project sirius/opi/common in the hla repository. Follow the instructions for configuring CS-Studio given in the High Level Applications and Virtual Accelerator page to set them as default.
Monitoring Screens

CS-Studio will be used for monitoring screens. We are assuming a 1920x1080 resolution for the monitors that will be used for displaying the monitoring screens, and two screens per monitor. The space needed by CS-Studio for menus, tabs, and separators must also be taken into account.

Figure 1 shows a monitoring screen for general light source status. It illustrates some of the proposed standards for a uniform visual presentation:

* Screen size: 940×1000 (width×height)
* Screen title: centralised at the top; first element under it at Y=70
* Screen border spacing: at least 10 from left and right borders
* Containers:
  * Border Style: Ridged Style
  * Border Width: 1
  * Title: at X=0, Y=10
  * Separation: 10 (horizontal and vertical)
  * Label alignment: right aligned
  * Value alignment: left aligned
* Graphs:
  * X-axis and -scale: black
  * Y-axis and -scale: black if only one trace; use colours to distinguish otherwise
* Colours (defined in colours.def): when available, use one of the predefined colours (for orbit plots, for example)
* Fonts (defined in fonts.def):
  * Title: Monitor Title
  * Container header: Monitor Header
  * Regular text: Monitor Data
  * Graph axis text: Monitor Graph Axis
  * Graph scale text: Monitor Graph Scale

 ![](/img/machine/hla_visual_guide/hla_opi_light_source_status.png)