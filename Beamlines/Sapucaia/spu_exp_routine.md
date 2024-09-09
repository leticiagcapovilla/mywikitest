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