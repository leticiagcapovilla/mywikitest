---
title: Log
description: 
published: 1
date: 2024-02-29T16:24:11.105Z
tags: 
editor: markdown
dateCreated: 2024-02-28T20:58:00.258Z
---

# FAC: Log

* 2015-10-30

    * update Sirius wiki with fieldmap analysis of Q14,Q20,Q30 and BC_model5
    * generate AT survey of SI.V13 and compare it with AutoCAD drawing
        * generalize lnls_build_ref_orbit to accept both an origin and a rotation angle
        * rotation of the storage ring is such that the injection straight line makes a 23 degree angle with the EAST-EST line.

* 2015-10-29

    * running dynapt calcs for SI.V13 (after nominal quadrupole models with systematic multipoles)
    * running dynapt calcs for SI.V13 (before nominal quadrupole models with systematic multipoles)
    * ~~moved systematic multipoles of quadrupoles from sirius_si_systematic_multipoles.m to the nominal model in sirius_si_lattice.m for SI.V13~~

* 2015-10-28

    * We will optimize SI.V13 with MOGA
    * ~~reduced number of significant digits in lengths for SI.V13~~
    * ~~SI.V12-C2-BC5 hasn been renamed to SI.V13~~
    * finalize implementation of the AT model for TS.V02 (initial version at lnls82)
    * ~~running dynamical aperture calculations for new SI.V12-C2-BC5 model~~
    	* ~~dynapt got a bit smaller than for SI.V12~~
    * run dynamical aperture calculations for new BO.V02B model

* 2015-10-27

    * ~~Create BO lattice with new dipole segmented model (XRR)~~ 
    * Reduce number of significant digits in lengths for all lattice models (XRR)
    	* ~~SI.V13~~
    * SI injection study (go back to it) (XRR)
    * Update TS lattice model with segmented dipole model (XRR)
    	* ~~Field map analysed and sent to Liu~~
      	* ~~waiting for Priscila to send fieldmap file for analysis (XRR)~~
        

* 2015-10-26

    *  ~~Created SI lattice with BC model 5 (XRR)~~
    	* ~~dynamical aperture calculations are running (with sextupoles on)~~
		* ~~Analysis of BO dipole used in TS with nominal deflection angle of 5.3333 degrees (new RK traj) (XRR)~~
    		* ~~the idea is to look at effects of multipoles around the TS RK trajectory on transport efficiency~~
        	* ~~had to reduce field strength of the BO excitation by a factor of 0.7399 to get to correct nominal deflection for the transport lin~~
    * File sirius_si_multipole_systematic_errors.m has to be updated with lastest Q14, Q20 and Q30 models. (XRR)
    * ~~Analysis of new model 5 fieldmap for BC (XRR)~~
    	* ~~analysis data sent to Liu for the creation of segmented model~~
        
* 2015-10-23

    * ~~Updated hardedge lengths for sextupoles in sirius_si_lattice_bc_model3. (XRR)~~ 
    	* ~~this model may be overseeded by model 5~~