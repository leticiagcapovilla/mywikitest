---
title: Projeto Data
description: 
published: 1
date: 2024-05-16T16:58:42.329Z
tags: 
editor: markdown
dateCreated: 2024-05-14T14:19:38.055Z
---

## Projeto DATA
##### Data Access Through Automation (Acesso a Dados Através da Automação)

O projeto surgiu da necessidade de implementar, documentar e automatizar o sistema de criação de relatórios e consulta de dados de diversas naturezas. Abrange desde a Arquitetura de Dados até a Engenharia, Ciência e Análise de Dados, realizando o processo, ou seja, o pipeline, completo dos Dados.

## Arquitetura de Dados
#### Categorias
Os dados serão mapeados desde sua origem, seja ela de domínio próprio do GPP, como o Smartsheet, ou de terceiros, que realizam o armazenamento e manutenção dos dados. Além disso, temos os dados que são fornecidos a nós, mas cujo armazenamento é de nossa responsabilidade. Sendo assim, são divididos em três categorias: Próprias, Consultadas e Fornecidas.

#### Armazenamento
Após o mapeamento, os dados serão salvos em formato CSV no Ibirá para backup. Devido ao formato, poderemos realizar uma migração dos dados, se necessário. Outra consequência do mapeamento é a transferência desses dados para uma máquina virtual, onde executamos scripts em Python e um banco de dados. Assim, centralizamos todas as três categorias de dados em uma única fonte, o que é crucial para a próxima etapa.

## Engenharia de Dados
#### Modelo
Considerando a evolução constante das técnicas, optamos pelo modelo ELT (Extract, Load and Transform) em vez do ETL (Extract, Transform and Load). Este modelo é mais benéfico para nós, pois leva em conta as especificidades e a redundância dos dados.

#### Extração
Por meio dos serviços Python executados na máquina virtual, faremos a extração dos dados de diversas fontes diferentes, como Smartsheet, Excel, Jira, etc., com uma frequência diária.

#### Carga
Após a extração, os dados serão armazenados no banco de dados MariaDB.

#### Transformação
A partir do MariaDB, começaremos a processar os dados. Teremos tanto uma tabela bruta (raw) quanto tabelas pré-processadas, onde usaremos SQL para economizar processamento. Após a transformação dos dados, realizaremos uma conexão via Fluxo de Dados (Dataflow) para preparar os dados para disponibilização ao Analista de Dados. Assim, geramos uma conexão através de um gateway para os dados na nuvem.

## Análise e Ciência de Dados
#### Combinação
Nesta última etapa, se necessário, será feita a junção de dados do Dataflow, a criação de colunas que atendam a necessidades específicas e a preparação final para a carga no Power B.I. Depois disso, o usuário poderá conectar seu relatório, notebook para Aprendizado de Máquina (A.M), ou qualquer outra necessidade que precise ser atendida.