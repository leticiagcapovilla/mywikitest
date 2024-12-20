---
title: Imbuia Introduction
description: Infrared beamline at Sirius
published: 1
date: 2024-09-13T20:30:09.233Z
tags: 
editor: markdown
dateCreated: 2024-03-04T20:05:53.880Z
---

# Introduction

IMBUIA is the first infrared (IR) beamline to operate in the new brazilian accelerator Sirius. This beamline will serve the worldwide community on multiscale chemical and optical analysis of multidisciplinary materials. For that, this beamline comprises two experimental stations: the IMBUIA-micro, dedicated to chemical mapping of microscale materials and the IMBUIA-nano, that will approach optical and vibrational analysis of materials at the nanoscale.

-   IMBUIA = **I**nfrared **M**icro- and nano-spectroscopy **B**eamline for **U**ltra-resolved **I**maging **A**pplications
-   Website: [https://lnls.cnpem.br/facilities/imbuia-en/](https://lnls.cnpem.br/facilities/imbuia-en/)
-   Location: Sirius experiment floor, **axis 43**

**Basic information**

## Tabset {.tabset}
### Energy ranges

| Parameter | value |
| --- | --- |
| Energy | 62 meV to 1.9 eV |
| Wavenumber | 500 cm^\-1^ to 15384 cm^\-1^ |
| Wavelength | 40 µm to 650 nm |
| Frequency | 15 THz to 461 THz |

**Notes**:

-   Despite the beamline delivers a broader range, the current coverage is limitted by the detector sensitivity and optical windows transmission.

### Flux and Brilliance

| Parameter | value |
| --- | --- |
| Flux | ∼10^11^ ph/s/0.1%bw @ 10 µm |
| Brilliance | ∼10^14^ ph/s/0.1%bw/mm^2^ @ 10 µm |

**Notes**:

-   Flux calculation used SRW code.
-   Storage ring current: 100 mA
-   Brilliance calculation ...
-   Values for the beam at the endstation (after windows and optics)

### Beam power

| Parameter | value |
| --- | --- |
| Full beam power (VIS+IR) | 550 µW |
| Filtered beam (mid-IR) | 14 µW |

**Notes**:

-   Storage ring current: 100 mA
-   Beam measured at the endstation (after windows and optics) using an Ophir power meter
-   mid-IR filter UDR8 (Agilent Technologies, Inc.): 900-2000 cm^\-1^

### Contacts

| Contact | Name | email | Extension |
| --- | --- | --- | --- |
| Coordinator | Raul Freitas | [raul.freitas@lnls.br](raul.freitas@lnls.br) | 5060 |
| Staff scientist | Francisco Maia | [francisco.maia@lnls.br](francisco.maia@lnls.br) | 5047 |
| Staff scientist | Ohanna Menezes | [ohanna.costa@lnls.br](ohanna.costa@lnls.br) | 5020 |
| Staff scientist | Lucyano Macedo | [lucyano.macedo@lnls.br](lucyano.macedo@lnls.br) | 5030 |
| Specialist | Thiago Santos | [thiago.santos@lnls.br](thiago.santos@lnls.br) | 5030 |
| Beamline | IMBUIA-nano station | [imbuia@lnls.br](imbuia@lnls.br) | 5030 |
| Beamline | IMBUIA-micro station | [imbuia@lnls.br](imbuia@lnls.br) | 5030 |

**Notes**:

> In case of emergency, call **(19) 35149686** or the extension 686


<br>
<br>

## Radiation extraction and source details

The 5-bend-achromat (5BA) cell of Sirius is comprised of 4 low-field (0.56 T) magnets named B1 and B2, one super-bend (BC, peak field 3.2 T) and one straight section, as illustrated in Fig. 1a. The IMBUIA beamline source is located in the Sector 7 of the storage ring, inside the first B2 dipole downstream the straight section. The source is defined by an extraction port (originally designed for visible photons diagnostics) centered at 3.01∘^\\circ∘ from the electrons orbit (Fig. 1b) and longitudinally located at 295 mm upstream the dipole center. A radiation mask of 7.07 ×\\times× 6.00 mm^2^ located in the pumping station of the B2 dipole (1137 mm from the source) defines a radiation extraction of 5.57 ×\\times× 5.27 mrad^2^ (Fig. 1c).

![extraction](/img/beamlines/imbuia/extraction.svg =700x)

-   **Figure 1**: IR extraction port. a) Magnetic lattice of the sector 7 of the accelerator with indication of the bending magnet source (B2, 0.57 T). b) Top-view section of the B2 dipole chamber highlighting the electrons orbit, SR extraction port and source origin. c) Pumping station after the dipole with radiation mask of 5.57 ×\\times× 5.27 mrad^2^ for SR extraction.

Simulations of IR intensity at the radiation mask are presented in Fig. 2. The maps were calculated using the code Synchrotron Radiation Workshop ([SRW](http://www.esrf.eu/Accelerators/Groups/InsertionDevices/Software/SRW)) for an observation window located at the radiation mask of the pumping station of the B2 dipole and for 350 mA stored current. The intensity maps show that the horizontal polarization is dominant as the wavelengths get longer. For instance, for 1 µm wavelength, the 6 mm vertical aperture of the mask allows a fair portion of vertically polarized radiation to be collected, while, for a wavelength of 20 µm, very little of this radiation can exit the port.

![fluxmask](/img/beamlines/imbuia/flux-at-mask.png)

-   **Figure 2**: SRW simulation of the flux at the radiation mask of the B2 pumping station for several wavelengths. Intensity maps simulated for a stored current of 350 mA.

An important figure to be considered in the designing of SR probes is the source size. Fig.3 presents the simulation of the IR source for the wavelengths of 1, 10 and 20 µm. Since the source is inside the magnetic fields of a B2 dipole, most of the numerical codes do not allow a direct visualisation of the source. Therefore, we used a 1:1 magnification system based on thin lens of the SRW (top row diagram of Fig.3) to simulate the source at its origin. The FWHM of the IR intensity distribution at the origin are 0.22 µm, 1.82 µm and 3.53 µm for the wavelengths of 1, 10 and 20 µm, respectively.

![source](/img/beamlines/imbuia/imbuia_source.jpg)

-   **Figure 3**: SRW simulation of the IMBUIA source produced by an imaging optical scheme with magnification 1. Simulations performed for 100 mA stored current.

## Flux, Polarization, Brilliance and Irradiance from far- to mid-IR

The size of the source is directly proportional to the wavelength, therefore, it is a diffraction-limited point source in the infrared range. In the other hand, the maximum value for the flux density does not follow the same proportion law as it influenced by the maximum collection angle of the port. To illustrate this in depth, we calculated the spectral flux (Fig. 4a), polarization portions (Fig. 4b), spectral brilliance (Fig. 4c) and irradiance (Fig. 4d). By observing the flux trend (Fig. 4a), it is clear that longer wavelengths are hardly penalized by the small vertical aperture of the port, as the curve drops fast above 1 μm wavelengths. Moreover, the extracted radiation is dominated by horizontal polarization, as the total polarization flux is just slightly above the h-polarized flux. This is confirmed by the polarization study in Fig. 4b, where the h-polarized portion correspond to more than 75% of the total. For longer wavelengths (>20 μm) the polarization becomes mainly horizontal (above 90%), confirming that a very small central portion of the far-IR/THz beam is passing through the extraction port.

![figures-merit](/img/beamlines/imbuia/flux_brilliance.jpg)

-   **Figure 4**: Calculated spectral flux, polarization degree, brilliance and irradiance in the visible-to-IR ranges considering the extraction port described in Fig. 1 at 100 mA. All simulations were done using SRW.

## Radiation extraction element (M1 mirror)

For radiation collection, we designed a vertically-supported flat mirror (M1) installed in front of the extraction port illustrated in Fig. 1c. The full white beam from the bending magnet illuminates the Au-coated Glidcop flat surface that absorbs most of the high energy portion (X-rays) and reflects the lower energy portion (UV, visible and IR), as illustrated in Fig. 5a. As a safety requirement, the entire M1 shaft can move vertically in case the mirror needs to be removed from the beam path, which is the only degree of freedom of M1. Most of the heat load from the white beam is absorbed by the M1, which corresponds to ∼\\sim∼ 140 W. Hence, a water-cooling system operates to drain this large power and to reduce M1 surface deformations. For that, a coaxial concept flows cold water (21∘^\\circ∘ C, 150 ml/min) towards the illuminated area guided by an inner pipe which returns warmer through the outer gap, as schemed in Fig. 5b. The maximum temperature of the mirror surface is about 130∘^\\circ∘ C predicted for 350 mA (maximum storage ring current), as depicted in Fig. 5c (left panel). Given the total heat load and illumination area of the beam over M1, we calculated the deformation in the X direction (thermal bump quasi-normal to the surface) whose maximum is near 1.24 μm, as displayed in Fig. 5c (middle panel) sided by the equivalent stress that peaks at 72 MPa (Fig. 5c, right panel).

![m1](/img/beamlines/imbuia/m1.jpg)

-   **Figure 5**: IR extraction mirror heat load. a) Vertical-mounted flat mirror (M1) is illuminated by near 140 W of SR from the B2 bending magnetic. The Au coated mirror surface reflects low energy radiation (UV-VIS-IR) and transmits the high energy portion (mostly X-rays) that is mainly absorbed by the Glidcop substrate. b) Cross-section of the M1 shaft highlighting the water cooling flow path. c) Numerical simulation of the thermal load, X-deformation and stress around the illuminated area of the mirror, respectively. d) Optical simulation of the secondary source produced by a M1 flat mirror with a Si substrate at -150 ∘^\\circ∘C (control case) and the Glidcop substrate (actual case with thermal bump) with the heat load and water cooling system for λ\\lambdaλ=15 μm (scale bars 1 mm) and λ\\lambdaλ=1.24 μm (scale bars 100 μm), respectively.

The choice for the Glidcop substrate was based on the simulation study that compared 4 different substrates cooled at room temperature or cryogenic conditions (Table 2). Gladcop is the one with the lowest values for surface temperature, deformation and stress when operating cooled near room temperature.

| Material | Max. Temp. \[°C\] | Max. Deformation \[mm\] | Max. Stress \[MPa\] |
| --- | --- | --- | --- |
| Al @ 24 °C | 220 | 0.0128 | 199 |
| CuCrZr @ 26 °C | 81  | 0.0024 | 65  |
| **GlidCop @ 21 °C** | **130** | **0.0012** | **72** |
| Si @ -150 °C | \-118 | 7.9E-6 | 1   |

-   **Table 1**: Main results on numerical simulations using Ansys code for the mirror substrates options at room temperature or at cryogenic conditions. All results were calculated for 350 mA. GlidCop was the best choice in the study.

## Beamline optics and optomechanics

The optical layout of IMBUIA is comprised of 4 mirrors in vacuum that delivers the broadband IR beam to either the IMBUIA-nano station or the IMBUIA-micro station (Fig. 4a). The bending magnet IR radiation is first collected by a custom- designed water-cooled Au/Glidcop flat mirror (M1, Fig. 3) that directs the beam towards a periscope made of two Au/glass 2- inches flat mirrors (M2 and M3). Before the periscope, a 1-inch diameter and 500 nm thick CVD diamond window (W1) separates the storage ring and beamline vacuum environments. Flowing downstream, the IR beam crosses the X-rays beam from the neighbor undulator beamline, a concept that avoids extra reflections and makes the beam path as shorter as possible. Then a BaF2 window (W2) separates UHV and open-air environments downstream M3.

![optics](/img/beamlines/imbuia/optics.jpg)

-   **Figure 6**: IMBUIA optical layout: three flat mirrors (M1, M2 and M3) deliver the VIS-IR broadband beam to the IMBUIA-nano station. A movable parabolic mirror (M4) collimates and directs the beam towards the IMBUIA-micro station on demand.

Yet on the optical table in air environment, a custom designed Au/Aluminum toroidal mirror (M5) collects the naturally divergent IR beam and focuses it 419 mm downstream, producing a secondary source (SS). Using a regular CCD and a band pass filter centered at λ\\lambdaλ=980 nm, we imaged the SS as showed in (Fig. 4e), whose shape and dimen- sions (FWHM ∼\\sim∼ 20 μm) are consistent to the SRW numerical simulation of the SS (FWHM ∼\\sim∼ 33 μm at λ\\lambdaλ=1.24 μm) depicted in Fig. 4d. The small discrepancy between experiment and simulation regarding the FWHM is associated to the slightly different wavelengths and exposure parameters. We used different wavelengths since we could not match available bandpass filters with the minimum energy that SRW can simulate. By positioning a screen at the M5 position and using a 633 nm band pass filter, we could image the beam cross-section (Fig. 4c) with horizontal ×\\times× vertical dimensions of 26 ×\\times× 23 mm^2^, respectively, and with good agreement with the numerical prediction (Fig. 4b). A structure of rings is observed in both experiment and simulation for λ\\lambdaλ=633 (Fig. 4b,c) nm and it is understood here as diffraction fringes from the bending magnet extraction port, previously presented in Fig. 1c. An intense curved feature was observed (white arrow in Fig. 4c) and is interpreted as an internal reflection from the dipole chamber. Inside the UHV periscope, a custom-designed Au/Aluminum parabolic mirror (M4) is mounted on a long travel linear stage that enables beam selection to the IMBUIA-micro station.

![beam-profiles](/img/beamlines/imbuia/beam_diagnostics.jpg)

-   **Figure 7**: a,b) Simulated and experimental beam cross-section at the M5 position for 633 nm wavelength. Scale bars represent 10 mm. c,d) Simulation and experiment of the secondary source (SS) after the elliptical focusing mirror (M5) at 1.24 μm and 980 nm wavelengths, respectively.

Figure 8 shows the supports and stages for the primary optical elements for IMBUIA. The first element M1 is mounted on a custom long travel linear stage (150 mm in vertical) that will be used in special situations when M1 cannot be exposed to the full synchrotron beam (vacuum or thermal failures). M1 stage should not be used for beam alignment purposes. M2, M3 are be mounted on commercial 2-axis (Rx, Ry) kinematic mounts driven by picomotors. M4 is mounted on two commercial stages: *i)* a long travel Z-stage (103 mm) that allows the selection of the beam to the IMBUIA-micro station and *ii* a 5-axis stage (Rx, Ry, XYZ) for alignment and collimation purposes of the beam towards the W3 window. All the stages in Figure 8 are ultra-high vacuum (UHV) compatible and controlled by either step motors or piezo drivers.

![mirrors-mounts](/img/beamlines/imbuia/mirrors_mounts.jpg)

-   **Figure 8**: Mirrors mounts and stages. a) M1 long travel vertical stage (Y) manufactured by UHV Design Ltd. b) 2-axis (Rx, Ry) kinematic mount for M2 and M3 manufactured by Newport. c) Long travel linear stage (Z) manufactured by Smaract and d) 5-axes stage (Rx, Ry, XYZ) for positioning M4 manufactured by Newport.

Table 2 shows the complete list os specifications of the mirrors and respective positioning mechanisms.

| Optical element | L \[mm\] | Substrate | Reflecting surface | Manufacturer (Model) | Surface quality | Surface shape | RFL \[mm\] | Mounts & stages | Degrees of freedom | Environment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1  | 1200 | GlidCop® | Gold | Thales SESO   <br>custom | // ⩽ 3 arcmin   <br>⏥ < λ/10 @ 633 nm (RMS) | Plane | \-  | UHV Design Ltd (PLSMT38, **Fig.8a**) | Y (100 mm) | Ultra-high vacuum |
| M2  | 3790 | UV Fused Silica | Gold | Thorlabs   <br>PF20-03-M03 | // ⩽ 3 arcmin   <br>⏥ < λ/10 @ 633 nm (RMS) | Plane | \-  | Newport (8822-AC-UHV, **Fig.8b**) | Rx,Ry (±40 mrad) | Ultra-high vacuum |
| M3  | 4160 | UV Fused Silica | Gold | Thorlabs   <br>PF20-03-M03 | // ⩽ 3 arc-min   <br>⏥ < λ/10 @ 633 nm (RMS) | Plane | \-  | Newport (8822-AC-UHV, **Fig.8b**) | Rx,Ry (±40 mrad) | Ultra-high vacuum |
| M4  | 4250 | Aluminum | Gold | Thales SESO   <br>custom | ρ < 100 Å   <br>RWE < λ/4 @ 633 nm (RMS) | Paraboloid | 4071 | Smaract (SLS-92152, **Fig.8c**), Newport (8081M-UHV, Fig.8d) | Rx,Ry (±70 mrad), XYZ (±3 mm), Z (103 mm) | Ultra-high vacuum |
| M5  | 5200 | Aluminum | Gold | Thales SESO   <br>custom | ρ < 100 Å   <br>RWE < λ/4 @ 633 nm (RMS) | Ellipsoid | 5200, 539 | Newport (8822-AC-UHV, **Fig.8b**) | Rx,Ry (±40 mrad) | Air/N~2~ |
| M6  | 6040 | Aluminum | Gold | Thorlabs   <br>MPD169-M03 | ρ < 100 Å   <br>RWE < λ/4 @ 633 nm (RMS) | Paraboloid | 154 | Thorlabs (KM100) | Rx,Ry (±40 mrad) | Air/N~2~ |

-   **Table 2**: Summary of specifications for the primary optical elements of IMBUIA. Coordinates system based on the general conventions for [Sirius](https://wiki-sirius.lnls.br/mediawiki/index.php/Machine:Coordinate_System_and_Conventions). L = longitudinal distance from the source origin, ρ = roughness, RFL = reflected focal length, RWE = reflected wavefront error, // = parallelism and ⏥ = flatness.

Table 3 shows the specifications optical-vacuum windows of the beamline

| Optical window | L \[mm\] | Window material | Thickness \[µm\] | Manufacturer, Model | Transmission range | Environment |
| --- | --- | --- | --- | --- | --- | --- |
| W1  | 1621 | Diamond CVD | 500 | Diamond Materials, ø25 mm | THz to UV | UHV-UHV |
| W2  | 4934 | BaF~2~ | 4000 | Hositrad, ø50 mm | 500 nm to 30 µm | HV-Air |
| W3  | 14199 | BaF~2~ | 4000 | Hositrad, ø50 mm | 500 nm to 30 µm | HV-Air |

-   **Table 3**: Summary of specifications for the optical/vacuum windows of the IMBUIA primary optics. L = longitudinal distance from the source origin.

## Vacuum layout

The vacuum concept have two main objectives: *i)* to be compatible to the requirements of the storage ring since the first optical element almost inside the B2 pumping station and *ii)* to offer a humidity-free path for the IR radiation. Despite UHV is not required, the use of ion pumps is mandatory as it avoids extra mechanical noise in the station. The sketch in Figure 9 presents the main idea for the vacuum components for this beamline.

![vacuum-layout-sketch.png](/img/beamlines/imbuia/vacuum-layout-sketch.png)

-   **Figure 9**: Whiteboard with preliminary thoughts for the vacuum setup for the IMBUIA beamline. Credits: Thiago Miguel, Gustavo Rodrigues and Rafael Molena.

Figure 10 shows the actual vacuum layout installed in the IMBUIA beamline. The first gate valve (GV1) is responsible for isolating the vacuum environment of the storage ring from the M1 chamber when it is in retracted position (case of failure of M1). Bellow the M1 mirror, a non evaporable getter (NEG) cartridge is installed for enhancing the vacuum in the nearby volume. GV2 and GV3 gate valves are responsible for isolating the vacuum paths of the IMBUIA and CATERETÊ beamlines. A CVD diamond window (W1) is installed right after GV3 for isolating the storage ring vacuum from the experimental stations vacuum environments. Before the shielding wall, an ion pump (PMP1) is installed in the gamma shutter chamber together with a pressure sensor (VPS1) and pre-vacuum all-metal angle valve (AV1). A gate valve (GV4) is the last vacuum component inside the accelerator tunnel. Right after the wall, a mirror box (M2-M4) is responsible for delivering the beam to the experimental stations, where a pressure sensor (VPS2) and pre-vacuum all-metal angle valve (AV2) are installed. Towards the IMBUIA-nano station, a BaF~2~ IR window (W2) separates UHV and air environments. Towards the IMBUIA-micro station, a pair of ion pumps (PMP2 and PMP3) and gate valves (GV5 and GV6) keep an ultra low pressure in a ∼\\sim∼ 10 m beam path. Finally, a pressure sensor (VPS3) and pre-vacuum all-metal angle valve (AV3) allow monitoring and pumping the volume right before a BaF~2~ IR window (W3).

![imbuia-vac-full-layout.png](/img/beamlines/imbuia/imbuia-vac-full-layout.png)

-   **Figure 10**: IMBUIA vacuum layout. Up to the first window (W1), the vacuum of the beamline is shared with the storage ring and is connected to the pre-frontend of the Caterê beamline. After the shielding wall, the vacuum path is extended to the two experimental station of the beamline (IMBUIA-nano and IMBUIA-micro stations).

Table 4 lists all the vacuum components of the IMBUIA beamline followed by their main specifications.

| Element | L \[mm\] | Description | Model | Manufacturer | Actuator/control |
| --- | --- | --- | --- | --- | --- |
| GV1 | 1200 | All-metal gate valve CF40 + angle valve CF16 bypass | series 481 + series 541 | VAT | Manual |
| NEG1 | 1200 | NEG cartridge | Z200 | Saes Group | \-  |
| GV2 | 1338 | All-metal gate valve CF16 | series 481 | VAT | Pneumatic |
| GV3 | 1576 | All-metal gate valve CF40 + angle valve CF16 bypass | series 481 + series 541 | VAT | Pneumatic |
| W1  | 1621 | CVD diamond window - 25 mm | UHV window | Diamond Materials | \-  |
| VPS1 | 2032 | Cold cathode pressure sensor | 422 | MKS | \-  |
| AV1 | 2032 | All-metal angle valve CF63 | series 541 | VAT | Manual |
| PMP1 | 2032 | Ion pump 100 l | 100L-CV-8S-SC-220-N | Gamma Vacuum | \-  |
| GV4 | 2233 | All-metal gate valve CF63 | series 482 | VAT | Pneumatic |
| W2  | 4943 | BaF~2~ window - 50 mm | HV window | Hositrad | \-  |
| VPS2 | 4117 | Cold cathode pressure sensor | 422 | MKS | \-  |
| AV2 | 4117 | All-metal angle valve CF63 | series 541 | VAT | Manual |
| PMP2 | 5168 | Ion pump 200 l | 200L-CV-8D-SC-220-N | Gamma Vacuum | \-  |
| GV5 | 5450 | Gate valve CF63 | series 108 | VAT | Pneumatic |
| PMP3 | 9675 | Ion pump 200 l | 200L-CV-8D-SC-220-N | Gamma Vacuum | \-  |
| GV6 | 13877 | Gate valve CF63 | series 108 | VAT | Pneumatic |
| VPS3 | 14047 | Cold cathode pressure sensor | 422 | MKS | \-  |
| AV3 | 14047 | All-metal angle valve CF63 | series 541 | VAT | Manual |
| W3  | 14199 | BaF~2~ window - 50 mm | HV window | Hositrad | \-  |

-   **Table 4**: Summary of specifications for the optical/vacuum windows of the IMBUIA primary optics. L = longitudinal distance from the source origin.

## Radiation protection

![imbuia-rad.png](/img/beamlines/imbuia/imbuia-rad.png)

-   **Figure 11**: IMBUIA vacuum layout. Up to the first window (W1), the vacuum of the beamline is shared with the storage ring and is connected to the pre-frontend of the Caterê beamline. After the shielding wall, the vacuum path is extended to the two experimental station of the beamline (IMBUIA-nano and IMBUIA-micro stations).

## Experimental stations

### IMBUIA-nano

Brief explanation of the s-SNOM technique and its combination with SR.

![imb-nano-overview.png](/img/beamlines/imbuia/imb-nano-overview.png)

**Figure 12**: Overview of the IMBUIA-nano station.

| Parameter | Value |
| --- | --- |
| Average temperature (hutch) | 22 ∘^\\circ∘C |
| Temperature variation (hutch) | ±\\pm± 0.5 ∘^\\circ∘C/h |
| Particles density (hutch) | 1000 particles/m^3^ |
| Typical acoustic noise level (hutch) | < 10 dB |
| Average temperature (instrument box) | 22 ∘^\\circ∘C |
| Temperature variation (instrument box) | ±\\pm± 0.5 ∘^\\circ∘C/h |
| Relative humidity (instrument box) | < 3% |

-   **Table 5**: Station environmental conditions.

> **Topics to be added**

-   [x] Environmental conditions
-   [ ] Clean nitrogen line
-   [ ] Compressed air
-   [ ] Power outlets
-   [ ] No-break system
-   [ ] Controllers cabling and connections
-   [ ] Neasnom server: cables/connectors/switches
-   [ ] Lasers: cables/connectors/switches

### IMBUIA-micro

![commissioning.png](/img/beamlines/imbuia/commissioning.png)

The IMBUIA-micro station is still under technical commissioning. This section will be added as soon as it starts operation with synchrotron radiation.

## Beam and experiment diagnostics

### M1 camera and temperature readings

### Secondary source

### Collimation

### Synchrotron power, near-field signal levels and spectral response

### DFG laser power, near-field signal levels and spectral response

### QCL laser: standard PsHet imaging

## Control interfaces

### Hvac

### Vacuum sensors and power supplies

### Shutter operation

### Primary optics mirrors

### Compressed air and nitrogen flow control

### Beamline cameras

### Remote access: beamline IHM

### IMBUIA archiver

### Remote access: Neasnom client

## Data storage and processing

### Accessing and saving data in the Ibira storage

### Browsing data in the Neasnom server

### Visualization and post-processing data with Orange

### Visualization and post-processing data NeaPlot

## Safety guidelines

### Liquid nitrogen handling

### Laser beams risks

### Monitoring the oxygen level in the hutch

### In case of emergency

### Allowed chemicals in the hutch

## Recommended lab practices and procedures

### Semi-clean room dress code

### Watch out for sensitive optical components

### Samples handling

### AFM tips replacement

### Mind the acoustic noise level in the hutch

### Do not speak over the samples or optical elements

### Keep it clean and neat

## Troubleshooting

### What to do in case of power failure?

### How to re-open the photon shutter?

### How to reset the oxygen sensor alarm?

### My spectrum is weak or null, what do I do?

> Written with [StackEdit](https://stackedit.io/).