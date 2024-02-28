# Machine: Timing System

## Introduction 

The Sirius timing system will be responsible for providing low jitter synchronized signals for the beam injection process as well as reference clocks and triggers for diverse subsystems such as electron BPMs, fast orbit feedback and beamlines. The system is event-based (see Figure 1), transmitting time-multiplexed  event codes, i.e., an event distribution system that broadcasts the timing information to all the relevant devices in the accelerator's complex. 
The hardware performance and the interface between timing modules and other hardware modules must satisfy the Sirius requirements. 
Furthermore, the timing system needs to perform the Sirius machine operation sequence and arbitrary bucket injection.

![](/img/machine/timing_system/TI_event_based_system.png)

**Figure 1**: Event-based timing system.

## Physical Requirements 

### Basic Parameters 

Table 1 shows the Sirius parameters concerning timing system.

| Parameter | Value | Unit |
| --- | --- | --- |
|Storage Ring Circumference| 518.3899 | m |
|Storage Ring RF Frequency| 499.664 | MHz |
|Storage Ring Harmonic Number| 864 | - |
|Storage Ring Revolution Frequency| 0.578 | MHz |
|Booster Circumference| 496.8 | m |
|Booster RF Frequency| 499.654 | MHz |
|Booster Harmonic Number| 828 | - |
|Booster Revolution Frequency| 0.603 | MHz |
|Coincidence Number| 19872 | - |
|Coincidence Frequency| 0.025 | MHz |
|Linac RF Frequency| 3.0 | GeV |
|Repetition rate of E-gun and pulsed magnets| 2.0 | Hz |
|Repetition rate of Modulators| 2.0 | Hz |
|E-gun jitter| < 50 ps | rms* |

**Table 1**: Sirius parameters.


''*Note: This is defined as the jitter of the E-gun trigger relative to the RF clock. The experience from the high voltage modulators of the existing LNLS Linac showed us that equipment are also quite sensitive to jitter. We believe the amplitude modulation (or ripple) in the high voltage pulses are responsible for that. The closer to 50 ps RMS the modulators jitter are, the better.''

The detailed machine operation sequence is shown in Figure 2, in accordance to Sirius' energy ramp scheme.

Booster ramping power supplies start ramp waveform at $T_0$; E-gun is triggered at $T_G$; beam is injected into Booster at $T_{BIN}$; beam is extracted from Booster at $T_{BEX}$; and beam is injected into Storage Ring at $T_{RIN}$.

* SROC is the storage ring revolution clock (RF/864). 
* BROC is the booster revolution clock (RF/828).
* CROC is the coincide clock of SROC and BROC (RF/19872).

The E-gun trigger is synchronized with CROC so that the beam can be injected into the deterministic buckets in both storage ring and booster. Meanwhile, the repetition rate (2 Hz, 1/30 of AC line frequency) of the E-gun trigger is frequency-locked with the mains. The relation between different clocks and E-gun trigger is listed in Figure 3.

![](/img/machine/timing_system/TI_sequence.png)

**Figure 2**: Sirius timing sequence.

![](/img/machine/timing_system/TI_different_clocks.png)

**Figure 3**: Relation between different clocks.>

###  Machine Operation Mode 

Top-up is foreseen to be the Sirius normal operation mode after the commissioning phase. According to its requirement, timing system should support the injection to any bucket.
The bucket selection is supported by low-level timing software, and the beam filling pattern is realized in top-level injection software.

## System Structure 

### System Layout 

In the Sirius' timing system, all required triggers and clocks are generated and encoded into a timing event by STD-EVG and transmitted through a fibre network. The STD-EVRs and STD-EVEs receive and decode the timing events and output the corresponding signals through an optical fibre and an electrical cable, respectively. STD-MOE, STD-SOE and SOE are optical to electrical converters and FANOUTs receive and broadcast the same signal out of each of its ports. The length of each fibre connecting STD-EVG to STD-EVRs is uniform so that the triggers and clocks in different EVRs could be output simultaneously. The simplified system structure of Sirius timing system is shown in Figure 4.

![](/img/machine/timing_system/TI_simplified_system_structure.png)

**Figure 4**: The simplified system structure of Sirius timing system.

The system topology of Sirius timing system is a 3-level star. 
The first level contains the STD-EVO/EVG, that is connected to STD-EVE or STD-EVO/EVR by multimode fibre.
The second level contains STD-EVO/EVR modules that are connected to STD-MOE and FANOUT modules by multimode fibres. The EVO/EVR also is connected to SOE or STD-SOE modules by plastic fibres. STD-MOE, SOE and STD-SOE provide triggers to high voltage device, like E-gun, septa, kickers and ramping power supplies.
The third level contains FANOUTs that are connected to OEL by multimode fibres. OEL devices provide triggers and clocks to BPM electronics at both Booster and Storage Ring, and can also provide triggers and clocks to some special beamline devices in time resolved experiments.

### Fibre Network 

The proposed fibre network for Sirius timing system is shown in Figure 5.

![](/img/machine/timing_system/TI_schematic_fiber_network.png)

**Figure 5**: Schematic fiber network for Sirius timing system

The multimode fibre is a 50 µm OM3 multimode with LC connectors. The multimode fibre network is arranged in a three level star topology:
*	Level-1 has the fibres connecting EVO/EVG to EVO/EVR or EVE. The length of level-1 fibres should be the same. The event timing protocol is transmitted through these fibres.
*	Level-2 has the fibres connecting EVO to STD-MOE, STD-SOE and FANOUT modules. The modulated triggers and clocks are transmitted through these fibres. The level-2 fibres, which are used for the devices in Booster and Storage Ring, should be of the same type and have the same length. The level-2 fibres used for FANOUT of BPM electronics in Booster and Storage Ring should be of the same length. The level-2 fibres used for FANOUT of beamline triggers and clocks should be of the same length.
*	Level-3 has the fibres from FANOUT to OEL. The modulated triggers and clocks are transmitted through these fibres. Level-3 fibres should be of the same type and length.
Plastic optical fibre links connect the outputs of EVO/EVR to the STD-SOE. These fibres are 1 mm Plastic Optical Fibre (POF) with SC connectors. The length of plastic fibres should be the same.
The following is the list of fibres for Sirius timing system.

|Fibre| Quantity| Length (m) |
| --- | --- | --- |
|Level-1 multimode fibre| 8| 250 |
|Level-2 multimode fibre (E-gun)| 1| 50 |
|Level-2 multimode fibre (BS & SR device)| 7| 250 |
|Level-2 multimode fibre (FANOUT for BPM electronics)| 4| 50 |
|Level-2 multimode fibre (FANOUT for Beamline)| 1| 50 |
|Level-3 multimode fibre| 26| 150 |
|Plastic fibre| 20| 50  |

**Table 2**: Fibres for Sirius timing system.

###  Interfaces to Hardware Devices 

The detailed interface diagram of Sirius timing system is shown in Figure 6.

![](/img/machine/timing_system/Timing_Network.svg)

**Figure 6**: Detail interface diagram of Sirius timing system.

The outputs of STD-EVE are LVTTL level with $50 \Omega$ impedance, and the interface of beam diagnostic devices in LINAC, TB (transport line Linac-Booster), TS (transport line Booster-Storage Ring) and streak camera should be compatible with LVTTL level with $50 \Omega$ impedance.
The outputs of STD-MOE and STD-SOE are TTL level with $50 \Omega$ impedance. The electrical standard of the OEL outputs should be designed according to BPM electronics and beamline device requirements.

### Hardware Modules 

The hardware modules of Sirius timing system, STD-EVO and STD-EVE, in standalone modules STD-EVO and STD-EVE, STD-MOE, STD-SOE, SOE, FANOUT and OEL, are listed below.

|Module| Quantity| Specification |
| --- | --- | --- |
|STD-EVO| 6| **Front panel:** <br />1 SFP input <br />8 SFP outputs <br />1 RF clock input <br />1 AC-line input <br />**Rear panel:** <br />12 optic outputs <br />1 interlock input <br />1 Ethernet port |
|STD-EVE| 3| **Front panel:** <br />1 SFP input <br />1 recovery RF clock output <br />8 LVTTL outputs <br />**Rear panel:** <br />12 optic outputs <br />1 interlock input <br />1 Ethernet port |
|STD-MOE| 5| 4 SFP inputs <br />|4 TTL outputs |
|STD-SOE| 3| 4 optic inputs <br />4 TTL outputs |
|SOE| 12| 1 optic input <br />1 TTL output |
|FANOUT| 5| 1 SFP input <br />11 SFP outputs |
|OEL| 26| 1 SFP input <br />12 LVDS outputs  |

**Table 3**: Hardware modules of Sirius timing system.

## Software System Design 

### Event timing system parameters 

The key function blocks in STD-EVO/EVG are the Distributed Bus, the Event Sequencer and the Synchronizer.

In the Distributed Bus, there are 8 dividers (MUX0-MUX7) to generate 8 channel clocks outputs.

The Event Sequencer block transmits event codes according to the timestamp associated to each event. Its diagram is shown in Figure 7.

The function diagram of the Synchronizer is shown in Figure 8. The AC line is synchronized with the output of MUX 7 divider. The output of D flip-flop is divided by AC divider and generates the output.

![](/img/machine/timing_system/TI_event_sequencer.png)

**Figure 7**: Caption

![](/img/machine/timing_system/TI_event_synchronizer.png)

**Figure 8**: The event synchronizer.

According to the physical requirements of Sirius' Timing System, the main parameters in STD-EVO/EVG are:
* RF divider is set to 4, so that event clock is the RF clock divided by 4; 
* MUX divider in the Synchronizer is set to 4968 to generate CROC clock;
* AC divider is set to 30 to generate 2 Hz machine repetition rate.
The output of the Synchronizer in STD-EVO/EVG is the trigger of the Event Sequencer, so every event code of STD-EVO/EVG output could be synchronized with the AC-line input and CROC. 

In STD-EVO/EVR, the key blocks are Triggers, TB Outputs and SFP Outputs.

Triggers is the block which provide the source for TB Outputs and SFP Outputs. Any trigger in the Triggers block can be generated from any event code by the event mapping function block. Triggers delay, width and polarity can also be programmed. The adjust resolution is one event period. Its diagram is shown in Figure 9.

The TB Outputs block maps the outputs of Triggers to OTP0 – OTP11 in rear panel respectively.

The SFP Outputs maps the outputs of Triggers or Distributed Bus to any OUT0 – OUT7 in front panel.

![](/img/machine/timing_system/TI_EVR_triggers_block.png)

**Figure 9**: STD-EVR triggers block

### Event Code Definition 

Following is the definition of event code in Sirius timing system:
* 0x01 for beam diagnosis in storage ring
* 0x02 for the trigger of LINAC device
* 0x03 for the trigger of Booster device
* 0x04 for the trigger of Booster extraction
* 0x06 for the trigger of E-gun
* 0x07 for the trigger of Booster injection
* 0x08 for the trigger of Storage ring injection 

### Bucket Selection Design 

The arbitrary bucket injection is realized by changing the timestamp of event code in sequence RAM and the RF delay of the E-gun trigger. 
Assuming that the injection bucket number is N, the timestamp offset related to the bucket number zero in the sequence RAM needs to change REM(N / 4), and the RF delay step (1/20 event clock) of E-gun triggers needs to changed 5*MOD(N / 4).
The timestamp of the event code 0x1 is fixed when the injection bucket number changing, but the address of event code 0x2, 0x3, 0x4, 0x6, 0x7 and 0x8 should be changed with the bucket number.

### Software 

Sirius timing system software works on the platform of EPICS base 3.14.12.4 running in a Linux environment. It provides low-level driver for the bucket selection, device control panels of timing and high-level injection control panel.
Furthermore, in STD-EVO and STD-EVE, the parameters could be set through UDP protocol, however there is no EPICS IOC (Input/Output Controller) run inside the modules. The EPICS IOC runs in a Linux server to set the parameters of STD-EVO and STD-EVE.

Some high level PVs related to injection proccess already defined:

**Linac**
- LI:TI:CYCLE : initiates the entire injection cycle
- LI:TI:EGUN:ENABLED : sets when to pulse the E-gun [0|1]
- LI:TI:EGUN:DELAY : sets the delay of the pulse for the E-gun [second]
- LI:TI:MOD1:ENABLED : sets when to pulse the modulator [0|1]
- LI:TI:MOD1:DELAY : sets the delay of the pulse for the modulator [second]
- LI:TI:MOD2:ENABLED : sets when to pulse the modulator [0|1]
- LI:TI:MOD2:DELAY : sets the delay of the pulse for the modulator [second]
- LI:TI:LLRF:ENABLED : sets when to pulse the Low Level RF system [0|1]
- LI:TI:LLRF:DELAY : sets the delay of the pulse for the Low Level RF system [second]
- LI:TI:BPM:ENABLED : sets when to pulse the BPMs for Linac [0|1]
- LI:TI:BPM:DELAY : sets the delay of the pulse for the BPMs for Linac [second]


**Booster**
- BO:TI:KICKINJ:ENABLED : sets when to pulse the Booster injection kicker [0|1]
- BO:TI:KICKINJ:DELAY : sets the delay of the pulse for the Booster injection kicker [second]
- BO:TI:KICKEX:ENABLED : sets when to pulse the Booster extraction kicker [0|1]
- BO:TI:KICKEX:DELAY : sets the delay of the pulse for the Booster extraction kicker [second]
- BO:TI:LLRF:ENABLED : sets when to pulse the Low Level RF system [0|1]
- BO:TI:LLRF:DELAY : sets the delay of the pulse for the Low Level RF system [second]
- BO:TI:RAMPPS:ENABLED : sets when to start the ramp of the magnets power supplies [0|1]
- BO:TI:RAMPPS:DELAY : sets the delay of the pulse for the ramp of the magnets power supplies[second]
- BO:TI:SEPTINJ:ENABLED : sets when to pulse the Booster injection septa [0|1]
- BO:TI:SEPTINJ:DELAY : sets the delay of the pulse for the Booster injection septa [second]
- BO:TI:SEPTEX:ENABLED : sets when to pulse the Booster extraction septa [0|1]
- BO:TI:SEPTEX:DELAY : sets the delay of the pulse for the Booster extraction septa [second]


**Storage Ring**
- SI:TI:KICKINJ:ENABLED : sets when to pulse the Storage Ring injection kicker [0|1]
- SI:TI:KICKINJ:DELAY : sets the delay of the pulse for the Storage Ring injection kicker  [second]
- SI:TI:PMMINJ:ENABLED : sets when to pulse the Storage Ring injection pulsed multipole magnet [0|1]
- SI:TI:PMMINJ:DELAY : sets the delay of the pulse for the Storage Ring injection pulsed multipole magnet  [second]
- SI:TI:SEPTINJ:ENABLED : sets when to pulse the Storage Ring injection septa [0|1]
- SI:TI:SEPTINJ:DELAY : sets the delay of the pulse for the Storage Ring injection septa [second]


**Transport Lines**
- TB:TI:BPM:ENABLED : sets when to pulse the BPMs for the Linac-Booster transport line [0|1]
- TB:TI:BPM:DELAY : sets the delay of the pulse for the BPMs for the Linac-Booster transport line [second]
- TS:TI:BPM:ENABLED : sets when to pulse the BPMs for the Booster-Storage Ring transport line [0|1]
- TS:TI:BPM:DELAY : sets the delay of the pulse for the BPMs for the Booster-Storage Ring transport line [second]

##  Status 

### SINAP Modules
13/02/2015 - Modules were produced, tested by SINAP staff and sent to Brazil.

02/03/2015 - Modules stopped in red channel at the Brazilian customs.

### LNLS Modules

12/03/2015 - Modules produced and received. Tests started.

### Low-level Software (EPICS IOC)

13/02/2015 - EPICS IOC developed by SINAP was received. 

27/02/2015 - Initial test in EPICS IOC was done and it is ok. Waiting for SINAP Modules to continue the tests.

### High-level software

02/03/2015 - Starting design of the timing control panel based on CSS (Control System Studio).
