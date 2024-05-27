---
title: EPICS notification messaging - Telegram
description: 
published: 1
date: 2024-05-27T19:13:41.026Z
tags: 
editor: markdown
dateCreated: 2024-05-27T19:03:01.620Z
---

# CON: EPICS notification telegram

<br>

## Introduction

EpicsTel is an automated script that monitors the values of a given group of EPICS Process Variables (PVs) and notifies users in case said groups exceed it's limits, these notifications are done via [Telegram Messenger](https://telegram.org/){target=_blank} application by a [BOT](https://en.wikipedia.org/wiki/Internet_bot){target=_blank}.

<br>

## Usage

Setting up the application, gaining access to the BOT, BOT's structure, registering PV Groups, user Teams and subscribing to PV Notifications

<br>

### Setting Up

[Download Telegram Messenger in your smartphone](https://telegram.org/apps#mobile-apps){target=_blank} and register with your personal information: cellphone number, name and surname. Optional configurations include two step verification and adding a username.

By now the setup is complete, it's important to know that Telegram is a cloud based messaging application, so it can also be used via Web or through your computer application (without your phone necessarily having an internet connection at the time) but this is only possible after you properly configure the application thorough your smartphone.

<br>

### Gaining access

After properly installing and setting-up Telegram Messenger application on your smartphone, start a conversation with *@ControlsGroupInfoBot* sending any message to it (usually */start* command). You won't have access at the first contact, the BOT will return a warning message followed by your credentials which are your first name followed by your chat id.

|![](/img/groups/con/epics_messaging/Telegram_setup.jpeg)|
|-|
|**Figure 1**: Telegram first contact.|

After that, contact [Controls Group](/Machine/Groups/CON) informing your name, the laboratory's group you work on and attach the credentials ***as is*** (e.g. Peter:12345678, ControlsGroup:-87654321), the BOT will then inform you when you are added to the authorized personnel.

<br>

### BOT's structure

<br>

#### Teams

Teams are the groups of users allowed to use the BOT. There are 3 types of Teams: **Administrators, Team Administrators and Regular Teams**.


**Administrators** or ADM is the only Team with complete access to the BOT's functionalities, such as: 

* Adding/removing users to/from authorized personnel.

* Registering new PV Groups.

* Subscribing/Unsubscribing entire Teams to PV notifications.

**Team Administrators** or TeamADM is a  Team with partial access to the BOT's functionalities, such as:

* Knowing ids from users

* Subscribing/Unsubscribing the Teams they manage to PV notifications

* Removing users from the Teams they manage

**Regular Teams** are the most limited type of Teams, they are usually named after LNLS workgroups. It's users can subscribe to PV notifications and get instant values of PVs.

<br>

#### PV Groups

PV Groups are groups of EPICS Process Variables that will be monitored with their specific limits. One PV Group can have many PVs and different limits for each PV, but only one timeout, and one PV can belong to more than one group.

PV Groups are registered on demand by the BOT administrators, but you can request registration through the BOT.

<br>

### BOT Commands

The BOT functionalities are: getting instant values of a PV and constantly monitoring PV values. The BOT commands are:

* **/help**         

[[File:Epicstel_caget.jpeg|Caget Example|400px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_caget.jpeg)|
|-|
|**Figure 2**: Caget Example.|

Show BOT commands.

* **/caget** (PVs)

Sends instant values of the requested PVs.

Example: performing a /caget to PVs:

- **IA-17:CO-LM35:Temperature-Mon** 

- **IA-17:CO-Fan:Current-Mon**

* **/checkstatus** (PVs)

Gets archiver information for the requested PVs.

Example: ```/checkstatus SomePV:Voltage```

* **/isalive**

Sends the state of the monitoring function, if BOT sends False means that the BOT is not working properly (you can still acquire instant values of PVs but won't be notified of PVs exceeding their limits).

<br>

#### User

[[File:Epicstel_checkme.jpeg|checkme Example|400px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_checkme.jpeg)|
|-|
|**Figure 3**: checkme Example.|

* **/checkme**

Sends the user information:

- Name

- ChatID

- Teams

- PVGroups subscribed (if the user Team is subscribed to any PV Group the Team name will be in parentheses)


* **/forward** (Message)

Forwards the specified message to the BOT administrators.

Example: ```/forward Hello, how can I perform a ''caget''?```


[[File:Epicstel_checkgp.jpeg|checkgp Example|400px|thumb]]

<br>

#### PV Groups

* **/pvgroups**

Sends the list of PV Groups registered for notification.


* **/pvgroupsfile**

Sends a Comma Separated Values (CSV) file containing the PV Groups information (timeout, PVs and maximum and minimum values).


* **/checkgp** (PVGroups)

Sends the requested PVGroups information (PVs, maximum and minimum values).

Example: ```/checkgp Temperature-LINAC SI:01-Pressure```


* **/addpvgroup** (Group) (PVs) (Maximum Limit) (Minimum Limit) (Timeout)

Sends a request to the BOT administrators to register a new PV notification group. The maximum, minimum and timeout parameters will be the same for all PVs in the first moment, if you want to add PVs with different maximum and minimum limits adjust their limits later with **/addpv**.

The ''Timeout'' parameter is the time in minutes between two notifications of a PV that exceeded it's limits. PV Notifications are retriggerable, which means if a PV exceeds it's limits and then goes back to normal the Timeout timer will be reseted and if a second fault occurs you will be notified instantly.

|![](/img/groups/con/epics_messaging/Epicstel_addpvgroup.jpeg)|
|-|
|**Figure 4**: addpvgroup Example.|

In this example a request is forwarded to the BOT's Administrators to add a PV group with the following specifications:

- **Name**: RackMonCons

- **PVs**: IA-17:CO-LM35:Temperature-Mon (Max: 30°C  Min: 20°C)

- **Timeout**: 60 minutes


* **/addpv** (Group) (PV) (Maximum Limit) (Minimum Limit)

Sends a request to the BOT administrator to add a new PV to an existing PV Group or alter the maximum and minimum limits of a PV that already exists in a PV Group.

[[File:Epicstel_addpv.jpeg|addpv Example|500px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_addpv.jpeg)|
|-|
|**Figure 5**: addpv Example.|

Following the previous example for ''/addpvgroup'', in the picture a new request is forwarded to the BOT's Administrators to add the PV **IA-17:CO-Fan:Current-Mon** to the previously registered ''RackMonCons PV Group'' with the maximum limit of 0.32A and minimum limit of 0.27A, remembering the ''timeout'' parameter is unique for each PV group (in this example, 60 minutes).

* **/removepv** (Group) (PV)

Sends a request to the BOT administrator to remove a PV from a group. If you're an administrator, that'll remove the PV from the group it's in.

Example: ```/removepv TestGroup SomePV:Voltage ```
#### Teams


* **/add** (Team) (Username:ChatID)

Sends a request to the BOT administrators to add multiple users into the given Team.

Example: ```/add CONS Peter:12345678 ControlsGroup:-87654321```


* **/addteam** (AdminName:AdminID) (Team) (UserName:UserID)

Sends a request to the BOT administrators to register a new Team.

Example: ```/addteam Peter:12345678 ENGENHARIA-SIRIUS ControlsGroup:-87654321 John:98765432```

<br>

#### Notification subscription

* **/subscribe** (PVGroups)

Subscribes to the requested PVGroups notification **(does not work for group chats due to SPAM policies)**.

Example: Subscribing to 3 new PV groups (IA01, Temp-BO01, Linac) and to one group that the user was already subscribed (CorrenteAnel)

[[File:Epicstel_subscribe.jpeg|Subscription Example|400px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_subscribe.jpeg)|
|-|
|**Figure 6**: Subscription Example.|

[[File:Epicstel_unsubscribe.jpeg|Unsubscription Example|400px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_unsubscribe.jpeg)|
|-|
|**Figure 7**: Unsubscription Example.|

* **/unsubscribe** (PVGroups)

Cancels subscription from the requested PVGroups notification.

Example: unsubscribing from CorrenteAnel PV Group

* **/pause** (PVs/PV Groups)

Pauses PV monitoring for a certain PV without unsubscribing you and your team from the group (only applies to user who executed the command).

Example: ```/pause SomePV:Voltage (single PV)
         /pause SomeGroup (single group)
         /pause SomePV:Voltage SomePV:Current SomePV:Radiation (multiple PVs)```

* **/unpause** (PVs/PV Groups)

Unpauses PV monitoring for a certain PV, does not subscribe/re-subscribe you to the group (only applies to user who executed the command).

Example: ```/unpause SomePV:Voltage (single PV)
         /unpause SomeGroup (single group)
         /unpause SomePV:Voltage SomePV:Current SomePV:Radiation (multiple PVs)```

<br>

#### Team Administrator
Team Administrators also have access to the following commands:

* **/subscribeteam** (Team) (PV Groups)

Subscribes the Team they manage to the desired PV Groups.

Example: /subscribeteam CONS Temperature-LINAC SI:01-Pressure

* **/unsubscribeteam** (Team) (PV Groups)

Unsubscribes the Team they manage from the desired PV Groups.

Example: /unsubscribegp CONS Temperature-LINAC SI:01-Pressure

* **/teams**

Sends the list of Teams registered. 

* **/getids** (Teams)

Sends a list of users and chat ids from the desired Team.

Example: /getids CONS ADM ENGENHARIA-SIRIUS

* **/remove** (Team) (ChatIDs)

Removes the users with the specified chat_ids from the Team they manage.

Example: /remove CONS 12345678

<br>

#### Administrator
Administrators also have access to the following commands

* **/removepvgroup** (PVGroups)

Removes PV Groups that are not being used from the program files.

Example: /removepvgroup Temperature-LINAC SI:01-Pressure

* **/forward** (ChatID) (Message)

If ChatID is an authorized user, forwards the specified message to the desired ChatID.

Example: /forward 12345678 Hello! To perform a caget simply send '/caget' followed by the PVs you desire to acquire

* **/update**

Updates all dictionaries and authorized personnel according to the program files. Use when manually altering the program files.

* **/enabledisconnectmon** (PVs)

Enables disconnect monitoring and auto-pausing (maintains data, interrupts archiving) of PVs. Since PV pausing applies ''globally'', affecting all users, this must be done by an administrator (enabled by default).

Example:```/enabledisconnectmon SomePV:Voltage```

* **/disabledisconnectmon** (PVs)

Disables disconnect monitoring and auto-pausing.

Example:```/disabledisconnectmon SomePV:Voltage```


The commands: /add, /addteam, /addpvgroup, /removepv and /addpv use the same syntax specified before, the only difference is Administrators already have permission to write on the files (''be careful!'').

<br>

## Application

The Software was written in Python3 and uses 3 modules to read .csv files that contain information about PV Groups and authorized users and using that data write an algorithm to answer properly through Telegram. These modules are:

* pyepics - Python/EPICS integration

* telepot - Python/TelegramBot integration

* pandas - acronym for Python Data Analysis, used to read the files

<br>

### Files

The program generates three Comma Separated Values (CSV) files containing and one log file for errors.

<br>

#### Authorized Personnel CSV

This file contains the user Teams authorized to use the bot. Each cell is a user's credential, Name:ChatID pair.

<br>

#### Groups CSV

This file contains the information about all PV Groups, including it's Process Variables, their maximum and minimum limits and the PV Group timeout.

PVs are divided by semicolons, their limits are also divided that way and are in the same sequence as the PVs.

<br>

#### Monitor Info CSV

This file contains monitoring information about the PVs: PVGroup, limits and users subscribed (separeted by semicolons in ChatIDs column). It's generated by using Groups CSV file and permit monitoring.

<br>

#### Telegram Bot Log

Registers every message that comes to the bot and many other occurences and errors.

<br>

### Dictionaries

The application uses many dictionaries to organize data about users and PVs.

<br>

#### PV Dictionaries

* **all_groups**

Enables quick access to PV groups names, which PVs said groups contain and their maximum and minimum limits. Structured as:

all_groups = {'PV_Group_A' : {'timeout' : x, 'PV1' : [max, min], 'PV2' : [max, min]}}


* **PV_values**

It's keys are the monitored PVs names' and it's values are the PV objects. Structured as:

PV_values = {'PV1' : epics.PV, 'PV2' : epics.PV}


* **PV_mon**

Contains all monitoring information, organized in "folders": PV_Group > PV_Name > Users > Limits

Structured as:

PV_mon = {'Grupo_de_PVs' : {'PV1' : {'chat_id' : {'max' : max, 'min' : min, 'timeout' : timeout, 'tmax' : time_since_max, 'tmin' : time_since_min, 'max_bool' : max_trigger, 'min_bool' : min_trigger}}}}

Where:

- max = maximum limit

- min = minimum limit

- timeout = timeout between notification

- tmax = time since PV overcame maximum limit

- tmin = time since PV overcame minimum limit

- max_bool = trigger for maximum limit

- min_bool = trigger for minimum limit

<br>

#### User Dictionaries

* authorized_personnel

A simple dictionary that contains the users' credentials being the ChatID a key and the FirstName the value:

authorized_personnel = {'123456' : Name1, '987654' : Name2}

* teams

Provides information of which team contain which users:

teams = {'TeamX' : {'123456' : Name1', '987654' : Name2}, 'TeamY' : {'456123' : Name3, '987654' : Name2}}

<br>

### Help

For support, questions, suggestions or bug reports, message [Guilherme]([https://t.me/g_freitas){target=_blank} or [Patricia](https://t.me/patriciahn){target=_blank}. If you prefer, you could also mailto: guilherme.freitas@cnpem.br mail one of the developers directly.

<br>

## EPICSTel User Interface

[[File:epicstel_ui.png|EPICSTel UI's current appearance|500px|thumb]]

|![](/img/groups/con/epics_messaging/Epicstel_ui.png)|
|-|
|**Figure 8**: EPICSTel UI's current appearance.|

In order to facilitate changes to the EPICSTel database by admins, a GUI was created. Focusing on ease of use, this interface is capable of editing production databases directly (with authentication), local files or creating new databases altogether.

<br>

### Requirements

Along with the [Sirius HLA CONS GUI](https://github.com/lnls-sirius/pydm-opi){target=_blank}, from which you can display the EPICSTel Management Interface, you must have the following Python packages installed:

* [Paramiko](https://pypi.org/project/paramiko){target=_blank} (used for SSH file transfer)
* [Pandas](https://pypi.org/project/pandas){target=_blank} (used for file manipulation)

An easy way of installing all three requirements (assuming you're using pip) is:

```
pip install siriushlacon paramiko pandas**
```

<br>

### Technical Aspects

Currently, the UI establishes a SSH connection with the production server hosting the EPICSTel bot in order to download relevant database files. These files are stored temporarily in the user's computer and are checked for errors before being displayed.

In order to push back a change to the server, the user must authenticate with valid credentials (the same ones used in the Archiver Management Interfaces). Otherwise, he won't be able to apply any modifications to groups, PVs or other data at all.
