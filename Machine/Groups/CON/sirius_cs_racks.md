---
title: Sirius control system racks
description: 
published: 1
date: 2024-06-03T21:13:34.804Z
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

|Slot #| IP| Description |
|1| -----| [POE] CountingPRU - LTB 1 |
|2| -----| [POE] CountingPRU - LTB 2 |
|3| -----| [POE] DIG Camera - LTB 1 |
|4| -----| [POE] DIG Camera - LTB 2 |
|5| -----| [POE] DIG Camera - LTB 3 |
|6| -----| DIG Galil - LTB 1 |
|7| -----| DIG Galil - LTB 2 |
|8| -----| DIG Galil - LTB 3 |
|9| -----| DIG Fenda de Energia 1H |
|10| -----| DIG Fenda de Energia 1V |
|11| -----| DIG Fenda de Energia 2H |
|12| -----| DIG Fenda de Energia 2V |
| |
|Slot #| IP| Description |
|13| -----|  |
|14| -----|  |
|15| -----|  |
|16| -----|  |
|17| -----|  |
|18| -----|  |
|19| -----|  |
|20| -----|  |
|21| -----|  |
|22| -----|  |
|23| -----|  |
|24| -----|  |



'''Ethernet Patch Panel - Bottom'''

|Slot #| IP| Description |
|1| -----| LINAC Controls Room #1 |
|2| -----| LINAC Controls Room #2 |
|3| -----| LINAC Controls Room #3 |
|4| -----| LINAC Controls Room #4 |
|5| -----| LINAC Controls Room #5 |
|6| -----| LINAC Controls Room #6 |
|7| -----| LINAC Controls Room #7 |
|8| -----| LINAC Controls Room #8 |
|9| -----| LINAC Controls Room #9 |
|10| -----| LINAC Controls Room #10 |
|11| -----| LINAC Controls Room #11 |
|12| -----| LINAC Controls Room #12 |
| |
|Slot #| IP| Description |
|13| -----| LINAC Controls Room #13 |
|14| -----| LINAC Controls Room #14 |
|15| -----| LINAC Controls Room #15 |
|16| -----| LINAC Controls Room #16 |
|17| -----|  |
|18| -----|  |
|19| -----|  |
|20| -----|  |
|21| -----|  |
|22| -----|  |
|23| -----|  |
|24| -----|  |


'''SERIALxxCON - Serial Networks'''

|Boards| SERIALxxCON ID| IP| Device |
|1| 	10.128.122.101| Temperature Monitor - MBTemp - LTB & UPS Monitoring |
|2| 	10.128.122.160| Temperature and Humidity Monitor - Linac |
|3| 		 |
|4| 		 |
|5| 		 |

<br>

### Room 01

'''Ethernet Patch Panel'''
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:cet-size:10px; text-align:left;  " | [POE] CountingPRU - LTB 5
|-
| style="textr; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.101.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 1 M1 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose BC 
|-
|}





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
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 278
| style="font-size:10px; text-align:center;  " | 10.128.112.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 277
| style="font-size:10px; text-align:center;  " | 10.128.112.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.112.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINK - Storage Ring 
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 300
| style="font-size:10px; text-align:center;  " | 10.128.112.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 312
| style="font-size:10px; text-align:center;  " | 10.128.112.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->) 
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.112.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.112.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2 
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
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
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 13 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.113.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 13 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.113.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 13 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.113.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 13 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.113.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 13 M1
|-
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
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 232
| style="font-size:10px; text-align:center;  " | 10.128.113.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 231
| style="font-size:10px; text-align:center;  " | 10.128.113.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 234
| style="font-size:10px; text-align:center;  " | 10.128.113.106
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Booster
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 236
| style="font-size:10px; text-align:center;  " | 10.128.113.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 235
| style="font-size:10px; text-align:center;  " | 10.128.113.105
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP - Booster
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 233
| style="font-size:10px; text-align:center;  " | 10.128.113.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 306
| style="font-size:10px; text-align:center;  " | 10.128.113.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 310
| style="font-size:10px; text-align:center;  " | 10.128.113.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.113.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.113.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2 
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.113.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
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
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 14 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.114.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 14 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.114.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 14 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.114.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 14 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
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
! style="font-weight:bold; font-size:12px; text-align:center;" width="80px" | SERIALxxCON ID
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 228
| style="font-size:10px; text-align:center;  " | 10.128.114.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 227
| style="font-size:10px; text-align:center;  " | 10.128.114.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 230
| style="font-size:10px; text-align:center;  " | 10.128.114.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 229
| style="font-size:10px; text-align:center;  " | 10.128.114.105
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP - Booster
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 309
| style="font-size:10px; text-align:center;  " | 10.128.114.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 321
| style="font-size:10px; text-align:center;  " | 10.128.114.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)  
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.114.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.114.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2 
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.114.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1 
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.114.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2 
|}

### Room 15

'''Ethernet Patch Panel'''
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 15 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.115.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 15 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.115.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 15 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.115.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 15 C3
|-
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
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 224
| style="font-size:10px; text-align:center;  " | 10.128.115.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 225
| style="font-size:10px; text-align:center;  " | 10.128.115.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 219
| style="font-size:10px; text-align:center;  " | 10.128.115.106
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Booster
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINK - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 226
| style="font-size:10px; text-align:center;  " | 10.128.115.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 327
| style="font-size:10px; text-align:center;  " | 10.128.115.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 316
| style="font-size:10px; text-align:center;  " | 10.128.115.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.115.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|}

### Room 16

'''Ethernet Patch Panel'''
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 16 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.116.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 16 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.116.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 16 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.116.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 16 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.116.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 16 M1

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
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 222
| style="font-size:10px; text-align:center;  " | 10.128.116.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 223
| style="font-size:10px; text-align:center;  " | 10.128.116.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 221
| style="font-size:10px; text-align:center;  " | 10.128.116.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 220
| style="font-size:10px; text-align:center;  " | 10.128.116.105
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP - Booster
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 303
| style="font-size:10px; text-align:center;  " | 10.128.116.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 326
| style="font-size:10px; text-align:center;  " | 10.128.116.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.116.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.116.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.116.131
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
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 17 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.117.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 17 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.117.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 17 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.117.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 17 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.117.154
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
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 249
| style="font-size:10px; text-align:center;  " | 10.128.117.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 250
| style="font-size:10px; text-align:center;  " | 10.128.117.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 251
| style="font-size:10px; text-align:center;  " | 10.128.117.106
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Booster
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 252
| style="font-size:10px; text-align:center;  " | 10.128.117.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 253
| style="font-size:10px; text-align:center;  " | 10.128.117.105
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP - Booster
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 254
| style="font-size:10px; text-align:center;  " | 10.128.117.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 328
| style="font-size:10px; text-align:center;  " | 10.128.117.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 261
| style="font-size:10px; text-align:center;  " | 10.128.117.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.117.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.117.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.117.131
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
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 18 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.118.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 18 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.118.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 18 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.118.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 18 C3
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
! style="font-weight:bold; font-size:12px; text-align:center;" | IP
! style="font-weight:bold; font-size:12px; text-align:center;" | Device
|-
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 218
| style="font-size:10px; text-align:center;  " | 10.128.118.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 217
| style="font-size:10px; text-align:center;  " | 10.128.118.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.118.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINK - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-

| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 262
| style="font-size:10px; text-align:center;  " | 10.128.118.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 318
| style="font-size:10px; text-align:center;  " | 10.128.118.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.118.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.118.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.118.131
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
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - Trecho 19 BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.119.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 19 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.119.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 19 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.119.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 19 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.119.154
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
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 214
| style="font-size:10px; text-align:center;  " | 10.128.119.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 216
| style="font-size:10px; text-align:center;  " | 10.128.119.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 116
| style="font-size:10px; text-align:center;  " | 10.128.119.106
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Booster
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.119.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINK - Storage Ring 
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 215
| style="font-size:10px; text-align:center;  " | 10.128.119.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 304
| style="font-size:10px; text-align:center;  " | 10.128.119.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 315
| style="font-size:10px; text-align:center;  " | 10.128.119.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->) 
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.119.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.119.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.119.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
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
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Booster
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] Basler Camera DIG (Visible Light) - Booster
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG 4 (Rack DIG)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Booster - Monitor 1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Booster - Monitor 2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Trecho 20/M1 - Monitor 1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Trecho 20/M1 - Monitor 2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Trecho 20/M1 - Monitor 3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] DIG BTS - Trecho 20/M1 - Monitor 4
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 1
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 3
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 4
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 5
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | DIG BTS - Galil 6
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
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
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | General Purpose - BC
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.120.151
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 20 M2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.120.152
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 20 C2
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.120.153
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 20 C3
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | 10.128.120.154
| style="text-align:center; font-size:10px; text-align:left;  " | [POE] CountingPRU - Trecho 20 M1
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
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 103
| style="font-size:10px; text-align:center;  " | 10.128.120.101
| style="font-size:10px; text-align:left;    " | Vacuum System - Gauge Controller MKS - LTB & Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 105
| style="font-size:10px; text-align:center;  " | 10.128.120.102
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - LTB & Booster
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.120.116
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - BTS
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 112
| style="font-size:10px; text-align:center;  " | 10.128.120.103
| style="font-size:10px; text-align:left;    " | Vacuum System - Ion Pump 4UHV - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 113
| style="font-size:10px; text-align:center;  " | 10.128.120.104
| style="font-size:10px; text-align:left;    " | Power Supplies - DCLINKs - Booster & Storage Ring
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 114
| style="font-size:10px; text-align:center;  " | 10.128.120.105
| style="font-size:10px; text-align:left;    " | Power Supplies - FBP - Booster
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 
|-
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 10.128.120.117
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (<-BC)
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 10.128.120.118
| style="font-size:10px; text-align:left;    " | Temperature Monitor - MBTemp - Storage Ring (BC->)
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.120.121
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 1 - Storage Ring - Left 1
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.120.122
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 2 - Storage Ring - Left 2
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.120.131
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 3 - Storage Ring - Right 1
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 10.128.120.132
| style="font-size:10px; text-align:left  ;  " | Power Supplies - FBP 4 - Storage Ring - Right 2
|---
| style="font-size:10px; text-align:center; "  colspan="4" | Note: IPs 107 and 108 '''are reserved''' for EPP.
|}

### Room 21 (Transport Lines)

'''Ethernet Patch Panel'''
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 1
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " |  Cable 01 to Rack LA-RaPS02 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 2
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 02 to Rack LA-RaPS02 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 3
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 03 to Rack LA-RaPS02 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 4
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 04 to Rack LA-RaPS02 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 5
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 05 to Rack LA-RaPS02 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 6
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 06 to Rack LA-RaPS04 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 7
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 07 to Rack LA-RaPS04 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 8
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | Cable 08 to Rack LA-RaPS04 (Room 21)
|-
| style="text-align:center; font-size:10px; text-align:center;" | 9
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 10
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 11
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 12
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
|}
{| class="wikitable" style="display: inline-table; margin-left: auto; margin-right: auto;"
! scope="col" width="20px" style="font-weight:bold; font-size:10px; text-align:center;" | Slot #
! scope="col" width="80px" style="font-weight:bold; font-size:10px; text-align:center;" | IP
! scope="col" width="300px" style="font-weight:bold; font-size:10px; text-align:center;" | Description
|-
| style="text-align:center; font-size:10px; text-align:center;" | 13
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 14
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 15
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 16
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 17
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 18
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 19
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 20
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 21
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 22
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 23
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
|-
| style="text-align:center; font-size:10px; text-align:center;" | 24
| style="text-align:center; font-size:10px; text-align:center;" | -----
| style="text-align:center; font-size:10px; text-align:left;  " | 
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
| style="font-size:10px; text-align:center;  " | 1
| style="font-size:10px; text-align:center;  " | 396
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 
|-
| style="font-size:10px; text-align:center;  " | 2
| style="font-size:10px; text-align:center;  " | 397
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 
|-
| style="font-size:10px; text-align:center;  " | 3
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 4
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 
|-
| style="font-size:10px; text-align:center;  " | 5
| style="font-size:10px; text-align:center;  " | 398
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 6
| style="font-size:10px; text-align:center;  " | 399
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 7
| style="font-size:10px; text-align:center;  " | 98
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 8
| style="font-size:10px; text-align:center;  " | 64
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:left;    " | 
|-  
| style="font-size:10px; text-align:center;  " | 9
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 10
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 11
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 12
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 13
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 14
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 15
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 16
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 17
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|-
| style="font-size:10px; text-align:center;  " | 18
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
| style="font-size:10px; text-align:center;  " | 
|}
