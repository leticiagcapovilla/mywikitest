---
title: Sirius control system single-board computers
description: 
published: 1
date: 2024-03-05T19:07:44.396Z
tags: 
editor: markdown
dateCreated: 2024-03-05T19:07:44.396Z
---

# CON: Sirius control system SBCs

<br />

## Default configuration for SBCs

This section presents a brief tutorial about how to set up a BeagleBone Black/Green for use in [[Machine:Control_System|Sirius control system]]. The procedure has been used for the development of control node prototypes.

Currently we are working with BeagleBone Black Revision C (the last hardware version of the board) and Beaglebone Green. It's necessary to configure the software environment before running applications.

With an "out of the box" BeagleBone Black/Green, first of all we write the latest operating system (OS) image to the board. Our OS choice is Debian Linux 7 (Wheezy). In a Linux desktop machine running Ubuntu (just as [[CON:CON|Controls Group]] workstations), download the image with:

 $ wget <nowiki>https://debian.beagleboard.org/images/rcn-ee.net/rootfs/bb.org/release/2016-06-15/console/bone-debian-7.11-console-armhf-2016-06-15-2gb.img.xz</nowiki>

There are two options of BeagleBone Black/Green official Debian 7 images. A minimal one ("console image") and another with several software packages included ("LXDE image"). The last comes with LXDE (Lightweight X11 Desktop Environment), a graphical environment, among other software that absolutely aren't useful for our purposes.

Insert a microSD card into the computer and run GNOME Disks, in order to write the downloaded image to the card:

 $ gnome-disks

Select the inserted device, click on the "More actions" button and choose "Restore Disk Image...". Then indicate the previously downloaded image file and click on "Start Restoring...". It might require superuser permission.

After the process has been completed, it is possible to run Debian 7.11 from this microSD card. In order to flash the image into your Beaglebone's eMMC, edit the file ''uEnv.txt'' with sudo permission:
 $ sudo nano /PATH_TO_YOUR_MEDIA/boot/uEnv.txt

And uncomment the following line at the end of the file:
 #cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh

Unmout the device and insert it into BeagleBone Black microSD card slot (the board must be powered off). Then, without any other cable or cape plugged, connect a 5V power supply to the board. Wait until D2, D3, D4 and D5 blue LEDs start to blink in sequence.

When the OS image has been downloaded into board's eMMC (embedded MultiMediaCard), the four LEDs will be on for some time and then the board shuts down. It's time to remove the microSD card from slot.

Now we take away the 5V power supply and plug an Ethernet cable to BeagleBone Black/Green. It's necessary to connect it to the Internet in order to perform software updates and install further basic software. When working at our office with prototypes, we use DHCP for network authentication, since the "console image" has by default a network configuration with dynamic IP.

Plug the BeagleBone Black/Green to a PC with a USB cable and wait some time until its boot process is done.

All instructions presented here must be executed from a desktop machine in a SSH terminal:

 $ ssh root@192.168.7.2

It is appropriate to update all installed software:

 # apt-get update

It is also recommended to install and configure Locales framework, which switches between multiple languages and allow users to use their configurations (language, country, characters, etc).
 
 $ apt-get install locales
 $ dpkg­-reconfigure locales

Generate, at least, these locales: ''en_US.UTF-8 UTF-8'' and ''pt_BR.UTF-8 UTF-8''. Select them from the list. OK. Define ''english'' as default locale for the system environment. OK. Wait until locales are generated and, finally, upgrade all installed software:

 # apt-get upgrade

BeagleBone Black/Green Debian "console image" is minimal. We need several other software packages from now on:

 # apt-get -y install acpid acpi-support-base am335x-pru-package build-essential device-tree-compiler git man-db ntp perl picocom procserv python python-dev python-numpy swig telnet usbutils

After that, set the system time zone to "America/Sao_Paulo" with ''dpkg-reconfigure'' utility:

 # dpkg-reconfigure tzdata

Disabling BeagleBone Black HDMI interface is mandatory. Some AM335x HDMI pins may be configured for other funcionalities, but this can only be done after disabling the video. [[CON:PRUserial485|PRUserial485]] serial interface PRU software, for instance, uses the same pins as the HDMI interface for communication. So, if HDMI video is not disabled, [[CON:PRUserial485|PRUserial485]] will not work. Moreover, we will never plug a video monitor to a BeagleBone Black. Skip this step if you are configuring a Beaglebone Green, once it does not have HDMI interface. To disable HDMI video, execute:

 # nano /boot/uEnv.txt

Then uncomment the following line at the file and reboot the board:

 #cape_disable=capemgr.disable_partno=BB-BONELT-HDMI,BB-BONELT-HDMIN

 # reboot

After performing previous steps, it's time to install some software intended to support applications. All software installed from now on is used by one or more [[Machine:Control_System|Sirius control system]] server-side software, so installing all packages listed below results in a BeagleBone Black/Green ready for use in any network node.

<br />

### EPICS Base

Download and build EPICS Base with:

 # apt-get -y install libreadline-gplv2-dev
 # cd
 # wget --no-check-certificate <nowiki>https://epics.anl.gov/download/base/base-3.15.5.tar.gz</nowiki>
 # tar -xvzf base-3.15.5.tar.gz
 # rm base-3.15.5.tar.gz
 # cd base-3.15.5
 # make

It's convenient to add EPICS binaries directory to the system path and set other two environment variables. Edit ''/root/.bashrc'', adding at the end of the file:

 export PATH=/root/base-3.15.5/bin/linux-arm:$PATH
 export EPICS_BASE="/root/base-3.15.5"
 export EPICS_HOST_ARCH="linux-arm"
 export EPICS_CA_MAX_ARRAY_BYTES=1048576

To apply these settings to the current session:

 # source /root/.bashrc

<br />

### asynDriver

asynDriver is an useful EPICS module for communication to control hardware. Installing it is very simple:

 # cd
 # wget --no-check-certificate <nowiki>https://epics.anl.gov/download/modules/asyn4-33.tar.gz</nowiki>
 # tar -xvzf asyn4-33.tar.gz
 # rm asyn4-33.tar.gz
 # sed -i -e '3,4s/^/#/' -e '8s/^/#/' -e '11s/^/#/' -e '14cEPICS_BASE=/root/base-3.15.5' asyn4-33/configure/RELEASE
 # cd asyn4-33
 # make

<br />

### Python modules

We don't install Python modules available at Debian repositories or with pip in BeagleBone Black. Instead, all modules we use are installed from sources.

pySerial allows Python code to access serial ports. Currently we are using version 3.4 (latest release) of this module.

 # cd
 # git clone <nowiki>https://github.com/pyserial/pyserial.git</nowiki>
 # cd pyserial
 # git checkout c54c81d933b847458d465cd77e96cd702ff2e7be
 # python setup.py install

requests is a Python library for handling HTTP requests easily. The steps below are required for requests 2.9.1 installation, the same version we use on desktop workstations with Ubuntu Linux:

 # cd
 # git clone <nowiki>https://github.com/requests/requests.git</nowiki>
 # cd requests
 # git checkout 1108058626450b863d154bb74d669754b480caa4
 # python setup.py install

pcaspy is a module for building EPICS Channel Access servers. Its latest version (0.7.1) can be installed with:

 # cd
 # git clone <nowiki>https://github.com/paulscherrerinstitute/pcaspy.git</nowiki>
 # cd pcaspy
 # git checkout 9b09c54a5a066dfaf9d6fea7a06c07c46226b92c
 # python setup.py install

pyepics is a Channel Access (CA) client for EPICS-based control systems. We work with the latest release of pyepics (3.3.1):

 # cd
 # git clone <nowiki>https://github.com/pyepics/pyepics.git</nowiki>
 # cd pyepics
 # git checkout b9c25433b85661728e0bf60bef2dfecc4db7bfba
 # NOLIBCA=1 python setup.py install

It is necessary to tell pyepics where EPICS libraries are installed. This can be done adding the following line at the end of ''/root/.bashrc'' file:

 export PYEPICS_LIBCA=/root/base-3.15.5/lib/linux-arm/libca.so

Adafruit_BBIO is a library to interface with built-in peripherals in Beaglebone's SoC, such as GPIOs, PWMs and SPI. It can be installed with:

 # git clone <nowiki>https://github.com/adafruit/adafruit-beaglebone-io-python.git</nowiki>
 # cd adafruit-beaglebone-io-python
 # sed -i -e 's/\"-Wno-unit_address_vs_reg\", //g' overlays/builder.py
 # python setup.py install

<br />

### PRUserial485

[[CON:PRUserial485|PRUserial485]] software should be installed on BeagleBone Black with the commands below (the Git repository is available only on the internal network).

 # cd
 # git clone <nowiki>http://git.cnpem.br/patricia.nallin/PRUserial485.git</nowiki>
 # cd PRUserial485/src
 # ./library_build.sh

In order to load [[CON:PRUserial485|PRUserial485]] device tree overlay, run the following command. This script must be executed after every system reboot.

 # ./overlay.sh

Any USB/UART bridge based on the FTDI FT232RL IC should work without any additional software installation. For instance, [[CON:SERIALxxCON|SERIALxxCON]] has a serial interface of this type. Note that BeagleBone Black may not recognize the device if you plug it after system boot. So make sure to plug the USB/UART bridge before turnig on the single-board computer.

<br />

## Customized image

This section will contain a link for downloading the image generated for BeagleBone Black through the configuration guide presented above.

<br />

## Known problems

* In the past, when we were working with older Debian Linux images, sometimes BeagleBone Black Ethernet PHY was't detected at boot. As a consequence, the board couldn't communicate to other nodes in a computer network. As we started using fresher images, we have never experienced this anymore.
* USB/UART bridges based on FT232RL chip have never been recognized by the operating system in an attempt of hotplug connection. Apparently, the only way to get it working is to plug the adapter to the board before turning it on. During the boot, the FTDI chip is always recognized. Although disappointing, this is not a critical issue, since our applications don't require a USB host with hotplug capabilitiy.
* Eventually, when connecting a BeagleBone Black to a Ubuntu desktop PC with a USB cable, USB to Ethernet adapter of the board is not detected by the host machine. When it happens, in some cases the PC can detect the adapter properly after a BeagleBone Black power cycle.
* After a reboot, either via software or hardware, Beaglebone Black running Debian 7.9 may not be able to restart itself. User LEDs remain off, the system does not restart and applications do not run. It is needed to push "reset" button to have it working again. It happens frequently and a "hard-reset system" was developed to reset the hardware automatically every ~30 seconds after a reset command until Beaglebone Black's reboot succeeds.

<br />

## Mechanical design

Section under construction.

<br />

## BeagleBone Green

A few years ago, [[CON:CON|Controls Group]] started working with BeagleBone Black. More recently, [https://beagleboard.org/green BeagleBone Green] was released. It is almost the same as BeagleBone Black, from which it derives. BeagleBone Green doesn't have the HDMI interface, a feature that is not used by any of our applications. Beside that, it costs a few dollars less than BeagleBone Black, which is, indeed, a real advantage.

BeagleBone Green is being used as a cheaper substitute for BeagleBone Black in some designs. From a software perspective, there is no difference between these boards. So Linux images, configuration procedures and applications will work the same way in both of them. But there are some hardware differences between BeagleBone Black and BeagleBone Green. The lack of a barrel jack connector in BeagleBone Green for power supply is the most significant for us.

<br />

## Other BeagleBoard.org boards

Other BeagleBoard.org boards may be useful for control system designs in the future. Aimed at wireless systems, [https://beagleboard.org/black-wireless BeagleBone Black Wireless] and [https://beagleboard.org/green-wireless BeagleBone Green Wireless] are counterparts of their wired Ethernet versions. Another option for embedded designs is [https://beagleboard.org/x15 BeagleBoard-x15], the most powerful board from the BeagleBoard.org pool.

We have bought a few units of the three single-board computers cited in the previous paragraph for some experiments.

<br />

### Wi-Fi configuration for CNPEM campus wireless network

While developing some prototypes with BeagleBone Black Wireless or BeagleBone Green Wireless, the reader may want to connect the board to CNPEM campus wireless network. In order to do that, create a file named ''Proteu.config'' at the directory ''/var/lib/connman'' and add the following content to it, replacing <user> and <password> by the CNPEM credentials.

 [service_Proteu]
 Type=wifi
 Name=Proteu
 EAP=peap
 Phase2=MSCHAPV2
 Identity=<user>
 Passphrase=<password>
 Timeservers=pool.ntp.br

After saving the file, the system will connect to the campus wireless network in a while. An IP will be obtained through DHCP.

<br />

## External links

*[https://beagleboard.org/black BeagleBone Black web site]
