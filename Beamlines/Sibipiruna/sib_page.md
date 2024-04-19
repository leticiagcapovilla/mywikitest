---
title: SIBIPIRUNA
description: Soft X-rays tomography beamline at Orion
published: 1
date: 2024-04-19T17:41:39.011Z
tags: teste
editor: markdown
dateCreated: 2024-04-08T20:19:17.974Z
---

# Introdução

![](/home/Beamlines/1.png)

Figura 1: Missão e Capacidades da linha de luz SIBIPIRUNA

No contexto do Orion, alguns objetivos científicos foram criados, sendo um deles o de gerar imagens 3D com resolução nanométrica de células ex-vivo infectadas com agentes de nível 4 de biossegurança (BSL4) em estado quase nativo. Para isso a linha de luz SIBIPIRUNA foi criada, possuindo como capacidade fundamental a utilização de raios-X moles (*soft X-rays*) para gerar tomografia 3D de células isoladas. Esta capacidade necessariamente demanda que a célula esteja em estado criogênico, assim possibilitando que a célula tanto mantenha sua geometria quanto resista às doses de radiação dos raios-X ao longo das medidas. Além disso, com o intuito de ampliar as capacidades científicas do instrumento com um maior volume de informações das características da célula, concluiu-se ser necessário complementar as imagens de raios-X com uma técnica de imagem correlativa, criando-se assim uma plataforma de microscopia fluorescente de luz visível e tomografia de raios-X (CLXT do inglês *correlative light and X-ray tomography*). Dessa forma, a técnica de microscopia fluorescente também poderá ser empregada nas amostras estudadas na SIBIPIRUNA. A [Figura 1](#fig-1) traz uma síntese do processo de análise e decisão do objetivo científico, onde é apresentado um diagrama de Missão e Capacidades, sendo que letra ’M’ define a Missão, que nesse caso representa o objetivo científico proposto, e ‘C’ as Capacidades a serem desempenhadas para que o objetivo da Missão seja alcançado. Além disso, a figura ainda apresenta uma estrutura hierárquica onde as Capacidades são derivadas, a partir da representação das letras ‘i’ e ‘e’ sobre as setas, que representam inclusão e extensão, respectivamente.

![](/home/Beamlines/2.png)

Figura 2: Diagrama de arquitetura do Porta-Amostras Criogênico, especificando os componentes, subcomponentes, funções e informações/matéria/energia trocada entre as funções

Para o desenvolvimento da Capacidade 1.2, foi identificada a necessidade de um componente chamado de *Manipulador* para posicionar a amostra, montada a um *Suporte de Amostra*, no foco da linha de luz e realizar o movimento de tomografia. Ainda, devido ao fato de a amostra estar em estado criogênico, a solução também demandará um *Sistema de Refrigeração* para gestão térmica com a função de manter a amostra em temperatura criogênica. A partir disso, optou-se por desenvolver um Sistema de Porta-Amostras Criogênico (PACRIO), que deverá possuir as funções descritas conforme Figura 2.

Este documento irá abordar o status de desenvolvimento do componente PACRIO, bem como da Capacidade 1.1, visto que essa capacidade em associação com a 1.2 possibilita a Capacidade 1.1.1. Logo as operações de 1.1 e 1.2 deverão ser compatíveis entre si para que a 1.1.1 seja atingida. Estudos de viabilidade técnica dos métodos tradicionais para um *Sistema de Preparo de Amostras* com congelamento também serão apresentados neste documento, assim como um *Sistema de Transferência de Amostras*, uma vez que são pré-requisitos para a solução de porta-amostra (Figura 3).

Figura 3: Diagrama de arquitetura e capacidade principal da linha de luz SIBIPIRUNA

## Orçamento

As aquisições desse projeto vêm ocorrendo através do centro de custo referente ao PACRIO, com um montante total previsto de R$4.500.000,00. Na Tabela 1 são detalhados os montantes destinados às aquisições para cada um dos subsistemas e a data prevista para compra.

Tabela 1: Orçamento para o SoI

|     | Subsistema | Total Área | Fase A | Fase B | Fase C | Previsão de compra Fase A |
| --- | --- | --- | --- | --- | --- | --- |
| PACRIO | TXM Imaging | R$1.505.000,00 | R$559.500,00 | R$644.500,00 | R$301.000,00 | 01/03/2024 |
| Sample transfer | R$800.000,00 | R$240.000,00 | R$400.000,00 | R$160.000,00 |     |     |
| Correlative Imaging | R$885.000,00 | R$419.500,00 | R$288.500,00 | R$177.000,00 |     |     |
| Sample preparation | R$1.310.000,00 | R$393.000,00 | R$655.000,00 | R$262.000,00 |     |     |

## Estágios do ciclo de vida

A Tabela 2 apresenta os estágios do ciclo de vida do PACRIO em uma escala temporal de trimestres. Nos capítulos posteriores serão descritas as atividades específicas para cada um desses estágios.

Tabela 2: Estágios do ciclo de vida do PACRIO

|     | Conceitual | Desenvolvimento | Produção | Utilização | Suporte | Desfazimento |
| --- | --- | --- | --- | --- | --- | --- |
| 10/23 - 12/23 | X   |     |     |     |     |     |
| 01/24 - 03/24 | X   |     |     |     |     |     |
| 04/24 - 06/24 | X   | X   |     |     |     |     |
| 07/24 - 09/24 | X   | X   |     |     |     |     |
| 10/24 - 12/24 |     | X   |     |     |     |     |
| 01/25 - 03/25 |     | X   | X   |     |     |     |
| 04/24 - 06/25 |     | X   | X   |     |     |     |
| 07/25 - 09/25 |     |     |     | X   | X   |     |
| 10/25 - 12/25 |     |     |     | X   | X   |     |
| 01/26 - 03/26 |     |     |     |     |     | X   |

### Conceitual

A etapa conceitual consiste em estudos de avaliação das soluções, observando o entendimento do problema, requisitos e performance. Esta etapa se encerra a partir da aprovação de uma das soluções propostas, na qual será avaliado o conceito proposto para cinemática, dinâmica, gerenciamento térmico, minimização da exposição a área de descontaminação e viabilidade de manutenção.

Na etapa conceitual, representada pelo CDR da estação experimental, foram identificados os requisitos de baixo nível para o sistema de movimentação. Estes requisitos abrangem capacidades essenciais que o sistema deve possuir para alcançar os objetivos finais do projeto. É importante ressaltar que a análise de viabilidade desses conceitos, assim como a validação de sua capacidade em atender totalmente aos requisitos mapeados, representa um passo subsequente. Esse processo envolverá a atuação das equipes de engenharia na modelagem e prototipagem. Assim, embora os conceitos aqui apresentados ainda não tenham passado por uma validação final, eles demonstram potencial para atender aos requisitos em uma avaliação preliminar. A lista de requisitos (LLR, de *low-level requirement*) pertinentes ao projeto do estágio do porta-amostras criogênico é apresentada abaixo.

-   LLR-4.1: A temperatura da amostra preservada não deverá exceder 110K em todo o fluxo de trabalho.
-   LLR-4.6: Um manipulador de amostras criogênicas com quatro graus de liberdade deverá ser incluído na Estação SIBIPIRUNA.
-   LLR-4.7: Um cryocooler de circuito fechado deverá ser usado para o sistema de transferência de amostra.
-   LLR-4.8: O suporte de amostra deverá ser compatível com grades TEM (*Transmission Electron Microscopy*) de 3,5 mm.
-   LLR-4.9: O suporte de amostra deverá ser compatível com substratos de membrana de nitreto de silício.
-   LLR-4.10: O suporte de amostra deverá ser compatível com capilares de vidro.
-   LLR-5.12: O Estágio de Amostra deverá fornecer capacidades de posicionamento total de todo o substrato de amostra para eficiência de área de imagem otimizada.
-   LLR-5.13: Para o uso de grades TEM, o estágio deverá permitir um deslocamento cartesiano mínimo de ±1,5 mm em todas as direções XYZ.
-   LLR-5.14: O sistema de Estágio de Amostra deverá realizar um alinhamento rotacional preciso em torno de pelo menos um eixo que intersecta a região de imagem alvo.
-   LLR-5.15: O estágio de rotação deverá permitir pelo menos 180° de rotação, com a opção de 360° para correção da orientação da amostra.

A partir das definições básicas dos requisitos para o estágio do Manipulador de Amostras da SIBIPIRUNA, pode-se desenvolver um design conceitual. Prezando por diretrizes de isolamento da região da amostra em relação ao restante da linha de luz por questões de biossegurança, impondo simplificações nas interfaces mecânicas, e possibilitando o uso de tecnologias já validadas no Sirius/LNLS, o design atual aplica os conceitos de um *Tripod*, que utiliza cinemática paralela para movimentação cartesiana. Acoplado a ele, um estágio rotativo pode ser utilizado para o eixo de tomografia (Figura 4).

![](4.png)

Figura 4: Manipulador da amostra e Sistema Gerenciamento Térmico. A) vista isométrica da parte interna (exposta às amostras e ciclos de descontaminação mais frequentes), e B) vista isométrica da parte externa (em ambiente de vácuo separado da amostra)

Conceitos de atuadores foram explorados para o estágio em questão. O nano-posicionador NSAU, da JPE, surgiu como um candidato promissor, devido ao seu curso de movimentação e força necessários, além de um design completamente hermético, selado em um encapsulamento metálico e equipado com um sistema de feedback de posicionamento (encoder) integrado. No design atual, é viável isolar totalmente os componentes eletrônicos de precisão e os sistemas de movimentação dos atuadores do ambiente de amostra, minimizando a exposição desses componentes a agentes de descontaminação que podem causar corrosão e desgaste.

Embora o sistema NSAU possua encoders internos, muitas vezes é preferível medir a posição o mais próximo possível da região de interesse. Assim, o conceito atual incorpora um sistema de interferometria para a metrologia na posição imediatamente antes da amostra, permitindo que os elementos interferométricos sejam posicionados fora do ambiente de amostra e transmitindo o sinal através de três janelas ópticas. A viabilidade deste conceito será explorada, com foco na validação dos cursos de movimentação e na aplicabilidade dos interferômetros em um sistema com um grande desvio angular natural.

Uma outra característica distintiva do design atual é a utilização de um acoplamento flexível para a transferência de calor por condução, conectando um criostato à região de interesse do estágio. Isso possibilita que o sistema de refrigeração, a saber, um criostato do tipo pulse tube (PT) ou Joule-Thomson (JT), também esteja localizado em outro ambiente. Para simplificar esse acoplamento e reduzir as cargas no sistema de rotação, um pequeno goniômetro operando em condições criogênicas pode ser empregado, sendo responsável unicamente pela movimentação do pino de amostras, que terá sua massa limitada a poucos gramas. Atualmente, existem diversas opções de goniômetros criogênicos que podem ser utilizados na aplicação, sendo o Attocube ANR240 e o JPE CSR1 opções candidatas (Figura 5).

![A diagram of a machineDescription automatically generated](5.png)

Figura 5: Componentes principais do Manipulador de Amostra

Foi elaborado um modelo teórico do conceito apresentado na Figura 4, utilizando como base o esquema apresentado na Figura 6. Neste esquemático é possível verificar uma abstração do conceito proposto, bem como os principais parâmetros geométricos que impactam a análise de viabilidade. Dentre eles, pode-se citar a distância dos atuadores com relação ao centro R e à altura do pino de amostras com relação ao ponto de articulação do mecanismo h.

![Interface gráfica do usuárioDescrição gerada automaticamente](6.png)

Figura 6: Representação esquemática do conceito proposto. A) Vista posterior do mecanismo de movimentação, destacando as folded leaf springs FL e os atuadores X. B) Vista lateral do mecanismo, destacando novamente as folded leaf springs FL e o pino de amostras indicado por 1

O conceito apresentado na Figura 4 foi validado por simulação de maneira preliminar por meio da determinação da tensão máxima nas *folded leaf springs* (Figura 6), que atuam como guias elásticos no mecanismo quando estas são deslocadas pelo atuador. Desta análise (Figura 7), percebe-se que é factível o emprego de *folded leaf springs* de certas ligas de titânio e aço, que podem atingir tensão de escoamento de até cerca de 900 – 1000 GPa.

![GráficoDescrição gerada automaticamente](7.png)

Figura 7: Tensão máxima teórica em função dos parâmetros geométricos. A) Desenho esquemático da folded leaf spring e suas propriedades geométricas, sendo b a largura da chapa, L os comprimentos, t a espessura e ∆X1 o movimento imposto pelo atuador na ponta da flexure. B) O gráfico apresenta o comportamento da tensão em uma folded leaf spring com as propriedades geométricas apresentadas no gráfico quando sujeita a um deslocamento de 10,00 mm em sua extremidade