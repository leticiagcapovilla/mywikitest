# FAC:Low-alpha optics mode

The idea in this optics mode is to generate a very short beam for terahertz experiments. This is accomplished by reducing the linear compaction factor $\alpha _{1}$ as much as possible. 

## Linear optics model calibration

Model calibration is performed with [LOCO](/home/leticia/Documents/GPP/WikiSirius/sirius_page/docs/machine_page/Groups/FAC/loco.md) algorithm.

## Chromaticities and second-order momentum compaction factor measurements

Measurement of transverse chromaticities and second-order momentum compaction factor is performed by varying the RF frequency $f_{RF}$ and registering the horizontal $f_x$, vertical $f_y$ and longitudinal $f_s$ betatron frequencies. Transverse frequencies are measured using the spectral analyzer and the longitudinal frequency is measured with the bunch-by-bunch feedback system. These measured quantities are dependent on the RF frequency according to the following expressions:

$\frac{\nu_s}{\nu_{s,0}} = \left\{ 1 - \frac{4 \alpha_2}{\alpha_1^2} \left(\frac{\delta f}{f}\right)_{RF}\right\}^{1/4}$

$\xi_x \equiv \frac{\delta\nu_x}{\delta\epsilon} = \frac{\delta}{\delta\epsilon}\left(\frac{f_x}{f_{rev}}\right)$

$\xi_y \equiv \frac{\delta\nu_y}{\delta\epsilon} = \frac{\delta}{\delta\epsilon}\left(\frac{f_y}{f_{rev}}\right)$

As the RF frequency is varied the beam has its energy changed by the quantity $\delta\epsilon$ so that it retains the correct synchronous phase:

$-\left(\frac{\delta f}{f}\right)_{RF} = \frac{\delta L}{L} = \alpha_1 {\delta\epsilon} + \alpha_2 {\delta\epsilon}^2$

The second-order momentum compaction factor $\alpha_2$ is obtained from linear fitting and from the $\alpha_1$ value extracted from the LOCO-calibrated model of the low-alpha optics. These two parameters are then used to calculate the beam energy variation $\delta\epsilon$ which is used to estimate the chromaticities $\xi_x$ and $\xi_y$ from linear fitting of the tune curves.
Below are the measurement data

| $\delta f_{rf} [Hz]$ | $\delta f_x [kHz]$ | $\delta f_y [kHz]$ | $\delta f_s [kHz]$ |
| --- | --- | --- | --- |
| -100 |270.5 |120.5 |5.30|
| -90 | 271.5 | -- | --|
| -80 | 272.5 | 120.5 | 5.30|
| -70 | 273.5 | --  | --|
| -60 | 274.5 | 117.5 | 5.37|
| -50 | 275.5 | 115.5 | 5.34|
| -40 | 275.5 | 114.5 | 5.41|
| -30 | 276.6 | 115.5 | 5.45|
| -20 | 276.6 | 114.5 | 5.45|
| -10 | 277.6 | 114.5 | 5.49|
| +0 | 277.6 | 112.4 | 5.49|
| +20 | 278.6 | 110.4 | 5.60|
| +40 | 280.6 | 108.4 | 5.64|
| +60 | 281.6 | 109.4 | 5.68|
| +80 | 283.6 | 106.4 | 5.71|
| +100 | 284.7 | 104.3 | 5.75|
| +120 | 286.7 | 100.3 | 5.79 |

**Table 1**: 2014-07-14 Low-alpha and chromaticities measurement.

Betatron frequency shifts from initial values of $f_x$ = 635 kHz and $f_y = 540 kHz$ are recorded w.r.t. a marker of the spectrum analyzer which is fixed at the 37$^{th}$ harmonic of revolution frequency $(f_{rev} = 3.216667 MHz)$ for the initial RF frequency of 476.06678 MHz. The harmonic number of the UVX ring is 148. Fitting the data above to the given analytical expressions yields

| $Parameter$ | $Value$ |
| --- | --- |
| $\alpha_1$ | $3.35 \times 10^{-4}$|
| $\alpha_2$ | $(-2.47 \pm 0.02) \times 10^{-2}$|
| $\xi_x$ | $-3.4 \pm 0.1$|
| $\xi_y$ | $+4.2 \pm 0.1$|

**Table 2**: Low-alpha fitted parameters

![](/img/groups/fac/Low-alpha_measurements.png)

**Figure 1**: Low-alpha second-order compaction factor and chromaticities measurements of 2014-07-14.