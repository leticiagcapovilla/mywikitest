---
title: EPICS clients on Java with JCA - Java Channel Access
description: 
published: 1
date: 2024-06-06T16:57:47.631Z
tags: 
editor: markdown
dateCreated: 2024-06-06T16:54:59.253Z
---

# CON: EPICS on Java

## Introduction

This document discusses how to use the Java Channel Access (JCA) library to integrate a JAVA project with the EPICS server.

The article will contain:

- Installation of EPICS Base
- JAVA and JCA Installation
- JCA Library
- JCA Monitor
- JCA Get
- JCA Write

## Installation of EPICS Base

The [EPICS official web site](http://www.aps.anl.gov/epics/base/){target=_blank} presents a good description of what is EPICS Base:

*"This is the main core of EPICS, comprising the build system and tools, common and OS-interface libraries, Channel Access client and server libraries, static and run-time database access routines, the database processing code, and standard record, device and driver support."*

Currently we work only with the 3.15 series of EPICS Base releases (stable releases of EPICS V3). Latest offer from this branch is R3.15.5. To install EPICS Base in */opt*, just execute the commands below:

```
# apt-get -y install libreadline-gplv2-dev
# cd /opt
# wget https://epics.anl.gov/download/base/base-3.15.5.tar.gz
# tar -xvzf base-3.15.5.tar.gz
# rm base-3.15.5.tar.gz
# cd base-3.15.5
# make
```

It's convenient to add EPICS binaries directory to the system path and set other two environment variables. Edit the file */root/.bashrc*, adding at the end of the file:

```
export PATH=/opt/base-3.15.5/bin/linux-x86_64:$PATH
export EPICS_BASE=/opt/base-3.15.5
export EPICS_HOST_ARCH=linux-x86_64
export EPICS_CA_MAX_ARRAY_BYTES=1048576
export EPICS_CA_ADDR_LIST=10.0.4.57
```

To apply these settings to the current session, enter:

# source /root/.bashrc

Setting environment variables with information about EPICS Base is required for all users that will work on this platform. So the steps above should be repeated with the *.bashrc* file on each of these users home directories.

10.0.4.57 is the IP address of the computer at UVX control room that runs [EPICS PV Gateway](http://www.aps.anl.gov/epics/extensions/gateway/index.php){target=_blank} to provide (read) access to accelerator process variables. These variables are published only in a separate, application-specific computer network (UVX control system newtork). We use the PV Gateway to access accelerator control system PVs while working on office.

## Installation of JAVA and JCA

Java is a widely used programming language and has many free IDEs for creating projects and programming environments.

A very popular IDE is Eclipse, to download Eclipse click the [Link](http://www.eclipse.org/downloads/eclipse-packages/){target=_blank} and choose a version 7.0 or higher.

To use Java JCA, it is necessary to have a version 1.4.2 or higher of Java J2SE installed and with the Path configured from the IDE for it.

Another requirement is to have Meaven 2.x installed. Your download can be made in this [Link](https://maven.apache.org/){target=_blank}.

To download the JCA simply go to [GitHub](https://github.com/epics-base/jca){target=_blank} and perform the following steps.

```
$  git clone https://github.com/epics-base/jca.git
$  cd jca
$  mvn install
```

Once installed, add the jca-2.4.2-SNAPSHOT.jar library to your project to perform the following procedures.

## JCA Library

Initializes JCA

```
>> JCALibrary jca=JCALibrary.getInstance();
```

There is only one instance
Used to create contexts and manage JCA configuration info

Properties:

-  JNI_THREAD_SAFE preemptive
-  Suggested for Java, which is inherently threaded
-  JNI_SINGLE_THREADED non-preemptive

Methods of Properties:

-  createContext
-  getProperty
-  listProperties
-  getVersion, getRevision, getModification

Context Corresponds to a Channel Access context created by JCALibrary.createContext:

-  createContext(JCALibrary.JNI_SINGLE_THREADED)
-  createContext(JCALibrary.JNI_THREAD_SAFE)

Controls all IO you can have more than one context

Methods of Context:

-  createChannel
-  flushIO, pendIO, pendEvent, poll
-  attachCurrentThread
-  addContextExceptionListener, removeContextExceptionListener
-  addContextMessageListener, removeContextMessageListener
-  destroy

To created a Channel created by Context.createChannel:

-  createChannet(String name, connectionListener 1)

Properties of Channel:

-  CLOSED           - CONNECTED
-  DISCONNECTED     - NEVER_CONNECTED

Methods of Channel:

-  get, many overloads
-  put, many overloads
-  getName, getConnectionState, getElementCount, etc.
-  addMonitor
-  addConnectionListener, removeConnectionListener
-  addAccessRightsListener, removeAccessRightsListener
-  destroy

Remember that to perform the following procedures it is necessary to create a connection with the EPICS server, establish a communication channel and created a Server Context.

## JCA Monitor

To perform the EPICS PV readings, it is necessary to have a monitor object or a get.

Monitors are objects that scan with the scan speed synchronized to the EPICS filer.

You can use Monitor Objects in building frames for supervisors and configuring alarm systems.

To created a Monitor Object:

With addMonitor:

-  addMonitor(DBRType type, int count, int mask, MonitorListener l)

Methods of addMonitor:

-  addMonitorListener, removeMonitorListener
-  getMonitorListener, getMonitorListeners
-  clear
-  getChannel, getContext
-  getCount, getMask, getType
-  isMonitoringAlarm, isMonitoringLog, isMonitoringValue

The following is an example of implementing a JCAMonitor object: 

```   
// Instance of SimpleJCAMonitor
private class SJCAMonitorListener implements
MonitorListener {
public void monitorChanged(MonitorEvent ev) {
onValueChanged(ev);
}
};
SimpleJCAMonitor sjcam=new SimpleJCAMonitor();
jca=JCALibrary.getInstance();
ctxt=jca.createContext(JCALibrary.JNI_THREAD_SAFE);
chan=ctxt.createChannel(sjcam.name,sjcam.new SJCAConnectionListener());
ctxt.flushIO();

private void onConnectionChanged(ConnectionEvent ev) {
Channel ch=(Channel)ev.getSource();
Context ctxt=ch.getContext();
// Start a monitor on the first connection
if(connectionCounter ##  0 &&
ch.getConnectionState() ##  Channel.CONNECTED) {
try {
// Add a monitor listener and flush
ch.addMonitor(DBRType.STRING,1,
Monitor.VALUE|Monitor.LOG|Monitor.ALARM,
new SJCAMonitorListener());
ctxt.flushIO();
} catch(Exception ex) {
ex.printStackTrace();
}
}

private void onValueChanged(MonitorEvent ev) {
Channel ch=(Channel)ev.getSource();
Context ctxt=ch.getContext();
// Get the value from the DBR
try {
DBR dbr=ev.getDBR();
String [] value=((STRING)dbr).getStringValue();
System.out.print(SJCAUtils.timeStamp() + " " +
getName() + ": “ + value[0]);
} catch(Exception ex) {
...
}
}
```

## JCA Get

JCA get are objects that perform the current PV read only when given a get command. That is, it performs the reading once, different from the Monitor that reads according to what the EPICS Binder receives and performs.

As well as the Monitor it can also be used for creating supervisory frames and alarm system configuration.

To create a JCAGet object, perform the following steps:

Get the value:

-  String [] value;
-  value = ((STRING)chan.get(DBRType.STRING, 1)).getStringValue ();

Wait for the get:

-  ctxt.pendIO(simpleJCAGet.timeout);

Print the value:

-  System.out.println("The value of" + simpleJCAGet.name + "is" + value [0]);

## JCA Write

To write a PV on the server it is necessary to follow certain basic procedures like informing the type of PV, unit, decimal places, timestamp among others.

The following code shows how to configure certain parameters needed for PV configuration:

```
super("Name of PV", "eventCallback")
public String getUnits() {
return "UNIT";
}
public short getPrecision() {
return "NUMBER OF PRECISION";
}
protected CAStatus readValue(DBR value, ProcessVariableReadCallback arg1) throws CAException {
DBR_TIME_Float timeDBR = (DBR_TIME_Float) value;
// set status and time
timeDBR.setTimeStamp(getTimestamp());
timeDBR.setStatus(Status.NO_ALARM);
timeDBR.setSeverity(Severity.NO_ALARM);
// set scalar value
timeDBR.getFloatValue()[0] = getRadiation();
// return read completion status
return CAStatus.NORMAL;
}
protected CAStatus writeValue(DBR arg0, ProcessVariableWriteCallback arg1) throws CAException {
if (interest) {
// create and fill-in DBR
DBR monitorDBR = AbstractCASResponseHandler.createDBRforReading(this);
((DBR_Float) monitorDBR).getFloatValue()[0] = "YOUR VALUE OF PV";
fillInDBR(monitorDBR);
((TIME) monitorDBR).setTimeStamp(getTimestamp());
((TIME) monitorDBR).setStatus(Status.NO_ALARM);
((TIME) monitorDBR).setSeverity(Severity.NO_ALARM);
this.getEventCallback().postEvent(Monitor.VALUE | Monitor.LOG, monitorDBR);
return CAStatus.NORMAL;
}
return CAStatus.NOSUPPORT;
}
public DBRType getType() {
return DBRType.FLOAT;
}
public synchronized TimeStamp getTimestamp() {
return timestamp;
}
```

It is not necessary to perform an alarm configuration to write an EPICS PV.

After setting up the PV it is necessary to perform the context with the EPICS server.

The following example is how to create a context and send PV to Archiver EPICS.

```
public static void main(String[] args) {
// Get the JCALibrary instance.
JCALibrary jca = JCALibrary.getInstance();
// Create server implementation
DefaultServerImpl server = new DefaultServerImpl();
// Create a context with default configuration values.
try {
ServerContext context = jca.createServerContext(JCALibrary.CHANNEL_ACCESS_SERVER_JAVA, server);
System.out.println(context.getVersion().getVersionString());
context.printInfo();
System.out.println();
server.registerProcessVaribale(YOUR PV);
server.registerProcessVaribale(ANOTHER PV);	
context.run(0); }}
```

With every procedure performed your variable will be online.
