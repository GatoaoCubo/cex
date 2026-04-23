---
id: kc_pillar_brief_p01_knowledge_pt
kind: knowledge_card
pillar: P01
title: "P01 Knowledge — A Camada de Fundação"
version: 1.1.0
created: "2026-04-22"
updated: "2026-04-22"
author: n04_knowledge
quality: 6.0
language: pt-br
domain: pillar_architecture
tier: mechanic
tags: [knowledge-card, pillar-brief, p01, knowledge, rag, embeddings, chunking, llm-engineering]
tldr: "P01 Knowledge: 30 kinds cobrindo RAG, embeddings, chunking, knowledge graphs — cada LLM sem P01 alucina; com P01 opera sobre corpus curado, versionado e pesquisável."
when_to_use: "Ao projetar pipeline RAG, estruturar base de conhecimento, configurar embedding/retrieval ou ensinar engenharia de conhecimento LLM em PT-BR."
keywords: [rag-pipeline, knowledge-card, chunk-strategy, embedding-config, knowledge-graph]
long_tails:
  - Como construir pipeline RAG com chunk strategy e retriever config
  - Qual a diferenca entre knowledge_card context_doc e glossary_entry no CEXAI
axioms:
  - SEMPRE versionar knowledge_cards (campo version incrementado em qualquer mudanca de conteudo)
  - NUNCA injetar conhecimento sem fonte verificavel (campo data_source obrigatorio)
  - SE busca plana falha em perguntas relacionais ENTAO usar knowledge_graph + graph_rag_config
  - NUNCA misturar instrucoes em knowledge_cards (instrucoes pertencem a P03, fatos a P01)
source_concepts: [kc_lens_index, mentor_context]
density_score: 0.87
data_source: "https://arxiv.org/abs/2005.11401"
linked_artifacts:
  primary: kc_pillar_brief_p01_knowledge_en
  related:
    - kc_pillar_brief_p02_model_pt
    - cm_driver_01_structured_thinking
    - kc_lens_factory
    - kc_lens_index
    - p01_kc_8f_pipeline
    - p01_kc_rag_fundamentals
related:
  - kc_pillar_brief_p01_knowledge_en
  - kc_pillar_brief_p02_model_pt
  - kc_pillar_brief_p03_prompt_pt
  - cm_driver_01_structured_thinking
  - kc_lens_factory
  - kc_lens_index
  - p01_kc_8f_pipeline
  - p01_kc_rag_fundamentals
  - p01_kc_knowledge_graph
  - mentor_context
---

# P01 Knowledge — A Camada de Fundação: Como LLMs Sabem o Que Sabem

## Quick Reference

```yaml
topic: P01_Knowledge
scope: Substrato de memoria de sistemas LLM — 30 kinds, funcao LLM INJECT
owner: n04_knowledge
criticality: high
llm_function: INJECT (F3 no pipeline 8F)
kinds_count: 30
dependency: alimenta P02, P03, P07, P10, P12
anti_pattern: confiar no conhecimento de treinamento do modelo para fatos de dominio
```

## Key Concepts

| Kind / Conceito | Tipo | Uso Principal | Limite |
|-----------------|------|---------------|--------|
| `knowledge_card` | conteudo | fato atomico pesquisavel, density >= 0.8 | 5120B |
| `context_doc` | conteudo | visao geral de dominio para hidratacao de prompts | 2048B |
| `glossary_entry` | conteudo | definicao de termo, vocabulario controlado | 512B |
| `few_shot_example` | conteudo | aprendizado in-context, par input/output | — |
| `chunk_strategy` | runtime | como dividir docs antes da indexacao | — |
| `embedding_config` | runtime | modelo vetorial, dimensoes, provedor | — |
| `retriever_config` | runtime | BM25 + denso + reranker, trade-off recall/precisao | — |
| `vector_store` | runtime | pgvector / Chroma / FAISS / Qdrant | — |
| `reranker_config` | runtime | filtra 20 candidatos -> top_k=5, +12% MRR@5 | — |
| `knowledge_graph` | estrutural | entidades + relacoes, perguntas multi-hop | — |
| `agentic_rag` | avancado | loop de recuperacao controlado por agente | — |
| `ontology` | estrutural | taxonomia formal, vocabulario de dominio | — |

## Golden Rules

- **SEMPRE versionar**: campo `version` incrementado em qualquer mudanca de conteudo; drift silencioso e o modo de falha mais comum
- **NUNCA colar documentos inteiros**: chunking injeta as secoes relevantes, nao o documento inteiro; mais tokens != respostas melhores
- **STACK RAG minima**: `chunk_strategy` + `embedding_config` + `retriever_config` = pipeline RAG operacional
- **Grafo vs vetores**: busca plana para Q&A simples; `knowledge_graph` para perguntas multi-hop ou relacionais
- **Densidade obrigatoria**: `density_score >= 0.8`; frases de preenchimento diluem sinal de recuperacao e reprovam no gate H08

## Ciclo de Vida do Conhecimento

```text
[fonte externa] -> [rag_source] -> [chunk_strategy] -> [embedding_config]
                                                              |
                                                       [vector_store]
                                                              |
[knowledge_card escrito/destilado] -> [git commit] -> [cex_compile.py]
                                                              |
                                                    [cex_retriever.py TF-IDF]
                                                              |
                                                    [F3 INJECT no prompt]
                                                              |
                                                    [geracao fundamentada]
```

---

## O Princípio Universal: Seu AI Tem Amnésia

Aqui está a coisa mais importante que você precisa entender sobre qualquer sistema de AI com que trabalha — ChatGPT, Claude, Gemini, um modelo Ollama local, qualquer um: **ele esquece tudo entre as sessões.** Não parcialmente. Completamente. Cada conversa começa do mesmo ponto zero.

Isso não é um bug. É uma propriedade arquitetural fundamental dos modelos de linguagem baseados em transformers. Os pesos do modelo codificam entendimento geral de linguagem construído durante o treinamento. Mas seus fatos específicos — seus preços de produto, suas políticas internas, suas descobertas de pesquisa, seu histórico de clientes — não existem em lugar nenhum nesse modelo a menos que você os coloque lá, toda vez.

P01 Knowledge é a disciplina de engenharia que resolve esse problema. A metáfora que fica: **um AI sem conhecimento organizado é um gênio com amnésia — brilhante, capaz de raciocínio extraordinário, mas começando do zero toda conversa.** P01 é o sistema que dá ao gênio um arquivo, um motor de busca e uma forma de encontrar os fatos certos antes de responder.

Isso não é um problema específico do CEXAI. É universal. Os mesmos padrões — knowledge cards, pipelines RAG, embedding configs, retrieval tuning — aparecem no LangChain, LlamaIndex, Haystack e em todo deployment LLM sério de produção. A taxonomia de 12 pilares do CEXAI dá a esses padrões nomes canônicos e quality gates, mas a engenharia subjacente se aplica quer você esteja usando uma assinatura de R$100/mês do ChatGPT ou um deployment enterprise de R$1M.

**A conclusão prática:** se seu AI está alucinando, a causa raiz é quase sempre um problema de P01. O modelo está chutando porque não tem o conhecimento certo na sua janela de contexto quando gera a resposta.

---

## O Que Esse Pilar Faz

P01 Knowledge é o substrato de memória de qualquer sistema baseado em LLM. Onde P03 governa o que um agente *diz*, P02 governa o que um agente *é*, P01 governa o que um agente *sabe*. Sem P01, cada chamada de LLM começa do zero — a alucinação preenche o espaço onde deveria haver conhecimento. Com P01 populado corretamente, o modelo opera sobre um corpus curado, versionado e pesquisável de fatos destilados que ele de outra forma não teria ou confundiria.

Na taxonomia de 12 pilares do CEXAI, P01 está no extremo mais upstream: ele alimenta todos os outros pilares. Templates de prompt (P03) precisam de conhecimento de domínio injetado. Agentes (P02) precisam de contexto carregado no boot. Avaliadores (P07) precisam de ground truth para comparar. Orquestradores (P12) precisam de fatos relevantes à missão para planejar ondas de forma inteligente. Tudo que faz um modelo de linguagem produzir output confiável e específico ao domínio flui do que você coloca em P01.

O pilar mapeia para uma função LLM dominante: **INJECT**. No pipeline 8F, INJECT é F3 — carregar contexto na janela de trabalho do modelo antes da geração. Todo artefato P01 é, em sua essência, uma unidade de conhecimento injetável: densa, versionada, recuperável, com fronteiras bem definidas.

Em termos agnósticos de framework, P01 responde três perguntas:

- **Que fatos temos?** — `knowledge_card`, `context_doc`, `glossary_entry`, `citation`
- **Como os recuperamos?** — `chunk_strategy`, `embedding_config`, `retriever_config`, `vector_store`, `reranker_config`, `embedder_provider`
- **Como os estruturamos relacionalmente?** — `knowledge_graph`, `ontology`, `graph_rag_config`, `agentic_rag`

A distinção entre *kinds de conteúdo* (os fatos em si) e *kinds de runtime* (infraestrutura de recuperação) é crítica para o design de sistemas. Kinds de conteúdo são escritos por humanos ou destilados por agentes a partir de fontes externas. Kinds de runtime configuram a maquinaria que torna o conteúdo pesquisável.

> **Por que isso importa para você:** Empresas que usam bases de conhecimento estruturadas com seus AIs reportam 40-60% menos respostas do tipo "não sei" ou alucinadas. A diferença entre uma resposta genérica de AI e uma resposta de especialista de domínio é quase sempre se você investiu em P01.

---

## Os 30 Kinds de P01 — Reencuadrados como Capacidades Universais

Em vez de listar nomes de kinds do CEXAI de forma isolada, aqui está cada capacidade principal explicada como um conceito universal de engenharia LLM — com um exemplo prático que você pode tentar com qualquer AI que já tem.

### Kinds de Conteúdo Core — O Próprio Conhecimento

| Kind | Capacidade Universal | Funciona com Qualquer AI? |
|------|---------------------|--------------------------|
| `knowledge_card` | Armazenamento estruturado de fatos — um fato atômico e pesquisável por unidade | Sim — ChatGPT, Claude, Gemini, modelos locais |
| `context_doc` | Injeção de contexto amplo — visão geral do domínio para hidratação de prompts | Sim — cole como contexto em qualquer chat |
| `glossary_entry` | Definições de termos — garante que o AI use seu vocabulário, não termos genéricos | Sim — inclua no system prompt |
| `citation` | Afirmações fundamentadas — cada fato vinculado a uma fonte verificável | Sim — previne alucinação na raiz |
| `few_shot_example` | Aprendizado in-context — mostrar ao AI exatamente o formato que você quer | Sim — a técnica LLM mais universal |
| `rag_source` | Ponteiros de dados ao vivo — URL + metadados de freshness para indexação externa | Sim — qualquer implementação RAG |
| `dataset_card` | Documentação de dataset — estilo HuggingFace para fine-tuning ou eval sets | Sim — padrão em todos os frameworks ML |
| `faq_entry` | Pares Q&A — respostas canônicas para deflexão de suporte | Sim — a forma mais simples de base de conhecimento |

**Tente agora — padrão de Knowledge Card com qualquer AI:**
Abra o ChatGPT ou Claude. Cole isso:

> "Vou te dar fatos sobre meu negócio. Armazene cada um como um fato separado e pesquisável com uma categoria. Aqui vai o fato 1: Nossa política de reembolso permite devoluções em até 30 dias após a compra, sem necessidade de justificativa. Categoria: Política."

Você acabou de criar um sistema de knowledge card em um único prompt. O rótulo de categoria é sua tag de recuperação. A separação de fatos é seu chunking. A especificidade de "sem necessidade de justificativa" é seu requisito de densidade. O CEXAI formaliza isso em um artefato tipado com quality gates — mas o conceito funciona em qualquer lugar.

### Kinds de Infraestrutura RAG — A Maquinaria de Recuperação

| Kind | Capacidade Universal | O Problema de Engenharia que Resolve |
|------|---------------------|--------------------------------------|
| `chunk_strategy` | Como alimentar documentos longos ao AI | Você não pode colar um livro inteiro — você cola o parágrafo certo |
| `embedding_config` | Como o AI entende significado, não apenas palavras | Busca semântica encontra "reclamação de entrega" mesmo que a palavra "entrega" não apareça |
| `embedder_provider` | Qual modelo vetorial usar | OpenAI, Cohere, Ollama (local gratuito), Voyage — cada um com trade-offs |
| `retriever_config` | Ajuste de busca — recall vs precisão | BM25 para termos exatos; vetores densos para semântica; híbrido para produção |
| `reranker_config` | Melhoria de precisão após recuperação inicial | Filtra 20 candidatos para os 5 que realmente respondem a pergunta |
| `vector_store` | Onde os vetores vivem | pgvector, Chroma, FAISS, Qdrant — decisões de camada de persistência |
| `graph_rag_config` | Recuperação de conhecimento relacional | Quando "encontre documentos similares" não é suficiente — você precisa de "encontre documentos conectados a X via relação Y" |
| `agentic_rag` | Loops de recuperação controlados por agente | Raciocínio multi-hop: encontre A, use A para encontrar B, use B para responder |

**Tente agora — RAG sem código:**
Faça upload de um PDF para o Claude. Faça uma pergunta sobre ele. Isso É RAG — Retrieval Augmented Generation (Geração Aumentada por Recuperação). O AI recuperou chunks relevantes do seu documento e aumentou a geração com eles. A diferença entre essa experiência de tier gratuito e um sistema RAG de produção é: (1) escala — milhares de documentos, não um PDF; (2) precisão — chunking e reranking ajustados; (3) freshness — reindexação automática quando as fontes mudam.

**Tente agora — intuição de Chunk Strategy:**
Pegue um documento de 10 páginas. Cole todas as 10 páginas no ChatGPT e faça uma pergunta específica. Depois cole apenas os 2 parágrafos mais relevantes para aquela pergunta e faça a mesma pergunta. A versão focada quase sempre vence. Isso é chunking — a disciplina de alimentar o conteúdo CERTO, não todo o conteúdo.

**Tente agora — intuição de Busca Semântica:**
Peça ao Claude: "Encontre qualquer coisa relacionada à frustração de clientes com tempos de entrega." Observe como ele traz passagens sobre logística, fulfillment, tempos de espera e envio — mesmo quando nenhuma dessas passagens usa a frase exata "tempos de entrega." Isso é busca semântica via embeddings. O AI entende significado, não apenas padrões de caracteres.

### Kinds de Conhecimento Estruturado — Ontologias e Grafos

| Kind | Capacidade Universal | Quando a Busca Plana Falha |
|------|---------------------|---------------------------|
| `knowledge_graph` | Mapas de entidades + relações | "Quais empresas a OpenAI adquiriu?" requer travessia, não busca por similaridade |
| `ontology` | Taxonomia formal — vocabulário controlado | Evita que o AI use "cliente", "usuário" e "comprador" como sinônimos |
| `repo_map` | Extração de contexto ciente de código | Navegação em codebases grandes para RAG ciente de código |

### Templates de Vertical por Indústria — Conformidade de Domínio Pré-construída

Esses são scaffolds, não documentos genéricos. Cada um codifica os padrões de conformidade, padrões de integração e vocabulário de domínio para uma indústria específica:

| Template | O Que Pré-codifica |
|----------|-------------------|
| `ecommerce_vertical` | Padrões PCI-DSS, abandono de carrinho, estruturas de motor de recomendação |
| `fintech_vertical` | SOC2, KYC/AML, padrões de detecção de fraude |
| `healthcare_vertical` | HIPAA, HL7/FHIR, regras de tratamento de PHI |
| `legal_vertical` | Regras de privilégio advocatício, estruturas de hora faturável, padrões de análise de contratos |

> **Impacto no mundo real:** Um AI de saúde sem conhecimento `healthcare_vertical` dará respostas genéricas sobre dados de pacientes. Com ele carregado, ele conhece o padrão mínimo necessário da HIPAA, a diferença entre PHI e dados desidentificados, e quais campos acionam regras de divulgação. Essa é a diferença entre uma demo e um sistema deployável.

### Kinds de Inteligência Comercial

| Kind | Capacidade Universal |
|------|---------------------|
| `competitive_matrix` | Battle cards — comparação de features para habilitação de vendas |
| `discovery_questions` | Bancos de perguntas MEDDIC/BANT para qualificação estruturada de prospects |
| `lineage_record` | Cadeias de proveniência — como esse conhecimento foi derivado? |
| `domain_vocabulary` | Registro canônico de termos — impor linguagem consistente em um sistema |

---

## Padrões de Engenharia Fundamentais

### O knowledge_card como Unidade Atômica

O `knowledge_card` (KC) é o artefato fundamental de P01. Todo o resto em P01 ou alimenta os KCs ou serve para torná-los recuperáveis.

Um KC tem restrições estritas:
- **max_bytes: 5120** — força densidade, evita inchaço
- **density_score >= 0.8** — cada frase deve carregar informação não-óbvia; sem preenchimento vazio
- **13 campos obrigatórios de frontmatter**: `id`, `kind`, `pillar`, `title`, `version`, `created`, `updated`, `author`, `domain`, `quality`, `tags`, `tldr`, `when_to_use`
- **padrão de nomenclatura**: `p01_kc_{topico}.md` com um irmão `.yaml` compilado

Três subtipos de KC existem com estruturas de corpo distintas:
- **domain_kc**: conhecimento vertical (quick_reference, key_concepts, golden_rules, visual_flow)
- **meta_kc**: conhecimento transversal do sistema (executive_summary, patterns, anti_patterns, application)
- **kind_kc**: meta-conhecimento sobre um kind do CEXAI em si (spec, cross_framework_map, decision_tree)

Os campos `tldr` e `title` são os principais sinais de ranking BM25. Cada cabeçalho `## ` define um limite de chunk de embedding. Isso significa que a estrutura do KC afeta diretamente a qualidade da recuperação — KCs mal estruturados são difíceis de encontrar mesmo quando seu conteúdo está correto.

**A lição universal:** armazenamento estruturado de fatos supera texto não-estruturado em escala. Quando você tem 5 fatos em um system prompt, não-estruturado funciona bem. Quando você tem 500 fatos, precisa de um sistema de recuperação que encontre os 5 certos dentre os 500. É aí que os KCs se tornam essenciais.

Referências cruzadas via campos `linked_artifacts` e `related` transformam o corpus de KCs em um grafo navegável. O `cex_retriever.py` do repositório usa atualmente TF-IDF sobre 2.184 documentos com vocabulário de 12K; recuperação baseada em vetores é o caminho de atualização.

### O Pipeline RAG: Três Kinds como Um Sistema

A stack RAG mínima em P01 são três kinds trabalhando juntos:

```
chunk_strategy + embedding_config + retriever_config = pipeline RAG
```

1. **chunk_strategy** decide *como* dividir documentos antes da indexação. O exemplo canônico no repositório CEXAI (`ex_chunk_strategy_recursive_1000.md`) usa RecursiveCharacterTextSplitter com `chunk_size=1000`, `chunk_overlap=200` e separadores cientes de Markdown (`\n## `, `\n### `, `\n#### `). Ele conta tokens com tiktoken (cl100k_base), não caracteres — o alinhamento com o espaço de tokens do modelo de embedding importa. Benchmarks no corpus do repositório mostram 0.89 de recall@5 com essa configuração vs 0.81 sem o overlap de 20%.

2. **embedding_config** especifica o modelo, dimensões e quaisquer configurações específicas do provedor. O exemplo nomic-embed-text no repositório usa 768 dimensões e roda localmente via Ollama a custo zero de API. Mudar o modelo de embedding requer reindexação completa — essa é uma decisão de nível de schema, não um toggle de runtime.

3. **retriever_config** é onde os trade-offs de recall/precisão são feitos. O padrão de recuperação híbrida em `ex_retriever_config_hybrid_rag.md` combina BM25 (peso 0.3) para consultas de termos exatos com busca densa FAISS (peso 0.7) para consultas semânticas. Um reranker Cohere reduz 20 candidatos iniciais para o top_k=5 final, entregando +12% MRR@5 vs sem reranker.

Esse padrão de três kinds mapeia diretamente para todos os principais frameworks de engenharia LLM:

| Kind P01 | Equivalente LangChain | Equivalente LlamaIndex |
|----------|----------------------|----------------------|
| `chunk_strategy` | `RecursiveCharacterTextSplitter` | `SentenceSplitter` |
| `embedding_config` | `OpenAIEmbeddings` / `OllamaEmbeddings` | `OpenAIEmbedding` |
| `vector_store` | `FAISS`, `Chroma`, `PGVector` | `VectorStoreIndex` |
| `retriever_config` | `EnsembleRetriever` + `ContextualCompressionRetriever` | `VectorIndexRetriever` + `Reranker` |

> **Por que isso importa para você:** A diferença entre uma assinatura de R$100/mês do ChatGPT e um deployment enterprise de R$1M é — quase inteiramente — gestão de conhecimento. O sistema enterprise não é mais inteligente. Ele tem conhecimento mais bem estruturado, melhor recuperação e melhor injeção. Você pode replicar 80% disso com ferramentas open-source e um P01 bem projetado.

### Knowledge Graph e Ontologia: Conhecimento Relacional Estruturado

A busca vetorial plana resolve "encontre documentos similares a esta consulta." Ela não resolve "quais empresas a OpenAI adquiriu?" ou "quais são os temas globais neste corpus?" Isso requer `knowledge_graph` e `graph_rag_config`.

O kind `knowledge_graph` define:
- **entity_types** — lista branca restrita (extração irrestrita causa explosão de nós)
- **relation_types** — lista branca restrita (previne relações alucinadas)
- **extraction_prompt** — o prompt LLM que extrai triplas (sujeito, predicado, objeto) do texto
- **storage_backend** — `neo4j`, `falkordb`, `in_memory` ou `json`
- **traversal_strategy** — `local` (centrado em entidade), `global` (resumos de comunidade via Leiden/Louvain) ou `hybrid`
- **dedup_strategy** — `exact`, `fuzzy` ou `llm` (resolução de entidades: "OpenAI" = "Open AI")

O anti-padrão central é usar knowledge graph onde busca vetorial plana é suficiente. A árvore de decisão é clara: Q&A plano → vetores apenas; perguntas sobre "temas/tendências" → GraphRAG com detecção de comunidade; ontologia de domínio conhecida → grafo com schema restrito.

### Agentic RAG: Quando o Agente Dirige a Recuperação

RAG padrão é um pipeline fixo: consulta → embedding → recuperação → injeção. **Agentic RAG** (kind `agentic_rag`) transforma a recuperação em um loop controlado pelo agente: o agente decide *se* recuperar, *o que* recuperar, *quantos hops* executar, e *quando* a informação recuperada é suficiente antes de gerar.

Esse padrão se torna necessário quando:
- Consultas requerem raciocínio multi-hop (recuperar entidade A, usar A para consultar B)
- Documentos recuperados contêm ponteiros para outros documentos que também precisam ser recuperados
- O agente precisa avaliar a qualidade do conteúdo recuperado antes de se comprometer com ele

A implementação sempre envolve um `retriever_config` e adiciona um loop de raciocínio de agente ao redor dele. O agente tem ferramentas explícitas: `search(query)`, `fetch(url)`, `evaluate(docs)`, `synthesize(docs)`.

---

## Mergulho Arquitetural

### Grafo de Dependências

```
fontes externas
      |
   rag_source ─────────────────────┐
      |                            |
  chunk_strategy                   |
      |                            v
  embedder_provider ──> knowledge_card ──> context_doc
      |                     |              glossary_entry
  embedding_config           |              citation
      |                  few_shot_example   dataset_card
  vector_store                |
      |                  knowledge_graph
  retriever_config        ontology
      |
  reranker_config
      |
  agentic_rag (encapsula tudo acima)
```

O fluxo é unidirecional: fontes brutas são ingeridas, divididas em chunks, embutidas e armazenadas. KCs são escritos a partir de fatos destilados. A infraestrutura de recuperação lê dos vector stores para retornar KCs e outros artefatos. O `knowledge_graph` fica paralelo à recuperação plana e adiciona travessia relacional.

### O Padrão Template-First

Ao construir um novo KC, o pipeline 8F aplica Template-First em F4 REASON: se um KC similar existe (pontuação de recuperação >= 60%), adapte-o em vez de construir do zero. Isso não é uma disciplina específica do CEXAI — mapeia diretamente para o que engenheiros de prompt experientes fazem manualmente: encontrar uma estrutura de prompt existente que funciona, adaptá-la, em vez de começar do zero a cada vez.

### Ciclo de Vida do Conhecimento

```
DESCOBERTA             DESTILAÇÃO          VALIDAÇÃO
fonte externa ──> pesquisa bruta ──> knowledge_card ──> quality gate
rag_source          cluster_kc         densidade >= 0.8   quality >= 7.0
                    _reference/

PERSISTÊNCIA       INDEXAÇÃO              RECUPERAÇÃO        INJEÇÃO
git commit ──> cex_compile.py ──> cex_retriever.py ──> F3 INJECT
yaml irmão     TF-IDF / vetor     candidatos top_k    contexto no prompt
```

O passo de compilação produz um irmão `.yaml` para cada artefato `.md`. Essa representação em formato duplo (Markdown legível por humanos + YAML parseável por máquinas) é o que permite tanto a autoria de conteúdo quanto o consumo programático.

O versionamento é inegociável: o campo `version` no frontmatter deve ser incrementado em qualquer mudança de conteúdo. Drift silencioso é o modo de falha mais comum em sistemas de gestão de conhecimento.

---

## Exemplos Reais do Repositório

### Exemplo 1: `ex_knowledge_card_cex_lp01_knowledge.md`

Este é o KC autodescritivo do P01 — conhecimento sobre o próprio pilar Knowledge. Qualidade: 9.2, density_score: 1.0. Escolhas estruturais notáveis:

- A tabela **Comparativo** (seis tipos × propósito × tamanho × flag core) é maximamente densa — seis fatos por célula.
- O diagrama **Flow** mostra o pipeline de ingestão em 6 tokens por etapa.
- O campo `axioms` contém invariantes legíveis por máquina: "SEMPRE versionar knowledge_cards" e "NUNCA injetar conhecimento sem fonte verificável." Esses não são para humanos — são recuperados e injetados em prompts de builder para restringir a geração.
- `data_source` aponta para o artigo de Lewis et al. sobre RAG (arXiv 2005.11401) — a fundamentação empírica para a abordagem de geração aumentada por recuperação.

### Exemplo 2: `ex_chunk_strategy_recursive_1000.md`

Uma `chunk_strategy` de nível de produção com benchmarks. Detalhe técnico crucial: usa **tiktoken** (cl100k_base) para length_function, não o `len()` do Python. Divisão baseada em caracteres desalinha com o espaço de tokens do modelo de embedding — um bug comum que degrada silenciosamente o recall. Os quality gates embutidos no artefato são limiares explícitos: mín. 50 tokens (mesclar se menor), máx. 1200 (redividir), sem headings órfãos (heading sem >= 20 tokens de corpo é mesclado com o próximo chunk).

A seção "When NOT to Use" é orientação de engenharia essencial: dados tabulares (CSV/JSON) → StructuredSplitter; código-fonte → CodeSplitter com parsing ciente de linguagem; documentos abaixo de 500 tokens → sem chunking necessário.

### Exemplo 3: `ex_retriever_config_hybrid_rag.md`

A configuração do retriever RAG híbrido inclui uma tabela de benchmark completa (corpus de 1.957 documentos): MRR@5 = 0.82 para híbrido+rerank vs 0.71 para apenas denso vs 0.54 para apenas BM25. Latência em p50 é 180ms vs 45ms (denso) vs 12ms (BM25). Essa tabela de trade-offs é a decisão central de engenharia: se você precisa de latência < 100ms, BM25-only. Se você precisa de recall > 0.85, híbrido+rerank.

### Exemplo 4: `library/kind/kc_knowledge_graph.md`

O kind KC de knowledge graph demonstra o padrão de mapa cross-framework. Ele mapeia sistematicamente o mesmo conceito através do Microsoft GraphRAG, LlamaIndex KG, LangChain + Neo4j, LightRAG, Haystack, Amazon Neptune e FalkorDB. Esse mapa serve a dois propósitos de engenharia: (1) profissionais migrando entre frameworks podem encontrar o conceito equivalente; (2) o builder do CEXAI usa-o para gerar imports e configuração corretos para o framework alvo.

---

## Anti-Padrões — Erros Universais que Todo Mundo Comete

### Anti-Padrão 1: Confiar no Conhecimento Embutido em Vez de Fornecer o Seu

Este é o erro mais caro. Fazer deploy de um LLM puro sem gestão de conhecimento, observar alucinação e tentar corrigir com system prompts cada vez mais detalhados. A causa raiz é que o conhecimento vive no system prompt como texto indiferenciado — não versionado, não recuperável, sem density gate, sem fundamentação em fontes. Quando o conhecimento muda, o system prompt precisa ser reescrito manualmente.

**Lição universal:** o conhecimento de treinamento do seu AI tem 18-24 meses de defasagem e cobre seu domínio no nível da Wikipedia, não da expertise interna da sua empresa. A única forma de dar a ele conhecimento atual, específico e confiável é injetá-lo explicitamente no momento da geração. Isso é P01.

### Anti-Padrão 2: Colar Documentos Inteiros em Vez de Seções Relevantes

O erro mais comum de iniciantes. Colar um PDF de 50 páginas em um chat e fazer uma pergunta específica. O AI responderá — mas está trabalhando com ruído, não com sinal. Chunking é a disciplina de identificar e injetar as seções relevantes, não o documento inteiro.

**Lição universal:** o tamanho da janela de contexto não é uma licença para ser preguiçoso com gestão de conhecimento. Mais tokens não significa respostas melhores — significa mais oportunidades de diluir o sinal relevante com conteúdo irrelevante.

### Anti-Padrão 3: Pedir ao AI para "Lembrar" Sem Dar a Ele um Sistema

"Lembra isso para a próxima vez" dito a um LLM sem estado é um desejo, não uma instrução. O AI vai reconhecer e esquecer imediatamente. Memória requer infraestrutura externa: um banco de dados, um vector store, um sistema de arquivos, um sistema de knowledge cards. Qualquer um desses pode funcionar; nenhum acontece automaticamente.

**Lição universal:** sem estado é o padrão. Com estado requer engenharia deliberada. P01 é essa engenharia.

### Anti-Padrão 4: Violações de Densidade do KC

Escrever knowledge cards com frases de preenchimento ("Este documento fornece uma visão geral de...") causa dois problemas: (1) o density gate rejeita durante validação; (2) se de alguma forma admitido, dilui o sinal de recuperação. O campo `when_to_use` é o gatilho de recuperação — deve ser o mais específico possível. Valores vagos de `when_to_use` produzem falsos positivos na recuperação.

### Anti-Padrão 5: Instruções em Knowledge Cards

KCs respondem "o que é verdadeiro." Instruções respondem "o que fazer." Misturar isso — escrever "você deve usar busca híbrida quando..." em vez de "busca híbrida supera apenas denso em 12% MRR@5 quando..." — cria conhecimento que pertence a P03 (prompt) em vez de P01. A fronteira é aplicada pelo campo `boundary` no schema e pela validação F7.

### Anti-Padrão 6: Chunking Plano por Contagem de Caracteres

Dividir por contagem fixa de caracteres ignora a estrutura do documento. Uma divisão de 1000 caracteres no meio de um bloco de código produz dois chunks inúteis. A abordagem correta é hierarquia de separadores: dividir no nível de heading primeiro, depois parágrafos, depois linhas, depois palavras — apenas caindo para divisões de caracteres como último recurso.

### Anti-Padrão 7: Modelo de Embedding Único para Coleções Mistas

Misturar vetores de diferentes modelos de embedding na mesma coleção causa comparações de similaridade coseno em espaços incompatíveis. O kind `vector_store` aplica `dimensions` como campo obrigatório especificamente para capturar isso no tempo de configuração em vez de no tempo de consulta.

### Anti-Padrão 8: Extração de Grafo Irrestrita

Executar extração de entidades sobre um corpus sem uma lista branca explícita de `entity_types` produz um grafo com milhares de nós, a maioria dos quais é ruído. O kind `knowledge_graph` requer `entity_types` e `relation_types` como campos obrigatórios. A qualidade do grafo correlaciona diretamente com a especificidade da ontologia.

---

## Conexão com Outros Pilares

### P01 → P03 Prompt (conhecimento alimenta a construção do prompt)

Esta é a dependência mais direta. F3 INJECT no pipeline 8F carrega artefatos P01 (KCs, context_docs, few_shot_examples) no prompt no tempo de geração. Um template de prompt (P03) sem injeção P01 é um template estático; um template de prompt com injeção P01 torna-se uma superfície de geração dinâmica, fundamentada em conhecimento.

**Lição universal:** todo prompt sofisticado que você já viu e que funciona de forma confiável tem P01 embutido — mesmo que informalmente. O padrão "você é um especialista em X, aqui estão os fatos relevantes: [cola fatos]" É injeção de conhecimento. O CEXAI apenas formaliza e automatiza isso.

### P01 → P10 Memory (conhecimento persiste entre sessões)

P10 Memory é a extensão com estado de P01 Knowledge. Onde um KC é versionado e estável (escreva-uma-vez-depois-versione), entity memories (P10) são mutáveis — representam o que o sistema aprendeu durante interações. O `knowledge_index` (P10) é o índice que torna o conteúdo P01 recuperável em runtime.

### P01 → P07 Evaluation (qualidade do conhecimento é avaliada)

Quality gates no pipeline 8F (F7 GOVERN) comparam artefatos gerados com ground truth. Esse ground truth é P01. O campo `quality` em cada KC é atribuído por revisão de pares (nunca auto-pontuado). `cex_score.py` executa três camadas de pontuação: estrutural (30%, automatizado), rubrica (30%, dimensões de quality gate) e semântico (40%, avaliação por LLM quando camadas 1+2 passam o limiar).

### P01 → P08 Architecture (conhecimento informa decisões arquiteturais)

Decision records (P08) referenciam KCs como evidência. Quando uma decisão de arquitetura é tomada — "usar recuperação híbrida em vez de apenas densa" — o KC contendo os dados de benchmark é vinculado como fonte de evidência. Isso cria uma trilha de auditoria da decisão até os dados.

### P01 → P02 Model (agentes são carregados com KCs de domínio no boot)

Configurações de boot de agentes referenciam KCs P01 como fontes de contexto obrigatórias. O `agent_card` do agente (P08) lista quais KCs devem ser injetados em F3. É assim que um agente de suporte ao cliente "sabe" sobre features do produto, preços e políticas — não por fine-tuning, mas por injeção estruturada de KC em cada invocação.

---

## O Princípio Fractal e o Papel do P01

O sistema CEXAI aplica a mesma estrutura de 12 pilares em toda escala. P01 é o primeiro pilar adicionado quando um prompt precisa de memória:

```
L0 Prompt: apenas P03 (template estático, zero conhecimento)
L1 Chain: P03 + P12 (prompts encadeados, sem conhecimento)
L2 Agente: P01 + P02 + P03 + P06 (conhecimento injetado, agente tem identidade)
L3 Runtime: +P04 + P09 (ferramentas + configuração)
L4 Agent_group: +P10 + P11 (memória + feedback)
L5 Sistema: todos os 12 pilares
```

No momento em que você precisa que o agente saiba qualquer coisa específica do domínio — preços, regulações, especificações do produto, cenário competitivo — você ativa P01. Esse é o limiar entre uma demo de brinquedo e um sistema de IA de nível de produção.

A consequência prática para times de engenharia: o investimento em P01 é o que distingue sistemas LLM que melhoram com o tempo (corpus de KC cresce, é versionado, é recuperado com mais precisão) daqueles que degradam com o tempo (system prompts inflam, ficam inconsistentes, perdem fatos). P01 é onde o conhecimento organizacional se torna patrimônio computável — não texto jogado em um prompt, mas artefatos tipados, pesquisáveis e governados que qualquer agente pode consumir.

---

## Guia de Decisão: Qual Kind P01 Usar?

```
Tenho um fato de domínio para capturar?
  |-- É uma única definição de termo? --> glossary_entry (max 512B)
  |-- É um contexto amplo de fundo? --> context_doc (max 2048B)
  |-- É um fato denso e pesquisável? --> knowledge_card (max 5120B, densidade >= 0.8)
  |-- É uma fonte externa para indexar? --> rag_source (URL + freshness)
  |-- É um par input/output de ensino? --> few_shot_example

Preciso construir um pipeline RAG?
  |-- Como dividir meus documentos? --> chunk_strategy
  |-- Qual modelo vetorial usar? --> embedding_config + embedder_provider
  |-- Onde armazenar os vetores? --> vector_store
  |-- Como buscar? (recall/precisão) --> retriever_config
  |-- Preciso melhorar precisão pós-busca? --> reranker_config
  |-- O agente precisa controlar o loop de recuperação? --> agentic_rag

Meu domínio tem relações complexas entre entidades?
  |-- Perguntas multi-hop necessárias? --> knowledge_graph + graph_rag_config
  |-- Preciso de vocabulário controlado? --> ontology + domain_vocabulary

Estou construindo para uma indústria específica?
  |-- eCommerce, EdTech, Fintech, Healthcare, Legal, GovTech? --> vertical_template correspondente
```

Esse guia de decisão é executável através do `_tools/cex_intent_resolver.py` — Python-first, zero tokens de LLM, mapeamento direto de intenção para kind via padrões bilíngues PT+EN.

## Artefatos Relacionados

| Artefato | Relacionamento | Score |
|----------|---------------|-------|
| [[kc_pillar_brief_p01_knowledge_en]] | translation | 1.00 |
| [[kc_pillar_brief_p02_model_pt]] | sibling | 0.85 |
| [[kc_pillar_brief_p03_prompt_pt]] | sibling | 0.82 |
| [[cm_driver_01_structured_thinking]] | downstream | 0.60 |
| [[kc_lens_factory]] | upstream | 0.45 |
| [[kc_lens_index]] | upstream | 0.43 |
| [[p01_kc_8f_pipeline]] | related | 0.41 |
| [[p01_kc_rag_fundamentals]] | related | 0.39 |
| [[p01_kc_knowledge_graph]] | related | 0.38 |
| [[mentor_context]] | upstream | 0.38 |
