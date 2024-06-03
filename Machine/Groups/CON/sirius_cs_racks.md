---
title: Sirius control system racks
description: 
published: 1
date: 2024-06-03T21:26:37.449Z
tags: 
editor: markdown
dateCreated: 2024-06-03T21:08:07.259Z
---

# CON: Sirius control system racks

<br>

## Introduction

The Controls group will count on 24 racks to install its components, including [[CON:Sirius_control_system_servers|servers]], [[CON:Sirius_control_system_network|switches]] and control hosts. The [https://www.rittal.com/de_de/ts-it/public/index.php/en TS IT] developed by the German company [https://www.rittal.com/com-en/content/en/start/ Rittal] was chosen as the model and two different depths were acquired, according to the individual needs of each room.

<br>

## Amount and functions

The table below summarizes the location, count and physical dimension of our racks.

| Amount| Physical |
| |
|Dimensions (mm) |
|	Location |
|20| 600x800| Rack rooms around the ring |
|1| 600x800| RF room |
|1| 600x1000| High power supply room |
|1| 600x1000| Connectivity room |
|1| 600x1000| LINAC klystron room  |

<br>

## Internal organization

This section describes the internal organization for each group of racks.

The proposed internal assembling models can be found [here](https://docs.google.com/spreadsheets/d/1LKvopICk3yRigLOoKa1PeqR0IQa8sIx_pQtwNyGZ84I/edit?usp=sharing).

<br>

### Rack rooms with only one Aruba 2930M switch

In this kind of rooms, we count on two switches: one [2930M](http://www.arubanetworks.com/assets/ds/DS_2930MSwitchSeries.pdf|Aruba) and another [1810-24G](https://h20195.www2.hpe.com/v2/GetDocument.aspx?docname=4AA4-6971ENW&doctype=data%20sheet&doclang=EN_US&searchquery=&cc=th&lc=en|HP). The rack dimensions, in millimeters, are 600x800.

<br>

### Rack rooms with two 2930M switches

Two [2930M](http://www.arubanetworks.com/assets/ds/DS_2930MSwitchSeries.pdf|Aruba) switches and other two [1810-24G](https://h20195.www2.hpe.com/v2/GetDocument.aspx?docname=4AA4-6971ENW&doctype=data%20sheet&doclang=EN_US&searchquery=&cc=th&lc=en|HP) are needed for rooms '''01''' and '''19/20''', due to the bigger amount of connections on these sectors. As in the previous section, these are 600x800mm racks.

<br>

### RF room

The Controls group has a rack in the RF room as well. In this case, we use three Aruba 2930M switches dedicated for the RF systems. No HP 1810 switches are used here.

<br>

### High power supplies room

The connection density in the power supply room is high: five Aruba 2930M switches are used in total. As all other racks in this room are wider, we chose to use a 600x1000 rack too.


'''Ethernet Patch Panel'''

|Slot #| IP| Description |  |Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----|  ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| -----|  |
|9| -----|  ||21| -----|  |
|10| -----|  ||22| -----|  |
|11| -----|  ||23| -----|  |
|12| -----|  ||24| -----|  |

<br>

### LINAC klystron room

Our rack in the LINAC klystron room is going to be the root of half of our star topology. A 600x1000mm rack will be placed in this room.

<br>

### Connectivity room

This room will host one of our [core switches](/Machine/Groups/CON/sirius_cs_network) and one of our [servers](/Machine/Groups/CON/sirius_cs_servers). As consequence, this rack must be wider: 600x1000mm.


'''Ethernet Patch Panel - Top'''

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|
|1| -----| [POE] CountingPRU - LTB 1 ||13| -----|  |
|2| -----| [POE] CountingPRU - LTB 2 ||14| -----|  |
|3| -----| [POE] DIG Camera - LTB 1 ||15| -----|  |
|4| -----| [POE] DIG Camera - LTB 2 ||16| -----|  |
|5| -----| [POE] DIG Camera - LTB 3 ||17| -----|  |
|6| -----| DIG Galil - LTB 1 ||18| -----|  |
|7| -----| DIG Galil - LTB 2 ||19| -----|  |
|8| -----| DIG Galil - LTB 3 ||20| -----|  |
|9| -----| DIG Fenda de Energia 1H ||21| -----|  |
|10| -----| DIG Fenda de Energia 1V ||22| -----|  |
|11| -----| DIG Fenda de Energia 2H ||23| -----|  |
|12| -----| DIG Fenda de Energia 2V ||24| -----|  |


'''Ethernet Patch Panel - Bottom'''

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|
|1| -----| LINAC Controls Room #1 ||13| -----| LINAC Controls Room #13 |
|2| -----| LINAC Controls Room #2 ||14| -----| LINAC Controls Room #14 |
|3| -----| LINAC Controls Room #3 ||15| -----| LINAC Controls Room #15 |
|4| -----| LINAC Controls Room #4 ||16| -----| LINAC Controls Room #16 |
|5| -----| LINAC Controls Room #5 ||17| -----|  |
|6| -----| LINAC Controls Room #6 ||18| -----|  |
|7| -----| LINAC Controls Room #7 ||19| -----|  |
|8| -----| LINAC Controls Room #8 ||20| -----|  |
|9| -----| LINAC Controls Room #9 ||21| -----|  |
|10| -----| LINAC Controls Room #10 ||22| -----|  |
|11| -----| LINAC Controls Room #11 ||23| -----|  |
|12| -----| LINAC Controls Room #12 ||24| -----|  |


'''SERIALxxCON - Serial Networks'''

|Boards| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 	|10.128.122.101| Temperature Monitor - MBTemp - LTB & UPS Monitoring|
|2| 	| 10.128.122.160| Temperature and Humidity Monitor - Linac |
|3| 	|	 | |
|4| 	|	 | |
|5| 	|	 | |

<br>

### Room 01

'''Ethernet Patch Panel'''

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|
|1| -----| [POE] CountingPRU - LTB 3 ||13| -----| DIG Galil - LTB 6 |
|2| -----| [POE] CountingPRU - LTB 4 ||14| -----| DIG Galil - Booster 1 |
|3| -----| [POE] CountingPRU - LTB 5 ||15| -----| DIG Galil - Booster 2 |
|4| -----| [POE] CountingPRU - Booster ||16| -----| DIG Galil - Booster 3 |
|5| -----| [POE] DIG Camera - LTB 4 ||17| -----| DIG - Scrapper 03 |
|6| -----| [POE] DIG Camera - LTB 5 ||18| -----| DIG - Scrapper 04 |
|7| -----| [POE] DIG Camera - LTB 6 ||19| -----| Diagnostics Beamline |
|8| -----| [POE] DIG Camera - Booster 1 ||20| 10.128.101.151| [POE] CountingPRU - Trecho 1 M2 |
|9| -----| [POE] DIG Camera - Booster 2 ||21| 10.128.101.152| [POE] CountingPRU - Trecho 1 C2 |
|10| -----| [POE] DIG Camera - Booster 3 ||22| 10.128.101.153| [POE] CountingPRU - Trecho 1 C3 |
|11| -----| DIG Galil - LTB 4 ||23| 10.128.101.154| [POE] CountingPRU - Trecho 1 M1 |
|12| -----| DIG Galil - LTB 5 ||24| -----| General Purpose BC  |}







'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold;
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 94
| style="font-size:10px; text-align:center;  " | 10.128.101.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10p0px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| stypx; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.101.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|----
| style="font-size:10px; text-align:center; " colspan="4" | Note: IPs 107 and 108 '''are reserved''' for EPP.
|}

### Room 02


'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Descriptionfont-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; fon
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="tent-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.102.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 2 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}





'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center; width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center; width="80px" | SERIALxxCON ID
! style="font-weight:bold; f
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 62
| style="font text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.102.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1 
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.102.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 03

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; foer; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.103.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 3 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:ize:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10ize:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.103.121
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP 1 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.103.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Right 2
|}

### Room 04

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" styl; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-px; text-align:center;  " | 10.128.104.104
| style="font-size:10p10px; text-align:center;  " | 301
| style="font-size:10px; text-align:center;  " | 10.128.104.118
| style="font-size:10pe:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.104.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 05

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - BC
|-er; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:centernter; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 5 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.105.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 5 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold;x; text-align:left;    " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.105.132
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 06


'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center;
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:centeer; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 6 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.106.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 6 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weightext-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.106.104
| style="font-size:10pxtext-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC ->)
|-
| style="font-size:10px;0px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.106.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.106.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 07

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" s font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center;r; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 7 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.107.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 7 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.107.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 7 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-wei
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.107.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.107.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 08

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Descriptiongn:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-si font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.108.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 8 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bol0px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10ppx; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.108.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 09

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px"; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; ffont-size:10px; text-align:left;  " | 
|-
| style="text-align:center; rfont-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 9 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; fontext-align:center;  " | 10.128.109.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->) 
|-
| style="font-size:10px; text-a
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " |
| style="font-size:1
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.109.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 10

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; f fonont-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:10px; text-align:left;  " | [POE] CountingPRU - Trecho 10 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weig
| style="font-size:ze:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.110.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 11

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" stenter; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; fnter; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 11 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.111.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 11 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 11 
|-
|}


'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; fonx; text-align:left;    " | Temperature Monitor - MBTemp - Booster
|-px; text-align:cen:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.111.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 12

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-wze:10px; text-align:center;" | 6
| style="text-align:center; font-ize:10px; text-align:center;" | -----
| style="text-align:center; font-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.112.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 12 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 12 
|-
|}


'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weig:10px; text-align:center;  " | 
| style="font-size:10px; -align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.112.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.112.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}



### Room 13

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Descriptionnt-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-t-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 13
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:baliext-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.113.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2 
|}


### Room 14

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|--size:10px; text-align:le; font-size:10px; text-align:center;" | 10.128.114.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 14 C2
|-
| style="text-align:center; font-sont-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.114.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 14 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 14
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold;ext-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.114.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2 
|}


### Room 15

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center;
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.115.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 15 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 15
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:b; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 16

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" st
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 16
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; fxt-align:center;  " | 221
| style="font-size:10px; text-align:center;  " | 10.128.116.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-0px; text-align:centeze:1ext-align:center;  " | 10.128.116.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.116.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2 
|}


### Room 17

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style-size:10px; text-align:center;" | -----
| style="text-align:center; font-size; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-; font-size:10px; text-align:center;" | 10.128.117.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 17 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 17
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-siz
| style="font-size:10px; text-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; texxt-align:center;  " | 10.128.117.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.117.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 18-I

'''Ethernet Patch Panel'''


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-w0px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; fonont-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 18 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.118.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 18 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 18
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font--align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:; text-align:center;  " | 10.128.118.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.118.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}


### Room 18-II

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.119.153
| style="text-align:center; fonnt-size:10px; text-align:center;" | 10.128.119.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 19 M1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU Booster - Trecho 19
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px;
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.119.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 19/20

'''Upper Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style=
|-nt-size:10px; text-align:center;" | -----
| style="text-align:center; font--size:10px; text-align:left;  " | 
|-font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG - Scrapper 01
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG - Scrapper 02
|-
|}


'''Lower Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="fze:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; foont-size:10px; text-align:center;" | 10.128.120.151
| style="text-align:center; fontt-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.120.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 20 M1
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-silign:center;  " | 10.128.120.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring; text-align:center;  " | 10.128.120.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|---
| style="font-size:10px; text-align:center; "  colspan="4" | Note: IPs 107 and 108 '''are reserved''' for EPP.
|}


### Room 21 (Transport Lines)

'''Ethernet Patch Panel'''

{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="f
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; ; font-size:10px; text-align:left;  " | 
|-font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}



'''SERIALxxCON - Serial Networks'''

[[File:Racks_SERIALxxCON.png|350px|thumb|left]]


{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | Board Location
! style="font-weight:bold; font-ext-align:center;  " | 399
| style="font-size:10px10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10p
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|}
