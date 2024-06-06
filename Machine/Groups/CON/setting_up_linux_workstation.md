# CON: Setting up a Linux workstation

<br>

## Introduction

This page is a tutorial on how to set up a Linux workstation for [Controls Group](/Machine/Groups/CON) office.

<br>

## Linux distribution

Linux has become the standard operating system (OS) for [[CON:CON|Controls Group]] in the past years. Considering the huge variety of flavors (distributions) available, Ubuntu Linux certainly is not the first choice for many people. But it's the recommended OS for our workstations, since it seems to be the most compatible Linux distribution with all the software we use everyday. Because of their extended support period, Ubuntu LTS (long-term support) versions are preferred over the standard Ubuntu releases. Current Ubuntu LTS release is 18.04 (supported until April 2023).

<br>

## Steps for system configuration

The following sections assume the presence of a fresh Ubuntu 18.04 LTS 64-bit installation. Superuser privileges and a connection to the Internet are required for most of the steps described herein.

Many steps below depends on previously described instructions. So the reader should follow this configuration guide sequentially.

<br>

### Upgrading all installed software

First of all, a complete upgrade of the system is recommended. In order to do that, open a command-line shell (Ctrl+Alt+T) and type:

```
$ sudo -i
# apt-get update
# apt-get -y upgrade
# apt-get -y dist-upgrade
# apt-get -y autoremove
# apt-get clean
```

<br>

### Some basic tools

Execute the command below to install some basic tools.

```
# apt-get -y install build-essential git iperf3 meld nmap openssh-server procserv socat ttf-mscorefonts-installer unrar-free
```

<br>

### NTP client

To keep the computer clock accurate, we choose the Network Time Protocol (NTP). In office, where all the computers are connected to the Internet, we use the servers from the [NTP.br project](https://ntp.br/){target=_blank} as a reference to keep computer clocks synchronized. Configuring this solution is easy.

```
# apt-get -y install ntp
# sed -i -e '21,24s/^/#/' -e '27s/^/#/' -e '$a\\npool pool.ntp.br' /etc/ntp.conf
# systemctl restart ntp
```

For Sirius operation, [LNLS Controls Group](/Machine/Groups/CON){target=_blank} will provide some local NTP servers for clock synchronization of all equipment connected to the control system, even those that will not be connected to the Internet.

<br>

### EPICS-related software

EPICS stands for Experimental Physics and Industrial Control System, an ecosystem of open source software for building distributed control systems. It consists of a set of tools, libraries and applications, which should be installed individually. This is our default software platform for [Sirius control system](/Machine/control_system).

<br>

#### EPICS Base

The [EPICS official web site](https://epics.anl.gov/base/index.php){target=_blank} presents a good description of what is EPICS Base:

''"This is the main core of EPICS, comprising the build system and tools, common and OS-interface libraries, Channel Access client and server libraries, static and run-time database access routines, the database processing code, and standard record, device and driver support."''

Currently we work mainly with the 3.15 series of EPICS Base releases (stable releases of EPICS V3). Latest offer from this branch is can be found at [https://github.com/epics-base/epics-base/releases](https://github.com/epics-base/epics-base/releases){target=_blank}. To install EPICS Base R3.15.8, first run the commands below:

```
# apt-get -y install libreadline-gplv2-dev
# cd /opt
# mkdir epics-R3.15.8
# mkdir modules
# cd epics-R3.15.8
# wget https://github.com/epics-base/epics-base/archive/R3.15.8.tar.gz
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

<br>

#### Sequencer

For installing the latest release of [EPICS Sequencer](https://www-csr.bessy.de/control/SoftDist/sequencer/){target=_blank} (2.2.8), enter the following commands:

```
# apt-get -y install re2c
# cd /opt/epics-R3.15.8/modules
# wget https://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.8.tar.gz
# tar -zxvf seq-2.2.8.tar.gz
# rm seq-2.2.8.tar.gz
# cd seq-2.2.8
# sed -i -e '6cEPICS_BASE='${EPICS_BASE} configure/RELEASE
# make
```

Export the following environment variable and append it to ''~/.bashrc'':

```
# export SNCSEQ=${EPICS_MODULES}/seq-2.2.8
```

<br>

#### synApps sscan module

This module contains the sscan [https://epics.anl.gov/bcda/synApps/sscan/sscan.html](https://epics.anl.gov/bcda/synApps/sscan/sscan.html){target=_blank} record and related software for systematically moving positioners, triggering detectors, and acquiring and storing resulting data.

```
# mkdir -p ${EPICS_MODULES}/synApps
# cd ${EPICS_MODULES}/synApps
# wget https://github.com/epics-modules/sscan/archive/R2-11-3.tar.gz
# tar -zxvf R2-11-3.tar.gz
# rm R2-11-3.tar.gz
# cd sscan-R2-11-3
# sed -i -e '7s/^/#/' -e '11cSNCSEQ='${SNCSEQ} -e '14cEPICS_BASE='${EPICS_BASE} configure/RELEASE
# make
```

Export the following environment variable and append it to ''~/.bashrc'':

```
# export SSCAN=${EPICS_MODULES}/synApps/sscan-R2-11-3
```

<br>

#### synApps calc module

Now we install the synApps calc module [https://github.com/epics-modules/calc](https://github.com/epics-modules/calc){target=_blank}, which is required for building and running some IOCs. R3-7-4 is the latest release of the calc module.

```
# cd /opt/epics-R3.15.8/modules
# mkdir synApps
# cd synApps
# wget wget https://github.com/epics-modules/calc/archive/R3-7-4.tar.gz
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

<br>

#### asynDriver

[asynDriver](https://epics.anl.gov/modules/soft/asyn/){target=_blank} (from "Asynchronous Driver Support") is an useful EPICS module for developing input/output controllers (IOCs). We install the latest release of asynDriver from the source code:

```
# cd /opt/epics-R3.15.8
# mkdir modules
# cd modules
# wget https://github.com/epics-modules/asyn/archive/R4-40-1.tar.gz
# tar -zxvf R4-40-1.tar.gz
# rm R4-40-1.tar.gz
# cd cd asyn-R4-40-1/
# sed -i -e '3,7s/^/#/' -e '8s/^/#/' -e '10cSNCSEQ='${SNCSEQ} -e '13cCALC='${CALC} -e '16cSSCAN='${SSCAN}\
        -e '19cEPICS_BASE='${EPICS_BASE} configure/RELEASE
# make
```

Export the following environment variable and append it to ''~/.bashrc'':
 
```
# export ASYN=${EPICS_MODULES}/asyn-R4-40-1
```

<br>

#### StreamDevice

[StreamDevice](http://epics.web.psi.ch/software/streamdevice/){target=_blank} is a generic EPICS device support for devices with a "byte stream" based communication interface.

```
# apt-get -y install libpcre3-dev
# cd /opt/epics-R3.15.8/modules
# wget --no-check-certificate https://github.com/paulscherrerinstitute/StreamDevice/archive/2.8.16.tar.gz
# tar -zxvf 2.8.16.tar.gz
# rm 2.8.16.tar.gz
# cd StreamDevice-2.8.16
# sed -i -e '20cASYN='${ASYN}\
        -e '21cCALC='${CALC}\
        -e '22cSNCSEQ='${SNCSEQ}\
        -e '23cSSCAN='${SSCAN}\
        -e '25cEPICS_BASE='${EPICS_BASE}\
        configure/RELEASE && cat configure/RELEASE
# echo 'PCRE_INCLUDE=/usr/include' > configure/RELEASE.Common.linux-x86_64
# echo 'PCRE_LIB=/usr/lib/x86_64-linux-gnu' >> configure/RELEASE.Common.linux-x86_64
# make
```

<br>

#### StreamDevice 2.7.11

```
# apt-get -y install libpcre3-dev
# cd /opt/epics-R3.15.8/modules
# mkdir StreamDevice-2.7.11
# cd StreamDevice-2.7.11
# echo '' | makeBaseApp.pl -t support && echo ''
# wget https://github.com/paulscherrerinstitute/StreamDevice/archive/stream_2_7_11.tar.gz
# tar -xvzf stream_2_7_11.tar.gz
# rm stream_2_7_11.tar.gz
# sed -i -e '28iASYN=/opt/epics-R3.15.8/modules/asyn4-33' configure/RELEASE
# sed -i -e '29iCALC=/opt/epics-R3.15.8/modules/synApps/calc-R3-7-1' configure/RELEASE
# echo 'PCRE_INCLUDE=/usr/include' > configure/RELEASE.Common.linux-x86_64
# echo 'PCRE_LIB=/usr/lib/x86_64-linux-gnu' >> configure/RELEASE.Common.linux-x86_64
# sed -i -e '20istreamApp_DBD += system.dbd' StreamDevice-stream_2_7_11/streamApp/Makefile
# rm StreamDevice-stream_2_7_11/GNUmakefile
# sed -i -e '11iDIRS += StreamDevice-stream_2_7_11' Makefile
# make
```

<br>

#### PV Gateway

[PV Gateway](https://epics.anl.gov/extensions/gateway/index.php){target=_blank} is an useful tool for EPICS-based control systems. Steps below should be performed for installing the latest release of PV Gateway (2.1.0):

```
# cd /opt/epics-R3.15.8/modules
# wget https://github.com/epics-extensions/ca-gateway/archive/R2-1-0-0.tar.gz
# tar -xvzf R2-1-0-0.tar.gz
# rm R2-1-0-0.tar.gz
# echo 'EPICS_BASE=/opt/epics-R3.15.8/base' > ca-gateway-R2-1-0-0/configure/RELEASE.local
# cd ca-gateway-R2-1-0-0
# make
```

<br>

#### EDM

To install the latest [EDM](https://ics-web.sns.ornl.gov/edm/){target=_blank} release (1-12-105B), first enter the following command to install some dependencies:

```
# apt-get install -y libgif-dev libmotif-dev libxmu-dev libxmu-headers libxt-dev libxtst-dev xfonts-100dpi xfonts-75dpi x11proto-print-dev
```

Then reboot the computer, open a command-line shell (Ctrl+Alt+T), enter superuser mode and change the working directory to ''/opt/epics-R3.15.8''.

```
$ sudo -i
# cd /opt/epics-R3.15.8
```

Although we have installed some Ubuntu packages required by EDM before, there are two other dependencies that are not available at Ubuntu 18.04 LTS repositories: "libxp6" and "libxp-dev". So they can not be installed with tools such as "apt-get". Instead, we download them from an Ubuntu 14.04 LTS mirror, in this case the [Federal University of São Carlos (UFSCar)](http://www.ufscar.br/){target=_blank} mirror.

```
# wget http://mirror.ufscar.br/ubuntu/pool/main/libx/libxp/libxp-dev_1.0.2-1ubuntu1_amd64.deb
# wget http://mirror.ufscar.br/ubuntu/pool/main/libx/libxp/libxp6_1.0.2-1ubuntu1_amd64.deb
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
# export EDM_URL="https://ics-web.sns.ornl.gov/edm/log/getAttachment.php?attachId=473&name=edm-1-12-105B.tgz&type=application/x-compressed-tar&size=3006332&mon=May&theDay=1&year=2017"
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

After building EDM, we configure which component libraries it should use. There is a script at the ''setup'' directory for doing that. Before running the script, it should be modified to include all components required by the EDM screens we have been using:

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

<br>

#### MEDM

[MEDM (Motif Editor and Display Manager)](https://epics.anl.gov/extensions/medm/index.php){target=_blank} is another tool for creating and running operator interfaces. This subsection contains instructions for installing the latest release of MEDM (3.1.14).

```
# apt-get -y install libxpm-dev
# cd /opt/epics-R3.15.8/extensions/src
# wget https://github.com/epics-extensions/medm/archive/MEDM3_1_14.tar.gz
# tar -xvzf MEDM3_1_14.tar.gz
# rm MEDM3_1_14.tar.gz
# cd medm-MEDM3_1_14
# make
# cd /etc/X11/fonts/misc
# wget https://epics.anl.gov/EpicsDocumentation/ExtensionsManuals/MEDM/medmfonts.ali.txt
# mv medmfonts.ali.txt medm.alias
# update-fonts-alias misc
```

After the steps above are performed, a system reboot is necessary to get MEDM working properly.

<br>

#### Control System Studio

[Control System Studio](http://controlsystemstudio.org/){target=_blank} (also written as "CS-Studio") is a very useful supervisor software for EPICS-based control systems. CS-Studio is built upon the Eclipse platform. As it is an open source software, LNLS [Controls Group](/Machine/Groups/CON){target=_blank} maintains a customized distribution of CS-Studio, available at [http://10.0.4.57/lnls-studio/](http://10.0.4.57/lnls-studio/){target=_blank} (internal access only).

Using CS-Studio is simple. Just download the [latest release](https://github.com/lnls-sirius/lnls-studio/releases/download/4.5.2/lnls-studio-4.5.2-SNAPSHOT-linux.gtk.x86_64.tar.gz){target=_blank} from the link above, decompress the file and run the executable "lnls-csstudio" at the root of the directory structure.

```
# apt-get -y install openjdk-8-jre
```

<br>

#### EPICS Base (R3.14)

Although EPICS R3.15 is the default EPICS version adopted at LNLS Controls Group by now, some applications may not be able to work with the R3.15 series of EPICS releases. So keeping the latest release of EPICS Base R3.14 in the system is necessary to work around this problem. For instance, we use [netDev](http://www-linac.kek.jp/cont/epics/netdev/){target=_blank} and [EtherIP](https://ics-web.sns.ornl.gov/kasemir/etherip/){target=_blank} only with EPICS R3.14.

Below are the instructions for installing EPICS Base R3.14.12.7:

```
# cd /opt
# mkdir epics-R3.14.12.7
# cd epics-R3.14.12.7
# wget https://epics.anl.gov/download/base/baseR3.14.12.7.tar.gz
# tar -xvzf baseR3.14.12.7.tar.gz
# rm baseR3.14.12.7.tar.gz
# mv base-3.14.12.7 base
# cd base
# make
```

<br>

#### netDev

[netDev](http://www-linac.kek.jp/cont/epics/netdev/){target=_blank} is an useful module for writing IOCs for Yokogawa programmable logic controllers. Below are the steps for netDev latest release (1.0.3) installation:

```
# cd /opt/epics-R3.14.12.7
# mkdir modules
# cd modules
# wget http://www-linac.kek.jp/cont/epics/netdev/netDev-1.0.3.tar.gz
# tar -xvzf netDev-1.0.3.tar.gz
# rm netDev-1.0.3.tar.gz
# sed -i -e '18cEPICS_BASE=/opt/epics-R3.14.12.7/base' netDev-1.0.3/configure/RELEASE
# cd netDev-1.0.3
# make
```

<br>

#### EtherIP

```
# cd /opt/epics-R3.14.12.7/modules
# wget https://github.com/EPICSTools/ether_ip/archive/ether_ip-2-27.tar.gz
# tar -xvzf ether_ip-2-27.tar.gz
# rm ether_ip-2-27.tar.gz
# sed -i -e '11s/^/#/' -e '12iEPICS_BASE=/opt/epics-R3.14.12.7/base' ether_ip-ether_ip-2-27/configure/RELEASE
# cd ether_ip-ether_ip-2-27
# make
```

<br>

### Python environment

Python is our default programming language for workbench test automation and data visualization and analysis, among other tasks. This section presents some instructions on how to configure a Python environment for everyday.

Ubuntu Linux 18.04 LTS doesn't ship with Python 2 installed, and we don't encourage installing it, as Python 2 end of life was already announced. Current [[CON:CON|Controls Group]] recommendation is working only with Python 3.

For increasing the capabilities of Python, we use a set of additional modules. We always prefer installing the latest available version of Python modules. As Ubuntu Linux repositories usually don't offer these latest versions, our default strategy is installing them with pip. Before calling pip, it is necessary to install it:

```
# apt-get -y install python3-pip
```

In some cases, an older version of a Python module may be part of Ubuntu Linux default installation. If such, we keep using the version that is bundled with Ubuntu, instead of installing another version with pip. requests is an example of this situation. Ubuntu Linux 18.04 LTS includes the version 2.18.4 of this Python module (for Python 3), while requests 2.19.1 is the latest version.

These other Python modules should be installed with pip. Commands below will install the latest version of modules matplotlib (2.2.2), numpy (1.15.0), pcaspy (0.7.1), pyepics (3.3.1), pyqtgraph (0.10.0), pyserial (3.4) and scipy (1.1.0).

```
# pip3 install matplotlib numpy
# apt-get -y install swig
# pip3 install pcaspy
# NOLIBCA=1 pip3 install pyepics
# pip3 install pyqtgraph pyserial scipy
```

<br>

#### PyDM and PyQt

[PyDM](https://github.com/slaclab/pydm){target=_blank} (Python Display Manager) is a tool based on Python and Qt for creating and running graphical user interfaces for EPICS control systems. It provides a drag-and-drop environment for designing operator interfaces trough the Qt Designer application. Moreover, it allows easily embedding Python code inside the screens, for data processing or other parallel tasks. PyDM was chosen by [LNLS Accelerator Physics Group (FAC)](/Machine/Groups/FAC){target=_blank} as the framework for Sirius high-level applications.

As a general rule, we recommend installing always the latest stable release of Python modules with pip. But there are some exceptions. One of them is PyQt, which is a dependency for PyDM. If the user installs PyQt with pip, then the system will have the latest stable release of this Python module, but the library that loads PyDM widgets inside Qt Designer (libpyqt5.so) will be lacking. A common recommendation for solving this issue is building PyQt from sources, but we discourage it, as the building process is not straightforward and may take a long time to complete, especially on older computers. Installing PyQt and Qt Designer through Ubuntu repositories is another way to solve this:

```
# apt-get -y install pyqt5-dev-tools python3-pyqt5 python3-pyqt5.qtsvg python3-pyqt5.qtwebkit qttools5-dev-tools
```

Commands below will install the latest release of PyDM (1.7.3). It is necessary to modify the setup.py file of PyDM to skip PyQt installation through pip. This is done by the first sed command.

```
# cd /opt
# wget https://github.com/slaclab/pydm/archive/v1.7.3.tar.gz
# tar -xvzf v1.7.3.tar.gz
# rm v1.7.3.tar.gz
# sed -i -e '35s/extras/#extras/' -e '36i\ \ \ \ pass' pydm-1.7.3/setup.py
# cd pydm-1.7.3
# pip3 install .[all]
# sed -i -e '$a\PYQTDESIGNERPATH=/opt/pydm-1.7.3' /etc/environment
```

After these steps, the session should be restarted. This way Qt Designer will be able to work with PyDM widgets.

<br>

### Oracle VM VirtualBox

When developing and testing software solutions, sometimes we need to set up some virtual machines. The commands below will install the latest release of [Oracle VM VirtualBox](https://www.virtualbox.org/){target=_blank} (6.0.4), which is the only hypervisor we are currently using.

```
# wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add -
# wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key add -
# add-apt-repository "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian bionic contrib"
# apt-get -y install virtualbox-6.0
```

These instructions were obtained from [Oracle VM VirtualBox Linux downloads web page](https://www.virtualbox.org/wiki/Linux_Downloads){target=_blank}.

<br>

### Docker

[Docker](https://www.docker.com/){target=_blank} is a software technology that provides containerization (operating-system-level virtualization). Currently we are working with Docker Community Edition (CE) on workstations:

```
# apt-get -y install apt-transport-https curl
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
# apt-get install -y docker-ce
```

<br>

### Wireshark

[Wireshark](https://www.wireshark.org/){target=_blank} is a very useful tool for debugging network communications. It can be installed with:

```
# apt-get -y install tshark wireshark
```

When installing Wireshark, the user should see a prompt on the screen, which asks "Should non-superusers be able to capture packets?". As we recommend running Wireshark only as a normal user, "Yes" should be chosen as the answer to this prompt. The file permission setting below, for the file ''/usr/bin/dumpcap'', is necessary to allow all users of the computer to capture packets using Wireshark:

```
# chmod 755 /usr/bin/dumpcap
```

[cashark](https://github.com/mdavidsaver/cashark){target=_blank} is a Wireshark disector plugin for the Channel Access protocol. Installing it is recommended:

```
# cd /opt
# git clone https://github.com/mdavidsaver/cashark.git
# sed -i -e '$a\\ndofile("/opt/cashark/ca.lua")' /etc/wireshark/init.lua
```

As mentioned before, Wireshark should preferably be executed by a normal user. cashark will not work while running Wireshark as root.

<br>

### KiCad suite

KiCad has been adopted as our default electronic design automation (EDA) tool. We always work with the latest stable release of it, which can be installed through these steps:

```
# add-apt-repository --yes ppa:js-reynaud/kicad-5
# apt-get update
# apt-get -y install kicad
```

KiCad depends on Python 2. So the commands above will implicitly install Python 2. As discussed in the [[CON:Setting_up_a_Linux_workstation#Python_environment|Python environment]] section of this document, Python 2 is not recommended for new projects.

<br>

### Atom

[Atom](https://atom.io/){target=_blank} is a free and open-source text editor. Instructions for installing Atom are as follows (obtained from [its official documentation](https://flight-manual.atom.io/getting-started/sections/installing-atom/){target=_blank}):

```
# curl -sL https://packagecloud.io/AtomEditor/atom/gpgkey | apt-key add -
# add-apt-repository "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main"
# apt-get -y install atom
```

<br>

### Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/){target=_blank} is a streamlined code editor with support for development operations like debugging, task running, and version control. It aims to provide just the tools a developer needs for a quick code-build-debug cycle and leaves more complex workflows to fuller featured IDEs. Is available at https://github.com/Microsoft/vscode under the MIT license agreement. 

[Install instructions](https://code.visualstudio.com/docs/setup/linux){target=_blank}.

<br>

<br>

### VNC server

Ubuntu has a built-in VNC server, called Vino. You can configure it in a graphical interface (typing ''Desktop Sharing'' on search bar) ou through command line.

From command line in either Ubuntu 16.04 or 18.04, follow these instructions to configure and set a password:

```
# gsettings set org.gnome.Vino icon-visibility 'always'
# gsettings set org.gnome.Vino prompt-enabled false
# gsettings set org.gnome.Vino vnc-password $(echo -n ''''VNC_PASSWORD'''' | base64)
```

Some VNC clients (such as UltraVNC Viewer) doesn't support the encryption method used by this server, so it must also be disabled by the command below. This option is not available on the graphical interface mentioned above.

```
# gsettings set org.gnome.Vino require-encryption false
```

In order to enable VNC server, it is needed to:

##### Ubuntu 16.04

```
# gsettings set org.gnome.Vino enabled true
```

<br>

##### Ubuntu 18.04

In Ubuntu 18.04, connections on which remote access will be passing must be enabled individually. To show the available ones:
 
```
# nmcli connection show
```

Now, write to system key the connection UUID to be allowed to remotely connect to the device, replacing xxxxx's with connection UUID:

```
# dconf write /org/gnome/settings-daemon/plugins/sharing/vino-server/enabled-connections "['xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx']"
# systemctl restart NetworkManager
```

Now, having your IP address, it is possible to use a VNC client to have desktop shared in another computer. If asked, VNC default port is 5900.
