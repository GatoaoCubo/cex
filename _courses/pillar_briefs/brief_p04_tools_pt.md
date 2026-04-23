---
id: kc_pillar_brief_p04_tools_pt
kind: knowledge_card
pillar: P04
title: "P04 Tools — As Mãos Que Alcançam o Mundo"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
quality: 6.6
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p04, tools, mcp, function-calling, agents, retriever, browser-tool, llm-engineering]
tldr: "Brief técnico aprofundado sobre P04 Tools: 36 kinds cobrindo servidores MCP, executores de código, retrievers, ferramentas de comunicação, pipelines de voz — framework universal para uso de ferramentas de IA e capacidade agêntica."
source_concepts: [kc_lens_index, mentor_context, p03_pc_cex_universal]
related:
  - kc_pillar_brief_p04_tools_en
  - kc_pillar_brief_p03_prompt_pt
  - cm_driver_01_structured_thinking
  - kc_lens_factory
  - kc_lens_technical
  - mentor_context
density_score: 0.99
updated: "2026-04-22"
---

# P04 Tools — As Mãos: Como a IA Alcança o Mundo Real

## O Princípio Central: IA Precisa de Mãos

Aqui está o modelo mental mais importante em engenharia de LLM. Imagine a pessoa mais brilhante que você conhece — profundamente conhecedora, raciocínio rápido, articulada, criativa. Agora imagine essa pessoa trancada em uma sala à prova de som, sem janelas, sem telefone, sem computador, sem conexão com o mundo exterior. Ela pode pensar brilhantemente, mas não consegue tocar em nada. Não pode buscar informações. Não pode enviar uma mensagem. Não pode executar um cálculo. Só pode conversar com quem estiver na sala.

Isso é um LLM sem ferramentas.

Agora dê a essa pessoa um celular, um laptop, acesso à internet, a capacidade de enviar e-mails, executar código, consultar bancos de dados e controlar softwares. De repente, essa mesma mente brilhante pode agir sobre o mundo. Ela passa de "aqui está o que eu penso" para "aqui está o que eu fiz."

Isso é um LLM com ferramentas.

**Ferramentas são as mãos, os olhos, a voz e os ouvidos de um agente de IA.** Sem elas, um LLM é um cérebro dentro de um pote — capacidade cognitiva extraordinária, zero capacidade de interagir com o mundo fora da conversa. Com ferramentas, esse mesmo modelo se torna um agente: algo que percebe, raciocina, age e produz resultados no mundo real.

Essa mudança não é incremental. É arquitetural. E se aplica igualmente ao ChatGPT, ao Claude, ao Gemini, a um modelo Llama local rodando no seu computador, ou a qualquer outro LLM com que você trabalhe. O framework neste pilar é universal.

### O Antes e o Depois

**Antes das ferramentas existirem**, toda interação com LLM seguia o mesmo padrão: o usuário pergunta, o LLM responde, a conversa termina. A IA era um preditor de texto muito sofisticado. Seu único resultado eram palavras. Se você precisava que ela fizesse algo de verdade — buscar informação atual, executar um cálculo, salvar um arquivo, enviar uma mensagem — você tinha que fazer isso manualmente e colar o resultado de volta na conversa.

**Depois das ferramentas**, o padrão mudou completamente. A IA agora pode:
- Navegar na web para obter informações atuais
- Executar código e mostrar a saída real, não apenas a saída prevista
- Ler seus documentos e arquivos diretamente
- Enviar mensagens para outros sistemas em seu nome
- Consultar bancos de dados e retornar dados reais
- Lembrar coisas entre sessões por meio de armazenamento externo
- Disparar fluxos de trabalho em outras aplicações

A IA não está mais respondendo à sua pergunta. Ela está executando sua intenção.

### O Loop de Uso de Ferramentas

Todo agente de IA, independentemente do modelo que o alimenta, segue o mesmo loop fundamental ao usar ferramentas:

1. **Planejar**: dado o objetivo do usuário, decidir o que precisa acontecer
2. **Selecionar**: escolher qual ferramenta ou sequência de ferramentas usar
3. **Chamar**: invocar a ferramenta com os parâmetros corretos
4. **Interpretar**: ler e entender a saída da ferramenta
5. **Decidir**: o objetivo foi alcançado? Se sim, sintetizar o resultado. Se não, voltar ao passo 1 com novas informações
6. **Repetir**: a maioria das tarefas reais requer múltiplas chamadas de ferramentas em sequência

Esse loop é o que separa um chatbot de um agente. Um chatbot retorna uma resposta. Um agente itera por esse loop quantas vezes forem necessárias para realmente completar o trabalho.

Entender esse loop é a base de tudo o mais neste pilar.


## As 5 Categorias de Ferramentas de IA — Um Framework Universal

Antes de mergulhar em implementações específicas, aqui está um framework que se aplica a todo sistema de IA com que você vai trabalhar. Independentemente do provedor, modelo ou framework, todas as ferramentas de IA se enquadram em cinco categorias fundamentais. Pense nelas como os cinco tipos de mãos que uma IA pode ter.

### Categoria A: Mãos que CONSTROEM — Ferramentas de Execução

Essas são ferramentas que permitem à IA escrever E executar coisas, não apenas descrevê-las.

**O que fazem**: executam código, manipulam arquivos, consultam bancos de dados, controlam processos, interagem com sistemas operacionais.

**A mudança de jogo**: antes das ferramentas de execução de código, uma IA podia escrever Python. Com ferramentas de execução de código, uma IA pode escrever Python, executá-lo em um sandbox, ver a saída, depurar erros e te dar o resultado final funcionando. A diferença entre "aqui está o código que deveria funcionar" e "aqui está o código funcionando com a saída real" é enorme.

**Funciona com qualquer IA — experimente hoje**:
- No ChatGPT: clique em "Interpreter de Código" (agora chamado "Análise Avançada de Dados"). Faça o upload de um arquivo CSV. Pergunte: "Limpe esses dados, remova duplicatas, encontre as 10 principais linhas por receita e crie um gráfico." A IA acabou de escrever Python, executou e mostrou resultados reais. Sem necessidade de código da sua parte.
- No Claude: use o Claude Code (este terminal que você está usando agora). Peça para ele criar um arquivo, executar um script, verificar informações do sistema. Ele está fazendo tudo isso por meio de ferramentas de execução.
- No Cursor ou GitHub Copilot: o loop inteiro de "execute seus testes e corrija o que falhar" são ferramentas de execução em ação.

**Kinds principais nesta categoria**: `code_executor`, `cli_tool`, `db_connector`, `daemon`, `computer_use`, `diff_strategy`

A decisão de engenharia mais crítica nesta categoria é o sandboxing. Um `cli_tool` que executa comandos shell não tem isolamento — se o comando der errado, dá errado no seu sistema real. Um `code_executor` com isolamento via Docker ou E2B roda em um ambiente contido. A IA pode executar código destrutivo no sandbox sem afetar nada real. Sempre escolha a ferramenta mais fraca que resolve o problema, mas nunca pule o sandbox quando o risco de efeitos colaterais for real.

### Categoria B: Olhos que ENXERGAM — Ferramentas de Percepção

Essas são ferramentas que permitem à IA observar o mundo: ler sites, entender documentos, analisar imagens, processar áudio.

**O que fazem**: navegam em páginas web, extraem texto de PDFs, interpretam screenshots, transcrevem áudio, leem dados estruturados de planilhas.

**A mudança de jogo**: os dados de treinamento de um LLM têm uma data de corte. Sem ferramentas de percepção, a IA está operando a partir da memória — potencialmente desatualizada, definitivamente incompleta. Com ferramentas de percepção, a IA pode ler qualquer página web agora, processar qualquer documento que você entregar a ela e ver qualquer imagem que você compartilhar. Seu conhecimento efetivo se torna tão atual e completo quanto as fontes às quais você dá acesso.

**Funciona com qualquer IA — experimente hoje**:
- Com o ChatGPT ou Claude com navegação habilitada: pergunte "Acesse a página de preços do Stripe e resuma os planos deles comparados com os preços do PayPal." A IA acabou de fazer pesquisa competitiva em 30 segundos lendo dois sites ao vivo.
- Com qualquer IA que aceite PDFs: faça o upload de um contrato, um artigo científico ou um relatório financeiro. Faça perguntas sobre ele. A IA está usando percepção de documentos — ela está lendo esse arquivo do jeito que você leria, extraindo significado de estrutura e conteúdo.
- Com modelos com visão habilitada (GPT-4V, Claude, Gemini): tire um screenshot de uma mensagem de erro, um wireframe de UI ou uma planilha. Cole na conversa. Pergunte o que você quer saber. A IA está usando ferramentas de percepção visual para entender o conteúdo da imagem.

**Kinds principais nesta categoria**: `browser_tool`, `vision_tool`, `document_loader`, `stt_provider`, `search_tool`

A distinção mais importante aqui é entre `search_tool` e `retriever`. Uma ferramenta de busca chama um serviço externo (Tavily, Perplexity, Bing) e retorna resultados web ranqueados — ao vivo, externos, amplitude potencialmente ilimitada, mas você paga por consulta e suas consultas vão para terceiros. Um retriever consulta um armazenamento vetorial local que você controla — privado, rápido, custo fixo, mas só conhece o que você indexou. Sistemas reais geralmente usam os dois: o retriever para seu conhecimento proprietário, a ferramenta de busca para informação externa atual.

### Categoria C: Voz que FALA — Ferramentas de Comunicação

Essas são ferramentas que permitem à IA enviar mensagens, fazer chamadas de API, disparar ações em outros sistemas e interagir com o mundo exterior.

**O que fazem**: enviam e-mails, postam mensagens no Slack ou Discord, chamam APIs REST, disparam webhooks, publicam em redes sociais, enviam notificações push.

**A mudança de jogo**: antes das ferramentas de comunicação, a IA era reativa — só respondia quando você falava com ela. Com ferramentas de comunicação, a IA se torna proativa. Ela pode perceber que algo aconteceu e fazer algo a respeito. Ela pode ser a que entra em contato, não apenas a que responde.

**Funciona com qualquer IA — experimente hoje**:
- Use o Zapier ou Make.com para conectar qualquer IA a mais de 5.000 aplicativos. Construa isso: "Quando um novo e-mail chegar com 'URGENTE' no assunto, use IA para resumir, categorizar e me enviar uma notificação no Slack com o resumo." Zero código. A IA faz a leitura e o resumo; o Zapier cuida da comunicação com Gmail e Slack.
- Construa um webhook: sempre que algo acontecer no seu aplicativo (novo usuário se cadastra, pagamento falha, erro registrado), envie esse evento para um endpoint de IA. A IA lê o evento e decide o que fazer — talvez enviar uma mensagem de suporte, talvez abrir um ticket, talvez apenas registrar. Isso é IA orientada a eventos.
- Use o function calling da OpenAI ou o tool use da Anthropic para dar à sua IA uma função `enviar_email`. Agora quando um usuário perguntar à sua IA "manda um follow-up para as pessoas que não responderam", a IA pode realmente fazer isso em vez de apenas redigir o texto para você.

**Kinds principais nesta categoria**: `api_client`, `webhook`, `notifier`, `messaging_gateway`, `social_publisher`, `event_stream`

### Categoria D: Ouvidos que ESCUTAM — Ferramentas de Entrada

Essas são ferramentas que permitem à IA receber informações de eventos externos, não apenas da entrada direta do usuário.

**O que fazem**: recebem payloads de webhook, processam streams de áudio, monitoram feeds de dados em tempo real, recebem gatilhos agendados.

**A mudança de jogo**: a maioria das interações com IA é iniciada por um humano digitando uma mensagem. Ferramentas de entrada quebram essa restrição. A IA pode agora ser disparada por eventos externos — um pagamento processado, a leitura de um sensor de temperatura, um novo commit enviado ao GitHub, um agendamento cron disparando. A IA se torna parte da sua infraestrutura, não apenas uma interface de chat.

**Funciona com qualquer IA — experimente hoje**:
- Configure um webhook no seu aplicativo que dispara quando um usuário cancela. Faça esse webhook chamar um endpoint de IA com os dados e o motivo do cancelamento do usuário. A IA analisa o cancelamento, redige um e-mail de reativação e coloca na fila para sua revisão. Você construiu um loop de recuperação de churn impulsionado por IA sem nenhuma intervenção manual.
- Use um gatilho agendado (cron) para que uma IA analise seus dados de vendas toda manhã às 7h e te envie um briefing de um parágrafo por e-mail. A IA está iniciando isso, não você.
- Processe entrada de voz por uma ferramenta de fala para texto primeiro, depois para a sua IA. De repente seu aplicativo de IA entende linguagem falada, não apenas texto digitado. Essa é a fundação de todo assistente de voz que importa.

**Kinds principais nesta categoria**: `stt_provider`, `audio_tool`, `webhook` (entrada), `event_stream`, `daemon`

### Categoria E: Memória que PERSISTE — Ferramentas de Armazenamento

Essas são ferramentas que permitem à IA lembrar informações entre sessões, pesquisar em grandes bases de conhecimento e acessar armazenamentos de dados estruturados.

**O que fazem**: armazenam e recuperam informações por significado semântico (busca vetorial), pesquisam em bases de conhecimento indexadas, consultam bancos de dados, acessam sistemas de arquivos.

**A mudança de jogo**: a janela de contexto de um LLM é uma memória de trabalho — o que ele pode manter de uma vez. Sem ferramentas de armazenamento, toda conversa começa do zero. Com ferramentas de armazenamento, a IA pode ter uma memória que cresce ao longo do tempo, pesquisar em documentos que você vem acumulando há anos e recuperar fatos relevantes para a conversa atual mesmo que tenham sido aprendidos meses atrás.

**Funciona com qualquer IA — experimente hoje**:
- Construa um pipeline RAG (Retrieval-Augmented Generation) com LlamaIndex ou LangChain: indexe a documentação da sua empresa, seu histórico de e-mails, suas anotações de projeto. Conecte a qualquer LLM. Agora quando usuários fizerem perguntas, a IA pesquisa sua base de conhecimento primeiro e embasa as respostas nos seus documentos reais. Alucinação cai drasticamente. A precisão para o seu domínio específico sobe drasticamente.
- Use um servidor MCP (veja a próxima seção) para dar à sua IA acesso de leitura ao seu workspace do Notion, Google Drive ou uma pasta local. A IA pode agora pesquisar nos seus arquivos reais para responder perguntas. Ela não está inventando coisas dos dados de treinamento — está lendo suas coisas.
- Configure memória persistente com uma ferramenta como MemGPT ou um banco de dados simples. Cada conversa adiciona ao que a IA sabe sobre você. Após 20 conversas, a IA conhece suas preferências, seus projetos em andamento, seu estilo de comunicação. Ela se torna genuinamente personalizada.

**Kinds principais nesta categoria**: `retriever`, `search_tool`, `knowledge_index`, `document_loader`, `mcp_server`


## A Revolução MCP — USB para IA

De todos os padrões de ferramentas emergindo em engenharia de LLM agora, o MCP — Model Context Protocol — é o que você precisa entender mais profundamente. Ele está mudando a arquitetura das ferramentas de IA da mesma forma que o USB mudou a arquitetura da conectividade de dispositivos.

### O Problema Antes do MCP

Antes do MCP, conectar uma IA a uma ferramenta externa significava escrever código de integração personalizado — toda vez, para cada combinação de modelo de IA e ferramenta. O Claude precisava do formato de tool-use da Anthropic. O GPT precisava do formato de function-calling da OpenAI. O Gemini precisava do formato do Google. Se você queria que sua IA acessasse seu repositório GitHub, você escrevia código de integração com o GitHub. Se também queria que ela acessasse seu banco de dados, escrevia código de integração com o banco de dados. E escrevia tudo isso separadamente para cada modelo de IA que pudesse querer suportar.

Esse era o mundo pré-USB da IA. Cada dispositivo precisava do seu próprio cabo proprietário.

### O Que o MCP Faz

O MCP define um protocolo universal: uma forma padrão para qualquer cliente de IA (Claude, ChatGPT, Gemini, modelos Ollama locais, qualquer coisa) se conectar a qualquer servidor de ferramentas. O servidor expõe suas capacidades. A IA as descobre. A IA as chama com argumentos estruturados. O servidor retorna resultados estruturados. Nenhum dos dois precisa saber nada sobre a implementação do outro.

A analogia com o USB é precisa: assim como o USB permitiu que qualquer dispositivo com porta USB se conectasse a qualquer computador com porta USB — independentemente do fabricante, sistema operacional ou o que o dispositivo faz — o MCP permite que qualquer IA compatível com MCP se conecte a qualquer servidor de ferramentas compatível com MCP.

Essa é a padronização que vai definir a próxima geração de ferramentas de IA.

### Como o MCP Funciona na Prática

Um servidor MCP é um software que:
1. Inicia e registra suas capacidades (quais ferramentas fornece, quais dados pode acessar)
2. Aguarda solicitações de um cliente de IA
3. Recebe chamadas estruturadas com argumentos
4. Executa a operação solicitada
5. Retorna resultados estruturados

Um cliente MCP (sua IA) é um software que:
1. Descobre quais ferramentas o servidor expõe
2. Inclui essas capacidades no conjunto de ferramentas disponíveis da IA
3. As chama quando o raciocínio da IA determina que são necessárias
4. Processa os resultados como observações no loop de raciocínio da IA

Exemplos reais de servidores MCP que você pode usar hoje:
- **GitHub MCP**: sua IA pode ler seus repositórios, issues, pull requests e histórico de commits. Pergunte ao Claude: "Quais são os tipos de erros mais comuns nos nossos logs de erro nos últimos 30 dias?" e ele pode realmente ir ler suas issues do GitHub para responder.
- **Slack MCP**: sua IA pode ler e enviar mensagens do Slack. Seu assistente de IA pode agora pesquisar no histórico do Slack da sua empresa para encontrar contexto para uma pergunta.
- **Filesystem MCP**: sua IA pode ler e escrever arquivos na sua máquina local. É isso que permite ao Claude Code editar os arquivos reais do seu projeto.
- **Database MCP**: sua IA pode executar consultas SQL no seu banco de dados. Faça perguntas sobre seus dados em linguagem natural; a IA descobre a query e retorna os resultados.
- **Notion/Google Drive MCP**: sua IA pode pesquisar nas suas bases de conhecimento e documentos.

### Por Que o MCP Importa para Você Agora

Se você trabalha com IA e ainda não usa MCP, aqui está a implicação prática: cada servidor MCP que você configura multiplica o que sua IA pode fazer. Uma vez que você configura o Claude (ou qualquer cliente compatível com MCP) com um conjunto de servidores MCP, você deu a essa IA acesso a todas essas capacidades. Você não escreveu código de integração personalizado. Você não mudou o modelo de IA. Você apenas conectou algumas mãos.

O artefato `mcp_server` do CEXAI especifica:
- `transport`: `stdio` (processo local) ou `http_sse` (remoto pela rede)
- `tools_provided`: a lista de funções chamáveis que o servidor expõe
- `resources_provided`: fontes de dados que a IA pode ler

Esse é o padrão. Defina a capacidade, declare o transporte, especifique as ferramentas. Qualquer IA compatível com MCP pode pegá-lo e começar a usar.


## Os 36 Kinds do P04 — Um Mapa Completo das Mãos da IA

Todos os 36 kinds no P04 estão organizados em cinco subcategorias. Cada kind é uma definição de artefato tipada e versionada com um papel definido no sistema. Cada kind tem um builder dedicado para criar instâncias com finalidade específica.

### Ferramentas de Execução (9 kinds)

| Kind | Finalidade | Quando Usar | Complexidade |
|------|-----------|-------------|--------------|
| `cli_tool` | Wrapper de comando shell único | Chamadas de subprocesso simples; sandbox não necessário | Baixa |
| `code_executor` | Runtime isolado (Docker, E2B, Jupyter) | Código gerado por LLM que precisa rodar com segurança | Alta |
| `db_connector` | Acesso SQL/GraphQL/REST-to-DB | Consultas a dados estruturados em qualquer banco | Média |
| `supabase_data_layer` | Supabase: tabelas + RLS + edge functions | Produtos baseados em Supabase com RLS aplicado | Média |
| `computer_use` | Automação de GUI: tela, teclado, mouse | Apps desktop sem API; último recurso | Alta |
| `diff_strategy` | Algoritmo de aplicação e correspondência de mudanças | Patching de código, resolução de conflitos de merge | Média |
| `daemon` | Processo em background persistente | Serviços de longa duração, watchers, loops de polling | Alta |
| `hook` | Hook de pré/pós-processamento | Efeitos colaterais orientados a eventos em pontos de ciclo de vida conhecidos | Baixa |
| `hook_config` | Configuração declarativa do ciclo de vida de hooks | Orquestração de hooks no nível do builder | Baixa |

Distinção fundamental: `cli_tool` termina após cada chamada; `daemon` persiste entre chamadas. `code_executor` usa sandbox; `cli_tool` não. Use a ferramenta mais fraca que resolve o problema — sandboxing desnecessário desperdiça latência e processamento.

### Ferramentas de Comunicação (9 kinds)

| Kind | Finalidade | Quando Usar | Complexidade |
|------|-----------|-------------|--------------|
| `mcp_server` | Servidor MCP expondo tools + resources | Qualquer ferramenta que deva ser compartilhada entre clientes LLM | Alta |
| `mcp_app_extension` | Ciclo de vida de app MCP: instalar/lançar/encerrar | Empacotar ferramentas como apps MCP descobríveis | Alta |
| `webhook` | Endpoint HTTP orientado a eventos (entrada/saída) | Receber eventos externos ou enviar notificações | Média |
| `messaging_gateway` | Mensagens bidirecionais multiplataforma | Sessão unificada Telegram/Discord/Slack/WhatsApp | Alta |
| `notifier` | Notificação push unidirecional (email, SMS, Slack) | Alertas sem contexto de conversa | Baixa |
| `api_client` | Cliente tipado REST/GraphQL/gRPC | Chamadas de saída para APIs externas | Média |
| `agent_name_service_record` | Registro IETF ANS para descoberta de agentes | Redes multiagente; roteamento A2A | Média |
| `event_stream` | Configuração de sequência de eventos de domínio em tempo real | Feeds pub/sub; pipelines de processamento de streams | Alta |
| `social_publisher` | Pipeline completo de publicação em redes sociais | Publicação autônoma de conteúdo | Alta |

O `messaging_gateway` é arquiteturalmente notável. Ele mantém conexões simultâneas em múltiplas plataformas sob um único modelo de sessão — a mesma identidade, a mesma memória, independentemente de se o usuário está conversando com sua IA no Telegram, Discord ou Slack em determinado momento.

### Ferramentas de Pesquisa e Conhecimento (6 kinds)

| Kind | Finalidade | Quando Usar | Complexidade |
|------|-----------|-------------|--------------|
| `research_pipeline` | Motor de 7 estágios: INTENT→PLAN→RETRIEVE→RESOLVE→SCORE→SYNTHESIZE→VERIFY | Coleta profunda de inteligência; síntese multifonte | Alta |
| `search_tool` | Busca web/semântica/híbrida (Tavily, Serper, Perplexity) | Recuperação de informação externa | Baixa |
| `retriever` | Busca vetorial/keyword/híbrida local (núcleo do RAG) | Consultas à base de conhecimento local | Média |
| `document_loader` | Ingestão e chunking de arquivos (PDF, HTML, CSV) | Transformar arquivos em chunks prontos para recuperação | Média |
| `search_strategy` | Alocação de compute de inferência para busca | RAG multi-pass; trade-offs entre dense e sparse | Média |
| `browser_tool` | Playwright/Puppeteer: navegação DOM, screenshots | Páginas com JS pesado onde fetch estático falha | Alta |

O `research_pipeline` é qualitativamente diferente de `search_tool`. Uma ferramenta de busca faz uma chamada e retorna resultados ranqueados. Um pipeline de pesquisa executa sete estágios mediados por LLM e produz um artefato de conhecimento citado e com pontuação de qualidade. O campo `min_sources` é uma restrição rígida — o pipeline não avançará para a síntese até que um número mínimo de fontes distintas tenha sido recuperado e resolvido, evitando que o LLM fabrique evidências.

### Ferramentas de Mídia e Multimodalidade (6 kinds)

| Kind | Finalidade | Quando Usar | Complexidade |
|------|-----------|-------------|--------------|
| `vision_tool` | Análise de imagem, OCR, interpretação de screenshots | Extração de dados visuais; compreensão de layout | Média |
| `audio_tool` | STT/TTS/análise de áudio (combinado) | I/O de áudio quando o provedor ainda não foi escolhido | Baixa |
| `tts_provider` | Contrato de provedor text-to-speech | Identidade vocal estável para uma persona ou produto | Média |
| `stt_provider` | Contrato de provedor speech-to-text | Camada de transcrição para pipelines de voz | Média |
| `voice_pipeline` | Arquitetura completa STT→LLM→TTS | Agente de conversa falada de ponta a ponta | Alta |
| `multi_modal_config` | Formato de entrada, resolução, codificação e regras de roteamento | Configurar como entradas multimodais fluem para LLMs | Baixa |

Esses kinds formam uma pilha de mídia composável. `stt_provider` e `tts_provider` são os componentes atômicos; `voice_pipeline` os conecta com um LLM como o cérebro, especificando metas de latência, tratamento de interrupções e protocolo de tomada de turno.

### Ferramentas de Integração e Extensão (6 kinds)

| Kind | Finalidade | Quando Usar | Complexidade |
|------|-----------|-------------|--------------|
| `toolkit` | Bundle de ferramentas com JSON Schema automático | Atribuir um ambiente completo de ferramentas a um agente | Média |
| `function_def` | Função chamável por LLM (JSON Schema tool) | Definições individuais de capacidade chamável | Baixa |
| `skill` | Capacidade reutilizável com trigger + fases | Comportamentos lazy de auto-disparo; handlers de slash commands | Média |
| `plugin` | Extensão plugável do sistema | Extensões com ciclo de vida além de um único evento | Média |
| `action_paradigm` | Contrato de execução ReAct/Plan-Execute/orientado a eventos | Definir como um agente interage com seu ambiente de ferramentas | Alta |
| `sdk_example` | Código de exemplo de SDK por linguagem | Referência para desenvolvedores; reduz fricção de integração | Baixa |


## Padrões de Engenharia Fundamentais

### Function Calling — A Fundação do Uso de Ferramentas

Antes do MCP se tornar difundido, a forma como a maioria dos LLMs usava ferramentas era por meio de function calling (termo da OpenAI) ou tool use (termo da Anthropic). O conceito é o mesmo em todos os provedores.

Você define uma função com uma descrição em JSON Schema: como a função se chama, quais argumentos ela recebe, o que cada argumento significa. Você inclui isso na solicitação de API junto com a mensagem do usuário. O LLM lê a definição da função e, quando determina que a função seria útil, produz uma chamada estruturada — não uma resposta, mas uma instrução para chamar aquela função específica com argumentos específicos. Seu código intercepta isso, realmente chama a função e alimenta o resultado de volta para o LLM. O LLM então continua seu raciocínio com esse resultado.

Esse é o mecanismo fundamental por trás de todo "uso de ferramentas de IA" que você vê em produtos hoje.

**Exemplo prático na API da OpenAI**:
```python
tools = [{
    "type": "function",
    "function": {
        "name": "obter_clima_atual",
        "description": "Obtém o clima atual para uma localização",
        "parameters": {
            "type": "object",
            "properties": {
                "localizacao": {
                    "type": "string",
                    "description": "Cidade e estado, ex: São Paulo, SP"
                }
            },
            "required": ["localizacao"]
        }
    }
}]
```

Quando o usuário pergunta "O que devo vestir em Paris hoje?", o LLM não chuta. Ele chama `obter_clima_atual(localizacao="Paris, França")`, recebe a temperatura real e dá uma resposta fundamentada.

O campo `description` de cada parâmetro não é documentação para humanos. É engenharia de prompt dentro de um schema — o LLM lê isso para entender o que passar. Se a descrição for ambígua, o LLM vai passar argumentos errados. Escreva descrições como se estivesse escrevendo instruções para um colega inteligente mas literal que nunca viu a função antes.

### O Padrão Toolkit — Gerenciando Ambientes de Ferramentas

Um `toolkit` é o artefato que responde "a quais ferramentas este agente tem acesso?". Ele agrupa múltiplas definições de ferramentas em um pacote nomeado e versionado que pode ser atribuído a um agente na inicialização. O flag `auto_schema: true` aciona a geração automática de JSON Schema a partir de todas as definições de ferramentas incluídas, para que o LLM receba um schema consistente e completo sem manutenção manual.

Exemplo de toolkit para um agente de coleta de inteligência:
```yaml
id: tk_n01_intelligence_tools
kind: toolkit
pillar: P04
nucleus: n01
auto_schema: true
max_parallel_calls: 5
tools:
  - st_tavily_web_search
  - ret_cex_tfidf_local
  - dl_pdf_semantic_chunker
  - ct_git_ops
```

O campo `max_parallel_calls` é um limite de segurança importante. Sem ele, um loop ReAct com ferramentas de busca pode gerar dezenas de chamadas concorrentes sob pressão de latência, esgotando cotas de API e criando condições de corrida. Sempre defina limites explícitos para o fan-out de ferramentas.

### O Paradigma de Ação — Como Agentes Usam Ferramentas

O kind `action_paradigm` codifica como os loops de uso de ferramentas operam. Existem quatro padrões fundamentais, cada um com trade-offs distintos:

**ReAct (Reason + Act)**: o agente intercala passos de raciocínio com chamadas de ferramentas. "Preciso saber o preço atual. Vou chamar a ferramenta de busca. Ok, o preço é X. Agora preciso compará-lo com Y. Vou chamar a ferramenta de banco de dados." Esse é o padrão mais comum. Alta transparência, latência ligeiramente maior porque cada passo de raciocínio é uma chamada separada ao LLM.

**Plan-Execute**: o agente gera um plano completo primeiro — "vou chamar as ferramentas A, B, C em sequência" — e depois executa todas as chamadas sem raciocínio intercalado. Mais rápido para workflows determinísticos. Arriscado quando o ambiente é dinâmico e os resultados iniciais mudam o que os passos posteriores devem fazer.

**Orientado a Eventos**: chamadas de ferramentas são disparadas por sinais de entrada, não por passos de raciocínio do LLM. Um webhook dispara, um evento agendado aciona, a leitura de um sensor chega — o agente responde. Esse é o padrão para daemons e processos em background.

**Reflexion**: o agente faz uma chamada de ferramenta, lê o resultado, critica seu próprio raciocínio e decide se deve tentar uma abordagem diferente antes de continuar. A mais alta qualidade para tarefas de pesquisa complexas. A mais cara. Use quando a precisão importa mais do que o custo.

O campo `observation_format` em uma definição de paradigma de ação especifica como a saída da ferramenta é estruturada para o LLM. Formatos de saída estruturados — `{"tool": "busca", "result": [...], "error": null}` — deixam o LLM raciocinar diretamente a partir dos dados. Saída de texto não estruturado exige que o LLM primeiro analise antes de raciocinar, adicionando um passo propenso a erros.

### Skills — Comportamentos de Auto-Disparo

O kind `skill` difere do `function_def` em uma dimensão crítica: a condição de disparo. Uma definição de função é chamada explicitamente por um passo de raciocínio do LLM — o modelo decide chamá-la. Um skill dispara automaticamente quando seu padrão de trigger é detectado, sem que o LLM precise raciocinar sobre se deve usá-lo.

Esse é o padrão por trás de: auto-completar em editores de código, handlers de slash commands em bots do Slack, comportamentos do tipo "quando você detectar X, faça Y automaticamente".

Skills têm dois modos de carregamento: `lazy: true` significa que o skill carrega no primeiro trigger (economiza espaço na janela de contexto na inicialização); `lazy: false` significa que carrega na inicialização. O carregamento lazy é o padrão porque carregar todos os skills possíveis na inicialização infla a janela de contexto sem benefício até que o trigger dispare.


## Segurança e Guardrails — Poder Requer Limites

Ferramentas dão poder à IA. Poder requer limites explícitos. Isso não é opcional.

Uma IA com acesso de escrita ao banco de dados pode também deletar seu banco de dados. Uma IA que pode enviar e-mails pode fazer spam para toda a sua lista de contatos. Uma IA com acesso ao shell pode executar `rm -rf /`. Esses não são riscos hipotéticos — são exatamente o que acontece quando ferramentas são dadas sem fronteiras de segurança.

O framework CEXAI separa a definição de capacidade (P04) das restrições de permissão (P09 Configuração). O artefato P04 descreve o que uma ferramenta PODE fazer. A configuração P09 descreve o que ela tem PERMISSÃO para fazer em um contexto de implantação específico.

Essa separação é crítica por dois motivos. Primeiro, significa que a mesma definição de ferramenta pode ser implantada com diferentes níveis de permissão em contextos diferentes — um ambiente de desenvolvimento com acesso amplo, um ambiente de produção com acesso restrito. Segundo, significa que permissões não podem ser definidas por acidente dentro de uma descrição de ferramenta. Elas são artefatos explícitos, revisados e versionados.

### O Padrão Sandbox

Quando uma IA executa código, sempre use sandbox. Isso significa executar o código em um ambiente isolado — um container Docker, um sandbox na nuvem como E2B, um kernel Jupyter — onde ele não pode afetar o sistema host. Se a IA escrever código malicioso ou com bugs, apenas o sandbox quebra. Seu sistema real fica intocado.

O kind `code_executor` codifica esse padrão. Um executor de código definido corretamente especifica:
- `runtime`: qual tecnologia de sandboxing usar
- `timeout_seconds`: tempo máximo de execução (previne loops infinitos)
- `resource_limits`: CPU, memória, acesso à rede (previne esgotamento de recursos)

Um executor de código sem limites de recursos pode esgotar a memória do host. Um executor de código sem timeout pode rodar para sempre. Esses não são casos extremos — são rotineiros em código gerado por LLM.

### O Padrão Human-in-the-Loop

Para ações de alto risco — enviar dinheiro, deletar dados, contatar clientes, postar publicamente — exija aprovação humana antes que a IA aja. Não é uma questão de confiança. É uma questão de gerenciamento de risco. Mesmo uma IA altamente precisa cometendo erros em 1% das ações é muito alta quando os erros envolvem transferência de fundos ou exclusão de dados de clientes.

O kind `revision_loop_policy` codifica quantas vezes uma IA pode tentar uma chamada de ferramenta e avaliar o resultado antes de exigir revisão humana. Defina isso explicitamente. Nunca deixe ilimitado.

### O Padrão de Rate Limit

Toda API externa tem limites. Uma IA em um loop agêntico pode esgotar cotas de API em segundos se as chamadas de ferramentas não forem limitadas. O kind `api_client` codifica o contrato de limitação de taxa explicitamente — não como comentário, como campo legível por máquina:

```yaml
retry_policy:
  tool_error: {max: 3, backoff: exponential}
  rate_limit: {max: 5, backoff: honor_retry_after}
  auth_error: {max: 1, backoff: none}
```

O caso `auth_error` é importante: falhas de autenticação não são transitórias. Tentar novamente desperdiça tempo e pode acionar bloqueios de conta. Falhe rápido em erros de autenticação; tente novamente apenas em erros transitórios.

### Segurança MCP — Somente Leitura por Padrão

Servidores MCP podem expor capacidades de leitura e escrita. O princípio de segurança é: comece com somente leitura, adicione permissões de escrita explicitamente e deliberadamente.

O servidor MCP do GitHub no CEXAI aplica isso com uma lista de permissões de operações permitidas — apenas operações `get_*`, `list_*` e `search_*`. Todas as operações de mutação são negadas no nível de permissão, não por confiança no julgamento do LLM. Um LLM pode decidir que "deveria" criar um branch ou fazer merge de um PR. O sistema de permissões garante que não possa, independentemente do seu raciocínio.

O kind de gateway de mensagens aplica o mesmo princípio no nível humano: `dm_pairing: true` exige que um usuário inicie o primeiro contato antes que o agente aceite comandos. Isso previne injeção de comandos de usuários arbitrários que encontrem o endereço do seu bot.


## Arquitetura: Como Ferramentas Conectam ao Resto do Sistema

P04 é onde o agente alcança o mundo exterior, mas não opera em isolamento. Toda definição de ferramenta se conecta a outras partes do sistema em relacionamentos específicos e tipados.

### Descoberta de Ferramentas: o Registro de Capacidades

P04 define ferramentas. P08 (Arquitetura) fornece o índice. O `capability_registry` é a tabela de consulta autoritativa para todos os agentes disponíveis e suas capacidades de ferramentas. Quando um orquestrador planeja qual agente atribuir a uma tarefa, consulta o registro de capacidades para encontrar quais agentes podem lidar com quais tipos de chamadas de ferramentas — não varrendo todas as definições de ferramentas, mas por meio de um índice pré-computado.

Essa separação é deliberada: definições são a fonte de verdade para o que uma ferramenta é; o registro é um índice otimizado para decisões de roteamento. O registro pode sempre ser reconstruído a partir do P04 a qualquer momento, mas o roteamento não paga o custo de varrer tudo em cada decisão.

### A Ponte de Prompt

Ferramentas são definidas em P04 mas chamadas a partir de artefatos P03 (Prompt). Uma chain de prompts executa múltiplos passos em sequência, e cada passo pode incluir chamadas de ferramentas. A ponte entre os dois é o JSON Schema: as definições de parâmetros do artefato `function_def` se tornam o schema que o LLM vê em seu contexto de uso de ferramentas. Escreva essas definições com tanto cuidado quanto você escreve instruções de prompt — elas são engenharia de prompt dentro de um schema.

### O Fio do Guardrail

Os resultados de chamadas de ferramentas alimentam avaliadores P11 (Feedback) antes de chegar ao LLM:
- Um guardrail pode inspecionar resultados de busca e rejeitar conteúdo não permitido antes que o LLM o veja
- Um bugloop impulsiona um executor de código em loop até que a saída de execução satisfaça um quality gate
- Uma revision_loop_policy define o número máximo de iterações de chamada-de-ferramenta-avaliação antes de forçar revisão humana

Isso cria um loop de feedback completo: ferramentas executam, avaliadores analisam a saída, e o pipeline avança ou itera. É assim que você evita que um agente de IA reintente infinitamente chamadas de ferramentas com falha ou consuma saída de ferramenta ruim.


## Exemplos Reais do Repositório

### 1. Stack de Scraping de Marketplace (Inteligência Comercial)

A composição de pipeline de pesquisa e ferramenta de navegador em `N00_genesis/P04_tools/` demonstra como ferramentas de percepção e pesquisa se combinam. O pipeline de pesquisa define 8 estágios (estendendo os 7 canônicos com um estágio de síntese específico da marca) e referencia a ferramenta de navegador como sua camada de execução.

Decisões de engenharia fundamentais codificadas no artefato: limitação de taxa (1 solicitação por segundo por domínio, 5 concorrentes globalmente), scraping respeitoso (User-Agent transparente, conformidade com robots.txt) e um contrato de saída tipado (linha na tabela de inteligência de mercado mais digest LLM diário). A ferramenta de navegador especifica Playwright com justificativa explícita sobre Puppeteer — melhor interceptação de rede e semânticas de auto-wait — mais limites de recursos e contrato de interface com assinaturas TypeScript.

Esse é o padrão de codificar decisões como artefatos em vez de deixá-las em comentários ou na memória do desenvolvedor.

### 2. API Client Shopify (Integração E-commerce)

O exemplo de `api_client` de nível produção mostra como decisões de negócio se tornam política legível por máquina: limitação de taxa como um contrato de leaky bucket (1000 cost points, 50 restaurados por segundo, emitindo a métrica `shopify.rate_limit.remaining`), uma regra de reparo de UTF-8 aplicada apenas no caminho de leitura e uma estratégia de retry que distingue entre erros de rede (backoff exponencial), rate limits (honrar o cabeçalho Retry-After) e erros de cliente (falha rápida).

Variáveis de template de marca (`{{BRAND_SHOPIFY_API_VERSION}}`, `{{BRAND_SHOPIFY_ADMIN_TOKEN}}`) fazem com que a mesma definição de artefato sirva qualquer loja Shopify. A referência ao token aponta para um nome de variável de ambiente, nunca para a credencial real.

### 3. TTS de Persona de Marca (Identidade Vocal)

O exemplo de `tts_provider` mostra como uma decisão de identidade vocal — qual voz representa sua marca — se torna um artefato governado em vez de uma string hardcoded. O identificador de voz é uma variável de configuração de marca. A voz de fallback para quando a voz primária falhar está explicitamente definida. Regras de seleção são declaradas em linguagem natural: "Rejeitar vozes que distorcem nomes de produtos ou frases de CTA."

Esse padrão — codificar política de negócio como restrições de artefato — é o que separa P04 de configuração ad hoc de ferramentas.

### 4. Segurança do Gateway de Mensagens (Arquitetura HERMES)

O template do gateway de mensagens mostra campos de segurança como requisitos de artefato de primeira classe, não comentários opcionais. O requisito `dm_pairing: true` força um usuário a iniciar o primeiro contato antes que o agente aceite comandos. O campo `rate_limit_per_user_per_min: 30` limita a velocidade com que qualquer usuário pode interagir. Os campos `command_approval_list: []` e `allowed_user_ids: []` começam vazios e devem ser explicitamente preenchidos — negar por padrão, permitir por exceção.


## Anti-Padrões como Erros Universais

Esses erros não são específicos a nenhuma plataforma. Aparecem em todo sistema de IA que usa ferramentas.

**Dar ferramentas à IA sem fronteiras de segurança** é como dar uma furadeira elétrica para uma criança. A ferramenta é poderosa. O usuário da ferramenta pode não ter o julgamento para usá-la com segurança em toda situação. Limites não são falta de confiança — são engenharia responsável.

**Não testar as saídas de ferramentas antes de confiar nelas** é a fonte da maioria das falhas de IA em produção. Chamadas de ferramentas podem retornar resultados parciais, dados malformados, informações desatualizadas ou erros explícitos. Uma camada de guardrail que valida a saída da ferramenta antes que o LLM raciocine a partir dela não é overhead — é a diferença entre um agente que funciona de forma confiável e um que falha de forma espetacular.

**Construir integrações personalizadas quando o MCP ou protocolos padrão existem** é o erro pré-USB aplicado à IA. Cada hora que você passa escrevendo código de integração sob medida é dívida técnica que o MCP teria evitado. Verifique servidores MCP existentes antes de construir integrações de ferramentas personalizadas.

**Tratar ferramentas como opcionais** é o erro mais comum e mais custoso. Desenvolvedores que pensam em ferramentas de IA como "recursos avançados" constroem chatbots quando precisam de agentes. Ferramentas não são melhorias opcionais — são a camada arquitetural que separa um sistema que sugere de um sistema que age. Se sua IA precisa produzir resultados (não apenas texto), ela precisa de ferramentas.

**Definições monolíticas de ferramentas** — uma função grande que faz muitas coisas — criam acoplamento frágil e tornam granularidade de permissão impossível. O padrão correto: cada definição de função faz uma coisa com um schema estreito e tipado. Definições relacionadas são agrupadas em toolkits. Toolkits são atribuídos a agentes. A configuração P09 restringe quais toolkits cada agente tem permissão para usar.

**Ignorar o tratamento de erros** em definições de ferramentas força cada chamador a inventar seu próprio tratamento de erros, criando inconsistência. Chamadas de ferramentas falham rotineiramente em produção — timeouts de rede, rate limits de API, respostas malformadas, erros de autenticação. Codifique a política de retry na definição da ferramenta, não no código de chamada.


## Conexão com Outros Pilares

Ferramentas P04 não operam em isolamento. Toda ferramenta se conecta a outras partes do sistema por meio de relacionamentos tipados:

| Origem | Destino | Relação | Mecanismo |
|--------|---------|---------|-----------|
| P04 `toolkit` | P02 `agent` | alimenta | agent.tools referencia o ID do toolkit |
| P04 `function_def` | P03 `chain` | chamado de | passos da chain incluem nós tool_call |
| P04 `mcp_server` | P08 `capability_registry` | indexado por | registry armazena todos os endpoints mcp_server |
| P04 `code_executor` | P09 `sandbox_config` | restrito por | P09 define limites de recursos e política de rede |
| P04 `retriever` | P01 `chunk_strategy` | consome saída de | retriever consulta chunks indexados pela estratégia P01 |
| P04 `research_pipeline` | P01 `knowledge_card` | produz | estágio SYNTHESIZE gera um knowledge_card |
| P04 `browser_tool` | P11 `guardrail` | saída avaliada por | guardrails inspecionam saída da ferramenta antes do uso pelo LLM |
| P04 `social_publisher` | P12 `schedule` | disparado por | artefato schedule aciona social_publisher via cron |
| P04 `skill` | P03 `instruction` | referencia | fases do skill citam artefatos de instrução |
| P04 `voice_pipeline` | P04 `stt_provider` + `tts_provider` | compõe | pipeline conecta os três componentes |

O padrão mais importante: ferramentas P04 são definidas uma vez na arquitetura canônica e instanciadas por agente. Um agente de coleta de inteligência tem sua própria instância de `retriever` ajustada para pesquisa competitiva. Um agente de gestão de conhecimento tem um `retriever` diferente ajustado para consultas à base de conhecimento interna. Ambos herdam do mesmo schema P04. Ambos são pontuados contra o mesmo rubric. Mas são artefatos distintos e propositalmente ajustados — a mesma mão, segurando ferramentas diferentes.

P04 não é uma biblioteca de ferramentas que você copia e cola. É uma fábrica tipada, governada e com pontuação de qualidade para capacidades externas. De uma biblioteca você copia; de uma fábrica você opera.

A verdade central deste pilar é simples: todo resultado que sua IA produz que importa para o mundo real exigiu uma ferramenta para acontecer. A qualidade da sua engenharia de ferramentas determina a qualidade do impacto do seu agente. Construa bem as mãos, e a brilhância do cérebro finalmente poderá alcançar o mundo.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_pillar_brief_p04_tools_en]] | translation | 1.00 |
| [[kc_pillar_brief_p03_prompt_pt]] | sibling | 0.85 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.50 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[kc_lens_technical]] | upstream | 0.42 |
| [[mentor_context]] | upstream | 0.38 |
