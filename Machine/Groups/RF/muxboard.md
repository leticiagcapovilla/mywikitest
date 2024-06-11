# RF: RF-MuxBoard

## Introduction

A placa MUX do sistema de aquisição de correntes tem por principal objetivo multiplexar os sinais de tensão referentes as medidas de correntes dos módulos amplificadores das torres e os sinais de tensão referentes as medidas de potência intermediárias.

Cada placa MUX multiplexa os sinais de uma barra dissipadora (16 módulos amplificadores, 1 módulo pré amplificador e 4 sinais de potência), totalizando 38 sinais de tensão. Os dados são enviados para a respectiva placa de controle.

A versão utilizada no Booster (V1I1) está localizada nos crates [[RF:RF-BOMux|RF-BOMux]](link) e trabalha em conjunto com o crate [[RF:RF-BOMuxC|RF-BOMuxC]](link) e a placa [[RF:RF-RFDET|RF Detector Board]].

As versões utilizadas no anel (V2I1 e V3I1) estão localizadas nos crates [[RF:RF-SSAMux|RF-SSAMux]](link), e trabalham em conjunto com [[RF:RF-MuxCtrlBoard|RF-MuxCtrlBoard]](link) (V2I1)/[[RF:RF-BBMuxCtrlCape|RF:RF-BBMuxCtrlCape]](link) (V3I1), [[RF:RF-CurrentDist|RF-CurrentDist]](link), [[RF:RF-CurrentDistPre|RF-CurrentDistPre]](link) e [[RF:RF-RFDET|RF Detector Board]](link).

## General description

A placa MUX tem como objetivo receber as tensões enviadas pelas respectivas placas de medição de corrente e potência, e envia-las para a sua respectiva placa de controle.

Essa placa recebe da sua controladora 4 sinais (A0-A3) de endereçamento para selecionar qual dos 16 canais do multiplexador será lido e 3 sinais (E1-E3) para escolher qual multiplexador está ativo. 

### V1I1

A primeira versão fabricada é utilizada no crate [[RF:RF-BOMux|RF-BOMux]](link). 

|![](/img/groups/rf/mux_board/RF-MuxBoard_block_diagram.svg)|
|-|
|**Figure 1**: MUX Board block diagram.|

### V2I1

A primeira versão utilizada no anel foi, basicamente, uma cópia da V1I1, com os componentes rearranjados. Nenhuma das escolhas de design ou componentes foram mudadas. 

Apesar de funcional, essa versão se mostrou inconveniente para o novo design da torre por alguns pontos:

*  **Componentes PTH** - os componentes da primeira versão são todos PTH. Isso faz com que o custo de montagem seja elevado além da área necessária para a PCI seja maior;
* **Tamanho** - como citado no item anterior, a área dessa versão é muito maior do que precisaria ser. Isso causou problemas na montagem do crate, fazendo com que fosse necessário um segundo "andar" dentro da [[RF:RF-SSAMux|RF-SSAMux]](link);
* **Dado de saída** - a V1I1 utiliza um cabo SMA para transportar o dado de saída até a controladora. Essa solução faz sentido nesse projeto, onde o sinal precisa percorrer um longo caminho até a placa controladora. Porém, neste, essa abordagem não é necessária, uma vez que a placa multiplexadora e de controle estão no mesmo crate;

### V3I1

Esta versão manteve o mesmo princípio de funcionamento da anterior, porém visando, principalmente, solucionar os problemas listados acima.

* **Componentes SMD** - todos os componentes eletrônicos agora são SMD. Isso fez com que a área da PCI diminuísse consideravelmente, não sendo mais necessário um segundo andar no crate;
* **Melhoria dos componentes** - apesar de todos os componentes utilizados na versão V2I1 terem suas versões em SMD, foram feitas alterações para melhorar o projeto e ser compatível com a [[RF:RF-BBMuxCtrlCape|RF-BBMuxCtrlCape]](link);
* **Alimentação** - foi adicionado um conversor DCDC DCP010512DBP-U. Agora, não é mais necessário fornecer +12V e -12V como na versão V2I1, basta uma fonte de +5V para que a PCI funcione;
* **Dado de saída** - Saída agora é enviada pelo mesmo flat cable onde chegam os dados de controle.

#### CD74HC4067SM96

O CD74HC4067SM96 é um mux/demux de 16 canais de alta velocidade que utiliza lógica CMOS. Este CI é alimentado com +5V e, nessa placa, é utilizado como 16 entradas e 1 saída.

Para selecionar qual saída será lida, são utilizados os pinos S0-S4, selecionando um dos 16 canais. Além disso, para essa seleção funcionar, é necessário que o pino E' esteja em nível lógico 0.

#### SN7407DR

A placa de controle [[RF:RF-BBMuxCtrlCape|RF-BBMuxCtrlCape]](link) envia sinais em nível LTTL (0-3.3V). Porém, o multiplexador CD74HC4067SM96 é endereçado com nível TTL (0-5V). Para que essa conversão de nível lógico seja feita, foi utilizado o buffer não inversor SN7407DR.

O SN7407DR é um buffer coletor aberto não inversor de 6 elementos, 1 bit por elemento.  O VIH deste CI é baixo o suficiente (2V) para que o sinal de nível alto enviado pela controladora (3.3V) seja suficiente para que a saída do buffer seja 5V.

## Versions Control

{{Table:RF-MuxBoard_version_control}}

The schematic, bill of materials and all other files related to this crate can be found at: <br>
''\\centaurus\LNLS\Grupos\RF\Sirius DOC_TEC_RF\Sirius_DOC_TEC_RF\PCB Projects\Released Files\Sirius Current Aquisition\Mux Boards\Multiplexing Board''

### Devices in use

**Table 1**: RF-MuxBoard version control. 

|Version| Date| Description |
|-|-|-|
|V1I1| 	First manufacturing |
|V2I1| 2018| Redesigned to new Sirius SSAmpTower project |
|V3I1| 01/2021| Redesigned to SMD components  |

## Device PVs

**Table 2**: RF-MuxBoard devices.

|Device Name| Device #| Board Version| Number of Boards| Location |
|-|-|-|-|-|
|RA-ToBO:RF-BOMux| 001-006| V1I1| 1| Booster SSA Tower |
|RA-ToSIA01:RF-SSAMux| 001-004| V2I1| 2| Storage Ring A SSA Tower 1 |
|RA-ToSIA02:RF-SSAMux| 005-008| V2I1| 2| Storage Ring A SSA Tower 2 |

## Issues
