---
title: Logging system
description: 
published: 1
date: 2024-05-28T15:50:30.543Z
tags: 
editor: markdown
dateCreated: 2024-05-27T20:46:46.491Z
---

# CON: Control-olog

##  Introduction 

The [olog](http://olog.github.io/2.2.7-SNAPSHOT/){target=_blank}, developed in a collaboration between the [Brookhaven National Laboratory](https://www.bnl.gov/world/){target=_blank} and the [Facility for Rare Isotope Beams](https://frib.msu.edu/){target=_blank}, is a system which allows to keep track of machine operations and maintenances. Basically, it consists of two main components:

* [MySQL](https://www.mysql.com/){target=_blank} database, where logs, tags and logbooks are stored.
* Web service, deployed with a [Glassfish](https://javaee.github.io/glassfish/){target=_blank} instance.

The project's git repository can be accessed from this [link](https://github.com/Olog/){target=_blank}.

##  Installation 

This subsection is dedicated to the steps needed to the installation and configuration of the Olog logging service. 

###  Virtualization 

All components which compose the olog system were set up to be executed in a completely virtualized environment. All modules will be encapsuled and run inside Docker containers, exactly as it has been done for every other service provided by our group.

####  Structure 

Two Docker images were developed with the objective of wrapping the components described in the section '''Introduction'''. Such images can be found in the git repositories [docker-olog-server](https://github.com/gciotto/docker-olog-server){target=_blank} and [docker-olog-mysql-db](https://github.com/gciotto/docker-olog-mysql-db){target=_blank}. The network communication between the containers obtained from these images is granted by an internal and private network, provided by the Docker engine itself.

####  Docker images 

Some aspects can be pointed out regarding the Docker images discussed in the previous section:

* Auxiliary scripts for the image building and deployment of the containers are also provided in the directories of each project, however it's advised their use only in a development environment. For the production deployment of the application, use either Docker Compose or Docker Swarm, as explained next.  Image creation is achieved with the following command, replacing `<image>` by `server` or `db`, depending on, evidently, the respective image.

```
$ ./build-docker-olog-<image>.sh
```

* Docker image [docker-olog-server](https://github.com/gciotto/docker-olog-server){target=_blank} uses ''Glassfish'' version 4.1.1 and it's based on [openjdk:8-jdk](https://hub.docker.com/_/openjdk/){target=_blank}. When it's launched, the script `setup-olog.sh` is executed, applying all desired settings to the server, such as the ones corresponding to authentication and database connection, por example.

* Docker image [docker-olog-mysql-db](https://github.com/gciotto/docker-olog-mysql-db){target=_blank} encapsulates the database and its only peculiarity is to run some `sql` scripts during its initialization.

####  Deployment 

Scripts for two container deployment tools, Docker Compose and Docker Swarm, are available in [this repository](https://github.com/lnls-sirius/docker-olog-compose){target=_blank}.

#####  Docker Compose 

Deployment of the logging service is done from the [docker-compose](https://docs.docker.com/compose/){target=_blank} tool and the scripts provided in the  [docker-olog-compose](https://github.com/gciotto/docker-olog-compose){target=_blank} repository. The `docker-compose.yml` file contains the definition of the containers and other resources required to run the system. Therefore:

* `olog-server` container encapsulates both the server and the Glassfish servlet. `/glassfish4/glassfish/domains/domain1/config/jackrabbit/` volume should be persistent, since that the figures eventually attached to the logs will stored into this directory.
* `olog-mysql-db` container, in turn, contains the MySQL server instance which will store all data produced by the system. Directory `/var/lib/mysql`, where all tables are saved, should be mapped to a persistent volume in order to grant that no data be lost in the case of an eventual interruption of the container.
* An internal network, `olog-network`, was created with the objective of isolating the communication of the two containers above.

To enable the `systemd` service that launches the containers according to the file `docker-compose.yml`, execute in the folder where the repository was cloned

```
$ make install
```

and to disable

```
$ make uninstall
```

#####  Docker Swarm 

The implementation for this case is very similar with the solution provided for Docker Compose. Both use a file with extension `.yml`. A fundamental difference between them consists in the fact that [it is not possible to assign static addresses](https://github.com/moby/moby/issues/24170){target=_blank} to the services specified for a Swarm. Therefore, a container is identificated only by its hostname.

The use of this kind of solution must be associated with a distributed storage mechanism, such as the GlusterFS, since that the container execution will be distributed as well.

The deployment can be done by executing

```
$ docker stack deploy -c docker-swarm.yml olog-con
```

and its removal with

```
$ docker stack rm olog-con
```

The state of all services being executed by the swarm engine can be obtained with 

```
$ docker service ls
```

To list more details of a specific service, use the following command the service ''id'' given by the command above.

```
$ docker service ps <ID>
```

The logs of each service can be viewed with the command 

```
$ docker service logs <ID>
```

##  Integration with LNLS-studio 

The [LNLS-studio](/Machine/Groups/CON/lnls_studio) configuration is done from the window `Edit > Preferences > CSS Core > Logbook`. Edit the field `Olog Service URL` with the machine address where the olog server has been deployed and disable the option `use authentication`.

To test your new settings, restart LNLS-Studio and open the `LogViewerPerspective` through `Window > Open Perspective > Other... > LogViewerPerspective`. If everything is set up correctly, you should see a window like the one outlined below:

|![](/img/groups/con/loggin_system/Lnls-studio-olog.png)|
|-|
|**Figure 1**: LNLS Studio Olog|

##  Controls group's olog instance 

An instance of this server has been installed on Sirius control system servers and can be configured from its [web interface](http://10.0.6.57/olog/){target=_blank} (internal access only).
