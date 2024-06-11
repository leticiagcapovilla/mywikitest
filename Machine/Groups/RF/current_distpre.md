---
title: Current Distribution Pre Amplifier
description: 
published: 1
date: 2024-06-11T15:42:53.369Z
tags: 
editor: markdown
dateCreated: 2024-06-11T14:21:27.683Z
---

# RF: RF-CurrentDistPre

## Introduction

A placa de distribuição de correntes pré é utilizada para medir a corrente de alimentação de um dos módulo pré amplificador das torres amplificadoras em estado sólido do Sirius. 

O CI utilizado é o sensor hall ACS724-20AU, que retorna uma tensão de 0-5V, proporcional a corrente máxima de 20A. 

Essa placa é utilizada em conjunto com a [[RF:RF-SIMuxBoard|RF-SIMuxBoard]](link) e a [[RF:RF-SIMuxCBoard|RF-SIMuxCBoard]](link) no crate [[RF:RF-SSAMux|RF-SSAMux]](link)
.

A placa [[RF:RF-CurrentDist|RF-CurrentDist]](link) é uma versão de oito canais canal desta, utilizada para medir a corrente de alimentação de quatro módulos amplificadores.

## General description

A placa de distribuição de corrente, em conjunto com a [[RF:RF-SIMuxBoard|RF-SIMuxBoard]](link) e a [[RF:RF-SIControlBoard|RF-SIMuxCBoard]](link), dentro do crate [[RF:RF-SSAMux|RF-SSAMux]](link), é responsável por medir e distribuir a corrente de alimentação dos módulos amplificadores em estado sólido do anel do Sirius.


|![](/img/groups/rf/current_distpre/RF-CurrentDistPre_top_pic.jpg =150x)|
|-|
|**Figure 1**: Current Distribution Pre Top view picture.|

Cada PCI é fixada no barramento de cobre interno da [[RF:RF-SSAMux|RF-SSAMux]](link) através do furo M6 contido na placa. Na Figura 2 é possível ver a seção onde não há máscara de solda - por ali é feito o contato elétrico entre a placa e o barramento de cobre.

A corrente é então distribuída em 2 ramos, onde cada um contém um sensor hall ACS724-20AU. Tanto o envio do sinal de saída quanto a alimentação dos sensores são feitos através do conector de 6 vias.

Após passar pelo ACS, a corrente é enviada para o módulo através dos conectores da Anderson Power vermelho e branco que podem ser vistos na Figura 1. Os módulos amplificadores estão conectados a esta placa através de cabos PP 2 vias.

Cada módulo amplificador necessita de 2 pontos de alimentação de 48V, dessa forma, esta placa é projetada para monitorar apenas 1 módulos - mais especificamente, um módulo pré amplificador

### ACS724-20AU

O ACS724, mais especificamente o CI de part number ACS724LLCTR-20AU-T, é um sensor de efeito Hall fabricado pela Allegro MicroSystems. Esse componente suporta uma corrente unidirecional máxima de 20A e rejeita campos de modo comum através da sensitividade Hall diferencial. 


|![](/img/groups/rf/current_distpre/RF-CurrentDistPre_bot_pic.jpg =150x)|
|-|
|**Figure 2**: Current DistributionPre Bot view picture.|

O CI é alimentado com 5V e tem uma sensibilidade de 200mV/A e uma tensão de saída de (Vcc*0.1)V quando não há corrente. Assim, tensão de saída pode ser idealmente calculada da seguinte forma:

$$
V_{out} = 0.2 * I + 0.5
$$

Ainda de acordo com o Datasheet, o CI tem um erro total de saída de ±0.7%, erro de sensitividade ±0.7% e um offset de tensão de ±6mV.

### Anderson Power Connectors

A saída de corrente é feita utilizando conectores PP15/45 da Anderson Power, nas cores vermelha (P/N 1327FP) e branca (1327G7FP). Além disso, é utilizado o contato de cobre (P/N 1377G1) utilizado para ligar o conector a placa.

Esse conjunto fornece uma conexão compacta e de alta capacidade de corrente (até 55A por polo) para a alimentação dos módulos.

### Layers

Esta PCI é composta por 4 layers. 

As duas layers externas tem espessura de 4oz e são projetadas para suportar as altas correntes exigidas pelos módulos.

As duas layers internas tem espessura de 1oz e são responsáveis pelo plano de terra do circuito e também pela passagem dos sinais de nível TTL.

## Versions Control

**Table 1**: RF-CurrentDistPre version control. 

|Version| Date| Description |
|-|-|-|
|V1I1| 	First manufacturing |
|V1I2| 01/2021| Changed comunication connector |

The schematic, bill of materials and all other files related to this crate can be found at: <br>
`\\centaurus\LNLS\Grupos\RF\Sirius DOC_TEC_RF\Sirius_DOC_TEC_RF\PCB Projects\Released Files\Sirius Current Aquisition\Current Aquisition Boards\Current_distribution_ACS724_pre`

### Devices in use

**Table 2**: RF-CurrentDistPre devices. 

lalalalalalalala testeeeeee

|Device Name| Device #| Board Version| Number of Boards| Location |
|-|-|-|-|-|
|RA-ToSIA01:RF-SSAMux-1| 001| V1I1| 2| Storage Ring A SSA Tower 1 |
|RA-ToSIA01:RF-SSAMux-2| 002| V1I1| 1| Storage Ring A SSA Tower 1 |
|RA-ToSIA01:RF-SSAMux-3| 003| V1I1| 1| Storage Ring A SSA Tower 1 |
|RA-ToSIA01:RF-SSAMux-4| 004| V1I1| 1| Storage Ring A SSA Tower 1 |
|RA-ToSIA02:RF-SSAMux-1| 005| V1I1| 1| Storage Ring A SSA Tower 2 |
|RA-ToSIA02:RF-SSAMux-2| 006| V1I1| 1| Storage Ring A SSA Tower 2 |
|RA-ToSIA02:RF-SSAMux-3| 007| V1I1| 1| Storage Ring A SSA Tower 2 |
|RA-ToSIA02:RF-SSAMux-4| 008| V1I1| 2| Storage Ring A SSA Tower 2 |

## Device PVs

There is no PVs associated with this device.

## Issues

### Bad mechanical resistance

**Problema:** Como não há espaço para que os acessórios de montagem sejam fixados, o projeto original não contempla estes. Dessa forma, é difícil a conexão do conector, uma vez que este está fixo apenas pela haste de cobre soldada.

**Solução provisória:** O acessório de montagem foi utilizado em conjunto com uma abraçadeira plástica, como é possível ver nas figuras acima, melhorando consideravelmente a resistência mecânica.
