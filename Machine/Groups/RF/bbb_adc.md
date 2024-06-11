# RF: RF-BBADCape

## Introduction

A BBADCape é uma placa no formato cape para a Beagle Bone utilizada para medir sinais analógicos em diversos hardwares nos sistemas RF. Até 4 placas podem ser utilizadas em conjunto.

A comunicação com a BBB é feita através de um protocolo SPI, e tem uma precisão de 12 bits.

É possível adequar o valor dos resistores de entrada (R*, R** e R***) da placa, para adequar a tensão de entrada à tensão suportada pelo ADC.

Os scripts para aquisição dos dados podem ser encontrados no [github](https://github.com/lnls-sirius/cas-rf-poe-adc/tree/master/poeAdcSPI){target=_blank}

## General description

A Capa Analogico-Digital foi criada para ser um item que pudesse ser facilmente utilizada em qualquer hardware que contenha uma BeagleBone. Ela conta com 4 entradas que podem ser condicionadas utilizando os divisores resistivos ou utilizando os amplificadores operacionais.

No máximo quatro placas podem ser empilhadas ao mesmo tempo, sendo necessário apenas modificar o número no switch rotatório.

A primeira versão (V3I2) não admite sinais negativos de tensão na entrada, enquanto a versão V3I3 pode ser adequada para medir esse tipo de sinal. Maiores detalhes serão explicados abaixo. 

|![](/img/groups/rf/bbb_adc/RF-BBADCape_block_diagram.svg =600x)|
|-|
|**Figure 1**: BBB ADC Cape block diagram.|


### AD7923

O ADC utilizado é o AD7923. Este CI, fabricado pela Analog Devices, dispõe de 4 canais de 12 bits, 200 kSPS, que se comunica através de protocolo SPI.

Este CI tem a capacidade de medir tensões até 2*Vref, onde Vref é uma tensão de referência externa, que, neste caso, tem valor de 2.5V e é fornecida pelo AD1582.

Para a comunicação SPI, os sinais CS', MOSI, MISO e SCLK estão, respectivamente, nos pinos 17, 18, 21 e 22 do conector P9 da BBB. 

### DCP010512DBP

O CI DCP010512DBP-U é um conversor DCDC que fornece ±12V para o circuito a partir da tensão de 5V que alimenta a Beagle Bone Black.

|![](/img/groups/rf/bbb_adc/RF-BBADCape_V3I2_resistors.svg =600x)|
|-|
|**Figure 2**: V3I2 Resistor bridge.|

### Resistive Divider

O AD7923 admite em sua entrada tensões de 0-5V. Para que esse circuito possa ser usado em qualquer hardware, há um divisor resistivo em cada uma das 4 entradas para condicionar as tensões que chegam ao ADC.

#### V3I2

Na primeira versão fabricada, o divisor resistivo é o mostrado na figura 2. A tensão de saída pode ser encontrada através da equação:

$$
V_{ADC} = \frac{R_2}{R_1+R_2}*V_{in}
$$

Este circuito é útil para a função proposta, porém é limitado em um aspecto: A tensão de entrada deve ser positiva para que a saída esteja entre 0-5V. Para aumentar a versatilidade dessa placa, o divisor resistivo de entrada foi modificado para o abaixo.


|![](/img/groups/rf/bbb_adc/RF-BBADCape_V3I3_resistors.svg =600x)|
|-|
|**Figure 3**: V3I3 Resistor bridge.|


#### V3I3

Na segunda versão, o divisor resistivo é o mostrado na figura 3. A tensão de saída pode ser encontrada através da equação:

$$
V_{ADC} = \frac{R_3*(R_1*V_{in} + R_2*V_{cc})}{R_1*R_2 + R_1*R_3 + R_2*R_3}
$$

Onde, nesse circuito, Vcc = 12V. 

Essa solução pode ser reduzida à anterior deixando o resistor R* (R1) em aberto, e também pode ser utilizada para a medição de entradas negativas, escolhendo corretamente os resistores.

Por exemplo, podemos medir um sinal que varia entre -12V e 0V utilizando R1 = 900Ω, R2 = 1kΩ e R3 = 1.8kΩ

[Este link](https://gitlab.cnpem.br/david.daminelli/resistors_calc){target=_blank} do gitlab contém a demonstração matemática e também scripts para auxiliar a calcular os resistores.

## Versions Control

**Table 1**: RF-ADCape version control. 

|Version| Date| Description |
|-|-|-|
|V3I2| 	First manufacturing |
|V3I3| 	Added new resistor on input, input capacitor is now optional, added activation circuit. |

The schematic, bill of materials and all other files related to this crate can be found at: <br>
`\\centaurus\LNLS\Grupos\RF\Sirius DOC_TEC_RF\Sirius_DOC_TEC_RF\PCB Projects\Released Files\BBB ADC Cape`

### Devices in use

List of where this board is being used.

**Table 2**: RF-ADCap devices. 

|Device Name| Device #| Board Version| Number of Boards| Location |
|-|-|-|-|-|
|RA-RaSIA01:RF-CalSys| 002| V3I2| 4| Storage Ring A LLRF Rack |
|RA-RaBO01:RF-LLRFLinPS| 001| V3I2| 2| Booster LLRF Rack |
|RA-RaSIA01:RF-LLRFLinPS| 002| V3I2| 2| Storage Ring A LLRF Rack |
|RA-RaBO01:RF-LLRFSwPS| 001| V3I2| 2| Booster LLRF Rack |
|RA-RaSIA01:RF-LLRFSwPS| 002| V3I2| 2| Storage Ring A LLRF Rack |
|RA-RaSIA01:RF-CavPlDrivers| 002| V3I2| 3| Storage Ring A LLRF Rack |
|RA-RaBO02:RF-SSASwPS| 001| V3I2| 2| Booster Interlock Rack |
|RA-RaSIA02:RF-SSASwPS| 002| V3I2| 2| Storage Ring A Interlock Rack |

## Device PVs

There is no PVs associated with this device.

## Issues

### BBB doesn't initiate (solved)

**Descrição**: Quando mais de uma placa está empilhada, a BBB não inicia.

**Solução temporária**: Dessoldando alguns capacitores, a BBB passa a iniciar corretamente. 

**Solução final**: Na versão V3I3 foi adicionado um circuito de ativação que faz com que a BBADCape só inicie após a BBB iniciar por completo.
