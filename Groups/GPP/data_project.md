---
title: Projeto Data
description: 
published: 1
date: 2024-05-16T14:02:51.817Z
tags: 
editor: markdown
dateCreated: 2024-05-14T14:19:38.055Z
---

# DATA
Data Access Through Automation

O projeto surgiu com a necessidade de implementar, documentar e automatizar o sistema de criação de relatórios e consulta de dados de diversas naturezas. Realizando desde a Arquitetura de Dados, Engenharia, Ciência e Análise de Dados, fazendo o processo, *pipeline*, completo dos Dados.


## Arquitetura de Dados
#### Categorias
Os dados serão mapeados de sua origem, seja ela de domínio próprio do GPP, como o Smartsheet. Também podem ser de terceiros, que os mesmos realizam o armazenamento e manutenção dos dados. E por último, temos os dados que são fornecidos a nós, porém seu armazenamento é de nossa responsabilidade. Sendo assim, dividos em três categorias: Próprias, Consultadas e Fornecidas.

#### Armazenamento
Após o mapeamento, os dados serão salvos em CSV no Ibirá, para backup e por conta do formato deles poderemos, se necessário realizar uma migração dos dados. Outra consequência do mapeamento, é a movimentação destes dados para uma máquina virtual, onde nela executamos scripts em python e um banco de dados, que assim centralizamos todas as três categorias de dados em uma fonte só, sendo mais importante para a próxima etapa.

## Engenharia de Dados
#### Modelo
Visto como as técnicas estão evoluindo cada vez mais, optamos por ELT(Extract, Load and Transform) ao invés de ETL(Extract, Transform and Load). Este modelo é mais benéfico para nós ao visarmos as especificidades dos dados e redundância dos mesmos.

#### Extração
Através dos serviços Python