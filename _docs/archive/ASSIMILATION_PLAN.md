---
id: assimilation_plan_agno
kind: context_doc
pillar: P08
title: "Plano de Assimilação Agno → CEX — Versionamento Universal LLM"
version: 1.0.0
author: N07
created: 2026-04-01
quality: 9.0
tags: [assimilation, agno, roadmap, versioning, runtime, sdk]
tldr: "4 fases, 8 semanas, 14 módulos. Absorve runtime do Agno como camada P04/P02 do CEX. De v6.0 para v10.0."
density_score: 1.0
---

# Plano de Assimilação Agno → CEX

## Filosofia

```
CEX não copia o Agno inteiro.
CEX absorve os PADRÕES UNIVERSAIS e os veste com a gramática CEX.

Agno code → adapta namespace → veste com frontmatter CEX → 
registra como kind → builder ISOs → 8F pipeline → versionado.
```

**Regra**: Todo código absorvido passa por:
1. Rename namespace `agno.*` → `cex.*`
2. Frontmatter CEX obrigatório em todo .py (docstring padrão)
3. Registro no kinds_meta.json
4. Builder ISO gerado (13 arquivos)
5. Teste mínimo (smoke + unit)

---

## Versioning Strategy

```
CEX 6.0.0  (atual)     — Governance
CEX 7.0.0  (Fase 1)    — Runtime Foundation
CEX 8.0.0  (Fase 2)    — Knowledge Pipeline
CEX 9.0.0  (Fase 3)    — Execution Engine
CEX 10.0.0 (Fase 4)    — Integrations + Production
```

Cada versão = 1 minor por sub-módulo absorvido:
```
7.0.0 → 7.1.0 (Model SDK) → 7.2.0 (Toolkit) → 7.3.0 (Guardrails) → 7.4.0 (Structured Output)
```

---

## Árvore de Destino (onde cada módulo aterrissa no CEX)

```
cex/
├── _tools/                          # Existente (25K lines)
│   ├── cex_*.py                     # Ferramentas existentes mantidas
│   └── tests/                       # Testes existentes mantidos
│
├── cex_sdk/                         # ← NOVO: Runtime absorvido do Agno
│   ├── __init__.py
│   ├── models/                      # ← agno/models/ adaptado
│   │   ├── __init__.py
│   │   ├── base.py                  # Model ABC (invoke/ainvoke)
│   │   ├── message.py               # Message dataclass
│   │   ├── response.py              # ModelResponse + ToolExecution
│   │   ├── metrics.py               # RunMetrics, token counting
│   │   └── providers/
│   │       ├── anthropic.py         # Claude wrapper
│   │       ├── openai.py            # GPT wrapper
│   │       ├── google.py            # Gemini wrapper
│   │       ├── ollama.py            # Local models
│   │       ├── openrouter.py        # Multi-provider
│   │       └── litellm.py           # Fallback universal
│   │
│   ├── tools/                       # ← agno/tools/ adaptado
│   │   ├── __init__.py
│   │   ├── toolkit.py               # Toolkit base class
│   │   ├── function.py              # Function wrapper + auto-schema
│   │   ├── decorator.py             # @tool decorator
│   │   ├── mcp/                     # MCP bridge
│   │   │   ├── __init__.py
│   │   │   ├── client.py            # MCPTools
│   │   │   └── multi.py             # MultiMCPTools
│   │   └── builtin/                 # 10 tools essenciais absorvidos
│   │       ├── file.py
│   │       ├── shell.py
│   │       ├── python.py
│   │       ├── sql.py
│   │       ├── websearch.py
│   │       ├── website.py
│   │       ├── github.py
│   │       ├── calculator.py
│   │       ├── csv_toolkit.py
│   │       └── json_toolkit.py      # (placeholder — import sob demanda)
│   │
│   ├── knowledge/                   # ← agno/knowledge/ adaptado
│   │   ├── __init__.py
│   │   ├── reader/
│   │   │   ├── base.py              # Reader ABC
│   │   │   ├── pdf.py
│   │   │   ├── docx.py
│   │   │   ├── markdown.py
│   │   │   ├── csv.py
│   │   │   ├── json.py
│   │   │   ├── web.py
│   │   │   ├── youtube.py
│   │   │   └── arxiv.py
│   │   ├── chunking/
│   │   │   ├── base.py              # ChunkStrategy ABC
│   │   │   ├── fixed.py
│   │   │   ├── recursive.py
│   │   │   ├── semantic.py
│   │   │   ├── markdown.py
│   │   │   └── code.py
│   │   ├── embedder/
│   │   │   ├── base.py              # Embedder ABC
│   │   │   ├── openai.py
│   │   │   ├── cohere.py
│   │   │   ├── sentence_transformer.py
│   │   │   └── ollama.py
│   │   └── reranker/
│   │       ├── base.py
│   │       └── cohere.py
│   │
│   ├── vectordb/                    # ← agno/vectordb/ adaptado
│   │   ├── __init__.py
│   │   ├── base.py                  # VectorDb ABC
│   │   ├── chroma.py
│   │   ├── qdrant.py
│   │   ├── pgvector.py
│   │   ├── pinecone.py
│   │   └── lancedb.py               # Top 5 mais usados
│   │
│   ├── memory/                      # ← agno/memory/ + agno/learn/ adaptado
│   │   ├── __init__.py
│   │   ├── manager.py               # MemoryManager (LLM-powered)
│   │   ├── compression.py           # CompressionManager
│   │   ├── stores/
│   │   │   ├── user_profile.py
│   │   │   ├── user_memory.py
│   │   │   ├── entity_memory.py
│   │   │   ├── session_context.py
│   │   │   ├── learned_knowledge.py
│   │   │   └── decision_log.py
│   │   └── config.py                # LearningMode, configs
│   │
│   ├── guardrails/                  # ← agno/guardrails/ adaptado
│   │   ├── __init__.py
│   │   ├── base.py                  # BaseGuardrail ABC
│   │   ├── pii.py                   # PIIDetectionGuardrail
│   │   ├── prompt_injection.py      # PromptInjectionGuardrail
│   │   └── moderation.py            # OpenAI moderation
│   │
│   ├── workflow/                    # ← agno/workflow/ adaptado
│   │   ├── __init__.py
│   │   ├── step.py                  # Step (agent/team/executor)
│   │   ├── parallel.py              # Parallel execution
│   │   ├── loop.py                  # Loop with condition
│   │   ├── condition.py             # Conditional branching
│   │   ├── router.py                # Dynamic routing
│   │   └── types.py                 # StepInput, StepOutput, OnError
│   │
│   ├── eval/                        # ← agno/eval/ adaptado
│   │   ├── __init__.py
│   │   ├── base.py                  # BaseEval (pre_check/post_check)
│   │   └── accuracy.py              # AccuracyEval
│   │
│   ├── reasoning/                   # ← agno/reasoning/ adaptado
│   │   ├── __init__.py
│   │   ├── step.py                  # ReasoningStep + NextAction
│   │   └── manager.py               # Chain-of-thought orchestrator
│   │
│   ├── session/                     # ← agno/session/ adaptado
│   │   ├── __init__.py
│   │   ├── base.py                  # Session state management
│   │   └── db.py                    # SQLite/Postgres persistence
│   │
│   ├── tracing/                     # ← agno/tracing/ adaptado
│   │   ├── __init__.py
│   │   ├── exporter.py
│   │   └── schemas.py
│   │
│   └── utils/                       # ← agno/utils/ selecionados
│       ├── __init__.py
│       ├── log.py
│       ├── timer.py
│       └── safe_formatter.py
│
├── P01_knowledge/                   # EXISTENTE — ganha readers/chunking
│   ├── readers/                     # ← symlink ou import de cex_sdk/knowledge/reader
│   └── chunking/                    # ← symlink ou import de cex_sdk/knowledge/chunking
│
├── P02_model/                       # EXISTENTE — ganha model SDK
│   └── sdk/                         # ← symlink ou import de cex_sdk/models
│
├── P04_tools/                       # EXISTENTE — ganha toolkit framework
│   └── sdk/                         # ← symlink ou import de cex_sdk/tools
│
├── P07_evals/                       # EXISTENTE — ganha guardrails
│   └── guardrails/                  # ← symlink ou import de cex_sdk/guardrails
│
└── P12_orchestration/               # EXISTENTE — ganha workflow primitives
    └── workflows/                   # ← symlink ou import de cex_sdk/workflow
```

---

## FASE 1: Runtime Foundation (v7.0.0) — Semana 1-2

### Objetivo
Dar ao CEX a capacidade de **chamar LLMs programaticamente** em vez de via subprocess CLI.

### 1.1 Model SDK (v7.1.0)

**Fonte Agno:** `libs/agno/agno/models/` (100 files, 18.452 lines)
**Destino CEX:** `cex_sdk/models/`
**Absorve:** base.py, message.py, response.py, metrics.py + 6 providers

```
TAREFAS:
├── [T1.1.1] Criar cex_sdk/__init__.py com version = "7.1.0"
├── [T1.1.2] Copiar+adaptar agno/models/base.py → cex_sdk/models/base.py
│   ├── Rename: agno.* → cex_sdk.*
│   ├── Remover: refs a agno.cloud, agno.api (SaaS coupling)
│   ├── Manter: Model ABC, invoke(), ainvoke(), MessageData
│   └── Adicionar: docstring CEX + type hints
├── [T1.1.3] Copiar+adaptar agno/models/message.py → cex_sdk/models/message.py
├── [T1.1.4] Copiar+adaptar agno/models/response.py → cex_sdk/models/response.py
├── [T1.1.5] Copiar+adaptar agno/models/metrics.py → cex_sdk/models/metrics.py
├── [T1.1.6] Provider: anthropic.py (Claude)
│   ├── Fonte: agno/models/anthropic/claude.py (~600L)
│   └── Adaptar: remover agno.cloud telemetry
├── [T1.1.7] Provider: openai.py (GPT-4)
├── [T1.1.8] Provider: google.py (Gemini)
├── [T1.1.9] Provider: ollama.py (local)
├── [T1.1.10] Provider: openrouter.py (multi)
├── [T1.1.11] Provider: litellm.py (fallback universal)
├── [T1.1.12] Testes: test_model_base.py, test_providers.py
├── [T1.1.13] Registrar kind "model_provider" em kinds_meta.json
│   └── Pillar: P02 (já tem model_card kind)
└── [T1.1.14] Atualizar cex_8f_runner.py F5 CALL para usar SDK
    └── Manter subprocess como fallback se SDK não disponível
```

**Critério de aceite:**
```python
from cex_sdk.models.providers.anthropic import Claude
model = Claude(id="claude-sonnet-4-6")
response = model.invoke([Message(role="user", content="Hello")])
assert response.content  # Funciona sem subprocess
```

**Impacto no 8F:**
- F5 CALL: Usa `model.invoke()` em vez de `subprocess.run(["claude", ...])`
- F7 GOVERN: Pode inspecionar `response.metrics` (tokens, latência)

### 1.2 Toolkit Framework (v7.2.0)

**Fonte Agno:** `libs/agno/agno/tools/toolkit.py` + `function.py` (~2.500L)
**Destino CEX:** `cex_sdk/tools/`

```
TAREFAS:
├── [T1.2.1] Copiar+adaptar toolkit.py
│   ├── Manter: Toolkit class, auto-registration, include/exclude
│   ├── Remover: cache_dir (CEX tem seu próprio .cex/cache)
│   └── Adicionar: Integração com CEX kind "function_def" (P04)
├── [T1.2.2] Copiar+adaptar function.py
│   ├── Manter: Function dataclass, get_entrypoint_docstring, auto-schema
│   ├── Remover: UserFeedbackQuestion (CEX tem GDP)
│   └── Adicionar: Mapeamento para JSON Schema do P04 function_def kind
├── [T1.2.3] Criar decorator.py com @cex_tool
│   └── Pattern: @cex_tool(name="x", kind="function_def", pillar="P04")
├── [T1.2.4] Testes: test_toolkit.py, test_function.py
├── [T1.2.5] Migrar signal_writer.py para usar Toolkit pattern
└── [T1.2.6] Registrar kind "toolkit" em kinds_meta.json (P04)
```

**Critério de aceite:**
```python
from cex_sdk.tools import Toolkit, cex_tool

class MyTools(Toolkit):
    @cex_tool(kind="function_def")
    def search(self, query: str) -> str:
        """Busca no índice CEX."""
        return cex_retriever.query(query)

# Auto-gera JSON Schema para LLM tool_use
tools = MyTools()
assert tools.functions["search"].parameters  # Schema gerado
```

### 1.3 Guardrails (v7.3.0)

**Fonte Agno:** `libs/agno/agno/guardrails/` (5 files, **315 lines**)
**Destino CEX:** `cex_sdk/guardrails/`

```
TAREFAS:
├── [T1.3.1] Copiar base.py → adaptar BaseGuardrail
│   ├── Adicionar: hook no F7 GOVERN como pre_check
│   └── Manter: check() / async_check() pattern
├── [T1.3.2] Copiar pii.py (regex-based PII detection)
│   └── Adicionar: padrões BR (CPF, CNPJ, CEP, telefone BR)
├── [T1.3.3] Copiar prompt_injection.py
│   └── Adicionar: patterns PT-BR
├── [T1.3.4] Copiar openai moderation wrapper
├── [T1.3.5] Integrar com 8F pipeline:
│   ├── F1 CONSTRAIN: Guardrails no input
│   └── F7 GOVERN: Guardrails no output
├── [T1.3.6] Testes: test_guardrails.py
├── [T1.3.7] Registrar kind "guardrail" em kinds_meta.json (P07)
└── [T1.3.8] Criar builder ISO: archetypes/builders/guardrail-builder/
```

**Módulo MAIS fácil de absorver** — 315 linhas, zero deps externas, valor imediato.

### 1.4 Structured Output (v7.4.0)

**Fonte Agno:** Pattern `response_model=` de `agno/agent/_run.py`
**Destino CEX:** `cex_sdk/models/structured.py`

```
TAREFAS:
├── [T1.4.1] Criar structured.py com parse_structured_output()
│   ├── Input: response text + Pydantic BaseModel class
│   ├── Output: validated model instance
│   └── Fallback: regex extraction se JSON parse falhar
├── [T1.4.2] Integrar com F6 PRODUCE do 8F
│   └── Se kind tem schema Pydantic → forçar structured output
├── [T1.4.3] Criar base models para kinds CEX existentes:
│   ├── KnowledgeCard(BaseModel)
│   ├── AgentSpec(BaseModel)
│   ├── FunctionDef(BaseModel)
│   └── EvalResult(BaseModel)
├── [T1.4.4] Testes: test_structured.py
└── [T1.4.5] Adicionar pyproject.toml dep: pydantic>=2.0
```

### Entregável Fase 1
```
pyproject.toml:
  version = "7.4.0"
  dependencies = ["pyyaml>=6.0", "pydantic>=2.0"]
  [project.optional-dependencies]
  sdk = ["anthropic>=0.39.0", "openai>=1.0", "google-genai>=1.0"]
  local = ["ollama"]
  all = ["litellm"]

Novos arquivos: ~35 files em cex_sdk/
Testes novos: ~12
Kinds novos: model_provider, toolkit, guardrail
Builders novos: 3 (model-provider-builder, toolkit-builder, guardrail-builder)
```

---

## FASE 2: Knowledge Pipeline (v8.0.0) — Semana 3-4

### Objetivo
Dar ao CEX a capacidade de **ingerir, chunkar, embeddar e buscar** conhecimento externo — substituindo TF-IDF por vector search real.

### 2.1 Knowledge Readers (v8.1.0)

**Fonte Agno:** `libs/agno/agno/knowledge/reader/` (21 readers, ~4.000L)
**Destino CEX:** `cex_sdk/knowledge/reader/`

```
TAREFAS:
├── [T2.1.1] Copiar+adaptar base.py (Reader ABC)
│   ├── Interface: read(path) → List[Document]
│   └── Document = agno/knowledge/document/base.py adaptado
├── [T2.1.2] Copiar readers prioritários (8 de 21):
│   ├── pdf_reader.py       — PyMuPDF/pymupdf4llm
│   ├── docx_reader.py      — python-docx
│   ├── markdown_reader.py  — nativo
│   ├── csv_reader.py       — nativo
│   ├── json_reader.py      — nativo
│   ├── website_reader.py   — BeautifulSoup
│   ├── youtube_reader.py   — transcripts
│   └── arxiv_reader.py     — pesquisa acadêmica
├── [T2.1.3] Integrar com P01 schema:
│   └── Reader output → kind "rag_source" ou "knowledge_card" automático
├── [T2.1.4] Integrar com F3 INJECT do 8F:
│   └── Se input é URL/path → auto-detect reader → inject no contexto
├── [T2.1.5] CLI: python -m cex_sdk.knowledge.reader --file doc.pdf --output kc
├── [T2.1.6] Testes: test_readers.py (mocks para cada formato)
└── [T2.1.7] Registrar kind "document_loader" em kinds_meta.json (P04)
    └── Já existe! Apenas linkar com implementação
```

### 2.2 Chunking Strategies (v8.2.0)

**Fonte Agno:** `libs/agno/agno/knowledge/chunking/` (9 strategies, ~2.000L)
**Destino CEX:** `cex_sdk/knowledge/chunking/`

```
TAREFAS:
├── [T2.2.1] Copiar+adaptar strategy.py (ChunkStrategy ABC)
│   ├── Interface: chunk(document) → List[Document]
│   └── Parâmetros: chunk_size, chunk_overlap, separators
├── [T2.2.2] Copiar 5 estratégias core:
│   ├── fixed.py         — tamanho fixo
│   ├── recursive.py     — recursive character text splitter
│   ├── semantic.py      — embedding-based boundaries
│   ├── markdown.py      — header-aware splitting
│   └── code.py          — language-aware splitting
├── [T2.2.3] Integrar com P01 kind "chunk_strategy":
│   └── Já tem o kind definido! chunk_size, chunk_overlap no schema
├── [T2.2.4] Conectar com cex_retriever.py:
│   └── retriever agora aceita estratégia de chunking configurável
├── [T2.2.5] Testes: test_chunking.py
└── [T2.2.6] Criar builder ISO: chunk-strategy-builder/ (já existe!)
    └── Atualizar com ref para implementação SDK
```

### 2.3 Embeddings + VectorDB (v8.3.0)

**Fonte Agno:** `libs/agno/agno/knowledge/embedder/` (19 providers) + `libs/agno/agno/vectordb/` (22 backends)
**Destino CEX:** `cex_sdk/knowledge/embedder/` + `cex_sdk/vectordb/`

```
TAREFAS:
├── [T2.3.1] Copiar+adaptar embedder base.py
│   └── Interface: embed(text) → List[float], embed_batch(texts) → List[List[float]]
├── [T2.3.2] Copiar 4 embedder providers:
│   ├── openai.py           — text-embedding-3-small
│   ├── cohere.py           — embed-v4
│   ├── sentence_transformer.py — local (MTEB)
│   └── ollama.py           — local embeddings
├── [T2.3.3] Copiar+adaptar vectordb base.py
│   └── Interface: create(), insert(), search(), delete()
├── [T2.3.4] Copiar 5 vectordb backends:
│   ├── chroma.py           — zero-config local (dev)
│   ├── lancedb.py          — embedded (produção leve)
│   ├── qdrant.py           — cloud/local
│   ├── pgvector.py         — Postgres extension
│   └── pinecone.py         — cloud managed
├── [T2.3.5] Evoluir cex_retriever.py:
│   ├── Modo 1 (default): TF-IDF (zero deps, mantém retrocompat)
│   ├── Modo 2: Vector search via cex_sdk embedder + vectordb
│   └── Modo 3: Hybrid (TF-IDF + vector, reranked)
├── [T2.3.6] Integrar com P01 kinds existentes:
│   ├── embedding_config: agora linkado a implementação real
│   ├── retriever_config: agora linkado a implementação real
│   └── knowledge_index (P10): agora instanciável
├── [T2.3.7] Testes: test_embedder.py, test_vectordb.py
├── [T2.3.8] Registrar kinds: "embedder_provider", "vector_store"
└── [T2.3.9] CLI: python -m cex_sdk.knowledge --build --embedder openai --db chroma
```

**Migração do cex_retriever.py:**
```python
# ANTES (v6.0):
from cex_retriever import load_index, query_index
results = query_index(index, "RAG chunking", top_k=5)  # TF-IDF

# DEPOIS (v8.3.0):
from cex_sdk.knowledge.embedder.openai import OpenAIEmbedder
from cex_sdk.vectordb.chroma import ChromaDb

embedder = OpenAIEmbedder(model="text-embedding-3-small")
db = ChromaDb(collection="cex_knowledge", embedder=embedder)
results = db.search(query="RAG chunking", limit=5)  # Vector search

# FALLBACK AUTOMÁTICO:
from cex_retriever import query  # Detecta se SDK disponível
results = query("RAG chunking")  # Usa vector se disponível, TF-IDF se não
```

### 2.4 Reranker (v8.4.0)

**Fonte Agno:** `libs/agno/agno/knowledge/reranker/` (6 files)
**Destino CEX:** `cex_sdk/knowledge/reranker/`

```
TAREFAS:
├── [T2.4.1] Copiar base.py (Reranker ABC)
├── [T2.4.2] Copiar cohere.py (Cohere reranker)
├── [T2.4.3] Copiar sentence_transformer.py (local reranker)
├── [T2.4.4] Integrar com retriever pipeline:
│   └── query → initial results → rerank → top_k final
└── [T2.4.5] Testes: test_reranker.py
```

### Entregável Fase 2
```
pyproject.toml:
  version = "8.4.0"
  [project.optional-dependencies]
  readers = ["pymupdf", "python-docx", "beautifulsoup4", "youtube-transcript-api"]
  embeddings = ["openai>=1.0", "sentence-transformers"]
  vectordb-chroma = ["chromadb"]
  vectordb-lance = ["lancedb"]
  vectordb-qdrant = ["qdrant-client"]
  vectordb-pg = ["pgvector", "psycopg2-binary"]

Novos arquivos: ~40 files em cex_sdk/knowledge/ + cex_sdk/vectordb/
Testes novos: ~15
cex_retriever.py atualizado com fallback TF-IDF ↔ Vector
```

---

## FASE 3: Execution Engine (v9.0.0) — Semana 5-6

### Objetivo
Dar ao CEX **workflow primitives**, **memory inteligente**, e **compression** — evoluindo de pipeline linear para execução DAG typed.

### 3.1 Workflow Primitives (v9.1.0)

**Fonte Agno:** `libs/agno/agno/workflow/` (15 files, 16.734L)
**Destino CEX:** `cex_sdk/workflow/`

```
TAREFAS:
├── [T3.1.1] Copiar+adaptar tipos base:
│   ├── types.py: StepInput, StepOutput, OnError, OnReject
│   └── Manter session_state pattern, remover WebSocket refs
├── [T3.1.2] Copiar step.py (Step com agent/team/executor)
│   ├── Adaptar: Step.agent aceita CEX nucleus ID
│   └── Adicionar: Step.kind para linkar com CEX kind system
├── [T3.1.3] Copiar parallel.py (execução paralela)
│   └── Mapear para CEX spawn_grid.ps1 (manter compatibilidade)
├── [T3.1.4] Copiar loop.py (loop com condição)
│   └── Integrar com cex_evolve.py (evolution = loop com metric)
├── [T3.1.5] Copiar condition.py (branching condicional)
│   └── Integrar com GDP: condition pode ser "ask_user"
├── [T3.1.6] Copiar router.py (roteamento dinâmico)
│   └── Mapear para CEX nucleus routing (N01-N07)
├── [T3.1.7] Integrar com cex_crew_runner.py:
│   ├── Manter DAG do Motor 8F como source of truth
│   ├── Cada step do DAG = Step(executor=8f_function)
│   └── Parallel steps = Parallel(step_f3, step_f5)
├── [T3.1.8] Integrar com P12 kinds existentes:
│   ├── workflow (P12): agora instanciável como Workflow()
│   ├── dag (P12): agora executável como Steps()
│   ├── checkpoint (P12): agora mapeado para Step state saving
│   └── schedule (P12): conectar com scheduler futuro
├── [T3.1.9] Testes: test_workflow.py, test_step.py, test_parallel.py
└── [T3.1.10] Registrar kind "workflow_primitive" em kinds_meta.json
```

**Integração 8F × Workflow:**
```python
from cex_sdk.workflow import Workflow, Step, Parallel, Condition

# O 8F pipeline agora é um Workflow tipado:
pipeline_8f = Workflow(
    name="8F Pipeline",
    steps=[
        Step(name="F1_CONSTRAIN", executor=constrain),
        Step(name="F2_BECOME", executor=become),
        Parallel(
            Step(name="F3_INJECT", executor=inject),
            Step(name="F4_REASON", executor=reason),
        ),
        Step(name="F5_CALL", executor=call),
        Step(name="F6_PRODUCE", executor=produce),
        Step(name="F7_GOVERN", executor=govern),
        Condition(
            check=lambda state: state.quality >= 8.0,
            on_true=Step(name="F8_COLLABORATE", executor=collaborate),
            on_false=Step(name="RETRY", executor=retry_loop),
        ),
    ]
)
```

### 3.2 Memory Manager (v9.2.0)

**Fonte Agno:** `libs/agno/agno/memory/` (6 files, 1.893L) + `libs/agno/agno/learn/` (14 files, 13.013L)
**Destino CEX:** `cex_sdk/memory/`

```
TAREFAS:
├── [T3.2.1] Copiar+adaptar MemoryManager
│   ├── Manter: LLM-powered extraction, CRUD tools
│   ├── Remover: agno.cloud sync
│   └── Adicionar: integração com .cex/memory/ (file backend existente)
├── [T3.2.2] Copiar LearningMachine com 6 stores:
│   ├── user_profile → mapeia para P10 entity_memory
│   ├── user_memory → mapeia para P10 learning_record
│   ├── entity_memory → mapeia para P10 entity_memory
│   ├── session_context → mapeia para P10 session_state
│   ├── learned_knowledge → mapeia para P01 knowledge_card (auto-gerado!)
│   └── decision_log → mapeia para GDP decision_manifest
├── [T3.2.3] Copiar Curator (memory maintenance)
│   └── Integrar com cex_memory_update.py (decay + prune)
├── [T3.2.4] Copiar LearningMode enum:
│   ├── ALWAYS → auto-extract após cada run
│   ├── AGENTIC → agente decide quando
│   ├── PROPOSE → propõe, user confirma (= GDP!)
│   └── HITL → reservado
├── [T3.2.5] Evoluir cex_memory.py:
│   ├── Modo 1 (default): File-based (retrocompat)
│   └── Modo 2: LLM-powered via MemoryManager
├── [T3.2.6] Evoluir cex_memory_select.py:
│   └── Usar MemoryManager.search() em vez de keyword matching
├── [T3.2.7] Testes: test_memory_manager.py, test_learning.py
└── [T3.2.8] Atualizar P10 kinds com refs para implementação SDK
```

### 3.3 Compression Manager (v9.3.0)

**Fonte Agno:** `libs/agno/agno/compression/manager.py` (**283 lines**)
**Destino CEX:** `cex_sdk/memory/compression.py`

```
TAREFAS:
├── [T3.3.1] Copiar CompressionManager (283 linhas)
│   ├── Manter: prompt de compressão, preserve facts
│   └── Adicionar: integração com cex_token_budget.py
├── [T3.3.2] Integrar com 8F pipeline:
│   ├── F3 INJECT: Se context > budget → compress tool outputs
│   └── F6 PRODUCE: Compress output se excede max_bytes do kind
├── [T3.3.3] Criar kind "compression_config" em P10
├── [T3.3.4] Testes: test_compression.py
└── [T3.3.5] Integrar com cex_crew_runner.py (compress entre steps)
```

### 3.4 Eval Framework (v9.4.0)

**Fonte Agno:** `libs/agno/agno/eval/` (7 files, 3.145L)
**Destino CEX:** `cex_sdk/eval/`

```
TAREFAS:
├── [T3.4.1] Copiar BaseEval ABC (pre_check + post_check)
├── [T3.4.2] Integrar com 8F:
│   ├── F1 CONSTRAIN: pre_check (input validation)
│   ├── F7 GOVERN: post_check (output validation)
│   └── Guardrails rodam ANTES de evals
├── [T3.4.3] Mapear para P07 kinds:
│   ├── unit_eval → BaseEval subclass
│   ├── smoke_eval → BaseEval com timeout < 30s
│   ├── llm_judge → EvalWithModel (usa LLM para avaliar)
│   └── benchmark → MetricEval (mede performance)
├── [T3.4.4] Evoluir cex_score.py para usar BaseEval:
│   └── score_artifact() se torna um PostCheckEval
├── [T3.4.5] Testes: test_eval_framework.py
└── [T3.4.6] Atualizar P07 kinds com refs para implementação SDK
```

### 3.5 Reasoning Steps (v9.5.0)

**Fonte Agno:** `libs/agno/agno/reasoning/` (13 files, 2.939L)
**Destino CEX:** `cex_sdk/reasoning/`

```
TAREFAS:
├── [T3.5.1] Copiar ReasoningStep + NextAction
│   ├── title, action, result, reasoning, next_action, confidence
│   └── NextAction: CONTINUE | VALIDATE | FINAL_ANSWER | RESET
├── [T3.5.2] Integrar com F4 REASON do 8F:
│   └── F4 agora produz List[ReasoningStep] tipado
├── [T3.5.3] Integrar com GDP:
│   └── Se confidence < threshold → trigger GDP (ask user)
├── [T3.5.4] Testes: test_reasoning.py
└── [T3.5.5] Registrar kind "reasoning_trace" em P03
```

### Entregável Fase 3
```
pyproject.toml:
  version = "9.5.0"
  # Sem deps novas — tudo usa cex_sdk/models que já está instalado

Novos arquivos: ~30 files em cex_sdk/
Testes novos: ~15
cex_crew_runner.py evoluído para usar Workflow primitives
cex_memory.py evoluído para usar MemoryManager
cex_score.py evoluído para usar BaseEval
```

---

## FASE 4: Integrations + Production (v10.0.0) — Semana 7-8

### Objetivo
MCP, tools essenciais, tracing, e a interface de produção.

### 4.1 MCP Bridge (v10.1.0)

**Fonte Agno:** `libs/agno/agno/tools/mcp/` (~800L)
**Destino CEX:** `cex_sdk/tools/mcp/`

```
TAREFAS:
├── [T4.1.1] Copiar MCPTools (client que expõe MCP como tools)
├── [T4.1.2] Copiar MultiMCPTools (múltiplos servers)
├── [T4.1.3] Integrar com P04 kind "mcp_server":
│   └── Cada mcp_server kind spec → instancia MCPTools automaticamente
├── [T4.1.4] Criar CLI: python -m cex_sdk.tools.mcp --url https://... --list
├── [T4.1.5] Testes: test_mcp.py (mock server)
└── [T4.1.6] Atualizar mcp-server-builder ISOs
```

### 4.2 Built-in Tools (v10.2.0)

**Fonte Agno:** `libs/agno/agno/tools/` (selecionados)
**Destino CEX:** `cex_sdk/tools/builtin/`

```
TAREFAS — absorver 10 tools mais universais:
├── [T4.2.1] file.py          — read/write/list files
├── [T4.2.2] shell.py         — execute shell commands (sandboxed)
├── [T4.2.3] python.py        — execute Python code
├── [T4.2.4] websearch.py     — DuckDuckGo/Tavily search
├── [T4.2.5] website.py       — scrape URL → text
├── [T4.2.6] sql.py           — query databases
├── [T4.2.7] github.py        — GitHub API operations
├── [T4.2.8] calculator.py    — math operations
├── [T4.2.9] csv_toolkit.py   — CSV operations
├── [T4.2.10] json toolkit    — JSON operations
├── [T4.2.11] Cada tool → registrar como kind "function_def" (P04)
├── [T4.2.12] Cada tool → gerar builder ISO minimal
└── [T4.2.13] Testes: test_builtin_tools.py
```

### 4.3 Tracing (v10.3.0)

**Fonte Agno:** `libs/agno/agno/tracing/` (4 files, 561L)
**Destino CEX:** `cex_sdk/tracing/`

```
TAREFAS:
├── [T4.3.1] Copiar schemas.py (trace data models)
├── [T4.3.2] Copiar exporter.py (OpenTelemetry-compatible)
├── [T4.3.3] Integrar com 8F pipeline:
│   └── Cada F1-F8 emite trace span com duração + tokens + status
├── [T4.3.4] Integrar com cex_feedback.py:
│   └── Traces alimentam quality tracking automaticamente
├── [T4.3.5] CLI: python -m cex_sdk.tracing --show-last --json
└── [T4.3.6] Testes: test_tracing.py
```

### 4.4 Session Persistence (v10.4.0)

**Fonte Agno:** `libs/agno/agno/session/` (5 files, 1.400L) + `libs/agno/agno/db/`
**Destino CEX:** `cex_sdk/session/`

```
TAREFAS:
├── [T4.4.1] Copiar session base (state management)
├── [T4.4.2] Copiar SQLite backend (zero-config persistence)
│   └── .cex/runtime/sessions.db
├── [T4.4.3] Integrar com CEX runtime:
│   ├── .cex/runtime/handoffs/ → session state
│   ├── .cex/runtime/signals/ → session events
│   └── .cex/runtime/pids/ → session tracking
├── [T4.4.4] Testes: test_session.py
└── [T4.4.5] Registrar kind "session_backend" em P10
```

### Entregável Fase 4 (v10.0.0 FINAL)
```
pyproject.toml:
  version = "10.0.0"
  [project.optional-dependencies]
  mcp = ["mcp"]
  search = ["duckduckgo-search"]
  tracing = ["opentelemetry-sdk"]

Novos arquivos: ~25 files
Testes novos: ~12
Total acumulado: cex_sdk/ com ~130 files, ~15K lines absorvidos
```

---

## Resumo de Versionamento

```
VERSION    NOME                    MÓDULOS                          LINES    KINDS NOVOS
───────    ────                    ───────                          ─────    ───────────
6.0.0      Governance (atual)     _tools/ existente                25.409   99
7.1.0      Model SDK              cex_sdk/models/                  +2.500   +1 (model_provider)
7.2.0      Toolkit Framework      cex_sdk/tools/{toolkit,fn}       +1.200   +1 (toolkit)
7.3.0      Guardrails             cex_sdk/guardrails/              +400     +1 (guardrail)
7.4.0      Structured Output      cex_sdk/models/structured.py     +300     —
8.1.0      Knowledge Readers      cex_sdk/knowledge/reader/        +2.000   —  (document_loader já existe)
8.2.0      Chunking               cex_sdk/knowledge/chunking/      +1.200   —  (chunk_strategy já existe)
8.3.0      Embeddings+VectorDB    cex_sdk/knowledge/embedder+vdb   +3.000   +2 (embedder_provider, vector_store)
8.4.0      Reranker               cex_sdk/knowledge/reranker/      +400     +1 (reranker)
9.1.0      Workflow Primitives    cex_sdk/workflow/                 +2.500   +1 (workflow_primitive)
9.2.0      Memory Manager         cex_sdk/memory/                  +2.000   —  (P10 kinds já existem)
9.3.0      Compression            cex_sdk/memory/compression.py    +300     +1 (compression_config)
9.4.0      Eval Framework         cex_sdk/eval/                    +800     —  (P07 kinds já existem)
9.5.0      Reasoning Steps        cex_sdk/reasoning/               +500     +1 (reasoning_trace)
10.1.0     MCP Bridge             cex_sdk/tools/mcp/               +500     —  (mcp_server já existe)
10.2.0     Built-in Tools (10)    cex_sdk/tools/builtin/           +2.000   —  (function_def já existe)
10.3.0     Tracing                cex_sdk/tracing/                 +400     +1 (trace_config)
10.4.0     Session Persistence    cex_sdk/session/                 +600     +1 (session_backend)
───────────────────────────────────────────────────────────────────────────────────────
TOTAL                                                              +20.600  +11 kinds (→ 110 total)
```

---

## Protocolo de Absorção por Arquivo

Cada arquivo copiado do Agno segue este checklist:

```markdown
## Checklist de Absorção: {filename}

- [ ] 1. COPY — copiar arquivo fonte do Agno
- [ ] 2. RENAME — namespace agno.* → cex_sdk.*
- [ ] 3. STRIP — remover refs a agno.cloud, agno.api, agno.client (SaaS)
- [ ] 4. ADAPT — ajustar imports para cex_sdk.* tree
- [ ] 5. DOCSTRING — adicionar docstring CEX padrão:
      ```python
      """
      cex_sdk.{module}.{file} — {description}
      
      Absorbed from: agno/{original_path}
      CEX version: {version}
      Pillar: {P0x}
      Kind: {kind_name}
      8F function: {CONSTRAIN|BECOME|INJECT|REASON|CALL|PRODUCE|GOVERN|COLLABORATE}
      """
      ```
- [ ] 6. TEST — criar test_{name}.py com pelo menos 3 testes
- [ ] 7. REGISTER — adicionar ao kinds_meta.json se novo kind
- [ ] 8. ISO — gerar builder ISO se é um novo archetype
- [ ] 9. COMPILE — rodar cex_compile.py para gerar .yaml
- [ ] 10. DOCTOR — rodar cex_doctor.py e confirmar 0 errors
```

---

## Matriz de Dependências entre Fases

```
Fase 1 (Foundation)
  ├── 1.1 Model SDK          ← independente
  ├── 1.2 Toolkit            ← independente  
  ├── 1.3 Guardrails         ← independente
  └── 1.4 Structured Output  ← depende de 1.1 (Model SDK)

Fase 2 (Knowledge)
  ├── 2.1 Readers            ← independente
  ├── 2.2 Chunking           ← independente
  ├── 2.3 Embeddings+VDB     ← depende de 1.1 (Model para embeddings)
  └── 2.4 Reranker           ← depende de 2.3 (VectorDB)

Fase 3 (Execution)
  ├── 3.1 Workflows          ← independente
  ├── 3.2 Memory Manager     ← depende de 1.1 (Model para extração)
  ├── 3.3 Compression        ← depende de 1.1 (Model para compressão)
  ├── 3.4 Eval Framework     ← independente
  └── 3.5 Reasoning Steps    ← depende de 1.4 (Structured Output)

Fase 4 (Integration)
  ├── 4.1 MCP                ← depende de 1.2 (Toolkit)
  ├── 4.2 Built-in Tools     ← depende de 1.2 (Toolkit)
  ├── 4.3 Tracing            ← independente
  └── 4.4 Session            ← independente
```

**Caminho crítico:** 1.1 → 1.4 → 2.3 → 3.2 (Model SDK é prerequisite de tudo)

---

## O Que NÃO Absorver (lista definitiva)

| Módulo Agno | Linhas | Razão para ignorar |
|-------------|--------|-------------------|
| `agno/os/` (AgentOS) | 3.000+ | FastAPI serving — CEX usa dispatch/spawn próprio |
| `agno/cloud/` | 2.000+ | SaaS proprietário — irrelevante |
| `agno/api/` | 1.500+ | Client do cloud deles |
| `agno/client/` | 500+ | Client do cloud deles |
| `agno/culture/` | 980 | Experimental — CEX brand system é 6x mais maduro |
| `agno/team/` | 19.881 | CEX nucleus system (N01-N07) é mais rico |
| `agno/agent/agent.py` | 1.714 | CEX builders (13 ISOs × 99 kinds) são superiores |
| `agno/skills/` | 1.225 | CEX já tem skill system via builders |
| `agno/integrations/` | varies | Coupling a frameworks externos — copiar sob demanda |
| 110+ tool wrappers | 35.000+ | Copiar apenas 10 essenciais, resto sob demanda |
| `agno/scheduler/` | 1.295 | Fase futura (v11+) — não é prioridade |

**Total ignorado:** ~65.000 linhas (23% do Agno) — SaaS coupling + redundância com CEX

---

## Governança do Processo

### Branching Strategy
```
main (v6.0.0)
  └── feature/cex-sdk-phase-1
       ├── feature/model-sdk        → merge → v7.1.0 tag
       ├── feature/toolkit          → merge → v7.2.0 tag
       ├── feature/guardrails       → merge → v7.3.0 tag
       └── feature/structured-out   → merge → v7.4.0 tag
  └── feature/cex-sdk-phase-2
       ├── feature/readers          → merge → v8.1.0 tag
       ...
```

### Quality Gates (por versão minor)
```
ANTES do merge:
  [ ] cex_doctor.py: 0 errors
  [ ] pytest: todos passam (novos + existentes)
  [ ] ruff check: 0 violations
  [ ] Changelog atualizado
  [ ] kinds_meta.json atualizado
  [ ] Builder ISOs gerados (se novo kind)

DEPOIS do merge:
  [ ] git tag v{X.Y.0}
  [ ] cex_compile.py --all
  [ ] cex_system_test.py: 54+ testes passam
```

### Licenciamento
```
Agno License: Mozilla Public License 2.0 (MPL-2.0)
→ Permite uso comercial, modificação, distribuição
→ Requer: manter copyright notices + declarar modificações
→ File-level copyleft (não viral para o projeto inteiro)

Ação: Cada arquivo absorvido mantém header:
  # Originally from agno (https://github.com/agno-agi/agno)
  # Licensed under MPL-2.0. Modified for CEX integration.
```

---

*Plano gerado em 2026-04-01 por N07_admin.*
*Próximo passo: Executar Fase 1 começando por T1.3 (Guardrails — 315 linhas, maior ROI/linha).*
