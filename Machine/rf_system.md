---
title: RF System
description: 
published: 1
date: 2024-03-14T17:48:49.588Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:45.041Z
---

# Machine: RF System

The RF system is responsible for supplying energy to the electrons during the acceleration process and replenishing the energy lost due to the emission of synchrotron radiation  or to other dissipative processes. The electrons gain energy from electric fields excited in special components of the RF system called accelerating structures and resonant cavities. The main role of the RF systems is to excite and maintain these accelerating fields in line with the stability requirements of the three machines that make up the light source. Linac, booster and storage ring each have their dedicated RF system, designed to meet the specifications required by electron beam dynamics for each of these main components of the light source. The linac is being purchased turn-key from SSRF/SINAP and no development is being pursued in house for any part of its RF system. The RF systems for the booster and for the storage ring are being designed in house and the main specifications of both systems are presented below.

<br />

## Introduction

In a nutshell, RF systems consist of one or more accelerating cavities, low power RF controls, waveguide systems, a main RF generator and signal amplification networks that culminate in a set of high power amplifiers able to deliver enough power to cope with the demands of beam dynamics. In addition, support systems are usually necessary to supply the appropriate infrastructure required by some elements of the RF system. For Sirius, each cavity will have its own dedicated set of amplifiers, waveguides and low level RF controls and the whole ensemble will be henceforth addressed as an RF plant.

A single RF plant will be sufficient to meet the requirements for the booster synchrotron. A single 5-cell normal conducting (NC) cavity will suffice to deliver the required gap voltage. For the storage ring, two possibilities are being considered. The required gap voltage can be achieved either by using two superconducting (SC) RF cavities or six room temperature (NC) RF copper cavities. Both the booster and storage ring RF plants will be driven by high power solid state amplifiers. The strategic decision concerning the RF systems for Sirius is to purchase the RF cavities and to produce in house the high power amplifiers. An analogue low level RF (LLRF) is being produced for the booster and studies are still under way concerning the system for the storage ring. The booster and storage ring RF systems will operate at 500 MHz and the main reason for that is the availability of RF cavities that can be commercially supplied at this frequency. The storage ring high power solid state amplifiers will be designed to deliver a maximum of 60 kW output power at the operation frequency. By combining the output power of two or more amplifiers the required power for the storage ring system can be achieved. The SC RF plants will require four amplifiers per plant in order to supply enough power for the operation of the machine at the designed current. In this case each NC RF plant will require two high power amplifiers per plant.

The RF system has to be carefully designed since it may be a serious source of instabilities for the electron beam. The higher order resonant modes (HOM) of the RF cavities may be particularly harmful if not efficiently dealt with. HOM may excite longitudinal and transverse beam instabilities that can limit the maximum stored current or result in beam oscillations that lead to a much higher effective emittance. The efficient damping of such undesirable modes is the main reason why superconducting (SC) cavities would be the preferred choice for Sirius. SC cavities are operating with great success in most of the recently built 3rd generation light sources. The technology has reached maturity and turn-key systems are available in the market. However, a recently developed HOM damped room temperature cavity is now in operation at ALBA and is being installed in other machines, such as BESSY and ESRF. However, there is no experience with the operation of these cavities at high current although no instabilities have been observed at ALBA for beam currents up to 200 mA.

<br />

## RF System for the Storage Ring

|As the electron travels along the vacuum pipe it loses energy due to the interaction with the electromagnetic environment it finds along its path. Energy is lost both in the form of synchrotron radiation and from the interaction of the electrons with the walls of the vacuum chamber. Sirius has 20 achromatic arcs, each one deflecting the beam by 18 degrees. Except for a 12 cm long short dipole with 1.95 T peak magnetic field in the mid of the arch and which accounts for just about 1° deflection, all the remaining deflection in each 5BA arch is performed by a set of 0.58 T low field dipoles. Even with such low fields the energy loss per turn at the elements of the magnetic lattice dominates, followed by the energy radiated in the insertion devices. The energy loss per turn is about 450 keV in the dipoles and up to 400 keV is being considered for the insertion devices at full capacity. In this scenario, the RF power necessary in order to compensate for the radiation losses is about 85 kW per 100 mA. In the design of the RF system an extra 10% power loss is added in order to account for other energy losses such as HOM and vacuum chamber impedance losses and losses in the RF lines.

<br />

### Major Design Parameters

The design parameters for the RF system consider a maximum beam current of 500 mA and a maximum total accelerating voltage of 3 MV. The choice of the RF cavities has a great impact on the way the RF system will be implemented. In case the choice falls upon the SC cavities the RF system is planned to be implemented in two steps. The initial commissioning of the machine should be preferably performed with room temperature cavities. For the initial phase the RF system should be able to sustain a beam current of 100 mA with a beam lifetime of more than 10 hours. Increasing beam current and beam lifetime requires an upgrade in the available RF power that would be accomplished either by replacing the NC cavities by the SC ones or by installing additional NC cavities to the system, in case the choice falls on the NC cavities. For the commissioning phase at least three cavities should be installed in the storage ring from the the start.

| Parameter | Value | Unit |
| --- | --- | --- |
|Energy | 3.0 | GeV |
|Maximum Beam current | 500 | mA |
|RF frequency | 499.664 | MHz |
|Harmonic number | 864 |  |
|Energy loss/turn from dipoles | 471.01 | keV |
|Energy loss/turn from insertions (estimated) | 400 | keV |
|Total energy loss/turn | 871.01 | keV |
|Synchrotron radiation power from dipoles | 236 | kW |
|Synchrotron radiation power from insertions | 200 | kW |
|Total synchrotron radiation power | 436 | kW |
|Peak RF voltage | 3.0 | MV |
|Overvoltage, q=V/U0 | 3.4 |  |
|Synchronous phase | 163.1 | Â° |
|Synchrotron tune | 0.004652 |  |
|Synchrotron frequency | 2.690 | kHz |
|Momentum compaction factor | 1.6×10-4 |  |
|Natural bunch length | 8.2 | ps |
|RF energy acceptance | 5.13 |  %  |
{.dense}

**Table 1**: Main SI RF System Parameters

<br />

### Specifications

The specifications of the RF system are dictated by the beam stability requirements for the experiments that are planned to be performed by the users in the experimental stations. Under normal conditions the rule of thumb for longitudinal beam oscillation is to keep it within 10% of the RMS bunch length. For each cavity there are active feedback loops to control the amplitude of the accelerating voltage, the resonant frequency of the fundamental mode of the cavity and the relative phase of the RF signal in each cavity. Phase and amplitude jitter beyond certain limits have a negative impact on beam characteristics that may severely restrain the range of applicability of the beamlines by making important experiments unfeasible. Jitter may lead to vertical beam size and effective impedance increase and can be a problem for timing experiments. Phase and momentum jitter can also reduce the brightness of the higher harmonics emitted by the undulators by increasing the vertical divergence of the photon beam. Experiments using infrared radiation in the existing machines are very demanding and point to the need to achieve timing jitter of the order of only 5% of the RMS beam bunch length. Under these circumstances the tolerances for phase and momentum jitter would be:

| Parameter | Value |
| --- | --- |
|Phase Jitter | 0.1° |
|Momentum Jitter (Δp/p) | 5×10⁻⁵ |
{.dense}

For the other beamlines and techniques, such as timing experiments, the tolerances can be more relaxed. In addition, the installation of harmonic cavities to stretch the electron bunches will slack the tolerances even more. For the natural bunch length, which is about 9 ps, the tolerances are still tight but with the harmonic cavities they will not be determined by timing experiments anymore:

| Parameter | Value |
| --- | --- |
|Phase Jitter | 0.5° |
|Momentum Jitter (Δp/p) | 2×10⁻⁴ |
{.dense}

<br />

### RF cavities

There are still two possible options being considered for the storage ring RF cavities. Although there is a strong drive to use SC cavities mostly based on beam stability issues there is on the other hand some concern about the reliability of these systems in long term routine operation. It is known that the experience of some light sources with SC cavities have been quite traumatic, with the RF system responding for considerable increase in machine down time. Otherwise, SC systems seem to be working very well in other facilities even though frequent periodic maintenance seems to be crucial for the reliability of these systems. The impact of the SC cavities when it comes to beam dynamics is very positive with no cavity HOM driven instabilities observed in any of the machines using them. The only normal conducting alternative being considered for Sirius is the HOM damped cavity nicknamed DAMPY, which is being used at ALBA, BESSY and ESRF. ALBA has reached 200 mA during machine studies shifts and no HOM have been observed in the cavities.

In addition to stability considerations there are other aspects that should be taken into account when choosing the cavities, mainly because it is not clear that the normal conducting cavity should be discarded as unfitted based on insufficient HOM damping. Some of the pros and cons of each system, from the viewpoint of LNLS' experience with RF systems, are listed below

**Pros**

|NC System | SC System |
| --- | --- |
|Less expensive to install | Efficient HOM damping |
|Experience with the technology | Demands less RF power |
Smaller number of RF plants  |
{.dense}

**Cons**

|NC System | SC System |
| --- | --- |
|Larger number of RF plants | More expensive to install |
|Demands more RF power | Expensive cryogenic system |
|Larger number of amplifiers | Dedicated cryogenic group |
|Requires large water cooling capacity | Maintenance intensive |
|Larger impact on tunnel temperature control | Expensive spare cavity  |
{.dense}

**?**

|NC System | SC System |
| --- | --- |
|Sufficient HOM damping | May require longer shutdowns |
|May need feedback |  |
{.dense}

The main advantages of the SC system are the reduced number of RF plants and high power amplifiers needed to run the system, and the great beam dynamics performance due to the efficient suppression of beam driven higher order modes (HOM) that can be achieved in the SC cavities. The high shunt impedance of these cavities minimizes the number of necessary RF plants leading to an overall simplification of the RF system. However, the SC system is more expensive than the NC one, requiring a cryogenic infrastructure that is at the same time also expensive and complex. The initial investment required for the installation of the SC system is much higher than the one required for the NC system. The DAMPY cavity also features an efficient suppression of the HOM and it is much less expensive. However these cavities have much lower shunt impedance and many of them are needed to establish the necessary total gap voltage, each one requiring its own RF plant, which is also an expensive component of the system. In the case of SC cavities only two RF plants are necessary to supply the RF power required to maintain the beam stored in the machine. In its final configuration the output power of each RF plant will be the combination the output power of four solid state amplifiers. On the other hand, a NC system with six DAMPY cavities will require a total of six RF plants, although each plant will include the combination of just two solid state amplifiers. In both cases the RF system will be able to maintain the nominal beam current of 350 mA.

In the current scenario there are two alternative paths that could be pursued depending on the technology chosen for the cavities. For each option a different approach can be adopted for the installation of the cavities. If the decision falls on the SC cavities there is a possibility of starting the commissioning of the machine either with three normal conducting cavities or with the two SC cavities. There are two main reasons for not having the SC cavities operating from the outset. First of all, it would leave more time for analysis, specification and installation of the cryogenic and SC cavity systems. Most importantly however, that would reduce the risks of contaminating the cryogenic surface of the cavities during the vacuum chamber clean up period. Commissioning periods are always more prone to accidents and it would be safer to operate the machine with NC cavities during that period. In the early stage of operation each cavity could be driven by a dedicated RF plant with only two high power amplifiers. Subsequently, a shutdown will have to be planned for the installation and tests of the SC or extra NC cavities and auxiliary systems. This is the main disadvantage of using NC cavities for the start up since a quite long shutdown is needed to install the SC cavities and put the whole system to work in a time when the machine is already running.

In order to operate the machine with a NC system at least three cavities have to be used in commissioning and the initial operation stage of Sirius. Taking the DAMPY cavity for reference, each single cell cavity is designed to run at a gap voltage up to 0.6 MV so that the total accelerating voltage should be limited to 1.8 MV. The main drawback of operating at lower gap voltage is the reduction of beam lifetime it entails. For a total accelerating voltage of 1.8 MV the beam lifetime will be just about 7 hours for 100 mA, considering 230 keV for the energy lost in the IDs and without taking into account any bunch lengthening. Each cavity will be driven by a dedicated RF plant, each one including two high power amplifiers, which means that 6 solid state amplifiers must be available by the time the commissioning of the storage ring starts. In fact, the full output power of one amplifier is needed just to excite the 600 kV in each cavity.

The table below shows the minimum requirements for each of the two systems for starting the commissioning and first operation of Sirius in a safe condition, without pushing the RF cavities to higher than normal gap voltages. That corresponds to a Phase 1 of the RF system installation. For the SC system the machine would be able to operate at the nominal gap voltage from the start but a gradual increase in the gap voltage up to the nominal voltage should be preferable. The subsequent phases of RF upgrade correspond to increase in gap voltage, available power and the final installation of a third SC cavity.

According to the cavity type:

| Parameter | Phase1 <br />NC | Phase 1 <br />SC | Phase 2 <br />SC | Phase3 <br />SC | Unit |
| --- | --- | --- | --- | --- | --- |
|Number of cavities | 3 | 2 | 2 | 3 |  |
|Peak RF voltage | 1.8 | 2.5 | 3.0 | 3.0 | MV |
|Peak RF voltage per cavity | 0.6 | 1.25 | 1.5 | 1.0 | MV |
|Energy accecptance | 3.5 | 4.7 | 5.2 | 5.1 |  % |
|Shunt Impedance/cavity | 3.2 | 44500 | 44500 | 44500 | MΩ |
|Energy loss/turn from dipoles | 456 | 456 | 456 | 456 | keV |
|Energy loss/turn from IDs | 230 | 230 | 350 | 400 | keV |
|Number of high power amplifiers | 6 | 4 | 8 | 12 |  |
|Total RF power available | 360 | 240 | 480 | 720 | kW |
|Beam lifetime @100mA (w/o 3HC) | 6 | 11 | 13 | 12 | h |
|Beam lifetime @100mA (with 3HC) | 14 | 18 | 19 | 19 | h |
|Maximum beam current | 200 | 300 | 500 | 600 | mA |
{.dense}

If the decision falls on the NC cavities there is no need to have all six cavities from the start.  It is also possible to start the commissioning with only three RF cavities and add the other cavities as the operation of the machine requires more gap voltage and available RF power. However, to reach the nominal gap voltage it would require an upgrade with the addition of at least two other cavities.

|Number of NC cavities | 3 | 3 | 4 | 5 | 6 | Unit |
| --- | --- | --- | --- | --- | --- | --- |
|Total gap voltage | 1.5 | 1.8 | 2.4 | 3.0 | 3.0 | MV |
|Gap voltage/cavity | 0.5 | 0.6 | 0.6 | 0.6 | 0.5 | MV |
|Energy loss in the dipoles | 456 | 456 | 456 | 456 | 456 | keV |
|Energy loss in the IDs | 230 | 230 | 230 | 350 | 400 | keV |
|Overvoltage | 2.18 | 2.62 | 3.50 | 3.72 | 3.50 |  |
|Energy acceptance | 2.9 | 3.5 | 4.5 | 5.2 | 5.1 |  % |
|Beam lifetime @ 100 mA (w/o 3HC) | 4 | 6 | 11 | 13 | 13 | h |
|Beam lifetime @ 100 mA (with 3HC) | 11 | 14 | 17 | 19 | 19 | h |
|Number of high power amplifiers | 6 | 6 | 8 | 10 | 12 |  |
|Total RF power available | 360 | 360 | 480 | 600 | 720 | kW |
|Power lost in the cavity walls | 120 | 160 | 220 | 270 | 230 | kW |
|Maximum sustainable beam current | 300 | 200 | 300 | 300 | 450 | mA  |
{.dense}

As already mentioned the beam lifetime with only three NC cavities and without bunch lengthening is just about 7 hours. In order to raise the beam lifetime to more than 10 hours it would be necessary to either install a 3HC or to install an additional cavity (4 NC cavities). Notice that in order to reach 500 mA with NC conducting cavities with a total gap voltage of 3.0 MV would require either the installation of an extra cavity or designing the amplifiers to deliver more RF power, 70 kW for example. With such higher output power it would be possible to reach the design specifications even with five cavities.

<br />

### Superconducting cavity

Currently, we are going to use in the storage ring, since the conditioning phase, two SC cavities CESR type (Figure 1). The Table 2 lists some of the main parameters of this cavity. In CESR cavity the coupling between the waveguide and the cavity is done through a hole located in Round Beam Tube (RBT). The geometry and dimensions of this hole are determined from the specification of the external Q of the cavity ($Q_{ext}$). To determine the ideal $Q_{ext}$, in which the RF power reflected is minimal, we have to know some ring operating parameters such as the stored current, energy lost per turn by electrons and some parameters of the harmonic cavity[^1] 

[^1]: We are assuming to use the harmonic cavity type NSLS-II which the main parameters are represents at [link]

![](/img/machine/rf_system/CESR_cavity_SRF_module.png)

**Figure 1**: Cut view of the CESR cavity SRF module.

| Parameter | Value | Unit |
| --- | --- | --- |
|RF frequency | 499.654 | MHz |
|Accelerating voltage | 2 | MV |
|Dynamic losses @ 2 MV | < 70 | W |
|Q0 at 2 MV | > 1 × 10⁹ | MV/m |
|Shunt impedance | 44500 | MΩ |
|External Q | 1.5 - 2.5 ± 0.3 × 10⁵ | - |
|Power forward (TW mode) | 250 | kW  |
{.dense}


**Table 2**: CESR cavity SRF module parameters.

The Figure 2 and Figure 3 shows, for the phase 2 of operation, the RF forward and reflected power as a function of stored beam current and external cavity Q. The black dashed line in the diagram represents the ideal situation (minimum reflected power).

> Note that using $Q_{ext}$ ~ 1.6*10⁵ (ideal value for the nominal operation current of 350 mA) results in a reflected power of about 5 kW per cavity at 500 mA.
{.is-info}


Table 2  shows some RF parameters calculated for each phase of operation using cavities with $Q_{ext}$ optimized for this nominal operation phase with 350 mA. Table 3 shows some RF parameters calculated for all phases of operation using cavities with $Q_{ext}$ optimized for the phase 2 with 350 mA.

Until now we only have some estimates about the energy loss per turn from IDs. The Figure 4 and Figure 5 show the reflected power within a range of energy loss from IDs in the oparation pahse 1 and phase 2.

|![](/img/machine/rf_system/CESR_RF_forward_power.png =400x)|![](/img/machine/rf_system/CESR_RF_reflected_power.png =400x)|
|---|---|
|**Figure 2**: RF forward power as a function of the storage beam current and external cavity Q.|**Figure 3**: RF reflected power as a function of the storage beam current and external cavity Q.|


|Parameter|Phase 0 <br />(commissioning)|Phase 1 <br />(initial user mode)| Phase 2 <br />(final user mode)|Phase 2 <br />(high current)|
 --- | --- | --- | --- | --- |
|Cavity type | CESR | CESR | CESR | CESR |
|Number of cavities | 2 | 2 | 2 | 2 |
|RF voltage per cavity (MV) | 1.25 | 1.25 | 1.5 | 1.5 |
|Beam current (mA) | 100 | 100 | 350 | 500 |
|Energy loss/turn: <br />• Dipoles (keV) <br />• IDs (keV) <br />• Harmonic cavity (eV) |<br />532.5 <br />- <br />- |<br />532.5 <br />144.6 <br />- |<br />532.5 <br />377.0 <br />29.8 |<br />532.50 <br />377.0 <br />20.9 |
|External Q | 1.6 × 10⁵ | 1.6 × 10⁵ | 1.6 × 10⁵ | 1.6 × 10⁵ |
|Synchronous phase (°) | 167.7 | 164.3 | 162.4 | 162.4 |
|Forward power per cavity (kW) | 42.4 | 47.0 | 158.1 | 233.1 |
|Reflected Power per cavity (kW) | 15.7 | 13.1 | 0.0 | 7.3 |
|Fundamental Bunch Form Factor | 1.000 | 1.000 | 0.993 | 0.993 |
|Optimum tuning angle (°) | -48.0 | -47.6 | -72.4 | -77.4 |
|Harmonic cavity type | - | - | NSLS-II | NSLS-II |
|Harmonic cavity optimum tuning angle (°) | - | - | 90.0 | 90.0 |
|Harmonic Bunch Form Factor | - | - | 0.938 | 0.938 |
|Harmonic cavity voltage (kV) | - | - | 946.9 | 946.9 |
|Bunch length (ps) | 8.1 | 8.2 | 37.7 | 37.7 |
|RF energy acceptance (%) | 5.0 | 4.7 | 4.9 | 4.9  |
{.dense}

**Table 3**: Storage ring RF parameters for each operation phase.

|![](/img/machine/rf_system/Reflected_power_phase1.png =400x)|![](/img/machine/rf_system/RF_forward_power_phase2.png =400x)|
|---|---|
|**Figure 4**: RF reflected power per cavity at oparation phase 1.|**Figure 5**: RF forward power per cavity at oparation phase 2.|

<br />

## High Power Amplifiers

The RF plants of Sirius RF system are being designed to operate with high power solid state amplifiers. Each high power amplifier will supply at least 60 kW at maximum output power. For the NC cavities the plants will use a combination of the output power of two amplifiers and will be able to supply up to 120 kW per cavity. The same set of amplifiers could also be used to start the SC system and even with such reduced power it would be possible to operate the machine at 300 mA, considering the initial set of IDs planned to be installed in the machine (230 keV energy loss). After the installation of the SC RF system it would be possible to upgrade the output power of the plants by combining the output power of four amplifiers. This increase in output power is necessary to reach the design beam current and meets the power requirements for a possible future upgrade of the beam current to 500 mA. The experience with the two amplifiers of the UVX RF system has shown that working in a relaxed condition results in increased reliability. After four years there has not been a single beam loss caused by failures in the amplifier modules. In this period very few of them have failed and that happened without any impact on the beam. Besides, no degradation of the modules has been observed whatsoever. As much as possible, the amplifiers should be designed to operate not too close to the maximum output power of the modules. So, for the SC system there is plenty of power coming from the 60 kW amplifiers. For NC cavities it would be advisable to have more output power coming from each amplifier.

![](/img/machine/rf_system/Amplificador.jpg =700x)

**Figure 6**: Schematic view of the module combination topology for the 60 kW high power solid state amplifier.

The topology of the high power solid state amplifiers is expected to be similar to the one adopted for the amplifiers designed and built for the UVX storage ring. The UVX amplifiers operate at 476 MHz and combine the output power of 160 modules in order to reach 50 kW. The amplifier modules for the Sirius high power amplifiers use a new generation of MOSFET that can reach higher output power. By combining the output power of 128 modules the amplifier will be able to deliver up to 60 kW at 500 MHz. The figure on the right shows a schematic view of the module combination structure of the high power amplifier. In addition to the modules in the combining grid other four modules are used as pre-amplifiers summing up 132 modules per amplifier. A set of power dividers, combiners and power couplers for different power levels is used in the assembly. Each module has its own power supply and they are both attached to a water cooled bar that provides mechanical fixation and cooling. Each bar houses up to 17 modules. The power supplies are DC-DC converters that are combined to supply the 1 kW needed by the module. A high power DC power supply is used to drive the DC-DC converters.

The 500 MHz amplifier module is a variation of the 476 MHz modified for the new frequency and for the new power transistor. The module uses the BLF578, a power LDMOS-FET produced by NXP, and reaches the 1-dB compression point above 600 W output power. This is about 70% higher than the nominal output power of the modules used in the 476 MHz 50 kW amplifiers that are in operation at the UVX storage ring. For such higher output power the components of the amplifier will have to be redesigned not only due to the new RF frequency but also to account for the higher thermal load they will have to handle.

<br />

## Low Level RF System

A fully analogue LLRF could be used for the commissioning and first years of operations of Sirius. Fully analogue LLRF controls are still used at Soleil even though a digital system has been developed and tested. The analogue version of the LLRF will comprise the conventional amplitude, phase and tune control loops, even though the regulation of the amplitude and phase of the cavity fields may be implemented using IQ techniques.

<br />

## RF System for the Booster

Booster and storage ring have very different stability specifications for the RF system. The excitation of HOM in the cavities is a problem that has to be tackled with care in the storage ring but that it is not a serious issue in the booster. A 5-cell PETRA NC cavity is going to be used for the booster and the RF plant will be driven by a single solid state amplifier. A gap voltage of 1 MV is enough to provide sufficient beam lifetime for a safe ejection at the final energy. However, considering a safety margin related to the energy acceptance and optical parameters of the booster, the whole system is being designed considering a final gap voltage of 1.1 MV.

<br />

### General Design

The storage ring and the booster synchrotron will share the same tunnel. The booster synchrotron is a long machine designed to have very low emittance and a magnetic lattice with very small momentum compaction factor. As a result, for a final accelerating voltage of 1.1 MV the beam life time at the ejection energy is expected to be close to one hour. At the booster injection energy the accelerating voltage will be about 100 kV and the gap voltage will ramp with the booster energy. The booster is being designed to operate at a cycling frequency of 2 Hz. The table below lists the main parameters of the booster RF system. Most of the parameters refer to the extraction energy.

| Parameter | Value | Unit |
| --- | --- | --- |
|Beam energy | 3.0 | GeV |
|Beam current | 2.0 | mA |
|Energy loss/turn | 721.3 | keV |
|SR power | 1.44 | kW |
|Cavity type | PETRA 5-cell |  |
|Peak RF voltage | 1.05 | MV |
|Total scaled shunt impedance | 15 | MÃŽÂ© |
|Maximum RF power needed | 45.0 | kW |
|Energy spread | 0.0874 |  % |
|RF frequency | 499.654 | MHz |
|RF wavelength | 0.6000 | m |
|Harmonic number | 828 |  |
|Momentum compation factor | 7.19×10-4 |  |
|Overvoltage | 1.456 |  |
|Synchronous phase | 136.6 | Â° |
|Synchrotron tune | 0.0044 |  |
|Synchrotron frequency | 2.67 | kHz |
|Natural bunch length | 11.25 | mm |
|Natural bunch length | 37.53 | ps |
|Energy acceptance | 0.79 |  % |
|Quantum lifetime | 4267 | s |
|Linac to Booster phase stability @500MHz | 5.0 | °  |
{.dense}

**Table 4**: Parameters used to design the booster RF system.

<br />

### RF Cavity

In order to obtain the necessary gap voltage using just one RF plant a 5-cell PETRA RF cavity was chosen for the booster RF system. The cavity has high shunt impedance and can provide the necessary gap voltage with a relatively low RF power. The table below shows the main parameters of the 5-cell PETRA RF cavity.

| Parameter | Value | Unit |
| --- | --- | --- |
|Number of cells | 5 |  |
|Fundamental frequency | 499.654 | MHz |
|Maximum gap voltage | 1.5 | MV |
|Nominal gap voltage | 1.1 | MV |
|Tuning range | ±0.2 | MHz |
|Minimum unloaded Q | 29,000 |  |
|Minimum R/Q | 370 | Ω/m |
|Minimum shunt impedance | 15 | MΩ |
|Dissipated cavity power @1.1MV | 33 | kW |
|Coupling factor | 1.04 |  |
|Operating temperature | 30 | °C |
|Detuning due to plunger position | 20 | kHz/mm |
|Total length between flanges | 1,800 | mm |
|Beam tube aperture | 120 | mm |
|Beam height | 1,400 | mm  |
{.dense}

**Table 5**: Parameters of the Booster RF cavity.

This same model is used in many machines to drive the injection booster. The cavity is being purchased from an external supplier.

|![](/img/machine/rf_system/SSA_RFBooster_Sirius.jpg =350x)|
|---|
|**Figure 7**: Schematic view of the 50 kW high power solid state amplifier for the booster synchrotron.|

<br />

### High Power Amplifier

Since the booster will operate at very low beam current the power required by the beam will be very small and most of the RF power from the amplifier will be used to excite the gap voltage. The booster system will use a 50 kW solid state amplifier which is not the same used for the storage ring RF plants. The modules are exactly the same but a smaller number is used in the combination chain. The amplifier is expected to work at fairly relaxed condition since the total RF power needed to produce the maximum gap voltage in the 5-cell cavity should is of the order of 40 kW. The nominal maximum output power of the amplifier modules is 600 W but the amplifier is being designed so that each module will deliver no more than 550 W. The modules have been thoroughly tested in the RF lab under conditions which replicate years of actual operating conditions in the booster and showed no signs of degradation.

<br />

### Low Level RF

An analogue LLRF is being designed for the booster RF system based on IQ techniques. The system is an improvement on the UVX LLRF and will include frequency, phase, gap voltage and field homogeneity controls. The use of a digital system is not discarded but the movement towards the development of an in-house digital system is still in very preliminary stage.

<br />

## Harmonic Cavity

Harmonic cavities are used in many machines to lengthen the electron bunches. The main effect of the bunch lengthening provided by these cavities is an increase of the Touschek lifetime due to the lowering of the bunch charge density, and an increase of beam stability due to an increase in the spread of synchrotron frequencies within the bunch. The harmonic cavities is used to add to the accelerating voltage produced by the main RF cavities a higher harmonic component which, given the correct phase and amplitude, zeroes (ideally) the slope of the resulting voltage as seen by the electron bunches at the synchronous phase. Harmonic cavities can operate in passive or active mode. An active cavity is driven by an external RF source; the passive cavity is driven by the beam itself. As expected, the efficiency of passive cavities depends on the beam current variation. In addition, harmonic cavities can also be normal conducting (NC) or superconducting (SC) cavities. Besides the advantages coming from the very high shunt impedance, the SC cavities also feature an efficient HOM suppression system. SC cavities are usually designed so as to have a smaller number of trapped HOM and to include means for damping the ones still standing.

Third harmonic cavities (3HC) are being considered for installation in the Sirius storage ring. For a total gap voltage of 3.0 MV in the storage ring fundamental cavities the ideal gap voltage in the harmonic cavities would be 953 kV. That would increase the bunch length by a factor in between 4 to 5 and would have a big impact on the tolerances of the LLRF coming from timing experiments. The necessary gap voltage can be achieved by using passive SC harmonic cavities (SC-3HC). A single 2-cell cavity like the one installed at SLS or the one designed for NSLS-2 would perfectly match the specifications for Sirius. SC-3HC have the advantage of reaching higher gap voltages so that a small number of cells are enough to reach the usually high gap voltage needed for an efficient operation. In addition, the impact on the main RF system is very small since the overall power lost by the beam in the cavities is of the order of a few dozen Watts.

<br />

### Specifications

The Table 1 show the SIRIUS parameters considered in high current phase 2 operation. From these values we can calculate the optimum parameters for a passive third harmonic cavity, the power loss in this cavity and the new synchronous phase (Table 6).

A large number of NC cavities would be required in order to reach a gap voltage of the order of 1 MV. SC harmonic cavities have very high shunt impedance, in the GΩ range, so that the power lost by the beam to excite the necessary gap voltage for passive operation is very small, of the order of just a few tens of watts. For NC cavities the power loss is considerably higher, of the order of 100 keV, and has to be taken into account in the dimensioning of the main RF system. Besides, the SC-3HC also include efficient HOM damping mechanisms, which make them undoubtedly the best choice for very low emittance machines like Sirius. If the main RF system is chosen to be based on SC cavities an additional heat load due to the SC 3HC has to be included in the specifications of the cryogenic plant. If the main RF system is based on NC cavities then a cryogenic plant has to be provided for the SC-3HC.

A two cell SC-3HC like the one built for the NSLS-2 light source would perfectly fit the needs of Sirius. Table 7 shows the NSLS-2 SC-3HC parameters. We decided by the initial calculations set the harmonic phase in the value witch the peak RF voltage was equal the optimum value. Table 7 also show the parameters of operation of this SC-3HC. As we can note, the tuning angle do not differ much from the optimum value (Δψ$_h$= 6.46°).

| Parameter | Value | Unit |
| --- | --- | --- |
|Energy | 3.0 | GeV |
|Maximum Beam current | 500 | mA |
|RF frequency | 499.664 | MHz |
|Harmonic number | 864 |  |
|Energy loss/turn from dipoles | 471.01 | keV |
|Energy loss/turn from insertions (estimated) | 400 | keV |
|Total energy loss/turn | 871.01 | keV |
|Synchrotron radiation power from dipoles | 236 | kW |
|Synchrotron radiation power from insertions | 200 | kW |
|Total synchrotron radiation power | 436 | kW |
|Peak RF voltage | 3.0 | MV |
|Overvoltage, q=V/U0 | 3.4 |  |
|Synchronous phase | 163.1 | Â° |
|Synchrotron tune | 0.004652 |  |
|Synchrotron frequency | 2.690 | kHz |
|Momentum compaction factor | 1.6×10⁻⁴ |  |
|Natural bunch length | 8.2 | ps |
|RF energy acceptance | 5.13 |  % |
{.dense}

**Table 1**: Main SI RF System Parameters.

| Parameter | Value | Unit |
| --- | --- | --- |
|Harmonic number | 3 | - |
|Resonance frequency | 1.499 | GHz |
|Peak RF voltage | 953 | kV |
|Shunt impedance | 8.48 | MΩ |
|Optimum tuning angle | 83.54 | ° |
|New synchronous phase | 161.26 | ° |
|Power loss in the 3HC | 53.5 | kW |
{.dense}

**Table 6**: Sirius SR optics parameters.

| Parameter | Value | Unit |
| --- | --- | --- |
|Cavity frequency (pi-mode) | 1.499 | GHz |
|R/Q (pi-mode) | 88 | Ω |
|Quality factor | 2.6∙108 | - |
|Peak electric field | 12.8 | MV/m |
|Peak magnetic field | 22 | mT |
|Integrated voltage | 0.5 | MV/cell |
|Operating temperature | 4.5 | K |
|New synchronous phase | 163.41 | °  |
{.dense}

**Table 7**: NSLS-2 SC-3HC parameters.

<br />

### Bunch length

To calculate the bunch length using the harmonic cavities we need understand the equations of longitudinal motion of a single electron given by

$$
\frac{dz}{dt} = \alpha c \epsilon,
$$

$$
\frac{d \epsilon}{dt} = \frac{1}{ET_0}(eV(z)-U(\epsilon)),
$$

where <b>z</b> is the longitudinal coordinate of the electron; <b>ε</b> is the fractional energy deviation from a synchronous electron; <b>α</b> is the momentum compaction; <b>E</b> is the energy. The combined voltage from the main and harmonic RF system is

$$
V(z) = V_{RF} \left[ \cos \left( \frac{\omega_{RF} }{c} z+ \frac{\pi}{2} -\phi_s \right) - r \cos \left( \frac{m \omega_{RF} }{c} z +\psi_h \right) \right]
$$

where <b>r</b> is the relative harmonic voltage to the main voltage; <b>φ<sub>s</sub></b> is the synchronous phase; <b>ψ<sub>h</sub></b> is the harmonic tuning angle; <b>m</b> is the harmonic number. The potential well is given by

$$
\Phi (z) = \frac{\alpha}{EC} \int_{0}^{z} [eV(z')-U_0]\, dz'
$$

where <b>C</b> is the ring circumference; <b>U<sub>0</sub></b> is the energy loss/turn. And the charge density distribution can be calculated by

$$
\rho (z) = \rho_0  \exp { \left( \frac{ -\Phi (z)}{ \alpha^2 \sigma_e^2 } \right)}
$$

where <b>ρ<sub>0</sub></b> is a normalization constant.

So the longitudinal bunch distribution can be shaped by varying the relative voltage and phase of the harmonic voltage. These parameters should be adjusted to cancel the slope of main RF voltage at the bunch center. The main RF voltage is perfectly canceled when the potential and its first two derivatives are zero. At this condition we have

$$
r= \sqrt{ \frac{1}{m^2}-\frac{1}{m^2-1} \left( \frac{U_0}{eV_{RF}} \right)^2}
$$

$$
\tan (\psi_h) = \frac{1}{m} \frac{eV_{RF}}{U_0} \sqrt{(m^2-1)^2 - \left( \frac{m^2U_0}{eV_{RF}} \right)^2}
$$

and the new synchronous phase is given by

$$
\sin(\phi_s) = \frac{m^2}{m^2-1} \frac{U_0}{eV_{RF}}.
$$


For passive harmonic cavity, the gap harmonic voltage is a function of beam loading effect

$$
r = \frac{2I_bR_hF \cos (\psi_h)}{V_{RF}}
$$

where <b>R<sub>h</sub></b> is the harmonic cavity shunt impedance; <b>I<sub>b</sub></b> is the beam current; <b>F</b> is the form factor.

Using these equation above is possible calculate the longitudinal density distribution of the bunch. The Figure 8 shows the potential well and the density distribution for three different situations: without 3HC, with optimum 3HC and with NSLS-2 3HC. The Figure 9 shows, in more detail, the density distribution and the bunch length for each case. Is noted that using the 3HC increases the bunch length by a factor of ~5.

| | |
|---|---|
|![](/img/machine/rf_system/SI_potential_well_HC.svg =400x) <br />**Figure 8**: Potential well distortion and charge distribution with 3HC. |![](/img/machine/rf_system/SI_charge_distribution_HC.svg =400x) <br />**Figure 9**: Charge distribution and bunch length with 3HC.|

<br />

### Touschek lifetime

To calculate the improvement in Touschek lifetime, consider the expression for the Touschek loss rate[^2].

[^2]: Byrd, J. M. and Georgsson, M., Phys. Rev. ST Accel. Beams 4, 030701 (2001).

$$
\dot{N} = \overline{\upsilon \sigma} \int_{V}^{} \rho^2 \, dV
$$

where $\overline{\upsilon \sigma}$ is the probability for scattering beyond the RF acceptance <b>ε<sub>RF</sub></b>; <b>ρ</b> is the volume charge density.

The scattering probability $\overline{\upsilon \sigma}$ is proportional to <b>1/ε<sub>RF</sub><sup>2</sup></b>, so it is necessary to include the effect of the harmonic voltage on the RF acceptance <b>ε<sub>RF</sub></b>. The ratio of lifetime with and without harmonic voltage can be found from

$$
R = \frac{\tau_{hc}}{\tau} = \frac{\epsilon_{hc}^2}{\epsilon_{RF}^2}\frac{\int \rho^2(z)\,dz}{\int \rho_{hc}^2(z)\,dz}
$$

where <b>ε<sub>hc</sub></b> is the RF acceptance with harmonic cavity; <b>ρ<sub>hc</sub></b> is the longitudinal density with harmonic cavity.

Using the NSLS-2 3HC in Sirius we have an improvement in the ratio of lifetime by a factor of 5. The Figure 10 shows the separatrices for each case studied.

![](/img/machine/rf_system/SI_separatrix_HC.svg =400x)

**Figure 10**: RF bucket with and without 3HC.

### Dependence of RF voltage

In this section we studied the dependence of some parameters with the total voltage in the main RF system: The Figure 11 shows the dependence of RF acceptance, Figure 12 the ratio of lifetime and Fig 5 shows the power loss by the beam in the harmonic cavity.

|![](/img/machine/rf_system/SI_energy_acceptance_HC.svg =400x)|![](/img/machine/rf_system/SI_lifetime_ratio_HC.svg =500x)|![](/img/machine/rf_system/SI_power_loss_NSLS_2_HC.svg "teste de texto" =400x)|
|---|---|---|
|**Figure 11**: RF acceptance versus total RF voltage with and without 3HC.|**Figure 12**: Lifetime ratio versus total RF voltage with 3HC.|**Figure 13**: Power loss by the beam (@Ib=500 mA) in the NSLS-2 harmonic cavity.|


<br />

### LLRF

The control system for the harmonic cavity is basically a tune control loop. Since the cavity is passively excited by the beam the control of the amplitude of the gap voltage is performed by changing the tune of the fundamental mode. So, the frequency loop is necessary to optimise the operation of the harmonic cavity for different beam currents and also to control the cavity tuning.

<br />

## References
