---
title: SIBIPIRUNA
description: Soft X-rays tomography beamline at Orion
published: 1
date: 2024-05-03T11:46:42.717Z
tags: teste
editor: markdown
dateCreated: 2024-04-08T20:19:17.974Z
---

# Introdução

No contexto do Orion, alguns objetivos científicos foram criados, sendo um deles o de gerar imagens 3D com resolução nanométrica de células ex-vivo infectadas com agentes de nível 4 de biossegurança (BSL4) em estado quase nativo. Para isso a linha de luz SIBIPIRUNA foi criada, possuindo como capacidade fundamental a utilização de raios-X moles (*soft X-rays*) para gerar tomografia 3D de células isoladas. Esta capacidade necessariamente demanda que a célula esteja em estado criogênico, assim possibilitando que a célula tanto mantenha sua geometria quanto resista às doses de radiação dos raios-X ao longo das medidas. Além disso, com o intuito de ampliar as capacidades científicas do instrumento com um maior volume de informações das características da célula, concluiu-se ser necessário complementar as imagens de raios-X com uma técnica de imagem correlativa, criando-se assim uma plataforma de microscopia fluorescente de luz visível e tomografia de raios-X (CLXT do inglês *correlative light and X-ray tomography*). Dessa forma, a técnica de microscopia fluorescente também poderá ser empregada nas amostras estudadas na SIBIPIRUNA. A Figura 1 traz uma síntese do processo de análise e decisão do objetivo científico, onde é apresentado um diagrama de Missão e Capacidades, sendo que letra ’M’ define a Missão, que nesse caso representa o objetivo científico proposto, e ‘C’ as Capacidades a serem desempenhadas para que o objetivo da Missão seja alcançado. Além disso, a figura ainda apresenta uma estrutura hierárquica onde as Capacidades são derivadas, a partir da representação das letras ‘i’ e ‘e’ sobre as setas, que representam inclusão e extensão, respectivamente.


|![](/img/beamlines/sibipiruna/1.png =700x) |
|-|
| **Figura 1: Missão e Capacidades da linha de luz SIBIPIRUNA** |

Para o desenvolvimento da Capacidade 1.2, foi identificada a necessidade de um componente chamado de *Manipulador* para posicionar a amostra, montada a um *Suporte de Amostra*, no foco da linha de luz e realizar o movimento de tomografia. Ainda, devido ao fato de a amostra estar em estado criogênico, a solução também demandará um *Sistema de Refrigeração* para gestão térmica com a função de manter a amostra em temperatura criogênica. A partir disso, optou-se por desenvolver um Sistema de Porta-Amostras Criogênico (PACRIO), que deverá possuir as funções descritas conforme Figura 2.

![](/img/beamlines/sibipiruna/2.png) |
|-|
| **Figura 2: Diagrama de arquitetura do Porta-Amostras Criogênico, especificando os componentes, subcomponentes, funções e informações/matéria/energia trocada entre as funções** |

Este documento irá abordar o status de desenvolvimento do componente PACRIO, bem como da Capacidade 1.1, visto que essa capacidade em associação com a 1.2 possibilita a Capacidade 1.1.1. Logo as operações de 1.1 e 1.2 deverão ser compatíveis entre si para que a 1.1.1 seja atingida. Estudos de viabilidade técnica dos métodos tradicionais para um *Sistema de Preparo de Amostras* com congelamento também serão apresentados neste documento, assim como um *Sistema de Transferência de Amostras*, uma vez que são pré-requisitos para a solução de porta-amostra (Figura 3).

|![](/img/beamlines/sibipiruna/3.png) |
|-|
| **Figura 3: Diagrama de arquitetura e capacidade principal da linha de luz SIBIPIRUNA** |


# Ciclo de vida do PACRIO

Sistema de Interesse (SoI): o sistema de interesse que esse documento irá abordar será o PACRIO.

Objetivo/Missão: desenvolver um sistema de Porta Amostras Criogênico (PACRIO) para linha de luz SIBIPIRUNA.

Status atual: o projeto do PACRIO encontra-se em fase final do seu estágio Conceitual e inicial do estágio de Desenvolvimento, tendo uma pré-aprovação do design mecatrônico e térmico sido realizada pelo grupo de Mecatrônica e Engenharia de Precisão (MEP). A fase de Desenvolvimento está sendo iniciada a partir de uma análise de tolerâncias mecânicas do PACRIO.

Definindo o problema: conforme descrito no PDR da linha SIBIPIRUNA, a preparação de amostras criofixadas permitiu um salto na evolução da microscopia por possibilitar a realização de trabalhos com amostras biológicas mais estáveis quando expostas a radiação, como também por preservar as amostras em seu estado quase nativo. No entanto, uma série de limitações ainda existe para a execução desse tipo de preparo e operação, desde a dependência de atividades manuais em etapas críticas até diferentes tipos de porta amostras e técnicas de vitrificação, o que exige mecanismos de transferência e soluções de gestão térmica. A título de exemplo de diferentes protocolos existentes, podemos citar as linhas de luz XM-2 e B24, no *Advanced Light Source* e no *Diamond Light Source*, respectivamente, que possuem a mesma técnica da linha de luz da SIBIPIRUNA (cryogenic *transmission soft X-rays microscopy, cryo-TXM*), porém com preparo e estágios de amostras inteiramente diferentes (Le Gros et al. 2014; Okolo et al. 2021). Além disso, os equipamentos de proteção individual (EPIs) a serem utilizados durante a preparação das amostras no laboratório de biossegurança nível 4 (BSL4) do Orion tendem a aumentar a dificuldade de realização do fluxo de atividades.

Dessa forma, realizou-se uma análise funcional da operação da linha de luz SIBIPIRUNA a partir das suas capacidades. Essas informações são apresentadas no diagrama de arquitetura da Figura 3.Nota-se que o PACRIO possui funções essenciais dentro das capacidades principais da linha de luz, como parte da geração de imagens 3D da célula isolada a partir da utilização de raios-X. As funções definidas ao PACRIO estão sendo estudadas de forma sistêmica, partindo-se de uma compreensão de cenários, interfaces e requisitos, em busca de soluções viáveis e robustas para cada uma das funções. Esses estudos serão apresentados nos capítulos posteriores.

## Orçamento

As aquisições desse projeto vêm ocorrendo através do centro de custo referente ao PACRIO, com um montante total previsto de R$4.500.000,00. Na Tabela 1 são detalhados os montantes destinados às aquisições para cada um dos subsistemas e a data prevista para compra.

**Tabela 1: Orçamento para o SoI**

|     | Subsistema | Total Área | Fase A | Fase B | Fase C | Previsão de compra Fase A |
| --- | --- | --- | --- | --- | --- | --- |
| **PACRIO** | TXM Imaging | R$1.505.000,00 | R$559.500,00 | R$644.500,00 | R$301.000,00 | 01/03/2024 |
| Sample transfer | R$800.000,00 | R$240.000,00 | R$400.000,00 | R$160.000,00 |
| Correlative Imaging | R$885.000,00 | R$419.500,00 | R$288.500,00 | R$177.000,00 |
| Sample preparation | R$1.310.000,00 | R$393.000,00 | R$655.000,00 | R$262.000,00 |

## Estágios do ciclo de vida

A Tabela 2 apresenta os estágios do ciclo de vida do PACRIO em uma escala temporal de trimestres. Nos capítulos posteriores serão descritas as atividades específicas para cada um desses estágios.

**Tabela 2: Estágios do ciclo de vida do PACRIO**

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

|![](/img/beamlines/sibipiruna/4.png) |
|-|
| **Figura 5: Manipulador da Amostra e Sistema Gerenciamento Térmico do PACRIO. A) vista isométrica da parte interna (exposta às amostras e ciclos de descontaminação mais frequentes), e B) vista isométrica da parte externa (em ambiente de vácuo separado da amostra).** |

Conceitos de atuadores foram explorados para o estágio em questão. O nano-posicionador NSAU, da JPE, surgiu como um candidato promissor, devido ao seu curso de movimentação e força necessários, além de um design completamente hermético, selado em um encapsulamento metálico e equipado com um sistema de feedback de posicionamento (encoder) integrado. No design atual, é viável isolar totalmente os componentes eletrônicos de precisão e os sistemas de movimentação dos atuadores do ambiente de amostra, minimizando a exposição desses componentes a agentes de descontaminação que podem causar corrosão e desgaste.

Embora o sistema NSAU possua encoders internos, muitas vezes é preferível medir a posição o mais próximo possível da região de interesse. Assim, o conceito atual incorpora um sistema de interferometria para a metrologia na posição imediatamente antes da amostra, permitindo que os elementos interferométricos sejam posicionados fora do ambiente de amostra e transmitindo o sinal através de três janelas ópticas. A viabilidade deste conceito será explorada, com foco na validação dos cursos de movimentação e na aplicabilidade dos interferômetros em um sistema com um grande desvio angular natural.

Uma outra característica distintiva do design atual é a utilização de um acoplamento flexível para a transferência de calor por condução, conectando um criostato à região de interesse do estágio. Isso possibilita que o sistema de refrigeração, a saber, um criostato do tipo pulse tube (PT) ou Joule-Thomson (JT), também esteja localizado em outro ambiente. Para simplificar esse acoplamento e reduzir as cargas no sistema de rotação, um pequeno goniômetro operando em condições criogênicas pode ser empregado, sendo responsável unicamente pela movimentação do pino de amostras, que terá sua massa limitada a poucos gramas. Atualmente, existem diversas opções de goniômetros criogênicos que podem ser utilizados na aplicação, sendo o Attocube ANR240 e o JPE CSR1 opções candidatas (Figura 5).

|![](/img/beamlines/sibipiruna/5.png) |
|-|
| **Figura 5: Componentes principais do Manipulador de Amostra** |

Foi elaborado um modelo teórico do conceito apresentado na Figura 4, utilizando como base o esquema apresentado na Figura 6. Neste esquemático é possível verificar uma abstração do conceito proposto, bem como os principais parâmetros geométricos que impactam a análise de viabilidade. Dentre eles, pode-se citar a distância dos atuadores com relação ao centro R e à altura do pino de amostras com relação ao ponto de articulação do mecanismo h.

O conceito apresentado na Figura 4 foi validado por simulação de maneira preliminar por meio da determinação da tensão máxima nas *folded leaf springs* (Figura 6), que atuam como guias elásticos no mecanismo quando estas são deslocadas pelo atuador. Desta análise (Figura 7), percebe-se que é factível o emprego de *folded leaf springs* de certas ligas de titânio e aço, que podem atingir tensão de escoamento de até cerca de 900 – 1000 GPa.

|![](/img/beamlines/sibipiruna/6.png) |
|-|
| **Figura 6: Representação esquemática do conceito proposto. A) Vista posterior do mecanismo de movimentação, destacando as folded leaf springs FL e os atuadores X. B) Vista lateral do mecanismo, destacando novamente as folded leaf springs FL e o pino de amostras indicado por 1** |

![](/img/beamlines/sibipiruna/7.png) |
|-|
| **Figura 7: Tensão máxima teórica em função dos parâmetros geométricos. A) Desenho esquemático da folded leaf spring e suas propriedades geométricas, sendo b a largura da chapa, L os comprimentos, t a espessura e ∆X1 o movimento imposto pelo atuador na ponta da flexure. B) O gráfico apresenta o comportamento da tensão em uma folded leaf spring com as propriedades geométricas apresentadas no gráfico quando sujeita a um deslocamento de 10,00 mm em sua extremidade** |

Além da determinação da tensão máxima foi feito um estudo para a avaliação do volume que este conceito é capaz de varrer. A Figura 8 apresenta uma esquematização deste volume com base no pino de amostras considerado no conceito apresentado na Figura 4.

![](/img/beamlines/sibipiruna/8.png) |
|-|
| **Figura 8: A) Vista frontal do pino de amostras, sendo 1,2 e 3 os grids e 4 o pino de amostras. B) Representação do pino de amostras, a área hachurada representa a área a ser analisada, delimitada por um perímetro na forma de um oblongo, a variável r representa o raio dos grids, a representa o espaçamento entre eles e θ representa um parâmetro da curva que descreve o perímetro** |

O perímetro da área hachurada apresentado na Figura 8B representa a região mais externa a qual o estágio deve ser capaz de levar as amostras. Assim, para avaliar o comportamento dos 3 atuadores, a curva que descreve este perímetro foi parametrizada em função de um ângulo θ. Deste modo, para cada valor de θ tem-se os valores de x e y que satisfazem a curva que descreve o perímetro. Os pontos descritos por x e y por sua vez são inseridos nas matrizes de cinemática possibilitando assim a determinação do movimento que cada atuador deve realizar, estes resultados são apresentados na Figura 9.

|![](/img/beamlines/sibipiruna/9.png) |
|-|
| **Figura 9: Resultados obtidos por meio da análise cinemática preliminar. A) Curso necessário considerando a não superposição dos grids. B) Curso necessário considerando a superposição dos grids** |

O cenário apresentado na Figura 9A demonstra que o curso necessário excede o curso nominal dos atuadores para um espaçamento de 3,5 mm entre os grids, entretanto, ao considerar um espaçamento de 3 mm entre os grids, tem-se que o curso é suficiente. Outras modificações geométricas também têm impacto no curso necessário, porém não foram demonstradas pois este estudo se caracteriza apenas como uma avaliação preliminar, podendo ser estendido no futuro.

### Desenvolvimento

A etapa de desenvolvimento consiste na evolução de projeto detalhada do SoI. Esse estágio se encerra após uma validação analítica da dinâmica, cinemática, térmica e mecânica do PACRIO. Além disso, espera-se que os elementos e a operação do PACRIO sejam validados sob a ação de um agente de esterilização a ser utilizado na SIBIPIRUNA.

### Produção

O estágio de produção se inicia a partir da tradução de todas as informações do desenvolvimento em elementos do SoI. Durante essa etapa é esperada uma grande integração entre o MEP e o grupo de Gestão de Projetos, por ser uma fase com elevado número de aquisições de fornecedores externos. Além disso, é esperado um grande esforço por parte do MEP na tradução das especificações do desenvolvimento em documentação técnica para que fornecedores e grupos internos forneçam os componentes e serviços que atendam corretamente às especificações. Atividades relacionadas ao registro e gestão de problemas também são esperadas, e será necessário estimar um tempo de execução que leve em conta esses retrabalhos. Essa fase será encerrada quando o equipamento estiver montado, integrado e com todas as funções validadas em consonância com os parâmetros determinados na etapa de Desenvolvimento. Conforme a Tabela 2, a data prevista para início e conclusão da etapa de Produção será entre 01/2025 e 06/2025.

### Utilização e Suporte

O estágio de Utilização e Suporte é caracterizado por atividades nas quais o SoI entrará em operação em seu ambiente de uso, durante o qual ocorrerão paralelamente atividades de manutenção.

Durante essa etapa são esperadas atividades de revisão de projeto e suporte aos usuários. Além disso, será necessário estimar um tempo para correção das intercorrências que venham a ocorrer e consequentemente registro das soluções, comunicando os operadores da linha a partir de recomendações técnicas. Ao final, o objetivo a ser alcançado é da completa operação do ecossistema responsável pela operação do SoI.

### Desfazimento

O estágio de Desfazimento consiste das atividades planejadas para o encerramento do ciclo de vida do SoI. Para o PACRIO é esperado que, quando a sua utilidade seja esgotada, seus componentes sejam encaminhados para a própria estação experimental da linha SIBIPIRUNA, tanto quanto possível, ou desmontados e armazenados em condições adequadas, para que possam vir a ser reutilizados ou realocados em outros projetos.

# Estudos de viabilidade e Sistemas Interoperacionais

A operação da SIBIPIRUNA envolve a interação entre diversos sistemas, e integrar essas interfaces é uma tarefa fundamental para garantir que todos os componentes possam ser desenvolvidos e operados em conformidade. Avaliando a operação do PACRIO, é possível identificar as dependências do sistema, sendo elas listadas abaixo:

-   Sistema de Preparo de Amostras: dado que a amostra será preparada e carregada em um suporte específico e este transferido para o PACRIO, identificou-se a necessidade de incluir o preparo de amostras nessa fase de prototipagem, cobrindo principalmente questões relacionadas à vitrificação adequada das amostras criogênicas e à otimização do fluxo de trabalho e da transferência da amostra entre os sistemas;
-   Sistema de Microscopia de Luz Visível Fluorescente Criogênico: a partir da capacidade 1.1.1 que determina que a SIBIPIRUNA seja capaz de gerar uma imagem CLXT, mostrou-se necessário também o desenvolvimento de um microscópio de fluorescência, de forma a garantir compatibilidade entre ele e o microscópio de raios-X da SIBIPIRUNA.

A partir dessas demandas, frentes de trabalho paralelas e iterativas com PACRIO foram iniciadas, de forma a criar um cenário que atenda ao funcionamento desses diferentes sistemas. A seguir serão listadas as frentes de trabalho e nos capítulos posteriores seus status de desenvolvimento.

## Fluxo e Sistemas de Preparo de Amostras

A evolução da criomicroscopia, especialmente no contexto da microscopia de raios-X moles, marcou uma transição significativa na forma como os espécimes biológicos são preparados e analisados. Esse avanço centra-se no processo de vitrificação (ou criofixação), uma técnica que substitui os métodos tradicionais de fixação química usados na microscopia eletrônica. A vitrificação, como evidenciado pela pesquisa de criomicroscopia eletrônica, é fundamental para minimizar alterações morfológicas que poderiam comprometer a representatividade e a precisão dos resultados (Figura 10). Além disso, a análise de amostras vitrificadas em estado criogênico não apenas garante sua excelente preservação, mas também proporciona uma estabilidade robusta contra danos por radiação na microscopia de raios-X moles. Consequentemente, esses avanços na criomicroscopia de espécimes biológicos têm relevância para o projeto SIBIPIRUNA, que pretende utilizar a criofixação para examinar amostras biológicas em condições que representem de perto seu estado natural, visando uma representação imparcial e detalhada das estruturas biológicas envolvidas nos processos de infecção viral.

|![](/img/beamlines/sibipiruna/10.png)|
|-|
| **Figura 10: Seções virtuais de tomogramas de raios-X moles de fibroblastos vitrificados, secos ao ar e secos por CPD, indicando nucléolos, gotículas de lipídio e mitocôndrias. A célula seca ao ar na grade mostra contração. Barra de escala: 10 μm (Adaptado de Chatzimpinou et al. (2023)) (2) Micrografias eletrônicas comparando tecidos de testículos de N. lamellosa processados por fixação química e vitrificação seguida de inclusão em resina. Espécimes quimicamente fixados mostram coagulação da membrana e encolhimento entre células (adaptado de Martens et al. (2009)) (3) Comparação de preparações do vírus Vaccinia: fixação química, congelamento em alta pressão/substituição por congelamento e microscopia eletrônica criogênica. A fixação química leva ao colapso das camadas do vírus (Adaptado de Chlanda et al. (2009)​). (4) Micrografias comparativas de envelopes celulares de M. smegmatis: fixação química e vitrificação seguida de inclusão em resina. A vitrificação resulta em menor largura do envelope celular (Adaptado de ​​Bleck et al. (2010)). (5) Comparação de tomogramas de raios-X moles em linfócitos B humanos nativos e fixados da linhagem GM12878. As células fixadas apresentam morfologia distorcida e gotículas de lipídio (Adaptado de Loconte et al. (2021)​).** |

Como apresentado na Figura 11, para a linha SIBIPIRUNA será empregado um fluxo de trabalho criogênico completo de células congeladas e hidratadas (vitrificadas) em substratos finos (e possivelmente também em capilares). Embora essa abordagem traga vantagens substanciais para a qualidade dos dados de tomografia e a abordagem científica, ela impõe desafios significativos para o projeto do fluxo de trabalho de preparação e manuseio de amostras. Isso se torna ainda mais complexo no contexto do ambiente BSL3/4, onde o uso de EPIs pode reduzir a mobilidade e destreza do usuário. Com isso em mente, o fluxo de trabalho atual está sendo projetado para minimizar o número de interações manuais do usuário com a amostra e reduzir a quantidade de equipamentos dentro da chamada "zona quente". Uma frente de trabalho específica foi criada para tratar do fluxo de trabalho para otimização do processo de vitrificação de células, que será abordado em detalhes no capítulo posterior.

|![](/img/beamlines/sibipiruna/11.png)|
|-|
|**Figura 11: Fluxo de trabalho proposto para a preparação de amostras para análise celular dentro do framework da linha de luz SIBIPIRUNA. Inicialmente, (1) as grades ou membranas passam por uma descarga de plasma para melhorar a hidrofilicidade, um pré-requisito para uma aderência eficaz das amostras. Em seguida, (2) é realizada a litografia de padrões de adesão nas grades usando os sistemas PRIMO & DMi8, garantindo a adesão celular direcionada. A preparação continua com (3) a deposição de cultura de células ou suspensão nas grades. Em certos casos, (7) nanopartículas de ouro são depositadas como marcadores fiduciais para análise tomográfica. As amostras são então submetidas a (4) triagem em temperatura ambiente com o DMi8 para verificação antes do (8) blotting com o dispositivo Leica GP2. Posteriormente, as amostras são (9) imersas em etano, uma etapa crucial para sua preservação morfológica. O fluxo de trabalho continua à medida que as amostras são carregadas em uma (10) GridBox, transferidas criogenicamente para um (11) módulo de carregamento de amostras (VCM) e fixadas usando o sistema (12) AutoGrid. Após a (13) transferência criogênica para o criomicroscópio para imagens de super-resolução por iluminação estruturada (SIM), elas podem passar por (14) microscopia correlativa sobre o criomicroscópio SIM. As amostras são então (15) retornadas ao VCM criogenicamente, (16) carregadas em um suporte de amostra e colocadas em um (17) cartucho de transferência. Este cartucho é então carregado no sistema (18) VCT500, que finalmente leva à (19) transferência para a linha de luz para imagens de tomografia de raios-X moles (SXT). Essa sequência abrangente garante que as amostras sejam meticulosamente preparadas e preservadas para análises de alta resolução.**|

Além de a SIBIPIRUNA ser projetada para a capacidade de TXM confiável, segura e de alto desempenho, com uma integração direta com o ambiente BLS4 do Orion para imagens 3D de células infectadas com patógenos de nível 3 e 4, pesquisas e colaborações com especialistas de outros síncrotrons (como cientistas da linha B24, no Diamond Light Source) demonstraram que o uso de outras técnicas baseadas em microscopia de luz para imageamento de proteínas e pequenas moléculas fluorescentes acopladas ou intercaladas a organelas específicas podem fornecer um contexto celular adicional importante. Em certo sentido, as imagens de microscopia de fluorescência podem ajudar os cientistas a compreender melhor a localização e discernir estruturas subcelulares quando sobrepostas aos dados tomográficos de cryo-TXM, o que é feito a partir de técnicas matemáticas de registro de imagens. Com isso em mente, o atual fluxo de trabalho criogênico está sendo projetado para também incorporar um criomicroscópio de fluorescência 3D de super-resolução com base em um microscópio de iluminação estruturada (SIM).

## Otimização do processo de vitrificação e manipulação de amostras

Para otimização do processo de vitrificação, foi feita uma revisão bibliográfica a respeito dos métodos e equipamentos comerciais existentes para essa finalidade. Foram avaliados 4 equipamentos, sendo eles o Vitrobot da Thermo Fisher (“Vitrobot Mark IV System - BR”, s.d.), o EM GP2 da Leica (“EM GP2 Automatic Plunge Freezing”, s.d.), o Cryogenium da Linkam (“Cryogenium”, s.d.) e o VitroJet da CryoSol (Cryosol-World, s.d.). A Tabela 3 apresenta uma comparação entre eles.

**Tabela 3: Comparação entre principais equipamentos de vitrificação de amostra**

|     | Deposição de amostra | Técnica de controle da espessura da amostra | Técnica de vitrificação |
| --- | --- | --- | --- |
| Vitrobot | Manual | Blotting com papel | Imersão (*plunge)* |
| EM GP2 | Manual | Blotting com papel | Imersão (*plunge)* |
| Cryogenium | Imersão automática | Sucção | Imersão (*plunge)* |
| Vitrojet | Deposição automática | Deposição precisa | Jato (*jet)* |

Atualmente, o equipamento Vitrojet da CryoSol, o único da lista com vitrificação pelo processo recente e patenteado conhecido como *jet freezing*, apresenta-se como o candidato preferível para aplicação dentro do fluxo de trabalho da SIBIPIRUNA, por permitir um nível de automação maior e ser, em teoria, mais robusto e repetitivo em termos da qualidade de vitrificação. No entanto, o equipamento comercial foi originalmente desenvolvido para preparo das chamadas *single particles*, exigindo que customizações e validações sejam realizadas para células isoladas, que é o caso de interesse para a SIBIPIRUNA. Portanto, planeja-se a realização de colaborações técnicas, prototipagem e testes de validação para a tecnologia de *jet freezing* dentro das condições de contorno da SIBIPIRUNA no futuro próximo. Até lá, uma primeira rota mais conhecida, via *plunge freezing*, está sendo colocada em prática para validação antecipada do maior número possível de equipamentos e etapas do fluxo de trabalho (Figura 11), a partir da qual primeiros estudos sobre a qualidade da vitrificação e dos passos de manipulação das amostras podem ser conduzidos.

## Sistema de Microscopia de Luz Visível Fluorescente Criogênico

Para viabilização de microscopia correlativa na linha de luz SIBIPIRUNA, será desenvolvido um criomicroscópio de fluorescência de super-resolução por iluminação estruturada (SIM), que deverá se adequar às necessidades específicas de biossegurança e robustez, além de ser projetado especificamente para o suporte de amostra da estação experimental. Esse microscópio será desenvolvido com base em outros designs ópticos já comprovados. Nesse sentido, um dos designs estudados é o microscópio cryo-SIM B24, desenvolvido para a linha de luz B24 do Diamond Light Source ​(Phillips et al. 2020). Em uma visão geral, o sistema emprega quatro lasers de excitação de comprimentos de onda distintos — 405, 488, 561 e 647 nm — para gerar padrões de iluminação estruturada através de um modulador de luz espacial (SLM — *Spatial Light Modulator*). Esses padrões são o núcleo do SIM, pois induzem franjas de moiré que codificam informações da amostra que não seriam observadas em um microscópio convencional devido ao limite de difração da lente objetiva. Se o padrão de iluminação for conhecido, é possível utilizar métodos matemáticos de reconstrução para recuperar a estrutura original da amostra com até o dobro da resolução originalmente limitada pela objetiva.

|![](/img/beamlines/sibipiruna/12.jpeg)|
|-|
|**Figura 12: Layout óptico do microscópio cryo-SIM da B24. Retirado de Phillips et al. (2020).**|

# Referências

Bleck, C.k.e., A. Merz, M.g. Gutierrez, P. Walther, J. Dubochet, B. Zuber, e G. Griffiths. 2010. “Comparison of Different Methods for Thin Section EM Analysis of Mycobacterium Smegmatis”. *Journal of Microscopy* 237 (1): 23–38. https://doi.org/10.1111/j.1365-2818.2009.03299.x.

Chatzimpinou, Anthoula, Charlotta Funaya, David Rogers, Stephen O’Connor, Sergey Kapishnikov, Paul Sheridan, Kenneth Fahy, e Venera Weinhardt. 2023. “Dehydration as Alternative Sample Preparation for Soft X-Ray Tomography”. *Journal of Microscopy* 291 (3): 248–55. https://doi.org/10.1111/jmi.13214.

Chlanda, Petr, Maria Alejandra Carbajal, Marek Cyrklaff, Gareth Griffiths, e Jacomine Krijnse-Locker. 2009. “Membrane Rupture Generates Single Open Membrane Sheets during Vaccinia Virus Assembly”. *Cell Host & Microbe* 6 (1): 81–90. https://doi.org/10.1016/j.chom.2009.05.021.

“Cryogenium”. s.d. Linkam Scientific. Acedido a 4 de abril de 2024. https://www.linkam.co.uk/cryogenium.

Cryosol-World. s.d. “Technology”. CryoSol-World. Acedido a 4 de abril de 2024. https://cryosol-world.com/vitrojet-solutions/technology/.

“EM GP2 Automatic Plunge Freezing”. s.d. Acedido a 4 de abril de 2024. https://www.leica-microsystems.com/products/sample-preparation-for-electron-microscopy/p/leica-em-gp2/.

Le Gros, M. A., G. McDermott, B. P. Cinquin, E. A. Smith, M. Do, W. L. Chao, P. P. Naulleau, e C. A. Larabell. 2014. “Biological Soft X-Ray Tomography on Beamline 2.1 at the Advanced Light Source”. *Journal of Synchrotron Radiation* 21 (6): 1370–77. https://doi.org/10.1107/S1600577514015033.

Loconte, Valentina, Jian-Hua Chen, Mirko Cortese, Axel Ekman, Mark A. Le Gros, Carolyn Larabell, Ralf Bartenschlager, e Venera Weinhardt. 2021. “Using Soft X-Ray Tomography for Rapid Whole-Cell Quantitative Imaging of SARS-CoV-2-Infected Cells”. *Cell Reports Methods* 1 (7). https://doi.org/10.1016/j.crmeth.2021.100117.

Martens, Garnet, Elaine C. Humphrey, Lionel G. Harrison, Begonia Silva-Moreno, Juan Ausió, e Harold E. Kasinsky. 2009. “High-Pressure Freezing of Spermiogenic Nuclei Supports a Dynamic Chromatin Model for the Histone-to-Protamine Transition”. *Journal of Cellular Biochemistry* 108 (6): 1399–1409. https://doi.org/10.1002/jcb.22373.

Okolo, Chidinma A., Ilias Kounatidis, Johannes Groen, Kamal L. Nahas, Stefan Balint, Thomas M. Fish, Mohamed A. Koronfel, et al. 2021. “Sample Preparation Strategies for Efficient Correlation of 3D SIM and Soft X-Ray Tomography Data at Cryogenic Temperatures”. *Nature Protocols* 16 (6): 2851–85. https://doi.org/10.1038/s41596-021-00522-4.

“Vitrobot Mark IV System - BR”. s.d. Acedido a 4 de abril de 2024. https://www.thermofisher.com/br/en/home/electron-microscopy/products/sample-preparation-equipment-em/vitrobot/instruments/vitrobot-mark-iv.html.