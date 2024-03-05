---
title: Setup workstations for sirius
description: 
published: 1
date: 2024-03-05T21:04:51.299Z
tags: 
editor: markdown
dateCreated: 2024-03-05T20:57:59.965Z
---

# FAC:Setup workstations for sirius

## Create Users

Then create user 'fac' in group fac:

*sudo adduser fac; # need to choose a password for fac user*
*sudo usermod -aG sudo fac*

Create other local users:

```
for user in fernando ximenes guilherme liulin ana alexandre murilo; do
sudo adduser $user --ingroup fac; # initialize the password with boo500mev
sudo usermod -aG sudo $user;
done;
```

logout and login with your local user.

## Configure ssh with other computers

If you already have the publickey method for ssh configured in other computer and you want to keep that configuration, including the keys. Just copy the folder:

`scp -r <other machine>:~/.ssh ~/`

and skip the rest of this section.

Generate your public key

`ssh-keygen` 

and copy it to all the computers you want to login without password:

`ssh-copy-id <computer name or address>`

and create the ssh config file:

```
echo "Host *" > ~/.ssh/config
echo "        ForwardX11 yes" >> ~/.ssh/config
echo "        PreferredAuthentications publickey,password" >> ~/.ssh/config
```

## Install Git

```
sudo apt-get install git
git config --global core.editor vim
git config --global push.default simple
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Open the [https://www.github.com github] website and add the ssh key of your computer:
 
`cat ~/.ssh/id_rsa.pub`
 
to the list of authorized keys.

## Create fac_files folder

```
cd /home
sudo mkdir -p fac_files/
sudo chown -R fac fac_files
sudo sed -i -e 's/\(remount-ro\)/&,acl/; s/\(defaults\)/&,acl/' /etc/fstab
sudo mount -oremount /
sudo mount -oremount /home/ # in case your /home is in a different partition
sudo chgrp -R fac fac_files
sudo setfacl -Rdm u::rwx,g:fac:rwx,o::r /home/fac_files
sudo setfacl -Rm u::rwx,g:fac:rwx,o::r /home/fac_files
cd /home/fac_files/
mkdir lnls-fac lnls-sirius lnls-ima
```

## Install the scripts repository

The sirius-bashrc file is useful for compiling and using some of the packages below, as it defines environment variables and add binaries to the path. First clone the [https://github.com/lnls-fac/scripts scripts] repository with

```
cd /home/fac_files/lnls-fac
git clone ssh://git@github.com/lnls-fac/scripts
```

Then install bashrc-sirius and binaries:

```
sudo apt-get install -y make
cd scripts
sudo make develop
```

Finally, source bashrc-sirius in your .bashrc file, adding the following lines to it (at the beggining of the file):

```
sed -i -e '5i #Sirius bashrc' ~/.bashrc
sed -i -e '6i SIRIUSBASHRC=/usr/local/etc/bashrc-sirius' ~/.bashrc
sed -i -e '7i if [ -f "$SIRIUSBASHRC" ] ; then' ~/.bashrc
sed -i -e '8i \ \ \ \ source "$SIRIUSBASHRC"' ~/.bashrc
sed -i -e '9i fi\n' ~/.bashrc
```

Load the new bashrc file:

`source ~/.bashrc`

## Append useful aliases to /etc/hosts

```
sudo chown fac.fac /etc/hosts && sudo chmod g+wr /etc/hosts
fac-hosts-update.py
```

## Install Python3.6

We defined to use python 3.6 as the default version of python to run our applications. Considering that the native version of Ubuntu 16.04 is python3.5, it is necessary to install python3.6 as an alternate version. The link bellow has the instruction for compiling python3.6.

```
sudo apt-get install build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev \
                     libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev 
cd ~/Downloads
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
tar xzf Python-3.6.1.tgz
cd Python-3.6.1/
./configure --enable-shared --with-ensurepip=install
make -j32
make -j32 test
sudo make altinstall
sudo ldconfig
sudo ln -f -s /usr/local/bin/python3.6 /usr/bin/python-sirius
```

## Install Epics

Clone the sirius repository which makes the installation and install:

 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/epics-dev.git
 cd epics-dev/
 git checkout base-3.15
 ./run-all.sh -a no -e yes -x no -s yes -i -o -c

To add the binaries to the path and define useful environment variables, install the bashrc-sirius as described above.

## pcaspy and pyepics

Install pcaspy and pyepics:
 sudo -H pip3.6 install pyepics
 sudo apt-get install swig
 sudo -HE pip3.6 install pcaspy

=Download and install Qt=
 cd ~/Downloads
 wget http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run
 chmod +x qt-unified-linux-x64-online.run
 sudo ./qt-unified-linux-x64-online.run 

Follow the instructions and install version 5.10.1.

 sudo ln -s /opt/Qt/5.10.1/gcc_64/bin/designer /usr/local/bin/designer-qt5

=SIP and PyQt5.10=
First install the package:
 sudo apt-get install libgl1-mesa-dev
Now isntall SIP and PyQt5.10
 cd ~/Downloads
 wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.8/sip-4.19.8.tar.gz
 tar -xvf sip-4.19.8.tar.gz
 cd sip-4.19.8
 python3.6 configure.py
 make -j32
 sudo make install
 cd ../
 wget https://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.10/PyQt5_gpl-5.10.tar.gz
 tar xzf PyQt5_gpl-5.10.tar.gz
 cd PyQt5_gpl-5.10/
 sudo mkdir /opt/Qt/5.10.1/gcc_64/plugins/PyQt5
 python3.6 configure.py --qmake=/opt/Qt/5.10.1/gcc_64/bin/qmake \
                        --sip-incdir=/usr/local/include/python3.6m \
                        --designer-plugindir=/opt/Qt/5.10.1/gcc_64/plugins/designer \
                        --qml-plugindir=/opt/Qt/5.10.1/gcc_64/plugins/PyQt5 \
                        --confirm-license \
                        --assume-shared
 make -j32
 sudo make install

=Install FAC Codes=

In this tutorial we will install the python packages in python3.6, if is is also desired to have them installed in the native python version all the commands must be executed again, replacing python3.6 with python3.

##  Basic python packages:
 sudo apt-get install libffi6 libffi-dev libfreetype6 \
                      libfreetype6-dev libpng3 nmap dvipng
 sudo -H pip3.6 install python-nmap wakeonlan pyepics requests pyqtgraph pandas \
                     psutil termcolor sh cairocffi matplotlib scipy jupyter

change backend of matplotlib to Qt5Agg
 sudo vi /usr/local/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc

## Essential repositories

### MML
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/MatlabMiddleLayer.git
Open matlab as sudo
 sudo matlab
and edit the path to include the folder
 /home/fac_files/lnls-fac/MatlabMiddleLayer/Release/lnls/startup_scripts
close matlab. Open matlab again without sudo:
 matlab
And compile the .mex files in matlab:
 >> sirius;
 >> atmexall;
 >> naff_cc;

### apsuite
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/apsuite.git
 cd apsuite/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### lnls
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/lnls.git
 cd lnls/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### mathphys
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/mathphys.git
 cd mathphys/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### trackcpp
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/trackcpp.git
 cd trackcpp/
 sudo apt-get install g++ libgsl0-dev swig liblapack-dev
 sudo apt-get install libpython3.5-dev libpython3.5
 make -j32 PYTHON=python3.6 PYTHON_VERSION=python3.6
 sudo make develop PYTHON=python3.6 PYTHON_VERSION=python3.6
test with:
 trackcpp

### pyaccel
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/pyaccel.git
 cd pyaccel/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### pymodels
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/pymodels.git
 cd pymodels/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### Control System Constants
 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/control-system-constants.git

### dev-packages
 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/dev-packages.git
 cd dev-packages/siriuspy/
 python3.6 setup.py build
 sudo python3.6 setup.py develop
 cd ../siriusdm
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### pydm
 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/pydm.git
 cd pydm/ 
 sudo pip3.6 install requests scipy numpy pyqtgraph
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### hla
 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/hla.git
 cd hla/pyqt-apps/
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### machine-applications

 cd /home/fac_files/lnls-sirius/
 git clone ssh://git@github.com/lnls-sirius/machine-applications.git

### Virtual Accelerator
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/va.git
 cd va/ 
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### Job Manager
First install the package psutil
 sudo apt-get install python3-pip
 sudo pip3 install psutil
and then, install the package
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/job_manager.git
 cd job_manager/apps
 sudo make install
 cd ../
 sudo ./install_services.py
the last command will finish with errors, but if you run:
 sudo systemctl start pyjob_run.service
it will work.

At this point your terminal will be locked, in order to gain its control again type CRTL+z and then type
 bg
to continue running the service in background.

## Other packages (Optional)

### collective effects
 sudo apt-get install libfftw3-3 libfftw3-dev
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/collective_effects.git
 cd collective_effects/cppcolleff/
 make -j32 PYTHON=python3.6
 sudo make install PYTHON=python3.6
 cd ../pycolleff/
 python3.6 setup.py build
 sudo python3.6 setup.py develop
 cd ../scripts/
 sudo make develop

### FieldMapTrack
 cd /home/fac_files/lnls-fac/
 git clone ssh://git@github.com/lnls-fac/fieldmaptrack.git
 cd fieldmaptrack/
 python3.6 setup.py build
 sudo python3.6 setup.py develop

### CS-Studio LNLS
 cd ~/Downloads
 wget https://github.com/lnls-sirius/lnls-studio/releases/download/4.5.2/lnls-studio-4.5.2-SNAPSHOT-linux.gtk.x86_64.tar.gz
 tar -xvf lnls-studio-4.5.2-SNAPSHOT-linux.gtk.x86_64.tar.gz
 sudo mv lnls-studio /opt/
 cd /opt/lnls-studio
 sudo ln -s /opt/lnls-studio/lnls-csstudio /usr/bin/

### Windows Applications

There are some windows applications for beam dynamics which are very usefull such as OPA MAD8 and ECHO. You can copy a folder with all them from the computer lnls210-linux:
 scp -r lnls210-linux:/home/fac_files/windows_applications /home/fac_files
then, you need to install wine
 sudo apt-get install wine
and finally, create links to the executables:
 sudo ln -s /home/fac_files/windows_applications/ECHO/Linux_MPI/ECHO /usr/bin/echo2d
 sudo ln -s /home/fac_files/windows_applications/ECHO/Release2D_v_2_1a/Codes/Windows/ECHOz1.exe /usr/bin/echoz1
 sudo ln -s /home/fac_files/windows_applications/ECHO/Release2D_v_2_1a/Codes/Windows/ECHOz2.exe /usr/bin/echoz2
 sudo ln -s /home/fac_files/windows_applications/ECHO/Release2D_v_2_1a/Codes/Windows/ECHOzR.exe /usr/bin/echozr
 sudo ln -s /home/fac_files/windows_applications/MAD8/mad8.exe /usr/bin/MAD8
 sudo ln -s /home/fac_files/windows_applications/OPA_versao_3.32/opa.exe /usr/bin/OPA

=Data Repositories=
Create the folder structure:
 cd /home/fac_files
 mkdir -p data/sirius/beam_dynamics
 cd data/sirius/
Clone the collective_effects data repository:
 git clone lnls350-linux:/home/fac_files/repo/collective_effects.git
The Insertion devices data repository:
 git clone lnls350-linux:/home/fac_files/repo/insertion_devices.git
the latest accelerators models' data:
 cd beam_dynamics
 git clone lnls350-linux:/home/fac_files/repo/beam_dynamics/bo.v02.03.git
 git clone lnls350-linux:/home/fac_files/repo/beam_dynamics/si.v22.01.git
 git clone lnls350-linux:/home/fac_files/repo/beam_dynamics/ts.v03.02.git
 git clone lnls350-linux:/home/fac_files/repo/beam_dynamics/tb.v01.02.git
and the electromagnetic simulations data repository:
 cd /home/fac_files/data
 git clone lnls350-linux:/home/fac_files/repo/em_simulations.git

=Other useful applications (Optional)=

Applications available with apt-get:
 sudo apt-get install htop
 sudo apt-get install doxygen
 sudo apt-get install inkscape
 sudo apt-get install texlive-latex-extra texlive-fonts-recommended
 sudo apt-get install kile
 sudo apt-get install okular
 sudo apt-get install flashplugin-*

## Oracle Virtualbox
If you already have a previous version of virtualbox installed, remove it with:
 sudo apt-get purge virtualbox*
You may have to reboot to unload the old kernel modules.

Next, add the repository to your sources
 sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"

Add public keys to verify downloads
 wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
 wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -

Now update to complete the process of adding the repository
 sudo apt-get update

Install dkms if you haven't already
 sudo apt-get install dkms

Install virtualbox:
 sudo apt-get install virtualbox

## Openbox
 sudo apt-get install openbox obconf numlockx gmrun suckless-tools

Configure openbox creating the folder: 
 mkdir ~/.config/openbox
and then create the autostart file, the rc.xml file and the menu.xml file (you can start from a copy of the global files in /etc/xdg/openbox).
logout and login

## Atom Editor
 sudo add-apt-repository ppa:webupd8team/atom
 sudo apt-get update
 sudo apt-get install atom

Atom has some useful packages that can be installed:
#Sublime-Style-Column-Selection: for column selection and edition
#language-matlab: to recognize and highlight matlab codes
#linter-pylama: python module that points out syntax bugs and good practices violations (pep8)
#autocomplete-python: autocomplete with installed packages attributes, methods, modules...
#gitplus: Additional git tools.

## Google Chrome
 wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
 sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
 sudo apt-get update
 sudo apt-get install google-chrome-stable

## Mendeley Desktop
 cd ~/Downloads
 wget https://www.mendeley.com/repositories/ubuntu/stable/amd64/mendeleydesktop-latest
 sudo dpkg -i mendeleydesktop-latest
