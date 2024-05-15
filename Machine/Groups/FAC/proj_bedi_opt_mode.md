---
title: Project BEDI optics mode
description: 
published: 1
date: 2024-03-19T19:07:52.536Z
tags: 
editor: markdown
dateCreated: 2024-03-19T19:07:38.384Z
---

# FAC: Project BEDI optics mode

## Introduction

Realizamos estudos no modo BEDI para controlar instabilidades coletivas longitudinais e transversais com o sistema de feedback. Também tentamos otimizar o tempo de vida desse modo alterando a tensão de GAP das cavidades de RF, sem sucesso e atualmente estamos trabalhando para gerar um modo similar ao BEDI que possua tempo de vida mais elevado. A vantagens desses modos de baixa emitância é que eles possuem feixes de elétrons menores, o que melhora a qualidade da luz síncrotron gerada. Assim, tornar um desses modos adequado para a operação do UVX seria benéfico para os usuários da máquina. Ainda, aprender a usar equipamentos avançados, como o sistema de feedback, serve como treinamento para a operação futura do sírius, onde tais ferramentas serão essenciais para o funcionamento da máquina.

## Detalhamento

O modo **BEDI** (**B**aixa **E**mitância com **D**ispositivos de **I**nserção) é um modo de operação do UVX criado com o intuito de minimizar a emitância do anel já considerando o efeito dos dispositivos de inserção que estão instalados na máquina e respeitando fortes vínculos sobre a óptica.

Esse modo foi encontrado a partir do modelo do anel que temos em nossos códigos de simulação, com o auxílio de um algorítmo genético e da varredura dos parâmetros independentes nos intervalos de valores viáveis. Os parâmetros que assumimos como independentes para fazer a procura foram as forças das três famílias de quadrupolos instalados no anel e para todas as máquinas testadas impusemos que sua sintonia deveria ser parecida com a sintonia do modo de operação convencional, além de vínculos que garantem a estabilidade e a baixa sensibilidade frente a perturbações.

Após algumas iterações nos algorítmos chegamos a um resultado que previa uma redução da emitância pela metade e de 23% no tamanho horizontal do feixe nos trechos retos, onde estão instalados os dispositivos de inserção. A implementação do modo foi facilitada pelo vínculo de sintonia que impuséramos, citada anteriormente. Assim pudemos injetar o feixe no modo convencional, aumentar sua energia para a energia de operação e fazer uma migração da ótica, sem que o feixe fosse perdido no processo.

Testamos o modo em baixa corrente e verificamos a redução do tamanho horizontal e a assinatura da função dispersão como previstos pelo modelo, dentro das precisões experimentais. Contudo, quando testamos o modo em alta corrente com algumas linhas de luz abertas para verificar se elas conseguiam evidenciar aumento de brilho da luz síncrotron, o feixe apresentou uma forte instabilidade transversal gerada por efeitos coletivos que resultou em um aumento do seu tamanho horizontal.

Esses experimentos foram realizados no primeiro semestre do ano de 2011. Nessa época não tínhamos um sistema de feedback bunch-by-bunch instalado e operacional na máquina, o que inviabilizou a continuação dos estudos com esse modo até o início do ano de 2014. Nesse período o LNLS adquiriu três controladores de feedback bunch-by-bunch da empresa [Dimtel](http://www.dimtel.com/), projetou, produziu e instalou uma cavidade ressonante para funcionar como atuador longitudinal e comissionou todo o sistema.

O Grupo de Diagnóstico foi o principal envolvido nesse processo de estruturação do sistema bunch-by-bunch e teve uma contribuição fundamental nos experimentos de máquina realizados nesse ano, nos ensinando a utilizar o equipamento.

Antes de voltar a fazer estudos com alta corrente, primeiro simetrizamos a óptica linear do modo em baixa corrente, situação em que ele é estável. A simetrização foi feita por um processo indireto: primeiro medimos a função dispersão e a matriz resposta da máquina e calibramos um modelo para ajustar as medidas; em seguida simetrizamos o modelo e aplicamos no anel de armazenamento as variações de força das famílias de quadrupolo entre o modelo ajustado e o simetrizado. Para conferir os resultados da simetrização, repetimos a medida da função dispersão e matriz resposta e calibramos novamente o modelo. Esta segunda iteração apresentou uma redução significativa do betabeating e de assimetrias na função dispersão em relação à primeira.

Após a simetrização, realizamos um ajuste de cromaticidades e medimos o fator compactação de momento de segunda ordem, para caracterizarmos a optica não linear do modo. A medição dessas três quantidades é feita por meio da variação dos tunes transversais e longitudinal em função da energia do feixe, sendo que para conseguir alterar a energia, temos que variar a frequência de RF do anel. Para ajustar as cromaticidades, fizemos um procedimento parecido com o de simetrização: primeiro calibramos o modelo para reproduzir os valores medidos; em seguida corrigimos a cromaticidade no modelo e aplicamos as variações de força das famílias de sextupolos no anel. A segunda medida de cromaticidade forneceu, dentro das precisões experimentais, os mesmos valores que tínhamos definido no modelo, o que também é um indício indireto de que nosso modelo linear do anel representa satisfatoriamente o comportamento real da máquina, haja vista que as cromaticidades, apesar de serem parâmetros da rede não linear, dependem diretamente das funções óticas lineares nos pontos onde estão instalados os sextupolos.

Com o modo caracterizado, injetamos alta corrente e começamos a trabalhar com o sistema de feedback. Em todas as injeções que fizemos, o feixe apresentou uma instabilidade dipolar longitudinal, caracterizada pelo surgimento de picos ressonantes no sinal gerado pelo feixe em um analisador de espectros (também chamados de raias). Esses picos aparecem em torno dos harmônicos da frequência de RF, separados destes pela frequência síncrotron. Outra evidência dessa instabilidade é o aumento no tamanho longitudinal do feixe medido pela streak camera e no tamanho horizontal em trechos dispersivos, medido pela linha de diagnósticos DFX.

Após a identificação da instabilidade, tentamos configurar o sistema de feedback, principalmente por meio do ajuste dos parâmetros do filtro TAP, para fechar o loop longitudinal e controlar a instabilidade mas, em nenhuma das tentativas o sistema de feedback conseguiu estabilizar o feixe sozinho. Ainda não conseguimos explicar esse comportamento de modo satisfatório e com evidências experimentais, mas possíveis motivos são:

1. O kick que o sistema de feedback aplica no feixe é proporcional à amplitude de oscilação dos pacotes e não à taxa de crescimento da instabilidade. Assim, com a instabilidade completamente instalada, o valor do kick calculado pelo sistema satura o amplificador, o que poderia prejudicar o controle.
2. As grandes amplitudes de oscilação poderiam ativar efeitos não lineares que deformariam o feixe no espaço de fase longitudinal, descaracterizando uma oscilação pura dos centroides dos pacotes, que é o modo no qual o feedback é eficaz.

A última hipótese poderia explicar também porque o tempo de vida do feixe é menor com o loop fechado.

Por essas razões, para conseguir fechar o loop longitudinal tivemos que seguir o seguinte procedimento: primeiro ligamos a modulação de fase para controlar parcialmente as oscilações dipolares, ligamos o sistema de feedback com as configurações de filtro adequadas e em seguida desligamos a modulação. Apesar de a modulação de fase introduzir raias quadrupolares no espectro do feixe, essas raias somem assim que a modulação é desligada, não interferindo no controle do sistema de feedback. Contudo, em algumas injeções, dependendo do perfil de preenchimento e de sutís mudanças no estado das cavidades de RF, para correntes acima de 210 mA aproximadamente, instabilidades quadrupolares apareciam no feixe mesmo com a modulação desligada. Nesses casos conseguíamos fechar o loop mas o controle era perdido após alguns minutos. Para contornar essa situação, configuramos o filtro do sistema de feedback para maximizar a atenuação de sinais com o dobro da frequência síncrotron. Após esse ajuste conseguimos controlar a instabilidade dipolar sem perder o controle, mesmo com a quadrupolar presente.

Quando conseguimos fechar o loop longitudinal, notamos o surgimento de uma instabilidade vertical, verificada tanto pelo surgimento de raias bétatron na interface do sistema de feedback vertical, como pelo aumento de %80 no tamanho vertical do feixe, medido pela DFX. Fechar o loop vertical foi bem mais simples que o longitudinal. Nesse caso o sistema feedback conseguiu controlar as oscilações sozinho, após ajustarmos corretamente os parâmetros do filtro.

Em todas as injeções que fizemos durante os dias de estudo de máquina, não precisamos fechar o loop horizontal, porque não surgiu instabilidade nesse plano. Assim, verificamos que o tamanho do feixe medido nos três planos estavam maiores, porém próximos aos valores nominais previstos pelo modelo. As discrepâncias podem ser qualitativamente explicadas por efeitos de IBS (Intra Beam Scattering) e, nas situações em que a instabilidade longitudinal quadrupolar estava instalada, pelo aumento efetivo da dispersão de energia devido às oscilações no espaço de fase longitudinal. 