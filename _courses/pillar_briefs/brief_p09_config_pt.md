---
id: kc_pillar_brief_p09_config_pt
kind: knowledge_card
pillar: P09
title: "P09 Config — O Sistema Nervoso da Sua IA"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
quality: 7.0
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p09, config, runtime, secrets, rate-limits, llm-engineering]
tldr: "P09 Config governa o comportamento em runtime sem alterar o modelo — variáveis de ambiente, secrets, rate limits, RBAC, orçamentos de raciocínio e specs de sandbox."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p09_config_en
  - kc_pillar_brief_p08_architecture_pt
  - kc_pillar_brief_p10_memory_pt
  - kc_pillar_brief_p11_feedback_pt
  - n00_p09_kind_index
density_score: 1.0
updated: "2026-04-22"
---

# P09 Config — O Sistema Nervoso da Sua IA: Configurações Que Controlam o Comportamento Sem Tocar no Cérebro

---

## O Princípio Universal: O Comportamento Vive Fora do Modelo

Existe um fato contraintuitivo que todo praticante de IA aprende da forma difícil: **a maior parte do que faz um sistema de IA se comportar de maneira diferente em produção versus desenvolvimento não tem nada a ver com o modelo em si.** Os pesos são fixos. A arquitetura é fixa. O que muda é o ambiente operacional — a camada de configuração que envolve o modelo e controla como ele é executado.

P09 Config é esse ambiente operacional. A metáfora do sistema nervoso é precisa: o seu sistema nervoso não muda a estrutura do seu cérebro quando você entra numa sala fria ou numa reunião estressante — ele ajusta os parâmetros que governam como o cérebro opera naquele contexto. Cortisol elevado. Fluxo sanguíneo restrito. Sensibilidade aumentada a ameaças. O cérebro executa os mesmos cálculos subjacentes; o ambiente modula as saídas.

Sistemas de IA funcionam de forma idêntica. Um modelo Claude ou GPT-4 rodando com `thinking_config` definido como `budget_tokens: 100` produz respostas rasas e rápidas. O mesmo modelo com `budget_tokens: 10000` produz chain-of-thought profundo e deliberado. O modelo não mudou. A configuração mudou. Um `rate_limit_config` com `concurrent_requests: 20` mantém seu grid estável. Sem ele, você tem cascatas de 429 que podem matar uma execução noturna.

Isso não é específico do CEXAI. Todo framework LLM importante — LangChain, LlamaIndex, CrewAI, AutoGen, OpenAI Assistants — tem uma camada de configuração. P09 é a taxonomia sistemática dessa camada: **30 tipos distintos cobrindo cada dimensão do comportamento em runtime que importa em sistemas de IA em produção.**

O princípio universal: **separe configuração de código, e separe configuração de runtime da identidade do modelo.** A identidade de um agente (P02) responde "quem sou eu". Os prompts do agente (P03) respondem "como eu respondo". A configuração do agente (P09) responde "sob quais restrições operacionais eu executo". Essas são três preocupações ortogonais, e conflacioná-las é a causa mais comum de sistemas de IA frágeis.

**A consequência prática:** se o seu sistema de IA se comporta de forma diferente em produção do que em desenvolvimento, o diagnóstico quase sempre aponta para um artefato P09 ausente ou incompatível. Variáveis de ambiente erradas. Rate limits não documentados. Secrets hardcoded em prompts. Deriva de configuração entre ambientes. P09 existe para tornar esses problemas visíveis, versionados e sistemáticos.

---

## O Que Este Pilar Faz

P09 Config governa o contexto operacional em que os agentes executam — as regras do ambiente em vez das regras do agente. Ele responde a três categorias de perguntas:

**Limites operacionais:** Com que velocidade este agente pode executar? Quanto pode gastar? Quais recursos pode acessar? Isso cobre `rate_limit_config`, `cost_budget`, `usage_quota` e `effort_profile`.

**Perímetro de segurança:** Quem pode acessar este agente? Quais credenciais ele usa? Como essas credenciais são rotacionadas? Isso cobre `secret_config`, `permission`, `rbac_policy`, `sso_config`, `oauth_app_config` e `sandbox_config`.

**Ajuste de comportamento em runtime:** Quanto este agente pensa antes de responder? Quais regras de runtime governam retentativas e timeouts? Em qual ambiente de execução ele opera? Isso cobre `thinking_config`, `runtime_rule`, `terminal_backend` e `hibernation_policy`.

No pipeline 8F, os artefatos P09 servem predominantemente às funções LLM GOVERN (F7) e CONSTRAIN (F1). Eles são contratos passivos — descrevem restrições em vez de produzir conteúdo. Você não escreve um artefato P09 durante a geração — você lê artefatos P09 no F1 para entender quais restrições o runtime impõe, e valida contra eles no F7 para garantir que a saída produzida respeita essas restrições.

O insight arquitetural crítico: **P09 é a camada de convenção-sobre-configuração.** Em vez de hardcodar `rpm = 50` dentro da sua classe de agente, você escreve um artefato `rate_limit_config`. Qualquer agente pode lê-lo. Qualquer runtime pode aplicá-lo. Qualquer operador pode atualizá-lo sem tocar no código do agente.

---

## Os 30 Tipos em P09 — Referência Universal de Capacidades

| Tipo | Capacidade Universal | Importância em Produção |
|------|---------------------|------------------------|
| `env_config` | Variáveis de ambiente para o runtime do agente | Crítica — separa dev/staging/prod |
| `path_config` | Declarações de caminhos do sistema de arquivos | Alta — deployments multiplataforma |
| `permission` | Regras de controle de acesso read/write/execute | Crítica — previne escalada de privilégios |
| `feature_flag` | Toggles de feature em runtime com rollout gradual | Alta — releases incrementais seguras |
| `runtime_rule` | Timeouts, contagens de retry, circuit breakers | Crítica — previne agentes em loop infinito |
| `secret_config` | Gerenciamento de chaves de API com rotação | Crítica — baseline de segurança |
| `rate_limit_config` | Caps de RPM, TPM, requisições concorrentes por provider | Crítica — previne tempestades de 429 |
| `cost_budget` | Limites de gasto por provider/modo/sessão | Alta — previne cobranças excessivas |
| `usage_quota` | Limites de uso justo por usuário ou tenant | Alta — segurança multi-tenant |
| `effort_profile` | Tier de modelo + orçamento de raciocínio por classe de tarefa | Alta — otimização qualidade vs. custo |
| `thinking_config` | Configurações de orçamento de tokens para raciocínio estendido | Alta — controla profundidade de chain-of-thought |
| `sandbox_config` | Ambiente de execução de código isolado | Crítica — segurança na execução de código |
| `sandbox_spec` | Especificações de sandbox para pilots empresariais | Média — gate de procurement |
| `rbac_policy` | Controle de acesso baseado em roles para isolamento multi-tenant | Crítica — deployments empresariais |
| `sso_config` | Integração com identity provider SAML/OIDC | Alta — autenticação empresarial |
| `oauth_app_config` | Escopos OAuth2/PKCE e config de redirect | Alta — integrações de API |
| `data_residency` | Config de localização regional de dados GDPR | Alta — conformidade |
| `experiment_config` | Configuração de testes A/B e variantes de prompt | Média — melhoria contínua |
| `quantization_config` | Configurações de quantização para modelos locais | Média — otimização de deployment local |
| `terminal_backend` | Abstração de ambiente de execução (local/Docker/cloud) | Alta — flexibilidade de deployment |
| `hibernation_policy` | Política de desligamento e wake de serverless ocioso | Alta — controle de custo |
| `batch_config` | Configuração de processamento em lote assíncrono | Alta — otimização de throughput |
| `transport_config` | Camada de rede para sessões em tempo real | Média — agentes de voz/realtime |
| `realtime_session` | Configuração de sessão bidirecional ao vivo | Média — agentes de voz/streaming |
| `vad_config` | Configurações de detecção de atividade de voz | Baixa — específico de voz |
| `prosody_config` | Parâmetros de personalidade e emoção de voz | Baixa — específico de voz |
| `playground_config` | Sandbox de avaliação interativa | Média — ferramentas de desenvolvedor |
| `marketplace_app_manifest` | Metadados de listagem em app stores | Baixa — distribuição |
| `kubernetes_ai_requirement` | Topologia de GPU CNCF KAR e conformidade | Média — deployments K8s |
| `white_label_config` | Configuração de branding white-label | Baixa — cenários de revendedor |

---

## Padrões de Engenharia Chave — Universais, Funcionam com Qualquer IA

### Padrão 1: A Hierarquia de Configuração

Todo deployment sério de IA tem pelo menos três níveis de configuração: padrões, overrides de ambiente e overrides de runtime. O erro que a maioria das equipes comete é implementar isso como lógica de código ad-hoc. A abordagem correta é modelá-la explicitamente:

```
Nível 1: padrões do arquétipo  (N00_genesis/P09_config/)
Nível 2: overlay de ambiente    (P09/ específico do núcleo)
Nível 3: override de runtime   (nível de sessão, do orquestrador)
```

Em qualquer framework: estabeleça padrões em um arquivo de config base, faça override por ambiente (dev/staging/prod), permita overrides por sessão para parâmetros dinâmicos. Essa hierarquia de três níveis previne o modo de falha "funciona em dev, quebra em prod" que afeta a maioria dos deployments de IA de primeira geração.

**Experimente agora (funciona com qualquer IA):**
Antes do próximo deployment de LLM, escreva três arquivos de configuração:
1. `config_base.yaml` — provider, modelo, temperatura padrão, timeout
2. `config_dev.yaml` — logging de debug, rate limits menores, secrets de mock
3. `config_prod.yaml` — secrets reais via variáveis de ambiente, rate limits rígidos, alertas

Carregue o arquivo apropriado na inicialização. Nunca hardcode nenhum dos dois conjuntos.

### Padrão 2: Profilaxia de Rate Limit

Rate limits não são uma restrição do provider para contornar — são uma rede de segurança em produção que você deve configurar defensivamente do seu lado. O padrão é: documente o limite do provider, defina seu limite seguro em 80% disso, configure backoff exponencial começando em 1 segundo, e defina uma contagem máxima de requisições concorrentes.

```yaml
# Padrão universal de rate limit config
provider: anthropic
model: claude-sonnet-4-6
rpm: 50
tpm: 200000
concurrent_requests: 20       # 20 dos 32 do provider = margem de segurança
backoff_strategy: exponential
backoff_base_ms: 1000
safe_limit_pct: 80            # nunca se aproxime do teto
```

A regra `safe_limit_pct: 80` vale ser internalizada: a 80% de utilização, a probabilidade de atingir um erro 429 cai abaixo de 2%. A 95% de utilização, sobe para mais de 40% sob carga.

### Padrão 3: Perfis de Esforço — Roteamento de Qualidade vs. Custo

Nem todas as tarefas merecem o mesmo tier de modelo ou profundidade de raciocínio. Uma tarefa de classificação de documentos não precisa do mesmo esforço que uma revisão complexa de arquitetura de código. O padrão `effort_profile` formaliza isso:

```yaml
# Baixo esforço: tarefas de rotina
effort: low
model_tier: haiku
thinking_budget_tokens: 0
max_tokens: 512

# Médio esforço: builds padrão
effort: medium
model_tier: sonnet
thinking_budget_tokens: 1024
max_tokens: 2048

# Alto esforço: decisões de arquitetura, código complexo
effort: high
model_tier: opus
thinking_budget_tokens: 10000
max_tokens: 8192
```

O impacto de custo é dramático: um grid que ingenuamente usa Opus para todos os 100 artefatos custa 10-15x mais do que um que usa Haiku para tarefas de rotina e Opus apenas para os 5 que genuinamente precisam.

### Padrão 4: Gerenciamento de Secrets — A Única Abordagem Correta

Existe exatamente uma abordagem correta para secrets em sistemas de IA: **secrets nunca aparecem em código, prompts ou arquivos de artefatos.** Eles vivem em variáveis de ambiente, injetadas em runtime por um orquestrador que as lê de um vault.

```yaml
# padrão secret_config
id: secret_anthropic_producao
kind: secret_config
provider: anthropic
key_name: ANTHROPIC_API_KEY
source: env              # lê de variável de ambiente
rotation_policy: 90d     # rotaciona a cada 90 dias
never_log: true          # nunca aparece em logs de trace
never_commit: true       # bloqueado por hook pre-commit
```

O artefato `secret_config` documenta que um secret existe e de onde vem — sem conter o secret em si. O valor real vive no vault do seu CI/CD, arquivo `.env` (no .gitignore) ou gerenciador de secrets.

### Padrão 5: Abstração de Terminal Backend

Sistemas de IA em produção rodam em múltiplos ambientes: desenvolvimento local, containers Docker, VMs na nuvem, plataformas serverless. Hardcodar suposições de execução cria quebras específicas de ambiente. O padrão `terminal_backend` abstrai isso:

```yaml
# terminal_backend: abstraia o "onde"
backend: auto            # resolve: local > docker > modal > daytona
fallback_chain: [local, docker, modal]
container_image: cexai/nucleus:latest
resource_requirements:
  gpu: optional
  ram_gb: 8
  cpu_cores: 2
```

---

## Mergulho Arquitetural

### O Grafo de Dependências do P09

Artefatos P09 raramente existem isoladamente. Eles formam uma cadeia de dependências:

```
secret_config
    |
    v
env_config -----> rate_limit_config
    |                    |
    v                    v
permission          cost_budget -----> usage_quota
    |
    v
rbac_policy -----> sso_config / oauth_app_config
    |
    v
sandbox_config -----> terminal_backend -----> hibernation_policy
```

A hierarquia importa para a ordem de deployment. O secret config deve estar disponível antes que o env config possa referenciá-lo. Os rate limits devem ser estabelecidos antes que qualquer chamada de agente seja executada.

### A Fronteira Entre P09 e Outros Pilares

P09 é frequentemente confundido com pilares vizinhos. As fronteiras canônicas:

| Situação | Pilar Correto | Por quê |
|-----------|--------------|---------|
| Identidade e persona do agente | P02 | Quem o agente é (imutável) |
| System prompt do agente | P03 | O que o agente diz |
| Restrição de segurança em outputs | P11 | Guardrail, não config |
| Gate de qualidade em artefatos | P11 | Feedback, não config |
| Permissões de acesso a ferramentas | P09 (permission) | Controle de acesso em runtime |
| Limites de teste de avaliação | P07 | Infraestrutura de avaliação |
| Quais ferramentas existem | P04 | Definições de ferramentas |

A distinção chave: P09 governa **condições operacionais**. Tudo mais governa conteúdo, identidade ou qualidade.

---

## Exemplos Reais do N00_genesis

### rate_limit_config na prática

Arquivo: `N00_genesis/P09_config/kind_rate_limit_config/kind_manifest_n00.md`

O padrão canônico para documentar rate limits do provider. Este config exato foi derivado empiricamente: 32 requisições Sonnet concorrentes era o teto observado, 87,5% de taxa de sucesso, limite seguro é ~20. O config codifica inteligência operacional que levou horas de execuções de grid para descobrir.

### effort_profile na prática

Arquivo: `N00_genesis/P09_config/kind_effort_profile`

Perfis de esforço expressam o trade-off qualidade-custo como uma preocupação de configuração de primeira classe. Em vez de embutir lógica de seleção de modelo dentro do código do agente, o orquestrador seleciona um perfil de esforço com base na classificação da tarefa, e toda a seleção de modelo downstream flui desse perfil.

### hibernation_policy — o padrão de controle de custo

Arquivo: `N00_genesis/P09_config/tpl_hibernation_policy.md`

Para deployments serverless, computação ociosa é desperdício puro. A `hibernation_policy` declara:
- `idle_timeout`: quanto tempo sem requisições antes de hibernar
- `wake_trigger`: qual evento reinicia o serviço
- `warm_pool_size`: quantas instâncias pré-aquecidas manter

---

## Anti-Padrões — Erros Universais

**Anti-padrão 1: Config embutida em prompts**
Hardcodar `"Você deve responder em menos de 200 palavras"` dentro de um system prompt é uma preocupação de config embutida em um prompt. A abordagem correta: declare um `runtime_rule` com `max_output_tokens: 200` e referencie-o da config de execução do agente.

**Anti-padrão 2: Rate limits como try/catch**
O padrão prevalente em código LLM ingênuo: envolva cada chamada de API em try/except, capture o 429, durma e tente novamente. Isso é tratamento reativo de rate limit. O padrão P09 é proativo: configure seus próprios limites abaixo do teto do provider para nunca atingir 429.

**Anti-padrão 3: Um arquivo de config para todos os ambientes**
Um único `config.yaml` no git compartilhado entre desenvolvimento e produção é um incidente de segurança esperando para acontecer. Secrets aparecem no histórico do git. Overrides de dev desabilitam verificações de segurança de produção.

**Anti-padrão 4: Limites de quota não documentados**
"Atingimos um limite de quota e nossa execução noturna falhou" é uma história contada em post-mortems em toda a indústria. Documente cada quota — limites de provider, quotas de uso internas, limites por usuário — como artefatos `rate_limit_config` e `usage_quota` antes da primeira execução em produção.

**Anti-padrão 5: Orçamento de raciocínio fixo para todas as tarefas**
Definir `thinking_budget_tokens: 10000` para cada tarefa é o equivalente de exigir que todo funcionário escreva um relatório de 50 páginas antes de responder qualquer pergunta. Mapeie a complexidade da tarefa para perfis de esforço.

**Anti-padrão 6: Política de hibernação ausente no serverless**
Fazer deploy de um endpoint de IA serverless sem uma política de hibernação é pagar por computação ociosa. Uma `hibernation_policy` com `idle_timeout: 5m` elimina isso.

---

## Conexões Entre Pilares

| P09 consome | De pilar | O que usa |
|------------|---------|----------|
| Identidade do agente | P02 | Qual agente possui qual config |
| Definições de ferramentas | P04 | Quais ferramentas precisam de quais permissões |
| Limiares de qualidade | P11 | Qual effort_profile mira qual barra de qualidade |
| Decisões de arquitetura | P08 | Quais ambientes de runtime são aprovados |

| P09 alimenta | Para pilar | O que fornece |
|-------------|-----------|--------------|
| Restrições operacionais | P12 | Orquestrador lê rate limits antes de despachar |
| Ambiente de execução | P12 | Terminal backend determina onde os workflows rodam |
| Limites de permissão | P11 | Guardrails leem configs de permissão para escopo |
| Dados de custo | P07 | Relatórios de uso puxam de configs de cost_budget |

**A dependência entre pilares mais crítica:** P12 Orchestration lê P09 Config antes de cada despacho. O orquestrador não pode despachar com segurança 6 núcleos em paralelo sem primeiro ler `rate_limit_config` para entender os tetos do provider.

---

## Experimente Agora — Exercícios P09 para Qualquer Sistema de IA

**Exercício 1: Auditoria de Rate Limit (30 minutos)**
Para cada API de LLM que você usa em produção, escreva um documento `rate_limit_config`. Inclua: RPM, TPM, limite de requisições concorrentes, estratégia de backoff. Verifique: algum desses é atualmente implícito (você os descobre ao atingir erros)?

**Exercício 2: Varredura de Secret Config (1 hora)**
Pesquise no seu codebase por qualquer string correspondendo a `sk-`, `AIzaSy`, `AKIA` (prefixos comuns de chaves de API). Encontre cada secret hardcoded ou commitado. Para cada um: mova para variável de ambiente, escreva um artefato `secret_config` documentando seu nome, fonte e política de rotação.

**Exercício 3: Design de Perfil de Esforço (45 minutos)**
Liste os 5 tipos de tarefa principais que seu sistema de IA trata. Para cada um: qual é o tier de modelo apropriado? Raciocínio estendido ou não? Máximo de tokens de saída? Escreva um `effort_profile` para cada um. Estime a redução de custo ao rotear tarefas baratas para modelos menores.

**Exercício 4: Separação de Config de Ambiente (2 horas)**
Se você tem um único arquivo de config cobrindo todos os ambientes, divida-o em base + overlays por ambiente. Mova todos os secrets para variáveis de ambiente. Teste que `config_dev.yaml` não pode acidentalmente se conectar a recursos de produção.

---

## Artefatos Relacionados

| Artefato | Relação | Score |
|----------|---------|-------|
| [[kc_pillar_brief_p09_config_en]] | irmão (EN) | 1.00 |
| [[kc_pillar_brief_p08_architecture_pt]] | upstream | 0.48 |
| [[kc_pillar_brief_p10_memory_pt]] | downstream | 0.45 |
| [[kc_pillar_brief_p11_feedback_pt]] | relacionado | 0.43 |
| [[kc_pillar_brief_p12_orchestration_pt]] | downstream | 0.42 |
| [[n00_p09_kind_index]] | upstream | 0.68 |
| [[n00_rate_limit_config_manifest]] | upstream | 0.55 |
| [[mentor_context]] | upstream | 0.40 |
