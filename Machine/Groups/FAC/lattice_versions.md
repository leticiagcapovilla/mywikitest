---
title: Sirius lattice versions
description: 
published: 1
date: 2024-03-19T19:18:05.571Z
tags: 
editor: markdown
dateCreated: 2024-03-19T19:18:05.571Z
---

# FAC: Sirius lattice versions

In the course of the Sirius project's history, each submachine has been tagged with a version string identification. This identification consists in a two-letter initial indicating the submachine, a lattice version and, optionally, an identification of the optics of the lattice. Letters SI refer to the storage ring, TS refers to the booster to storage ring transport line, BO to the booster, TB refers to the linac to booster transport line and finally, LI refers to the linac.

Storage ring

SI.V23: jun/2018.

- (jun/2018). 29/05/2018 magnets that will be used as the fast correctors close to the BC magnet will have the shape of a normal quadrupole in the sections where there are the diagnostic eamlines. Hence it will not be possible to have skew quads there.

SI.V22: may/2017. (current documented version - in progress). 

- (may/2017). The BPM upstream of dipole B2 was moved by 50mm (closer to B2) to fit in the girder. Modification in sectors C1 and C3. This change was requested by the Mechanical Design Group. 

SI.V21: set/2016. 

- (out/2016). The fast corrector after BC was moved by 17 mm to avoid collision with Q3 coils. This change was requested by the Projects Group. 
- The BPM after dipole BC is moved to the other side of quadrupole Q4 and the fast corrector is moved to the other side of sextupole SFx2. In this way we avoid collision between the BMP and the BC beamline. 

SI.V20: jul/2016. 

- (ago/2016). The FC (fast corrector) position in low beta matching sectors has been changed by 9 mm to avoid collision with quadrupole coils. Since this change doesn't affect any of the calculations already performed, we kept the same version, SI.V20.01.
- The extra sextupole magnet SDx4 has been removed and the stand-alone booster vertical corrector CV is returned. An additional coil is introduced in the fast corrector to generate the QS necessary to apply BBA in the BPM next to BC. A new family FCQ (fast correctors with QS coil) has been created.
- FCQ is moved from the central region of the C2 sector to its extremity, close to dipole BC and the BPM.
- The QS in sextupole SDx2 has been removed. The total number of QS is 100 in this version.

SI.V19: jun/2016. 

- An extra sextupole magnet SDx4 in straight C2 close to BC has been added to allow BBA in the BPM close to BC. Only the QS and CV coils are used, the main sextupole coils are not used. The stand-alone CV has been removed.

SI.V18: jun/2016. 

- QS coils are 'turned-on' in some sextupoles to allow for BBA in BPMs close to them: SDx2 in sector C1 and SDx3 in sector C3. x = A, B, P 
- Sextupoles containing QS and CH/CV in the matching cells of high beta sections (A) have been exchanged to allow BBA in the BPM close to SFA0. In summary, CH/CV moved to SDA0 and QS moved to SFA0.
- For the low beta sections (B and P) the original configuration is preserved (that is CH/CV in SFB0/SFP0 and QS in SDB0/SDP0) since there are quadrupoles QDB2 close to the BPM.
- The total number of QS in the ring increased from 80 to 120.

SI.V17: jun/2016.

- Corrector CV and BPM next to BC moved away from it by 70 mm and 40 mm respectively.
- Position of dipole kicker (DIPK) moved closer to nonlinear kicker NLK. 

SI.V16: apr/2016.

- Symmetry 5 optics with one high and three consecutive low beta function straight sections. There are 21 independent sextupole families.

SI.V15: apr/2016. 

- Symmetry 5 optics with one high and three consecutive low beta function straight sections. There are 28 independent sextupole families.

SI.V14: dec/2015 

- Default sextupole strengths and optics mode has moved to C03, making the dynamics more robust to ID perturbations.
- The distance between dipole B1 and quadrupoles QDB1 and QDA (in the matching section) has been increased by 10 cm to allow moving the pumping station from B1B upstream to downstream. To keep the same ring circumference, the long straight sections have been reduced by the same amount.
- Fast correctors at the injection and RF cavity straight sections have been restored. In this way, all straight sections are the same regarding fast correctors.

SI.V13: oct/2015. 

- A new BC magnet design with a physical length of 912.52 mm (with end-plates). High field region is narrower in this new design.
- injection point has moved due to new transfer line TS.V02. On-axis kicker and PMM moved as well. Lattice BPMs are kept in injection straight section (in version V12 they were removed).
- Fast correctors at the injection and RF cavity straight sections have been removed
- Default optics mode C02 is optimized with Insertion Devices included to avoid 4-th order resonance that shows up and that was reducing the beam long-term stability. 
- (modelling) Also systematic multipoles from fieldmap analysis of the 3D magnet model have been added to the nominal lattice model.
- (modelling) In the model all magnet lengths were truncated to multiples of millimeters.

SI.V12: oct/2015. 

- New slow correction system so that orbit may be better corrected at radiation exits. The modifications are: 
- All radiation source points, comprising ID straights and BC dipoles, are now surrounded by BPMs, there is no longer any magnetic element from the lattice between the BPM and the light source point. 
- A BPM from the C2 section has been removed, decreasing the total number of BPMs in the ring by 20 units, from 180 to 160.
- A vertical corrector has been added before BC, next to it. This corrector can be of the Booster CV type since it has the same maximum strength specification. In total there are 20 of these correctors in the ring.
- Another extra vertical corrector coil combined with the sextupole SF2 in sector C3 has been added. This sextupole, which had only CH before, will now have CH and CV coils.
- The total number of vertical corrector power supplies has increased by 40 in this new version, from 120 to 160. The number of horizontal correctors remains the same, 120.
- The fast corrector positions have changed according to the new arrangement of BPMs.
- The sextupoles SF2J and SF2K were displaced by a small amount to allow placing the fast correctors closer to BC.

SI.V10: jun/2015. 

- Change in the straight sections: QDA/QDB1 changed positions with SDA/SDB sextupoles; QDB2 brought closer to QFB; longer straight sections (6.5/7.5m). 
- New Q14, Q20 and Q30 models (different physical lengths and systematics multipoles). 
- Change of sextupole family names: from sd1/sf1/sd2/sd3/sf2/sd6/sf4/sd5/sd4/sf3 to sd1j/sf1j/sd2j/sd3j/sf2j/sd1k/sf1k/sd2k/sd3k/sf2k. 
- The number of horizontal correctors used in the correction loop was diminished to 120. Now the sextupoles with correctors are: CH --> sd1j/sf2j/sd1k/sf2k/sfa/sfb | CV --> sd1j/sd3j/sd1k/sd3k/sfa/sfb.

SI.V09: jun/2015. 

The magnets B3 and BC were redesigned into a single permanent magnet, named BC. The central field changed from 2T to 3.2T. Few BPMs were moved: the BPMs on the straights were moved to the other side of the focalizing quadrupole, due to request of the vacuum group; the BPM close to the B1 dipole was moved to be close to the B2 dipole. 

SI.V08: mar/2015. 

Skew quadrupole correctors moved from sextupole to fast correctors magnets.

SI.V07: mar/2015. 

Small dislocations in sextupoles and quadrupoles. Circumference pinned to 518.396 m. Fast correctors CHF and CVF moved out from sextupole magnets. New MOGA optimization adopted (firstRun_000493.m). skew quadrupole correctors in SDA, SF1, SF4 and SDB sextupole families. New BC model with 12 segments being used. 

SI.V06: fev/2015. 

Length of quadrupoles: 14 cm, 20 cm and 30 cm.

SI.V05: fev/2015. 

The length of the quadrupoles are changed as follows: from 25 cm and 14 cm to 20 cm; from 34 cm to 25 cm.

SI.V04: fev/2015. 

In this version the model for dipoles B1, B2 and B3 have been changed to reflect the decision to use rectangular straight unit blocks to composed them. Each dipole magnetic length considers 396 mm blocks, 7 mm spacing between blocks and 29 mm gap. Note that the entrance and exit angle for all dipoles are now the same. The BC deflection is increased from 1.4 to 1.468 degrees, according to the magnet model. B1 uses 2 blocks, B2 uses 3 blocks and B3 uses 1 block.

SI.V03: set/2014. 

Corretoras H e V estão juntas. Retirado um bpm (saída do B3) por trecho. Redefinidas onde as corretoras rápidas ficarão.

SI.V02: set/2014. 

QFA passou de 34 cm para 25 cm. Ajustes na distância SEXT-QUAD. Corretoras aumentadas de 10 cm para 12 cm incluindo bobina. BPMs ao lado do B3 reposicionados para perto dos quadrupolos QF4 para otimizar BBA.

SI.V01: ago/2014. 

Familias de sextupolos no arco cromático foi separada: famílias antes do BC ficaram independentes das famílias depois do BC, ou seja não temos mais simetria de espelho para os sextupolos em relação ao BC.

SI.V00: ago/2014. 

Esta é a mesma versão que a v500. Reniciamos a numeração das versões.

SI.V500: nov/2013. 

Comprimento dos trechos retos ajustados para freqüência de RF de 499.654MHz. A circunferência passou de 518.25m para 518.396m. Aumento de 2 x 0,00365m nos trechos retos de inserção LIA e LIB.

SI.V403: 

bpms dos trechos dos IDs deslocados para posição entre SA2 e QAF (alto beta) e SB2 e QBF (baixo beta). Adicionado 1 bpm após o B3. Os sextupolos SA2 e SB2 tiveram que ser deslocados de 7 cm para mais longe dos quadrupolos.

SI.V402: 

deslocamento de 3cm da corretora vertical para mais longe do B2.

SI.V401: 

deslocamento de 4cm das corretoras para mais perto do B1.

SI.V400: 

a rede que apresentou melhor resultado nos testes foi a v350, com 180 bpms, 180 corretoras horizontais e 160 corretoras verticais e ainda, com todos os bpms longe das saídas de luz e sem o bpm no centro do BC. A partr dela, fizemos a v400, que ainda possui três alterações: alguns sextupolos foram deslocados 1.5cm para mais perto do quadrupolo mais próximo, para padronizar as distâncias entre elementos em inteiros de cm; as corretoras que estavam juntas foram separadas, e as corretoras simetrizadas em relação ao BC, apesar de os bpms não serem simétricos;

SI.V310: 

geramos uma rede com 200 bpms e 200 corretoras verticais para estudar o melhor posicionamento dos elementos, tentanto recuperar os resultados do antigo sistema de correção de órbita. redes v310, v320, v330, v340, v350 foram geradas.

SI.V300: 

mudança dos bpms para longe das saídas de luz e junção de corretoras verticais e horizontais próximas em apenas um magneto (alteração significativa no sistema de correção de órbita);

SI.V200: initial version

Booster to storage ring transport line

TS.V03: jun/2016

- Both booster extraction septa (thin and thick) had the magnetic fields increased to the same value of the storage ring injection septa. The angles are kept the same so the lengths are now shorter.
- The thick injection septa uses the same design as the thick extraction septum, so that there is now only one design for the thick injection and extraction septa. In this way the deflection angle of the thick injection septa is increased from 3.12 to 3.6 degree and the BTS dipole angles were reduced from 5.333 to 5.012 degree.

TS.V02: oct/2015

- BO.V02A, tentative dipole model 6 split into two parts. Its current has been adjusted as to generate nominal deflection angle while its integrated quadrupole and sextupole fields have changed. In this model the segments are pressed with one type of end plate.
- Thick and thin storage ring injection septa replaced by 3 identical injection septa. 
- Updated models of quadrupoles, sextupoles with corrected effective lengths. updated segmented model of dipoles.

TS.V01:
TS.V500:
TS.V300:
TS.V200:
TS.V100: initial version

Booster

BO.V04 : 30/05/2017. 

Straight sections with the sequence (Bend-SD-CV) (there are 5 of these in the Booster): CV was moved by 100mm away from SD to avoid the dipole chamber flange. Change requested by the Vacuum Group.

BO.V03 : 14/10/2016. 

a 10-cm skew quadrupole was introduced at sector 02D in order to allow for coupling up to 5%.

BO.V02 : 11/04/2016. current documented version. 

Dipoles are one-block magnets.
BO.V02.01 - 3D field model data for systematic multipoles of sextupoles are included.
BO.V02.02 - rotating coil measurements of systematic multipoles of sextupole magnets are included.
BO.V02.03 - New 3D field model data for systematic multipoles of sextupoles with multipole fitting of all the even monomials. (OFFICIAL)

BO.V01 : ago/2015. 

Lengths of hardedge models for sextupoles and QD were changed from 0.2 to 0.1 meters. The centers of these magnets were also shifted along the ring.

BO.V901 : --

BO.V900 : 03/10/2014.

Alterada posição do septum de extração para antes do quadruplo e feitos pequenos ajustes nas posições dos kickers de extração e injeção. A posição do BPM e CH no trecho de extração também foram alteradas.

BO.V800 : 12/11/2013.

O número de SD's aumentou para 10, voltamos a modelar o dipolo de acordo com o modelo hard-edge convencional (FINT=0).

BO.V600 : 01/04/2013.

Modelo com corretoras separadas e FINT=0.5 no dipolo. As distâncias entre os elementos (sextupolo-dipolo, corretora-dipolo, corretora-quadrupolo) )foi ajustada para ficar mais realista.

Linac to booster transport line

TB.V02: Aug/2017

- New dipole model 02.

TB.V01:
TB.V300:
TB.V200:
TB.V100: initial version