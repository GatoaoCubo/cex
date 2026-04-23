---
id: kc_pillar_brief_p10_memory_pt
kind: knowledge_card
pillar: P10
title: "P10 Memory — O Hipocampo da Sua IA"
version: 1.0.0
created: "2026-04-22"
author: n04_knowledge
quality: 6.6
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p10, memory, context, rag, session-state, llm-engineering]
tldr: "P10 Memory cobre tudo que um LLM precisa lembrar entre sessões: entity memories, índices de conhecimento, modelos de usuário, registros de aprendizado e compressão de contexto."
source_concepts: [kc_lens_index, mentor_context]
related:
  - kc_pillar_brief_p10_memory_en
  - kc_pillar_brief_p01_knowledge_pt
  - kc_pillar_brief_p09_config_pt
  - kc_pillar_brief_p11_feedback_pt
  - n00_p10_kind_index
density_score: 1.0
---

# P10 Memory — O Hipocampo da Sua IA: Como Ela Lembra, Esquece e Aprende ao Longo do Tempo

---

## O Princípio Universal: A Janela de Contexto Não É Memória

Todo praticante de IA que colocou um sistema em produção confronta o mesmo fato brutal: **a janela de contexto não é memória. É um quadro branco que é apagado no final de cada sessão.** O modelo não lembra do seu usuário da semana passada. Não lembra do bug que corrigiu ontem. Não lembra qual abordagem já tentou e qual falhou. Cada janela de contexto é uma ilha.

Isso não é um modo de falha para contornar — é uma restrição fundamental para engenheirar. A metáfora do hipocampo é precisa: nos humanos, o hipocampo não armazena memórias de longo prazo em si mesmo. Ele coordena a consolidação — pegando as experiências do dia e codificando as importantes no armazenamento de longo prazo enquanto descarta o ruído. P10 Memory é a disciplina de engenharia que constrói esse sistema de consolidação para IA.

Sem P10, todo sistema LLM é amnésico por padrão. Pode ser brilhante dentro de uma janela de contexto, mas esse brilho evapora. Com P10 devidamente engenheirado, sua IA acumula inteligência ao longo do tempo: lembra o que os usuários preferem, aprende com falhas passadas, evita repetir erros, constrói representações mais ricas de entidades recorrentes.

Isso é universal. O gerenciamento de memória aparece no LangChain como `ConversationBufferMemory`, `ConversationSummaryMemory`. No LlamaIndex como `ChatMemoryBuffer`. No sistema da OpenAI como instruções persistentes. No da Anthropic como artefatos persistentes em Projetos. Os nomes diferem; o problema subjacente é idêntico: **como você dá a um modelo sem estado a ilusão — e eventualmente a substância — de inteligência persistente?**

---

## O Que Este Pilar Faz

P10 Memory aborda quatro desafios distintos de engenharia de memória que todo sistema de IA em produção enfrenta:

**Desafio 1: Continuidade entre sessões** — Como o modelo lembra o que discutiu com o usuário X três sessões atrás? Resposta: `entity_memory`, `user_model`, `session_backend`.

**Desafio 2: Aprendizado operacional** — Como o modelo acumula lições de suas próprias execuções em vez de repetir os mesmos erros? Resposta: `learning_record`, `agent_grounding_record`, `procedural_memory`.

**Desafio 3: Gerenciamento de orçamento de contexto** — A janela de contexto tem um orçamento finito de tokens. Como você comprime meses de histórico em algumas centenas de tokens sem perder o que importa? Resposta: `memory_summary`, `compression_config`, `consolidation_policy`, `memory_type`.

**Desafio 4: Infraestrutura de recuperação** — Memória é inútil se não pode ser encontrada. Como você indexa o conhecimento acumulado para que os fatos certos carreguem no momento certo? Resposta: `knowledge_index`, `prompt_cache`, `runtime_state`.

No pipeline 8F, artefatos P10 são lidos no F3 INJECT — eles são o mecanismo primário de injeção de contexto para inteligência entre sessões. Construí-los acontece no F3b PERSIST — o sub-passo onde novo conhecimento é commitado em armazenamento durável após a geração.

---

## Os 19 Tipos em P10 — Referência Universal de Capacidades

| Tipo | Capacidade Universal | Caso de Uso Primário |
|------|---------------------|---------------------|
| `entity_memory` | Fatos estruturados persistentes sobre uma entidade nomeada | Perfis de clientes, fatos de produtos, inteligência competitiva |
| `user_model` | Representação dialética cross-sessão do usuário | Personalização, rastreamento de preferências, adaptação |
| `knowledge_index` | Configuração de índice de busca BM25/FAISS | Recuperação rápida sobre grandes stores de memória |
| `learning_record` | O que funcionou/falhou — inteligência operacional | Auto-melhoria do agente, evitação de falhas |
| `session_state` | Snapshot efêmero da sessão atual | Passagem de contexto de curto prazo entre passos |
| `memory_summary` | Representação comprimida de histórico longo | Caber meses de histórico em algumas centenas de tokens |
| `runtime_state` | Estado mental variável acumulado nesta sessão | Decisões de roteamento, observações acumuladas |
| `agent_grounding_record` | Proveniência por inferência: ferramentas chamadas, chunks usados | Auditabilidade, reprodutibilidade, debugging |
| `prompt_cache` | Configuração de TTL e evicção para pares prompt/completion em cache | Redução de custo via cache hits |
| `compression_config` | Estratégia de compressão de saída de ferramentas | Prevenção de overflow de contexto por retornos grandes de ferramentas |
| `memory_architecture` | Documento de design completo do sistema de memória | Planejamento de arquitetura de sistema |
| `memory_type` | Classificação de memória por fonte, confiança, decay | Taxonomia de memória para roteamento de recuperação |
| `procedural_memory` | Armazenamento/recuperação de habilidades e procedimentos | Conhecimento de como fazer que transfere entre sessões |
| `consolidation_policy` | Política de gerenciamento do ciclo de vida da memória | O que é promovido para longo prazo, o que é podado |
| `session_backend` | Backend de persistência de estado de sessão por usuário | Seleção de banco de dados para armazenamento de sessão |
| `model_registry` | Versionamento de modelo e rastreamento de artefatos | Qual versão do modelo produziu qual saída |
| `c2pa_manifest` | Credencial de conteúdo C2PA para mídia gerada por IA | Proveniência de conteúdo para conformidade regulatória |
| `vc_credential` | Credencial Verificável W3C para identidade de agente IA | Identidade e atestação de agente |
| `workflow_run_crate` | Proveniência de execução de workflow RO-Crate | Reprodutibilidade científica |

---

## Padrões de Engenharia Chave — Universais, Funcionam com Qualquer IA

### Padrão 1: A Taxonomia de Memória (Quatro Tipos)

Nem toda memória é igual. Antes de engenheirar qualquer sistema de memória, categorize o que você precisa armazenar:

| Tipo | Descrição | Taxa de Decay | Formato de Armazenamento |
|------|-----------|--------------|--------------------------|
| **Correção** | "Na última vez que fiz X, produziu um resultado errado" | Baixa — semi-permanente | learning_record |
| **Preferência** | "Este usuário prefere bullet points a parágrafos" | Média — 6-12 meses | user_model |
| **Convenção** | "Este codebase usa tabs, não espaços" | Nenhuma — até ser alterada | entity_memory |
| **Contexto** | "O projeto atual é um SPA React" | Alta — nível de sessão | session_state |

A taxa de decay importa para o design de recuperação: convenções permanentes devem ser injetadas em cada chamada; contexto de sessão deve expirar quando a sessão termina; preferências devem esmaecer se não reforçadas.

**Experimente agora (qualquer IA):**
Antes da sua próxima conversa estendida de projeto com ChatGPT ou Claude, escreva um documento de contexto de memória de 200 palavras com estas quatro seções: (1) Fatos sobre o projeto que nunca mudam, (2) Suas preferências de formato de resposta, (3) Decisões tomadas até agora, (4) Contexto da sessão atual. Cole no início. Observe a diferença de qualidade.

### Padrão 2: Entity Memory — O Padrão de Conhecimento Relacional

Uma `entity_memory` armazena fatos estruturados sobre uma entidade nomeada — uma pessoa, empresa, produto ou conceito — em um formato projetado para recuperação e atualização:

```yaml
# Padrão universal de entity memory
entity_name: "Acme Corp"
entity_type: company
attributes:
  founded: 2019
  sector: "B2B SaaS"
  hq: "Austin, TX"
  primary_contact: "Sarah Chen, CTO"
  pain_point: "relatórios de conformidade manuais"
  budget_range: "$50K-$200K/ano"
relationships:
  - entity: "competitor_xyz"
    type: "direct_competitor"
  - entity: "partner_abc"
    type: "integration_partner"
confidence: 0.92
last_updated: "2026-04-22"
```

O insight chave: isso não é um documento. É um **registro estruturado** onde cada campo é atualizável independentemente. Quando você descobre que a Acme Corp mudou sua sede, você atualiza um campo.

### Padrão 3: Compressão de Memória — O Padrão de Consolidação do Hipocampo

Um usuário que teve 500 conversas com sua IA gerou ~2 milhões de tokens de histórico de sessão. Você não pode injetar tudo isso no contexto. Mas também não pode descartar. A solução é compressão com perda com fidelidade controlada:

**Nível 1: Histórico recente** (últimas 10 conversas) — verbatim, injetado por completo
**Nível 2: Resumos de sessão** (sessões desta semana) — 100 tokens por resumo de sessão
**Nível 3: Resumos de longo prazo** (mais de 30 dias) — 20 tokens de insights extraídos apenas
**Nível 4: Entity memories** (fatos permanentes extraídos do histórico) — registros estruturados, sem decay de tokens

```yaml
# consolidation_policy
session_to_summary_threshold: 10        # após 10 turnos, escreve resumo de sessão
summary_to_longterm_threshold: 30d      # após 30 dias, comprime para longo prazo
entity_extraction_trigger: "qualquer entidade nomeada mencionada 3+ vezes"
preservation_priority: [corrections, decisions, preferences, context]
```

### Padrão 4: Learning Records — A Memória de Auto-Melhoria

Um `learning_record` é o mecanismo pelo qual um sistema de IA acumula inteligência operacional de suas próprias execuções. Toda vez que um quality gate falha, toda vez que uma abordagem de build tem sucesso, toda vez que uma chamada de ferramenta produz um resultado inesperado — esse evento deve gerar um learning record.

```yaml
# padrão learning_record
session_id: "session_20260422_n05"
nucleus: n05
outcome: failure
pattern: "Índice BM25 requer rebuild após adicionar novos tipos de artefatos"
evidence: "cex_retriever retornou 0 resultados para kind compression_config até rebuild"
applies_to: [knowledge_index, cex_retriever.py]
decay_rate: 0.0   # permanente — este é um comportamento do sistema
```

### Padrão 5: User Model — O Padrão Honcho

O padrão de memória mais poderoso para sistemas de IA voltados ao usuário é a representação cross-sessão do usuário, às vezes chamado de padrão Honcho (do projeto open-source da Plastic Labs). A ideia: após cada sessão, a IA extrai uma representação estruturada do que aprendeu sobre este usuário específico — e injeta essa representação no início de cada sessão futura.

```yaml
# padrão user_model
peer_id: "user_gato3"
communication_style: "conciso, técnico, autônomo"
domain_expertise: ["prompt engineering", "Python", "sistemas distribuídos"]
preferences:
  response_format: "tabelas em vez de prosa, bullet points para listas"
  language: "pt-br primário, EN para termos técnicos"
  decision_style: "quer opções, decide rápido, sem over-explanation"
corrections_applied: ["nunca pede confirmação para builds padrão", "pular preâmbulo"]
session_count: 47
last_interaction: "2026-04-22"
```

### Padrão 6: Prompt Cache — O Padrão de Engenharia de Custo

O cache de prompts é o mecanismo P10 com o maior ROI imediato. Toda vez que sua IA chama um LLM com o mesmo system prompt + definições de ferramentas, você está pagando pelos mesmos tokens repetidamente. O cache de prompts reduz isso a quase zero para a parte repetida.

```yaml
# configuração de prompt_cache
ttl_seconds: 300              # TTL de 5 minutos corresponde à janela de cache da Anthropic
eviction_strategy: lru
max_entries: 100
cache_key_method: content_hash
invalidation_trigger: "system_prompt_change"
storage_backend: redis
```

Em escala (um grid de 100 agentes), as economias do cache de prompts são substanciais. Um system prompt de 10K tokens atingido 100 vezes por sessão custa $0,30 sem cache. Com TTL de 5 minutos e 80% de hit rate, cai para $0,06.

---

## Mergulho Arquitetural

### A Stack de Memória — Quatro Camadas

Sistemas de memória de produção têm quatro camadas arquiteturais distintas:

```
Camada 4: CAMADA DE RECUPERAÇÃO
         knowledge_index (BM25/FAISS)
         runtime_state (decisões de roteamento)
              |
              v
Camada 3: CAMADA DE COMPRESSÃO
         memory_summary (histórico comprimido)
         compression_config (como comprimir)
         consolidation_policy (quando promover/podar)
              |
              v
Camada 2: CAMADA DE ARMAZENAMENTO
         entity_memory (fatos estruturados)
         user_model (representação do usuário)
         learning_record (inteligência operacional)
         procedural_memory (armazenamento de habilidades)
         session_backend (banco de dados)
              |
              v
Camada 1: CAMADA DE SESSÃO
         session_state (efêmero, sessão atual)
         prompt_cache (cache ativo)
         agent_grounding_record (proveniência da inferência atual)
```

O fluxo de dados: a camada de sessão captura eventos em tempo real. A camada de compressão os consolida periodicamente. A camada de armazenamento persiste os artefatos importantes. A camada de recuperação os torna encontráveis.

### Violações de Fronteira de Memória — Os Erros Mais Comuns

| Confusão | Por Que Está Errado | Separação Correta |
|----------|--------------------|--------------------|
| Tratar `session_state` como armazenamento permanente | Sessões são efêmeras — reinício do servidor as destrói | Use `entity_memory` para fatos que você precisa na próxima semana |
| Usar `knowledge_card` (P01) para fatos específicos de usuário | Knowledge cards são conhecimento de domínio, não estado de usuário | `user_model` para específico de usuário, `entity_memory` para fatos de entidade |
| Armazenar `runtime_state` sem política de decay | Runtime state de ontem está obsoleto | Aplique decay: TTL de 24-48h em observações de runtime |
| Pular `agent_grounding_record` | Sem auditabilidade quando a IA produz uma resposta errada | Registre proveniência em cada inferência |
| Comprimir muito agressivamente | Supercompressão perde contexto crítico | Teste fidelidade de compressão contra um conjunto holdout |

---

## Exemplos Reais do N00_genesis

### entity_memory na prática

Arquivo: `N00_genesis/P10_memory/ex_entity_memory_partner_profile.md`

Um perfil de parceiro como entity memory acumula: nome da empresa, setor, contato principal, pontos de dor, faixa de orçamento, status de integração e data da última interação. Cada sessão adiciona ou atualiza campos. A IA nunca pergunta "pode me lembrar de qual empresa você é?" — ela já sabe, porque a entity memory foi injetada no início da sessão.

### learning_record na prática

Arquivo: `N00_genesis/P10_memory/kind_learning_record/kind_manifest_n00.md`

O sistema CEXAI gera learning records após cada falha de quality gate e descoberta de padrão bem-sucedida. Exemplo de padrão capturado: "Índice BM25 perde novos artefatos P10 se rebuild não for acionado." Isso se torna um lembrete permanente injetado antes de cada tarefa de build relacionada a recuperação.

### user_model na prática

Arquivo: `N00_genesis/P10_memory/tpl_user_model.md`

O template de user_model captura: peer_id, estilo de comunicação, expertise de domínio, preferências de formato, histórico de correções e contagem de sessões. No CEXAI, N07 mantém um user_model para o operador que acumula preferências ao longo do tempo.

---

## Anti-Padrões — Erros Universais de Engenharia de Memória

**Anti-padrão 1: Stuffing de contexto**
Injetar todo o histórico de sessão verbatim em cada janela de contexto. A 200 sessões × 4K tokens cada, isso são 800K tokens — impossível em qualquer modelo com limite de contexto de 200K. Use compressão `memory_summary`.

**Anti-padrão 2: Um tipo de memória para tudo**
Misturar preferências de usuário, fatos de entidades, aprendizados operacionais e estado de sessão em um blob não tipado. Use a taxonomia de quatro tipos: correção, preferência, convenção, contexto.

**Anti-padrão 3: Sem política de decay**
Armazenar memórias sem expiração. Uma preferência de usuário de 18 meses atrás pode não ser mais válida. Todo artefato de memória deve declarar um decay_rate ou TTL.

**Anti-padrão 4: Recuperação apenas por recência**
Carregar os N memórias mais recentes independentemente da relevância para a query atual. Uma sessão sobre componentes React não deve injetar memórias sobre configuração Kubernetes. Use busca semântica (FAISS) ou BM25 para recuperação ranqueada por relevância.

**Anti-padrão 5: Sem proveniência em outputs de IA**
Implantar IA em contextos regulados sem `agent_grounding_record`. Quando a IA produz uma saída errada, você precisa saber: quais chunks RAG ela usou? Qual era a versão do modelo? Qual ferramenta ela chamou?

**Anti-padrão 6: Esquecer de consolidar**
Acumular estados de sessão sem uma política de consolidação. Após 100 sessões, você tem 100 blobs de estado efêmero que deveriam ter sido destilados em 10 entity memories e 5 learning records.

---

## Conexões Entre Pilares

Memória está no centro do sistema de 12 pilares porque inteligência requer tanto conhecimento (P01) quanto memória (P10). A distinção crítica:

| P01 Knowledge | P10 Memory |
|--------------|-----------|
| Fatos de domínio — verdades universais | Fatos de sessão — específicos deste usuário/sistema |
| Nunca expira (até o mundo mudar) | Decai ao longo do tempo |
| Compartilhado entre todos os usuários | Por usuário ou por agente |
| Recuperação RAG | Injeção personalizada |

| P10 alimenta | Para pilar | O que fornece |
|-------------|-----------|--------------|
| Preferências de usuário | P02 | Agente adapta persona ao usuário conhecido |
| Aprendizados operacionais | P11 | Loop de feedback consome learning records |
| Registros de proveniência | P07 | Avaliação usa grounding records como ground truth |
| Estado de sessão | P12 | Orquestrador lê runtime_state ao planejar próximos passos |

---

## Experimente Agora — Exercícios P10 para Qualquer Sistema de IA

**Exercício 1: Entity Memory para Seus 5 Principais Clientes (45 minutos)**
Para seus cinco clientes/parceiros mais importantes, escreva arquivos de entity memory estruturados. Inclua: nome da empresa, setor, contato principal, pontos de dor, status, última interação. Antes da sua próxima interação de IA voltada ao cliente, injete a entity memory relevante no system prompt.

**Exercício 2: Revisão de Aprendizado Operacional (30 minutos)**
Pense nas últimas 3 vezes que seu sistema de IA produziu um resultado errado ou subótimo. Para cada um: escreva um `learning_record` documentando o padrão e evidência. Adicione como contexto persistente ao seu system prompt.

**Exercício 3: Auditoria de Tipo de Memória (1 hora)**
Levante tudo que seu sistema de IA atualmente "sabe" sobre usuários e contexto. Categorize cada parte do conhecimento como: correção, preferência, convenção ou contexto. Atribua taxas de decay. Remova qualquer coisa obsoleta.

**Exercício 4: Design de Compressão de Sessão (2 horas)**
Design uma política de consolidação para um sistema com mais de 100 sessões por usuário. Defina: o que aciona um resumo de sessão, qual formato de resumo captura máxima informação por token, o que aciona a promoção para entity memory de longo prazo.

---

## Artefatos Relacionados

| Artefato | Relação | Score |
|----------|---------|-------|
| [[kc_pillar_brief_p10_memory_en]] | irmão (EN) | 1.00 |
| [[kc_pillar_brief_p01_knowledge_pt]] | upstream | 0.52 |
| [[kc_pillar_brief_p09_config_pt]] | upstream | 0.45 |
| [[kc_pillar_brief_p11_feedback_pt]] | downstream | 0.50 |
| [[kc_pillar_brief_p12_orchestration_pt]] | downstream | 0.44 |
| [[n00_p10_kind_index]] | upstream | 0.70 |
| [[n00_entity_memory_manifest]] | upstream | 0.55 |
| [[n00_learning_record_manifest]] | upstream | 0.52 |
| [[mentor_context]] | upstream | 0.42 |
