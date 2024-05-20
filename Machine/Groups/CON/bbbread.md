---
title: bbbread
description: 
published: 1
date: 2024-05-20T21:29:58.705Z
tags: 
editor: markdown
dateCreated: 2024-05-20T20:55:13.988Z
---

# CON: BBBread

<br>

## Introduction

BBBread, BeagleBone Black - Redis Activity Display, is a python software project that stores information about Control System's nodes in a [Redis database](https://redis.io/){target=_blank} on the server. It also provides functions to stop/restart services on a BBB, reboot nodes and configure it's:

* IP
* Hostname
* DNS

<br>

### Requirements

The main requirements for BBBread installation in a BBB are:

* A Redis database open to local connections to port 6379
* pyredis
* [bbb-function](https://github.com/lnls-sirius/bbb-function){target=_blank}

<br>

### Installation

* Clone [this repository](https://github.com/lnls-sirius/bbbread){target=_blank} in BBB's root repository

```
# cd /root
# git clone https://github.com/lnls-sirius/bbbread
```

* Use make to automatically install and start BBBread

```
# cd bbbread/
# make install
```

Alternatively, manually install following these steps:

* Install pyredis

```
# pip3 install redis
```

* Configure and start systemd service

```
# cd bbbread
# cp bbbread.service /etc/systemd/system
# systemctl daemon-reload
# systemctl start bbbread
# systemctl enable bbbread
```

<br>

## Server Database

All information related to BeagleBones is stored in [hashes](https://pt.wikipedia.org/wiki/Tabela_de_dispers%C3%A3o){target=_blank} into the server's database. Each hash contains one BBB's information, the hashes' names are formatted as "BBB:IP:Hostname".

The information stored in the hashes are:

- ip_address: the node's IPv4 address
- name: the node's hostname
- ip_type: the node's IP type (static or DHCP)
- state_string: the node's state (Connected, Disconnected or Moved)
- config_time: the node's bbb-function configuration time
- ping_time: the epoch time of the last time the node updated the hash's information
- details: details about the equipment the connected to the BBB
- sector: the node's network location
    - "Sala01": first rack room
    - "Sala02": second rack room
    - "Sala03": third rack room and so on
    - "LT": Transport Line
    - "Conectividade": Connectivity room
    - "Fontes": Power supply room
    - "RF": RF room
    - "Outros": Other locations, such as corporate network and pulsed magnets subnet.

<br>

### Node State

In the database BeagleBones can be classified in three different states:

* Connected
* Disconnected
* Moved

The third state is used when a BeagleBone changes it's hostname or IP address.

Since the name of the hash that stores the BBB information depends on the node's hostname and IP, if one of these changes the hash should change too. If any service changes the BBB's information or hostname, the [CON:BBBread#Pinging|Pinging Thread](link) identifies the changes and set's the "state_string" key on the original hash with the new hash's name, so the operator can identify where the information about the BBB will be stored next.

<br>

### Command List

Each BBB looks for it's specific command list in the Redis server, the list name is "BBB:IP:Hostname:Command". If the list exists, the BBB pops it's first value, decodes the bytes into a string and splits it into a list using a semicolon (; ) as separator. The first item of this list is the command and the remaining items are the command's parameters.

- **Reboot**

The reboot command is simply the number 1, taking no parameters.

- **Set IP**

The number used to represent SET_IP command is 17. It also needs the following parameters, respectively: 

  - IP type: manual or dhcp
  - New IP (needed only for manual IP)
  - subnet mask (needed only for manual IP)
  - gateway (needed only for manual IP)

After all, what needs to be sent to the list is: b"17;ip_type;new_ip;netmask;gateway"

- **Set Hostname**

The number used to represent SET_HOSTNAME command is 18, it only needs the new hostname as parameter, so what is pushed to the list is: b"18;Hostname"

- **Set Nameservers**

The number used to represent SET_NAMESERVERS command is 19, it takes as parameters the primary and backup nameservers IP, in this order. The entire command pushed to the list is: b"19;Nameserver1;Nameserver2"

- **Restart Service**

The number used to represent RESTART_SERVICE command is 20, it's only parameter is the service name that you want to restart. The command that should be pushed to the list is: b"20;Service"

- **Stop Service**

The number used to represent STOP_SERVICE command is 21, it's only parameter is the service name that you want to stop. The command that should be pushed to the list is: b"21;Service"

<br>

### Server Thread

The program running on the server looks for hashes that start with "BBB:", listing those hashes and verifying if the key ping_time was updated in the last 11 seconds, if it wasn't the server considers the node as disconnected and writes this to the "state_string" key.

On the other hand, if "state_string" value is moved (starting with "BBB:") the thread does not operate any changes.

<br>

## Redis Client

The Redis Client, updates it's corresponding hash in the server every 10 seconds and searches the server's database for commands every 2 seconds. These two operations run in two separate threads.

The pinging thread uses the bbb.py module (used mostly on bbb-function service) to extract the nodes information, it then uses this information to update the BBB's database and the server's database.

<br>

## BBBread Module

Quick description of the classes and methods present on BBBread python module

<br>

### Command Class

A simple class used to standardize the commands and associate them to a specific integer.

<br>

### Redis Server Class

When initializing this class define the "log_path" parameter as where the commands sent and errors will be registered.

<br>

#### Listing and reading nodes

The **list_connected** method is used to return a list of all BBB hashes present on the database. If 'ip' or 'hostname' parameters are provided, it looks for BBB with the provided information.

With the hashname in hands, the **get_node** method can be used to read information from the hash.

<br>

#### Sending commands

The methods that can be used to send commands are:

* **reboot_node**(ip, hostname="", override=False)
* **change_ip**(current_ip, ip_type, hostname="", new_ip="", new_mask="", new_gateway="", override=False)
* **change_hostname**(ip, new_hostname, current_hostname="", override=False)
* **change_nameservers**(ip, nameserver_1, nameserver_2, hostname="", override=False)
* **restart_service**(ip, service, hostname="", override=False)

In all methods, if hostname is not provided, the server looks for hashes with the specified IP, if it finds one or more hashes with the same IP then server fails to send the command.

The override parameter determines if the server will search the database for the hash with the specified ip and hostname before sending the command, if it's True the server will send the command even if it doesn't find any hash or finds more than one hash. This parameter should be True when sending multiple commands that change the node's hashname in a short period of time (<10s).

The most appropriate order to send multiple commands is:

* DNS change
* Hostname change
* IP change
* Reboot

Commands can also be sent manually using **send_command(ip, command, hostname="", override=False)**, where the "command" parameter is the [CON:BBBread#Command_List|previously seen byte structure](link). **Sending commands manually is NOT recommended.**

<br>

#### Database management

Providing a hashname to **bbb_state** method returns a integer representing the state of the beaglebone: 0 (Connected), 1 (Disconnected) or 2 (Moved). This method also updates the value for 'state_string' if the hash wasn't updated for the last 15 seconds. This method is mainly used in the [CON:BBBread#Server_Thread|Server Thread](link).

A hash can be deleted from the database using **delete_node** method.

<br>

### Redis Client Class

The Redis Client class updates the BBB local database and the remote server database and waits commands from the server.

<br>

#### Pinging

Pinging is the act of updating the server database with the BBB information, a thread (ping_remote) does this every 10 seconds right after updating the local database with **force_update** method.

<br>

#### Listening

The **listen** method looks for the BBB's command list on the server database every 2 seconds. If the list exists, the first value is popped and the command is processed.

<br>

## Graphical User Interface

This project also includes a Graphical User Interface, which provides a quick and practical way to search for BBB is the network, show their information and change it's configuration.

<br>

### Basic Filter


|![](/img/groups/con/bbbread/Main_screen.png)|
|-|
|**Figure 1**: Basic Filter Visualization.|


Filters only by the node state, disconnected nodes will be shown in the color red and moved nodes will be shown in the color yellow. There is a filter present on all tabs to filter by sector/room or by name.

<br>

### Advanced Filter

![](/img/groups/con/bbbread/Advanced_filter.png)|
|-|
|**Figure 2**: Advanced Filter Visualization.|


Provides more options to find a BBB, including State, IP Type and Equipment.

<br>

### Service Tab

|![](/img/groups/con/bbbread/Service_tab.png)|
|-|
|**Figure 3**: Service Tab.|

This tab provides a way to stop or restart the following services: bbb-function, BBBread and PRUSerial485

<br>

### Information Screen

|![](/img/groups/con/bbbread/Info_screen.png)|
|-|
|**Figure 4**: BBB Info Screen.|

By clicking the info button after selecting any BBB this screen will provide the node's information.

<br>

### Configuration Screen

[[File:Config_screen.png|Configuration Screen|center]]

|![](/img/groups/con/bbbread/Config_screen.png)|
|-|
|**Figure 5**: Configuration Screen.|

By clicking the "Configure Node" button this screen provides a way to configure the node's IP, Hostname and or DNS.
