# CON: LLRF EPICS IOC

## Introduction

This page will contain all information related to the EPICS IOC for Sirius LLRF systems.

## System setup for building and running the IOC

The guide below was written for a fresh Ubuntu 16.04 LTS (64-bit) installation.

### Upgrading all installed software

First of all, a complete upgrade of the system is recommended. In order to do that, open a command-line shell (Ctrl+Alt+T) and type:

 $ sudo -i
 # apt-get update
 # apt-get -y upgrade
 # apt-get -y dist-upgrade
 # apt-get -y autoremove
 # apt-get clean
<section end=systemUpgrade />
### Some basic tools

Execute the command below to install some basic tools.

 # apt-get -y install build-essential git iperf3 meld nmap openssh-server procserv socat ttf-mscorefonts-installer unrar-free

### NTP client

To keep the computer clock accurate, we choose the Network Time Protocol (NTP). In office, where all the computers are connected to the Internet, we use the servers from the [NTP.br project](https://ntp.br/){target=_blank} as a reference to keep computer clocks synchronized. Configuring this solution is easy.

```
# apt-get -y install ntp
# sed -i -e '21,24s/^/#/' -e '27s/^/#/' -e '$a\\npool pool.ntp.br' /etc/ntp.conf
# systemctl restart ntp
```

For Sirius operation, [LNLS Controls Group](/Machine/Groups/CON) will provide some local NTP servers for clock synchronization of all equipment connected to the control system, even those that will not be connected to the Internet.

### EPICS-related software

#### EPICS Base

The [EPICS official web site](https://epics.anl.gov/base/index.php){target=_blank} presents a good description of what is EPICS Base:

*"This is the main core of EPICS, comprising the build system and tools, common and OS-interface libraries, Channel Access client and server libraries, static and run-time database access routines, the database processing code, and standard record, device and driver support."*

Currently we work mainly with the 3.15 series of EPICS Base releases (stable releases of EPICS V3). Latest offer from this branch is can be found [here](https://github.com/epics-base/epics-base/releases){target=_blank}. To install EPICS Base R3.15.8, first run the commands below:

```
# apt-get -y install libreadline-gplv2-dev
# cd /opt
# mkdir epics-R3.15.8
# mkdir modules
# cd epics-R3.15.8
# wget <nowiki>https://github.com/epics-base/epics-base/archive/R3.15.8.tar.gz</nowiki>
# tar -zxvf R3.15.8.tar.gz
# rm R3.15.8.tar.gz
# mv epics-base-R3.15.8 base
# cd base
# make
```

It is convenient to add EPICS Base binaries directory to the system path and set other environment variables. Edit the file at ''~/.bashrc'', adding at the end of the file:

```
export EPICS_BASE=/opt/epics-R3.15.8/base
export EPICS_MODULES=/opt/epics-R3.15.8/modules
export EPICS_HOST_ARCH=$(${EPICS_BASE}/startup/EpicsHostArch)
export EPICS_CA_MAX_ARRAY_BYTES=1073741824
export PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:$PATH
```

To apply these settings to the current session, enter:

```
# source ~/.bashrc
```

Setting environment variables with information about EPICS Base is required for all users that will work on this platform. So the steps above should be repeated with the ''.bashrc'' file on each of these users home directories.

#### synApps calc module

Now we install the synApps [calc module](https://github.com/epics-modules/calc){target=_blank}, which is required for building and running some IOCs. R3-7-4 is the latest release of the calc module.

```
# cd /opt/epics-R3.15.8/modules
# mkdir synApps
# cd synApps
# wget <nowiki>wget https://github.com/epics-modules/calc/archive/R3-7-4.tar.gz</nowiki>
# tar -zxvf R3-7-4.tar.gz
# rm R3-7-4.tar.gz
# cd calc-R3-7-4
# sed -i -e '5s/^/#/' -e '7,8s/^/#/' -e '12cSSCAN='${SSCAN} -e '16cSNCSEQ='${SNCSEQ}\
         -e '19cEPICS_BASE='${EPICS_BASE} configure/RELEASE
# make
```

Export the following environment variable and append it to ''~/.bashrc'':

```
# export CALC=${EPICS_MODULES}/synApps/calc-R3-7-4
```

### ADP 6.6 and CCE 2.13.21

Another requirement for the IOC is the ADP (Advanced Development Platform) software package from Nutaq. It includes libraries for communication between the computer that is running the IOC and the PicoDigitizer box. Although ADP has been replaced by BAS (Boards & Systems) software tools, Sirius LLRF system relies on ADP because it was used since the beginning of the project. As BAS is not compatible with ADP, porting the whole system to BAS would involve some effort, and in the short term we won't do that.

ADP 6.6 must be used. As it is not available for download on Nutaq's web site anymore, we have requested this version of ADP through [this technical support form](https://www.nutaq.com/technical-support-form/){target=_blank}. If you are reading this tutorial and would like to install ADP 6.6, please ask LNLS Controls Group for the file ''nutaq-adp6-microtca-sdk_6.6.0-2_amd64.deb''. Although Nutaq support team told us this Debian package was designed for Ubuntu 12.04 LTS, we haven't noticed any problems in using it with Ubuntu 16.04 LTS yet. If we notice, certainly we will roll back to Ubuntu 12.04 LTS. To install ADP 6.6, type:

```
# apt-get -y install libtool
# dpkg -i nutaq-adp6-microtca-sdk_6.6.0-2_amd64.deb
```

After installing ADP 6.6, it is necessary to load CCE (Central Communication Engine) version 2.13.21 in the PicoDigitizer. CCE is the software component at the PicoDigitizer that allows its remote control. It is the application used for Ethernet communications between the IOC and the hardware. The PicoDigitizers we bought came with CCE version 3.2.0. As the LLRF system was developed with CCE 2.13.21, which is the CCE version for ADP 6.6, we decided to use it.

To install CCE 2.13.21, first connect the PicoDigiter to the computer, plugging an Ethernet cable between PicoDigitizer Ethernet port 1 and a PCI Express network adapter card in the host computer. Power on the PicoDigitizer and wait for its boot. PicoDigitizer's default IP address is 192.168.0.101, so we configure the network interface in the host computer properly:

```
# ifconfig <interface_name> 192.168.0.100 mtu 9000
```

The maximum transmission unit (MTU) of the network interface on the host computer must be 9000. Otherwise the fast data logger (FDL) functionality of the IOC will not work. To certify you can connect to the PicoDigitizer, just ping its IP address:

```
# ping 192.168.0.101
```

If the device is answering, we can go on. Now we launch ADP Command Line Interface (CLI):

```
# /opt/Nutaq/ADP6/ADP_MicroTCA/sdk/bin/adp_cli.py
```

In ADP CLI, type the following commands to install CCE 2.13.21:

```
ADP$ connect 192.168.0.101
ADP-192.168.0.101$ update_cce /opt/Nutaq/ADP6/ADP_MicroTCA/sdk/fpga/bin/cce
ADP-192.168.0.101$ exit
```

You can now exit ADP CLI:

```
ADP$ exit
```

After these steps, the PicoDigitizer must be power cycled.

### Flashing the FPGA

If the PicoDigitizer you are working with doesn't have the LLRF firmware yet, you should use the ADP CLI to load it into the box. First check if your computer is connected to the PicoDigitizer, as we did in the previous subsection. Then download the firmware at ''/root'' and launch ADP CLI:

```
# cd
# git clone <nowiki>http://gitlab.cnpem.br/claudio.carneiro/dllrf-firmware.git</nowiki>
# /opt/Nutaq/ADP6/ADP_MicroTCA/sdk/bin/adp_cli.py
```

By now the firmware is hosted at [CNPEM Git repository](http://gitlab.cnpem.br/claudio.carneiro/dllrf-firmware){target=_blank} (internal access only).

In ADP CLI, type these commands to load the firmware into the PicoDigitizer:

```
ADP$ connect 192.168.0.101
ADP-192.168.0.101$ fpgaflash 2 /root/dllrf-firmware/Perseus_LLRFLDLS_V22_FPGA315T.bit
ADP-192.168.0.101$ fpgaflash_set_index 2
ADP-192.168.0.101$ exit
ADP$ exit
```

Now the PicoDigitizer must be power cycled. After doing this, launch the ADP CLI one more time to check if the programming task was successful:

```
# /opt/Nutaq/ADP6/ADP_MicroTCA/sdk/bin/adp_cli.py
```

Enter the following commands to get the firmware version from the PicoDigitizer:

```
ADP$ connect 192.168.0.101
ADP-192.168.0.101$ read 0x70000094
```

The last command should return "0x783997ac". This is the decimal number 2017040300, which corresponds to the version of the firmware (version of April 3, 2017).

### Building and running the IOC

After completing the steps above, we build and run the IOC. We are using the LLRF IOC developed at Diamond Light Source, with some minor modifications. At this time, the IOC source code is hosted at [CNPEM Git repository](https://gitlab.cnpem.br/claudio.carneiro/dllrf-epics-ioc){target=_blank} (internal access only).

Clone the repository at ''/root'' with:

```
# cd
# git clone <nowiki>https://gitlab.cnpem.br/claudio.carneiro/dllrf-epics-ioc.git</nowiki>
```

Now we build the sources:

```
# cd dllrf-epics-ioc/PerseusDLLRF
# make
# cd ../IOC/BR-RF-IOC-01App/Db
# ./generate_loop_template.py > loop.template
# ./generate_diag_template.py > diag.template
# cd ../..
# make
# cd ..
```

Alternatively, the user could run a script (build.sh) that contains all the steps needed to build the IOC:

```
# cd dllrf-epics-ioc
# ./build.sh
```

The IOC should be launched with:

```
# cd IOC/iocBoot/iocBR-RF-IOC-01
# ./st.cmd
```

## System setup for running operator interfaces

This section presents a simple tutorial on how to set up a fresh installation of Ubuntu 16.04 LTS (64-bit) for running LLRF operator interfaces.

First follow the steps described in the subsections "[[CON:LLRF_EPICS_IOC#Upgrading_all_installed_software|Upgrading all installed software]]", "[[CON:LLRF_EPICS_IOC#Some_basic_tools|Some basic tools]]", "[[CON:LLRF_EPICS_IOC#NTP_client|NTP client]]" and "[[CON:LLRF_EPICS_IOC#EPICS_Base|EPICS Base]]" above.

### Other EPICS-related software

We are using as operator interfaces for Sirius LLRF systems those developed at Diamond Light Source. They were built upon [Extensible Display Manager (EDM)](https://ics-web.sns.ornl.gov/edm/){target=_blank}. In the future we intend to create new LLRF screens with CS-Studio.

#### EDM

To install the latest [https://ics-web.sns.ornl.gov/edm/ EDM] release (1-12-105B), first enter the following command to install some dependencies:

```
# apt-get install -y libgif-dev libmotif-dev libxmu-dev libxmu-headers libxt-dev libxtst-dev fonts-100dpi xfonts-75dpi x11proto-print-dev
```

Then reboot the computer, open a command-line shell (Ctrl+Alt+T), enter superuser mode and change the working directory to ''/opt/epics-R3.15.8''.

```
$ sudo -i
# cd /opt/epics-R3.15.8
```

Although we have installed some Ubuntu packages required by EDM before, there are two other dependencies that are not available at Ubuntu 18.04 LTS repositories: "libxp6" and "libxp-dev". So they can not be installed with tools such as "apt-get". Instead, we download them from an Ubuntu 14.04 LTS mirror, in this case the [http://www.ufscar.br/ Federal University of São Carlos (UFSCar)] mirror.

```
# wget <nowiki>http://mirror.ufscar.br/ubuntu/pool/main/libx/libxp/libxp-dev_1.0.2-1ubuntu1_amd64.deb</nowiki>
# wget <nowiki>http://mirror.ufscar.br/ubuntu/pool/main/libx/libxp/libxp6_1.0.2-1ubuntu1_amd64.deb</nowiki>
```

Then install both packages with:

```
# dpkg -i libxp6_1.0.2-1ubuntu1_amd64.deb libxp-dev_1.0.2-1ubuntu1_amd64.deb
```

Now the downloaded files can be deleted:

```
# rm libxp6_1.0.2-1ubuntu1_amd64.deb libxp-dev_1.0.2-1ubuntu1_amd64.deb
```

The EDM source code must be built under an [EPICS extensions directory structure](https://epics.anl.gov/extensions/configure/index.php){target=_blank}. The latest extensions directory structure available at [EPICS web site](https://epics.anl.gov/extensions/configure/index.php){target=_blank} is aimed at EPICS R3.14. We have not observed problems while using this directory structure with EPICS R3.15. The directory structure can be downloaded and extracted with:

```
# wget https://epics.anl.gov/download/extensions/extensionsTop_20120904.tar.gz
# tar -xvzf extensionsTop_20120904.tar.gz
```

This guide always present instructions for deleting downloaded compressed files:

```
# rm extensionsTop_20120904.tar.gz
```

It is necessary to modify EPICS extensions configuration files in such a way to set the correct paths to EPICS Base and other system libraries. We use GNU sed for this task:

```
# sed -i -e '21cEPICS_BASE=/opt/epics-R3.15.8/base' -e '25s/^/#/' extensions/configure/RELEASE
# sed -i -e '14cX11_LIB=/usr/lib/x86_64-linux-gnu' -e '18cMOTIF_LIB=/usr/lib/x86_64-linux-gnu' extensions/configure/os/CONFIG_SITE.linux-x86_64.linux-x86_64
```

Now we download the latest EDM release source code and extract the downloaded file at ''/opt/epics-R3.15.8/extensions/src''. Each EPICS extension source code must be there.

```
# cd extensions/src
# export EDM_URL="<nowiki>https://ics-web.sns.ornl.gov/edm/log/getAttachment.php?attachId=473&name=edm-1-12-105B.tgz&type=application/x-compressed-tar&size=3006332&mon=May&theDay=1&year=2017</nowiki>"
# wget --output-document=edm-1-12-105B.tgz $EDM_URL
# tar -xvzf edm-1-12-105B.tgz
# rm edm-1-12-105B.tgz
```

We use GNU sed again to configure the EDM source code build process to consider the GIFLIB version installed on our system.

```
# sed -i -e '15s/$/ -DGIFLIB_MAJOR=5 -DGIFLIB_MINOR=1/' edm/giflib/Makefile
# sed -i -e 's| ungif||g' edm/giflib/Makefile*
```

Here everything is ready to build EDM. So we invoke GNU Make:

```
# cd edm
# make
```

After building EDM, we configure which component libraries it should use. There is a script at the *setup* directory for doing that. Before running the script, it should be modified to include all components required by the EDM screens we have been using:

```
# cd setup
# sed -i -e '53cfor libdir in baselib lib epicsPv locPv calcPv util choiceButton pnglib diamondlib giflib videowidget' setup.sh
# sed -i -e '79d' setup.sh
# sed -i -e '81i\ \ \ \ $EDM -add $EDMBASE/pnglib/O.$ODIR/lib57d79238-2924-420b-ba67-dfbecdf03fcd.so' setup.sh
# sed -i -e '82i\ \ \ \ $EDM -add $EDMBASE/diamondlib/O.$ODIR/libEdmDiamond.so' setup.sh
# sed -i -e '83i\ \ \ \ $EDM -add $EDMBASE/giflib/O.$ODIR/libcf322683-513e-4570-a44b-7cdd7cae0de5.so' setup.sh
# sed -i -e '84i\ \ \ \ $EDM -add $EDMBASE/videowidget/O.$ODIR/libTwoDProfileMonitor.so' setup.sh
```

Now run the script:

```
# HOST_ARCH=linux-x86_64 sh setup.sh
```

Finally, the following lines must be added at the end of ''/root/.bashrc'' file. They set some environment variables necessary for running EDM. Add these lines to ''.bashrc'' files at all user home directories, as we did when installing EPICS Base.

```
export EPICS_EXTENSIONS=/opt/epics-R3.15.8/extensions
 
export PATH=$EPICS_EXTENSIONS/bin/$EPICS_HOST_ARCH:$PATH
 
export EDMPVOBJECTS=$EPICS_EXTENSIONS/src/edm/setup
export EDMOBJECTS=$EPICS_EXTENSIONS/src/edm/setup
export EDMHELPFILES=$EPICS_EXTENSIONS/src/edm/helpFiles
export EDMFILES=$EPICS_EXTENSIONS/src/edm/edmMain
export EDMLIBS=$EPICS_EXTENSIONS/lib/$EPICS_HOST_ARCH
 
export LD_LIBRARY_PATH=$EDMLIBS:$EPICS_BASE/lib/$EPICS_HOST_ARCH
```

To apply the new settings to the current session, enter:

```
# source /root/.bashrc
```

As EDM installation is not trivial, we intend to embed EDM into a [Docker](https://www.docker.com/){target=_blank} container in the future.

We started to work on the LLRF EPICS interface in September 2017, and this was our very first experience with EDM. As we don't have much expertise with it yet, the EDM installation guide above may not be the best it could be. Nevertheless, if you follow it, everything will work fine.

As an example of a problem we had while using EDM, the LLRF screens developed at Diamond use the Arial font. We were not able to make EDM render texts with this font, even after spending some time investigating this issue. So we switched all font definitions in .edl files to Helvetica.

CS-Studio is the default tool that [[CON:CON|LNLS Controls Group]] is using for new EPICS operator interfaces designs.

#### LLRF screens

At the moment, the EDM screens developed at Diamond are hosted at [CNPEM Git repository](http://git.cnpem.br/eduardo.coelho/dllrf-edm-screens){target=_blank} (internal access only). To use them, just clone the repository at ''/root'':

```
# cd
# git clone http://git.cnpem.br/eduardo.coelho/dllrf-edm-screens.git
```

There is a shell script for launching the LLRF main screen. Make sure the IOC is running and then execute this script:

```
# cd dllrf-edm-screens
# ./dllrf-gui.sh
```

As of October 2017, the script ''dllrf-gui.sh'' was created for running the screens in the same computer that runs the IOC. If you intend to run the screens in other computer please edit the definition of environment variables EPICS_CA_AUTO_ADDR_LIST and EPICS_CA_ADDR_LIST in the script.

## Notes about Git repositories

Repositories for LLRF firmware, EPICS IOC and screens are hosted at [CNPEM Git repository](https://gitlab.cnpem.br/){target=_blank} (internal access only).
