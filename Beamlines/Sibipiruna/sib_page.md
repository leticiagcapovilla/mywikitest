---
title: SIBIPIRUNA
description: Soft X-rays tomography beamline at Orion
published: 1
date: 2024-04-15T18:48:28.978Z
tags: 
editor: markdown
dateCreated: 2024-04-08T20:19:17.974Z
---

**Prot tipos Porta Amostras Criog nico**

*Conceptual Design Report (CDR)*

**Janeiro 2024**[\[RR1\]](#_msocom_1) 

  

![Intentionally Left Blank](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image001.gif) 

  

Lista de Autores

|     |     |     |
| --- | --- | --- |
| **AUTORES** | **GRUPO** | **CARGO** |
| **Gabriel A. Souza** | MEP | ADT |
| **Mairon O. de Lima** | MEP | Estagi rio |
| **Francesco R. Lena** | MEP | ADT |
| **Michel B. Machado** | MEP | ADT |

Aprova es

|     |     |
| --- | --- |
| **Aprovadores** | **Assinatura** |
|     |     |
| **Renan R. Geraldes** |     |
| ***MEP, LNLS*** |
|     |     |
|     |     |

 

Table of Contents

[1. Introdu o. 6](#_Toc163728481)

[1.1. Est gios do Ciclo de Vida: 9](#_Toc163728482)

[1.1.1. Conceitual: 9](#_Toc163728483)

[1.1.2. Desenvolvimento: 15](#_Toc163728484)

[1.1.3. Produ o: 15](#_Toc163728485)

[1.1.4. Utiliza o e Suporte. 16](#_Toc163728486)

[1.1.5. Desfazimento: 16](#_Toc163728487)

[1.2. Conclus o. 17](#_Toc163728488)

[2. Estudos de viabilidade e Sistemas Interoperacionais. 18](#_Toc163728489)

[2.1. Fluxo e Sistemas de Preparo de Amostras. 18](#_Toc163728490)

[2.1.1. Otimiza o do processo de vitrifica o e manipula o de amostras 21](#_Toc163728491)

[2.2. Sistema de Microscopia de Luz Vis vel Fluorescente Criog nico. 22](#_Toc163728492)

[2.2.1. Introdu o. 22](#_Toc163728493)

[2.2.2. Desenvolvimento do microsc pio de super-resolu o criog nico da SIBIPIRUNA 24](#_Toc163728494)

[2.2.3. M dulo criog nico para o microsc pio DMi8. 27](#_Toc163728495)

[2.2.4. M dulo de ilumina o estruturada para microsc pio DMi8. 28](#_Toc163728496)

[3. Refer ncias. 36](#_Toc163728497)

  

Acr nimos

|     |     |
| --- | --- |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

Abrevia es

|     |     |
| --- | --- |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

  

# 1.      Introdu o

No contexto do Orion, alguns objetivos cient ficos foram criados, sendo um deles o de gerar imagens 3D com resolu o nanom trica de c lulas ex-vivo infectadas com agentes de n vel 4 de biosseguran a (BSL4) em estado quase nativo. Para isso a linha de luz SIBIPIRUNA foi criada, possuindo como capacidade fundamental a utiliza o de raios-X moles (*soft X-rays*) para gerar tomografia 3D de c lulas isoladas. Esta capacidade necessariamente demanda que a c lula esteja em estado criog nico, assim possibilitando que a c lula tanto mantenha sua geometria quanto resista s doses de radia o dos raios-X ao longo das medidas. Al m disso, com o intuito de ampliar as capacidades cient ficas do instrumento com um maior volume de informa es das caracter sticas da c lula, concluiu-se ser necess rio complementar as imagens de raios-X com uma t cnica de imagem correlativa, criando-se assim uma plataforma de microscopia fluorescente de luz vis vel e tomografia de raios-X (CLXT do ingl s *correlative light and X-ray tomography*). Dessa forma, a t cnica de microscopia fluorescente tamb m poder ser empregada nas amostras estudadas na SIBIPIRUNA. A Figura 1 traz uma s ntese do processo de an lise e decis o do objetivo cient fico, onde apresentado um diagrama de Miss o e Capacidades, sendo que letra M define a Miss o, que nesse caso representa o objetivo cient fico proposto, e C as Capacidades a serem desempenhadas para que o objetivo da Miss o seja alcan ado. Al m disso, a figura ainda apresenta uma estrutura hier rquica onde as Capacidades s o derivadas, a partir da representa o das letras i e e sobre as setas, que representam inclus o e extens o, respectivamente.

![A diagram of a diagram
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image002.jpg)

Figura 1 - Miss o e Capacidades da linha de luz SIBIPIRUNA

Para o desenvolvimento da Capacidade 1.2, foi identificada a necessidade de um componente para posicionar a amostra no foco da linha de luz e realizar o movimento de tomografia. Ainda, devido ao fato de a amostra estar em estado criog nico, este componente tamb m demandar um Sistema de Gest o de Temperatura Criog nico com a fun o de manter a amostra em temperatura criog nica. A partir disso, optou-se por desenvolver um Sistema de Porta-Amostras Criog nico (PACRIO), que dever possuir as fun es descritas conforme Figura 2.

![A diagram of a computer
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image003.jpg)

Figura 2 - Diagrama de arquitetura do Porta-Amostras Criog nico, especificando os componentes, subcomponentes, fun es e informa es/mat ria/energia trocada entre as fun es

Este documento ir abordar o status de desenvolvimento do componente PACRIO, bem como da Capacidade 1.1, visto que essa capacidade em associa o com a 1.2 possibilita a Capacidade 1.1.1. Logo as opera es de 1.1 e 1.2 dever o ser compat veis entre si para que 1.1.1 seja atingida. Estudos de viabilidade t cnica dos m todos tradicionais de preparo de amostras e congelamento tamb m ser o apresentados neste documento, uma vez que s o pr -requisitos para a solu o de porta-amostra a ser implementado no instrumento

  

![A screenshot of a computer
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image004.jpg)

Figura 3 Diagrama de arquitetura e capacidade principal da linha de luz SIBIPIRUNA

  

Or amento: as aquisi es desse projeto v m ocorrendo atrav s do centro de custo referente ao PACRIO, com um montante total previsto de R$4.500.000,00[\[RR2\]](#_msocom_2) . Na Tabela 1 s o detalhados os montantes destinados s aquisi es para cada um dos subsistemas e a data prevista para compra.

Tabela 1 Or amento para o SoI

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| **PACRIO** | **Subsistema** | **Total rea** | **Fase A** | **Fase B** | **Fase C** | **Previs o de compra Fase A** |
| TXM Imaging | R$1.505.000,00 | R$559.500,00 | R$644.500,00 | R$301.000,00 | 01/03/2024 |
| Sample transfer | R$800.000,00 | R$240.000,00 | R$400.000,00 | R$160.000,00 |
| Correlative Imaging | R$885.000,00 | R$419.500,00 | R$288.500,00 | R$177.000,00 |
| Sample preparation | R$1.310.000,00 | R$393.000,00 | R$655.000,00 | R$262.000,00 |

1.1.  Est gios do Ciclo de Vida: a tabela abaixo apresenta os est gios do ciclo de vida do PACRIO em uma escala temporal de trimestres. Nos cap tulos posteriores ser o descritas as atividades espec ficas para cada um desses est gios.

Tabela 2 - Est gios do ciclo de vida do PACRIO

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | **Conceitual** | **Desenvolvimento** | **Produ o** | **Utiliza o** | **Suporte** | **Desfazimento** |
| **10/23 - 12/23** | X   |     |     |     |     |     |
| **01/24 - 03/24** | X   |     |     |     |     |     |
| **04/24 - 06/24** | X   | X   |     |     |     |     |
| **07/24 - 09/24** | X   | X   |     |     |     |     |
| **10/24 - 12/24** |     | X   |     |     |     |     |
| **01/25 - 03/25** |     | X   | X   |     |     |     |
| **04/24 - 06/25** |     | X   | X   |     |     |     |
| **07/25 - 09/25** |     |     |     | X   | X   |     |
| **10/25 - 12/25** |     |     |     | X   | X   |     |
| **01/26 - 03/26** |     |     |     |     |     | X   |

1.1.1.     Conceitual: [\[RRG3\]](#_msocom_3) [\[FRL4\]](#_msocom_4) a etapa Conceitual consiste em estudos de avalia o das solu es, observando o entendimento do problema, requisitos e performance. Esta etapa se encerra a partir da aprova o de uma das solu es propostas, na qual ser avaliado o conceito proposto para cinem tica, din mica, gerenciamento t rmico, minimiza o da exposi o a rea de descontamina o e viabilidade de manuten o.

Na etapa conceitual, representada pelo CDR da esta o experimental, foram identificados os requisitos de baixo n vel para o sistema de movimenta o. Estes requisitos abrangem capacidades essenciais que o sistema deve possuir para alcan ar os objetivos finais do projeto. importante ressaltar que a an lise de viabilidade desses conceitos, assim como a valida o de sua capacidade em atender totalmente aos requisitos mapeados, representa um passo subsequente. Esse processo envolver a atua o das equipes de engenharia na modelagem e prototipagem. Assim, embora os conceitos aqui apresentados ainda n o tenham passado por uma valida o final, eles demonstram potencial para atender aos requisitos em uma avalia o preliminar. A lista de requisitos (LLR, de *low-level requirement*) pertinentes ao projeto do est gio do porta-amostras criog nico apresentada abaixo.

       LLR-4.1: A temperatura da amostra preservada n o dever exceder 110K em todo o fluxo de trabalho.

       LLR-4.6: Um manipulador de amostras criog nicas com quatro graus de liberdade dever ser inclu do na Esta o SIBIPIRUNA.

       LLR-4.7: Um cryocooler de circuito fechado dever ser usado para o sistema de transfer ncia de amostra.

       LLR-4.8: O suporte de amostra dever ser compat vel com grades TEM (*Transmission Electron Microscopy*) de 3,5 mm.

       LLR-4.9: O suporte de amostra dever ser compat vel com substratos de membrana de nitreto de sil cio.

       LLR-4.10: O suporte de amostra dever ser compat vel com capilares de vidro.

       LLR-5.12: O Est gio de Amostra dever fornecer capacidades de posicionamento total de todo o substrato de amostra para efici ncia de rea de imagem otimizada.

       LLR-5.13: Para o uso de grades TEM, o est gio dever permitir um deslocamento cartesiano m nimo de 1,5 mm em todas as dire es XYZ.

       LLR-5.14: O sistema de Est gio de Amostra dever realizar um alinhamento rotacional preciso em torno de pelo menos um eixo que intersecta a regi o de imagem alvo.

       LLR-5.15: O est gio de rota o dever permitir pelo menos 180 de rota o, com a op o de 360 para corre o da orienta o da amostra.

A partir das defini es b sicas dos requisitos para o est gio do Manipulador de Amostras da SIBIPIRUNA, pode-se desenvolver um design conceitual. Prezando por diretrizes de isolamento da regi o da amostra em rela o ao restante da linha de luz por quest es de biosseguran a, impondo simplifica es nas interfaces mec nicas, e possibilitando o uso de tecnologias j validadas no Sirius/LNLS, o design atual aplica os conceitos de um *Tripod*, que utiliza cinem tica paralela para movimenta o cartesiana. Acoplado a ele, um est gio rotativo pode ser utilizado para o eixo de tomografia (Figura 4).

![](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image005.gif)

Figura 4 - Manipulador da amostra e Sistema Gerenciamento T rmico. A) vista isom trica da parte interna (exposta s amostras e ciclos de descontamina o mais frequentes), e B) vista isom trica da parte externa (em ambiente de v cuo separado da amostra).

Conceitos de atuadores foram explorados para o est gio em quest o. O nano-posicionador NSAU, da JPE, surgiu como um candidato promissor, devido ao seu curso de movimenta o e for a necess rios, al m de um design completamente herm tico, selado em um encapsulamento met lico e equipado com um sistema de feedback de posicionamento (encoder) integrado. No design atual, vi vel isolar totalmente os componentes eletr nicos de precis o e os sistemas de movimenta o dos atuadores do ambiente de amostra, minimizando a exposi o desses componentes a agentes de descontamina o que podem causar corros o e desgaste.

Embora o sistema NSAU possua encoders internos, muitas vezes prefer vel medir a posi o o mais pr ximo poss vel da regi o de interesse. Assim, o conceito atual incorpora um sistema de interferometria para a metrologia na posi o imediatamente antes da amostra, permitindo que os elementos interferom tricos sejam posicionados fora do ambiente de amostra e transmitindo o sinal atrav s de tr s janelas pticas. A viabilidade deste conceito ser explorada, com foco na valida o dos cursos de movimenta o e na aplicabilidade dos interfer metros em um sistema com um grande desvio angular natural.

Uma outra caracter stica distintiva do design atual a utiliza o de um acoplamento flex vel para a transfer ncia de calor por condu o, conectando um criostato regi o de interesse do est gio. Isso possibilita que o sistema de refrigera o, a saber, um criostato do tipo pulse tube (PT) ou Joule-Thomson (JT), tamb m esteja localizado em outro ambiente. Para simplificar esse acoplamento e reduzir as cargas no sistema de rota o, um pequeno goni metro operando em condi es criog nicas pode ser empregado, sendo respons vel unicamente pela movimenta o do pino de amostras, que ter sua massa limitada a poucos gramas. Atualmente, existem diversas op es de goni metros criog nicos que podem ser utilizados na aplica o, sendo o Attocube ANR240 e o JPE CSR1 op es candidatas (Figura 5).

![A diagram of a machine
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image006.gif)

Figura 5 - Componentes principais do Manipulador de Amostra

Foi elaborado um modelo te rico do conceito apresentado na Figura 4, utilizando como base o esquema apresentado na Figura 6. Neste esquem tico poss vel verificar uma abstra o do conceito proposto, bem como os principais par metros geom tricos que impactam a an lise de viabilidade. Dentre eles, pode-se citar a dist ncia dos atuadores com rela o ao centro R e a altura do pino de amostras com rela o ao ponto de articula o do mecanismo h.

A partir do conceito da Figura 4 foi elaborado um modelo para avalia o dos principais par metros geom tricos (Figura 6) e din micos (Figura 7) e cinem tico (Figura 8) do PACRIO. Na Figura 6 destaca-se os par metros de dist ncia dos atuadores em rela o ao centro (R) e a dist ncia vertical entre pino de amostra e o seu ponto de articula o.

Al m disso o modelo da Figura 6 foi validado por simula o para determina o da tens o m xima nas *folded leaf springs*, que atuam como guias el sticos no mecanismo quando estas s o deslocadas pelo atuador. Desta an lise (Figura 7), percebe-se que fact vel o emprego de *folded* *leaf springs* de certas ligas de tit nio e a o, que podem atingir tens o de escoamento at cerca de 900 1000 GPa.

![Interface gr fica do usu rio
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image007.gif)

Figura 6 - Representa o esquem tica do conceito proposto. A) Vista posterior do mecanismo de movimenta o, destacando as *folded leaf springs* FL e os atuadores X. B) Vista lateral do mecanismo, destacando novamente as *folded leaf springs* FL e o pino de amostras indicado por 1.

![Gr fico
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image008.gif)

Figura 7 - Tens o m xima te rica em fun o dos par metros geom tricos. A) Desenho esquem tico da *folded leaf spring* e suas propriedades geom tricas, sendo b a largura da chapa, L os comprimentos, t a espessura e ∆X1 o movimento imposto pelo atuador na ponta da *flexure.* B) O gr fico apresenta o comportamento da tens o em uma *folded leaf spring* com as propriedades geom tricas apresentadas no gr fico quando sujeita a um deslocamento de 10,00 mm em sua extremidade.

Al m da determina o da tens o m xima foi feito um estudo para a avalia o do volume que este conceito capaz de varrer. A Figura 8 apresenta uma esquematiza o deste volume com base no pino de amostras considerado no conceito apresentado na Figura 4.

Al m dos estudos preliminares geom tricos e din micos do PACRIO, foi feito tamb m um estudo cinem tico com o intuito de se avaliar o volume que esse sistema capaz de varrer. A Figura 8 apresenta uma esquematiza o deste volume com base no pino de amostras considerado no conceito apresentado na Figura 4.

![Diagrama
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image009.gif)

Figura 8 - Esquematiza o . A) Vista frontal do pino de amostras, sendo 1,2 e 3 os grids e 4 o pino de amostras. B) Representa o do pino de amostras, a rea hachurada representa a rea a ser analisada, delimitada por um per metro na forma de um oblongo, a vari vel r representa o raio dos grids, a representa o espa amento entre eles e θ representa um par metro da curva que descreve o per metro.

O per metro da rea hachurada apresentado na Figura 8 B representa a regi o mais externa qual o est gio deve ser capaz de levar as amostras, assim, para avaliar o comportamento dos 3 atuadores, a curva que descreve este per metro foi parametrizada em fun o de um ngulo θ, deste modo, para cada valor de θ tem se os valores de x e y que satisfazem a curva que descreve o per metro. Os pontos descritos por x e y, por sua vez, s o inseridos nas matrizes de cinem tica possibilitando assim a determina o do movimento que cada atuador deve realizar, estes resultados s o apresentados na Figura 9.

![Uma imagem contendo Gr fico
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image010.gif)

Figura 9 Resultados obtidos por meio da an lise cinem tica preliminar. A) Curso necess rio considerando a n o superposi o dos grids. B) Curso necess rio considerando a superposi o dos grids.

O cen rio apresentado na Figura 9 A demonstra que o curso necess rio excede o curso nominal dos atuadores para um espa amento de 3,5 mm entre os grids, entretanto, ao considerar um espa amento de 3 mm entre os grids, tem-se que o curso suficiente (Figura 9 B). Outras modifica es geom tricas tamb m t m impacto no curso necess rio, por m n o foram demonstradas pois este estudo se caracteriza apenas como uma avalia o preliminar, podendo ser estendido no futuro.

1.1.2.     Desenvolvimento: a etapa de desenvolvimento consiste na evolu o de projeto detalhada do SoI. Esse est gio se encerra ap s uma valida o anal tica da din mica, cinem tica, t rmica e mec nica do PACRIO. Al m disso, espera-se que os elementos e a opera o do PACRIO sejam validados sob a a o de um agente de esteriliza o a ser utilizado na SIBIPIRUNA.[\[RRG5\]](#_msocom_5) 

1.1.3.     Produ o: o est gio de produ o se inicia a partir da tradu o de todas as informa es do desenvolvimento em elementos do SoI. Durante essa etapa esperada uma grande integra o entre o MEP e o grupo de Gest o de Projetos, por ser uma fase com elevado n mero de aquisi es atrav s fornecedores externos. Al m disso, esperado um grande esfor o por parte do MEP na tradu o das especifica es do desenvolvimento em documenta o t cnica para que fornecedores e grupos internos forne am os componentes e servi os que atendam corretamente s especifica es. Atividades relacionadas ao registro e gest o de problemas tamb m s o esperadas, e ser necess rio estimar um tempo de execu o que leve em conta esses retrabalhos. Essa fase ser encerrada quando o equipamento estiver montado, integrado e com todas as fun es validadas em conson ncia com os par metros determinados na etapa de Desenvolvimento. Conforme a Tabela 2, a data prevista para in cio e conclus o da etapa de Produ o ser entre 01/2025 e 06/2025.[\[RRG6\]](#_msocom_6) 

1.1.4.     Utiliza o e Suporte: o est gio de Utiliza o e Suporte caracterizado por atividades nas quais o SoI entrar em opera o em seu ambiente de uso, a partir disso o objetivo da miss o ser alcan ado. Esse est gio se encerra quando o SoI gerar informa es capazes de suportar a tomada de decis o sobre a viabilidade da sua opera o em um contexto real da linha de luz SIBIPIRUNA. A tomada de decis o dever possuir 2 possibilidades, sendo elas: otimizar o SoI mantendo seu conceito atual ou reprojetar o SoI a partir de um novo conceito.

1.1.5.     Desfazimento: O est gio de Desfazimento consiste das atividades planejadas para o encerramento do ciclo de vida do SoI. Para o PACRIO esperado que, quando a sua utilidade seja esgotada, seus componentes sejam encaminhados para a esta o experimental da linha SIBIPIRUNA, tanto quanto poss vel, ou desmontados e armazenados em condi es adequadas, para que possam vir a ser reutilizados ou realocados em outros projetos.

## 1.2. Conclus o

Pode-se observar que o projeto vem sendo conduzido a partir de uma an lise sist mica, onde espera-se uma integra o entre os componentes da opera o da linha de forma a garantir as capacidades da SIBIPIRUNA. Importante observar tamb m que foram realizados estudos a partir de outras linhas de luz que possuem capacidades similares a da SIBIPIRUNA, al m da utiliza o de conceitos j validados em projetos anteriores no LNLS. Isso possibilita que os grupos de engenharia do LNLS desenvolvam o projeto de forma mais assertiva e segura.

Atualmente o projeto possui como caminho cr tico a valida o de sua opera o em um cen rio de descontamina o. Cabe ressaltar que a etapa de Produ o tamb m pode ser cr tica devido ao fluxo de aquisi es de itens comerciais e servi os, que podem levar a atrasos que impactaram na evolu o do projeto e consequentemente avan o sobre os est gios do ciclo de vida.

  

# 2.    Estudos de viabilidade e Sistemas Interoperacionais

A opera o da SIBIPIRUNA envolve a intera o entre diversos sistemas, e integrar essas interfaces uma tarefa fundamental para garantir que todos os componentes possam ser desenvolvidos e operados em conformidade. Avaliando a opera o do PACRIO, poss vel identificar as depend ncias do sistema, sendo elas listadas abaixo:

       Sistema de Preparo de Amostras: dado que a amostra ser preparada e carregada em um suporte [\[RRG7\]](#_msocom_7) espec fico e este transferido para o PACRIO, identificou-se a necessidade de incluir o preparo de amostras nessa fase de prototipagem, cobrindo principalmente quest es relacionadas vitrifica o adequada das amostras criog nicas e otimiza o do fluxo de trabalho e da transfer ncia da amostra entre os sistemas;

       Sistema de Microscopia de Luz Vis vel Fluorescente Criog nico: a partir da capacidade 1.1.1 que determina que a SIBIPIRUNA seja capaz de gerar uma imagem CLXT, mostrou-se necess rio tamb m o desenvolvimento de um microsc pio de fluoresc ncia, de forma a garantir compatibilidade entre ele e o microsc pio de raios-X da SIBIPIRUNA.

A partir dessas demandas, frentes de trabalho paralelas e iterativas com PACRIO foram iniciadas, de forma a criar um cen rio que atenda ao funcionamento desses diferentes sistemas. A seguir ser o listadas as frentes de trabalho e nos cap tulos posteriores seus status de desenvolvimento.

## 2.1. Fluxo e Sistemas de Preparo de Amostras

A evolu o da criomicroscopia, especialmente no contexto da microscopia de raios-X moles, marcou uma transi o significativa na forma como os esp cimes biol gicos s o preparados e analisados. Esse avan o centra-se no processo de vitrifica o (ou criofixa o), uma t cnica que substitui os m todos tradicionais de fixa o qu mica usados na microscopia eletr nica. A vitrifica o, como evidenciado pela pesquisa de criomicroscopia eletr nica, fundamental para minimizar altera es morfol gicas que poderiam comprometer a representatividade e a precis o dos resultados (Figura 8). Al m disso, a an lise de amostras vitrificadas em estado criog nico n o apenas garante sua excelente preserva o, mas tamb m proporciona uma estabilidade robusta contra danos por radia o na microscopia de raios-X moles. Consequentemente, esses avan os na criomicroscopia de esp cimes biol gicos t m relev ncia para o projeto SIBIPIRUNA, que pretende utilizar a criofixa o para examinar amostras biol gicas em condi es que representem de perto seu estado natural, visando uma representa o imparcial e detalhada das estruturas biol gicas envolvidas nos processos de infec o viral.  

![A collage of images of different types of cells
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image011.gif)

Figura \- *(1) Se es virtuais de tomogramas de raios-X moles de fibroblastos vitrificados, secos ao ar e secos por CPD, indicando nucl olos, got culas de lip dio e mitoc ndrias. A c lula seca ao ar na grade mostra contra o. Barra de escala: 10 μm (Adaptado de* Chatzimpinou et al. (2023)*) (2) Micrografias eletr nicas comparando tecidos de test culos de N. lamellosa*[\[GA8\]](#_msocom_8)  *processados por fixa o qu mica e vitrifica o seguida de inclus o em resina. Esp cimes quimicamente fixados mostram coagula o da membrana e encolhimento entre c lulas (adaptado de* Martens et al. (2009)*) (3) Compara o de prepara es do v rus Vaccinia: fixa o qu mica, congelamento em alta press o/substitui o por congelamento e microscopia eletr nica criog nica. A fixa o qu mica leva ao colapso das camadas do v rus (Adaptado* de Chlanda et al. (2009)​*). (4) Micrografias comparativas de envelopes celulares de M. smegmatis: fixa o qu mica e vitrifica o seguida de inclus o em resina. A vitrifica o resulta em menor largura do envelope celular (Adaptado de* ​​Bleck et al. (2010)*). (5) Compara o de tomogramas de raios-X moles em linf citos B humanos nativos e fixados da linhagem GM12878. As c lulas fixadas apresentam morfologia distorcida e got culas de lip dio (Adaptado de* Loconte et al. (2021)​*).* 

Como apresentado na Figura 9, para a linha SIBIPIRUNA ser empregado um fluxo de trabalho criog nico completo de c lulas congeladas e hidratadas (vitrificadas) em substratos finos (e possivelmente tamb m em capilares). Embora essa abordagem traga vantagens substanciais para a qualidade dos dados de tomografia e a abordagem cient fica, ela imp e desafios significativos para o projeto do fluxo de trabalho de prepara o e manuseio de amostras. Isso se torna ainda mais complexo no contexto do ambiente BSL3/4, onde o uso de EPIs pode reduzir a mobilidade e destreza do usu rio. Com isso em mente, o fluxo de trabalho atual est sendo projetado para minimizar o n mero de intera es manuais do usu rio com a amostra e reduzir a quantidade de equipamentos dentro da chamada "zona quente". Uma frente de trabalho espec fica foi criada para tratar do fluxo de trabalho para otimiza o do processo de vitrifica o de c lulas, que ser abordado em detalhes no cap tulo posterior.

![A computer screen shot of a diagram
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image012.gif)

Figura \- *Fluxo de trabalho proposto para a prepara o de amostras para an lise celular dentro do framework da linha de luz SIBIPIRUNA. Inicialmente, (1) as grades ou membranas passam por uma descarga de plasma para melhorar a hidrofilicidade, um pr -requisito para uma ader ncia eficaz das amostras. Em seguida, (2) realizada a litografia de padr es de ades o nas grades usando os sistemas PRIMO & DMi8, garantindo a ades o celular direcionada. A prepara o continua com (3) a deposi o de cultura de c lulas ou suspens o nas grades. Em certos casos, (7) nanopart culas de ouro s o depositadas como marcadores fiduciais para an lise tomogr fica. As amostras s o ent o submetidas a (4) triagem em temperatura ambiente com o DMi8 para verifica o antes do (8) blotting com o dispositivo Leica GP2. Posteriormente, as amostras s o (9) imersas em etano, uma etapa crucial para sua preserva o morfol gica. O fluxo de trabalho continua medida que as amostras s o carregadas em uma (10) GridBox, transferidas criogenicamente para um (11) m dulo de carregamento de amostras (VCM) e fixadas usando o sistema (12) AutoGrid. Ap s a (13) transfer ncia criog nica para o criomicrosc pio para imagens de super-resolu o por ilumina o estruturada (SIM), elas podem passar por (14) microscopia correlativa sobre o criomicrosc pio SIM. As amostras s o ent o (15) retornadas ao VCM criogenicamente, (16) carregadas em um suporte de amostra e colocadas em um (17) cartucho de transfer ncia. Este cartucho ent o carregado no sistema (18) VCT500, que finalmente leva (19) transfer ncia para a linha de luz para imagens de tomografia de raios-X moles (SXT). Essa sequ ncia abrangente garante que as amostras sejam meticulosamente preparadas e preservadas para an lises de alta resolu o.* 

Al m de a SIBIPIRUNA ser projetada para a capacidade de TXM confi vel, segura e de alto desempenho, com uma integra o direta com o ambiente BLS4 do Orion para imagens 3D de c lulas infectadas com pat genos de n vel 3 e 4, pesquisas e colabora es com especialistas de outros s ncrotrons (como cientistas da linha B24, no Diamond Light Source) demonstraram que o uso de outras t cnicas baseadas em microscopia de luz para imageamento de prote nas e pequenas mol culas fluorescentes acopladas ou intercaladas a organelas espec ficas podem fornecer um contexto celular adicional importante. Em certo sentido, as imagens de microscopia de fluoresc ncia podem ajudar os cientistas a compreender melhor a localiza o e discernir estruturas subcelulares quando sobrepostas aos dados tomogr ficos de cryo-TXM, o que feito a partir de t cnicas matem ticas de registro de imagens. Com isso em mente, o atual fluxo de trabalho criog nico est sendo projetado para tamb m incorporar um criomicrosc pio de fluoresc ncia 3D de super-resolu o com base em um microsc pio de ilumina o estruturada (SIM).

### 2.1.1.     Otimiza o do processo de vitrifica o e manipula o de amostras

Para otimiza o do processo de vitrifica o, foi feita uma revis o bibliogr fica a respeito dos m todos e equipamentos comerciais existentes para essa finalidade. Foram avaliados 4 equipamentos, sendo eles o Vitrobot da Thermo Fisher ( Vitrobot Mark IV System - BR , s.d.), o EM GP2 da Leica ( EM GP2 Automatic Plunge Freezing , s.d.), o Cryogenium da Linkam ( Cryogenium , s.d.) e o VitroJet da CryoSol (Cryosol-World, s.d.). A Tabela 3 apresenta uma compara o entre eles.

Tabela 3 - Compara o entre principais equipamentos de vitrifica o de amostra

|     |     |     |     |
| --- | --- | --- | --- |
|     | **Deposi o de amostra** | **T cnica de controle da espessura da amostra** | **T cnica de vitrifica o** |
| **Vitrobot** | Manual | Blotting com papel | Imers o (*plunge)* |
| **EM GP2** | Manual | Blotting com papel | Imers o (*plunge)* |
| **Cryogenium** | Imers o autom tica | Suc o | Imers o (*plunge)* |
| **Vitrojet** | Deposi o autom tica | Deposi o precisa | Jato (*jet)* |

Atualmente, o equipamento Vitrojet da CryoSol, o nico da lista com vitrifica o pelo processo recente e patenteado conhecido como *jet freezing*, apresenta-se como o candidato prefer vel para aplica o dentro do fluxo de trabalho da SIBIPIRUNA, por permitir um n vel de automa o maior e ser, em teoria, mais robusto e repetitivo em termos da qualidade de vitrifica o. No entanto, o equipamento comercial foi originalmente desenvolvido para preparo das chamadas *single particles*, exigindo que customiza es e valida es sejam realizadas para c lulas isoladas, que o caso de interesse para a SIBIPIRUNA. Portanto, planeja-se a realiza o de colabora es t cnicas, prototipagem e testes de valida o para a tecnologia de *jet freezing* dentro das condi es de contorno da SIBIPIRUNA no futuro pr ximo. At l , uma primeira rota mais conhecida, via *plunge freezing*, est sendo colocada em pr tica para valida o antecipada do maior n mero poss vel de equipamentos e etapas do fluxo de trabalho (Figura 9), a partir da qual primeiros estudos sobre a qualidade da vitrifica o e dos passos de manipula o das amostras podem ser conduzidos.[\[RRG9\]](#_msocom_9) 

## 2.2. Sistema de Microscopia de Luz Vis vel Fluorescente Criog nico

### 2.2.1.     Introdu o

Para viabiliza o de microscopia correlativa na linha de luz SIBIPIRUNA[\[RRG10\]](#_msocom_10) , ser desenvolvido um criomicrosc pio de fluoresc ncia de super-resolu o por ilumina o estruturada (SIM), que dever se adequar s necessidades espec ficas de biosseguran a e robustez, al m de ser projetado especificamente para o suporte de amostra da esta o experimental. Esse microsc pio ser desenvolvido com base em outros designs pticos j comprovados. Um dos designs inspiradores que fomentaram os estudos preliminares desse projeto foi o microsc pio cryo-SIM B24[\[RRG11\]](#_msocom_11) , desenvolvido para a linha de luz B24 do Diamond Light Source ​(Phillips et al. 2020). Em uma vis o geral, o sistema emprega quatro lasers de excita o de comprimentos de onda distintos 405, 488, 561 e 647 nm para gerar padr es de ilumina o estruturada atrav s de um modulador de luz espacial (SLM *Spatial Light Modulator*). Esses padr es s o o n cleo do SIM, pois induzem franjas de moir que codificam informa es da amostra que n o seriam observadas em um microsc pio convencional devido ao limite de difra o da lente objetiva. Se o padr o de ilumina o for conhecido, poss vel utilizar m todos matem ticos de reconstru o para recuperar a estrutura original da amostra com at o dobro da resolu o originalmente limitada pela objetiva.

![A diagram of a diagram of a diagram
Description automatically generated with medium confidence](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image013.jpg)

Figura \- Layout ptico do microsc pio cryo-SIM da B24. Retirado de Phillips et al. (2020).

Conforme descrito na publica o original e ilustrado na Figura 10, a luz dos lasers direcionada e moldada atrav s de uma s rie de componentes pticos, incluindo lentes (L), aberturas (A), espelhos (M), pinholes (Ph) e espelhos dicroicos (D) para alcan ar um controle preciso da ilumina o. As aberturas A1 e A2 s o especificamente utilizadas para refinar o perfil do feixe e eliminar difra es de ordem superior, respectivamente. Um rotacionador de polariza o (PR *Polarization Rotator*) alinha a polariza o da luz com o eixo ptico do SLM, enquanto um telesc pio formado pelas lentes L1 e L2 garante a expans o e o foco dos padr es de luz estruturada na amostra[\[RRG12\]](#_msocom_12) . A emiss o de fluoresc ncia coletada por uma objetiva orientada perpendicularmente ao plano horizontal do arranjo ptico. Essa emiss o ent o refletida e dividida entre dois espelhos dicroicos (D1 e D2), isolando o sinal de fluoresc ncia, que posteriormente capturado pelas c meras Cam1 e Cam2. Essas c meras s o sincronizadas com o SLM para capturar sequencialmente m ltiplas imagens sob diferentes padr es de ilumina o, que s o posteriormente reconstru das para formar uma imagem de super-resolu o. A inclus o dos espelhos de desvio FM1 e FM2 [\[RRG13\]](#_msocom_13) [\[MB14\]](#_msocom_14) proporciona flexibilidade no caminho da luz, permitindo caminhos de ilumina o ou de imagem seletivos. O arranjo completo projetado para otimizar o processo de SIM, melhorando a resolu o e fornecendo informa es detalhadas sobre as complexidades estruturais de esp cimes biol gicos em um n vel abaixo do limite de difra o da objetiva (Adaptado de Phillips et al. (2020)).

No design descrito, a amostra imageada por uma objetiva alojada pr xima a um est gio criog nico da Linkam (Modelo CMS196), isolada por uma atmosfera de vapor de nitrog nio seco. Embora este m todo seja confi vel para a criopreserva o de amostras, o design com o compartimento aberto do est gio pode inadvertidamente levar deposi o de umidade atmosf rica nas amostras, resultando em contamina o por cristais de gelo o que, de fato, p de ser verificado experimentalmente por usu rios do sistema. Isso particularmente problem tico, pois os cristais de gelo podem difratar a ilumina o de raios-X moles incidente na microscopia de raios-X de transmiss o (TXM), manifestando-se como manchas escuras de alto contraste que podem obscurecer detalhes da amostra. Al m disso, o uso de um *dewar* de nitrog nio l quido diretamente acoplado ao est gio exige reabastecimentos frequentes, que podem induzir desvios posicionais devido a mudan as c clicas da massa do sistema. Ademais, com a lente objetiva posicionada pr xima amostra, a condu o e a convec o de calor atrav s da atmosfera de nitrog nio podem resfriar os elementos iniciais da lente, levando contra o t rmica e, possivelmente, a aberra es pticas. Consequentemente, um dos principais desafios de design para o criomicrosc pio de super-resolu o por ilumina o estruturada (SIM) da SIBIPIRUNA est na elimina o do est gio criog nico aberto e na redu o da depend ncia de fluidos criog nicos que requerem reabastecimento. 

Assim, o conceito previsto para o criomicrosc pio SIM da SIBIPIRUNA (Figura 11) integra um est gio criog nico dentro do v cuo e um criostato de ciclo fechado como mecanismo de resfriamento. Espera-se que esta configura o alivie os problemas mencionados, embora introduza desafios de engenharia substanciais. Estes incluem a necessidade de uma janela ptica para separar o ambiente de v cuo da amostra do entorno ptico e dos detectores, bem como a incorpora o de uma interface ar-v cuo para o carregamento da amostra. Esta interface pode ter uma dupla finalidade, abordando tamb m o desafio existente de desenvolver um sistema de carregamento de amostras para o TXM da esta o experimental da SIBIPIRUNA.

![A diagram of a machine
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image014.gif)

Figura \- Conceito do criomicrosc pio de super-resolu o por ilumina o estruturada (SIM) da SIBIPIRUNA: *(1) amostra em v cuo, (2) est gio criog nico, (3) lente objetiva de alta abertura num rica (NA), (4) janela ptica ar-v cuo; (5) espelho dicroico; (6) c mera de alta efici ncia; (7) gerador de padr es SLM; (8) lan ador de fibra; (9) unidade de combina o de laser acoplado por fibra (LCU); (10) v lvula de acoplamento para transfer ncia de amostra; (11) maleta de transfer ncia de amostra; (12) refrigerador de ciclo fechado (por exemplo, Stirling Pulse-Tube); e (13) tubula o de v cuo da zona quente.* 

A equipe de design do LNLS tamb m planeja aprimorar o design ptico para melhorar o desempenho na aquisi o de imagens e facilitar o alinhamento e a manuten o de tais pticas no ambiente BLS4. Isso inclui, mas n o se limita, a (1) aumentar o campo de vis o (FOV) do microsc pio usando um SLM maior e um detector CMOS de maior resolu o e maior tamanho; (2) incorporar est gios motorizados de inclina o e rota o para a maioria dos espelhos e elementos dicroicos, e est gios lineares para as lentes principais; (3) incorporar lasers acoplados por fibra que ser o colocados fora do ambiente BLS4 para facilitar a manuten o e aumentar a durabilidade dos lasers, pois qualquer contato com produtos qu micos de limpeza seria mitigado; e (4) introduzir pticas de modula o de frente de onda para compensar distor es da topologia da amostra e geometria do substrato da amostra (por exemplo, grades TEM planas e capilares de vidro cil ndricos). H tamb m o estudo de viabilidade de se ter uma nica c mera CMOS de alta efici ncia para aquisi o r pida em um nico canal. 

### 2.2.2.     Desenvolvimento do microsc pio de super-resolu o criog nico da SIBIPIRUNA

Com o avan o das pesquisas bibliogr ficas acerca dos microsc pios de super-resolu o por ilumina o estruturada, foi poss vel constatar a presen a de outros tra ados pticos que diferem daquele proposto por Phillips et al. (2020). A observa o de todos estes trabalhos permitiu o levantamento de diretrizes gerais para o desenvolvimento deste projeto, bem como de requisitos de alto n vel. Entretanto, alguns autores n o s o t o claros ao expor as decis es de projeto particulares de cada microsc pio, tornando alguns aspectos incertos. Assim, para um completo delineamento das decis es de projeto a serem adotadas, necess ria a constru o de prot tipos e o desenvolvimento de modelos computacionais para posterior simula o em *softwares* como o ANSYS ZEMAX, cuja licen a foi adquirida para realiza o deste projeto.

Dentre os desenvolvimentos em super-resolu o por ilumina o estruturada pela comunidade cientifica, destaca-se o OpenSIM (Hannebelle et al. 2024), por ser um acess rio incorpor vel a microsc pios de fluoresc ncia comerciais, valendo-se dos est gios de amostras e sistemas de captura de imagem destes microsc pios para produzir imagens SIM 2D com resolu o abaixo de 200 nm. Al m disso, o baixo custo do projeto e seu car ter *open source* o qualificam como uma ferramenta de prototipagem e valida o das ideias propostas para o criomicrosc pio SIM da SIBIPIRUNA. Deste modo, este conceito poderia ser utilizado nas etapas iniciais de prototipagem do criomicrosc pio de super-resolu o, ou at mesmo se tornar a solu o definitiva para a produ o de imagens de fluoresc ncia 3D (3D-SIM) de amostras vitrificadas ao ser utilizado em conjunto a um porta-amostras criog nico montado sobre um microsc pio invertido de fluoresc ncia convencional, aos moldes do trabalho desenvolvido por Li et al. (2023).

A Figura 14 sintetiza alguns dos poss veis cen rios de desenvolvimento do microsc pio de super-resolu o criog nico da linha de luz SIBIPIRUNA. Nos diferentes cen rios, o microsc pio invertido de fluoresc ncia Leica DMi8, adquirido para realiza o dos testes iniciais, atua como uma plataforma para o desenvolvimento de um microsc pio de super-resolu o por imagem estruturada, com a qual os diferentes prot tipos e m dulos podem ser incorporados para a valida o de conceitos. O diferencial de cada cen rio reside no produto final a ser entregue: no primeiro cen rio, os prot tipos de porta-amostras criog nico e de imagem estruturada s o utilizados apenas para valida o de conceitos, sendo o produto final um microsc pio criog nico SIM totalmente independente[\[RRG15\]](#_msocom_15) [\[MO16\]](#_msocom_16)  compat vel com amostras BSL3/4. No segundo cen rio, esses prot tipos s o refinados, constituindo uma solu o de criomicroscopia SIM integrada ao Leica DMi8. No terceiro cen rio, seriam desenvolvidas duas solu es de criomicroscopia: uma integrada ao Leica DMi8 e um outro criomicrosc pio SIM independente.

  

  

![](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image015.gif)

Figura 14[\[RRG17\]](#_msocom_17) [\[MO18\]](#_msocom_18)  - Poss veis cen rios de desenvolvimento para obten o de um criomicrosc pio 3D-SIM. Linhas cheias indicam que o componente em quest o derivado diretamente do componente anterior, enquanto linhas tracejadas indicam que apenas conceitos do componente anterior ser o aproveitados.

Dado que o microsc pio invertido Leica DMi8 reconhecido como uma plataforma universal modular para diferentes t cnicas de microscopia, o desenvolvimento de acess rios capazes de estender as suas capacidades originais fact vel. Visando transform -lo em um microsc pio SIM criog nico, iniciou-se o desenvolvimento de um m dulo de ilumina o estruturada e de um m dulo porta-amostras criog nico para o Leica DMi8. Uma representa o desta implementa o apresentada na Figura 15.

**![Uma imagem contendo Seta
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image016.gif)**

Figura 15 - No conceito baseado na plataforma DMi8, podem ser vistos os m dulos de ilumina o estruturada e porta-amostras criog nico acoplados ao microsc pio.

No conceito atual, o suporte de amostras dever ser montado no est gio de amostras comercial SCAN plus IM 130x85 adquirido junto ao microsc pio, enquanto a fonte de ilumina o estruturada deve ser acoplada a uma das chamadas portas infinitas do microsc pio, de modo an logo ao realizado com fontes de luz convencionais. O desenvolvimento deste m dulo foi inspirado pelo trabalho (Hannebelle et al. 2024), no qual um sistema de ilumina o estruturada de baixo custo foi desenvolvido visando atender a diferentes microsc pios de fluoresc ncia j existentes.

### 2.2.3.     M dulo criog nico [\[RRG19\]](#_msocom_19) para o microsc pio DMi8

Este m dulo consiste em uma c mara de v cuo posicionada sobre o est gio de amostras do microsc pio Leica DMi8 (Figura 16). Uma reentr ncia na c mara de v cuo permite que a lente objetiva se aproxime da amostra contida em grades TEM (ou capilares), que estar o posicionadas em um pino do m dulo criog nico do DMi8[\[RRG20\]](#_msocom_20) . Este pino inteiro est em contato com um pequeno *cryocooler* por meio de um link t rmico, e assim toda a pot ncia extra da do sistema para que a amostra se mantenha vitrificada. Uma janela ptica posicionada entre a lente objetiva e o suporte de amostra; por meio dela a luz pode ser transmitida, mantendo-se o v cuo da c mara. Por fim, um sistema de transfer ncia de amostras utilizado para o carregamento dos suportes de amostras, devendo tamb m atuar como interface de conten o biol gica, isolando as amostras do ambiente. Ainda, ele deve ser capaz de manter as amostras vitrificadas e possuir uma estrat gia de descontamina o pr pria compat vel com as diretrizes de descontamina o j estabelecidas para todo o fluxo de opera o da esta o experimental SIBIPIRUNA.

Um prot tipo deste sistema tamb m ser desenvolvido, como parte do esfor o de valida o de conceitos de prepara o, transfer ncia e conserva o da amostra de todo o fluxo de trabalho criog nico da esta o experimental SIBIPIRUNA. Um primeiro candidato a *cryocooler* o modelo TC2570, fabricado pela chinesa *Lihan Cryogenics*, capaz de extrair 500 mW a uma temperatura de 77 K, mas sua confirma o depende ainda de um modelo t rmico mais detalhado do sistema.

**![Interface gr fica do usu rio
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image017.gif)**

Figura 16 - Conceito para o M dulo Criog nico do DMi8[\[RRG21\]](#_msocom_21) : (1) est gio de amostras do DMi8; (2) lente objetiva; (3) janela ptica; (4) c mara de v cuo; (5) sistema de transfer ncia de amostra; (6) grades TEM; (7) suporte de amostras; (8) link t rmico; e (9) cryocooler.

### 2.2.4.     M dulo de ilumina o estruturada para microsc pio DMi8

Dentre os desafios envolvidos na constru o de um microsc pio de super-resolu o por ilumina o estruturada, destaca-se a elabora o do tra ado ptico. Por ser uma t cnica relativamente nova, a literatura corrente n o apresenta com clareza todos os requisitos necess rios para que se atinja a resolu o lateral de 100 nm e axial de 300 nm. Al m disso, diversos tra ados foram propostos por diferentes autores, que empregam diferentes componentes pticos para a aquisi o das imagens de super-resolu o. Deste modo, a constru o de prot tipos, aliada a simula es num ricas utilizando *softwares* *de ray tracing* como o ANSYS ZEMAX, mostram-se como ferramentas valiosas para um melhor delineamento das decis es de projeto a serem adotadas.

Ademais, o desenvolvimento de prot tipos permite a obten o de dados preliminares que podem ser utilizados para a valida o e otimiza o do fluxo de trabalho de reconstru o e correla o de imagens biol gicas, haja vista que o desenvolvimento destes algoritmos representa uma outra parcela do desafio de se desenvolver um microsc pio de super-resolu o por imagem estruturada.

O openSIM (Hannebelle et al., 2024) um m dulo de extens o desenvolvido para proporcionar ilumina o linearmente estruturada a microsc pios de fluoresc ncia convencionais (Figura ), permitindo que estes sejam usados para a aquisi o de imagens de super-resolu o com at o dobro da resolu o lateral original. O m dulo foi projetado e documentado como um instrumento com componentes mec nicos, pticos, eletr nicos e computacionais abertos, o que facilita sua replica o e modifica o por outros pesquisadores. Em seu design original, a luz colimada e polarizada de tr s LEDs com cores distintas ilumina um modulador espacial de luz (SLM), com o qual gerado o padr o a ser projetado na amostra. Para isso, a sa da do m dulo acoplada porta de ilumina o do microsc pio de fluoresc ncia, substituindo sua fonte de ilumina o por um padr o linear de excita o, que interage com a amostra para gerar as franjas de moir (Figura 17).

![Diagrama
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image018.gif)

Figura 17 - a) Representa o do m dulo OpenSIM conectado porta de ilumina o de um microsc pio ptico invertido gen rico. b) Representa o dos principais componentes pticos, el tricos e mec nicos do projeto original do OpenSIM: 1) LED. 2) Espelho. 3) Lente colimadora. 4) Espelho dicroico. 5) Polarizador linear. 6) Divisor de feixe polarizado. 7) Modulador espacial de luz. 8) Tube lens. 9) Placa de driver do LED. 10) Placa de driver do SLM. 11) Placa de interconex o. 12) Est gio de transla o linear. 13) Adaptador para a porta de ilumina o. c) Diagrama dos componentes pticos do OpenSIM.

Para dobrar a resolu o lateral de maneira quase isotr pica com o openSIM, o padr o linear precisa ser incidido em tr s fases e tr s ngulos diferentes, resultando em nove imagens com padr es linearmente distintos. As imagens resultantes s o utilizadas para solucionar um conjunto de equa es lineares, a partir das quais feita a separa o entre os componentes abaixo e acima do limite de resolu o da objetiva para a reconstru o da imagem final de super-resolu o.

Uma interface em software aberto re ne ferramentas de controle dos padr es de ilumina o; da intensidade de ilumina o de cada LED; do ganho, tempo de exposi o e captura de imagens pela c mera; e do dissipador de temperatura. Al m disso, um dispositivo para aquisi o de dados (DAQ) empregado para o cabeamento entre os elementos do sistema, como o OpenSIM, a c mera de captura, o computador, e o est gio do microsc pio para aquisi es volum tricas automatizadas.

Para avaliar a performance do m dulo, os autores imagearam esferas fluorescentes com di metro de 100 nm, com as quais obtiveram imagens reconstru das com 169 nm de resolu o, comparada resolu o original de 294 nm. Dessa forma, foi poss vel aumentar a resolu o das esferas em aproximadamente 1,74x. Os autores tamb m demonstraram sua aplica o em diferentes amostras biol gicas, como organoides intestinais de camundongos, embri es de *zebrafish*, a distribui o de *Mycobacterium smegmatis* em macr fagos durante um processo infeccioso, e a presen a de tubulina em c lulas endoteliais pulmonares fixadas de bovinos. Complementarmente, os autores demonstraram a capacidade de acoplar o m dulo do OpenSIM a um microsc pio de varredura por sonda, com o qual conseguiram correlacionar a topografia de uma c lula com a fluoresc ncia de seu citoesqueleto.

O OpenSIM apresenta como principal distin o o m todo de produ o dos padr es de interfer ncia. Enquanto microsc pios SIM convencionais utilizam fontes de luz coerentes associadas a um SLM operando como uma grade de difra o, os autores do OpenSIM propuseram a ado o de uma fonte de luz incoerente e da proje o do padr o de interfer ncia na amostra. Quando o SLM opera como uma grade de difra o, a luz incidida espalhada em diferentes ordens de difra o, que posteriormente s o conduzidas at a amostra para que interfiram entre si e produzam um padr o de interfer ncia linear.

Na concep o original do OpenSIM, os autores concentraram-se em desenvolver um sistema compacto e barato que fosse suficientemente simples para que outros pesquisadores pudessem replic -lo sem dificuldades. Por esse motivo, aspectos como o custo-benef cio, disponibilidade de pe as, dimens es reduzidas e seguran a de manuseio foram tidos como priorit rios para o projeto. Estes mesmos pontos, por m, acabam impondo restri es ao desempenho do m dulo em m ltiplos aspectos, o que impacta diretamente na qualidade das imagens reconstru das e na resolu o m xima obtida.

Como a estrutura do m dulo original baseada em diversas pe as impressas com filamento PLA em impressoras comerciais 3D, o correto alinhamento dos componentes pticos pode se tornar um problema, dado que esta t cnica de manufatura apresenta precis o inferior quando comparado com outros processos de fabrica o, como a usinagem das pe as.

Outro ponto de aten o est relacionado ao conceito de ilumina o empregado. Como LEDs s o fontes de luz pouco diretivas, os f tons se espalham em uma regi o, limitando sua aplica o direta em contextos em que a intensidade luminosa relevante. Deste modo, apesar de a combina o de LEDs em free-space apresentar um baixo custo, as perdas de pot ncia no layout s o significativas. Como consequ ncia, para garantir uma intensidade luminosa suficiente na amostra, LEDs de alta pot ncia foram utilizados pelos autores, gerando como subproduto uma carga t rmica consider vel em componentes pticos subjacentes, haja vista que estes LEDs dissipam muita pot ncia na forma de calor.

Para a reconstru o das imagens, os autores utilizaram o software SIMToolbox, uma ferramenta em c digo aberto desenvolvida para MATLAB (Kř ek et al. 2016). O algoritmo utilizado para a reconstru o pelo software baseia-se no m todo cl ssico de Heintzmann-Gustafsson, que defasado com rela o ao estado da arte para reconstru es de imagens com ilumina o estruturada. Algoritmos mais recentes possuem otimiza es em caracter sticas-chave n o implementadas no SIMToolbox, como estimativas mais precisas dos par metros de ilumina o; melhor supress o da emiss o de fundo; diminui o do tempo de reconstru o; aumento da m xima resolu o axial p s-reconstru o; e implementa o de filtros notch para minimiza o de artefatos de Gibbs. Quando combinados, esses algoritmos s o capazes de contornar grande parte das defici ncias do SIM frente a outras t cnicas de super-resolu o.

Como contorno s limita es do SIMToolbox, prop e-se um fluxograma de reconstru o (Figura 18) que una aspectos desej veis de diferentes algoritmos modernos, a partir do qual se espera obter imagens reconstru das de alta qualidade com pouco tempo de aquisi o. Inicialmente, o usu rio dever selecionar uma regi o de interesse (ROI) utilizando o modo de fluoresc ncia convencional do microsc pio. Selecionada a ROI, ser feita a aquisi o das imagens brutas com os diferentes padr es de ilumina o no plano focal selecionado. As imagens brutas ser o processadas para remo o da emiss o do fundo, e as imagens resultantes ser o usadas para reconstru o bidimensional com um algoritmo otimizado para o tempo de execu o. Se a ROI selecionada n o for apropriada para os interesses do usu rio, ele deve retornar para selecionar uma nova. Caso contr rio, prossegue-se para a reconstru o em alta qualidade do plano focal da ROI. Se o resultado apresentar artefatos de reconstru o, o usu rio dever seguir um manual para identifica o do tipo de artefato no espectro da imagem e quais par metros da reconstru o devem ser alterados para corrigi-los. Uma vez que a imagem reconstru da esteja sem artefatos identificados pelas ferramentas de diagn stico, prossegue-se com a aquisi o volum trica das imagens brutas da ROI. Feita a aquisi o volum trica, o usu rio deve ent o selecionar uma nova ROI para recome ar o fluxo de aquisi o e reconstru o. Em segundo plano, ocorre a reconstru o em alta qualidade do volume, utilizando os par metros previamente otimizados pelo pr prio usu rio. O volume reconstru do, ent o, submetido a uma rede neural capaz de corrigir a anisotropia axial (Li et al. 2023). Uma vez que o prot tipo modificado do OpenSIM n o conta com secionamento ptico, necess rio executar a etapa de supress o de fundo para cada uma das imagens brutas do volume. No entanto, como a remo o da emiss o de fundo j feita pelo secionamento ptico na reconstru o volum trica, essa etapa n o ser necess ria no microsc pio com tr s feixes (3D-SIM).

Os tempos de execu o para cada etapa s o dependentes da unidade de processamento dispon vel para o microsc pio. Como exemplo, testes preliminares indicam que a reconstru o em tempo real ocorre na ordem de milissegundos quando executada na unidade de processamento gr fico (GPU) de um computador pessoal.

![](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image019.gif)[\[GAdS22\]](#_msocom_22) 

Figura 18 - Fluxograma com as diferentes etapas propostas para a reconstru o de uma aquisi o volum trica em super-resolu o.

Dentre as modifica es propostas para o m dulo de imagem estruturada, pode-se citar a substitui o do *tube lens* especificado originalmente pelo modelo TTL-200-A fabricado pela Thorlabs. Esta modifica o se deu pela necessidade de compatibilizar o comprimento focal do *tube lens* com o comprimento focal padr o f = 200 mm utilizado pelos microsc pios fabricados pela Leica, para que nenhuma magnifica o adicional seja introduzida no sistema. Tamb m foi selecionado um adaptador de porta infinita compat vel com o microsc pio Leica DMi8 adquirido previamente.[\[GAdS23\]](#_msocom_23) 

Conforme apresentado nos par grafos anteriores, o conceito de ilumina o originalmente proposto por Hannebelle et al. (2024) apresenta baixa modularidade e manuten o dif cil, haja vista que a substitui o de qualquer componente ptico implica no desacoplamento do m dulo e posterior desmontagem dele. Ademais, a presen a de fontes de luz com baixa efici ncia nas proximidades de componentes pticos induz dist rbios t rmicos que podem afetar a performance do sistema, provocando, por exemplo, o surgimento de aberra es do tipo *coma* devido ao deslocamento dos centros pticos. Assim, a solu o proposta consiste na segrega o dos componentes respons veis por produzir a ilumina o dos componentes respons veis por produzir uma imagem com padr es estruturados. A partir disso, deriva-se um novo conceito para o m dulo estruturador, onde uma fibra ptica se torna respons vel por transmitir a luz j condicionada at os componentes respons veis por gerar o padr o estruturado, conforme apresentado na Figura 19.

![A blue circle with black text
Description automatically generated](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image020.gif)

Figura 19 - Conceito geral da separa o dos componentes de ilumina o e do gerador do padr o estruturado.

Assim, tem-se um novo conceito para o layout ptico do gerador do padr o estruturado (Figura 20). Quando comparado ao layout original apresentado na Figura 17, percebe-se que a solu o apresenta menos componentes, haja vista que nesta abordagem a fonte de luz tratada como um desenvolvimento independente. Com esta modifica o espera-se minimizar as perdas de pot ncia ao longo do layout ptico e o calor dissipado no sistema.

![Diagrama
Descri  o gerada automaticamente](20240404%20-%20Prot tipo%20Porta%20Amostras%20Cryo%20-%20CDR_files/image021.gif)

Figura 20 - Layout ptico simplificado do gerador de padr o estruturado modificado.

Nesta nova proposta, a fibra ptica conectada ao gerador de padr o estruturado por meio de um conector do tipo SMA. A luz ent o se propaga em espa o aberto at ser colimada por uma lente, de onde segue at o polarizador linear. Deste ponto em diante, o funcionamento do layout se mant m semelhante ao proposto pelos autores (Hannebelle et al. 2024). Al m das modifica es no tra ado ptico, tamb m s o propostas modifica es na arquitetura optomec nica do sistema, substituindo-se o *frame* monol tico impresso em 3D por outro tipo de estrutura. Em um primeiro momento, espera-se que os elementos pticos sejam montados em mesa ptica com postes e frames ajust veis, para posterior integra o em uma estrutura optomec nica definitiva, quando o projeto apresentar um grau de maturidade maior.

Com o prot tipo modificado e acoplado ao Leica DMi8, espera-se que seja poss vel reconstruir imagens de amostras biol gicas BSL1 com espessura de at 10 m e at o dobro da resolu o original da objetiva, o que ser feito em at 4 cores com os padr es de ilumina o em 3 ngulos e 3 fases. Os comprimentos de onda nominais escolhidos ser o 405 nm, 488 nm, 561 nm e 640 nm, por se tratarem de comprimentos de excita o tradicionais para os fluor foros utilizados na microscopia de fluoresc ncia de amostras biol gicas. As aquisi es ser o feitas em temperatura ambiente e a press o atmosf rica, com objetivas secas com abertura num rica de 0,75, magnifica o de 100x e dist ncia de trabalho de 3,5 mm.

As imagens brutas obtidas a partir do microsc pio permitir o avaliar a utilidade do fluxograma para reconstru o definido anteriormente (Figura ), tendo como crit rios de avalia o o tempo de reconstru o nas diferentes etapas, a incid ncia de artefatos ap s otimiza o dos par metros, e a resolu o m xima obtida em amostras biol gicas. Al m disso, pretende-se estabelecer um manual de calibra o, diagn stico e corre o de erros, que ser baseado no imageamento de esferas tetrafluorescentes com 100 nm de di metro (TetraSpeck, Thermofisher) e de l minas fluorescentes de microscopia (FSK5 slide set, Thorlabs). Ferramentas gratuitas para an lise das aquisi es brutas e ap s reconstru o (NanoJ-SQUIRREL, SIMcheck) ser o usadas para quantificar os artefatos resultantes e avaliar a confiabilidade das reconstru es.

As reconstru es volum tricas por fluoresc ncia no vis vel justificar o o desenvolvimento de um fluxo de trabalho para correla o com as medidas-teste de tomografia de raios-X moles (SXT) feitas no Prot tipo ptico da linha de Luz SIBIPIRUNA, descrito no CDR tica de Lentes e Guias de Onda. Para isso, ser necess rio empregar algoritmos de registro entre imagens de fluoresc ncia no vis vel e imagens de microscopia eletr nica de varredura, modificando-os para se adequarem s imagens de SXT. Ademais, um protocolo descrevendo as etapas utilizadas no registro entre o cryoSIM e os resultados da linha de luz B24, do Diamond Light Source, ser usado como guia para o desenvolvimento do algoritmo (Vyas et al. 2021).

Com os resultados preliminares da reconstru o, ser poss vel verificar se fontes incoerentes de luz resultam em uma profundidade de ilumina o suficientemente grande para a estimativa adequada dos par metros de ilumina o. Em caso negativo, o prot tipo ter que ser modificado para utilizar lasers como fonte de ilumina o, sendo necess rio especificar a pot ncia utilizada, as fibras para transportar a luz, e o m todo que ser utilizado para redu o do ru do de coer ncia do feixe.

Os resultados obtidos com o prot tipo permitir o estimar a viabilidade t cnica do desenvolvimento de um m dulo criog nico para o microsc pio Leica DMi8, o que depender n o apenas da qualidade do m dulo de ilumina o estruturada por si s , mas tamb m de caracter sticas inerentes ao pr prio microsc pio adquirido, como a estabilidade mec nica de seu est gio e a facilidade de sincronizar sua c mera com o SLM. Nessa situa o, n o ser mais necess rio desenvolver um microsc pio separado, o que corresponderia concretiza o do Cen rio 2 mapeado anteriormente (Figura 14). No entanto, ser preciso modificar o m dulo estruturador de luz, para que ele passe a operar com tr s feixes e em modo de interfer ncia, al m de ser preciso desenvolver um m dulo criog nico compat vel com o microsc pio.

  

# 3.    Refer ncias

Bleck, C.k.e., A. Merz, M.g. Gutierrez, P. Walther, J. Dubochet, B. Zuber, e G. Griffiths. 2010\. Comparison of Different Methods for Thin Section EM Analysis of Mycobacterium Smegmatis . *Journal of Microscopy* 237 (1): 23 38. https://doi.org/10.1111/j.1365-2818.2009.03299.x.

Chatzimpinou, Anthoula, Charlotta Funaya, David Rogers, Stephen O Connor, Sergey Kapishnikov, Paul Sheridan, Kenneth Fahy, e Venera Weinhardt. 2023. Dehydration as Alternative Sample Preparation for Soft X-Ray Tomography . *Journal of Microscopy* 291 (3): 248 55. https://doi.org/10.1111/jmi.13214.

Chlanda, Petr, Maria Alejandra Carbajal, Marek Cyrklaff, Gareth Griffiths, e Jacomine Krijnse-Locker. 2009. Membrane Rupture Generates Single Open Membrane Sheets during Vaccinia Virus Assembly . *Cell Host & Microbe* 6 (1): 81 90. https://doi.org/10.1016/j.chom.2009.05.021.

Cryogenium . s.d. Linkam Scientific. Acedido a 4 de abril de 2024. https://www.linkam.co.uk/cryogenium.

Cryosol-World. s.d. Technology . CryoSol-World. Acedido a 4 de abril de 2024. https://cryosol-world.com/vitrojet-solutions/technology/.

EM GP2 Automatic Plunge Freezing . s.d. Acedido a 4 de abril de 2024. https://www.leica-microsystems.com/products/sample-preparation-for-electron-microscopy/p/leica-em-gp2/.

Hannebelle, M lanie T. M., Esther Raeth, Samuel M. Leitao, Tom Luke , Jakub Posp il, Chiara Toniolo, Olivier F. Venzin, et al. 2024. Open-Source Microscope Add-on for Structured Illumination Microscopy . *Nature Communications* 15 (1): 1550. https://doi.org/10.1038/s41467-024-45567-7.

Kř ek, Pavel, Tom Luke , Martin Ovesn , Karel Fliegel, e Guy M. Hagen. 2016. SIMToolbox: a MATLAB toolbox for structured illumination fluorescence microscopy . *Bioinformatics* 32 (2): 318 20. https://doi.org/10.1093/bioinformatics/btv576.

Le Gros, M. A., G. McDermott, B. P. Cinquin, E. A. Smith, M. Do, W. L. Chao, P. P. Naulleau, e C. A. Larabell. 2014\. Biological Soft X-Ray Tomography on Beamline 2.1 at the Advanced Light Source . *Journal of Synchrotron Radiation* 21 (6): 1370 77. https://doi.org/10.1107/S1600577514015033.

Li, Shuoguo, Xing Jia, Tongxin Niu, Xiaoyun Zhang, Chen Qi, Wei Xu, Hongyu Deng, Fei Sun, e Gang Ji. 2023. HOPE-SIM, a cryo-structured illumination fluorescence microscopy system for accurately targeted cryo-electron tomography . *Communications Biology* 6 (abril): 474. https://doi.org/10.1038/s42003-023-04850-x.

Li, Xuesong, Yicong Wu, Yijun Su, Ivan Rey-Suarez, Claudia Matthaeus, Taylor B. Updegrove, Zhuang Wei, et al. 2023. Three-Dimensional Structured Illumination Microscopy with Enhanced Axial Resolution . *Nature Biotechnology* 41 (9): 1307 19. https://doi.org/10.1038/s41587-022-01651-1.

Loconte, Valentina, Jian-Hua Chen, Mirko Cortese, Axel Ekman, Mark A. Le Gros, Carolyn Larabell, Ralf Bartenschlager, e Venera Weinhardt. 2021. Using Soft X-Ray Tomography for Rapid Whole-Cell Quantitative Imaging of SARS-CoV-2-Infected Cells . *Cell Reports Methods* 1 (7). https://doi.org/10.1016/j.crmeth.2021.100117.

Martens, Garnet, Elaine C. Humphrey, Lionel G. Harrison, Begonia Silva-Moreno, Juan Ausi , e Harold E. Kasinsky. 2009. High-Pressure Freezing of Spermiogenic Nuclei Supports a Dynamic Chromatin Model for the Histone-to-Protamine Transition . *Journal of Cellular Biochemistry* 108 (6): 1399 1409. https://doi.org/10.1002/jcb.22373.

Okolo, Chidinma A., Ilias Kounatidis, Johannes Groen, Kamal L. Nahas, Stefan Balint, Thomas M. Fish, Mohamed A. Koronfel, et al. 2021. Sample Preparation Strategies for Efficient Correlation of 3D SIM and Soft X-Ray Tomography Data at Cryogenic Temperatures . *Nature Protocols* 16 (6): 2851 85. https://doi.org/10.1038/s41596-021-00522-4.

Phillips, Michael A., Maria Harkiolaki, David Miguel Susano Pinto, Richard M. Parton, Ana Palanca, Manuel Garcia-Moreno, Ilias Kounatidis, et al. 2020. CryoSIM: Super-Resolution 3D Structured Illumination Cryogenic Fluorescence Microscopy for Correlated Ultrastructural Imaging . *Optica* 7 (7): 802 12. https://doi.org/10.1364/OPTICA.393203.

Vitrobot Mark IV System - BR . s.d. Acedido a 4 de abril de 2024. https://www.thermofisher.com/br/en/home/electron-microscopy/products/sample-preparation-equipment-em/vitrobot/instruments/vitrobot-mark-iv.html.

Vyas, Nina, Stephan Kunne, Thomas M. Fish, Ian M. Dobbie, Maria Harkiolaki, e Perrine Paul-Gilloteaux. 2021. Protocol for image registration of correlative soft X-ray tomography and super-resolution structured illumination microscopy images . *STAR Protocols* 2 (2): 100529. https://doi.org/10.1016/j.xpro.2021.100529.

---

 [\[RR1\]](#_msoanchor_1)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br), vamos deixar a data retroativa.

 [\[RR2\]](#_msoanchor_2)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br), importante sempre indicar a moeda, pois qualquer mal-entendido tem um impacto gigante. $ -> R$

 [\[RRG3\]](#_msoanchor_3)[@Francesco Rossi Lena](mailto:francesco.lena@lnls.br), senti falta de pelo menos uma tabela de especifica o, resumindo o que esse conceito capaz de oferecer (em termos de posicionamento e temperatura).

 [\[FRL4\]](#_msoanchor_4)Vou colocar os requisitos do cdr, que o conceito atende

 [\[RRG5\]](#_msoanchor_5)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br) e [@Francesco Rossi Lena](mailto:francesco.lena@lnls.br), realoquei esse par grafo aqui pra baixo, pois falta um tanto ainda pra entrarmos na fase de desenvolvimento, de fato. O Desenvolvimento fica para o PDR. Mas o que est escrito no par grafo continua v lido.

 [\[RRG6\]](#_msoanchor_6)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br), formalmente, a entrega do FDR e do TIP est em junho/25. Talvez a gente precise ajustar uns prazos.

 [\[RRG7\]](#_msoanchor_7)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br) e [@Francesco Rossi Lena](mailto:francesco.lena@lnls.br), estou sugerindo de padronizarmos suporte de amostras (para o equivalente grid + carpin, ou capilar), para tirar a promiscuidade/degeneresc ncia do termo porta-amostra. (O equivalente de holder.)

 [\[GA8\]](#_msoanchor_8)[@Francesco Rossi Lena](mailto:francesco.lena@lnls.br) pode confirmar se est certo essa cita o?

 [\[RRG9\]](#_msoanchor_9)[@Francesco Rossi Lena](mailto:francesco.lena@lnls.br) e [@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br), dei uma reformulada aqui, pois para mim pareceu que est vamos com foco total no jet. Mas acontece que estamos comprando uma s rie de coisas que s o plunge com o dinheiro desse prot tipo. O que acham?

 [\[RRG10\]](#_msoanchor_10)[@Gabriel Antunes de Souza](mailto:gabriel.souza@lnls.br), estou achando estranho a gente fazer refer ncias para o PDR da linha por dois motivos. Esse relat rio aqui, o CRD, deveria ter sido entregue em janeiro, muito antes do PDR da linha, para abril. E, outro ponto, que mencionamos a cita o ao PDR e depois explicamos tudo na sequ ncia. Ent o, fica parecendo que nem precisa da refer ncia.

 [\[RRG11\]](#_msoanchor_11)[@Michel Bernardino Machado](mailto:michel.machado@lnls.br), ele continua como um candidato? A sequ ncia do texto e a pr xima se o parecem apontar numa dire o diferente... Talvez possamos equalizar um pouco mais.

 [\[RRG12\]](#_msoanchor_12)[@Michel Bernardino Machado](mailto:michel.machado@lnls.br), onde est a amostra mesmo, depois de M3? N o tem uma indica o de sample, n ? Poder amos acrescentar.

 [\[RRG13\]](#_msoanchor_13)[@Michel Bernardino Machado](mailto:michel.machado@lnls.br), s o M1 e M2 e/ou FM1 e FM2?

 [\[MB14\]](#_msoanchor_14)FM1 e FM2 para ficar de acordo com a imagem.

 [\[RRG15\]](#_msoanchor_15)[@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br), onde na figura d a entender que a solu o final independente? Graficamente (largura ou cor de linha, etc), n o parece ter diferen a entre o esquema do cen rio 1 e dos outros 2, em que essa independ ncia aparentemente n o ocorre.

 [\[MO16\]](#_msoanchor_16)Modifiquei a figura para deixar mais claro quais exatamente s o os produtos resultantes em cada cen rio

 [\[RRG17\]](#_msoanchor_17)[@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br), achei essa parte dos cen rios um tanto confusa, tanto a imagem quando a descri o. Os tons de azul na figura n o me transmitiram a informa o de forma clara (prototipagem e solu o final?). Podemos indicar o DMi8 na imagem? O que estamos chamando aqui de "m dulo porta-amostras criog nico" e "m dulo de imagem estruturada", d pra correlacionar com imagens anteriores ou posteriores do relat rio? S consegui entender melhor depois de ler as se es seguintes e ver a figura 13.

Em particular, n o podemos usar aqui o nome "porta-amostra criog nico", pois esse e o tema principal do relat rio, e o nome foi tomado pelo sistema de amostras na linha de luz (se o 2). Precisamos batizar de outra coisa.

 [\[MO18\]](#_msoanchor_18)Modifiquei as cores para refletir melhor quais s o os componentes de desenvolvimento e quais s o os produtos finais. Uma flecha do tempo foi adicionada lateral para indicar a ordem prov vel na qual os componentes ser o desenvolvidos. Setas tracejadas indicam componentes que se baseiam parcialmente no prot tipo anterior, em vez de serem refinamentos do componente anterior. O m dulo de ilumina o estruturada corresponde ao prot tipo que se baseia no OpenSIM.  
Ainda preciso substituir o termo "porta-amostras criog nico" por um mais apropriado.

 [\[RRG19\]](#_msoanchor_19)Ajustar nome

 [\[RRG20\]](#_msoanchor_20)[@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br), resolvemos hoje chamar o holder de suporte de amostra, pra evitar confus es com outros termos.

 [\[RRG21\]](#_msoanchor_21)[@Michel Bernardino Machado](mailto:michel.machado@lnls.br) e [@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br) , renomear.

 [\[GAdS22\]](#_msoanchor_22)[@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br) cite a imagem no texto, por gentileza.

 [\[GAdS23\]](#_msoanchor_23)[@Mairon Oliveira de Lima](mailto:mairon.lima@lnls.br) qual o microsc pio adquirido?