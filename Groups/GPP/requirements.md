---
title: Requerimentos
description: 
published: 1
date: 2024-07-30T12:48:15.447Z
tags: 
editor: markdown
dateCreated: 2024-07-30T12:48:15.447Z
---

### Fase 1
Como primeiro passo para este projeto, se fez necessário um ambiente em nuvem para que fosse possível a conexão remota das partes e também que os processos tivessem um ambiente exclusivo deles para serem construídos e executados, então para isso foi criada a VM GPP-DB e também alocado um espaço para nosso armazenamento.
Configuração da VM :
RAM: 4 GB
Memória: 10 GB + 5 PB
Necessário instalação: MariaDB, Python e as bibliotecas necessárias para os scripts.

#### Python:
  Utilizamos a linguagem Python como padrão para nossos scripts por conta da versatilidade e sua ampla gama de bibliotecas. Por conta do versionamento e já utilização do software internamente, estamos armazenando e controlando nossos códigos no repositório: [GPP / Business Intelligence / Scripts Python · GitLab (cnpem.br)](https://gitlab.cnpem.br/gpp/business-intelligence/scripts-python)
	Também usamos o daemon Cron, nativo do linux, que a partir do Crontab, podemos agendar para execução de comandos em determinados períodos. Recomenda-se leitura sobre o mesmo principalmente para a parte de Debug do mesmo.
#### MariaDB:
Como dito anteriormente, nesta fase do projeto, estaremos armazenando os dados em sua fase "raw/bronze", baseado na arquitetura Medalhão.

Dados do Banco:
Usuário: root
Senha: gppdb
            
                