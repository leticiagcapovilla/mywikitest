---
title: SIBIPIRUNA
description: Soft X-rays tomography beamline at Orion
published: 1
date: 2024-04-17T14:39:20.919Z
tags: 
editor: markdown
dateCreated: 2024-04-08T20:19:17.974Z
---

title:  
.  
.  
**Protótipos – Porta Amostras Criogênico**  
.  
*Conceptual Design Report (CDR)*

**Janeiro 2024**

**Intentionally Left Blank**

Lista de Autores

| AUTORES | GRUPO | CARGO |
| --- | --- | --- |
| Gabriel A. Souza | MEP | ADT |
| Mairon O. de Lima | MEP | Estagiário |
| Francesco R. Lena | MEP | ADT |
| Michel B. Machado | MEP | ADT |

Figura 1 - Missão e Capacidades da linha de luz SIBIPIRUNA

Aprovações

| **Aprovadores** | **Assinatura** |
| --- | --- |
|     |     |
| **Renan R. Geraldes** |     |
| ***MEP, LNLS*** |     |
|     |     |
|     |     |

Figura 2 - Diagrama de arquitetura do Porta-Amostras Criogênico, especificando os componentes, subcomponentes, funções e informações/matéria/energia trocada entre as funções

# Table of Contents \[table-of-contents\]

\[1. Introdução [6](#introdu%C3%A7%C3%A3o)\](#introdução)

\[Orçamento: [11](#_Toc164235204)\](#\_Toc164235204)

\[1.1. Estágios do Ciclo de Vida: [11](#_Toc164235205)\](#\_Toc164235205)

\[1.1.1. Conceitual: [11](#_Toc164235206)\](#\_Toc164235206)

\[1.1.2. Desenvolvimento: [17](#_Toc164235207)\](#\_Toc164235207)

\[1.1.3. Produção: [17](#_Toc164235208)\](#\_Toc164235208)

\[1.1.4. Utilização e Suporte [18](#_Toc164235209)\](#\_Toc164235209)

\[1.1.5. Desfazimento: [18](#_Toc164235210)\](#\_Toc164235210)

\[1.2. Conclusão [19](#conclus%C3%A3o)\](#conclusão)

\[2. Estudos de viabilidade e Sistemas Interoperacionais [20](#estudos-de-viabilidade-e-sistemas-interoperacionais)\](#estudos-de-viabilidade-e-sistemas-interoperacionais)

\[2.1. Fluxo e Sistemas de Preparo de Amostras [20](#fluxo-e-sistemas-de-preparo-de-amostras)\](#fluxo-e-sistemas-de-preparo-de-amostras)

\[2.1.1. Otimização do processo de vitrificação e manipulação de amostras [25](#otimiza%C3%A7%C3%A3o-do-processo-de-vitrifica%C3%A7%C3%A3o-e-manipula%C3%A7%C3%A3o-de-amostras)\](#otimização-do-processo-de-vitrificação-e-manipulação-de-amostras)

\[2.2. Sistema de Microscopia de Luz Visível Fluorescente Criogênico [27](#sistema-de-microscopia-de-luz-vis%C3%ADvel-fluorescente-criog%C3%AAnico)\](#sistema-de-microscopia-de-luz-visível-fluorescente-criogênico)

\[2.2.1. Introdução [27](#introdu%C3%A7%C3%A3o-1)\](#introdução-1)

\[2.2.2. Desenvolvimento do microscópio de super-resolução criogênico da SIBIPIRUNA [31](#desenvolvimento-do-microsc%C3%B3pio-de-super-resolu%C3%A7%C3%A3o-criog%C3%AAnico-da-sibipiruna)\](#desenvolvimento-do-microscópio-de-super-resolução-criogênico-da-sibipiruna)

\[2.2.3. Módulo criogênico para o microscópio DMi8 [37](#m%C3%B3dulo-criog%C3%AAnico-para-o-microsc%C3%B3pio-dmi8)\](#módulo-criogênico-para-o-microscópio-dmi8)

\[2.2.4. Módulo de iluminação estruturada para microscópio DMi8 [38](#m%C3%B3dulo-de-ilumina%C3%A7%C3%A3o-estruturada-para-microsc%C3%B3pio-dmi8)\](#módulo-de-iluminação-estruturada-para-microscópio-dmi8)

\[3. Referências [50](#refer%C3%AAncias)\](#referências)

Acrônimos

|     |     |
| --- | --- |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

Figura 3 – Diagrama de arquitetura e capacidade principal da linha de luz SIBIPIRUNA

Abreviações

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

Tabela 1 – Orçamento para o SoI

# Introdução

No contexto do Orion, alguns objetivos científicos foram criados, sendo um deles o de gerar imagens 3D com resolução nanométrica de células ex-vivo infectadas com agentes de nível 4 de biossegurança (BSL4) em estado quase nativo. Para isso a linha de luz SIBIPIRUNA foi criada, possuindo como capacidade fundamental a utilização de raios-X moles (*soft X-rays*) para gerar tomografia 3D de células isoladas. Esta capacidade necessariamente demanda que a célula esteja em estado criogênico, assim possibilitando que a célula tanto mantenha sua geometria quanto resista às doses de radiação dos raios-X ao longo das medidas. Além disso, com o intuito de ampliar as capacidades científicas do instrumento com um maior volume de informações das características da célula, concluiu-se ser necessário complementar as imagens de raios-X com uma técnica de imagem correlativa, criando-se assim uma plataforma de microscopia fluorescente de luz visível e tomografia de raios-X (CLXT do inglês *correlative light and X-ray tomography*). Dessa forma, a técnica de microscopia fluorescente também poderá ser empregada nas amostras estudadas na SIBIPIRUNA. A [Figura 1](#_Ref162968190) traz uma síntese do processo de análise e decisão do objetivo científico, onde é apresentado um diagrama de Missão e Capacidades, sendo que letra ’M’ define a Missão, que nesse caso representa o objetivo científico proposto, e ‘C’ as Capacidades a serem desempenhadas para que o objetivo da Missão seja alcançado. Além disso, a figura ainda apresenta uma estrutura hierárquica onde as Capacidades são derivadas, a partir da representação das letras ‘i’ e ‘e’ sobre as setas, que representam inclusão e extensão, respectivamente.

![A diagram of a diagram Description automatically generated](media/image3.png)

Para o desenvolvimento da Capacidade 1.2, foi identificada a necessidade de um componente chamado de *Manipulador* para posicionar a amostra, montada a um *Suporte de Amostra*, no foco da linha de luz e realizar o movimento de tomografia. Ainda, devido ao fato de a amostra estar em estado criogênico, a solução também demandará um *Sistema de Refrigeração* para gestão térmica com a função de manter a amostra em temperatura criogênica. A partir disso, optou-se por desenvolver um Sistema de Porta-Amostras Criogênico (PACRIO), que deverá possuir as funções descritas conforme [Figura 2](#_Ref163029232).

![A diagram of a computer Description automatically generated](media/image4.png)

Este documento irá abordar o status de desenvolvimento do componente PACRIO, bem como da Capacidade 1.1, visto que essa capacidade em associação com a 1.2 possibilita a Capacidade 1.1.1. Logo as operações de 1.1 e 1.2 deverão ser compatíveis entre si para que a 1.1.1 seja atingida. Estudos de viabilidade técnica dos métodos tradicionais para um *Sistema* *de* *Preparo de* *Amostras* com congelamento também serão apresentados neste documento, assim como um *Sistema de Transferência de Amostras*, uma vez que são pré-requisitos para a solução de porta-amostra (Figura 3).

![A screenshot of a computer Description automatically generated](media/image5.png)

Orçamento: as aquisições desse projeto vêm ocorrendo através do centro de custo referente ao PACRIO, com um montante total previsto de R$4.500.000,00. Na [Tabela 1](#_Ref162941169) são detalhados os montantes destinados às aquisições para cada um dos subsistemas e a data prevista para compra.

| PACRIO | Subsistema | Total Área | Fase A | Fase B | Fase C | Previsão de compra Fase A |
| --- | --- | --- | --- | --- | --- | --- |
|     | TXM Imaging | R$1.505.000,00 | R$559.500,00 | R$644.500,00 | R$301.000,00 | 01/03/2024 |
|     | Sample transfer | R$800.000,00 | R$240.000,00 | R$400.000,00 | R$160.000,00 |     |
|     | Correlative Imaging | R$885.000,00 | R$419.500,00 | R$288.500,00 | R$177.000,00 |     |
|     | Sample preparation | R$1.310.000,00 | R$393.000,00 | R$655.000,00 | R$262.000,00 |     |

Tabela 2 - Estágios do ciclo de vida do PACRIO

1.  Estágios do Ciclo de Vida: a tabela abaixo apresenta os estágios do ciclo de vida do PACRIO em uma escala temporal de trimestres. Nos capítulos posteriores serão descritas as atividades específicas para cada um desses estágios.

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

Figura 4 - Manipulador da amostra e Sistema Gerenciamento Térmico. A) vista isométrica da parte interna (exposta às amostras e ciclos de descontaminação mais frequentes), e B) vista isométrica da parte externa (em ambiente de vácuo separado da amostra).

1.  Conceitual: a etapa Conceitual consiste em estudos de avaliação das soluções, observando o entendimento do problema, requisitos e performance. Esta etapa se encerra a partir da aprovação de uma das soluções propostas, na qual será avaliado o conceito proposto para cinemática, dinâmica, gerenciamento térmico, minimização da exposição a área de descontaminação e viabilidade de manutenção.

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
    

A partir das definições básicas dos requisitos para o estágio do Manipulador de Amostras da SIBIPIRUNA, pode-se desenvolver um design conceitual. Prezando por diretrizes de isolamento da região da amostra em relação ao restante da linha de luz por questões de biossegurança, impondo simplificações nas interfaces mecânicas, e possibilitando o uso de tecnologias já validadas no Sirius/LNLS, o design atual aplica os conceitos de um *Tripod*, que utiliza cinemática paralela para movimentação cartesiana. Acoplado a ele, um estágio rotativo pode ser utilizado para o eixo de tomografia ([Figura 4](#_Ref163035977)).

![](media/image7.svg)

Conceitos de atuadores foram explorados para o estágio em questão. O nano-posicionador NSAU, da JPE, surgiu como um candidato promissor, devido ao seu curso de movimentação e força necessários, além de um design completamente hermético, selado em um encapsulamento metálico e equipado com um sistema de feedback de posicionamento (encoder) integrado. No design atual, é viável isolar totalmente os componentes eletrônicos de precisão e os sistemas de movimentação dos atuadores do ambiente de amostra, minimizando a exposição desses componentes a agentes de descontaminação que podem causar corrosão e desgaste.

Embora o sistema NSAU possua encoders internos, muitas vezes é preferível medir a posição o mais próximo possível da região de interesse. Assim, o conceito atual incorpora um sistema de interferometria para a metrologia na posição imediatamente antes da amostra, permitindo que os elementos interferométricos sejam posicionados fora do ambiente de amostra e transmitindo o sinal através de três janelas ópticas. A viabilidade deste conceito será explorada, com foco na validação dos cursos de movimentação e na aplicabilidade dos interferômetros em um sistema com um grande desvio angular natural.

Uma outra característica distintiva do design atual é a utilização de um acoplamento flexível para a transferência de calor por condução, conectando um criostato à região de interesse do estágio. Isso possibilita que o sistema de refrigeração, a saber, um criostato do tipo pulse tube (PT) ou Joule-Thomson (JT), também esteja localizado em outro ambiente. Para simplificar esse acoplamento e reduzir as cargas no sistema de rotação, um pequeno goniômetro operando em condições criogênicas pode ser empregado, sendo responsável unicamente pela movimentação do pino de amostras, que terá sua massa limitada a poucos gramas. Atualmente, existem diversas opções de goniômetros criogênicos que podem ser utilizados na aplicação, sendo o Attocube ANR240 e o JPE CSR1 opções candidatas ([Figura 5](#_Ref163036172)).

![A diagram of a machine Description automatically generated](media/image8.png)

Foi elaborado um modelo teórico do conceito apresentado na Figura 4, utilizando como base o esquema apresentado na [**\_Ref163647396**](#_Ref163647396). Neste esquemático é possível verificar uma abstração do conceito proposto, bem como os principais parâmetros geométricos que impactam a análise de viabilidade. Dentre eles, pode-se citar a distância dos atuadores com relação ao centro R e a altura do pino de amostras com relação ao ponto de articulação do mecanismo h.

A partir do conceito da [Figura 4](#_Ref163035977) foi elaborado um modelo para avaliação dos principais parâmetros geométricos ([Figura 6](#_Ref163661952)) e dinâmicos ([Figura 7](#_Ref163037086)) e cinemático ([Figura 8](#_Ref163719203)) do PACRIO. Na [Figura 6](#_Ref163661952) destaca-se os parâmetros de distância dos atuadores em relação ao centro (R) e a distância vertical entre pino de amostra e o seu ponto de articulação.

Além disso o modelo da [**\_Ref163037154**](#_Ref163037154) foi validado por simulação para determinação da tensão máxima nas *folded leaf springs*, que atuam como guias elásticos no mecanismo quando estas são deslocadas pelo atuador. Desta análise ([Figura 7](#_Ref163037086)), percebe-se que é factível o emprego de *folded leaf springs* de certas ligas de titânio e aço, que podem atingir tensão de escoamento até cerca de 900 – 1000 GPa.

![Interface gráfica do usuário Descrição gerada automaticamente](media/image9.png) ![Gráfico Descrição gerada automaticamente](media/image10.png)

Além da determinação da tensão máxima foi feito um estudo para a avaliação do volume que este conceito é capaz de varrer. A [**\_Ref163647748**](#_Ref163647748) apresenta uma esquematização deste volume com base no pino de amostras considerado no conceito apresentado na [Figura 4](#_Ref163035977).

Além dos estudos preliminares geométricos e dinâmicos do PACRIO, foi feito também um estudo cinemático com o intuito de se avaliar o volume que esse sistema é capaz de varrer. A [Figura 8](#_Ref163719203) apresenta uma esquematização deste volume com base no pino de amostras considerado no conceito apresentado na [Figura 4](#_Ref163035977).

![Diagrama Descrição gerada automaticamente](media/image11.png)

O perímetro da área hachurada apresentado na [Figura 8](#_Ref163719203) B representa a região mais externa à qual o estágio deve ser capaz de levar as amostras, assim, para avaliar o comportamento dos 3 atuadores, a curva que descreve este perímetro foi parametrizada em função de um ângulo θ, deste modo, para cada valor de θ tem se os valores de x e y que satisfazem a curva que descreve o perímetro. Os pontos descritos por x e y, por sua vez, são inseridos nas matrizes de cinemática possibilitando assim a determinação do movimento que cada atuador deve realizar, estes resultados são apresentados na [Figura 9](#_Ref163719790).

![Uma imagem contendo Gráfico Descrição gerada automaticamente](media/image12.png)

Figura 9 – Resultados obtidos por meio da análise cinemática preliminar. A) Curso necessário considerando a não superposição dos grids. B) Curso necessário considerando a superposição dos grids.

O cenário apresentado na [Figura 9](#_Ref163719790) A demonstra que o curso necessário excede o curso nominal dos atuadores para um espaçamento de 3,5 mm entre os grids, entretanto, ao considerar um espaçamento de 3 mm entre os grids, tem-se que o curso é suficiente ([Figura 9](#_Ref163719790) B). Outras modificações geométricas também têm impacto no curso necessário, porém não foram demonstradas pois este estudo se caracteriza apenas como uma avaliação preliminar, podendo ser estendido no futuro.

1.  Desenvolvimento: a etapa de desenvolvimento consiste na evolução de projeto detalhada do SoI. Esse estágio se encerra após uma validação analítica da dinâmica, cinemática, térmica e mecânica do PACRIO. Além disso, espera-se que os elementos e a operação do PACRIO sejam validados sob a ação de um agente de esterilização a ser utilizado na SIBIPIRUNA.
    
2.  Produção: o estágio de produção se inicia a partir da tradução de todas as informações do desenvolvimento em elementos do SoI. Durante essa etapa é esperada uma grande integração entre o MEP e o grupo de Gestão de Projetos, por ser uma fase com elevado número de aquisições através fornecedores externos. Além disso, é esperado um grande esforço por parte do MEP na tradução das especificações do desenvolvimento em documentação técnica para que fornecedores e grupos internos forneçam os componentes e serviços que atendam corretamente às especificações. Atividades relacionadas ao registro e gestão de problemas também são esperadas, e será necessário estimar um tempo de execução que leve em conta esses retrabalhos. Essa fase será encerrada quando o equipamento estiver montado, integrado e com todas as funções validadas em consonância com os parâmetros determinados na etapa de Desenvolvimento. Conforme a [Tabela 2 - Estágios do ciclo de vida do PACRIO](#_Ref163037455), a data prevista para início e conclusão da etapa de Produção será entre 01/2025 e 06/2025.
    
3.  Utilização e Suporte: o estágio de Utilização e Suporte é caracterizado por atividades nas quais o SoI entrará em operação em seu ambiente de uso, a partir disso o objetivo da missão será alcançado. Esse estágio se encerra quando o SoI gerar informações capazes de suportar a tomada de decisão sobre a viabilidade da sua operação em um contexto real da linha de luz SIBIPIRUNA. A tomada de decisão deverá possuir 2 possibilidades, sendo elas: otimizar o SoI mantendo seu conceito atual ou reprojetar o SoI a partir de um novo conceito.
    
4.  Desfazimento: O estágio de Desfazimento consiste das atividades planejadas para o encerramento do ciclo de vida do SoI. Para o PACRIO é esperado que, quando a sua utilidade seja esgotada, seus componentes sejam encaminhados para a estação experimental da linha SIBIPIRUNA, tanto quanto possível, ou desmontados e armazenados em condições adequadas, para que possam vir a ser reutilizados ou realocados em outros projetos.
    

## Conclusão

Pode-se observar que o projeto vem sendo conduzido a partir de uma análise sistêmica, onde espera-se uma integração entre os componentes da operação da linha de forma a garantir as capacidades da SIBIPIRUNA. Importante observar também que foram realizados estudos a partir de outras linhas de luz que possuem capacidades similares a da SIBIPIRUNA, além da utilização de conceitos já validados em projetos anteriores no LNLS. Isso possibilita que os grupos de engenharia do LNLS desenvolvam o projeto de forma mais assertiva e segura.

Atualmente o projeto possui como caminho crítico a validação de sua operação em um cenário de descontaminação. Cabe ressaltar que a etapa de Produção também pode ser crítica devido ao fluxo de aquisições de itens comerciais e serviços, que podem levar a atrasos que impactaram na evolução do projeto e consequentemente avanço sobre os estágios do ciclo de vida.

# Estudos de viabilidade e Sistemas Interoperacionais

A operação da SIBIPIRUNA envolve a interação entre diversos sistemas, e integrar essas interfaces é uma tarefa fundamental para garantir que todos os componentes possam ser desenvolvidos e operados em conformidade. Avaliando a operação do PACRIO, é possível identificar as dependências do sistema, sendo elas listadas abaixo:

-   Sistema de Preparo de Amostras: dado que a amostra será preparada e carregada em um suporte específico e este transferido para o PACRIO, identificou-se a necessidade de incluir o preparo de amostras nessa fase de prototipagem, cobrindo principalmente questões relacionadas à vitrificação adequada das amostras criogênicas e à otimização do fluxo de trabalho e da transferência da amostra entre os sistemas;
    
-   Sistema de Microscopia de Luz Visível Fluorescente Criogênico: a partir da capacidade 1.1.1 que determina que a SIBIPIRUNA seja capaz de gerar uma imagem CLXT, mostrou-se necessário também o desenvolvimento de um microscópio de fluorescência, de forma a garantir compatibilidade entre ele e o microscópio de raios-X da SIBIPIRUNA.
    

> A partir dessas demandas, frentes de trabalho paralelas e iterativas com PACRIO foram iniciadas, de forma a criar um cenário que atenda ao funcionamento desses diferentes sistemas. A seguir serão listadas as frentes de trabalho e nos capítulos posteriores seus status de desenvolvimento.

## Fluxo e Sistemas de Preparo de Amostras

A evolução da criomicroscopia, especialmente no contexto da microscopia de raios-X moles, marcou uma transição significativa na forma como os espécimes biológicos são preparados e analisados. Esse avanço centra-se no processo de vitrificação (ou criofixação), uma técnica que substitui os métodos tradicionais de fixação química usados na microscopia eletrônica. A vitrificação, como evidenciado pela pesquisa de criomicroscopia eletrônica, é fundamental para minimizar alterações morfológicas que poderiam comprometer a representatividade e a precisão dos resultados ([Figura 10](#_Ref163125092)). Além disso, a análise de amostras vitrificadas em estado criogênico não apenas garante sua excelente preservação, mas também proporciona uma estabilidade robusta contra danos por radiação na microscopia de raios-X moles. Consequentemente, esses avanços na criomicroscopia de espécimes biológicos têm relevância para o projeto SIBIPIRUNA, que pretende utilizar a criofixação para examinar amostras biológicas em condições que representem de perto seu estado natural, visando uma representação imparcial e detalhada das estruturas biológicas envolvidas nos processos de infecção viral.

![A collage of images of different types of cells Description automatically generated](media/image13.png)

Como apresentado na [Figura 11](#_Ref163117750), para a linha SIBIPIRUNA será empregado um fluxo de trabalho criogênico completo de células congeladas e hidratadas (vitrificadas) em substratos finos (e possivelmente também em capilares). Embora essa abordagem traga vantagens substanciais para a qualidade dos dados de tomografia e a abordagem científica, ela impõe desafios significativos para o projeto do fluxo de trabalho de preparação e manuseio de amostras. Isso se torna ainda mais complexo no contexto do ambiente BSL3/4, onde o uso de EPIs pode reduzir a mobilidade e destreza do usuário. Com isso em mente, o fluxo de trabalho atual está sendo projetado para minimizar o número de interações manuais do usuário com a amostra e reduzir a quantidade de equipamentos dentro da chamada "zona quente". Uma frente de trabalho específica foi criada para tratar do fluxo de trabalho para otimização do processo de vitrificação de células, que será abordado em detalhes no capítulo posterior.

![A computer screen shot of a diagram Description automatically generated](media/image14.png)

Além de a SIBIPIRUNA ser projetada para a capacidade de TXM confiável, segura e de alto desempenho, com uma integração direta com o ambiente BLS4 do Orion para imagens 3D de células infectadas com patógenos de nível 3 e 4, pesquisas e colaborações com especialistas de outros síncrotrons (como cientistas da linha B24, no Diamond Light Source) demonstraram que o uso de outras técnicas baseadas em microscopia de luz para imageamento de proteínas e pequenas moléculas fluorescentes acopladas ou intercaladas a organelas específicas podem fornecer um contexto celular adicional importante. Em certo sentido, as imagens de microscopia de fluorescência podem ajudar os cientistas a compreender melhor a localização e discernir estruturas subcelulares quando sobrepostas aos dados tomográficos de cryo-TXM, o que é feito a partir de técnicas matemáticas de registro de imagens. Com isso em mente, o atual fluxo de trabalho criogênico está sendo projetado para também incorporar um criomicroscópio de fluorescência 3D de super-resolução com base em um microscópio de iluminação estruturada (SIM).

### Otimização do processo de vitrificação e manipulação de amostras

Para otimização do processo de vitrificação, foi feita uma revisão bibliográfica a respeito dos métodos e equipamentos comerciais existentes para essa finalidade. Foram avaliados 4 equipamentos, sendo eles o Vitrobot da Thermo Fisher (“Vitrobot Mark IV System - BR”, s.d.), o EM GP2 da Leica (“EM GP2 Automatic Plunge Freezing”, s.d.), o Cryogenium da Linkam (“Cryogenium”, s.d.) e o VitroJet da CryoSol (Cryosol-World, s.d.). A [Tabela 3](#_Ref163122281) apresenta uma comparação entre eles.

|     | Deposição de amostra | Técnica de controle da espessura da amostra | Técnica de vitrificação |
| --- | --- | --- | --- |
| Vitrobot | Manual | Blotting com papel | Imersão (*plunge)* |
| EM GP2 | Manual | Blotting com papel | Imersão (*plunge)* |
| Cryogenium | Imersão automática | Sucção | Imersão (*plunge)* |
| Vitrojet | Deposição automática | Deposição precisa | Jato (*jet)* |

Figura 5 - Componentes principais do Manipulador de Amostra

Atualmente, o equipamento Vitrojet da CryoSol, o único da lista com vitrificação pelo processo recente e patenteado conhecido como *jet freezing*, apresenta-se como o candidato preferível para aplicação dentro do fluxo de trabalho da SIBIPIRUNA, por permitir um nível de automação maior e ser, em teoria, mais robusto e repetitivo em termos da qualidade de vitrificação. No entanto, o equipamento comercial foi originalmente desenvolvido para preparo das chamadas *single particles*, exigindo que customizações e validações sejam realizadas para células isoladas, que é o caso de interesse para a SIBIPIRUNA. Portanto, planeja-se a realização de colaborações técnicas, prototipagem e testes de validação para a tecnologia de *jet freezing* dentro das condições de contorno da SIBIPIRUNA no futuro próximo. Até lá, uma primeira rota mais conhecida, via *plunge freezing*, está sendo colocada em prática para validação antecipada do maior número possível de equipamentos e etapas do fluxo de trabalho ([Figura 11](#_Ref163117750)), a partir da qual primeiros estudos sobre a qualidade da vitrificação e dos passos de manipulação das amostras podem ser conduzidos.

## Sistema de Microscopia de Luz Visível Fluorescente Criogênico

### Introdução

Para viabilização de microscopia correlativa na linha de luz SIBIPIRUNA, será desenvolvido um criomicroscópio de fluorescência de super-resolução por iluminação estruturada (SIM), que deverá se adequar às necessidades específicas de biossegurança e robustez, além de ser projetado especificamente para o suporte de amostra da estação experimental. Esse microscópio será desenvolvido com base em outros designs ópticos já comprovados. Um dos designs inspiradores que fomentaram os estudos preliminares desse projeto foi o microscópio cryo-SIM B24, desenvolvido para a linha de luz B24 do Diamond Light Source ​(Phillips et al. 2020). Em uma visão geral, o sistema emprega quatro lasers de excitação de comprimentos de onda distintos — 405, 488, 561 e 647 nm — para gerar padrões de iluminação estruturada através de um modulador de luz espacial (SLM — *Spatial Light Modulator*). Esses padrões são o núcleo do SIM, pois induzem franjas de moiré que codificam informações da amostra que não seriam observadas em um microscópio convencional devido ao limite de difração da lente objetiva. Se o padrão de iluminação for conhecido, é possível utilizar métodos matemáticos de reconstrução para recuperar a estrutura original da amostra com até o dobro da resolução originalmente limitada pela objetiva.

![A diagram of a diagram of a diagram Description automatically generated with medium confidence](media/image15.jpeg)

Conforme descrito na publicação original e ilustrado na [Figura 12](#_Ref163115277), a luz dos lasers é direcionada e moldada através de uma série de componentes ópticos, incluindo lentes (L), aberturas (A), espelhos (M), pinholes (Ph) e espelhos dicroicos (D) para alcançar um controle preciso da iluminação. As aberturas A1 e A2 são especificamente utilizadas para refinar o perfil do feixe e eliminar difrações de ordem superior, respectivamente. Um rotacionador de polarização (PR – *Polarization Rotator*) alinha a polarização da luz com o eixo óptico do SLM, enquanto um telescópio formado pelas lentes L1 e L2 garante a expansão e o foco dos padrões de luz estruturada na amostra. A emissão de fluorescência é coletada por uma objetiva orientada perpendicularmente ao plano horizontal do arranjo óptico. Essa emissão é então refletida e dividida entre dois espelhos dicroicos (D1 e D2), isolando o sinal de fluorescência, que é posteriormente capturado pelas câmeras Cam1 e Cam2. Essas câmeras são sincronizadas com o SLM para capturar sequencialmente múltiplas imagens sob diferentes padrões de iluminação, que são posteriormente reconstruídas para formar uma imagem de super-resolução. A inclusão dos espelhos de desvio FM1 e FM2 proporciona flexibilidade no caminho da luz, permitindo caminhos de iluminação ou de imagem seletivos. O arranjo completo é projetado para otimizar o processo de SIM, melhorando a resolução e fornecendo informações detalhadas sobre as complexidades estruturais de espécimes biológicos em um nível abaixo do limite de difração da objetiva (Adaptado de Phillips et al. (2020)).

No design descrito, a amostra é imageada por uma objetiva alojada próxima a um estágio criogênico da Linkam (Modelo CMS196), isolada por uma atmosfera de vapor de nitrogênio seco. Embora este método seja confiável para a criopreservação de amostras, o design com o compartimento aberto do estágio pode inadvertidamente levar à deposição de umidade atmosférica nas amostras, resultando em contaminação por cristais de gelo – o que, de fato, pôde ser verificado experimentalmente por usuários do sistema. Isso é particularmente problemático, pois os cristais de gelo podem difratar a iluminação de raios-X moles incidente na microscopia de raios-X de transmissão (TXM), manifestando-se como manchas escuras de alto contraste que podem obscurecer detalhes da amostra. Além disso, o uso de um *dewar* de nitrogênio líquido diretamente acoplado ao estágio exige reabastecimentos frequentes, que podem induzir desvios posicionais devido a mudanças cíclicas da massa do sistema. Ademais, com a lente objetiva posicionada próxima à amostra, a condução e a convecção de calor através da atmosfera de nitrogênio podem resfriar os elementos iniciais da lente, levando à contração térmica e, possivelmente, a aberrações ópticas. Consequentemente, um dos principais desafios de design para o criomicroscópio de super-resolução por iluminação estruturada (SIM) da SIBIPIRUNA está na eliminação do estágio criogênico aberto e na redução da dependência de fluidos criogênicos que requerem reabastecimento.

Assim, o conceito previsto para o criomicroscópio SIM da SIBIPIRUNA ([Figura 13](#_Ref163115996)) integra um estágio criogênico dentro do vácuo e um criostato de ciclo fechado como mecanismo de resfriamento. Espera-se que esta configuração alivie os problemas mencionados, embora introduza desafios de engenharia substanciais. Estes incluem a necessidade de uma janela óptica para separar o ambiente de vácuo da amostra do entorno óptico e dos detectores, bem como a incorporação de uma interface ar-vácuo para o carregamento da amostra. Esta interface pode ter uma dupla finalidade, abordando também o desafio existente de desenvolver um sistema de carregamento de amostras para o TXM da estação experimental da SIBIPIRUNA.

![A diagram of a machine Description automatically generated](media/image16.png)

A equipe de design do LNLS também planeja aprimorar o design óptico para melhorar o desempenho na aquisição de imagens e facilitar o alinhamento e a manutenção de tais ópticas no ambiente BLS4. Isso inclui, mas não se limita, a (1) aumentar o campo de visão (FOV) do microscópio usando um SLM maior e um detector CMOS de maior resolução e maior tamanho; (2) incorporar estágios motorizados de inclinação e rotação para a maioria dos espelhos e elementos dicroicos, e estágios lineares para as lentes principais; (3) incorporar lasers acoplados por fibra que serão colocados fora do ambiente BLS4 para facilitar a manutenção e aumentar a durabilidade dos lasers, pois qualquer contato com produtos químicos de limpeza seria mitigado; e (4) introduzir ópticas de modulação de frente de onda para compensar distorções da topologia da amostra e geometria do substrato da amostra (por exemplo, grades TEM planas e capilares de vidro cilíndricos). Há também o estudo de viabilidade de se ter uma única câmera CMOS de alta eficiência para aquisição rápida em um único canal.

### Desenvolvimento do microscópio de super-resolução criogênico da SIBIPIRUNA

Com o avanço das pesquisas bibliográficas acerca dos microscópios de super-resolução por iluminação estruturada, foi possível constatar a presença de outros traçados ópticos que diferem daquele proposto por Phillips et al. (2020). A observação de todos estes trabalhos permitiu o levantamento de diretrizes gerais para o desenvolvimento deste projeto, bem como de requisitos de alto nível. Entretanto, alguns autores não são tão claros ao expor as decisões de projeto particulares de cada microscópio, tornando alguns aspectos incertos. Assim, para um completo delineamento das decisões de projeto a serem adotadas, é necessária a construção de protótipos e o desenvolvimento de modelos computacionais para posterior simulação em *softwares* como o ANSYS ZEMAX, cuja licença foi adquirida para realização deste projeto.

Dentre os desenvolvimentos em super-resolução por iluminação estruturada pela comunidade cientifica, destaca-se o OpenSIM (Hannebelle et al. 2024), por ser um acessório incorporável a microscópios de fluorescência comerciais, valendo-se dos estágios de amostras e sistemas de captura de imagem destes microscópios para produzir imagens SIM 2D com resolução abaixo de 200 nm. Além disso, o baixo custo do projeto e seu caráter *open source* o qualificam como uma ferramenta de prototipagem e validação das ideias propostas para o criomicroscópio SIM da SIBIPIRUNA. Deste modo, este conceito poderia ser utilizado nas etapas iniciais de prototipagem do criomicroscópio de super-resolução, ou até mesmo se tornar a solução definitiva para a produção de imagens de fluorescência 3D (3D-SIM) de amostras vitrificadas ao ser utilizado em conjunto a um porta-amostras criogênico montado sobre um microscópio invertido de fluorescência convencional, aos moldes do trabalho desenvolvido por Li et al. (2023).

A [Figura 1414](#_Ref163815533) sintetiza alguns dos possíveis cenários de desenvolvimento do microscópio de super-resolução criogênico da linha de luz SIBIPIRUNA. Nos diferentes cenários, o microscópio invertido de fluorescência Leica DMi8, adquirido para realização dos testes iniciais, atua como uma plataforma para o desenvolvimento de um microscópio de super-resolução por imagem estruturada, com a qual os diferentes protótipos e módulos podem ser incorporados para a validação de conceitos. O diferencial de cada cenário reside no produto final a ser entregue: no primeiro cenário, os protótipos de porta-amostras criogênico e de imagem estruturada são utilizados apenas para validação de conceitos, sendo o produto final um microscópio criogênico SIM totalmente independente compatível com amostras BSL3/4. No segundo cenário, esses protótipos são refinados, constituindo uma solução de criomicroscopia SIM integrada ao Leica DMi8. No terceiro cenário, seriam desenvolvidas duas soluções de criomicroscopia: uma integrada ao Leica DMi8 e um outro criomicroscópio SIM independente.

![](media/image18.svg)

Dado que o microscópio invertido Leica DMi8 é reconhecido como uma plataforma universal modular para diferentes técnicas de microscopia, o desenvolvimento de acessórios capazes de estender as suas capacidades originais é factível. Visando transformá-lo em um microscópio SIM criogênico, iniciou-se o desenvolvimento de um módulo de iluminação estruturada e de um módulo porta-amostras criogênico para o Leica DMi8. Uma representação desta implementação é apresentada na [Figura 1515](#_Ref163485397).

> ![Uma imagem contendo Seta Descrição gerada automaticamente](media/image19.png)

No conceito atual, o suporte de amostras deverá ser montado no estágio de amostras comercial SCAN plus IM 130x85 adquirido junto ao microscópio, enquanto a fonte de iluminação estruturada deve ser acoplada a uma das chamadas portas infinitas do microscópio, de modo análogo ao realizado com fontes de luz convencionais. O desenvolvimento deste módulo foi inspirado pelo trabalho (Hannebelle et al. 2024), no qual um sistema de iluminação estruturada de baixo custo foi desenvolvido visando atender a diferentes microscópios de fluorescência já existentes.

### Módulo criogênico para o microscópio DMi8

Este módulo consiste em uma câmara de vácuo posicionada sobre o estágio de amostras do microscópio Leica DMi8 ([Figura 1616](#_Ref163131694)). Uma reentrância na câmara de vácuo permite que a lente objetiva se aproxime da amostra contida em grades TEM (ou capilares), que estarão posicionadas em um pino do módulo criogênico do DMi8. Este pino inteiro está em contato com um pequeno *cryocooler* por meio de um link térmico, e assim toda a potência é extraída do sistema para que a amostra se mantenha vitrificada. Uma janela óptica é posicionada entre a lente objetiva e o suporte de amostra; por meio dela a luz pode ser transmitida, mantendo-se o vácuo da câmara. Por fim, um sistema de transferência de amostras é utilizado para o carregamento dos suportes de amostras, devendo também atuar como interface de contenção biológica, isolando as amostras do ambiente. Ainda, ele deve ser capaz de manter as amostras vitrificadas e possuir uma estratégia de descontaminação própria compatível com as diretrizes de descontaminação já estabelecidas para todo o fluxo de operação da estação experimental SIBIPIRUNA.

Um protótipo deste sistema também será desenvolvido, como parte do esforço de validação de conceitos de preparação, transferência e conservação da amostra de todo o fluxo de trabalho criogênico da estação experimental SIBIPIRUNA. Um primeiro candidato a *cryocooler* é o modelo TC2570, fabricado pela chinesa *Lihan Cryogenics*, capaz de extrair 500 mW a uma temperatura de 77 K, mas sua confirmação depende ainda de um modelo térmico mais detalhado do sistema.

> ![Interface gráfica do usuário Descrição gerada automaticamente](media/image20.png)

### Módulo de iluminação estruturada para microscópio DMi8

Dentre os desafios envolvidos na construção de um microscópio de super-resolução por iluminação estruturada, destaca-se a elaboração do traçado óptico. Por ser uma técnica relativamente nova, a literatura corrente não apresenta com clareza todos os requisitos necessários para que se atinja a resolução lateral de 100 nm e axial de 300 nm. Além disso, diversos traçados foram propostos por diferentes autores, que empregam diferentes componentes ópticos para a aquisição das imagens de super-resolução. Deste modo, a construção de protótipos, aliada a simulações numéricas utilizando *softwares* *de ray tracing* como o ANSYS ZEMAX, mostram-se como ferramentas valiosas para um melhor delineamento das decisões de projeto a serem adotadas.

Ademais, o desenvolvimento de protótipos permite a obtenção de dados preliminares que podem ser utilizados para a validação e otimização do fluxo de trabalho de reconstrução e correlação de imagens biológicas, haja vista que o desenvolvimento destes algoritmos representa uma outra parcela do desafio de se desenvolver um microscópio de super-resolução por imagem estruturada.

O openSIM (Hannebelle et al., 2024) é um módulo de extensão desenvolvido para proporcionar iluminação linearmente estruturada a microscópios de fluorescência convencionais ([Figura 1717](#_Ref163132016)), permitindo que estes sejam usados para a aquisição de imagens de super-resolução com até o dobro da resolução lateral original. O módulo foi projetado e documentado como um instrumento com componentes mecânicos, ópticos, eletrônicos e computacionais abertos, o que facilita sua replicação e modificação por outros pesquisadores. Em seu design original, a luz colimada e polarizada de três LEDs com cores distintas ilumina um modulador espacial de luz (SLM), com o qual é gerado o padrão a ser projetado na amostra. Para isso, a saída do módulo é acoplada à porta de iluminação do microscópio de fluorescência, substituindo sua fonte de iluminação por um padrão linear de excitação, que interage com a amostra para gerar as franjas de moiré ([Figura 1717](#_Ref163132016)).

![Diagrama Descrição gerada automaticamente](media/image21.png)

Para dobrar a resolução lateral de maneira quase isotrópica com o openSIM, o padrão linear precisa ser incidido em três fases e três ângulos diferentes, resultando em nove imagens com padrões linearmente distintos. As imagens resultantes são utilizadas para solucionar um conjunto de equações lineares, a partir das quais é feita a separação entre os componentes abaixo e acima do limite de resolução da objetiva para a reconstrução da imagem final de super-resolução.

Uma interface em software aberto reúne ferramentas de controle dos padrões de iluminação; da intensidade de iluminação de cada LED; do ganho, tempo de exposição e captura de imagens pela câmera; e do dissipador de temperatura. Além disso, um dispositivo para aquisição de dados (DAQ) é empregado para o cabeamento entre os elementos do sistema, como o OpenSIM, a câmera de captura, o computador, e o estágio do microscópio para aquisições volumétricas automatizadas.

Para avaliar a performance do módulo, os autores imagearam esferas fluorescentes com diâmetro de 100 nm, com as quais obtiveram imagens reconstruídas com 169 nm de resolução, comparada à resolução original de 294 nm. Dessa forma, foi possível aumentar a resolução das esferas em aproximadamente 1,74x. Os autores também demonstraram sua aplicação em diferentes amostras biológicas, como organoides intestinais de camundongos, embriões de *zebrafish*, a distribuição de *Mycobacterium smegmatis* em macrófagos durante um processo infeccioso, e a presença de tubulina em células endoteliais pulmonares fixadas de bovinos. Complementarmente, os autores demonstraram a capacidade de acoplar o módulo do OpenSIM a um microscópio de varredura por sonda, com o qual conseguiram correlacionar a topografia de uma célula com a fluorescência de seu citoesqueleto.

O OpenSIM apresenta como principal distinção o método de produção dos padrões de interferência. Enquanto microscópios SIM convencionais utilizam fontes de luz coerentes associadas a um SLM operando como uma grade de difração, os autores do OpenSIM propuseram a adoção de uma fonte de luz incoerente e da projeção do padrão de interferência na amostra. Quando o SLM opera como uma grade de difração, a luz incidida é espalhada em diferentes ordens de difração, que posteriormente são conduzidas até a amostra para que interfiram entre si e produzam um padrão de interferência linear.

Na concepção original do OpenSIM, os autores concentraram-se em desenvolver um sistema compacto e barato que fosse suficientemente simples para que outros pesquisadores pudessem replicá-lo sem dificuldades. Por esse motivo, aspectos como o custo-benefício, disponibilidade de peças, dimensões reduzidas e segurança de manuseio foram tidos como prioritários para o projeto. Estes mesmos pontos, porém, acabam impondo restrições ao desempenho do módulo em múltiplos aspectos, o que impacta diretamente na qualidade das imagens reconstruídas e na resolução máxima obtida.

Como a estrutura do módulo original é baseada em diversas peças impressas com filamento PLA em impressoras comerciais 3D, o correto alinhamento dos componentes ópticos pode se tornar um problema, dado que esta técnica de manufatura apresenta precisão inferior quando comparado com outros processos de fabricação, como a usinagem das peças.

Outro ponto de atenção está relacionado ao conceito de iluminação empregado. Como LEDs são fontes de luz pouco diretivas, os fótons se espalham em uma região, limitando sua aplicação direta em contextos em que a intensidade luminosa é relevante. Deste modo, apesar de a combinação de LEDs em free-space apresentar um baixo custo, as perdas de potência no layout são significativas. Como consequência, para garantir uma intensidade luminosa suficiente na amostra, LEDs de alta potência foram utilizados pelos autores, gerando como subproduto uma carga térmica considerável em componentes ópticos subjacentes, haja vista que estes LEDs dissipam muita potência na forma de calor.

Para a reconstrução das imagens, os autores utilizaram o software SIMToolbox, uma ferramenta em código aberto desenvolvida para MATLAB (Křížek et al. 2016). O algoritmo utilizado para a reconstrução pelo software baseia-se no método clássico de Heintzmann-Gustafsson, que é defasado com relação ao estado da arte para reconstruções de imagens com iluminação estruturada. Algoritmos mais recentes possuem otimizações em características-chave não implementadas no SIMToolbox, como estimativas mais precisas dos parâmetros de iluminação; melhor supressão da emissão de fundo; diminuição do tempo de reconstrução; aumento da máxima resolução axial pós-reconstrução; e implementação de filtros notch para minimização de artefatos de Gibbs. Quando combinados, esses algoritmos são capazes de contornar grande parte das deficiências do SIM frente a outras técnicas de super-resolução.

Como contorno às limitações do SIMToolbox, propõe-se um fluxograma de reconstrução ([Figura 1818](#_Ref163142922)) que una aspectos desejáveis de diferentes algoritmos modernos, a partir do qual se espera obter imagens reconstruídas de alta qualidade com pouco tempo de aquisição. Inicialmente, o usuário deverá selecionar uma região de interesse (ROI) utilizando o modo de fluorescência convencional do microscópio. Selecionada a ROI, será feita a aquisição das imagens brutas com os diferentes padrões de iluminação no plano focal selecionado. As imagens brutas serão processadas para remoção da emissão do fundo, e as imagens resultantes serão usadas para reconstrução bidimensional com um algoritmo otimizado para o tempo de execução. Se a ROI selecionada não for apropriada para os interesses do usuário, ele deve retornar para selecionar uma nova. Caso contrário, prossegue-se para a reconstrução em alta qualidade do plano focal da ROI. Se o resultado apresentar artefatos de reconstrução, o usuário deverá seguir um manual para identificação do tipo de artefato no espectro da imagem e quais parâmetros da reconstrução devem ser alterados para corrigi-los. Uma vez que a imagem reconstruída esteja sem artefatos identificados pelas ferramentas de diagnóstico, prossegue-se com a aquisição volumétrica das imagens brutas da ROI. Feita a aquisição volumétrica, o usuário deve então selecionar uma nova ROI para recomeçar o fluxo de aquisição e reconstrução. Em segundo plano, ocorre a reconstrução em alta qualidade do volume, utilizando os parâmetros previamente otimizados pelo próprio usuário. O volume reconstruído, então, é submetido a uma rede neural capaz de corrigir a anisotropia axial (Li et al. 2023). Uma vez que o protótipo modificado do OpenSIM não conta com secionamento óptico, é necessário executar a etapa de supressão de fundo para cada uma das imagens brutas do volume. No entanto, como a remoção da emissão de fundo já é feita pelo secionamento óptico na reconstrução volumétrica, essa etapa não será necessária no microscópio com três feixes (3D-SIM).

Os tempos de execução para cada etapa são dependentes da unidade de processamento disponível para o microscópio. Como exemplo, testes preliminares indicam que a reconstrução em tempo real ocorre na ordem de milissegundos quando executada na unidade de processamento gráfico (GPU) de um computador pessoal.

![](media/image23.svg)

Dentre as modificações propostas para o módulo de imagem estruturada, pode-se citar a substituição do *tube lens* especificado originalmente pelo modelo TTL-200-A fabricado pela Thorlabs. Esta modificação se deu pela necessidade de compatibilizar o comprimento focal do *tube lens* com o comprimento focal padrão f = 200 mm utilizado pelos microscópios fabricados pela Leica, para que nenhuma magnificação adicional seja introduzida no sistema. Também foi selecionado um adaptador de porta infinita compatível com o microscópio Leica DMi8 adquirido previamente.

Conforme apresentado nos parágrafos anteriores, o conceito de iluminação originalmente proposto por Hannebelle et al. (2024) apresenta baixa modularidade e manutenção difícil, haja vista que a substituição de qualquer componente óptico implica no desacoplamento do módulo e posterior desmontagem dele. Ademais, a presença de fontes de luz com baixa eficiência nas proximidades de componentes ópticos induz distúrbios térmicos que podem afetar a performance do sistema, provocando, por exemplo, o surgimento de aberrações do tipo *coma* devido ao deslocamento dos centros ópticos. Assim, a solução proposta consiste na segregação dos componentes responsáveis por produzir a iluminação dos componentes responsáveis por produzir uma imagem com padrões estruturados. A partir disso, deriva-se um novo conceito para o módulo estruturador, onde uma fibra óptica se torna responsável por transmitir a luz já condicionada até os componentes responsáveis por gerar o padrão estruturado, conforme apresentado na [Figura 1919](#_Ref163136584).

![A blue circle with black text Description automatically generated](media/image24.png)

Assim, tem-se um novo conceito para o layout óptico do gerador do padrão estruturado ([Figura 2020](#_Ref163136632)). Quando comparado ao layout original apresentado na [Figura 1717](#_Ref163132016), percebe-se que a solução apresenta menos componentes, haja vista que nesta abordagem a fonte de luz é tratada como um desenvolvimento independente. Com esta modificação espera-se minimizar as perdas de potência ao longo do layout óptico e o calor dissipado no sistema.

![Diagrama Descrição gerada automaticamente](media/image25.png)

Nesta nova proposta, a fibra óptica é conectada ao gerador de padrão estruturado por meio de um conector do tipo SMA. A luz então se propaga em espaço aberto até ser colimada por uma lente, de onde segue até o polarizador linear. Deste ponto em diante, o funcionamento do layout se mantém semelhante ao proposto pelos autores (Hannebelle et al. 2024). Além das modificações no traçado óptico, também são propostas modificações na arquitetura optomecânica do sistema, substituindo-se o *frame* monolítico impresso em 3D por outro tipo de estrutura. Em um primeiro momento, espera-se que os elementos ópticos sejam montados em mesa óptica com postes e frames ajustáveis, para posterior integração em uma estrutura optomecânica definitiva, quando o projeto apresentar um grau de maturidade maior.

Com o protótipo modificado e acoplado ao Leica DMi8, espera-se que seja possível reconstruir imagens de amostras biológicas BSL1 com espessura de até 10 µm e até o dobro da resolução original da objetiva, o que será feito em até 4 cores com os padrões de iluminação em 3 ângulos e 3 fases. Os comprimentos de onda nominais escolhidos serão 405 nm, 488 nm, 561 nm e 640 nm, por se tratarem de comprimentos de excitação tradicionais para os fluoróforos utilizados na microscopia de fluorescência de amostras biológicas. As aquisições serão feitas em temperatura ambiente e a pressão atmosférica, com objetivas secas com abertura numérica de 0,75, magnificação de 100x e distância de trabalho de 3,5 mm.

As imagens brutas obtidas a partir do microscópio permitirão avaliar a utilidade do fluxograma para reconstrução definido anteriormente ([Figura 1818](#_Ref163142922)), tendo como critérios de avaliação o tempo de reconstrução nas diferentes etapas, a incidência de artefatos após otimização dos parâmetros, e a resolução máxima obtida em amostras biológicas. Além disso, pretende-se estabelecer um manual de calibração, diagnóstico e correção de erros, que será baseado no imageamento de esferas tetrafluorescentes com 100 nm de diâmetro (TetraSpeck, Thermofisher) e de lâminas fluorescentes de microscopia (FSK5 slide set, Thorlabs). Ferramentas gratuitas para análise das aquisições brutas e após reconstrução (NanoJ-SQUIRREL, SIMcheck) serão usadas para quantificar os artefatos resultantes e avaliar a confiabilidade das reconstruções.

As reconstruções volumétricas por fluorescência no visível justificarão o desenvolvimento de um fluxo de trabalho para correlação com as medidas-teste de tomografia de raios-X moles (SXT) feitas no Protótipo Óptico da linha de Luz SIBIPIRUNA, descrito no CDR Ótica de Lentes e Guias de Onda. Para isso, será necessário empregar algoritmos de registro entre imagens de fluorescência no visível e imagens de microscopia eletrônica de varredura, modificando-os para se adequarem às imagens de SXT. Ademais, um protocolo descrevendo as etapas utilizadas no registro entre o cryoSIM e os resultados da linha de luz B24, do Diamond Light Source, será usado como guia para o desenvolvimento do algoritmo (Vyas et al. 2021).

Com os resultados preliminares da reconstrução, será possível verificar se fontes incoerentes de luz resultam em uma profundidade de iluminação suficientemente grande para a estimativa adequada dos parâmetros de iluminação. Em caso negativo, o protótipo terá que ser modificado para utilizar lasers como fonte de iluminação, sendo necessário especificar a potência utilizada, as fibras para transportar a luz, e o método que será utilizado para redução do ruído de coerência do feixe.

Os resultados obtidos com o protótipo permitirão estimar a viabilidade técnica do desenvolvimento de um módulo criogênico para o microscópio Leica DMi8, o que dependerá não apenas da qualidade do módulo de iluminação estruturada por si só, mas também de características inerentes ao próprio microscópio adquirido, como a estabilidade mecânica de seu estágio e a facilidade de sincronizar sua câmera com o SLM. Nessa situação, não será mais necessário desenvolver um microscópio separado, o que corresponderia à concretização do Cenário 2 mapeado anteriormente ([Figura 14](#_Ref163815533)). No entanto, será preciso modificar o módulo estruturador de luz, para que ele passe a operar com três feixes e em modo de interferência, além de ser preciso desenvolver um módulo criogênico compatível com o microscópio.

# Referências

Bleck, C.k.e., A. Merz, M.g. Gutierrez, P. Walther, J. Dubochet, B. Zuber, e G. Griffiths. 2010. “Comparison of Different Methods for Thin Section EM Analysis of Mycobacterium Smegmatis”. *Journal of Microscopy* 237 (1): 23–38. [https://doi.org/10.1111/j.1365-2818.2009.03299.x](https://doi.org/10.1111/j.1365-2818.2009.03299.x).

Chatzimpinou, Anthoula, Charlotta Funaya, David Rogers, Stephen O’Connor, Sergey Kapishnikov, Paul Sheridan, Kenneth Fahy, e Venera Weinhardt. 2023. “Dehydration as Alternative Sample Preparation for Soft X-Ray Tomography”. *Journal of Microscopy* 291 (3): 248–55. [https://doi.org/10.1111/jmi.13214](https://doi.org/10.1111/jmi.13214).

Chlanda, Petr, Maria Alejandra Carbajal, Marek Cyrklaff, Gareth Griffiths, e Jacomine Krijnse-Locker. 2009. “Membrane Rupture Generates Single Open Membrane Sheets during Vaccinia Virus Assembly”. *Cell Host & Microbe* 6 (1): 81–90. [https://doi.org/10.1016/j.chom.2009.05.021](https://doi.org/10.1016/j.chom.2009.05.021).

“Cryogenium”. s.d. Linkam Scientific. Acedido a 4 de abril de 2024. [https://www.linkam.co.uk/cryogenium](https://www.linkam.co.uk/cryogenium).

Cryosol-World. s.d. “Technology”. CryoSol-World. Acedido a 4 de abril de 2024. [https://cryosol-world.com/vitrojet-solutions/technology/](https://cryosol-world.com/vitrojet-solutions/technology/).

“EM GP2 Automatic Plunge Freezing”. s.d. Acedido a 4 de abril de 2024. [https://www.leica-microsystems.com/products/sample-preparation-for-electron-microscopy/p/leica-em-gp2/](https://www.leica-microsystems.com/products/sample-preparation-for-electron-microscopy/p/leica-em-gp2/).

Hannebelle, Mélanie T. M., Esther Raeth, Samuel M. Leitao, Tomáš Lukeš, Jakub Pospíšil, Chiara Toniolo, Olivier F. Venzin, et al. 2024. “Open-Source Microscope Add-on for Structured Illumination Microscopy”. *Nature Communications* 15 (1): 1550. [https://doi.org/10.1038/s41467-024-45567-7](https://doi.org/10.1038/s41467-024-45567-7).

Křížek, Pavel, Tomáš Lukeš, Martin Ovesný, Karel Fliegel, e Guy M. Hagen. 2016. “SIMToolbox: a MATLAB toolbox for structured illumination fluorescence microscopy”. *Bioinformatics* 32 (2): 318–20. [https://doi.org/10.1093/bioinformatics/btv576](https://doi.org/10.1093/bioinformatics/btv576).

Le Gros, M. A., G. McDermott, B. P. Cinquin, E. A. Smith, M. Do, W. L. Chao, P. P. Naulleau, e C. A. Larabell. 2014. “Biological Soft X-Ray Tomography on Beamline 2.1 at the Advanced Light Source”. *Journal of Synchrotron Radiation* 21 (6): 1370–77. [https://doi.org/10.1107/S1600577514015033](https://doi.org/10.1107/S1600577514015033).

Li, Shuoguo, Xing Jia, Tongxin Niu, Xiaoyun Zhang, Chen Qi, Wei Xu, Hongyu Deng, Fei Sun, e Gang Ji. 2023. “HOPE-SIM, a cryo-structured illumination fluorescence microscopy system for accurately targeted cryo-electron tomography”. *Communications Biology* 6 (abril): 474. [https://doi.org/10.1038/s42003-023-04850-x](https://doi.org/10.1038/s42003-023-04850-x).

Li, Xuesong, Yicong Wu, Yijun Su, Ivan Rey-Suarez, Claudia Matthaeus, Taylor B. Updegrove, Zhuang Wei, et al. 2023. “Three-Dimensional Structured Illumination Microscopy with Enhanced Axial Resolution”. *Nature Biotechnology* 41 (9): 1307–19. [https://doi.org/10.1038/s41587-022-01651-1](https://doi.org/10.1038/s41587-022-01651-1).

Loconte, Valentina, Jian-Hua Chen, Mirko Cortese, Axel Ekman, Mark A. Le Gros, Carolyn Larabell, Ralf Bartenschlager, e Venera Weinhardt. 2021. “Using Soft X-Ray Tomography for Rapid Whole-Cell Quantitative Imaging of SARS-CoV-2-Infected Cells”. *Cell Reports Methods* 1 (7). [https://doi.org/10.1016/j.crmeth.2021.100117](https://doi.org/10.1016/j.crmeth.2021.100117).

Martens, Garnet, Elaine C. Humphrey, Lionel G. Harrison, Begonia Silva-Moreno, Juan Ausió, e Harold E. Kasinsky. 2009. “High-Pressure Freezing of Spermiogenic Nuclei Supports a Dynamic Chromatin Model for the Histone-to-Protamine Transition”. *Journal of Cellular Biochemistry* 108 (6): 1399–1409. [https://doi.org/10.1002/jcb.22373](https://doi.org/10.1002/jcb.22373).

Okolo, Chidinma A., Ilias Kounatidis, Johannes Groen, Kamal L. Nahas, Stefan Balint, Thomas M. Fish, Mohamed A. Koronfel, et al. 2021. “Sample Preparation Strategies for Efficient Correlation of 3D SIM and Soft X-Ray Tomography Data at Cryogenic Temperatures”. *Nature Protocols* 16 (6): 2851–85. [https://doi.org/10.1038/s41596-021-00522-4](https://doi.org/10.1038/s41596-021-00522-4).

Phillips, Michael A., Maria Harkiolaki, David Miguel Susano Pinto, Richard M. Parton, Ana Palanca, Manuel Garcia-Moreno, Ilias Kounatidis, et al. 2020. “CryoSIM: Super-Resolution 3D Structured Illumination Cryogenic Fluorescence Microscopy for Correlated Ultrastructural Imaging”. *Optica* 7 (7): 802–12. [https://doi.org/10.1364/OPTICA.393203](https://doi.org/10.1364/OPTICA.393203).

“Vitrobot Mark IV System - BR”. s.d. Acedido a 4 de abril de 2024. [https://www.thermofisher.com/br/en/home/electron-microscopy/products/sample-preparation-equipment-em/vitrobot/instruments/vitrobot-mark-iv.html](https://www.thermofisher.com/br/en/home/electron-microscopy/products/sample-preparation-equipment-em/vitrobot/instruments/vitrobot-mark-iv.html).

Vyas, Nina, Stephan Kunne, Thomas M. Fish, Ian M. Dobbie, Maria Harkiolaki, e Perrine Paul-Gilloteaux. 2021. “Protocol for image registration of correlative soft X-ray tomography and super-resolution structured illumination microscopy images”. *STAR Protocols* 2 (2): 100529. [https://doi.org/10.1016/j.xpro.2021.100529](https://doi.org/10.1016/j.xpro.2021.100529).