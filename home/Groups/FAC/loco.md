# FAC: LOCO

[LOCO](http://accelconf.web.cern.ch/AccelConf/e02/PAPERS/WEPLE003.pdf), or Linear Optics from Closed Orbit, is a set of tools that aims at calibrating a given lattice model from closed orbit measurements in an storage ring. Currently it is implemented in Matlab using both MML and AT toolkits. Since its first applications in 2002 it has been applied to most existing storage rings and it has become a standard tool to calibrate the model of linear beam dynamics.

For a given lattice model, LOCO searches for effective quadrupolar strengths in the model and gains and cross-talks of bpms and orbit correctors in the real machine that produce the best match of dispersion functions and orbit response matrix between the model and the measurements. Quadrupolar strengths can be fitted for each individual magnet or for families. Bpm fluctuations are also measured and used to normalize the residual function. It is also possible to configure the model so that other parameters may be fitted as well: feed-down quadrupoles due to orbit-offsets at sextupoles, skew quadrupoles, etc.

At the LNLS UVX storage ring, the whole cycle of measurement and LOCO analysis is the iteration of the following steps (using MML):

* loading LNLS UVX paths, MML structures and machine connection: `lnls1`

* measurement of bpm fluctuations: `lnls1_monbpm`

* measurement of dispersion functions: `lnls1_measdisp`

* measurement of orbit response matrix: `lnls1_bpmresp`

* configuring the AT model to be calibrated (usually global variable `THERING`) can be used.

* building LOCO input file: `buillocoinput`

* use LOCO GUI to control the fitting algorithm: `locogui`