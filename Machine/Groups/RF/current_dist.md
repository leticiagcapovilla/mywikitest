---
title: Current Distribution
description: 
published: 1
date: 2024-06-11T15:39:55.880Z
tags: 
editor: markdown
dateCreated: 2024-06-11T14:21:25.321Z
---

# RF: RF-CurrentDist

<br>

## Introduction

A placa de distribuição de correntes é utilizada para medir a corrente de alimentação de cada um dos módulos das torres amplificadoras em estado sólido do Sirius. 

O CI utilizado é o sensor hall ACS724-20AU, que retorna uma tensão de 0-5V, proporcional a corrente máxima de 20A. 

Essa placa é utilizada em conjunto com a [[RF:RF-SIMuxBoard|RF-SIMuxBoard]](link) e a [[RF:RF-SIMuxCBoard|RF-SIMuxCBoard]](link) no crate [[RF:RF-SSAMux|RF-SSAMux]](link)
.

A placa [[RF:RF-CurrentDistPre|RF-CurrentDistPre]] é uma versão de um único canal desta, utilizada exclusivamente para medir a corrente de alimentação dos pré amplificadores.

<br>

## General description

A placa de distribuição de corrente, em conjunto com a [[RF:RF-SIMuxBoard|RF-SIMuxBoard]](link) e a [[RF:RF-SIControlBoard|RF-SIMuxCBoard]](link), dentro do crate [[RF:RF-SSAMux|RF-SSAMux]](link), é responsável por medir e distribuir a corrente de alimentação dos módulos amplificadores em estado sólido do anel do Sirius.


|![](/img/groups/rf/current_dist/RF-CurrentDist_top_pic.jpg =200x)|
|-|
|**Figure 1**: Current Distribution Top view picture.|

Cada PCI é fixada no barramento de cobre interno da [[RF:RF-SSAMux|RF-SSAMux]](link) através dos furos M6 contidos na placa. Na <xr id="fig:RF-CurrentDist_bot_pic.jpg" /> é possível ver a seção onde não há máscara de solda - por ali é feito o contato elétrico entre a placa e o barramento de cobre.

A corrente é então distribuída em 8 ramos, onde cada um contém um sensor hall ACS724-20AU. Tanto o envio do sinal de saída quanto a alimentação dos sensores são feitos através do conector de 10 vias.

Após passar pelo ACS, a corrente é enviada para os módulos através dos conectores da Anderson Power vermelho e branco que podem ser vistos na <xr id="fig:RF-CurrentDist_top_pic.jpg" />. Os módulos amplificadores estão conectados a esta placa através de cabos PP 2 vias.

Cada módulo amplificador necessita de 2 pontos de alimentação de 48V, dessa forma, esta placa é projetada para monitorar 4 módulos.

<br>

### ACS724-20AU

O ACS724, mais especificamente o CI de part number ACS724LLCTR-20AU-T, é um sensor de efeito Hall fabricado pela Allegro MicroSystems. Esse componente suporta uma corrente unidirecional máxima de 20A e rejeita campos de modo comum através da sensitividade Hall diferencial. 

|![](/img/groups/rf/current_dist/RF-CurrentDist_bot_pic.jpg =200x)|
|-|
|**Figure 2**: Current Distribution Top view picture.|

O CI é alimentado com 5V e tem uma sensibilidade de 200mV/A e uma tensão de saída de (Vcc*0.1)V quando não há corrente. Assim, tensão de saída pode ser idealmente calculada da seguinte forma:

$$
V_{out} = 0.2 * I + 0.5
$$

Ainda de acordo com o Datasheet, o CI tem um erro total de saída de ±0.7%, erro de sensitividade ±0.7% e um offset de tensão de ±6mV.

<br>

### Anderson Power Connectors

A saída de corrente é feita utilizando conectores PP15/45 da Anderson Power, nas cores vermelha (P/N 1327FP) e branca (1327G7FP). Além disso, é utilizado o acessório de montagem azul (P/N 1399G8), que fornece uma melhor resistência mecânica, além do contato de cobre (P/N 1377G1) utilizado para ligar o conector a placa.

Esse conjunto fornece uma conexão compacta e de alta capacidade de corrente (até 55A por polo) para a alimentação dos módulos.

<br>

### Layers

Esta PCI é composta por 4 layers. 

As duas layers externas tem espessura de 4oz e são projetadas para suportar as altas correntes exigidas pelos módulos.

As duas layers internas tem espessura de 1oz e são responsáveis pelo plano de terra do circuito e também pela passagem dos sinais de nível TTL.

<br>

## Versions Control

{{Table:RF-CurrentDist_version_control}}

The schematic, bill of materials and all other files related to this crate can be found at: <br>
`\\centaurus\LNLS\Grupos\RF\Sirius DOC_TEC_RF\Sirius_DOC_TEC_RF\PCB Projects\Released Files\Sirius Current Aquisition\Current Aquisition Boards\Current_distribution_ACS724`

<br>

### Devices in use

**Table 1**: RF-CurrentDist version control. 

|Version| Date| Description |
|-|-|-
|V1I1| 	First manufacturing |
|V1I2| 01/2021| Changed comunication connector |

<br>

## Device PVs

**Table 2**: RF-CurrentDist devices

|Device Name| Device #| Board Version| Number of Boards| Location |
|-|-|-|-|-|
|RA-ToSIA01:RF-SSAMux| 001-004| V1I1| 8| Storage Ring A SSA Tower 1 |
|RA-ToSIA02:RF-SSAMux| 005-008| V1I1| 8| Storage Ring A SSA Tower 2 |
<br>

## Issues

<br>

### Measured current too high

**Descrição:** A corrente medida apresentada no alto nível é muito alta (50% maior que o máximo valor típico do módulo), porém a corrente real está dentro do valor esperado.

Não foi possível reproduzir este erro em bancada. Testes mostraram que não é uma falha na conexão do conector de 10 vias de saída.

**Possível solução:** Dado espessura da PCI, os terminais do conector de 10 vias não atravessam completamente a placa. Dessa forma, a soldagem pode não ter sido eficiente, fazendo com que a conexão de terra, principalmente, não dê contato corretamente. Reforçar essa solda parece resolver o problema. Nas próximas versões, será utilizado o conector de P/N 09185106322 da Harting, que tem as mesmas especificações e dimensões, mudando apenas o comprimento dos terminais de solda.
