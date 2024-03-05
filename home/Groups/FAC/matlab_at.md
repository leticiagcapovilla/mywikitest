---
title: Matlab Accelerator Toolbox
description: 
published: 1
date: 2024-03-05T13:48:08.300Z
tags: 
editor: markdown
dateCreated: 2024-03-05T13:48:08.300Z
---

# FAC:Matlab Accelerator Toolbox

Accelerator Toolbox (AT) is a Matlab package [developed at SLAC](http://www.slac.stanford.edu/pubs/slacpubs/8000/slac-pub-8732.html) that implements a number of functions (scripts) that help in modeling elements, calculating optics in transport lines and storage rings and performing tracking simulations. A non-exhaustive list with help for available scripts can be obtained with the command `athelp`. Since AT is composed of a very large number of scripts there is no single document that describes every of its functionalities. The best documentation happens to be the source code of the scripts, which can looked at with matlab editor.

AT scripts are grouped in three basic categories:

1. *Passmethods*: a set of files implementing tracking transfer maps for all defined element types. These are files written in C which are located in the subfolders 

`<ROOT>/MatlabMiddleLayer/Release/at/simulator/element/`
`<ROOT>/MatlabMiddleLayer/Release/at/simulator/element/user/`

and can be compiled using the script `atmexall`. A list of all available `passmethods` can be obtained with the command passmethods. Up to now the complete list of implemented passmethods is as follows: 

```
-- passmethods used for Sirius --

IdentityPass                   StrMPoleSymplectic4Pass   StrMPoleSymplectic4RadPass
DriftPass                      BndMPoleSymplectic4Pass   BndMPoleSymplectic4RadPass 
CavityPass                     CorrectorPass             LNLSThickEPUPass 

-- other passmethods --

AperturePass                    BendLinearPass           EAperturePass
FFQuadLinearPass                Matrix66Pass             QuadLinearPass
ThinMPolePass                   BL11WolskiPass           FastKickerPass
SolenoidLinearPass              GWigSymplecticPass       LNLSThinEPUPass
Matrix66Pass                    SRotationPass            WigSymplectic4Pass
StrCorrMPoleSymplectic4Pass     TaylormapPass            TaylormapPass2
StrCorrMPoleSymplectic4RadPass  TaylormapPass3           ThinEPUPass              
ThinMPoleBendPass
```

2. *Lattice Tools*: group of scripts that are used to create and manipulate lattices (transport lines or storage rings). A lattice in AT is a Matlab cell array structure, one component for each element in the lattice. Many of AT scripts manipulate implicitly a special global variable called `THERING` which should contain the model of the lattice. In order to access an element of this structure the workspace first has to be informed that this global variable is to be used: 

```
sirius;          % loads current Sirius lattice model
global THERING;  % enable access to global cell array with the lattice
THERING{1}       % prints data on the first element of the model
```

In order to list all elements in the lattice with its main parameters `printlattice` may be used. A very useful function in this group, for example, is `findcells`. It is used to search for elements in the model that contains specific data: 

```
lnls1;           % loads current UVX lattice model (a listbox window opens for selection of connection type) 
global THERING;  % enable access to global cell array with the lattice
bpms = findcells(THERING, 'FamName', 'BPM');  % returns a vector with indices of all elements whose familyname field is 'BPM'of the model
```
Other commonly used scripts are `getcellstruct` and `setcellstruct` which are used to get and set properties of sets of elements at a time. Here is the complete list of scripts in `<ROOT>/MatlabMiddleLayer/Release/at/lattice/`: 

```
atelem.m                 getcellstruct.m      readmad.m                setshift.m
atindex.m                insertelem0.m        readmad_old.m            settags.m
atparamgroup.m           insertindrift.m      restoreparamgroup.m      settilt.m
buildlat.m               isatelem.m           reverse.m                splitdrift.m
combinebypassmethod.m    isatlattice.m        rmelem0.m                splitelem.m
combinelinear45.m        mergedrift.m         saveparamgroup.m
findcells.m              mkparamgroup.m       setcellstruct.m
findtags.m               mvelem.m             setparamgroup.m
```

3. *Physics Tools*: group of scripts used for calculations of various beam dynamics parameters: closed orbits, transfer matrices, Twiss and equilibrium parameters, tune and chromaticity fittings and so on. A script called `calctwiss` was written that returns Twiss functions around the storage ring. Another very important script is `atsummary`: it calculates most of the relevant equilibrium beam parameters of the ring. For example, 

```
sirius;
r = calctwiss;
figure; plot(r.pos, r.betax) % plots betax function
disp(r.mux/2/pi)             % prints horizontal tune
ats = atsummary;             % calcs (revTime,revFreq,chromaticities,compactionFactor,dampings,naturalEnergySpread,bunchlength,...)
disp(ats)                    % prints structure with all parameters
```

The complete list of scripts to calculate physical parameters of the beam dynamics is as follows: 

```
cavityoff.m                 findorbit.m                 ohmienvelope.m
cavityon.m                  findrespm.m                 plotbeta.m
findelemaddiffmatrix.m      findspos.m                  plotcod.m
findelemm44.m               findsyncorbit.m             radiationoff.m
findelemm66.m               findthickmpoleraddiffm.m    radiationon.m
findelemraddiffmatrix.m     findthinmpoleraddiffm.m     thickmpoleraddiffm.m
findelemraddiffm.m          fitchrom2.m                 thinmpoleraddiffm.m
findm44.m                   fittune2.m                  tunechrom.m
findm66line.m               intfft.m                    tunespaceplot.m
findm66.m                   linopt.m                    twissline.m
findmpoleraddiffmatrix.m    mcf.m                       twissring.m
findorbit4.m                mkSRotationMatrix.m
findorbit6.m                numdifparams.m

```