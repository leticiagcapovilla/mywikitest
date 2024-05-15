---
title: Naming System
description: 
published: 1
date: 2024-03-05T20:45:44.002Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:33.231Z
---

# Machine: Naming System

<br />

## Introduction

In the sections below the naming convention for Sirius is defined. It should be used to name device types, signals (properties) and machine slots.  
Moreover, the infrastructure of EPICS support applications that should be used to help managing lists of named objects for Sirius is described.

The Naming service and other support services can be accessed through the [EPICS Support Applications](/home/Machine/epics_support_apps) menu

The wiki page for the outdated previous naming convention can be [accessed here]

<br />

## PV Naming Specification

![](/img/machine/naming_system/SIRIUS_naming_convention.png)

<br />

### PV Name

sec-sub:dis-dev\[-idx\]:propty\[.field\]

|     |     |     |
| --- | --- | --- |
| Area | • sec  <br>(=Section)   <br>  <br>• sub  <br>(=Subsection) | • Accelerator Section comprising the machine (e.g, Storage Ring, Booster, Linac, Transport Lines, etc)   <br>  <br>• Accelerator Subsection within a specific Section (e.g., First Sector, First Chromatic Section = 01C1, 02C2, 01M2, 01M1, etc) |
| Device | • dis  <br>(=Discipline)   <br>  <br>• dev  <br>(=Device)   <br>  <br>• idx  <br>(=Index) | • Branch of knowledge indicating the context in which a device is used (e.g, VAC, DIG, etc)   <br>  <br>• Physical device or indirect controlled device (needs to be unique only inside the same Discipline) (e.g., BPM, PS, Shaker, BBB, temperature sensor, fan, etc)   <br>  <br>• Distinsgish between same Devices in the same Subsection and Discipline (e.g., 010, 020, 1, 2, 3, R1C2, etc). |
| PField | • propty  <br>(=Property)   <br>  <br>• field  <br>(=Field) | • A particular property of the accelerator system (e.g., Current, Position, Temperature).   <br>  <br>  <br>• A particular attribute of the property (an EPICS record field). |

<br />

### Rationale

#### AREA

(From ESS naming convention and DISCS Collaboration: [https://ess-ics.atlassian.net/wiki/display/NC](https://ess-ics.atlassian.net/wiki/display/NC) \[link\])

From the operational point of view it is beneficial to have names mentally linked to functional area.  
This would help physicists, operators, technicians and engineers to orient themselves on the site relative  
to named technical systems. Devices and signals are therefore sorted under a functional area structure in  
three levels:

-   Level 1. Super Section: Not part of the naming convention.
-   Level 2. Section (Sec)
-   Level 3. Subsection (Sub)

<br />

#### DEVICE

Any equipment that serves a particular function and is connected to the Control System is modelled as a device.

-   A Device name can represent Single piece of equipment, e.g. a temperature transmitter with only one signal.
-   Complex module of components, named devices and a local control system. Examples: Klystron modulators.
-   Indirectly controlled equipment, (e.g., a quadrupole magnet with the gradient field calculated from the settings and readouts from the connected power supply).

Devices can resided inside other devices, however the parent child relation cannot be resolved from the names.  
The hierarchy can instead be found in the configuration database or in other systems where the names are used.

-   Level 1. Discipline (Dis)
-   Level 2. Category: Not part of the naming convention.
-   Level 3. Device Type (Dev)

<br />

#### PROPERTY

Naming convention users prefer to use generic device type as device identifier in names.  
Essential for configuration of the control system is however the specific device type, which  
in principle could be viewed as the fourth level in the device structure. In difference to items  
in the device structure, which are managed in the Naming Service, the specific device types and  
signal part of names are handled by integrators in the IOC Factory. The specific device types and  
the signal part are therefore sorted under a separate configuration structure:

-   Level 1 Specific Device Type: Not part of the naming convention.
-   Level 2 Property (Property)
-   Level 3 Field (FIELD)

<br />

### Naming Rules

**R01** Instance index (Idx) shall be alphanumeric. I.e., only upper and lower case alphanumeric characters (a-z, A-Z, 0-9) are allowed.

* **R02** The device names Sec-Sub:Dis-Dev-Idx shall be distinguishable, which means that names shall be unique irrespective of:  
  * Letter case  
  * Letters I, l and number 1  
  * Letter O and number 0  
  * Letters V and W  
  * Leading zeros, i.e., number 0 immediately following a non-numerical character  
* **R03** The maximum length of instance index (Idx) is 6 characters.  
* **R04** Properties like temperature, current, voltage etc., will be used for many different device types.  
  * Therefore, the signal property shall follow the LNLS Signal-Property Standard. Users of the naming convention are strongly encouraged to update this list.

* **R05** A signal, which is intended only for debugging or for other private purposes, shall include a lowercase i as prefix (iProperty).

* **R06** To distinguish identical signals of the same device, suffices shall be appended to the property as  
 * PropertySuffix. Users shall refer to the LNLS Signal-Property Standard, where common suffices are listed,  
 * before inventing new ones for standard types such as read (Rd) and set (Set).

* **R07** Units must not be entered in the names. The record field for engineering units (EGU) handles this.

* **R08** Each part of the PV name must have the following number of characters:  
 * Sec >= 1 && Sec <= 6  
 * Sub >= 1 && Sub <= 6  
 * Dis >= 1 && Dis <= 6  
 * Dev >= 1 && Dev <= 12  
 * Idx >= 0 && Idx <= 12  
 * Prop >= 1

* **R09** Characters '-' (dash), '.' (dot) and ':' (colon) are reserved and should not be used in Sec, Sub, Dis, Dev, Idx, Property or FIELD fields. The exception to this rule is in the use of suffixes, as defined by table \[\[Table:Naming\_System\_Property\_Domains|Suffixes Table\]\]

<br />

### Abbreviation Tables

#### Device Names \[link\]

| Abbreviation | Device Name |
| --- | --- |
| AccStr | Accelerating Structure |
| Amp | Amplifier |
| Anode | Anode |
| B   | Bending magnet/Dipole |
| BakJ | Bakeout heating jackets |
| BE  | Back-End |
| BLM | Beam Loss Monitor |
| Blw | Non-RF bellows |
| BlwRF | RF shielded bellows |
| BMPS | Bending Magnet Photon Shutter |
| BPM | Beam Position Monitor |
| Brd | Board |
| Bun | Buncher |
| Cam | Camera |
| CCG | Cold cathode vacuum gauge |
| CH  | Horizontal Corrector Magnet |
| Corr | Corrector/Correction |
| CRL | Compound Refractive Lens |
| CV  | Vertical Corrector Magnet |
| DCCT | Direct Current Current Transformer |
| Detec | Detector |
| Dig | Digitizer |
| Distrib | Distributor/Distribution |
| Door | Door |
| EBeam | Electron beam |
| EjeKckr | Ejection Kicker |
| EjeSeptF | Ejection Thin Septum |
| EjeSeptG | Ejection Thick Septum |
| APU | Adjustable Phase Undulator |
| EPU | Elliptically Polarizing Undulator |
| FBE | Front/Back-End |
| FCH | Horizontal Fast Corrector Magnet |
| FCT | Fast Current Transformer |
| FE  | Front-End |
| FOFB | Fast Orbit Feedback |
| Fout | Fanout |
| EGun | Electron gun |
| GV  | Gate valve (may be used for FE and |
| H   | Horizontal |
| Hyb | Hybrid |
| ICT | Integrating Current Transformer |
| InjDpKckr | Injection Dipolar Kicker |
| InjKckr | Injection Kicker |
| InjNLKckr | Injection Non-Linear Kicker |
| InjSept | Injection Septum |
| InjSeptF | Injection Thin Septum |
| InjSeptG | Injection Thick Septum |
| IOC | EPICS IOC |
| IP  | Sputter Ion Pump |
| IPC | Ion Pump Controller |
| IVU | In-Vacuum Undulator |
| Kly | Klystron |
| Mark | Placeholder position for calculations |
| Modltr | Modulator |
| Mtr | Motor |
| Mpole | Multipole |
| NEG | Non-evaporable getter pump |
| NEGC | NEG pump controller |
| NetSw | Network Switch |
| Pkup | Pickup |
| Panel | HMI Panel |
| PLC | Programmable Logic Controller |
| PRV | Pressure relief valve |
| PS  | Power supply |
| QD  | Defocusing Quadrupole |
| QF  | Focusing Quadrupole |
| QN  | Normal Quadrupole |
| QS  | Skew Quadrupole |
| RGA | Residual gas analyzer / partial |
| Shkr | Shaker |
| SHB | Sub-Harmonic Buncher |
| Scan | Scan (for experiment control) |
| Scrap | Scraper |
| ScrapH | Horizontal Scraper |
| ScrapV | Vertical Scraper |
| Scrn | Screen monitor |
| Slnd | Solenoid |
| SD  | Defocusing Sextupole magnet |
| SF  | Focusing Sextupole magnet |
| Sx  | Sextupole magnet |
| SOFB | Slow Orbit Feedback |
| StrkCam | Streak Camera |
| TCU | Temperature Compensating Unit |
| TCG | Thermal conductivity vacuum gauge |
| TMP | Turbomolecular pump |
| TSP | Titanium sublimation pump |
| TSPC | Titanium sublimation pump |
| TSrv | Terminal server |
| V   | Vertical |
| VF  | Visual Flag |
| VFD | Variable Frequency Drive |
| VGC | Vacuum gauge controller |
| UPS | Uninterruptible Power Supply |

**Table 1**: Device Names Table.

<br />

#### Property Names \[link\]

| Abbreviation | Property Name |
| --- | --- |
| Addr | Address |
| Alrm | Alarm |
| Alpha | Alpha (physics calc) |
| Ampl | Amplitude |
| Beta | Beta (physics calc) |
| Beam | Beam |
| Btn | Button |
| Bw  | Bandwidth |
| Chan | Channel |
| Clk | Clock |
| Cmd | Command |
| Cnt | Count |
| Ctrl | Control |
| Cyc | Cyclic |
| Delay | Delay |
| DI  | Digital input |
| Dir | Direction |
| Div | Divider |
| DO  | Digital output |
| Dose | Accumulated Radiation Dose |
| Dsbl | Disable |
| Dur | Duration |
| Eff | Efficiency |
| Emit | Emittance (physics calc) |
| Enbl | Enable |
| EStop | Emergency Stop |
| EU  | Engineering Units |
| Evt | Event |
| Excit | Excitation |
| Fld | Field (magnetic) |
| Flt | Fault |
| Fluor | Fluorescent |
| Freq | Frequency |
| Fxd | Fixed |
| Gen | Generator |
| HwFlt | Hardware fault |
| Intvl | Interval |
| ID  | Indentifier (e.g. serial number) |
| In  | Input (e.g., from PLC) |
| Incr | Increment / Incremented |
| Ind | Indicator (e.g. lamp, light, LED) |
| Inh | Inhibit |
| Intlk | Interlock |
| Lvl | Level |
| Lk  | Lock |
| Lim | Limit |
| Mark | Mark (position indicatore) |
| Mig | Migration |
| Mode | Mode |
| Mon | Monitor |
| Mult | Mult |
| Offset | Offset |
| Out | Output (e.g., from PLC) |
| Pressure | Pressure |
| Permit | Permit |
| Phs | Phase |
| Pol | Polarity |
| Pos | Position |
| Pt  | Point |
| Pulse | Pulse |
| Pwr | Power |
| Rdy | Ready |
| Rmp | Ramp |
| Rx  | Receiver |
| RB  | Readback |
| Req | Request |
| Res | Resolution |
| Humidity | Relative humidity |
| ROI | Region of interest |
| Rslt | Result |
| Rslv | Resolver |
| Rsrv | Reserved |
| Rst | Reset |
| S   | Speed |
| Seq | Sequence |
| SP  | Setpoint |
| Src | Source |
| Sgl | Single |
| Sig | Signal |
| Siren | Alarm siren |
| Size | Size |
| Slope | Slope |
| Slot | Slot |
| Step | Step |
| Sw  | Switch |
| Temp | Temperature |
| Tbl | Table |
| Time | Time |
| Ts  | Time interval |
| Tx  | Transmitter |
| Trig | Trigger |
| Trip | Interlock trip |
| Type | Type (of device) |
| Undo | Undo |
| Volt | Voltage |
| W   | Weight or Force |
| Wfm | Waveform |
| X   | Horizontal |
| Y   | Vertical |
| Z   | Longitudinal |

**Table 2**: Properties Table.

<br />

##### Property Domains (suffixes) \[link\]

| Suffix | Read/Write | Description |
| --- | --- | --- |
| \-Cte | read | Constant device property variable |
| \-Cmd | write | Variable to issue a momentary binary digital command to the device |
| \-Sel | write/read | Enumerated device property setpoint variable |
| \-Sts | read | Enumerated device property readback variable |
| \-SP | write/read | Non-enumerated device property setpoint variable |
| \-RB | read | Non-enumerated device property readback variable |
| \-Mon | read | Monitor non-enumerated or enumerated device property variable |

**Table 3**: Suffixes for non Setpoint/Readback device properties.

<br />

#### General Names \[link\]

| Abbreviation | Name |
| --- | --- |
| Acc | Accelerator |
| Avg | Average/Averaging |
| BbB | bunch-by-bunch |
| Dev | Device |
| Eje | Ejection/Extraction |
| Err | Error |
| Fam | Family |
| Fib | Optical Fiber |
| Filt | Filter |
| Glob | Global |
| Hw  | Hardware |
| Img | Image |
| Inj | Injection |
| Integ | Integrated |
| Kicker | Kicker |
| Mat | Matrix |
| MultB | Multi bunch |
| Nr  | Number |
| Op  | Operation |
| Ref | Reference |
| Resp | Response |
| Ser | Serial |
| SingB | Single bunch |
| Spl | Sample(s)/Sampling |
| Struct | Structure |
| Strth | Strength |
| Tot | Total |
| Tr  | Transfer |
| Thold | Threshold |

**Table 4**: General Table.

<br />

#### Guidelines

Device names should use index suffixes (-H/-V) to differentiate between two equal devices (e.g., TuneAmp-H/TuneAmp-V). The exception to this guideline should be only for historical reasons, such as horizontal/vertical correctors that use H/V as prefixes (e.g., CH/CV).

Properties should use X/Y sufixes without "-" (e.g., MonitX/MonitY) for X and Y directions.

<br />

### Examples of PV Names

01) SI-Glob:AP-SOFB:Mode-Sel
02) SI-13SA:DI-TuneSh:ExcAmp
03) SI-Glob:AP-TuneM:TuneX-Mon
04) SI-01M2:DI-BPM:PosX-Mon
05) SI-02M1:PS-QFB:Current-SP
06) LI-01:TI-STDMOE:TrigDelayCh01 (sending signal to LI-01:EG-EGun)
07) SI-Fam:PS-B1B2-1:Current-RB
08) SI-13SA:DI-DCCT:BbBCurrent-Mon
09) SI-01SA:TI-SOE:TrigDelayCh02 (sending signal to SI-01SA:PU-InjDpK)

<br />

### ABNF grammar for PV naming

```
; ABNF grammar (conforming to http://www.ietf.org/rfc/rfc4234.txt)  
; for LNLS EPICS naming convention, candidate 2  
  
PV-Name            = area device record field  
  
area               = sec inner-separator sub group-separator  
  
; Section can only be one of the options listed and approved below  
  
; The following may not work on all parsers. So, the traditional decimal  
; coding is used.  
; sec                = ( %s"AS" "SI" / %s"BO" / %s"LI" / %s"TS" / %s"TB" / %s"BL" / %s"UT" )  
sec                = ( %d83.73 / %d66.79 / %d76.73 / %d84.83 / %d84.66 / %d66.76 / %d85.84 )  
sub                = sub-code  
  
; combination of numbers and letters (e.g., C1, C2, M1, M2, etc)  
sub-code           = 1\*6alpha-num  
  
; device definition with optional index  
device             = dis inner-separator dev opt-idx group-separator  
  
opt-idx            = ( inner-separator idx ) / ""  
  
; Discipline can only be one of the options listed and approved below  
  
; The following may not work on all parsers. So, the traditional decimal  
; coding is used.  
; dis                = ( %s"MA" / %s"DI" / %s"PS" / %s"VA" / %s"RF" / %s"CO" / %s"TI" / %s"PU" / %s"PM" / %s"EP" / %s"PP" / %s"AP" / %s"ID" / %s"MS" / %s"EG" / %s"MO" )  
dis                = ( %d77.65 / %d68.73 / %d80.83 / %d86.65 / %d82.70 / %d67.79 / %d84.73 / %d80.85 / %d80.77 / %d69.80 / %d80.80 / %d80.65 / %d73.68 / %d77.83 / %d69.71 / %d77.79 )  
dev                = 1\*12letter  
idx                = 1\*6alpha-num  
  
; the field is just optional so we can check for the validity of the PV name,  
; but the field is always present on regular EPICS IOCs  
record             = 1\*15alpha-num opt-suffix  
  
opt-suffix         = ( suffix-separator record-suffix ) / ""  
record-suffix      = 1\*letter  
  
field              = ( record-separator epics-field ) / ""  
  
; EPICS record fields  
epics-field        = 1\*30letter-upper  
  
; alphanumeric  
alpha-num          = ( digit / letter )  
  
; letter  
letter             = letter-lower / letter-upper  
  
; letter lowercase  
letter-lower       = ALPHA-LOWER  
  
; letter uppercase  
letter-upper       = ALPHA-UPPER  
  
; 1 or more digits  
number             = 1\*DIGIT  
  
; 1 or more letters  
word               = 1\*ALPHA  
  
; regular digit  
digit              = %x30-39  
  
; regular character a-z A-Z  
ALPHA          =  ALPHA-LOWER / ALPHA-UPPER  
ALPHA-LOWER    =  %x41-5A  
ALPHA-UPPER    =  %x61-7A  
  
; separators  
inner-separator    = "-"  
suffix-separator   = "-"  
group-separator    = ":"  
record-separator   = "."
```

<br />

## Drawings with Names of Lattice Elements

Links bellow point to drawings with family names of lattice elements for each accelerator section

-   [AS - Accelerator System drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-AS.pdf) PDF file [(sectors split in PDF files)](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings)
-   [SI - Storage Ring drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-SI.pdf) PDF file
-   [TS - Booster to Storage Ring transport line drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-TS.pdf) PDF file
-   [BO - Booster drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-BO.pdf) PDF file
-   [TB - Linac to Booster transport line drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-TB.pdf) PDF file
-   [LI - Linac drawing](https://github.com/lnls-sirius/control-system-constants/tree/master/documentation/drawings/devnames-LI.pdf) PDF file

<br />

## Reference

[https://wiki.bnl.gov/nsls2controls/index.php/Standards-Naming\_Convention\_Signal\_Names#Signal\_Domains](https://wiki.bnl.gov/nsls2controls/index.php/Standards-Naming_Convention_Signal_Names#Signal_Domains)