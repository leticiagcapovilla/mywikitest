---
title: Sirius control system network
description: 
published: 1
date: 2024-06-03T19:14:09.349Z
tags: 
editor: markdown
dateCreated: 2024-06-03T18:41:20.024Z
---

# CON: Sirius control system network

<br>

## Introduction

This page describes the computer network that will support [Sirius control system](/Machine/control_system). Our goal is to provide a reliable, flexible and dedicated network for controlling the machine.

<br>

## Network topology

The figure below shows Sirius control system network topology. It's composed of two layers: the upper one, called ''core'', contains two modular switches with at least 48 10GBASE-SR ports, redundant power supplies, fans and management modules, and the lower one, being constitued of 33 access PoE+ switches with 4 10GBASE-SR ports. For redundancy reasons, a ring is formed between all the border switches, so that any eventual problem in a cable connecting an access equipment to a core switch does not interrupt the operation of the entire sector supplied by this respective cable.


[[File:topologia-v5-eng.png|600px|thumb|center|Control system network topology]]

|![](/img/groups/con/sirius_cs_network/Topologia-v5-eng.png =600x)|
|-|
|**Figure 1**: Schematic view of the module combination topology for the 60 kW high power solid state amplifier.|

<br>

## Network equipments

During 2017, [Controls Group](/Machine/Groups/CON) evaluated some potential suppliers of network equipments for the control system. Aspects such as price, technical specifications, documentation, pre-sales support and service offerings were taken into account, considering the requirements and the budget available. We have also performed some proof of concept tests with switches and wireless access points provided by the manufacturers. At the end of this task, which took a few months to complete, [Aruba Networks](http://www.arubanetworks.com/){target=_blank}, now part of Hewlett Packard Enterprise (HPE), was chosen as the supplier.

<br>

### Switches

[Aruba 2930M](http://www.arubanetworks.com/products/networking/switches/2930m-series/){target=_blank} is the network switch for the access layer. It can be mounted with different options of power supplies and uplink modules. The following table summarizes parts ordered for the access switches.

**Table 1**: 

|Component| HPE description| HPE part number| Quantity ordered |
|-|-|-|-|
|Switch| Aruba 2930M 24G PoE+ 1-slot switch| JL320A| 64 |
|Mounting kit| HPE X410 1U Universal 4-post Rackmount kit| J9583A| 5 |
|Power supply| Aruba X372 54VDC 680W 100-240VAC Power Supply| JL086A| 98 |
|Uplink module| Aruba 3810M/2930M 4-port 100M/1G/10G SFP+ MACsec Module| JL083A| 64  |


As shown in the [Aruba 2930M data sheet](http://www.arubanetworks.com/assets/ds/DS_2930MSwitchSeries.pdf){target=_blank}, the JL320A switch has 24 10/100/1000 Mbps PoE+ RJ-45 ports, with one optional stacking module and one optional uplink module. All Aruba 2930M switches ordered for the control system don't have the stacking module, as we considered that it wouldn't be useful. Regarding the uplink module, all of them have the JL083A option, which comes with four SFP+ ports that will always operate at 10 Gbps when used. Concerning the power supplies, the JL320A switch can accomodate up two power supplies. We ordered only the JL086A power supply. Each Aruba 2930M switch of the control system will have two power supplies of this model. With these two power supplies, the PoE budget is 740 W and we have power redundancy. We will consider mounting access switches with the J9583A rackmount kit. In order to evaluate this option, 5 kits were bought.

For the core layer, switch model chosen is [Aruba 5412R zl2](http://www.arubanetworks.com/products/networking/switches/5400r-series/){target=_blank}. The table below summarizes parts ordered for the core layer:

**Table 2**:

|Component| HPE description| HPE part number| Quantity ordered |
|-|-|-|-|
|Chassis| Aruba 5412R zl2 switch| J9822A| 2 |
|Mounting kit| HPE X450 4U/7U Universal 4-post Rackmount Kit| J9852A| 2 |
|Power supply| Aruba 5400R 700W PoE+ zl2 power supply| J9828A| 8 |
|Management module| Aruba 5400R zl2 management module| J9827A| 2 |
|Line card| Aruba 8-port 1G/10GbE SFP+ MACsec v3 zl2 Module| J9993A| 12  |


Each core switch consists of a chassis (J9822A) with a mounting kit (J9852A), four power supplies (J9828A), two management modules (J9827A), one fan tray (J9832A) and six line cards (J9993A) with 8 SFP+ ports each, which results in a total of 48 SFP+ ports per switch. The J9822A comes with one fan tray (J9832A) and one management module (J9827A). We bought an additional management module for each 5412R zl2 switch for management redundancy. More information about Aruba 5412R zl2 switch can be obtained from [its data sheet](http://www.arubanetworks.com/assets/ds/DS_5400Rzl2SwitchSeries.pdf){target=_blank}.

A total of 216 "HPE X132 10G SFP+ LC SR Transceiver" (J9150A part number) transceivers were bought for connecting access to core switches through optical fiber cables.

Control system switches and their accessories were ordered in late 2017 and will be delivered until the middle of February 2018.

<br>

## Network cables

Control system network will employ a huge number of long-run cables and patch cords. This section presents the technical specifications of these cables.

<br>

### Copper cables

Default configuration for control system copper network cables will be category 6, U/UTP, with a green or grey LSZH jacket. The table below shows the color convention for network cables that will be adopted in Sirius building.

**Table 3**:

| Color| Reserved for |
|-|-|
|Green| Control system network |
|Red| Control system network |
|Grey| Campus wired and wireless networks and printers |
|Blue| Analog telephones |
|Yellow| Security devices, such as cameras and card readers used for access control |


As this color convention scheme for network cables was defined lately, we still will evaluate its adequation, taking into account the existing stock of network cable reels (and their colors). So the table above may change in the future.

<br>

### Optical fiber cables

Optical fiber cables will be used for uplinks between access and core switches and also for connecting control system servers to the network infrastructure. All fiber cables of the control system network will be multi-mode (OM4), with a black LSZH jacket.

<br>

## Power over Ethernet (PoE)

As mentioned in the previous section, all copper ports of access layer switches will offer PoE+. Despite of this fact, it may not be possible to plug PoE+ devices in all ports of the switch at the same time. The summation of power delivered by each of the ports should not exceed the maximum PoE power available from switch power supplies.

In order to facilitate calculations of the PoE budget for switches, the table below lists PoE devices in the control system and their power consumption.

|	Device| Description| Power consumption |
|-|-|-|

<br>

## Linac control system network

Sirius Linac is a turnkey solution from the Shanghai Institute of Applied Physics (SINAP). It comes with all hardware and software systems necessary for Linac operation, which includes three switches (Dell N3048 model) and various network cables. Linac switches will be connected to Sirius control system network.

A spare Dell N3048 switch was purchased in 2017.

This section will be updated with more information about Linac computer network soon.

<br>

## Network services

We are planning to run the following network services.

<br>

### Domain Name System (DNS)

With a DNS server, we can easily associate IPs with node names (for example, ''node1'' or ''node2''). This service will run at [[CON:Sirius_control_system_servers|control system servers]](link).

<br>

### Dynamic Host Configuration Protocol (DHCP)

[Controls Group](/Machine/Groups/CON) will use DHCP for IP address assignment of embedded and desktop computers that are not a permanent installation in Sirius control system. With a DHCP server, it won't be necessary to configure static IPs in laptops used during maintenance shifts, for instance. Along with the DHCP service, other features of the control system, such as the forwarding of EPICS UDP broadcast packets through the network, will allow the user to connect a new computer to the control system network under a plug-and-play manner.

Other groups may decide freely whether to use static or dynamic IP addresses on the equipments under their responsibility.

As we require that the IP addresses be allocated according to the port that the device is connected to, we decided to centralize the [DHCP service](/Machine/Groups/CON/dhcp_servers) in our [[CON:Sirius_control_system_servers|servers]](link) and to use two DHCP features: **DHCP relay agent** to forward IP requests from the switches to the server and **option 82** to append the respective switch's port and IP address to a DHCPDISCOVER packet.

<br>

### Lightweight Directory Access Protocol (LDAP)

A LDAP server will provide authentication for enabling special privileges for all control system software. Actually we could use CNPEM LDAP servers (Microsoft Active Directory) for that, but we are not allowed to create user groups in them, and these groups are necessary to define roles associated with each control system user.

<br>

### Network Time Protocol (NTP)

NTP is necessary for time synchronization between clocks of all devices. This way, all computer clocks of the [control system](/Machine/control_system) will be practically set together, leading to coherent timestamps for EPICS process variables or error log messages. Moreover, this network service is very important once BeagleBone Black, the default single-board computer choice for [Sirius control system](/Machine/control_system), doesn't have a built-in real-time clock (RTC) with a backup battery. Please refer to [this page](/Machine/Groups/CON/ntp) for more information about this service.

<br>

## Switches configuration

This section is reserved for the configuration details of all kinds of switches present in our network.

<br>

### Reserved VLANs

The VLANs IDs used so far and therefore unavailable for further use:

**Table 4**:

|VLAN ID| Function |
|-|-|
|2| GlusterFS and Docker |
|4| Connectivity routing VLAN (only for approach 1) |
|5| LINAC routing VLAN (only for approach 1) |
|100| Front-end BPMs |
|110| Diagnostics cameras (sectors 1 and 20) |
|200| Interlock MPS |
|201| Interlock IHM |
|202| Interlock PPS  |

<br>

### Core switches

|![](/img/groups/con/sirius_cs_network/Cores.jpg =750x)|
|-|
|**Figure 2**: |

These two switches act as the main packet routers in our network and the interface with the corporative network. This latter can be achieved by at least two means that have not been decided yet: the first consists of adding the `TA-TiRack:CO-FWSrv-1` as a firewall between the two networks. In this case, all users who need to access a node have to `ssh` into this computer before. The second option is to connect the core switches directly to the corporative equipment.

<br>

#### Server connectivity

As documented in [[CON:Sirius_control_system_servers| this page]], each server has 8 10GbE SFP+ ports. Two of them are reserved for the GlusterFS and Docker Swarm communication and the other six for general data traffic. They are connected according the following table.

**Table 5**:

| System | Server <br> Interface Port | Core Switch <br> Interface Port| VLAN |
|-|-|-|-|
|GlusterFS <br> Docker Swarm |	Board #1 - Port 1 <br> Board #2 - Port 2| D8 <br> F8 | 2 |
|General data traffic| Board #1 - Port 2 <br>  Board #2 - Port 2 <br>  Board #1 - Port 3 <br>  Board #2 - Port 3 <br>  Board #1 - Port 4 <br>  Board #2 - Port 4 | C7 <br> C8 <br>  D7 <br> E7 <br> E8 <br> F7| Default  |

Aggregated interfaces were used in each server in order to provide redundancy and automatic fail recovery. A dedicated VLAN was created for the GlusterFS and Docker services with the purpose to increase security and decrease latency between them. This latter is the main source of performance loss in this type of services. To create it, connect to the switch through either a serial micro USB cable or a ssh encrypted connection and execute the following steps. Replace `x` with 1 or 2 according to the core switch you connected.

```
# configure terminal
(config)# vlan 2 name "GlusterFS - Swarm"
(config)# vlan 2 ip address 10.128.2.x 255.255.255.0
```

The aggregation is achieved by using the [803.3ad Link Aggregation Control Protocol](https://en.wikipedia.org/wiki/Link_aggregation){target=_blank} and can be set up in the switches according to the steps below.

```
# GlusterFS and Docker aggregated interface
(config)# trunk D8,F8 trk1 lacp

# General data traffic aggregated interface
(config)# trunk C7,C8,D7,E7,E8,F7 trk3 lacp
```

Additionally, the workstation which participates in the [[CON:Sirius_control_system_servers|Controls Group's cluster]](link) also needs to be connected to the switches. Each interface of its 2-10GbE SFP+ board connects to the D5 port from each core switch. Add both `trk1` and D5 to the VLAN 2 with

```
(config)# vlan 2 untagged trk1
(config)# vlan 2 untagged D5
```

<br>

#### Core switches connectivity

The two core switches are connected to each other by an aggregated interface which uses the ports C6, D6, E6 and F6. To set it up, follow the instructions below in both switches.

```
# inter-switch aggregated interface
(config)# trunk C6,D6,E6,F6 trk2 lacp
```

As `trk2` will receive packets from both VLANs 1 and 2, we need to tag the frames in order to the switch to know the VLAN they come from:

```
(config)# vlan 1 tagged trk2
(config)# vlan 2 tagged trk2
```

Finally, set up the IP address for the default VLAN, where `x` equal to 1 for `CA-RaCtrl:CO-NetCoSw-1` and 2 for `LA-RaCtrl:CO-NetCoSw-1`:

```
(config)# vlan 1 ip address 10.128.255.x/24
```

<br>

### Access switches

This section describes the general configuration of the access switches.

<br>

#### Out-of-band management interface

All OOBM interfaces of all switches have the same address, 10.128.255.1/30. To configure them use the commands below:

```
# configure terminal
(config)# oobm ip address 10.128.255.1/30
(config)# oobm enable
```

<br>

#### Interlock VLANs

Eight interfaces of each switch (from 16-24) are reserved for the interlock system. As requested by the Magnets Group, 3 VLANs are created according to the following table:

**Table 6**:

|VLAN| Ports| Function |
|-|-|-|
|100| 17-18| MPS |
|101| 19-20| IHM |
|102| 21 - 24| PPS  |

As a ring is formed between all access switches, the [spanning tree protocol](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol){target=_blank} is enabled on these VLANs:

```
(config)# spanning-tree mode rapid-pvst
(config)# spanning-tree vlan 100-102 enable
```

Finally, we need to enable the VLANs on the interfaces used for the ring topology, i.e., A3 and A4.

```
(config)# vlan 100-102 tagged A3-A4
```

<br>

#### Front-end BPM VLANs

All Controls Group's access switched are connected to a same-model Diagnostics Group's switch. This latter should be configured with two different VLANs, the default and the one dedicated for the front-end BPM devices whose ID is **100** according to [[CON:Sirius_control_system_network#Reserved_VLANs|this]](link).

<br>

##### Diagnostics Group's switches configuration

As agreed by the group's members, ports in the range from 11 to 24 should be used to connect front-end devices. Use the command below to set it up:

```
(config)# vlan 100 untagged 11-24
```

Packets flowing from the interface used to connect the switch to the Control group's must be tagged on both VLANs. Set it with

```
(config)# vlan 1 tagged 1
(config)# vlan 100 tagged 1
```

<br>

##### Control Group's switches configuration

Configure the front-end BPM devices VLAN and its IP address to allow the switch to route packets to and from this VLAN. Don't forget to tag the packets on the interface `<interface>` used to connect to the Diagnostics group's switch.

```
(config)# vlan 100 ip address 192.168.2.0/24
(config)# vlan 1, 100 tagged <interface>
```

<br>

### Routing

We proposed some alternatives for routing considering the proposed topology. The subsections below are dedicated to explain those alternatives:

[[File:ospf.png|600px|center|Control system network topology. Dynamic routing with OSPF.]]

|![](/img/groups/con/sirius_cs_network/Ospf.png =600x)|
|-|
|**Figure 3**: Control system network topology. Dynamic routing with OSPF.|

<br>

#### Alternative 1: OSPF and static routes

In this approach, it's proposed dynamic routing with three OSPF areas for the star topology (according to figure) and static routing for the ring topology. For the dynamic routing, the core switches act as area border routers (ABRs) and the access switches, as internal routers. The left half of the network belongs to 0.0.0.1 area and the right, to the 0.0.0.2 area. The latter two are connected to each other through the backbone area and are of type `totally stubby`, since this type prevents routing information coming from external areas from entering it, limiting OSPF traffic in the internal routers.

<br>

##### Subnetwork Division

The location of each switch determines the subnetwork it will serve. As in this [[CON:Sirius_control_system_racks|page]], there are rooms having more than a single switch. The table below lists each room's subnet(s):

**Table 7**:

|Room| Switch| Subnet| Switch Address| Room| Switch| Subnet| Switch Address |
|-|-|-|-|-|-|-|-|
|**1**| **IA01-RaCtrl:CO-NetSw-1 <br> IA01-RaCtrl:CO-NetSw-2**| **10.128.10.0/25 <br> 10.128.10.128/25** | **10.128.10.1/25 <br> 10.128.10.129/25** | 8 <br> 9| IA08-RaCtrl:CO-NetSw-1 <br> IA09-RaCtrl:CO-NetSw-1| 10.128.80.0/24 <br> 10.128.90.0/24 | 10.128.80.1/24 <br> 10.128.90.1/24 |
|2| IA02-RaCtrl:CO-NetSw-1| 10.128.20.0/24| 10.128.20.1/24| 10| IA10-RaCtrl:CO-NetSw-1| 10.128.100.0/24| 10.128.100.1/24 |
|**RF** | **RA-RaCtrl:CO-NetSw-1 <br> RA-RaCtrl:CO-NetSw-2 <br> RA-RaCtrl:CO-NetSw-3** | **10.128.25.0/26 <br> 10.128.25.64/26 <br> 10.128.25.128/26**| **10.128.25.1/26 <br> 10.128.25.65/26 <br> 10.128.25.129/26** | 11 <br> 12 <br> 13 | IA11-RaCtrl:CO-NetSw-1 <br> IA12-RaCtrl:CO-NetSw-1 <br> IA13-RaCtrl:CO-NetSw-1| 10.128.110.0/24 <br> 10.128.120.0/24 <br> 10.128.130.0/24 | 10.128.110.1/24 <br> 10.128.100.1/24 <br> 10.128.130.1/24|
|3| IA03-RaCtrl:CO-NetSw-1| 10.128.30.0/24| 10.128.30.1/24| 14| IA14-RaCtrl:CO-NetSw-1| 10.128.140.0/24| 10.128.140.1/24 |
|4| IA04-RaCtrl:CO-NetSw-1| 10.128.40.0/24| 10.128.40.1/24| 15| IA15-RaCtrl:CO-NetSw-1| 10.128.150.0/24| 10.128.150.1/24 |
|5| IA05-RaCtrl:CO-NetSw-1| 10.128.50.0/24| 10.128.50.1/24| 16| IA16-RaCtrl:CO-NetSw-1| 10.128.160.0/24| 10.128.160.1/24 |
|6| IA06-RaCtrl:CO-NetSw-1| 10.128.60.0/24| 10.128.60.1/24| 17| IA17-RaCtrl:CO-NetSw-1| 10.128.170.0/24| 10.128.170.1/24 |
|7| IA07-RaCtrl:CO-NetSw-1| 10.128.70.0/24| 10.128.70.1/24| 18| IA18-RaCtrl:CO-NetSw-1| 10.128.180.0/24| 10.128.180.1/24 |
|**Power supplies**| **PA-RaCtrl:CO-NetSw-1 <br> PA-RaCtrl:CO-NetSw-2 <br> PA-RaCtrl:CO-NetSw-3 <br> PA-RaCtrl:CO-NetSw-4 <br> PA-RaCtrl:CO-NetSw-5** | **10.128.75.0/27 <br> 10.128.75.32/27 <br> 10.128.75.64/27 <br> 10.128.75.128/27 <br> 10.128.75.160/27** |**10.128.75.1/27 <br> 10.128.75.33/27 <br> 10.128.75.65/27 <br> 10.128.75.129/27 <br> 10.128.75.161/27 **| 18 (II) <br> **19/20 <br> " <br> LINAC <br> "**| **IA19-RaCtrl:CO-NetSw-1 <br> IA20-RaCtrl:CO-NetSw-1 <br>  IA20-RaCtrl:CO-NetSw-2 <br> LA-RaCtrl-CO-NetSw-1 <br> LA-RaCtrl-CO-NetSw-2** | **10.128.190.0/24 <br> 10.128.200.0/25 <br> 10.128.200.128/25 <br> 10.128.1.0/25 <br> 10.128.1.128/25**| **10.128.190.1/24 <br> 10.128.200.1/25 <br> 10.128.200.129/25 <br> 10.128.1.1/25 <br> 10.128.1.129/25** |
|	|	|	|	| **Connectivity**|**CA-RaCtrl:CO-NetSw-1** | **10.128.0.0/24**| **10.128.0.1/24** |

<br>

##### Dynamic routing: star topology

To configure OSPF in the core switches, follow the steps below:

```
# Enable OSPF
(config)# router ospf enable

# Create backbone area (0.0.0.0)
(config)# router ospf area backbone

# Enable backbone area (0.0.0.0) in VLAN 0
(config)# vlan 0 ip ospf area backbone
```

On `CA-RaCtrl:CO-NetCoSw-1`, configure the `totally stubby` area `0.0.0.1` and enable it on a newly created VLAN 4:

```
# Create totally stubby area (0.0.0.1)
(config)# router ospf area 0.0.0.1 stub no-summary 10

# Create VLAN 4 and assign the 10.128.4.1/24 address
(config)# vlan 4 ip address 10.128.4.1 255.255.255.0

# Enable OSPF area 0.0.0.1 on VLAN 4
(config)# vlan 4 ip ospf area 0.0.0.1
```

Don't forget to append the ports that will be connected to the access switches to VLAN 4:

```
# Append <port> to VLAN 4
(config)# vlan 4 untagged <port>
```

On `LA-RaCtrl:CO-NetCoSw-1`, configure the totally stubby area 0.0.0.2 and enable it on a newly created VLAN 5: 

```
# Create totally stubby area (0.0.0.2)
(config)# router ospf area 0.0.0.2 stub no-summary 10

# Create VLAN 5 and assign the 10.128.5.1/24 address
(config)# vlan 5 ip address 10.128.5.1 255.255.255.0

# Enable OSPF area 0.0.0.2 on VLAN 5
(config)# vlan 5 ip ospf area 0.0.0.2
```

Similarly, we need to append the ports that will be connected to the access switches to VLAN 5:

```
# Append <port> to VLAN 5
(config)# vlan 5 untagged <port>
```

To enable OSPF in the access switches, we need to perform basically two tasks: enable the area and assign it to the VLANs. In the access switches connected to `CA-RaCtrl:CO-NetCoSw-1`:

```
# Enable OSPF
(config)# router ospf enable

# Create totally stubby area (0.0.0.1)
(config)# router ospf area 0.0.0.1 stub no-summary 10

# Create VLAN 4 and assign the 10.128.4.x/24 address
(config)# vlan 4 ip address 10.128.4.x 255.255.255.0

# Append interface A1 into VLAN 4
(config)# vlan 4 untagged A1

# Enable OSPF area 0.0.0.1 on VLAN 4
(config)# vlan 4 ip ospf area 0.0.0.1

# Enable OSPF area 0.0.0.1 on the default VLAN
(config)# vlan 1 ip ospf area 0.0.0.1

# Enable passive mode on VLAN 1. This limits the number of packets in this interface as it prevents the switch making neighbors on the interfaces belonging to this VLAN.
(config)# vlan 1 ip ospf passive

# Enable static routes to be transmitted to other switches
(config)# router ospf redistribute static
```

The last steps is to lessen the priority of the access switch in order that the core switches be always chosen as the DR (designated router). As those devices have more processing power and memory, we leave to them the task to synchronize the adjacent router in case of a topology change. Execute the following command to lessen the access switch's priority:

```
(config)# vlan 4 ip ospf priority 2
```

Repeat the steps for the access switches connected to `LA-RaCtrl:CO-NetCoSw-1`:

```
# Enable OSPF
(config)# router ospf enable

# Create totally stubby area (0.0.0.2)
(config)# router ospf area 0.0.0.2 stub no-summary 10

# Create VLAN 5 and assign the 10.128.5.x/24 address
(config)# vlan 5 ip address 10.128.5.x 255.255.255.0

# Append interface A1 into VLAN 5
(config)# vlan 5 untagged A1

# Enable OSPF area 0.0.0.1 on VLAN 5
(config)# vlan 5 ip ospf area 0.0.0.2

# Enable OSPF area 0.0.0.2 on the default VLAN
(config)# vlan 1 ip ospf area 0.0.0.2

# Enable passive mode on VLAN 1. This limits the number of packets in this interface as it prevents the switch making neighbors on the interfaces belonging to this VLAN.
(config)# vlan 1 ip ospf passive

# Enable static routes to be transmitted to other switches
(config)# router ospf redistribute static
```

Finally, lessen access switch's DR priority with:

```
(config)# vlan 5 ip ospf priority 2
```

During tests, two BeagleBones Black were connected to the system, one to each access switch (figure), to simulate two host in different supersector communicating with each other. The latency obtained from the `ping` command was 0.212ms in average for 500 packets sent:

```
# Command executed in 10.128.1.10
$ ping -c 200 -i 0.1 10.128.0.10
--- 10.128.0.10 ping statistics ---
500 packets transmitted, 500 received, 0% packet loss, time 54784ms
rtt min/avg/max/mdev = 0.149/0.212/0.448/0.069 ms
```

The second test was based on `iperf` with UDP mode:

```
# On host 10.128.1.10
$ iperf -s -u
Server listening on UDP port 5001
Receiving 1470 byte datagrams
UDP buffer size:  160 KByte (default)
------------------------------------------------------------
[  3] local 10.128.1.10 port 5001 connected with 10.128.0.10 port 49219
[ ID] Interval       Transfer     Bandwidth        Jitter   Lost/Total Datagrams
[  3]  0.0-10.0 sec   114 MBytes  95.7 Mbits/sec   0.373 ms    0/81438 (0%)

# On host 10.128.0.10
$ iperf -c 10.128.1.10 -u -b 100m
[  3] local 10.128.0.10 port 49219 connected with 10.128.1.10 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec   114 MBytes  95.7 Mbits/sec
[  3] Sent 81438 datagrams
[  3] Server Report:
[  3]  0.0-10.0 sec   114 MBytes  95.7 Mbits/sec   0.372 ms    0/81438 (0%)
```

<br>

##### Static routing: ring topology

|![](/img/groups/con/sirius_cs_network/Ring.png =400x)|
|-|
|**Figure 4**: Control system network's ring topology. Static routing.|

As a redundancy option, a ring topology is created connecting all access switches. Two new static  default routes are added: one for the switch to the left and another, to the right. To avoid that two neighbor switches exchange packets indefinitely as in a ping-pong game, we need to define a prioritary sense. By default, the clockwise routes will cost less than the anticlockwise's. The bad consequence of this approach is that a switch will need to know the addresses of its neighbours and in the case of an eventual repair (addition or remotion), at least two switches will need to be reconfigured. Futhermore, at least three new VLANs will be needed (2 would be enough with the number of switches were even), according to the figure.

Given any three consecutive access switches `A`, `B` and `C` (whose addresses are `10.128.**A**.1`, `10.128.**B**.1` and `10.128.**C**.1` respectively), the VLAN used to connect `A` to `B` must be different from the one used to connect `B` to `C`.

To configure `B` accordingly, you need to access `A` and `C` and verify if any of the VLANs 6, 7 and 8 exist. In `A` (switch from the left), search for a VLAN with the address `10.128.X.**2**` and in `C` (switch from the right), for the address `10.128.Y.**1**`. In `B`, therefore, use VLANs `X` and `Y`:

```
# In switch B:
(config)# vlan X ip address 10.128.X.1 255.255.255.252
(config)# vlan Y ip address 10.128.Y.2 255.255.255.252
```

Add A3 and A4 interfaces into the VLANs above. The frames must be `tagged`, since those ports are going to be used to the Interlock VLANs too. By convention, A3 will be used to connect to the switch `A` and A4 to `C`.

```
# In switch B:
(config)# vlan X tagged A3
(config)# vlan Y tagged A4
```

Define two new static routes:

```
# In switch B:
# More prioritary route to the left:
(config)# ip route 10.128.A.0/24 10.128.X.2 distance 200

# Less prioritary route to the right:
(config)# ip route 10.128.C.0/24 10.128.Y.1 distance 300
```

Make them available to the OSPF routing with:

```
# In switch B:
(config)# router ospf redistribute static
```

<br>

##### DHCP relay agent

In order to forward the DHCPDISCOVER packets from each subnet to the DHCP servers, the relay agent should be enabled in each access switch in the default VLAN. Beside that feature, we need to append the option 82 to these packets in order to let the server know the port that the requester device is connected to. To enable both features, execute:

```
# Enable relay agent and option 82
(config)# dhcp-relay option 82 replace ip

# Forward broadcast request packets to the DHCP server accordingly
(config)# vlan 1 ip helper-address 10.128.255.3
```

<br>

#### Alternative 2: single and big network

In this approach, there's no routing setup at all. All hosts are connected to a single and big network whose address is 10.128.0.0/16. Despite the author's repetitive warnings about layer 2 (ARP) and 3 broadcasts (EPICS) that might congest the network, it was decided that this alternative is the one chosen for the Sirius control network. The author washes his hands.

The only thing we need to do is to enable the spanning tree protocol on the default VLAN in all switches (core and access):

```
(config)# spanning-tree mode rapid-pvst
(config)# spanning-tree vlan 1 enable
```
