---
title: Sirius control system racks
description: 
published: 1
date: 2024-06-04T15:34:56.711Z
tags: 
editor: markdown
dateCreated: 2024-06-03T21:08:07.259Z
---

# CON: Sirius control system racks

<br>

## Introduction

The Controls group will count on 24 racks to install its components, including [servers](/Machine/Groups/CON/sirius_cs_servers), [switches](/Machine/Groups/CON/sirius_cs_network) and control hosts. The [TS IT](https://www.rittal.com/de_de/ts-it/public/index.php/en) developed by the German company [Rittal](https://www.rittal.com/com-en/content/en/start/) was chosen as the model and two different depths were acquired, according to the individual needs of each room.

<br>

## Amount and functions

The table below summarizes the location, count and physical dimension of our racks.

| Amount| Physical Dimensions (mm) | Location |
|-|-|-|
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

Two [2930M](http://www.arubanetworks.com/assets/ds/DS_2930MSwitchSeries.pdf|Aruba) switches and other two [1810-24G](https://h20195.www2.hpe.com/v2/GetDocument.aspx?docname=4AA4-6971ENW&doctype=data%20sheet&doclang=EN_US&searchquery=&cc=th&lc=en|HP) are needed for rooms **01** and **19/20**, due to the bigger amount of connections on these sectors. As in the previous section, these are 600x800mm racks.

<br>

### RF room

The Controls group has a rack in the RF room as well. In this case, we use three Aruba 2930M switches dedicated for the RF systems. No HP 1810 switches are used here.

<br>

### High power supplies room

The connection density in the power supply room is high: five Aruba 2930M switches are used in total. As all other racks in this room are wider, we chose to use a 600x1000 rack too.


**Ethernet Patch Panel**

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


**Ethernet Patch Panel - Top**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
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


**Ethernet Patch Panel - Bottom**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
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


**SERIALxxCON - Serial Networks**

|Boards| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 	|10.128.122.101| Temperature Monitor - MBTemp - LTB & UPS Monitoring|
|2| 	| 10.128.122.160| Temperature and Humidity Monitor - Linac |
|3| 	|	 | |
|4| 	|	 | |
|5| 	|	 | |

<br>

### Room 01

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|
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
|12| -----| DIG Galil - LTB 5 ||24| -----| General Purpose BC  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 95| 10.128.101.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|2| 96| 10.128.101.105| Power Supplies - FBP - Booster |
|3| 93| 10.128.101.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|4| 94| 10.128.101.102| Vacuum System - Ion Pump 4UHV - Booster |
|5| 		 |	|	| 
|6| 111| 10.128.101.106| Temperature Monitor - MBTemp - Booster |
|7| 		 |	|	|
|8| 115| 10.128.101.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 293| 10.128.101.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 319| 10.128.101.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.101.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.101.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.101.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.101.132| Power Supplies - FBP 4 - Storage Ring - Right 2 |

> Note: IPs 107 and 108 are reserved for EPP. 
{.is-info}

<br>

### Room 02

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.102.151| [POE] CountingPRU - Trecho 2 M2 |
|9| -----|  ||21| 10.128.102.152| [POE] CountingPRU - Trecho 2 C2 |
|10| -----|  ||22| 10.128.102.153| [POE] CountingPRU - Trecho 2 C3 |
|11| -----|  ||23| 10.128.102.154| [POE] CountingPRU - Trecho 2 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 57| 10.128.102.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 58| 10.128.102.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 		 |	|	|
|5| 61| 10.128.102.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 62| 10.128.102.105| Power Supplies - FBP - Booster |
|7| 	| 10.128.102.119| Temperature Monitor - MBTemp - RF Petra-7 Cavity |
|8| 51| 10.128.102.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 537| 10.128.102.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 298| 10.128.102.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.102.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.102.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.102.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.102.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 03

**Ethernet Patch Panel**

| Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.103.151| [POE] CountingPRU - Trecho 3 M2 |
|9| -----|  ||21| 10.128.103.152| [POE] CountingPRU - Trecho 3 C2 |
|10| -----|  ||22| 10.128.103.153| [POE] CountingPRU - Trecho 3 C3 |
|11| -----|  ||23| 10.128.103.154| [POE] CountingPRU - Trecho 3 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 204| 10.128.103.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 207| 10.128.103.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 205| 10.128.103.106| Temperature Monitor - MBTemp - Booster |
|5| 		 |	|	|
|6| 	| 10.128.103.104| Power Supplies - DCLINK - Storage Ring | |
|7| 		 |	|	|
|8| 206| 10.128.103.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 295| 10.128.103.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 289| 10.128.103.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.103.131| Power Supplies - FBP 3 - Storage Ring - Left 1 | |
|14| 	| 10.128.103.132| Power Supplies - FBP 4 - Storage Ring - Left 2 | |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.103.121| Power Supplies - FBP 1 - Storage Ring - Right 1 |
|18| 	| 10.128.103.122| Power Supplies - FBP 2 - Storage Ring - Right 2 |

<br>

### Room 04

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.104.151| [POE] CountingPRU - Trecho 4 M2 |
|9| -----|  ||21| 10.128.104.152| [POE] CountingPRU - Trecho 4 C2 |
|10| -----|  ||22| 10.128.104.153| [POE] CountingPRU - Trecho 4 C3 |
|11| -----|  ||23| 10.128.104.154| [POE] CountingPRU - Trecho 4 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 283| 10.128.104.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 284| 10.128.104.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |	|	|
|4| 		 |	|	|
|5| 281| 10.128.104.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 282| 10.128.104.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 		 |	|	|
|9| 294| 10.128.104.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 301| 10.128.104.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.104.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.104.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.104.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.104.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 05

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.105.151| [POE] CountingPRU - Trecho 5 M2 |
|9| -----|  ||21| 10.128.105.152| [POE] CountingPRU - Trecho 5 C2 |
|10| -----|  ||22| 10.128.105.153| [POE] CountingPRU - Trecho 5 C3 |
|11| -----|  ||23| 10.128.105.154| [POE] CountingPRU - Trecho 5 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 209| 10.128.105.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 208| 10.128.105.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 211| 10.128.105.106| Temperature Monitor - MBTemp - Booster |
|5| 202| 10.128.105.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 203| 10.128.105.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 212| 10.128.105.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 288| 10.128.105.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 323| 10.128.105.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.105.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.105.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.105.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.105.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 06


**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.106.151| [POE] CountingPRU - Trecho 6 M2 |
|9| -----|  ||21| 10.128.106.152| [POE] CountingPRU - Trecho 6 C2 |
|10| -----|  ||22| 10.128.106.153| [POE] CountingPRU - Trecho 6 C3 |
|11| -----|  ||23| 10.128.106.154| [POE] CountingPRU - Trecho 6 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 200| 10.128.106.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 199| 10.128.106.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 213| 10.128.106.103| Power Supplies - 4UHV - Storage Ring |
|4| 		 |	|	|
|5| 		 |	|	|
|6| 	| 10.128.106.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |	|	|
|8| 		 |	|	|
|9| 314| 10.128.106.117| Temperature Monitor - MBTemp - Storage Ring (<- BC) |
|10| 317| 10.128.106.118| Temperature Monitor - MBTemp - Storage Ring (BC ->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.106.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.106.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.106.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.106.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 07

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.107.151| [POE] CountingPRU - Trecho 7 M2 |
|9| -----|  ||21| 10.128.107.152| [POE] CountingPRU - Trecho 7 C2 |
|10| -----|  ||22| 10.128.107.153| [POE] CountingPRU - Trecho 7 C3 |
|11| -----|  ||23| 10.128.107.154| [POE] CountingPRU - Trecho 7 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 260| 10.128.107.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 259| 10.128.107.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 257| 10.128.107.106| Temperature Monitor - MBTemp - Booster |
|5| 256| 10.128.107.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 255| 10.128.107.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 258| 10.128.107.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 135| 10.128.107.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 137| 10.128.107.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.107.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.107.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.107.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.107.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 08

**Ethernet Patch Panel**


|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.108.151| [POE] CountingPRU - Trecho 8 M2 |
|9| -----|  ||21| 10.128.108.152| [POE] CountingPRU - Trecho 8 C2 |
|10| -----|  ||22| 10.128.108.153| [POE] CountingPRU - Trecho 8 C3 |
|11| -----|  ||23| 10.128.108.154| [POE] CountingPRU - Trecho 8 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 248| 10.128.108.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 247| 10.128.108.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 		 |	|	|
|5| 280| 10.128.108.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 279| 10.128.108.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 63| 10.128.108.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 139| 10.128.108.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 138| 10.128.108.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.108.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.108.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.108.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.108.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 09

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.109.151| [POE] CountingPRU - Trecho 9 M2 |
|9| -----|  ||21| 10.128.109.152| [POE] CountingPRU - Trecho 9 C2 |
|10| -----|  ||22| 10.128.109.153| [POE] CountingPRU - Trecho 9 C3 |
|11| -----|  ||23| 10.128.109.154| [POE] CountingPRU - Trecho 9 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 244| 10.128.109.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 243| 10.128.109.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 245| 10.128.109.106| Temperature Monitor - MBTemp - Booster |
|5| 		 |	|	|
|6| 	| 10.128.109.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |	|	|
|8| 246| 10.128.109.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 133| 10.128.109.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 136| 10.128.109.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.109.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.109.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.109.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.109.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 10

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.110.151| [POE] CountingPRU - Trecho 10 M2 |
|9| -----|  ||21| 10.128.110.152| [POE] CountingPRU - Trecho 10 C2 |
|10| -----|  ||22| 10.128.110.153| [POE] CountingPRU - Trecho 10 C3 |
|11| -----|  ||23| 10.128.110.154| [POE] CountingPRU - Trecho 10 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU - Booster  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


| Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 274| 10.128.110.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 273| 10.128.110.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |	|	|
|4| 		 |	|	|
|5| 276| 10.128.110.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 275| 10.128.110.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 		 |	|	|
|9| 311| 10.128.110.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 325| 10.128.110.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	| 10.128.110.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	| 10.128.110.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	| 10.128.110.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	| 10.128.110.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 11

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 11 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.111.151| [POE] CountingPRU - Trecho 11 M2 |
|9| -----|  ||21| 10.128.111.152| [POE] CountingPRU - Trecho 11 C2 |
|10| -----|  ||22| 10.128.111.153| [POE] CountingPRU - Trecho 11 C3 |
|11| -----|  ||23| 10.128.111.154| [POE] CountingPRU - Trecho 11 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 11  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 237| 10.128.111.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 238| 10.128.111.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |	|	|
|4| 239| 10.128.111.106| Temperature Monitor - MBTemp - Booster |
|5| 240| 10.128.111.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 241| 10.128.111.105| Power Supplies - FBP - Booster |
|7| 		 |	|	|
|8| 242| 10.128.111.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 299| 10.128.111.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 269| 10.128.111.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	|10.128.111.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	|10.128.111.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	|10.128.111.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	|10.128.111.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 12

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 12 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.112.151| [POE] CountingPRU - Trecho 12 M2 |
|9| -----|  ||21| 10.128.112.152| [POE] CountingPRU - Trecho 12 C2 |
|10| -----|  ||22| 10.128.112.153| [POE] CountingPRU - Trecho 12 C3 |
|11| -----|  ||23| 10.128.112.154| [POE] CountingPRU - Trecho 12 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 12  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 278| 10.128.112.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 277| 10.128.112.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |	|	|
|4| 		 |	|	|
|5| 		 |	|	|
|6| 	|10.128.112.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |	|	|
|8| 		 |	|	|
|9| 300| 10.128.112.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 312| 10.128.112.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |	|	|
|12| 		 |	|	|
|13| 	|10.128.112.121| Power Supplies - FBP 1 - Storage Ring - Left 1 | |
|14| 	|10.128.112.122| Power Supplies - FBP 2 - Storage Ring - Left 2 | |
|15| 		 |	|	|
|16| 		 |	|	|
|17| 	|10.128.112.131| Power Supplies - FBP 3 - Storage Ring - Right 1 | |
|18| 	|10.128.112.132| Power Supplies - FBP 4 - Storage Ring - Right 2  | |

<br>

### Room 13

**Ethernet Patch Panel**


|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 13 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.113.151| [POE] CountingPRU - Trecho 13 M2 |
|9| -----|  ||21| 10.128.113.152| [POE] CountingPRU - Trecho 13 C2 |
|10| -----|  ||22| 10.128.113.153| [POE] CountingPRU - Trecho 13 C3 |
|11| -----|  ||23| 10.128.113.154| [POE] CountingPRU - Trecho 13 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 13  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 232| 10.128.113.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 231| 10.128.113.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |
|4| 234| 10.128.113.106| Temperature Monitor - MBTemp - Booster |
|5| 236| 10.128.113.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 235| 10.128.113.105| Power Supplies - FBP - Booster |
|7| 		 |
|8| 233| 10.128.113.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 306| 10.128.113.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 310| 10.128.113.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.113.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.113.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.113.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.113.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 14

**Ethernet Patch Panel**


|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 14 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.114.151| [POE] CountingPRU - Trecho 14 M2 |
|9| -----|  ||21| 10.128.114.152| [POE] CountingPRU - Trecho 14 C2 |
|10| -----|  ||22| 10.128.114.153| [POE] CountingPRU - Trecho 14 C3 |
|11| -----|  ||23| 10.128.114.154| [POE] CountingPRU - Trecho 14 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 14  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)

|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 228| 10.128.114.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 227| 10.128.114.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |
|4| 		 |
|5| 230| 10.128.114.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 229| 10.128.114.105| Power Supplies - FBP - Booster |
|7| 		 |
|8| 		 |
|9| 309| 10.128.114.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 321| 10.128.114.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.114.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.114.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.114.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.114.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 15

**Ethernet Patch Panel**


|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 15 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.115.151| [POE] CountingPRU - Trecho 15 M2 |
|9| -----|  ||21| 10.128.115.152| [POE] CountingPRU - Trecho 15 C2 |
|10| -----|  ||22| 10.128.115.153| [POE] CountingPRU - Trecho 15 C3 |
|11| -----|  ||23| 10.128.115.154| [POE] CountingPRU - Trecho 15 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 15  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)

|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 224| 10.128.115.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 225| 10.128.115.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |
|4| 219| 10.128.115.106| Temperature Monitor - MBTemp - Booster |
|5| 		 |
|6| 	10.128.115.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |
|8| 226| 10.128.115.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 327| 10.128.115.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 316| 10.128.115.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.115.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.115.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.115.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.115.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 16

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 16 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.116.151| [POE] CountingPRU - Trecho 16 M2 |
|9| -----|  ||21| 10.128.116.152| [POE] CountingPRU - Trecho 16 C2 |
|10| -----|  ||22| 10.128.116.153| [POE] CountingPRU - Trecho 16 C3 |
|11| -----|  ||23| 10.128.116.154| [POE] CountingPRU - Trecho 16 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 16  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 222| 10.128.116.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 223| 10.128.116.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |
|4| 		 |
|5| 221| 10.128.116.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 220| 10.128.116.105| Power Supplies - FBP - Booster |
|7| 		 |
|8| 		 |
|9| 303| 10.128.116.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 326| 10.128.116.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.116.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.116.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.116.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.116.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 17

**Ethernet Patch Panel**

| Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 17 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.117.151| [POE] CountingPRU - Trecho 17 M2 |
|9| -----|  ||21| 10.128.117.152| [POE] CountingPRU - Trecho 17 C2 |
|10| -----|  ||22| 10.128.117.153| [POE] CountingPRU - Trecho 17 C3 |
|11| -----|  ||23| 10.128.117.154| [POE] CountingPRU - Trecho 17 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 17  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 249| 10.128.117.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 250| 10.128.117.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |
|4| 251| 10.128.117.106| Temperature Monitor - MBTemp - Booster |
|5| 252| 10.128.117.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 253| 10.128.117.105| Power Supplies - FBP - Booster |
|7| 		 |
|8| 254| 10.128.117.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 328| 10.128.117.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 261| 10.128.117.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.117.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.117.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.117.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.117.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 18-I

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 18 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.118.151| [POE] CountingPRU - Trecho 18 M2 |
|9| -----|  ||21| 10.128.118.152| [POE] CountingPRU - Trecho 18 C2 |
|10| -----|  ||22| 10.128.118.153| [POE] CountingPRU - Trecho 18 C3 |
|11| -----|  ||23| 10.128.118.154| [POE] CountingPRU - Trecho 18 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 18  |



**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 218| 10.128.118.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 217| 10.128.118.102| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|3| 		 |
|4| 		 |
|5| 		 |
|6| 	10.128.118.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |
|8| 		 |
|9| 262| 10.128.118.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 318| 10.128.118.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.118.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.118.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.118.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.118.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 18-II

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - Trecho 19 BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| 10.128.119.151| [POE] CountingPRU - Trecho 19 M2 |
|9| -----|  ||21| 10.128.119.152| [POE] CountingPRU - Trecho 19 C2 |
|10| -----|  ||22| 10.128.119.153| [POE] CountingPRU - Trecho 19 C3 |
|11| -----|  ||23| 10.128.119.154| [POE] CountingPRU - Trecho 19 M1 |
|12| -----|  ||24| -----| [POE] CountingPRU Booster - Trecho 19  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 214| 10.128.119.101| Vacuum System - Gauge Controller MKS - Booster & Storage Ring |
|2| 216| 10.128.119.102| Vacuum System - Ion Pump 4UHV - Booster |
|3| 		 |
|4| 116| 10.128.119.106| Temperature Monitor - MBTemp - Booster |
|5| 		 |
|6| 	10.128.119.104| Power Supplies - DCLINK - Storage Ring |
|7| 		 |
|8| 215| 10.128.119.103| Vacuum System - Ion Pump 4UHV - Storage Ring |
|9| 304| 10.128.119.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 315| 10.128.119.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.119.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.119.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.119.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.119.132| Power Supplies - FBP 4 - Storage Ring - Right 2  |

<br>

### Room 19/20

**Upper Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| [POE] CountingPRU - Booster ||13| -----| DIG BTS - Galil 4 |
|2| -----| [POE] Basler Camera DIG (Visible Light) - Booster ||14| -----| DIG BTS - Galil 5 |
|3| -----| DIG 4 (Rack DIG) ||15| -----| DIG BTS - Galil 6 |
|4| -----| [POE] DIG BTS - Booster - Monitor 1 ||16| -----|  |
|5| -----| [POE] DIG BTS - Booster - Monitor 2 ||17| -----|  |
|6| -----| [POE] DIG BTS - Trecho 20/M1 - Monitor 1 ||18| -----|  |
|7| -----| [POE] DIG BTS - Trecho 20/M1 - Monitor 2 ||19| -----|  |
|8| -----| [POE] DIG BTS - Trecho 20/M1 - Monitor 3 ||20| -----|  |
|9| -----| [POE] DIG BTS - Trecho 20/M1 - Monitor 4 ||21| -----|  |
|10| -----| DIG BTS - Galil 1 ||22| -----|  |
|11| -----| DIG BTS - Galil 2 ||23| -----| DIG - Scrapper 01 |
|12| -----| DIG BTS - Galil 3 ||24| -----| DIG - Scrapper 02  |


**Lower Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| General Purpose - BC ||13| -----|  |
|2| -----|  ||14| -----|  |
|3| -----|  ||15| -----|  |
|4| -----|  ||16| -----|  |
|5| -----|  ||17| -----|  |
|6| -----|  ||18| -----|  |
|7| -----|  ||19| -----|  |
|8| -----|  ||20| -----|  |
|9| -----|  ||21| 10.128.120.151| [POE] CountingPRU - Trecho 20 M2 |
|10| -----|  ||22| 10.128.120.152| [POE] CountingPRU - Trecho 20 C2 |
|11| -----|  ||23| 10.128.120.153| [POE] CountingPRU - Trecho 20 C3 |
|12| -----|  ||24| 10.128.120.154| [POE] CountingPRU - Trecho 20 M1  |


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 103| 10.128.120.101| Vacuum System - Gauge Controller MKS - LTB & Booster & Storage Ring |
|2| 105| 10.128.120.102| Vacuum System - Ion Pump 4UHV - LTB & Booster |
|3| 	10.128.120.116| Vacuum System - Ion Pump 4UHV - BTS |
|4| 112| 10.128.120.103| Vacuum System - Ion Pump 4UHV - Booster & Storage Ring |
|5| 113| 10.128.120.104| Power Supplies - DCLINKs - Booster & Storage Ring |
|6| 114| 10.128.120.105| Power Supplies - FBP - Booster |
|7| 		 |
|8| 		 |
|9| 	10.128.120.117| Temperature Monitor - MBTemp - Storage Ring (<-BC) |
|10| 	10.128.120.118| Temperature Monitor - MBTemp - Storage Ring (BC->) |
|11| 		 |
|12| 		 |
|13| 	10.128.120.121| Power Supplies - FBP 1 - Storage Ring - Left 1 |
|14| 	10.128.120.122| Power Supplies - FBP 2 - Storage Ring - Left 2 |
|15| 		 |
|16| 		 |
|17| 	10.128.120.131| Power Supplies - FBP 3 - Storage Ring - Right 1 |
|18| 	10.128.120.132| Power Supplies - FBP 4 - Storage Ring - Right 2 |
| |

|Note: IPs 107 and 108 are reserved for EPP.  |

<br>

### Room 21 (Transport Lines)

**Ethernet Patch Panel**

|Slot #| IP| Description ||Slot #| IP| Description |
|-|-|-|-|-|-|-|
|1| -----| Cable 01 to Rack LA-RaPS02 (Room 21) ||13| -----|  |
|2| -----| Cable 02 to Rack LA-RaPS02 (Room 21) ||14| -----|  |
|3| -----| Cable 03 to Rack LA-RaPS02 (Room 21) ||15| -----|  |
|4| -----| Cable 04 to Rack LA-RaPS02 (Room 21) ||16| -----|  |
|5| -----| Cable 05 to Rack LA-RaPS02 (Room 21) ||17| -----|  |
|6| -----| Cable 06 to Rack LA-RaPS04 (Room 21) ||18| -----|  |
|7| -----| Cable 07 to Rack LA-RaPS04 (Room 21) ||19| -----|  |
|8| -----| Cable 08 to Rack LA-RaPS04 (Room 21) ||20| -----|  |
|9| -----|  ||21| -----|  |
|10| -----|  ||22| -----|  |
|11| -----|  ||23| -----|  |
|12| -----|  ||24| -----|  


**SERIALxxCON - Serial Networks**

![](/img/groups/con/sirius_cs_racks/Racks_SERIALxxCON.png =350x)


|Board Location| SERIALxxCON ID| IP| Device |
|-|-|-|-|
|1| 396| 	 |
|2| 397| 	 |
|3| 		 |
|4| 		 |
|5| 398| 	 |
|6| 399| 	 |
|7| 98| 	 |
|8| 64| 	 |
|9| 		 |
|10| 		 |
|11| 		 |
|12| 		 |
|13| 		 |
|14| 		 |
|15| 		 |
|16| 		 |
|17| 		 |
|18| 		 |
