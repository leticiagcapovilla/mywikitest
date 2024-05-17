# CON: Control-archiver

## Introdução 

O EPICS *Archiver Appliance*, desenvolvido pelo instituto americano *National Accelerator Laboratory (SLAC)*, é capaz de monitorar e arquivar um grande número de váriaveis, as chamadas *PVs*, geradas por servidores EPICS presentes na rede. O sistema fornece também opções de configuração de um largo conjunto de parâmetros referentes ao armazenamento e monitoramento. Uma *appliance* é composta basicamente por quatro módulos distintos, sendo eles:

* *Management*: provê as ferramentas necessárias para a gerência da *appliance*. Permite, por exemplo, adicionar ou remover *PVs* à lista de variáveis a serem arquivadas;
* *Engine*: o módulo funcional do arquivador. Captura as modificações ocorridas nas PVs, salvando-as em um *buffer* interno que é, posteriormente, transferido para o *short-term storage*;
* *Data Retrieval*: módulo responsável por recuperar os dados das *PVs* arquivadas. Responde a requisições JSON e de Matlab, por exemplo;
* *ETL*: responsável por mover os dados entre as unidades de armazenamento (*short-term*, *medium-term* e *long-term storage*);

A figura ao lado esquematiza o modo de funcionamento do *EPICS Archiver Appliance*.

|![](/img/groups/con/control_archiver/Applarch.png)|
|-|
|**Figure 1**: Modo de funcionamento de uma *appliance*.|

O instituto desenvolvedor da aplicação sugere que cada módulo seja lançada em sua própria instância *Tomcat*. Em adição, ele propõe a divisão da unidade de armazenamento em 3 outras unidades, de acordo com a frequência que os dados são salvos. Essas unidades são divididas *short-term*, *medium-term* e *long-term storage*, cujas frequências de armazenamento são, respectivamente, a cada hora, diária e anual. Essas configurações podem ser modificadas através da modificação de arquivos específicos, explicados nas próximas subseções.

Em um ambiente composto por diversos servidores EPICS e milhares de variáveis a serem monitoradas, tal como o *Sirius*, um sistema capaz de automizar e agilizar o armazenamento e recuperação de dados se torna fundamental para o monitoramento de eventuais problemas. Sendo assim, as próximas seções são dedicadas à instalação e exploração dos recursos disponíveis nesta aplicação.

## Instalação 

Esta subseção é dedicada às etapas necessárias para a instalação e configuração do arquivador EPICS.

### Virtualização  

A instalação e a configuração do *host* em que a instância do arquivador será executada não é um processo simples e rápido, envolvendo o ajuste de diversos arquivos de programas distintos, tais como base de dados e servidores *web*. Assim, um mecanismo capaz de facilitar e agilizar o processo de *deployment* em um novo ambiente, bem como abstrair detalhes de configuração, torna-se essencial para um ambiente como o do *Sirius*, em que o sistema deve estar sempre operante. Atualmente, a virtualização é uma técnica amplamente utilizada por várias empresas a fim de otimizar seus recursos e garantir um grande grau de flexibilidade nas suas soluções. Dentre as diversas técnicas de virtualização existentes, uma que vem crescendo nos últimos anos consiste no uso de unidades leves, independentes e executáveis, capazes de incluir tudo o que é necessário para executar determinado sistema em seu interior. A estas unidades, damos o nome de *containers*, justamente para refletir toda a sua capacidade de encapsulamento.

Dado que [Docker](https://www.docker.com/what-docker) é a principal plataforma de *containers* de software do mundo, possuindo um comunidade muito ativa, essa foi a alternativa adotada por nosso grupo para o *deployment* do arquivador.

#### Estrutura 

O arquivador necessita de cinco *containers* para ser executado: um para cada *appliance* e outro para a base de dados que armazenará as informações das variáveis, como tipo, período de amostragem etc, que estão sendo monitoradas. A comunicação entre os *containers* é garantida através de uma rede interna, provida pela própria ferramenta *Docker*.

#### Imagens 

As imagens que definem as funcionalidades dos *containers* são definidas por uma série *scripts*, presentes no repositório [git](https://github.com/orgs/lnls-sirius/teams/lnls-con/repositories) do nosso grupo. As imagens utilizadas para as *appliances* podem ser encontradas a partir de [docker-epics-archiver-appliances](https://github.com/lnls-sirius/docker-epics-archiver-appliances), enquanto que aquela usada para a base de dados, [docker-epics-archiver-db](https://github.com/lnls-sirius/docker-epics-archiver-db). Recentemente, para adequar a aplicação para o Docker Swarm, uma única imagem contendo todas as *appliances* foi criada. Alguns pontos importantes em relação às imagens:

* Os projetos referenciados acima possuem *scripts bash* capazes de gerar e executar as respectivas imagens, embora o seu uso seja recomendado em um ambiente de desenvolvimento e não de *deployment*. Informações para este último serão dadas nas próximas seções deste documento.

* As imagens de cada *appliance* utilizam a mesma imagem-base, chamada de [epics-archiver-generic](https://hub.docker.com/r/lnlscon/epics-archiver-generic). Esta última é baseada na imagem [tomcat:9](https://hub.docker.com/_/tomcat/) e utiliza a base [EPICS](https://www.aps.anl.gov/epics/download/base/index.php) versão *'3.14.12.6*'. Dois arquivos de configuração são basicamente copiados para dentro de *epics-archiver-generic*, sendo eles `lnls_appliances.xml` e `lnls_policies.py`. O primeiro especifica os endereços IP de cada *appliance* e deve reflitir os endereços obtidos pelos *containers* na rede interna. Conforme será discutido posteriormente, este arquivo raramente terá que ser modificado. O segundo, por sua vez, especifica as políticas que serão utilizadas para o armazenamento de dados. Em caso de alteração de quaisquer destes dois, é necessário reconstruir todas as imagens a partir dos comandos abaixo executados no diretório onde o repositório `docker-epics-archiver-appliances` foi clonado:

```
$ ./build-docker-generic-appliance.sh
$ ./docker-appliance-images/build-docker-appliance-images.sh
```

* As diferenças entre as imagens de cada *appliance* são regidas pelo *script* `docker-appliance-images/setup-appliance.sh`, que é executado no momento que a imagem está sendo construída. Neste *script*, ocorre a configuração de todos os arquivos do servidor *tomcat* referentes a segurança, conectividade com a base de dados e restrição de acesso. Para construir as imagens de cada *appliance* basta executar
```
$ ./docker-appliance-images/build-docker-appliance-images.sh
```

* A imagem adaptada para o Docker Swarm está disponível a partir [deste link](https://hub.docker.com/r/lnlscon/epics-archiver-single/).

Por último, o *script* `docker-appliance-images/tomcat-service.sh` será executado assim que cada imagem for lançada. Este *script*, por jamais terminar a sua execução (comando `tail -f` nunca termina), impede que o *Docker* finalize o *container*.

* A imagem do *container* contendo a base de dados, [epics-archiver-mysql-db](https://hub.docker.com/r/lnlscon/epics-archiver-mysql-db/), utiliza uma instância do MySQL e baseia-se em [mysql:latest](https://hub.docker.com/_/mysql/). Esta imagem foi configurada para executar o arquivo `archappl_mysql.sql` assim que for executada, populando, desta forma, o seu banco de dados com as tabelas usadas pelo arquivador.

#### Deployment 

*Scripts* para duas ferramentas de *deployment* dos containers são disponibilizados: [Docker Compose](https://docs.docker.com/compose/) e [Kubernetes](https://kubernetes.io/). A segunda, mantida e desenvolvida pela Google, destaca-se por apresentar muito mais recursos que a primeira não implementa, como por exemplo, armazenamento distribuído pelo *cluster*, porém esperamos utilizar a solução com *Docker Compose* nos nossos servidores pela maior facilidade de configuração.

##### Docker Compose 

Esta ferramenta utiliza o arquivo de configuração `docker-compose.yml` para realizar o *download* das imagens a partir do [Dockerhub](https://hub.docker.com/), configurar e lançar os respectivos *containers*. O projeto contendo este arquivo pode ser clonado a partir de [docker-epics-archiver-composed](https://github.com/lnls-sirius/docker-epics-archiver-composed). 

Cada um dos *containers* é especificado por uma entrada na seção `services`, no formato `epics-archiver-<container>`, em que `<container>` pode ser substituído por `mgmt`, `engine`, `etl`, `retrieval` ou `mysql-db`. Destacam-se os seguintes atributos de cada *container*:

* `container_name` e `image` definem, respectivamente, o nome do *container* e a imagem que ele utiliza.
* `networks` informa ao *Docker* a quais redes o respectivo *container* pertence. A *tag* `ipv4_address` permite definir explicitamente o endereço IP do *container* e *'deve refletir*' o que foi definido no arquivo `lnls_appliances.xml`, descrito na seção *'Imagens*'.
* `ports` permite expor uma porta do *container* e relacioná-la com uma porta do *host*. A relação `host_port:container_port` provoca que todas as requisições recebidas na porta `host_port` do *host* sejam direcionadas à porta `container_port` do *container* e vice-versa. Assim como no caso anterior, essa configuração *'deve corresponder*' ao que foi definido no arquivo `lnls_appliances.xml`, descrito na seção *'Imagens*'.
* `depends_on` permite especificar a ordem com que os *containers* seram lançados.
* `volumes` é utilizado para garantir a persistência dos dados modificados pelos *containers*. Quando um *container* é eliminado, todos os seus dados e configurações são excluídos. Se, por algum motivo, deseja-se armazenar dados que resistirão a exclusões de *containers*, usa-se essa *tag* no formato `path_host:path_container`. Assim, tudo que um *container* salvar em `path_container` será automaticamente salvo em `path_host`. Essa funcionalidade é essencial para as três áreas de armazenamento destacadas anteriormente (*short-term*, *medium-term* e *long-term storage*) e para o armazenamento do banco de dados.
* `env_file` e `environment` permitem a definição de variáveis de ambiente para os *containers*. Para `epics-archiver-mysql-db`, as variáveis especificadas devem ser idênticas àquelas definidas pelo arquivo `env-vars.sh` contido no projeto [docker-epics-archiver-appliances](https://github.com/lnls-sirius/docker-epics-archiver-appliances). Para `mgmt`, `engine`, `etl` e `retrieval`, o arquivo `lnls-epics-archiver.env` possui as *'variáveis de configuração do EPICS*'. A modificação de alguma delas não requer que as imagens sejam totalmente reconstruídas, requerindo apenas que os *containers* sejam reiniciados.

Alguns *scripts* ainda são fornecidos para a integração desta solução com o sistema de serviços do Linux, o `systemd`. Execute na pasta onde [docker-epics-archiver-composed](https://github.com/lnls-sirius/docker-epics-archiver-composed) foi clonado
```
make install
```
para instalar e habilitar o serviço `lnls-epics-archiver.service` e
```
make uninstall
```
para desinstalá-lo.

###### Debugging 

O principal método para se determinar a origem de algum *bug* é consultar os arquivos de *log* de cada *container*. Para tal, o primeiro passo é entrar no ambiente do *container*, através de 
```
$ docker exec -it epics-archiver-<appliance> bash
```
em que `<appliance>` pode ser substituído por `mgmt`, `engine`, `etl` ou `retrieval`. Em seguida, consultar os *logs* a partir de 
```
$ tail logs/arch.log4j
$ tail logs/catalina.out
```

##### Kubernetes 

###### Configuração inicial 

Um bom guia para a configuração inicial do Kubernetes pode ser encontrado a partir deste [guia](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html/getting_started_with_kubernetes/get_started_orchestrating_containers_with_kubernetes#starting_kubernetes), disponibilizado pela Red Hat.

###### Implementação 

A hierarquia dos elementos em *Kubernetes* é um pouco distinta daquela realizada pelo *Docker compose*.  Os *containers* são lançados em estruturas denominadas [pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/), cuja acessibilidade, por sua vez, é determinada por [services](https://kubernetes.io/docs/concepts/services-networking/service/). Na pasta `kubernetes` do projeto [docker-epics-archiver-composed](https://github.com/lnls-sirius/docker-epics-archiver-composed), disponibilizamos os arquivos de configuração dos *pods* e dos *services* necessários para a execução de uma instância do arquivador. Os nomes dos arquivos são da forma `epics-archiver-<appliance>-<type>.yaml`, em que `<appliance>`, assim como no caso anterior, deve ser substituído pelo nome de alguma das *appliances* ou `mysql-db`, e `<type>`, por `pod` ou `service`.

Nos arquivos `epics-archiver-<appliance>-pod.yaml` destacam-se:

* especificação de nome e imagem.
* portas a serem expostas. De preferência, devem ser iguais às portas especificadas no arquivo `lnls_appliances.xml` na seção *'Imagens*'.
* variáveis de ambiente.
* especificação de volumes persistentes de dados.

Nos arquivos `epics-archiver-<appliance>-service.yaml`, por sua vez, observam-se:

* o atributo [`ClusterIP`](https://kubernetes.io/docs/concepts/services-networking/service/#choosing-your-own-ip-address) determina o endereço IP que outros *pods* podem utilizar para comunicar com este serviço. 
* a determinação das portas com que o serviço receberá e enviará requisições. Três atributos determinam a conectividade do serviço: o primeiro, `port`, é a porta da qual o serviço recebe requisições a partir do endereço `ClusterIP`; o segundo, `targetPort`, consiste em uma porta publicada pelo *pod* para quais tais requisições são transmitidas e, por último, `nodePort` representa a porta com que o *'host*' recebe e envia requisições externas. Assim como na seção anterior, as portas especificadas em `port` e `targetPort`, bem como o endereço `ClusterIP`, devem ser compatíveis àqueles especificados no arquivo `lnls_appliances.xml`, que foi utilizado para a construção das imagens *Docker*.

O *script* `kubernetes/kubectl-appliances.sh` realiza a adição dos *pods* e *services* ao Kubernetes. Certifique-se que `kubelet.service` esteja ativo, conforme explicado em [[CON:Control-archiver#Configura.C3.A7.C3.A3o_inicial|Configuração Inicial]] e, então, adicione, primeiramente, os *pods* a partir do comando
```
$ kubernetes/kubectl-appliances.sh add pod
```
e, em seguida, os *services* através de
```
$ kubernetes/kubectl-appliances.sh add service
```
Para removê-los, basta executar 
```
$ kubernetes/kubectl-appliances.sh del pod
$ kubernetes/kubectl-appliances.sh del service
```

###### Debugging 

Para consultar os logs dos *pods*, assim como no caso do [[CON:Control-archiver#Debugging|Docker Compose]], execute o seguinte comando para entrar no container:

```
$ kubectl exec -it <pod> bash
```

E então:

```
$ tail logs/arch.log4j
$ tail logs/catalina.out
```

##### Docker Swarm 

Devido ao fato de que não é possível atribuirmos endereços IP aos serviços em um cluster Swarm, tivemos que criar uma única [imagem](https://hub.docker.com/r/lnlscon/epics-archiver-single/) contendo todas as *appliances*. Para lançá-la, clone o [repositório](https://github.com/lnls-sirius/docker-epics-archiver-composed) com o arquivo  `docker-swarm.yml` e entre no diretório `swarm`. Execute então:

```
$ sudo docker stack deploy -c docker-swarm.yml con-archiver
```

Siga as instruções dos arquivos README.md para configurar as variáveis de ambiente.

###### Debugging 

Assim como no caso do Docker Compose, a melhor forma de debugar a aplicação é verificar os arquivos de log gerados. Para tal, descubra em que máquina o serviço está rodando efetivamente com o seguinte comando:

```
$ sudo docker service ps con-archiver_epics-archiver
```

Então, entre no host e execute:

```
# Descubra o ID do container
$ sudo docker ps

# Entre no ambiente do container
$ sudo docker exec -it <ID> bash

# Acesse os logs da appliance desejada
$ tail <appliance>/logs/arch.log4j
```

## Uso do CS Studio no monitoramento 

O *CS Studio* pode ser usado para monitorar a *appliance*. Para isso, entre em `Edit > Preferences` e acesse o item `CSS Applications > Trends > Data Browser`. No campo *Archive Data Server URLs*, adicione o endereço contido em `<data_retrieval_url>` do arquivo configurado em `lnls_appliances.xml`, substituindo o protocolo `http://` por `pbraw://`. Escreva qualquer *Server alias*. Na tabela *Default Archive Data Sources*, adicione o mesmo endereço e aperte *Ok* para salvar as alterações.

É necessário alterar a perspectiva do *CS Studio*. Acesse `Windows > Open Perspective` e escolha *'Data Browser*'. Na aba *Archive Search*, escreva a *URL* configurada anteriormente e no campo *Pattern*, escreva o nome das variáveis arquivadas que deseja monitorar. Por exemplo, se escrevermos `MTTemp*`, todas as variáveis arquivadas com este início poderão ser acessadas. Clique com o botão direito na variável desejada e acesse `Process Variable > Data Browser`.

## Requisitando dados com *Python* 

|![](/img/groups/con/control_archiver/Archiver-test.png)|
|-|
|**Figure 2**: Gráfico gerado pela biblioteca `matplotlib` em *python*.|


A *appliance* pode ser acessada através de requisições *JSON* realizadas por um módulo escrito em *Python*, por exemplo. O *script* `add-pv-server.py`, contido na pasta `python/` do repositório [epics-archiver-appliance-scripts](http://git.cnpem.br/gustavo.pinton/epics-archiver-appliance-scripts/tree/master), implementa funções de adição, remoção de variáveis e de recuperação de dados do arquivador.

O módulo define duas *strings*, `MGMT_BPL` e `RETRIEVAL_DATA`, representando, respectivamente, os endereços dos *servlets* de gerenciamento e de obtenção de dados. A primeira *url* será usada para recuperar os dados e a segunda, para remover ou adicionar novas variáveis. A classe `ArchiverTester` provê métodos que permitem automatizar o processo de adição e remoção de PVs, sem que sejam necessários acessos à interface *web* do arquivador. Operações que alteram o estado do arquivador, como as estas duas últimas, requerem que o usuário esteja logado para efetuá-las. O método `registerUser`, desta forma, realiza a autenticação do usuário junto ao arquivador, habilitando a respectiva sessão a tais operações. Dessa forma, os métodos `archivePVs`, `pausePVs` e `deletePVs` devem ser executados somente após a uma chamada de `registerUser`.

O método `getDataPV` retorna os dados arquivados para uma lista de variáveis, passada como parâmetro. Como esse tipo de operação não necessita de direitos especiais, não é necessária que uma sessão com um usuáio logado tenha sido feita. Além da lista, esse método recebe dois outros valores, sendo eles objetos do tipo *time*, cuja implementação reside no módulo `time`. Esses parâmetros representam, por sua vez, as fronteiras do intervalo de tempo para o qual se deseja recuperar os dados, sendo que `beginning` é a data mais antiga e `end`, a mais recente. Os dados são recuperados através do método `getData.json`, disponível no *servlet* `retrieval` da *appliance*. Antes de realizarmos a requisição, é necessário traduzir os objetos *time* para o formato aceito pela servidor. Sendo assim, utiliza-se o método `strftime` do módulo `time` que retorna a representação *string*, segundo a máscara especificada (no nosso caso, `%Y-%m-%dT%H:%M:%S`), do objeto passado como parâmetro.

O servidor envia todos os dados, isto é, valores e datas do respectivo evento, em único vetor de dicionários. Por este motivo, é necessário processarmos essa estrutura antes de retorná-la ao programa que chamou o método. Os valores são acessíveis pelo índice `val` e seu tipo depende da aplicação. A data dos eventos relativos aos valores são recuperados pelas chaves `secs` e `nanos`, sendo números inteiros que contêm, respectivamente, a quantidadde de segundos e nanossegundos desde uma data de referência (1 de Janeiro de 1970) usada no *servlet*. É necessário notar que as datas retornadas estão em *UTC*, portanto é exigido que tais valores sejam convertidos para a o fuso local.

Os valores transmitidos pelo arquivador podem ser desenhados em forma de gráfico a partir da biblioteca `matplotlib`, por exemplo. A figura ao lado representa um gráfico obtido pelo módulo:

## Arquivador do Grupo de Controle 

Temos um arquivador rodando em uma das nossas *workstations* na sala de controle. Ele pode ser acessado a partir do endereço [http://10.0.4.57](http://10.0.4.57) (acesso apenas para computadores conectados à rede interna do CNPEM). Até o momento de edição desta página, essa instância já está monitorando mais de 900 PVs.

## Requisitando dados com o Jupyter Notebook 

Um [projeto](https://github.com/lnls-sirius/epics-archiver-jupyter-notebook) baseado no [Jupyter Notebook](http://jupyter.org/) foi criado com o intuito de auxiliar na recuperação dos dados. Para executá-lo, siga as instruções no README do projeto.

## Visualizador web para os dados do EPICS Archiver 

O Grupo de Controle iniciou em 2017 o projeto de uma interface web para visualização dos dados do arquivador EPICS, disponível [neste link](http://10.0.4.57:11998/retrieval/ui/archiver-viewer/index.html). Abaixo encontra-se uma lista de sugestões para a melhoria desse sistema. Trabalharemos nessa lista nos próximos meses.

* ~~[https://github.com/lnls-sirius/archiver-viewer/issues/2 Diminuir a espessura dos traços no gráfico, que estão muito grossos.]~~
* ~~[https://github.com/lnls-sirius/archiver-viewer/issues/3 Remover o texto "LNLS Archiver Web Viewer" no topo da área do gráfico].~~
* ~~Atualizar as bibliotecas JavaScript de terceiros usadas no projeto.~~
* ~~Adicionar ao projeto as bibliotecas JavaScript das quais o visualizador depende como submódulos Git.~~
* ~~Usar cores mais "vivas" para plotar os gráficos, o que permitirá diferenciar um traço do outro mais facilmente.~~
* Mudar a língua da página para o Português, com opção para outras línguas também.
* ~~Substituir a opção "Display Data" por links que permitam o download dos dados em diferentes formatos, como MATLAB, CSV, Microsoft Excel e outros. Oferecer a opção de baixar todos os dados armazenados ("raw data") ou então dados com decimação, no caso de janelas de tempo grandes.~~
* ~~Diminuir o tamanho dos botões da interface.~~
* Alterar o código de modo que o visualizador possa ser rodado em qualquer computador, e não apenas nos servidores do Grupo de Controle.
* Avaliar a possibilidade de o sistema ser usado não apenas para a visualização de dados armazenados pelo arquivador, mas também de dados em tempo real de variáveis EPICS que não estão sendo arquivadas.
* ~~Atualizar a URL na barra de endereços do navegador web a cada vez que uma nova configuração seja feita no gráfico. Isto permitirá que, após configurar uma visualização, o usuário guarde um link que permitirá retomar a mesma configuração futuramente.~~
* ~~Melhorar o resultado da busca de PVs, limitando o número máximo de PVs exibidas quando o resultado for muito grande e mostrando uma mensagem de aviso quando nenhuma PV for encontrada, por exemplo.~~
* Automatizar o processo de deploy nos servidores do Grupo de Controle quando o software for atualizado no repositório Git.
* ~~Permitir a exibição de dados brutos como uma opção do usuário. Por padrão, exibir dados brutos automaticamente para algumas janelas de tempo maiores, como uma ou duas horas.~~
* ~~Diminuir o tamanho dos logotipos do CNPEM e do LNLS na tela.~~
* ~~Diminuir o tamanho da fonte no quadro de alertas.~~
* ~~Não permitir uma visualização no modo "AUTO" quando a janela de tempo for muito grande (de um ano, por exemplo).~~
* ~~Adicionar botão "Desfazer" para reverter a última configuração feita no gráfico.~~
* Escrever um pequeno guia de uso para funcionar como um menu de ajuda para o usuário do sistema.
* Avaliar o uso de outras bibliotecas JavaScript em substituição à biblioteca Chart.js.
* ~~Aumentar o tamanho vertical da área de plotagem do gráfico.~~
* ~~Resolver o problema que ocorre quando não há nenhuma (ou há poucas) amostras dentro da janela de tempo escolhida. Este problema é muito comum quando se visualiza PVs associadas a números inteiros que indicam status, interlocks etc.~~
* ~~Modificar, se possível, as mensagens nos rótulos dos pontos do gráfico, evitando exibições de números decimais com muitas casas, por exemplo (uma alternativa aqui seria consuldar o campo .PREC do registro EPICS).~~
* Possibilitar que o usuário veja algumas informações da PV, como taxa de aquisição, descrição, precisão etc.
* O eixo vertical deve exibir corretamente a unidade do parâmetro que está sendo plotado. Atualmente ele exibe o nome da PV quando nenhuma unidade está definida e não exibe corretamente a unidade quando ela contém algum caractere de espaço.
* ~~Não exibir mensagem de erro quando nenhum dado de alguma PV for encontrado para uma determinada janela de tempo.~~
* ~~Limitar o número de parâmetros que podem ser plotados simultaneamente em uma mesma janela, exibindo uma mensagem ao usuário quando este limite for atingido.~~
* Pensar em modos de visualização para variáveis que não são números escalares, e sim textos, enumerações ou formas de onda, por exemplo.
* Considerar a possibilidade de mudarmos a [página inicial da nossa instalação do EPICS Archiver](http://10.0.4.57/) da página de gerenciamento para a página de visualização.
* A interface web de visualização parece sempre apresentar estampas de tempo sem nenhuma fração de segundo, o que é inadequado. Várias PVs possuem taxa de aquisição maior do que 1 Hz. Além disso, mesmo para as PVs que não possuem uma taxa de atualização muito rápida, seria interessante a exibição das estampas de tempo na escala do milissegundo, a fim de propiciar uma melhor análise de eventos encadeados, seperados por pequenos intervalos de tempo.
* Pensar em um modo de exibir os dados de grandezas de valor muito baixo (próximo de zero), como as pressões nas câmaras de vácuo (em mbar). Exibir muitos dígitos depois do ponto decimal? Usar escala logarítmica? Notação científica?
* Resolver o problema de limitação no número de casas decimais exibidas quando uma série de dados do tipo ponto flutuante tem baixa variação de valor em uma determinada janela de tempo.

O código-fonte do projeto encontra-se no [GitHub.com](https://github.com/lnls-sirius/archiver-viewer).
