---
title: Setting up EPICS
description: 
published: 1
date: 2024-06-06T19:42:28.604Z
tags: 
editor: markdown
dateCreated: 2024-06-06T19:33:42.682Z
---

# CON: Setting up EPICS

```
apt-get update
apt-get -y upgrade
apt-get -y dist-upgrade
apt-get -y autoremove
apt-get clean
apt-get -y install git ntp
```

```
sed -i -e '21,24s/^/#/' -e '27s/^/#/' -e '$a\\npool pool.ntp.br' /etc/ntp.conf
systemctl restart ntp
```

```
export CONS_IP=10.0.38.42
export CONS_REPO=http://${CONS_IP}:20081/download
```

```
### '''Base'''
apt-get -y install libreadline-gplv2-dev
mkdir -p /opt/epics-R3.15.6
cd /opt/epics-R3.15.6
# wget http://epics.anl.gov/download/base/base-3.15.6.tar.gz
wget ${CONS_REPO}/EPICS/base-3.15.6.tar.gz
tar -xzvf base-3.15.6.tar.gz
rm -f base-3.15.6.tar.gz
mv base-3.15.6 base
mkdir modules
cd base
make
```

```
export EPICS_VERSION=R3.15.6
export EPICS_BASE=/opt/epics-${EPICS_VERSION}/base
export EPICS_MODULES=/opt/epics-${EPICS_VERSION}/modules
export EPICS_HOST_ARCH=$(${EPICS_BASE}/startup/EpicsHostArch)
export PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}
export EPICS_CA_AUTO_ADDR_LIST=YES
```

```
export PYEPICS_LIBCA=${EPICS_BASE}/lib/${EPICS_HOST_ARCH}/libca.so
export ASYN=${EPICS_MODULES}/asyn4-35
export CALC=${EPICS_MODULES}/synApps/calc-R3-7-1
export AUTOSAVE=${EPICS_MODULES}/autosave-R5-9
export SNCSEQ=${EPICS_MODULES}/seq-2.2.6
export BUSY=${EPICS_MODULES}/busy-R1-7-2
export PROCSERVCONTROL=${EPICS_MODULES}/procServControl-1-9
```

```
### '''CaputLog'''
```

This module will log caputs at an iocLogServer. docs at [https://github.com/epics-modules/caPutLog/blob/master/docs/index.rst#id1](https://github.com/epics-modules/caPutLog/blob/master/docs/index.rst#id1)

```
cd ${EPICS_MODULES}
wget https://github.com/epics-modules/caPutLog/archive/R3.6.tar.gz
tar -zxvf R3.6.tar.gz
rm -f R3.6.tar.gz
cd caPutLog-R3.6
sed -i -e '22cEPICS_BASE='${EPICS_BASE} configure/RELEASE
make
```

```
### '''Sequencer'''
apt-get -y install re2c
cd ${EPICS_MODULES} 
# wget http://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.6.tar.gz
wget ${CONS_REPO}/EPICS/seq-2.2.6.tar.gz
tar -xvzf seq-2.2.6.tar.gz
rm -f seq-2.2.6.tar.gz
sed -i -e '6cEPICS_BASE=/opt/epics-R3.15.6/base' seq-2.2.6/configure/RELEASE
cd seq-2.2.6
make
```

```
### '''Asyn'''
cd ${EPICS_MODULES}
# wget https://www.aps.anl.gov/epics/download/modules/asyn4-35.tar.gz
wget ${CONS_REPO}/EPICS/asyn4-35.tar.gz
tar -xvzf asyn4-35.tar.gz
rm -f asyn4-35.tar.gz
sed -i \
    -e '3,4s/^/#/'                      \
    -e '8s/^/#/'                        \
    -e '11cSNCSEQ='${SNCSEQ}            \
    -e '14cEPICS_BASE='${EPICS_BASE}    \
    asyn4-35/configure/RELEASE
cd asyn4-35
make
```

```
### '''synApps calc'''
cd ${EPICS_MODULES}
mkdir synApps
cd synApps
# wget https://github.com/epics-modules/calc/archive/R3-7-1.tar.gz
wget ${CONS_REPO}/EPICS/R3-7-1.tar.gz
tar -xvzf R3-7-1.tar.gz
rm -f R3-7-1.tar.gz
sed -i -e '5s/^/#/' -e '7,8s/^/#/' -e '13s/^/#/' \
    -e '17cSNCSEQ='${SNCSEQ} \
    -e '20cEPICS_BASE='${EPICS_BASE} \
    calc-R3-7-1/configure/RELEASE
cd calc-R3-7-1
make
```

```
### '''Autosave'''
cd ${EPICS_MODULES}
# wget https://github.com/epics-modules/autosave/archive/R5-9.tar.gz
wget ${CONS_REPO}/EPICS/R5-9.tar.gz
tar -zxvf R5-9.tar.gz
rm -f R5-9.tar.gz
cd autosave-R5-9
sed -i '8cEPICS_BASE='${EPICS_BASE} configure/RELEASE 
make 
```

```
### '''Streamdevice'''
cd ${EPICS_MODULES}
mkdir StreamDevice-2.8.8
cd StreamDevice-2.8.8
echo '' | USER=root makeBaseApp.pl -t support && echo ''
# wget https://github.com/paulscherrerinstitute/StreamDevice/archive/2.8.8.tar.gz
wget ${CONS_REPO}/EPICS/2.8.8.tar.gz
tar -xvzf 2.8.8.tar.gz
mv StreamDevice-2.8.8 StreamDevice_2_8_8
rm -f 2.8.8.tar.gz
sed -i \
    -e '28iASYN='${ASYN}                  \
    -e '29iCALC='${CALC}                  \
    -e '30iAUTOSAVE='${AUTOSAVE}          \
    configure/RELEASE

if [ $EPICS_HOST_ARCH ##  "linux-arm" ]; then
    echo 'PCRE_INCLUDE=/usr/include' > configure/RELEASE.Common.linux-arm
    echo 'PCRE_LIB=/usr/lib/arm-linux-gnueabihf' >> configure/RELEASE.Common.linux-arm
else 
    echo 'PCRE_INCLUDE=/usr/include' > configure/RELEASE.Common.linux-x86_64
    echo 'PCRE_LIB=/usr/lib/x86_64-linux-gnu' >> configure/RELEASE.Common.linux-x86_64
fi

sed -i \
    -e '29iPROD_LIBS += autosave'           \
    -e '29istreamApp_DBD += asSupport.dbd'  \
    -e '20istreamApp_DBD += system.dbd'     \
    StreamDevice_2_8_8/streamApp/Makefile
sed -i \
    -e '3iinclude "asSupport.dbd"'          \
    StreamDevice_2_8_8/streamApp/streamAppInclude-3-13.dbd
rm -f StreamDevice_2_8_8/GNUmakefile1
sed -i -e '11iDIRS += StreamDevice_2_8_8' Makefile
make
```

```
### '''EtherIP'''
cd ${EPICS_MODULES}
# wget https://github.com/EPICSTools/ether_ip/archive/ether_ip-3-1.tar.gz
wget ${CONS_REPO}/EPICS/ether_ip-3-1.tar.gz
tar -zxvf ether_ip-3-1.tar.gz
rm -f ether_ip-3-1.tar.gz
cd ether_ip-ether_ip-3-1
sed -i  -e '11cEPICS_BASE='${EPICS_BASE}  configure/RELEASE
make
```

```
## '''netDev'''
cd ${EPICS_MODULES}
# wget https://www-linac.kek.jp/cont/epics/netdev/netDev-1.0.4.tar.gz
wget ${CONS_REPO}/EPICS/netDev-1.0.4.tar.gz
tar -zxvf netDev-1.0.4.tar.gz
rm -f netDev-1.0.4.tar.gz
sed -i  -e '18cEPICS_BASE='${EPICS_BASE}  configure/RELEASE
make
```

```
### '''Busy'''
cd ${EPICS_MODULES}
# wget https://github.com/epics-modules/busy/archive/R1-7-2.tar.gz
wget ${CONS_REPO}/EPICS/R1-7-2.tar.gz
tar -zxvf R1-7-2.tar.gz
rm -f R1-7-2.tar.gz
cd busy-R1-7-2
sed -i\
    -e '7,8s/^/#/'                    \
    -e '11cASYN='${ASYN}              \
    -e '14cAUTOSAVE='${AUTOSAVE}      \
    -e '17cBUSY='${BUSY}              \
    -e '20cEPICS_BASE='${EPICS_BASE}  \
    configure/RELEASE
make
```

```
### '''procServControl'''
cd ${EPICS_MODULES}
# wget http://controls.diamond.ac.uk/downloads/support/procServControl/1-9/procServControl-1-9.tgz
wget ${CONS_REPO}/EPICS/procServControl-1-9.tgz
tar -zxvf procServControl-1-9.tgz
rm -f procServControl-1-9.tgz
cd procServControl-1-9/
sed -i -e '18s/^/#/' Makefile
sed -i\
    -e '23s/^/#/'                     \
    -e '26cSNCSEQ='${SNCSEQ}          \
    -e '27cASYN='${ASYN}              \
    -e '28cBUSY='${BUSY}              \
    -e '31cEPICS_BASE='${EPICS_BASE}  \
    configure/RELEASE
make
```
