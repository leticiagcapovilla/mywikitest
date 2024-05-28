---
title: Diagnostics Beamline Single-Board-Computers (BBB)
description: 
published: 1
date: 2024-05-28T15:53:07.574Z
tags: 
editor: markdown
dateCreated: 2024-05-27T19:40:21.192Z
---

# CON: Diagnostics Beamline BBB SBCs (Debian 9)

## Diagnostics Beamline Team

- Prof. Antonio Rubens Castro
- Paulo de Tarso Fonseca


## Introduction

Beaglebone Black is a credit-card sized computer powered by a Texas Instrument Sitara processor (AM335x). This chip comes with an ARM Cortex-A8 core, running embedded Linux at frequencies up to 1 GHz. There are Debian images dedicated to Beaglebone architecture, which are released by Beagleboard.org.

For this application, latest Debian image for Beaglebone Black has been used (Debian 9.4). Any 9.x will be suitable. For configuring and installing libraries (including Zaber.Serial), refer to Appendix X (Setting Up a Beaglebone Black with Debian 9).

Zaber controllers are connected to Beaglebone through USB ports. Connecting these controllers to the board will have them mapped into two different ttyACMx devices, where x is a number defined by the operating system, they are not static and usually depends on the order that controllers are connected to the board. The automatic port number changes demands software changes constantly.

In order to solve this inconvenience, mapping the controllers into known device names (chosen by the user) is done, according to its master serial number. Zaber controller for motors ABC will always be named as “ttyMotorABC”, for exemple, whenever it is connected to the Beaglebone. Device rules for naming configuring have been created and is detailed in Appendix X (Static naming for Zaber USB controllers).

## Setting Up a Beaglebone Black with Debian 9

This is a brief tutorial about how to set up a BeagleBone Black for interfacing with Zaber controllers. The procedure has been used for the development of first prototype.

Currently, BeagleBone Black Revision C (the last hardware version of the board) is used. It's necessary to configure the software environment before running applications.

#### Initial Configuration
Having a Beaglebone Black in hands, first of all, it is necessary to write the operating system (OS) image to the board. Our OS choice is Debian Linux 9 (Stretch). Debian 9.3 will be downloaded and the upgrade to most recent version will be performed soon. In a Linux desktop machine running Ubuntu, download the image with:

```
$ wget debian.beagleboard.org/images/bone-debian-9.3-lxqt-armhf-2018-01-28-4gb.img.xz
```

There are two options of BeagleBone Black official Debian 9 images. The "Stretch IoT" and the "Stretch LXQT". The last one comes with LXQT (The Lightweight Qt Desktop Environment), agraphical environment. This version will be used for first developments, once it can be connected to a screen through HDMI port and show a graphical desktop.
Insert a microSD card into the computer and run GNOME Disks, in order to write the downloaded image to the card:

```
$ gnome-disks
```

Select the inserted device, click on the "More actions" button and choose "Restore Disk Image...". Then indicate the previously downloaded image file and click on "Start Restoring...". It might require superuser permission.
After the process has been completed, it is possible to run Debian 9.3 from this microSD card.
In order to flash the image into your Beaglebone's eMMC, edit the file "uEnv.txt" with sudo permission:

```
$ sudo nano /PATH_TO_YOUR_MEDIA/boot/uEnv.txt
```

And uncomment the following line at the end of the file:

```
cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh
```

Unmout the device and insert it into BeagleBone Black microSD card slot (the board must be powered off). Then, without any other cable or cape plugged, connect a 5V power supply to the board. Wait until D2, D3, D4 and D5 blue LEDs start to blink in sequence. When the OS image has been downloaded into board's eMMC (embedded MultiMediaCard), the four LEDs will be on for some time and then the board shuts down. It's time to remove the microSD card from slot.
Now take away the 5V power supply and plug an Ethernet cable to Beaglebone Black. It's necessary to connect it to the Internet in order to perform software updates and install further basic software. When working at CNPEM network with prototypes, DHCP is used for network authentication, since the "console image" has by default a network configuration with dynamic IP.
Plug the Beaglebone Black to a PC with a USB cable and wait some time until its boot process is done. The USB connection will be a virtual ethernet connection to Beaglebone Black.
Once the computer detected the board, it is time to access it through SSH.
All instructions presented here must be executed from a desktop machine in a SSH terminal:

```
$ ssh debian@192.168.7.2
```

The default password for the user "debian" is "temppwd". After entering the password, a kernel and a boot loader update should be done. Debian version will be update to 9.x. The scripts for doing so can be found at /opt/scripts which is a git repository.
To run all following scripts as root:

```
$ sudo -i
```

Updating the repository:# cd /opt/scripts

```
# git pull
```

Updating the kernel (this may take a while):

```
# cd /opt/scripts/tools
# ./update_kernel.sh --bone-kernel --lts-4_14
```
Updating the boot loader:

```
# cd /opt/scripts/tools/developers
# ./update_bootloader.sh
```

Confirm that "am335x_evm" is selected and press "y".
After that, reboot:

```
# reboot
```

When getting back from reboot, connect to the board through SSH once again. Then, to run all following scripts as root:

```
$ sudo -i
```

It is appropriate to update all installed software:

```
# apt-get update
```

It is also recommended to install and configure Locales framework, which switches between multiple languages and allow users to use their configurations (language, country, characters, etc):

```
# apt-get install locales
# dpkg-reconfigure locales
```

Generate, at least, these locales: "en_US.UTF-8 UTF-8" and "pt_BR.UTF-8 UTF-8". Select them from the list. OK. Define "en_US.UTF-8" as default locale for the system environment. OK. 
Wait until locales are generated and, finally, upgrade all installed software:

```
# apt-get -y upgrade
# apt-get -y dist-upgrade
# apt-get -y autoremove
# apt-get clean
# reboot
```

#### Changing password

To change password, run the command passwd and type new password:

```
# passwd
```

#### Libraries

Beaglebone Black Debian is minimal. We need several other software packages from now on:

```
# apt-get -y install build-essential man-db ntp perl python-serial swig telnet usbutils python python-dev
```

Some libraries are installed with pip , which includes Zaber Serial. Install them with:

```
# pip install zaber.serial pyserial
```

#### Enabling SSH root login

By default, Debian 9 comes with root login disabled. In order to enable it, it is necessary to edit the "sshd_config" file under /etc/ssh. For this, use the next command:

```
# sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
# /etc/init.d/ssh restart
```

#### Creating the rc.local file

This file is well known in previous Beaglebone Debian versions. It is a shell script that is run after system startup and user scripts that must run automatically is usually added to this file. There is no /etc/rc.local file in Debian 9 by default. In order to create one and have it called upon system
startup, edit the file "/etc/systemd/system/rc-local.service" and add the following content:

```
[Unit]
Description=/etc/rc.local
ConditionPathExists=/etc/rc.local

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99
 
[Install]
WantedBy=multi-user.target
```

After that, create the file "/etc/rc.local" and append the generic content below:

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.Exit 0
```

Finally, make it executable, enable it on boot and start it:

```
# chmod +x /etc/rc.local
# systemctl enable rc-local
# systemctl start rc-local.service
```

To check if any error occurred while starting the service, run the following command:

```
# systemctl status rc-local.service
```


#### NTP client

To keep the computer clock accurate, we choose the Network Time Protocol (NTP). In office, where all the computers are connected to the Internet, we use the servers from the NTP.br project as a reference to keep computer clocks synchronized. Configuring this solution is easy:

```
# sed -i '$apool pool.ntp.br' /etc/ntp.conf
# systemctl restart ntp
```

After that, set the system time zone to "America/Sao_Paulo" with "dpkg-reconfigure" utility:

```
# dpkg-reconfigure tzdata
```

Your Beaglebone Black is now ready for Zaber Controller projects!
