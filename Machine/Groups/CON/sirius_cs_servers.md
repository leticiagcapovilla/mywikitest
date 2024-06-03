---
title: Sirius control system servers
description: 
published: 1
date: 2024-06-03T20:37:26.693Z
tags: 
editor: markdown
dateCreated: 2024-06-03T19:49:45.993Z
---

# CON: Sirius control system servers

<br>

##  Introduction 

This page describes the servers and workstations which will be used to deploy our main applications, such as the [alarm server](/Machine/Groups/CON/control_beast) and [variable archiver](/Machine/Groups/CON/control_archiver).

<br>

##  Hardware description 

|![](/img/groups/con/sirius_cs_servers/Con-srv.jpg =700x)|
|-|
|**Figure 1**: Controls group servers. Placement is not definitive: we should move them to the Sirius installations in 2018.|

The two servers, purchased from [Supermicro](https://www.supermicro.com/index.cfm){target=_blank}, have identical settings and hardware attributes. The following table summarizes all the attributes of these two machines:

**Table 1**: 

|Component| Quantity| Description |
|-|-|-|
|Model| 1| SuperServer 6038R-E1CR16H (Black) |
|Motherboard| 1| Super X10DRH-i |
|Processor| 2| Intel® Xeon® Processor E5-2695 v4 |
|Memory| 8| 64GB DDR4-2400 4Rx4 ECC LRDIMM |
|Network Adapter| 2| Intel® Ethernet Converged Network Adapters X710 10GbE |
|HDD| 16| Seagate 3.5”, 8TB, SAS 12Gb/s, 7.2K RPM, 256M, 512E, Performance(MAKARA+) |
|OS SSD| 2| Seagate Nytro XF1230, 480GB, SATA 6Gb/s, enterprise 2.5" (0.6 DWPD) |
|RAID Controller| 1| AOC-S3108L-H8IR-O-P |

The two workstations, also bought from Supermicro, have more modest features:

**Table 2**: 

|Component| Quantity| Description |
|-|-|-|
|Model| 1| SuperWorkstation 7038A-I |
|Motherboard| 1| Super X10DAi |
|Processor| 2| Intel® Xeon® Processor E5-2620 |
|Memory| 4| 8GB DDR4-2400 4Rx4 ECC LRDIMM |
|Network Adapter| 1| AOC-STGN-i2S |
|HDD| 1| Seagate Entreprise 2.5", 1200GB, SAS 12GB/s, 10k RPM, 128MB, 512n |
|OS SSD| 1| Seagate Enterprise 2.5" Nytro XF1230, 480GB, SATA 6Gb/s, (0.6 DWPD) |
|Graphics Card| 1| Nvidia Quadro M2000 |
|SAS HBA| 1| Supermicro 12Gb/s Eight-Port SAS Internal Host Bus Adapter 

<br>

##  Software description 

<br>

###  Cluster infrastructure 

|![](/img/groups/con/sirius_cs_servers/Cluster.png =700x)|
|-|
|**Figure 2**: Cluster infrastructure.|

The controls group's cluster is composed of three machines (for now), being two servers and one workstation. All those machines share their data through the use of network file system. We have been testing two kind of solutions, [GlusterFS](https://www.gluster.org/){target=_blank} and [Ceph](http://ceph.com/){target=_blank}. For each one, it will presented the setting up steps and the advantages of using the respective soluntion. One of the purposes on using a network file system to replicate data among distributed servers lies on the fact that, with the large growth of the hard disks data capacity in the last decades, RAID recovery times also became larger.  In-house tests showed that a RAID1 set with two 8TB disks (model listed above) took more than 20 hours to be recovered after an intentional disk failure. Besides, the probability of a second disk failure occurs while recovering the first one increases, since that read and write activity is also increased during the recovery process.

Besides distributing the available storage among the servers, the deployment of our services as containers is performed either with [Docker Swarm](https://docs.docker.com/engine/swarm/){target=_blank} or [Kubernetes](https://kubernetes.io/){target=_blank}. At this moment, as the initial configuration for the first one is simpler and some of the tools for starting a Kubernetes cluster are in beta stage [^1] [^2], we decided to use only the Docker Swarm solution. However, we plan as well to provide support for Kubernetes in the near future.

[^1]: https://kubernetes.io/docs/getting-started-guides/centos/centos_manual_config/
[^2]: https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/

From now on, we are going to refer to the machines by their configured hostnames. The servers are named `CA-RaCtrl:CO-Srv-1` and `LA-RaCtrl:CO-Srv-1` and are connected to the switches from the connectiviry and LINAC areas via a dedicated VLAN in other to prevent big latency in their communication exchanges.This latter is the main cause of performance degradation in network filesystems, so maintaining a dedicated channel between them is essencial for the good operation of GlusterFS or Ceph. One of the workstations, named `TA-TiRack:CO-FWSrv-1`, integrates the cluster to work as manager (for Docker Swarm) and as a volume arbitrer (for GlusterFS).  The second workstation `con-workst2` is currently being used in UVX's operation to host the services that will be used in Sirius too. This machine is probably going to be moved to our cluster once that UVX is no longer in operation. The image displayed on the right summarizes our small cloud infrastructure.

<br>

###  Servers 

The next subsections describe the settings present in the controls group servers. Both of them are set up identically, since they are part of the same cluster. To append new hosts to the cluster, the subsections related to GlusterFS (or Ceph) and [[CON:Sirius_control_system_servers#Docker|Docker Swarm]] should be followed.

<br>

####  Status Monitoring 

|![](/img/groups/con/sirius_cs_servers/Ioc.png =700x)|
|-|
|**Figure 3**: OPI interface for monitoring the servers parameters.|

An [input/output controller](http://git.cnpem.br/gustavo.pinton/supermicro-ioc){target=_blank} (available only inside the campus network) was developed in order to monitor the main parameters of the servers, such as temperatures and total input power consumed. An OPI interface was also designed, according the figure to the right.

<br>

####  Operating System 

Both servers are set up with the [CentOS 7](https://www.centos.org/){target=_blank} release. For now, just one of the two OS disk drives was used for this functionality on each server. We've used the default partition scheme of the CentOS' installer, in which `/`, `/home/` and the `swap` area are mounted on [LVM](https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux){target=_blank}) volumes.

The following lines represent the output of `lsblk /dev/sda` (for the operating system's disk).

```
$ lsblk /dev/sdf
NAME                                   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sdf                                      8:80   0 447.1G  0 disk 
├─sdf1                                   8:81   0   200M  0 part /boot/efi
├─sdf2                                   8:82   0     1G  0 part /boot
└─sdf3                                   8:83   0   446G  0 part 
  ├─centos_ca--ractrl--co--srv--1-root 253:0    0    50G  0 lvm  /
  ├─centos_ca--ractrl--co--srv--1-swap 253:1    0     4G  0 lvm  [SWAP]
  └─centos_ca--ractrl--co--srv--1-home 253:2    0   392G  0 lvm  /home
```

<br>

####  Docker 

Independently of the container management tool used, i.e., [[CON:Sirius_control_system_servers#Docker_Swarm|Docker Swarm]] or [Kubernetes](/Machine/Groups/CON/sirius_cs_servers#kubernetes) !!!, both need the Docker engine to work properly.

To install Docker in CentOS 7, follow the described steps from [this official guide](https://docs.docker.com/engine/installation/linux/docker-ce/centos/){target=_blank}.

To enable non-root users to execute `docker` commands, follow [this link](https://docs.docker.com/engine/installation/linux/linux-postinstall/{target=_blank}).

The complete list of applications which will be launched in containers is shown below:

* [[CON:control-beast|Alarm system]]
* [[CON:control-archiver|Archiving system]]
* [[CON:control-olog|Logging system]]
* [[CON:Git_repository|Internal Gitlab system]]

<br>

####  Container orchestration 

We intend to support both Docker Swarm and Kubernetes to manage the containers deployment and scaling. The following subsections provide a guide to set them up.

For now, due to its configuration simplicity, only Docker Swarm was tested with our applications.

<br>

#####  Docker Swarm 

Before reading this subsection, it's suggested that you read the brief [description](https://docs.docker.com/engine/swarm/key-concepts/){target=_blank} of the Docker Swarm architecture's key aspects. Some of the terms used in the next paragraphs are explained in more details in this reference.

All machines joining the cluster, i.e. , `CA-RaCtrl:CO-Srv-1`, `LA-RaCtrl:CO-Srv-1` and `TA-TiRack:CO-FWSrv-1`, work as `manager` nodes, but only the servers act as `worker` nodes. This means that all hosts can act as managers and thus make all new deployments and orchestration decisions if that host was chosen as the cluster leader, but only `CA-RaCtrl:CO-Srv-1` and `LA-RaCtrl:CO-Srv-1` can actually run the docker containers. This choice of implementation supports the failure of up one manager node without interrupting the swarm operation [^3]. On the other hand, if we had chosen to use a single manager node, we wouldn't have this kind of protection. If that node failed, for example, we couldn’t add or remove nodes until recovering it.

[^3]: https://docs.docker.com/engine/swarm/admin_guide/#add-manager-nodes-for-fault-tolerance

`sudo docker node ls` command executed in any of the cluster host gives, therefore:

```
$ sudo docker node ls
ID                            HOSTNAME               STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
xmpld085jzceedss3n78lbxn1 *   CA-RaCtrl-CO-Srv-1     Ready               Active              Reachable           18.03.1-ce
ik2cyo7afqlfysozbo860ce2w     LA-RaCtrl-CO-Srv-1     Ready               Active              Reachable           18.03.1-ce
ykjiz4mhsmr7p2wgvnpxl2e7v     TA-TiRack-CO-FWSrv-1   Ready               Drain               Leader              17.12.1-ce
```

`TA-TiRack-CO-FWSrv-1 ` was elected as the swarm leader in the moment when this information was fetched. It was intentionally marked as '''Drain''' because it was prevented to execute containers and services as explained in this [page](https://docs.docker.com/engine/swarm/swarm-tutorial/drain-node/){target=_blank}. This grants that the heavy processing occurs in the servers only.

For further details about how to set up a node as manager or worker, refer to this [guide](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm){target=_blank}.

To consult which services are active, execute `sudo docker service ls` command, as following:

```
$ sudo docker service ls
ID                  NAME                                   MODE                REPLICAS            IMAGE                                    PORTS
xgxgsgi44y35        con-archiver_epics-archiver            replicated          1/1                 lnlscon/epics-archiver-single:latest     *:11995-11998->11995-11998/tcp
jre4sdbxgl2i        con-archiver_epics-archiver-mysql-db   replicated          1/1                 lnlscon/epics-archiver-mysql-db:latest   
f2gr5yag8zm6        con-beast_alarm-notifier               replicated          1/1                 lnlscon/alarm-server-notifier:latest     
rhi70867x4jb        con-beast_alarm-server                 replicated          1/1                 lnlscon/alarm-server:latest              
bmcc4ckbreho        con-beast_alarm-server-activemq        replicated          1/1                 lnlscon/alarm-server-activemq:latest     *:61616->61616/tcp
s4e64yjr4ev9        con-beast_alarm-server-postgres-db     replicated          1/1                 lnlscon/alarm-postgres-db:latest         *:5432->5432/tcp
j2sczagh505w        con-ldap_openldap-server               replicated          1/1                 osixia/openldap:latest                   *:389->389/tcp, *:636->636/tcp
dnnq5sj06ahl        con-monitor_bbb-server                 replicated          1/1                 lnlscon/bbb-daemon-container:latest      *:6789->6789/tcp, *:9877->9877/tcp, *:9876->9876/udp
626b40arkzy8        con-monitor_redis-db                   replicated          1/1                 redis:latest                             *:6379->6379/tcp
w5y3y75rdc4j        con-olog_olog-mysql-db                 replicated          1/1                 lnlscon/olog-mysql-db:latest             
tj7gbmtv9jb2        con-olog_olog-server                   replicated          1/1                 lnlscon/olog-server:latest               *:1527->1527/tcp, *:4848->4848/tcp, *:8181->8181/tcp
llxjippbhd6k        con-repo_gitlab                        replicated          1/1                 gitlab/gitlab-ce:latest                  *:10000->80/tcp, *:10443->443/tcp
```

Finally, to obtain which host executes a determined service run `sudo docker service ps ID` with the `ID` retrieved from the previous command.

```
$ sudo docker service ps con-repo_gitlab
ID                  NAME                IMAGE                     NODE                 DESIRED STATE       CURRENT STATE            ERROR               PORTS
0shcfz1yszam        con-repo_gitlab.1   gitlab/gitlab-ce:latest   LA-RaCtrl-CO-Srv-1   Running             Running 10 minutes ago 
```

For information about the services deployment process, refer to the documentation of the specific service in one of our [wiki pages](/Machine/Groups/CON).

Services listed above can be accessed from any of the IP addresses currently associated with the machines, which are `10.0.6.44`, `10.0.6.48` and `10.0.6.57`.

<br>

#####  Kubernetes 

As `kubeadm` is still in beta stage [^2], we chose to wait a little longer before setting everything up.

<br>

####  Distributed Network Filesystem 

Two distributed filesystems were considered for our cluster infrastructure. Until this moment, we have only set GlusterFS up, but we plan to deploy Ceph too, since the integration with Kubernetes and [OpenStack](https://www.openstack.org/){target=_blank} is simpler.

Some blogs discuss the advantages and disadvantages of these systems, arguing the use of one above the another. Our group's idea regarding this subject is to test both and verify each one is better suited for the Sirius' needs.

<br>

#####  GlusterFS 

GlusterFS is a scalable network filesystem suitable for data-intensive tasks such as cloud storage and media streaming. Despite being an open-source project, GlusterFS is maintained and developed by Redhat as it constitutes one of the commercial solutions (the other is Ceph) of the company for distributed network filesystems. Besides, GlusterFS is fairly used in Facebook's data clusters [^4] [^5].

[^4]: https://www.socallinuxexpo.org/scale/14x/presentations/scaling-glusterfs-facebook
[^5]: http://blog.gluster.org/scaling-glusterfs-facebook/

For a complete overview of the GlusterFS' architecture, refer to this [guide](http://docs.gluster.org/en/latest/Quick-Start-Guide/Architecture/){target=_blank}. From this point on, it's assumed that the user understands the concepts of GlusterFS volumes and bricks.

<br>

######  Installation 

Initial setting up for GlusterFS in very simple. To install it on CentOS 7, follow the instructions in [link this official guide](https://wiki.centos.org/HowTos/GlusterFSonCentOS){target=_blank}. There are two options of repositories to download the packages from. We chose to use the CentOS Storage SIG package source. First, select the packages version with 

```
$ yum search centos-release-gluster
```

Then, download them with the commands below.

```
$ yum install centos-release-gluster<version>
$ yum install glusterfs gluster-cli glusterfs-libs glusterfs-server
```

Check if the glusterfs daemon is running with 

```
$ systemctl status glusterd.service
$ systemctl enable glusterd.service
```

The last step is setting the firewall to allow the communication in GlusterFS ports. This can be achieved with

```
$ firewall-cmd --zone=public --add-service=nfs --add-service=samba --add-service=samba-client --permanent
success

$ firewall-cmd --zone=public --add-port=111/tcp --add-port=139/tcp --add-port=445/tcp --add-port=965/tcp --add-port=2049/tcp \
--add-port=38465-38469/tcp --add-port=631/tcp --add-port=111/udp --add-port=963/udp --add-port=49152-49251/tcp  --permanent
success

$ firewall-cmd --reload
success
```

If you prefer, you can disable the firewall instead:

```
$ sudo systemctl disable firewalld.service
```

Repeat this procedure for all nodes in the cluster.

'''Reminder:''' If you intend to use GlusterFS with a SELinux distribution such as CentOS, remember to set the policy to permissive!

<br>

######  Peer connection 

Before creating volumes, the nodes in the cluster need to be probed. From any of the nodes, probe the others two with the command 

```
$ gluster peer probe srv_addr
```

`srv_addr` must be replaced by one of the addresses presented in [this page](/Machine/Groups/CON/sirius_cs_servers#bonding-network-interfaces-addresses).

######  Volume creation 

The next step it to create the volumes which the data will be stored into. Volumes are composed of bricks which in our case are equivalent to a whole disk or a fraction, i.e., a partition of it.

To build a brick, choose an available disk and if it has been used before, backup it because all its contents will erased. For the servers, you may need to use the [StorCLI tool](/Machine/Groups/CON/sirius_cs_servers#storcli) to set a disk up for use. Then, format it using the XFS filesystem with the following command:

```
$ sudo mkfs.xfs -i size=512 /dev/sdX
```

Next, mount this disk in a directory, such as `/data/gluster/brick`. Repeat this in all nodes as well. Then, create and start a new volume with

```
$ sudo gluster volume create <volume-name> replica 3 arbiter 1 transport tcp \
                                           10.128.2.3:/data/gluster/brick/data \
                                           10.128.2.4:/data/gluster/brick/data \
                                           10.128.2.5:/data/gluster/brick/metadata
$ sudo gluster volume start <volume-name>
```

`10.128.2.3`, `10.128.2.4` and `10.128.2.5` correspond to the addresses of `LA-RaCtrl:CO-Srv-1`, `CA-RaCtrl:CO-Srv-1` and `A-TiRack:CO-FWSrv-1` respectively. Refer to this [section](/Machine/Groups/CON/sirius_cs_servers#bonding-network-interfaces-addresses) !!!.

The statement `replica 3 arbiter 1` informs the GlusterFS nodes that 3 replicas of each file should be saved, but one of them should operate as an arbiter. This means that for every 3 bricks listed, 1 of them is an arbiter. The kind of brick will store only the file/directory names (i.e. the tree structure) and extended attributes (metadata) but not any data. i.e. the file size (as shown by ls -l) will be zero bytes. It will also store other gluster metadata like the .glusterfs folder and its contents. Since the arbiter brick does not store file data, its disk usage will be considerably less than the other bricks of the replica. The sizing of the brick will depend on how many files you plan to store in the volume. A good estimate will be 4KB times the number of files in the replica. As in the Docker Swarm case, having 3 nodes grants enough quorum to support up to one host failure without interrupting the storage services. Besides, it prevents the volume from being in [split-brain](http://docs.gluster.org/en/latest/Administrator%20Guide/arbiter-volumes-and-quorum/#why-arbiter){target=_blank} state, i.e., a state in which the nodes for some reason have different versions of the same file but cannot decide which one is the good one.

Finally, mount the volume created to append or remove a file:

```
$ sudo mount -t glusterfs 10.128.2.X:/<volume-name> <path_to_mount>
```

An entry can be appended into `/etc/fstab` to mount the volume after a server boots automatically. In this case, append the following line:

```
10.128.2.X:/<volume-name> <path_to_mount> glusterfs  defaults,_netdev  0  0
```

In both cases, make sure that `<path_to_mount>` directory exists.

<br>

######  Control group's servers brick allocation 

The following table summarizes the brick allocation for the control group's services.

**Table 3**: 

|Service| Volume name| CA-RaCtrl:CO-Srv-1 <br> LA-RaCtrl:CO-Srv-1 | TA-TiRack:CO-FWSrv-1| Mount points |
|-|-|-|
|Alarm System <br> Logging System| epics-services| /data/gluster/disk0/epics-services-brick| /data/gluster/epics-services-metadata| /storage/epics-services |
|Gitlab system <br> Network services (DHCP, DNS, ...)| misc| /data/gluster/disk0/misc-brick| /data/gluster/misc-metadata| /storage/misc |
|Archiver System| epics-archiver| /data/gluster/disk0/epics-archiver-brick <br> /data/gluster/disk1/epics-archiver-brick <br> ... <br> /data/gluster/disk15/epics-archiver-brick | /data/gluster/epics-archiver-metadata-0 <br> /data/gluster/epics-archiver-metadata-1 <br> ... <br> /data/gluster/epics-archiver-metadata-15 | /storage/epics-archiver  |

<br>

#####  Ceph 

Ceph is a unified, distributed storage system designed for excellent performance, reliability and scalability.

<br>

######  Installation 

Follow the instructions in the [official website](http://docs.ceph.com/docs/master/start/quick-start-preflight/){target=_blank} to download and in [here](http://docs.ceph.com/docs/master/start/quick-ceph-deploy/){target=_blank} to set a Ceph cluster up.

<br>

####  Kernel-based Virtual Machine 

The two main servers can also host traditional virtual machines through the use of the Linux's KVM technology. KVM or (Kernel-based Virtual Machine) is a full virtualization solution for Linux on Intel 64 and AMD 64 hardware that is included in the mainline Linux kernel since 2.6.20 and is stable and fast for most workloads.

If you need some storage or computing, please contact us with your requirements!

<br>

####  Bonding network interfaces 

The [bonding](https://wiki.linuxfoundation.org/networking/bonding){target=_blank} driver is used to provide high availability and redundancy to the servers, as many interfaces can be aggregated into a single one. We can use it to create two bonded interfaces, one dedicated for the cluster services' communication and another for retriving data from the IOCs and other applications connected to the network. Those interfaces are composed of 2 and 6 physical fiber ports respectively (refer to the server configuration section above).

CentOS provides an application called `nmcli` that can help us to define those virtual interfaces. The following commands are executed in order to create the first bonded interface, `swarm-glusterfs`:

```
$ sudo nmcli connection add type bond ifname swarm-glusterfs bond.options "mode=802.3ad,miimon=100" ipv4.addresses 10.128.2.x/24 ipv4.gateway 10.128.2.1 ipv4.method manual
Connection 'bond-glusterfs-bond' (4f1e7702-e1e2-402d-8a41-020ff3970e6e) successfully added.
```

Add to the interface all the physical ports you desired with the following command:

```
$ nmcli con add type ethernet ifname ens7 master bond-swarm-glusterfs
```

Turn the bonded interface up with

```
$ nmcli con up bond-swarm-glusterfs
```

The configuration shown above is used only to the two main servers which will be connected to different switches, allowing therefore to use the 802.3ad mode to aggregate the interfaces. The bond interface used for general data can be set up the same way as shown above. On the other hand, the workstation cannot use this mode, as its two interfaces must be connected to different core switches. Considering this fact, mode `active-backup` will be used instead. In this mode only one slave in the bond is active. The following commands are executed to set the interfaces accordingly:

```
$ sudo nmcli connection add type bond ifname swarm-glusterfs bond.options "mode=active-backup,miimon=100" ipv4.addresses 10.128.2.5/24 ipv4.gateway 10.128.2.1
Connection 'bond-glusterfs-bond' (4f1e7702-e1e2-402d-8a41-020ff3970e6e) successfully added.

$ sudo nmcli con add type ethernet ifname ens1f0 master bond-swarm-glusterfs
Connection 'bond-slave-ens1f0' (521708de-ece6-472b-9a11-f71f4ce352a4) successfully added.

$ sudo nmcli con add type ethernet ifname ens1f1 master bond-swarm-glusterfs
Connection 'bond-slave-ens1f1' (0d6f29b7-42b8-4ae2-926b-79385eeb5f94) successfully added.

$ sudo nmcli con up bond-swarm-glusterfs
```

<br>

#####  Bonding network interfaces addresses 

Having set the bonded interfaces, we need to choose between static or dynamic addresses. For the cluster's services one, the best approach is to use first option, since they must not depend of any other service such DHCP and, therefore, should never change. For the general data case, the decision is still open. Besides these two bonded interfaces, each server offers a out-of-band IPMI interface for management whose addresses are statically set for the same reasons presented before. Table below summarizes the IP addresses of `CA-RaCtrl:CO-Srv-1`, `LA-RaCtrl:CO-Srv-1` and `TA-TiRack:CO-FWSrv-1`.

**Table 4**: 

| Node| Service| Mode| Address| Server Interfaces| Switch Interfaces |
|-|-|-|-|-|-|
|LA-RaCtrl:CO-Srv-1| GlusterFS, Docker <br> General Data <br> IPMI | Static| 10.128.2.3/24 <br> 10.128.255.3/24 <br> 10.128.1.3/24| enp129s0f0, enp130s0f0 <br> enp129s0f1 <br> ,| D8, F8 <br> C7  <br> -|
|CA-RaCtrl:CO-Srv-1| GlusterFS, Docker <br> General Data <br> IPMI | Static <br>  <br> | 10.128.2.4/24 <br> 10.128.255.4/24 <br> 10.128.0.3/24| enp129s0f0, enp130s0f0 <br> , <br> , | D8, F8 <br>  <br> -|
|TA-TiRack:CO-FWSrv-1| GlusterFS, Docker <br> General Data| Static <br> To be decided| 10.128.2.5/24 <br> -| ens1f0, ens1f1 <br> ,| D5, D5 (one port per switch) <br>|

<br>

####  Connecting to Windows virtual machines from Linux 

Use the `rdesktop` package to connect to the Windows Virtual Machine. In order to do that, you need to enable remote access in your machine. You may use this [guide](https://support.microsoft.com/en-us/help/17463/windows-7-connect-to-another-computer-remote-desktop-connection){target=_blank} for that. Finally, execute the following command from your bash terminal.

```
rdesktop -u <user> <Virtual machine's IP address> -f -g 2560x1440 -x l
```

<br>

####  StorCLI 

The Storage Command Line Tool ([StorCLI](https://docs.broadcom.com/docs/12352476){target=_blank})  is the command line management software designed for the MegaRAID®
product line. The StorCLI is a command line interface that is designed to be easy to use, consistent, and easy to script.

Download the compressed file from the Supermicro's FTP server:

```
$ wget ftp://ftp.supermicro.com/driver/SAS/LSI/3108/managment/StorCLI/storcli_All_OS.zip
```

Unzip it and choose the right version according to the installed operating system. For this guide, we choose the Linux release and the `.rpm` package. Enter `./Linux` folder and execute the following commands, as stated in `read_me.txt`:

```
$ cd Linux/
$ sudo rpm -ivh Linux/storcli-1.23.02-1.noarch.rpm
```

A complete description of this tool can be listed by executing
```
$ /opt/MegaRAID/storcli/storcli64 --help
```

<br>

####  VNC 

A [VNC server](https://wiki.centos.org/HowTos/VNC-Server){target=_blank} is also installed in the servers. To set it up, follow the instructions below:

```
$ sudo yum install vnc-server
$ sudo cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@.service
```

Edit `/etc/systemd/system/vncserver@.service` following the instructions contained in its first lines. Then start the server using display `:1`:

```
$ sudo systemctl daemon-reload
$ sudo systemctl enable vncserver@1.service
```

Before starting it, register the password with `vncpasswd`:

```
$ vncpasswd
$ sudo systemctl start vncserver@1.service
```

In another computer, connect to the server with `vncviewer` and the password registered in the step above (by option of the author, same as the user's):

```
$ vncviewer <server_address>:1
```

<br>

#####  Guacamole 

An [Apache Guacamole](https://guacamole.apache.org/){target=_blank} server is available to provide connection to the VNC servers from a simple web browser. Just access [it](https://10.0.6.57/guacamole){target=_blank}, login and choose the machine to access.

As any other of our services, [Docker configuration files](https://github.com/lnls-sirius/docker-guacamole){target=_blank} were written for deployment in the cluster infrastructure. LDAP is supported for user authentication, but the authorization for a user to use a connection must be granted by an administrator inside Guacamole. This is achieved by [creating a user with the same name](http://guacamole.apache.org/doc/gug/ldap-auth.html#ldap-and-database){target=_blank} as the one registered in the LDAP service.

<br>

###  Workstations 

|![](/img/groups/con/sirius_cs_servers/Con-workst.jpg =250x)|
|-|
|**Figure 4**: Controls group cluster's workstation..|

Both workstations are currently in operation. The first one is installed in the UVX's controls room and hosts some services which store data concerning this accelerator. Those services are also being tested for future uses in the Sirius.

The second workstation is being used as part of the cluster which will be used to host Sirius services. Besides this workstation, this cluster is composed of the two servers described above.

The settings for each one is described in the subsections below.

<br>

####  Cluster's workstation - TA-TiRack:CO-FWSrv-1 

Machine hosting HAProxy and acting as a GlusterFS arbiter and a Swarm drained manager.

<br>

#####  Operating system 

`TA-TiRack:CO-FWSrv-1` runs [Debian 9.2](https://www.debian.org/){target=_blank} release and as its operating system's drive is a solid state drive, only `/boot/efi`, `/boot` and `/` are stored into it. It's exactly the same as we did for the server in the subsection [Operating System](/Machine/Groups/CON/sirius_cs_servers#operating-system).

`lsblk` results in the following output:

```
$ lsblk /dev/sda
NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda       8:0    0 447.1G  0 disk 
├─sda1    8:1    0   190M  0 part /boot/efi
├─sda2    8:2    0   446G  0 part /
└─sda3    8:3    0   954M  0 part /boot
```

This workstation acts as a [manager node for the container swarm](/Machine/Groups/CON/sirius_cs_servers#docker-swarm) and as an [arbitrer node](/Machine/Groups/CON/sirius_cs_servers#glusterfs) for GlusterFS volumes. Refer to the subsections above for further information.

<br>

####  Controls' room workstation - con-workst2 

This workstation is set up with [Ubuntu Server 16.04 LTS](https://www.ubuntu.com/server){target=_blank} and its two network interfaces have the IP addresses `10.128.1.252` (`enp5s0` - internal control network) and `10.0.6.57` (`enp4s0` - campus network). The main services it hosts are an instance of the [EPICS archiver](/Machine/Groups/CON/control_archiver) accessible from [http://10.0.4.57](http://10.0.4.57){target=_blank} and another of the [alarm server](/Machine/Groups/CON/control_beast). Both of them run through Docker containers.

As we have only 2 disks being used, we didn't need to set any logical volume managers up. The mount points are configured as following:

```
$ sudo fdisk -l

Disk /dev/sdb: 1.1 TiB, 1200243695616 bytes, 2344225968 sectors

Device     Boot Start        End    Sectors  Size Id Type
/dev/sdb1        2048 2344224767 2344222720  1.1T 83 Linux


Disk /dev/sda: 447.1 GiB, 480103981056 bytes, 937703088 sectors

Device     Boot     Start       End   Sectors   Size Id Type
/dev/sda1  *         2048   2000895   1998848   976M 83 Linux
/dev/sda2         2002942 937701375 935698434 446.2G  5 Extended
/dev/sda5       928348160 937701375   9353216   4.5G 82 Linux swap / Solaris
/dev/sda6         2002944 928348159 926345216 441.7G 83 Linux
```

```
$ df

Filesystem      1K-blocks     Used  Available Use% Mounted on
/dev/sda6       455773544 13752032  418846500   4% /
/dev/sda1          967320   106712     794256  12% /boot
/dev/sdb1      1153588084 84183784 1010782348   8% /home
```

<br>

##  References 

<references />
