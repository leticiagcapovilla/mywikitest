# ELP: Power-supplies-room

In this page we will describe all procedures to execute tasks in Sirius power supplies room.

<br>

##  Run applications for PS Control 

1. Open a Ubuntu terminal:

**Ctrl + Alt + T**

2. Run command:

**sirius-hla-as-launcher.py**

<br>

##  Update repos for PS Control applications 

Run **git pull** in following repos:

**/home/sirius/repos/dev-packages**

**/home/sirius/repos/hla**

<br>

##  Switch use instructions 

1. To access CNPEM corporative network user ports from 1 to 12.

2. To access control network user ports from 13 to 24.

<br>

##  Create virtual COM port in Linux 

1. Open a terminal

2. Run following command:

Obs: 192.168.7.2 is an IP example. You need to replace it with your device IP.

**socat pty,link=/dev/virtualcom0,raw tcp:192.168.7.2:4000 &**
