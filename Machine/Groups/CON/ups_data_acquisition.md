# CON: Ups data acquisition

<br>

## Introduction

Among the data acquisition projects developed by the Sirius Controls Group, are obtaining informations from three UPS that power the Control Network servers, one present in the connectivity room and the other two in the Sirius Linac area. Below, these projects were divided into two, one aimed at Connectivity UPS and the other for the two UPS in the Linac Area, once that the implementation is the same for both.

<br>

## UPS - Connectivity Room

The UPS present in the control rack on connectivity room is from the manufacturer Eaton, model 9130 and connected to it is the CA-RaCtrl:CO-Srv-1 server and a network Switch Aruba 5412R zl2.
On the back of the Eaton 9130, a DB-9 connector is available, through which all communication and information is obtained, since no extra data acquisition card was bought (the compatible boards are of Network Card-MS and MODBUS-MS models). Using this connector, the data obtained is about whether the UPS is charging and whether the battery voltage is low, in addition to being able to obtain the equipment log file.

The data aquisition is though a SerialXXCON Board, via RS-232 serial communication, present in the same rack and with the ip: 10.128.122.101.

This project are available on Gitlab repository, [click here](https://gitlab.cnpem.br/robert.polli/ups_monitoring/){target=_blank}

<br>

### Acquisition of Data Log

The acquisition of events occurred on the UPS is by sending a command via RS232, this command is “0x1b4c”. The response received will be a string containing all the latest equipment events.
In the project repository, there is the file “Read_Event_Log.py”, responsible for opening a serial communication with the UPS, sending the command mentioned and process the information obtained.

<br>

### UPS Status

Beyond to the log file, it is possible to obtain two status about the UPS, if it is on battery (not charging) and whether the voltage level of battery is low, lower than 30% of total capacity. The manufacturar makes available this informations ("bool" type) acessible through the value of two pins on the DB-9 connector, not used in RS-232 communication, the DCD pin and CTS pin.

**CTS – Clear to Send:** This pin is responsible for indicating that the UPS is not charging, assuming "True" if it is on the battery or "False", otherwise.

**DCD – Data Carrier Detect:** This pin has the function of show when the UPS's battery is with a low level, lower than 30%, assuming "True" if the battery voltage is low of "False", otherwise.

Both status are linked to the epics variables and are stored in the Archiver, through the process variables shown below, its possible values are 0 or 1.  

`CA-RaCtrl:UPS-Eaton:OnBattery-Mon`
`CA-RaCtrl:UPS-Eaton:LowBattery-Mon`

<br>

## UPS - Linac Area

In the Area Linac there are two UPS of Santak, model Castle Rack 1-3KVA, one on the rack LA-CN:H1RACK1 and other on rack LA-CN:H1RACK3. The server LA-RaCtrl:CO-Srv-1, the workstation named TA-TiRack:CO-FWSrv-1 and some Advantecs, responsible for controlling the Linac subsystems, are connected to them. 

Among the functionalities of UPS, is the presentation of various data in a [https://10.0.38.46:8800 web interface](){target=_blank}, and this was the way found to acquire the informations and make it available in epics variables. The developed program is based on sending "requests" to this address, processing the response and updating each corresponding Process Variable.

The project developed to both UPS of Linac Area is available on its Gitlab repository, [https://gitlab.cnpem.br/robert.polli/UPS_Linac click here](){target=_blank}.

<br>

### Epics Process Variables 

The available Process Variables are:

|Data| Process Variable |
|-|-|
|Input Voltage| UPS:Linac01:InVoltage-Mon |
|Input Frequency| UPS:Linac01:InFrequency-Mon |
|Output Voltage| UPS:Linac01:OutVoltage-Mon |
|Output Frequency| UPS:Linac01:OutFrequency-Mon |
|Output Apparent Power| UPS:Linac01:OutApparentPower-Mon |
|Output Active Power| UPS:Linac01:OutActivePower-Mon |
|Output Load| UPS:Linac01:OutLoad-Mon |
|Battery Voltage| UPS:Linac01:BatVoltage-Mon |
|Battery Capacity| UPS:Linac01:BatCapacity-Mon |


|Data| Process Variable |
|-|-|
|Input Voltage| UPS:Linac03:InVoltage-Mon |
|Input Frequency| UPS:Linac03:InFrequency-Mon |
|Output Voltage| UPS:Linac03:OutVoltage-Mon |
|Output Frequency| UPS:Linac03:OutFrequency-Mon |
|Output Apparent Power| UPS:Linac03:OutApparentPower-Mon |
|Output Active Power| UPS:Linac03:OutActivePower-Mon |
|Output Load| UPS:Linac03:OutLoad-Mon |
|Battery Voltage| UPS:Linac03:BatVoltage-Mon |
|Battery Capacity| UPS:Linac03:BatCapacity-Mon  |

<br>

### On Battery - Hardware

When doing an analysis of the UPS, it was noted that there is no hardware notification that the equipment is charging, making it impossible to analyze the UPS power if the server were off. Based on this, a hardware was developed to analyze the equipment's input voltage, connected to a SerialXXCON board, to run a program external to the server.

This hardware is basically a relay connected in parallel to the UPS input connector. When there is voltage at the equipment input, a 5V signal is switched and sent to the BBB, which will be responsible for creating and changing the value of the corresponding epics variable.

The epics variables for each UPS in the Linac area are:

`LA-RaCtrl01:UPS-Santak:OnBattery-Mon - 10.128.122.111`
`LA-RaCtrl03:UPS-Santak:OnBattery-Mon - 10.128.122.113`

<br>

### UPS Software

The program utilized to controlling and monitoring all parameters of UPS and make them available on its web interface is the "Winpower", provided by the equipament manufacturer. It is running on Server in Linac Area, with the address 10.0.38.46.

The software must to be running on a Docker application, named "winpower". Access the container and start UPS's monitor program, following:

`./agent start`
`./monitor`

If the Winpower container does not exist, recreate it. The Dockerfile is on path /storage/service/repository/docker-winpower .

<br>

### Web Interface Configurations

For the Winpower program to provide data on its web interface, it is necessary to make two configurations, the first is to select which USB port the UPS is connecting with the Server and the second is to configure the default port of the web page. Opens the program and follow the steps below:

* When opening the program, the first step is to get root privileges. For this just go under *System --> Act as Administrator*. 
* A window will open asking for the Administrator password. Just leave it blank and press the OK button. If wanted, the password can be changed under *System --> Modify Administrator Password*.

* Next, we will configure the Port settings choosing *System --> COM Port Settings*.

* On the window that will open (*Communication Port Settings*) we will have to insert the devicebian8002 correspondent to the UPS. For this, we can list the devices by typing "ls /dev/tty*" on a Terminal window before and after the UPS is plugged and compare both lists to see which device was added.

* After typing the name of the device, just press the *Add* button. The device name should appear in the column to the left under the *COM Port List.*

* Next, we will ask the software to search the device we just entered in the previous window. For this, select *System --> Auto Search Device*.

* On the column to the left there should be a list with all interface connections. After the previous step, the device should have appeared under the *LAN* and *hostname* (lnls105-linux) options, if the search was successful.   

* A simple click on the text written in red under the column to the right should open the UPS interface for monitoring and controlling the system. 


The Next step is to configure the port of the web interface which the program will communicate.

* First, go to *Monitor* and make sure "Accept Remote Control" is checked.
* After, click on *Web Server Control*. 
* The window "Web Server Control" will open, if Http Port is **different from 8800**, press "Stop" button, change the value and click on "Start" button.

<br>

## Notification

Some projects have been developed by the Controls Group to notify if a specific Process Variable has assumed a value out of a defined range. For this application, there are [hmailpy](ttps://github.com/lnls-sirius/mailpy){target=_blank} and [Telegrampy‎](/Machine/Groups/CON/epics_messaging) projects.

<br>

## External Links

[Santak User Manual](https://www.santak.com/upload/file/Castle%20Rack1-3k%20user%20manual.pdf){target=_blank}

[Eaton 9130 UPS - User's Guide](https://www.eaton.com/content/dam/eaton/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/eaton-9130-ups/eaton-9130-ups-pdm-user-guide-manual-164201798.pdf){target=_blank}

[UPS Web Interface - Linac Area](https://10.0.38.46:8800/){target=_blank} (Internal network only)
