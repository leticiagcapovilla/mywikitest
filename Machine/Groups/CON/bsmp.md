---
title: bsmp
description: 
published: 1
date: 2024-05-20T21:21:40.224Z
tags: 
editor: markdown
dateCreated: 2024-05-20T21:00:22.711Z
---

# CON: Basic Small Messages Protocol (BSMP)

<br>

## Introduction


Basic Small Messages Protocol is a lightweight byte-oriented application layer protocol developed for low-level communication to devices designed internally at LNLS. It may be used over several physical links, like Ethernet or RS-485. Developed by the [[CON:CON|Controls Group]], it's used by [CON:PUC|PUC](link) and [CON:MBTemp|MBTemp](link).

<br>

## Clients and servers

BSMP protocol was designed to standardize the communication between a client (master) and a server (slave). It works under a request/reply manner. The client sends a message to the server, which sends back to the client the appropriate answer.

<br>

## Entities

BSMP communication is based on the manipulation of the following entities:

* Variable: stores from 1 to 128 bytes of data.
* Group of variables, which permits read or write all variables within the corresponding set of variables with a single command.
* Curve: stores large amounts of data (up to 4095 MB).
* Function: a specific procedure to be executed.

All BSMP entities are provided by a BSMP server, and clients can interact with them through a connection to the server.

## BSMP messages

Every message of BSMP protocol has the following format:

- **Header**
    | Command | Length (first byte) | Length (second byte) |

<br>

- **Payload**
    | First payload byte | Second payload byte | ... | Last payload byte |

When used in a RS-485 serial network, a byte will be added to the beginning of the message. This byte will contain the address of the destination device (protocol specification allows multicast and broadcast messages too). Messages addressed to more than one slave (multicast or broadcast messages) are not answered by any of them. If the message has only one receiver, it will always be answered.

At the end of the BSMP message, another byte may be added for message integrity checking purposes (a checksum byte).

The command byte specifies the desired operation (read or write a variable, read data from a curve or execute a function, for instance). The following two bytes together (big-endian byte order) specifies the size of the payload. All bytes following the header are named the payload of the message. It may contain data to be written to a variable or curve, for example.

<br>

## libbsmp

In order to ease the task of BSMP client/server programming, a C library (libbsmp) was developed. Its source code and documentation are available at [CNPEM Git repository](http://github.com/lnls-sirius/libbsmp){target=_blank}.

## More information

The complete specification of the BSMP protocol is available in two languages:
*[English](https://github.com/lnls-sirius/libbsmp/blob/master/doc/protocol_v2-30_en_US.pdf){target=_blank}
*[Portuguese](https://github.com/lnls-sirius/libbsmp/blob/master/doc/protocol_v2-30_pt_BR.pdf){target=_blank}

Currently we work on a revision of the protocol specification and the C library. This revision will not produce any significant changes. Its intent is mainly correct some typos at the protocol specification and fix some minor bugs at the library.
