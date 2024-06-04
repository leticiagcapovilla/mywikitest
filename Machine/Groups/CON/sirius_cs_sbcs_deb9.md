---
title: Sirius control system single-board computers (Debian 9)
description: 
published: 1
date: 2024-06-04T18:09:11.331Z
tags: 
editor: markdown
dateCreated: 2024-06-04T17:45:27.935Z
---

# CON: Sirius control system SBCs (Debian 9)

<br>

## Introduction

This page contains information about single-board computers (SBCs) used in [Sirius control system](/Machine/control_system). Main application of SBCs will be as gateways between Ethernet (default control system communication interface) and RS-485 or RS-232 local serial links. As they will have an embedded Linux operating system (Debian), SBCs can also be used for running EPICS applications associated with the devices to which they communicate.

There are several reasons for adopting SBCs as nodes of the control system. They offer a reasonable processing capacity, small size and necessary peripherals for integration to other devices. Furthermore, there exist some commercial models of SBCs with great cost-benefit ratio, such as the choice for [Sirius control system](/Machine/control_system): BeagleBone Black.

<br>

## BeagleBone Black

|![](/img/groups/con/sirius_cs_sbcs_deb9/BeagleBone_Black.jpg =300x)|
|-|
|**Figure 1**: BeagleBone Black single-board computer.|

BeagleBone Black is a credit-card sized computer powered by a Texas Instrument Sitara processor (AM335x). This chip comes with an ARM Cortex-A8 core, running Linux at frequencies up to 1 GHz. Additionally, it has two other dedicated cores (programmable real-time units, or PRUs). These two cores operate at 200 MHz and can be used to implement real-time tasks. An existing shared memory area permits communication between the main core and PRUs.

Talking about peripherals, BeagleBone Black has everything [Sirius control system](/Machine/control_system) needs: Ethernet and USB. Serial communication could be handled by BeagleBone Black native UARTs, but this option was disconsidered due to:
* Baud rate limitation. Native BeagleBone Black UARTs can't effectively handle communication at higher baud rates. In [Sirius control system](/Machine/control_system), there may be RS-485 serial networks operating at 10 Mbps.
* Need for a previous configuration routine (device tree overlay loading). BeagleBone Black UARTs are not plug-and-play and may lead an unexperienced developer to spend some time setting up UARTs properly.
* In case of RS-232 serial communication, native BeagleBone Black UARTs have only four wires: RxD, TxD, CTS and RTS. DSR and DTR are lacking, and may be useful in some situations.

To address all this issues, other UART peripheral are being developed:

* [PRUserial485](/Machine/Groups/CON/pruserial485), a high-performance RS-485 serial communication interface, which acts as a SPI/UART bridge with a maximum allowable baud rate of 12 Mbps. SPI communication to an external UART (Maxim Integrated MAX3107) is performed by one of the BeagleBone Black PRUs, and a simple C library is available to ease the task of programming user-space applications (the UART interface is not mapped as a system device).
* A circuit with FTDI FT232RL (USB/UART bridge). This bridge can drive a RS-232 or RS-485 serial link. For RS-232 communication, we are using MAX3243 line driver/receiver, from Texas Instruments. RS-485 communication is powered by IL3685 transceiver, from NVE. This interface is intended to operate at baud rates up to 115200 bps, and is mapped into the underlying operating system as a virtual serial port, so writing software to interact with it is straightforward.

These two hardware interfaces are mounted over BeagleBone Black through its two expansion headers. For more information about the associated hardware, see [SERIALxxCON](/Machine/Groups/CON/serialxxcon).

The operating system in SBCs is Debian, a stable and easy-to-use Linux distribution. Ubuntu Linux, which is based on Debian, is the Linux distribution installed in [Controls Group](/Machine/Groups/CON) desktop computers, so no one will have difficulties using Debian.

The default Debian installation of BeagleBone Black comes with interesting libraries and compilers. Moreover, many other software packages can be easily installed through the software repositories of the distribution.

<br>

## Default configuration for SBCs

This section presents a brief tutorial about how to set up a BeagleBone Black, BeagleBone Black Wireless, SeeedStudio BeagleBone Green or SeeedStudio BeagleBone Green Wireless for use in [Sirius control system](/Machine/control_system). The procedure has been used for the development of control node prototypes.

Currently we are working with BeagleBone Black Revision C (the last hardware version of the board) and Beaglebone Green. It's necessary to configure the software environment before running applications.

With an "out of the box" BeagleBone Black/Green, first of all we write the latest operating system (OS) image to the board. Our OS choice is Debian Linux 9 (Stretch). In a Linux desktop machine running Ubuntu (just as [Controls Group](/Machine/Groups/CON) workstations), download the image with:

```
$ wget debian.beagleboard.org/images/bone-debian-9.3-iot-armhf-2018-03-05-4gb.img.xz
```

There are two options of BeagleBone Black/Green official Debian 9 images. The "Stretch IoT" and the "Stretch LXQT". The last one comes with LXQT (The Lightweight Qt Desktop Environment), a graphical environment that absolutely aren't useful for our purposes.

Insert a microSD card into the computer and run GNOME Disks, in order to write the downloaded image to the card:

```
$ gnome-disks
```

Select the inserted device, click on the "More actions" button and choose "Restore Disk Image...". Then indicate the previously downloaded image file and click on "Start Restoring...". It might require superuser permission.

After the process has been completed, it is possible to run Debian 9.3 from this microSD card. In order to flash the image into your Beaglebone's eMMC, edit the file `uEnv.txt` with sudo permission:

```
sudo nano /PATH_TO_YOUR_MEDIA/boot/uEnv.txt
```

And uncomment the following line at the end of the file:

```
#cmdline=init=/opt/scripts/tools/eMMC/init-eMMC-flasher-v3.sh
```

Unmout the device and insert it into BeagleBone Black microSD card slot (the board must be powered off). Then, without any other cable or cape plugged, connect a 5V power supply to the board. Wait until D2, D3, D4 and D5 blue LEDs start to blink in sequence.

When the OS image has been downloaded into board's eMMC (embedded MultiMediaCard), the four LEDs will be on for some time and then the board shuts down. It's time to remove the microSD card from slot.

Now we take away the 5V power supply and plug an Ethernet cable to BeagleBone Black/Green. It's necessary to connect it to the Internet in order to perform software updates and install further basic software. When working at our office with prototypes, we use DHCP for network authentication, since the "console image" has by default a network configuration with dynamic IP.

Plug the BeagleBone Black/Green to a PC with a USB cable and wait some time until its boot process is done.

All instructions presented here must be executed from a desktop machine in a SSH terminal:

```
ssh debian@192.168.7.2
```

The default password for the user `debian` is `temppwd`. After entering the password, a kernel and a boot loader update will be done. The scripts for doing so can be found at /opt/scripts which is a git repository.

Updating the repository:

```
cd /opt/scripts
git pull
```

Get sudo permission:

```
sudo -i
```

Updating the kernel:

```
cd /opt/scripts/tools
./update_kernel.sh --bone-kernel --lts-4_14
```

Updating the boot loader:

```
cd /opt/scripts/tools/developers
./update_bootloader.sh
```

Confirm that `am335x_evm` is selected and press `y`. After that, reboot:

```
reboot
```

It is appropriate to update all installed software:

```
apt-get update

```
It is also recommended to install and configure Locales framework, which switches between multiple languages and allow users to use their configurations (language, country, characters, etc):

```
apt-get install locales
dpkg-reconfigure locales
```

Generate, at least, these locales: `en_US.UTF-8 UTF-8` and `pt_BR.UTF-8 UTF-8`. Select them from the list. OK. Define `en_US.UTF-8` as default locale for the system environment. OK. Wait until locales are generated and, finally, upgrade all installed software:

```
apt-get -y upgrade
apt-get -y dist-upgrade
apt-get -y autoremove
apt-get clean
reboot
```

BeagleBone Black/Green Debian is minimal. We need several other software packages from now on:

```
apt-get -y install acpid acpi-support-base build-essential device-tree-compiler git man-db ntp \
perl picocom procserv python python-dev python-numpy swig telnet usbutils wait-for-it vim tshark
```

After that, set the system time zone to `America/Sao_Paulo` with `dpkg-reconfigure` utility:

```
dpkg-reconfigure tzdata
```

Disabling BeagleBone Black HDMI interface is mandatory. Some AM335x HDMI pins may be configured for other funcionalities, but this can only be done after disabling the video. [PRUserial485](/Machine/Groups/CON/pruserial485) serial interface PRU software, for instance, uses the same pins as the HDMI interface for communication. So, if HDMI video is not disabled, [PRUserial485](/Machine/Groups/CON/pruserial485) will not work. Moreover, we will never plug a video monitor to a BeagleBone Black. Skip this step if you are configuring a Beaglebone Green, once it does not have HDMI interface. To disable HDMI video, execute:

```
sed -i 's/#disable_uboot_overlay_video=1/disable_uboot_overlay_video=1/g' /boot/uEnv.txt
reboot
```

<br>

### Enabling SSH root login and make root owner of /root 

By default, Debian 9 comes with root login disabled. In order to enable it, it is necessary to edit the `sshd_config` file under /etc/ssh. For this, use the next command:

```
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
/etc/init.d/ssh restart
```

Making root owner of /root:

```
chown root:root /root
```

<br>

### Creating the rc.local file

There is no /etc/rc.local file in Debian 9 by default. In order to create one and have it called upon system startup, edit the file `/etc/systemd/system/rc-local.service` and add the following content:

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

After that, create the file `/etc/rc.local` and append the generic content below:

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will `exit 0` on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

exit 0
```

Finally, make it executable, enable it on boot and start it:

```
chmod +x /etc/rc.local
systemctl enable rc-local
systemctl start rc-local.service
```

To check if any error occurred while starting the service, run the following command:

```
systemctl status rc-local.service
```

<br>

### NTP client

To keep the computer clock accurate, we choose the Network Time Protocol (NTP). In office, where all the computers are connected to the Internet, we use the servers from the NTP.br project as a reference to keep computer clocks synchronized. Configuring this solution is easy:

```
apt-get -y install ntp
sed -i '$apool pool.ntp.br' /etc/ntp.conf
systemctl restart ntp
```

For Sirius operation, LNLS Controls group will provide some local NTP servers for clock synchronization of all equipment connected to the control system, even those that will not be connected to the Internet. To configure this server, just type the next commands:

```
sed -i '$aserver 10.128.1.3' /etc/ntp.conf
systemctl restart ntp
```

To check if the servers were added with no errors, use the following command to see them on the list:

```
ntpq -p
```

<br>

### bb.org-overlays repository

This official BeagleBoard repository provides several overlays that can be loaded at the boot of the system by U-Boot. To get the device tree sources files, simply clone the repository:

```
cd 
git clone https://github.com/beagleboard/bb.org-overlays.git
```

To install it we just use apt-get:

```
sudo apt-get update
sudo apt-get install bb-cape-overlays
```

<br>

### beaglebone-universal-io

Another interesting repository to keep in the BeagleBone Black is the beaglebone-universal-io. This repo has some device tree overlays that exports certain pins of BeagleBone Black, depending on the usage or not of the HDMI audio and video interface and the eMMC pins. As the HDMI is not beeing used, we will export all the pins by enabling the `cape-universala-00A0.dtbo` device tree overlay:

```
cd 
git clone https://github.com/cdsteinkuehler/beaglebone-universal-io.git
sed -i 's/#uboot_overlay_addr4=\/lib\/firmware\/<file4>.dtbo/uboot_overlay_addr4=\/lib\/firmware\/cape-universala-00A0.dtbo/' /boot/uEnv.txt
```

This repository has also an useful utility. In the latest versions of Debian for BBB, loading device tree overlays can only be done during the boot. This way, configuring the mode of the pins can be achieved using the provided config-pin utility, which is intended to assist with setting up the various pin modes and querying the current pin state.

After performing previous steps, it's time to install some software intended to support applications. All software installed from now on is used by one or more [Sirius control system](/Machine/control_system) server-side software, so installing all packages listed below results in a BeagleBone Black/Green ready for use in any network node.

<br>

### EPICS Base

Prepare EPICS directory

```
cd /opt
mkdir epics-R3.15.7
```

Download and build EPICS Base with:

```
apt-get -y install libreadline-gplv2-dev
cd /opt/epics-R3.15.7
wget --no-check-certificate https://epics.anl.gov/download/base/base-3.15.7.tar.gz
tar -xvzf base-3.15.7.tar.gz
rm base-3.15.7.tar.gz
mv base-3.15.7 base
cd base
make
```

It's convenient to add EPICS binaries directory to the system path and set other two environment variables. Edit `/root/.bashrc`, adding at the end of the file:

```
export PATH=/opt/epics-R3.15.7/base/linux-arm:$PATH
export EPICS_BASE="/opt/epics-R3.15.7/base"
export EPICS_HOST_ARCH="linux-arm"
export EPICS_CA_MAX_ARRAY_BYTES=1048576
```

To apply these settings to the current session:

```
source /root/.bashrc
```

<br>

### Sequencer

```
apt-get -y install re2c
cd /opt/epics-R3.15.7
mkdir modules
cd modules
wget http://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.6.tar.gz
tar -xvzf seq-2.2.6.tar.gz
rm -f seq-2.2.6.tar.gz
sed -i -e '6cEPICS_BASE=/opt/epics-R3.15.7/base' seq-2.2.6/configure/RELEASE
cd seq-2.2.6
make
```

<br>

### asynDriver

asynDriver is an useful EPICS module for communication to control hardware. Installing it is very simple:

```
cd /opt/epics-R3.15.7/modules
wget --no-check-certificate https://epics.anl.gov/download/modules/asyn4-35.tar.gz
tar -xvzf asyn4-35.tar.gz
rm -f asyn4-35.tar.gz
sed -i \
-e '3,4s/^/#/'                      \
-e '8s/^/#/'                        \
-e '11cSNCSEQ=/opt/epics-R3.15.7/modules/seq-2.2.6'            \
-e '14cEPICS_BASE=/opt/epics-R3.15.7/base'    \
asyn4-35/configure/RELEASE
cd asyn4-35
make
```

<br>

### SynApps

```
cd /opt/epics-R3.15.7/modules
mkdir synApps
cd synApps
wget https://github.com/epics-modules/calc/archive/R3-7-1.tar.gz
tar -xvzf R3-7-1.tar.gz
rm -f R3-7-1.tar.gz
sed -i -e '5s/^/#/' -e '7,8s/^/#/' -e '13s/^/#/' \
    -e '17cSNCSEQ=/opt/epics-R3.15.7/modules/seq-2.2.6' \
    -e '20cEPICS_BASE=/opt/epics-R3.15.7/base' \
    calc-R3-7-1/configure/RELEASE
cd calc-R3-7-1
make
```

<br>

### Autosave

```
cd /opt/epics-R3.15.7/modules
wget https://github.com/epics-modules/autosave/archive/R5-9.tar.gz
tar -zxvf R5-9.tar.gz
rm -f R5-9.tar.gz
cd autosave-R5-9
sed -i '8cEPICS_BASE=/opt/epics-R3.15.7/base' configure/RELEASE 
make
```

<br>

### StreamDevice

REVIEW configure/RELEASE. MISSING EPICS_BASE

```
cd /opt/epics-R3.15.7/modules
wget https://github.com/paulscherrerinstitute/StreamDevice/archive/2.8.8.tar.gz
tar -xvzf 2.8.8.tar.gz
mv StreamDevice-2.8.8 StreamDevice_2_8_8
rm -f 2.8.8.tar.gz
cd StreamDevice_2_8_8
sed -i \
    -e '28iASYN=/opt/epics-R3.15.7/modules/asyn4-35'                \
    -e '29iCALC=/opt/epics-R3.15.7/modules/synApps/calc-R3-7-1'     \
    -e '30iAUTOSAVE=/opt/epics-R3.15.7/modules/autosave-R5-9'       \
    configure/RELEASE
echo 'PCRE_INCLUDE=/usr/include' > configure/RELEASE.Common.linux-arm
echo 'PCRE_LIB=/usr/lib/arm-linux-gnueabihf' >> configure/RELEASE.Common.linux-arm
sed -i \
    -e '29iPROD_LIBS += autosave'           \
    -e '29istreamApp_DBD += asSupport.dbd'  \
    -e '20istreamApp_DBD += system.dbd'     \
    streamApp/Makefile
sed -i \
    -e '3iinclude "asSupport.dbd"'          \
    streamApp/streamAppInclude-3-13.dbd
rm -f GNUmakefile1
sed -i -e '11iDIRS += StreamDevice_2_8_8' Makefile
make
```

<br>

### procServ

```
cd /opt/epics-R3.15.7/modules
wget https://github.com/ralphlange/procServ/releases/download/v2.8.0/procServ-2.8.0.tar.gz
tar -zxvf procServ-2.8.0.tar.gz
rm procServ-2.8.0.tar.gz
cd procServ-2.8.0
./configure --enable-access-from-anywhere
make install
```

<br>

### iocUser

Create a user for running IOCs with minimal system permissions:

```
useradd  iocuser
groupadd ioc
usermod -aG ioc      iocuser
usermod -aG gpio    iocuser
usermod -aG dialout iocuser
```

<br>

### Zabbix

For monitoring SBC's:

```
apt-get install zabbix-agent=1:4.0.3*
systemctl stop zabbix-agent.service
chmod ...
```

Edit the file xxxxxxx

<br>

### Python modules

We prefere to install Python modules in BeagleBone Black through pip, since its version is usually more recent than those ones found at Debian repositories. However, we still use the Debian repositories for some modules or even install the modules directly from sources.

```
pip install --upgrade pip
pip install pip-tools numpy ipython jupyter pandas sympy nose cython pandas pyserial pcaspy pyepics
apt-get install python-scipy
```

It is necessary to tell pyepics where EPICS libraries are installed. This can be done appending their path under the `/root/.bashrc` file:

```
sed -i '$aexport PYEPICS_LIBCA=\/root\/base-3.15.5\/lib\/linux-arm\/libca.so' /root/.bashrc
```

Matplotlib is a useful Python 2D plotting library. In order to install it, we first need to install its dependencies:

```
apt-get install libfreetype6-dev pkg-config
pip --no-cache-dir install matplotlib
```

Now we will install the Python packaging tool `pipenv` and then use it to install the library requests:

```
apt-get install libffi-dev libssl-dev
pip install pipenv
pipenv install requests
```

Adafruit_BBIO is a library to interface with built-in peripherals in Beaglebone's SoC, such as GPIOs, PWMs and SPI. It can also be installed with pip:

```
ntpd pool.ntp.org
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus -y
sudo pip install Adafruit_BBIO
```

The Python version defined as the default is the Python 3.6. We followed the installation guide described [here](https://wiki-sirius.lnls.br/mediawiki/index.php/FAC:Setup_workstations_for_sirius#Install_Python3.6){target=_blank} to install it.

<br>

### AM335x PRU package

In previous Debian versions this package could be installed directly from Debian repository with `apt-get`. However, since it has not been packaged in a long time, we will install it from source:

```
cd 
git clone https://github.com/beagleboard/am335x_pru_package.git
cp am335x_pru_package/pru_sw/app_loader/include/prussdrv.h /usr/include
cp am335x_pru_package/pru_sw/app_loader/include/pruss_intc_mapping.h /usr/include
cd /root/am335x_pru_package/pru_sw/app_loader/interface
make clean
CROSS_COMPILE="" make
cd /root/am335x_pru_package/pru_sw/app_loader/lib
cp libprussdrv.a libprussdrvd.a libprussdrvd.so libprussdrv.so /usr/lib
ldconfig
cd /root/am335x_pru_package/pru_sw/utils/pasm_source
source linuxbuild
cd /root/am335x_pru_package/pru_sw/utils
cp pasm /usr/bin
```

<br>

### PRUserial485

[PRUserial485](/Machine/Groups/CON/pruserial485) software is available in GitHub and should be installed on BeagleBone Black with the commands below:

```
cd
git clone https://github.com/lnls-sirius/pru-serial485
cd PRUserial485/src
./library_build.sh
```

In order to enable the usage of the PRU, a device tree overlay must be loaded. This can be done by editing the file under `/boot/uEnv.txt`, which can be achieved by typing the following command:

```
sed -i 's/#uboot_overlay_addr5=\/lib\/firmware\/<file5>.dtbo/uboot_overlay_addr5=\/lib\/firmware\/uio_pruss_enable-00A0.dtbo/' /boot/uEnv.txt
```

The next script is necessary to reserve DDR memory for PRU serial interface and it must be executed after every system reboot.

```
./overlay.sh
```

Any USB/UART bridge based on the FTDI FT232RL IC should work without any additional software installation. For instance, [SERIALxxCON](/Machine/Groups/CON/serialxxcon.md) has a serial interface of this type. Note that BeagleBone Black may not recognize the device if you plug it after system boot. So make sure to plug the USB/UART bridge before turnig on the single-board computer.

<br>

### SPIxCONV

[[CON:SPIxCONV|SPIxCONV]](link) software support can be installed in BeagleBone Black with the next commands:

```
cd 
git clone https://github.com/ito-rafael/SPIxCONV.git
```

To set the pin modes to support the SPI communication under SPIxCONV, the following commands must be executed:

```
cd /root/SPIxCONV
rm -r cpld/ hardware/ 
cd software/linux
cat /etc/rc.local | sed -i -e "$,/exit 0/{r config-pin SPIxCONV.txt" -e "d}" /etc/rc.local
echo "" >> /etc/rc.local
sed -i '$aexit 0' /etc/rc.local
```

<br>

### bbb-daemon

bbb-daemon is a software tool developed for monitor and initialize Sirius BBB's applications. It is available in GitHub and should be installed on BeagleBone Black with the commands below:

```
cd
git clone http://github.com/lnls-sirius/bbb-daemon
cd bbb-daemon/host
make install
```

<br>

### IOC Bridge

eth-bridge-pru-serial485 is a tool developed for interfacing remote IOC with PRUserial485 library. Recently, it has been used for Power Supplies IOCs.

```
cd 
git clone http://github.com/lnls-sirius/eth-bridge-pru-serial485
cd eth-bridge-pru-serial485/server
make install
```

<br>

### Ponte-py

Ponte is a serial bridge for write/read commands through TCP/IP network, used with ELP applications.

```
cd
git clone http://github.com/lnls-sirius/ponte-py
cd ponte-py
mv src/Ponte.py .
rm -r src/ gui*
```

<br>

## Customized image

This section will contain a link for downloading the image generated for BeagleBone Black through the configuration guide presented above.

<br>

## Known problems

* In the past, when we were working with older Debian Linux images, sometimes BeagleBone Black Ethernet PHY was't detected at boot. As a consequence, the board couldn't communicate to other nodes in a computer network. As we started using fresher images, we have never experienced this anymore.
* USB/UART bridges based on FT232RL chip have never been recognized by the operating system in an attempt of hotplug connection. Apparently, the only way to get it working is to plug the adapter to the board before turning it on. During the boot, the FTDI chip is always recognized. Although disappointing, this is not a critical issue, since our applications don't require a USB host with hotplug capabilitiy.
* Eventually, when connecting a BeagleBone Black to a Ubuntu desktop PC with a USB cable, USB to Ethernet adapter of the board is not detected by the host machine. When it happens, in some cases the PC can detect the adapter properly after a BeagleBone Black power cycle.
* After a reboot, either via software or hardware, Beaglebone Black running Debian 7.9 may not be able to restart itself. User LEDs remain off, the system does not restart and applications do not run. It is needed to push `reset` button to have it working again. It happens frequently and a `hard-reset system` was developed to reset the hardware automatically every ~30 seconds after a reset command until Beaglebone Black's reboot succeeds.

<br>

## Mechanical design

Section under construction.

<br>

## BeagleBone Green

A few years ago, [Controls Group](/Machine/Groups/CON) started working with BeagleBone Black. More recently, [BeagleBone Green](https://beagleboard.org/green){target=_blank} was released. It is almost the same as BeagleBone Black, from which it derives. BeagleBone Green doesn't have the HDMI interface, a feature that is not used by any of our applications. Beside that, it costs a few dollars less than BeagleBone Black, which is, indeed, a real advantage.

BeagleBone Green is being used as a cheaper substitute for BeagleBone Black in some designs. From a software perspective, there is no difference between these boards. So Linux images, configuration procedures and applications will work the same way in both of them. But there are some hardware differences between BeagleBone Black and BeagleBone Green. The lack of a barrel jack connector in BeagleBone Green for power supply is the most significant for us.

<br>

## Other BeagleBoard.org boards

Other BeagleBoard.org boards may be useful for control system designs in the future. Aimed at wireless systems, [BeagleBone Black Wireless](https://beagleboard.org/black-wireless){target=_blank} and [BeagleBone Green Wireless](https://beagleboard.org/green-wireless){target=_blank} are counterparts of their wired Ethernet versions. Another option for embedded designs is [BeagleBoard-x15](https://beagleboard.org/x15){target=_blank}, the most powerful board from the BeagleBoard.org pool.

We have bought a few units of the three single-board computers cited in the previous paragraph for some experiments.

<br>

### Wi-Fi configuration for CNPEM campus wireless network

While developing some prototypes with BeagleBone Black Wireless or BeagleBone Green Wireless, the reader may want to connect the board to CNPEM campus wireless network. In order to do that, create a file named `Proteu.config` at the directory `/var/lib/connman` and add the following content to it, replacing `<user>` and `<password>` by the CNPEM credentials.

```
[service_Proteu]
Type=wifi
Name=Proteu
EAP=peap
Phase2=MSCHAPV2
Identity=<user>
Passphrase=<password>
Timeservers=pool.ntp.br
```

After saving the file, the system will connect to the campus wireless network in a while. An IP will be obtained through DHCP.

<br>

### Configure a static IP connection

Debian, 9 distribution, has a connection manager called `connman`. This manager has its own ways of operating with both static IP and dynamic IP. By default, the IP configuration is set dynamically. But in some cases, it is necessary to make the IP static, but `connman` does not allow IP to be fixed in the ways known to most people, and it overrides the information when the Linux device is rebooted. To prevent this and make the IP static, the steps are:

1) Identify the eth0 name that `connman` manages. In directory in `/var/lib/connman` that identifies eth0:

```
# ls -la /var/lib/connman
It will be shown something like this:
drwxr-xr-x 3 root root 4096 Jan 27 18:42 .
drwxr-xr-x 33 root root 4096 Nov 6 15:28 ..
drwx------ 2 root root 4096 Jan 27 18:42 ethernet_9059af4beffc_cable
-rw------- 1 root root 284 Jan 27 18:42 settings
```

For example the ethernet card eth0 is identified by the directory `ethernet_9059af4beffc_cable`

2) Knowing this directory, run a `connman` command to make the static IP:

```
connmanctl config ethernet_9059af4beffc_cable --ipv4 manual XXX.XXX.XXX.XXX YYY.YYY.YYY.YYY ZZZ.ZZZ.ZZZ.ZZZ
```

Explaining the parts:

```
ethernet_9059af4beffc_cable => identification of eth0 card;
--ipv4 => identification of what will be configured, in this case the ipv4 protocol;
XXX.XXX.XXX.XXX => IP that I chose to configure the static IP of Linux;
YYY.YYY.YYY.YYY => Subnetmask;
ZZZ.ZZZ.ZZZ.ZZZ => Gateway IP #(Optional).
```

3) Reboot.

<br>

## External links

*[BeagleBone Black web site](https://beagleboard.org/black){target=_blank}
