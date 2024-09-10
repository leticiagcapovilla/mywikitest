---
title: Sapucaia Experimental Routine
description: 
published: 1
date: 2024-09-09T20:24:13.614Z
tags: 
editor: markdown
dateCreated: 2024-09-04T15:56:07.754Z
---

# Início do tempo de feixe

## Escolha do setup da linha (1x por proposta) [staff]​

- Alinhamento de porta-amostra e fendas (varreduras de motores)​
- Alinhamento do beamstopper (varredura de motores)​

## Escolha de energia da linha (1x por proposta)  [staff]​

- Mudança nos motores do DCM (varredura de motores)​
- Realinhamento do porta-amostras e fendas, caso necessário (varredura de motores)​

## Escolha da distância amostra-detector (1x ou 2x por proposta) [usuário + staff presente]​

### Ajuste fino das configurações do experimento usando amostra padrão (AgBh)​

#### Coleta da imagem do padrão (auto) – não requer altas velocidades (usar escrita em PVs)​
- Posicionamento da amostra padrão na frente do feixe (movimentação xy do porta-amostra – slider e bioy)​
- Abertura do fast shutter​
- Início da aquisição pelo detector​
- Finalização da aquisição pelo detector​
- Fechamento do fast shutter​
- Retorno dos motores para o reposicionamento da amostra​
- Todas etapas podem ser feitas usando a escrita nas PVs dos elementos​

#### Utilização da imagem do padrão para calibração da distância [staff]​

- Uso de software de terceiros (pyFAI)​
- Obtenção das variáveis para reconstrução geométrica do detector​
- Estas etapas não incluem ​

### Preparação da máscara para integração dos dados [staff]​
- Combinação da informação de pixeis problemáticos com pixeis removidos exclusivamente para o experimento (beamstopper/sombras/espalhamentos indesejados)​
- Uso de software de terceiros (pyFAI)


# Início das medidas​

## Escolha dos parâmetros da medida [usuário]​

- Posição das amostras nas placas (setups 1, 2, 3, 4 e 7)​
- Volume de amostra para coleta (setups 1 e 3)​
- Nome das amostras (1x por medida) (todos)​
- Temperatura (setups 1, 3, 4 e 7)​
- Tempo de exposição (todos)​
- Quantidade de medições (todos)​
    - Período da coleta (todos)​

## Disparo da medida [usuário]​

- Medida do I0 (auto)​
    - Introdução do fotodiodo (antes da amostra) – Atuador pneumático– escrever em PV​
    - Abertura do Fast Shutter – escrever em PV​
    - Aquisição das contagens no fotodiodo​
        - Medida de 1 s, por exemplo: resolução temporal da medida e range dinâmico do fotodiodo precisam ser muito bons para que a subtração dos dados seja feita de forma aceitável. Idealmente 1 em 104 ou 105, pelo menos.​
    - Fechamento do Fast Shutter​
    - Remoção do fotodiodo​
- Inclusão da amostra na frente do feixe (dependente do setup)

# SETUP 1 - biocube​

## Posicionamento da amostra na frente do feixe – parte 1​

### Injeção da amostra (auto)​

- Robô #1 faz a coleta da amostra e injeta na célula (biocube) e fica on hold (movimentação via software xenocs) – t(20-40s)​
- Bomba de seringa posiciona a amostra no capilar (região vista pela câmera) até a amostra ficar na região onde será exposta (movimentação via software xenocs) – t(2-5s) (*1)​
    - Movimento passa a ser controlado pelo feedback da câmera (*2)​
- Coloca-se a temperatura do sistema na temperatura de medida (mudança via software xenocs) – t(0 – 2min)​

### Medidas de UV-Vis são realizadas para a amostra (auto) –  t<1s​

- (trigger através do software da xenocs)​
- Informações devem ser gravadas no HDF5 da amostra​

### Medidas de raios X (auto)​

- Amostra é posicionada numa região onde o feixe de raios X incide sobre ela. (*1, já estava)​
- É feito o cálculo da velocidade do líquido para a realização do experimento (para evitar o desperdício e aproveitar ao máximo o volume escolhido da amostra) – esta etapa não existe, mas precisaríamos que existisse. Precisamos de alguma sugestão.​
- Coloca-se a amostra em movimento (utilizando a bomba de seringa) (*2) – o comando para mover a bomba de seringa é enviado ​
- No momento que o software da câmera reconhece que o líquido iniciou a movimentação (pois pode haver um delay entre a movimentação da bomba de seringa e a efetiva movimentação do menisco), é disparado o processo de abertura do fast shutter (FS). ​
    - O tempo entre o início da movimentação do menisco e o disparo do processo de abertura do FS é de extrema importância, pois se houver um tempo muito grande, haverá um desperdício grande de amostra; por outro lado, se o líquido não iniciar seu movimento, o feixe pode queimar a amostra antes dela começar a movimentar com velocidade terminal. ​
    - De forma geral, a velocidade da bomba de seringa é de aproximadamente 10 ul/s; o tempo do EPICS para ativar este processo faria com que houvesse a perda de aproximadamente uns 2 ul. Considerando a mesma perda para o fim do menisco, seria um desperdício de 4 ul, o que não é um grande problema. Os valores de velocidade da bomba e do EPICS precisam ser atualizados para uma melhor estimativa; porém, para agora, acreditamos que se o tratamento de imagem for rápido (~ 0.1s), a perda de amostra seria pequena, e seria possível fazer o experimento com menos de 10 ul, de forma geral. ​

- É enviado um sinal para o fast shutter para a realização de sua abertura​
    - O fast shutter será chamado pelo TATU para que o mesmo abra. O tempo de delay de abertura é de aproximadamente 7 ms depois do sinal chegar ao FS.​
    - Há uma medida analógica de resistência que informa se o FS abriu totalmente ou não. O sinal de abertura (quando passa um valor de threshold) comandará o início de aquisição dos dados do detector


## Posicionamento da amostra na frente do feixe – parte 2​

- O fast shutter, quando aberto, envia um sinal para o TATU, e este para o detector, para o último iniciar a aquisição dos dados – sinal instantâneo do TATU​
    - Os dados são coletados respeitando o tempo de aquisição, quantidade de medições e período de coleta​
    - Dependendo do período de coleta e do tempo de aquisição, o FS pode ser fechado. ​
    - Idealmente, o experimento deveria ser interrompido caso fosse identificado que o menisco do fim da amostra chegou antes do previsto (formação de bolhas ou insuficiência de amostra) – necessário reconhecimento de imagem para este ponto.​
    - Dados da temperatura da amostra são salvos ​
- O detector faz a coleta dos dados e os salva no servidor. ​
- O detector para de fazer as coletas e envia sinal para fast shutter (via TATU)​
- O fast shutter é fechado (delay de aproximadamente 7ms depois do sinal chegar nele)​
- A amostra para de ser movimentada pela bomba de seringa – não precisa ser imediata a parada. ​
- A bomba de seringa para de ser controlada pelo feedback da câmera​

​
## Limpeza do porta-amostras (auto)​

- O robô conecta no biocube para fazer a limpeza​
- A válvula do posicionador é colocada no sistema de bypass​
- A amostra é descartada usando as bomba peristálticas do rack líquido​
- As bombas peristálticas empurram os líquidos para limpeza (água, sabão e álcool)​
- É aberto o circuito para a passagem de N2 para secagem​
- Teste de imagem para verificação da correta limpeza do capilar: (não necessita TATU, mas pode ser usado)​
    - O fast shutter é aberto​
    - O detector realiza uma medida com tempo determinado​
    - O fast shutter é fechado​
    - A imagem coletada é processada e comparada com a imagem do capilar no início do experimento​
        - Caso haja diferença entre as medidas, é rodado outro ciclo de limpeza e secagem​
        - Se mesmo assim houver diferença, é indicado um alerta para troca de posição do feixe no capilar e, caso não resolver, troca do capilar​

## Inicia-se um novo ciclo de experimento. 


# SETUP 2 - Placa​

## Posicionamento da amostra na frente do feixe​

### Posicionamento da amostra (auto)​

- Robô #2 faz a coleta da placa que contém a amostra escolhida e posiciona a amostra escolhida na frente do feixe​
        - Não tem bomba peristáltica, temperatura, lavagem, medida de UV-Vis, sem feedback nem nada. O experimento é acompanhado pela câmera da linha para inspeção visual. ​

### Medidas de raios X (auto)​

- É enviado um sinal para o fast shutter para a realização de sua abertura (não precisa do TATU, mas pode ser feito como no anterior)​
- O fast shutter, quando aberto, envia um sinal para o detector iniciar a aquisição dos dados​
        - Os dados são coletados respeitando o tempo de aquisição, quantidade de medições e período de coleta​
        - Dependendo do período de coleta e do tempo de aquisição, o fast shutter pode ser fechado. ​
- O detector faz a coleta dos dados e os salva no servidor. ​
- O detector para de fazer as coletas e envia sinal para fast shutter​
- O fast shutter é fechado ​

## Inicia-se um novo ciclo de experimento


# SETUP 3 – Capivara (ainda não pensado como será daqui para frente)​

## Posicionamento da amostra na frente do feixe – parte 1​

### Injeção da amostra (auto)​

- Robô #3 (Alias?) faz a coleta da amostra e injeta na célula (Capivara) usando uma bomba peristáltica​
- O injetor com seringa, que possui maior precisão, suga a amostra para o capilar (região vista pela câmera) até a amostra ficar próxima à região onde será exposta. ​
- O injetor com seringa passa a ser controlado pelo feedback da câmera​
- Coloca-se a temperatura do sistema na temperatura de medida​
- A temperatura da amostra é monitorada pela câmera térmica. ​

### Medidas de UV-Vis são realizadas para a amostra (auto) ​

### Medidas de raios X (auto)​

- É feito o cálculo da velocidade do líquido para a realização do experimento (para evitar o desperdício e aproveitar ao máximo o volume escolhido da amostra)​
- Coloca-se a amostra em movimento (utilizando a seringa motorizada)​
- No momento que o software reconhece que o líquido passa pela região de iluminação do feixe, é disparado o processo de abertura do fast shutter (processo idêntico ao da xenocs)​
- É enviado um sinal para o fast shutter para a realização de sua abertura (TATU)​
- O fast shutter, quando aberto, envia um sinal para o detector iniciar a aquisição dos dados​
    - Os dados são coletados respeitando o tempo de aquisição, quantidade de medições e período de coleta​
    - Dependendo do período de coleta e do tempo de aquisição, o fast shutter pode ser fechado. ​
    - O experimento é interrompido caso seja identificado que o menisco chegou antes do previsto (formação de bolhas ou insuficiência de amostra)​
    - Dados da temperatura da amostra também são salvos​
- O detector faz a coleta dos dados e os salva no servidor. ​
- O detector para de fazer as coletas e envia sinal para fast shutter​
- O fast shutter é fechado ​
- A amostra para de ser movimentada pelo injetor, e o injetor para de ser comandado pelo feedback da câmera

## Limpeza do porta-amostras (auto)​

- As válvulas são acionadas para a bomba peristáltica controlar o líquido​
- A amostra é descartada usando a bomba peristáltica​
- Uma válvula é acionada para usar os líquidos de limpeza (água e, depois, água com sabão)​
- Uma bomba peristáltica empurra os líquidos para limpeza (água e sabão), alternando uma outra válvula entre os líquidos​
- É aberto o circuito para a passagem de N2 para secagem (válvulas acionadas)​
- Teste de imagem para verificação da correta limpeza do capilar:​
    - O fast shutter é aberto​
    - O detector realiza uma medida com tempo determinado​
    - O fast shutter é fechado​
    - A imagem coletada é processada e comparada com a imagem do capilar no início do experimento​
        - Caso haja diferença entre as medidas, é rodado outro ciclo de limpeza e secagem​
        - Se mesmo assim houver diferença, é indicado um alerta para troca de posição do feixe no capilar e, caso não resolver, troca do capilar​

## Inicia-se um novo ciclo de experimento. 


# SETUP 7 – Multicapilar​

## Posicionamento da amostra na frente do feixe​

### Posicionamento da amostra (auto)​

- Robô #2 faz a coleta do Holder do multicapilar que contém a amostra escolhida e posiciona a amostra escolhida na frente do feixe​
- A temperatura do Holder é setada para a do experimento. ​
        - Não tem bomba peristáltica, lavagem, medida de UV-Vis, sem feedback nem nada, a não ser o termopar. O experimento é acompanhado pela câmera da linha para inspeção visual. ​

### Medidas de raios X (auto)​

- É enviado um sinal para o fast shutter para a realização de sua abertura (não precisa do TATU, mas pode ser feito como no anterior)​
- O fast shutter, quando aberto, envia um sinal para o detector iniciar a aquisição dos dados​
        - Os dados são coletados respeitando o tempo de aquisição, quantidade de medições e período de coleta​
        - Dependendo do período de coleta e do tempo de aquisição, o fast shutter pode ser fechado. ​
- O detector faz a coleta dos dados e os salva no servidor. ​
- O detector para de fazer as coletas e envia sinal para fast shutter​
- O fast shutter é fechado ​

## Inicia-se um novo ciclo de experimento