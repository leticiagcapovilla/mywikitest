---
title: Beam Diagnostics and Feedback System
description: 
published: 1
date: 2024-02-29T15:27:55.307Z
tags: 
editor: markdown
dateCreated: 2024-02-28T20:27:15.655Z
---

# Machine: Beam Diagnostics and Feedback System

Beam diagnostics and feedback systems are essential in synchrotron light sources to monitor and control a variety of electron and photon beam parameters. Adequate diagnostics helps to reduce the light source commissioning time and is fundamental to provide a high level of reliability to the accelerators. Feedback systems, in turn, improve the machine performance thus improving the photon beam quality delivered to the light source users.


## Diagnostic Devices

Table 1 summarizes the diagnostic devices planned for the accelerators and transport lines.

|Device| SR| TS| Booster| TB| Linac |
| --- | --- | --- | --- | --- | --- |
|Stripline| 				5 |
|Faraday cup| 				1 |
|Fast current transformer| 	1| 	1| 1 |
|Integrating current transformer| 	2| 	2| 2 |
|DC current transformer| 2| 	1| 	 |
|Fluorescent screen| 	5| 4| 5| 5 |
|Energy slit| 			1|  |
|RF BPM – single pass| 	5| 	5| 5 |
|RF BPM – TBT & stored beam| 160| 	50| 	 |
|Photon BPM (dipole)| 40| 			 |
|Photon BPM (IDs)| 40| 			 |
|Filling pattern monitor| 1| 			 |
|Tune monitor stripline (driver)| 2| 	1| 	 |
|Tune monitor stripline (pick up)| 2| 	1| 	 |
|X-ray ports for pinhole camera| 2| 			 |
|Visible radiation ports| 2| 	1| 	 |
|Streak-camera| 1| 			 |
|Beam loss monitors| 40| 			 |
|Beam scrapers (H/V)| 1/1| 			 |
|Transverse feedback driver| 2| 			 |
|Transverse feedback pick-up| 1| 			 |
|Pinger magnet (H/V)| 1/1| 			 |				

The Linac diagnostics listed above are preliminary and may vary depending on the chosen external supplier. 

### RF BPMs

#### Button BPM Pick-ups

Storage ring and booster RF BPMs will use button pick-ups.

#### Stripline BPM Pick-ups

The pulsed RF-BPMs (single-pass) for Linac and transport lines will use stripline pick-ups.

#### BPM Electronics

The RF BPM electronics has been developed in-house. It consists of a beam-synchronous digital RF receiver with additional digital signal processing providing capabilities such as slow bean position monitoring (10 Hz data rate), turn-by-turn data acquisition, few microns long-term (one week) stability, sub-100 nm resolution (0.1 Hz to 1 kHz integration bandwidth), real-time low latency accelerator-wide data distribution for orbit feedbacks, triggered data acquisition, orbit interlock and fully reconfigurable digital signal processing chains in FPGA. 

Figure 1 gives an overview of the electronics main components.

![](/img/machine/beam_diag_feedback_sys/Sirius_bpm_electronics_block_diagram.png)

**Figure 1**: Overview of Sirius RF-BPM electronics hardware.

The main performance goals are given in Figure 2.

| Parameter | Value | Unit |
| --- | --- | --- |
|Resolution (RMS) @ 0.1 Hz to 1 kHz| 80| nm |
|Resolution (RMS) @ turn-by-turn full bandwidth| 3| µm |
|1 hour position stability (RMS)| 140| nm |
|1 week stability (RMS)| 5| µm |
|Beam current dependence (decay mode)| 1| µm |
|Beam current dependence (top-up mode)| 140| nm |
|Filling pattern dependence| 5| µm |
|First-turn resolution (RMS)| 500| µm |
|Horizontal/Vertical plane coupling| 1| % |

##### Hardware

Due to its hardware modularity, different variants of the RF BPM electronics could be obtained by redesigning the RF front-end and keeping the FPGA and digitizer boards. For instance, single-pass BPM electronics for Linac and transport lines and lower cost BPM electronics for the booster would require redesigning the digitizer module and possibly eliminating the need of a separate RF front-end.

##### Firmware

See also: [[DIG:Beam Position Calculation|Beam Position Calculation]]

The core digital signal processing of the RF BPM electronics is shown in Figure 2. Amplitude and phase information of the RF signal coming from each BPM antenna is downconverted from the intermediate frequency, produced on the sampling process, to baseband.

![](/img/machine/beam_diag_feedback_sys/Sirius_rfbpm_ddc.svg)

**Figure 2**: RF-BPM digital downconversion chain.

Considering all [[Beam Position Calculation|beam position calculation algorithms]] studied, the Partial Delta/Sigma as chosen as the default due to its acceptable accuracy, cheap cost of processing and mathematical cancellation of the equipment line gain.

##### Software

##### Integration with Accelerator Systems

### Photon BPMs

The installation of two blade photon BPMs, 7 meters apart one from the other, in every high field dipole front-end is foreseen. Special care will be taken to support these monitors in a robust and stable way. For soft X-ray beamlines, photoemission BPMs could also be employed, although a recent development carried out by NSLS-2 will be evaluated, where diamond blades with thin metal coating give the possibility of selecting a smaller portion of the beam spectrum thus reducing the background contamination effects.

The strategy for monitoring the photon beam positions at the insertion devices front-ends was defined. Experience from several light sources shows that the systematic errors cannot be reduced more than about 20 µm. Fluorescent based X-ray BPMs used in some accelerators, SSRL for instance, were recently improved and tested at APS and minimize the errors caused by background photons. The new concept is called GRID XBPM (GRazing Incident Insertion Device XBPM) and combines the functionalities of front-end photon masks and XBPMs. In-vacuum undulators front-ends will count on XBPMs based on this device. The use of X-ray area detectors instead of the traditional pin diodes can provide real imaging of the beam footprint and this proposal has been evaluated by the LNLS Detectors Group.

## Feedback Systems

### Fast Orbit Feedback

Closed-orbit control has a twofold role of keeping the electron beam at its nominal path and stabilizing the photon beam pointing angle at source points. The storage ring orbit control system will be decomposed in two feedback systems covering complementary frequency ranges. The Slow Orbit Feedback (SOFB) will make use of strong orbit correctors and RF frequency changes to correct orbit disturbances caused by magnets misalignment, ground motion and temperature variation. The Fast Orbit Feedback (FOFB) will employ dedicated fast orbit correctors and control hardware to tightly stabilize position and pointing angle of photon beams, attenuating fast disturbances caused by magnet vibrations, magnet power supplies ripple, stray fields during booster cycling and dynamic insertion devices reconfiguration. Both systems will use the same set of BPM readings and will be coordinated to avoid saturation of the fast correctors.

Table 3 gives the orbit stability performance target to be achieved with FOFB as well as requirements on the most critical subsystems.

| Parameter | Value | Unit |
| --- | --- | --- |
|Beam position integrated RMS (from 0.1 to 1 kHz)| 5|  % beam size |
|Disturbance rejection 0 dB crossover frequency| > 1| kHz |
|Overall closed-loop latency| < 75| μs |
|Fast orbit corrector -3dB bandwidth (small signal)| > 10| kHz  |

The fast orbit correctors will be located over stainless steel 0.3 mm orbit corrector vacuum chamber providing -3 dB bandwidth above 10 kHz. The design of the fast dipole magnet and power supply will exploit the entire bandwidth provided by the vacuum chamber for small signals.

The fundamental limiting factor of closed-loop latency was found to be the accelerator-wide sensors and actuators data distribution. Detailed calculations has shown that the use of multigigabit communication through FPGAs and efficient network topologies allows a theoretical minimum latency of approximately 5.3 μs, out of which approximately 2.5 μs would come from light propagation through several optical fibers along half storage ring circumference. The calculations considered data packet overheads such as frame headers and checksums as well as FPGA logic pipeline delay and a factor of 2 for fiber lengths. The BPM latency, typically dominated by decimation filters group delay, should be ideally made comparable to the data distribution latency so as to not dominate the latency. A preliminary performance goal of 10 μs BPM group delay has been considered, requiring a FOFB update rate of the order of 100 kHz.

Figure 3 shows the general BPM, orbit correctors and skew quadrupoles layout in the storage ring arc. Concerning the FOFB system, four fast orbit correctors per plane are employed to allow stabilization of photon beam position and pointing angle at all ID and high field dipole source points. BPMs at both ends of the straight sections, not shown in the diagram, will be installed concomitantly with the installation of new IDs to provide direct estimation of photon beam pointing angle on IDs.

![](/img/machine/beam_diag_feedback_sys/SI_arc_with_correctors.png)

**Figure 3**: Distribution of corrector magnets and BPMs for the global and local closed-orbit correction system. Skew quadrupoles (QS) are implemented as additional coil windings in the sextupole families SFA0, SDB0, SDP0, SDx2(C1), SDx3(C3) while slow horizontal and vertical orbit correctors (CH and CV) are implemented in SDA0, SFB0, SFP0, SDx1, SFx2 and SDA0, SFB0, SFP0, SDx1, SDx3, SFx2(C3) families respectively. An additional skew corrector QS is implemented as an extra coil in the fast corrector next to BC, and a stand-alone vertical corrector CV is placed before dipole BC. Fast correctors (FCH and FCV) are located at special sections with 0.3 mm thick stainless steel vacuum chambers.

#### Photon BPMs in the loop

Besides the RF-BPMs used for the slow and fast orbit correction loops, effort has been made to allow the integration of photon BPM readings in the feedback loop with compatible data rate, latency and communication interface.

### Fast Coupling Feedback

### Bunch-by-bunch Feedback

Even though the impedance of the machine components has been systematically studied and optimized, beam instabilities are expected to limit the maximum achievable beam current at unacceptable levels. Therefore bunch-by-bunch feedback systems for the transverse and longitudinal planes are essential to improve the machine performance. Figure 4 shows the proposed transverse bunch-by-bunch feedback topology, which is similar to the scheme adopted for the LNLS UVX storage ring.

![](/img/machine/beam_diag_feedback_sys/bbb_diagram.png)

**Figure 4**: Bunch-by-bunch feedback system general topology.

Stripline or button BPMs can be used as sensors. The monopulse comparator consists of a set of hybrid circuits that generate position error signals and should embed phase-trimmed cables and wideband hybrids around the third RF harmonic, where the position sensitivity is usually maximized. The front-end is essentially a demodulator unit which receives the position error signals modulated around the third harmonic, provides gain and proceeds with analog down-conversion. The baseband error signal produced by this element must present a flat top pulse, minimizing the effects of clock jitter on the digitizer side and the effect of beam phase oscillations.

The processor is the core of the system and determines the capabilities for bunch-by-bunch feedback, bunch-cleaning and diagnostics. Its interface to the control system is also very important, making commissioning and routine operations smoother. Delay lines can be external or part of the processor assembly, being crucial for matching the correction signal to the bunch arrival. Typically a resolution of 10 ps is enough. The broadband RF amplifier is also a critical component since it should provide linear frequency response within the bandwidth of interest. A second characteristic is related to the bandwidth – although bunch-by-bunch feedback demands a maximum bandwidth of 250 MHz for 500 MHz machines (from first revolution harmonic to ($f_{RF}/2$), a wider bandwidth is recommended (400 MHz) in order to ensure bunch-to-bunch isolation for bunch-cleaning operations, especially when only few bunches are excited at the same time. Similarly, in case a significant number of bunches are excited contiguously, the lower cutoff frequency for the system’s bandwidth needs to be the lowest possible (~10 KHz) in order to preserve the DC content of the excitation signal, minimizing the signal contamination in the bunches to be preserved/controlled.

The transverse system implemented in LNLS UVX storage ring is based on Instrumentation Technologies processors. Dimtel’s iGP processor for controlling longitudinal instabilities were also evaluate at UVX storage ring. Based on the experience with these two commercial systems, a decision in favor of Dimtel was taken, since important differences between the systems were observed during tests.
