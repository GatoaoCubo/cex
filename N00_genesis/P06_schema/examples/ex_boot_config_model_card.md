---
id: p06_bp_model_card
kind: artifact_blueprint
pillar: P06
llm_function: CONSTRAIN
title: "Blueprint: model_card — Meta-Template para Producao de Model Cards"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
quality: 9.1
tags: [blueprint, model-card, meta-template, production-mold, llm-spec]
tldr: "Meta-template que define COMO gerar model_cards validos — frontmatter layered, capabilities como booleans, pricing normalizado, freshness 90d"
when_to_use: "Antes de gerar qualquer model_card — este blueprint eh o molde"
synthesis: "research_agent (standards survey, 12 standards) + knowledge_agent-GEMINI (10-provider comparative) + operations_agent-CODEX (code patterns, 7 frameworks) + builder_agent (CEX analysis + boundary + quality gates)"
related:
  - bld_schema_model_card
  - bld_output_template_model_card
  - bld_config_model_card
  - model-provider-builder
  - model-card-builder
  - p03_sp_model_card_builder
  - bld_knowledge_card_model_card
  - p01_kc_model_card
  - bld_architecture_model_card
  - bld_config_model_provider
---

# Blueprint: model_card

## Boundary

model_card eh especificacao tecnica de um LLM: capacidades, custos, limites, status.
model_card NAO eh: boot_config (inicializacao), agent (identidade), persona (estilo), router (roteamento), benchmark (avaliacao).
Se responde "o que este LLM PODE fazer e quanto CUSTA?" → model_card.
Se responde "como INICIALIZAR este LLM?" → boot_config (P02).
Se responde "como este LLM se COMPORTA?" → persona (P02).

Source: Mitchell 2019 define model card como "documento que acompanha modelos treinados, provendo benchmarks, intended use e limitacoes". CEX restringe ao escopo operacional (capacidade + custo) e delega safety/alignment para secao opcional.

## Format

Arquivo `.md` com frontmatter YAML + body Markdown.
Motivo: brain search so indexa .md; LLMs geram MD melhor que YAML; frontmatter validavel por schema.
Mesmo formato de KC (P01) mas namespace P02 — model_card eh artefato de identidade, nao conhecimento generico.

## Naming

`p02_mc_{{provider}}_{{model_slug}}.md` — id == filename stem.
provider: lowercase (anthropic, openai, google, meta, mistral, cohere, deepseek).
model_slug: snake_case do nome canonico sem provider prefix (ex: `opus_4`, `gpt_4o`, `gemini_2_5_pro`).

Exemplos:
- `p02_mc_anthropic_opus_4.md`
- `p02_mc_openai_gpt_4o.md`
- `p02_mc_google_gemini_2_5_pro.md`
- `p02_mc_meta_llama_3_1_405b.md`

## Frontmatter

Schema layered: Identity > Model Spec > Capabilities > Economics > Search.
Source: operations_agent-CODEX recomenda 4 blocos separados; este frontmatter achata em YAML mas preserva a separacao logica via comentarios.

```yaml
---
# CEX IDENTITY (7) — REQUIRED — padrao CEX, mesmo de KC
id: p02_mc_{{provider}}_{{model_slug}}  # == filename stem
kind: model_card
pillar: P02
version: "{{semver}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{quem PRODUZIU}}"             # quem escreveu, NAO quem roteou

# MODEL IDENTITY (6) — REQUIRED
# Sources: Mitchell 2019 (model name, developers), HF (model_name, pipeline_tag),
#          LiteLLM (litellm_provider, mode), Anthropic SDK (id, display_name, created_at)
model_name: "{{id oficial do provider}}"         # ex: claude-opus-4-6520, gpt-4o-2024-08-06
provider: "{{anthropic|openai|google|meta|mistral|cohere|deepseek|other}}"
model_type: "{{text-generation|embedding|image-generation|audio|multimodal}}"  # HF pipeline_tag
status: "{{active|deprecated|sunset}}"           # CEX-extension: lifecycle tracking (justified by 90d freshness)
release_date: "{{YYYY-MM-DD or null}}"           # HF, Meta, Google DeepMind (8/10 providers)
knowledge_cutoff: "{{YYYY-MM or null}}"          # Mitchell (training_data), 6/10 providers

# CAPABILITIES (5) — REQUIRED
# Sources: LiteLLM (supports_* booleans), Anthropic SDK (ModelCapabilities),
#          LangChain (ModelProfile), knowledge_agent-GEMINI comparative (10 providers)
context_window: {{int}}                          # max input tokens — universal (10/10 providers)
max_output: {{int}}                              # max output tokens — 7/10 providers
modalities:
  text_input: {{bool}}
  text_output: {{bool}}
  image_input: {{bool}}                          # vision — 5/10 providers
  audio_input: {{bool}}                          # 3/10 providers
  pdf_input: {{bool}}                            # Anthropic SDK: pdf_input
features:
  tool_calling: {{bool}}                         # LiteLLM: supports_function_calling
  structured_output: {{bool}}                    # LiteLLM: supports_response_schema
  reasoning: {{bool}}                            # LiteLLM: supports_reasoning (extended thinking)
  prompt_caching: {{bool}}                       # LiteLLM: supports_prompt_caching
  code_execution: {{bool}}                       # Anthropic SDK: code_execution
  web_search: {{bool}}                           # LiteLLM: supports_web_search
  fine_tunable: {{bool}}                         # Meta, OpenAI (CEX-extension for routing)
  batch_api: {{bool}}                            # Anthropic SDK: batch

# ECONOMICS (1 object) — REQUIRED for commercial, null for open-weight
# Sources: LiteLLM (input_cost_per_token, output_cost_per_token),
#          OpenAI/Anthropic/Google pricing pages
pricing:
  input: {{float or null}}                       # USD per 1M tokens
  output: {{float or null}}                      # USD per 1M tokens
  cache_read: {{float or null}}                  # Anthropic: 0.1x base
  cache_write: {{float or null}}                 # Anthropic: 1.25x base
  unit: per_1M_tokens                            # ALWAYS this unit — normaliza comparacao

# SEARCH/DISCOVERY (7) — melhora recall ~30%
# Sources: CEX KC blueprint (padrao), brain search BM25
domain: model_selection
quality: null                                    # NUNCA auto-atribuir — validacao externa
tags: [model-card, {{provider}}, {{model_family}}, {{key_capability}}]
tldr: "{{1 frase com dados: modelo, provider, contexto, preco, destaque}}"
when_to_use: "{{condicao de decisao: roteamento, selecao, comparacao}}"
keywords: [{{provider}}, {{model_name}}, {{key terms}}]
linked_artifacts:
  primary: "{{boot_config que usa este card, ou null}}"
  related: ["{{outros model_cards do mesmo provider}}"]
data_source: "{{URL da pricing page ou docs do provider}}"
---
```

## Body — Variante A: spec_card (modelo individual)

Para documentar UM modelo especifico com specs completos.

```markdown
## Boundary
model_card EH: spec tecnica de LLM (capacidades, custos, limites).
model_card NAO EH: boot_config (inicializacao), agent (identidade), benchmark (avaliacao).

## Specifications
| Spec | Value | Source |
|------|-------|--------|
Tabela com: model, provider, context, max_output, release, cutoff, architecture.
Coluna Source: URL ou doc do provider para cada dado.

## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
Tabela com cada feature como boolean explicito.
Nao usar prosa — booleans sao machine-readable (LiteLLM pattern).

## When to Use
| Scenario | Use This Model? | Why / Alternative |
|----------|-----------------|-------------------|
>= 3 scenarios com alternativas e razao de custo.

## Rate Limits
| Tier | RPM | TPM | RPD |
|------|-----|-----|-----|
Limites por tier (se disponivel publicamente). Omitir se provider nao publica.

## References
- source: {{provider docs URL}}
- pricing: {{pricing page URL}}
- related: {{outros model_cards}}
```

## Body — Variante B: comparison_card (comparativo entre modelos)

Para comparar 2+ modelos do mesmo provider ou across providers.

```markdown
## Boundary
comparison_card EH: tabela comparativa de specs entre modelos.
comparison_card NAO EH: benchmark (avaliacao de performance), router (logica de decisao).

## Quick Reference
scope: {{provider ou categoria}} | models: {{N}} | focus: {{preco|capacidade|modalidade}}

## Comparison Matrix
| Spec | Model A | Model B | Model C |
|------|---------|---------|---------|
Tabela comparativa: context, max_output, pricing, features.
>= 5 specs, >= 2 modelos.

## Capability Diff
| Feature | Model A | Model B | Model C |
|---------|---------|---------|---------|
Booleans por modelo. Delta visual entre modelos.

## Decision Guide
| Use Case | Best Choice | Why |
|----------|-------------|-----|
>= 3 use cases com recomendacao e justificativa de custo.

## References
- source: {{URLs por modelo}}
```

## Quality Gates (automatizaveis)

```yaml
structural:
  - id starts with "p02_mc_"
  - id == filename_stem
  - type == "model_card"
  - lp == "P02"
  - model_name is not empty
  - provider in [anthropic, openai, google, meta, mistral, cohere, deepseek, other]
  - context_window > 0 (integer)
  - max_output > 0 (integer)
  - status in [active, deprecated, sunset]
  - modalities has >= 2 boolean fields
  - features has >= 3 boolean fields
  - tags is list, not string
  - quality == null (never self-score)
  - body_bytes >= 300 and <= 3072

density:
  - sem filler: "This document", "In summary", "As mentioned"
  - sem frases duplicadas (jaccard > 0.8)
  - pricing tem numeros concretos (nao "varies" ou "contact sales")
  - context_window eh numero exato (nao "up to" ou "approximately")
  - density_score >= 0.85 (mais alto que KC por ser spec pura)

completeness:
  - 7 CEX identity fields preenchidos
  - 6 model identity fields preenchidos (null OK para release_date, knowledge_cutoff)
  - modalities + features objects presentes
  - pricing object presente (null values OK para open-weight)
  - body >= 4 secoes da variante escolhida
  - Boundary section presente e nao-vazio
  - References >= 1 source link

accuracy:
  - pricing matches provider published pricing page
  - context_window matches provider docs
  - features verified against API docs or SDK
  - knowledge_cutoff verified against provider announcement
  - status reflects current provider lifecycle

freshness:
  # CEX-extension: model_cards degradam mais rapido que KCs
  # Source: builder_agent analysis — pricing/features mudam trimestralmente
  - updated date within 90 days
  - if status == "deprecated": linked_artifacts must point to replacement
  - if provider announces new version: card should update within 7 days
  - stale cards (> 90 days) flagged for review

scoring:
  quality = mean(structural_sub, density_sub, completeness_sub, accuracy_sub)
  # structural_sub = pass/fail (0 or 10)
  # density_sub = 10 * density_score
  # completeness_sub = 10 * (filled_fields / total_fields)
  # accuracy_sub = LLM-verified or manual (0-10)
  # threshold: >= 8.0 for pool, >= 9.5 for golden
```

## Cross-References (grafo de conhecimento)

```yaml
linked_artifacts:
  primary: "{{boot_config que consome este card}}"
  related: ["{{model_cards do mesmo provider}}", "{{fallback_chain que lista este modelo}}"]
# Relacoes validas: extends, depends_on, replaces, compares_to
```

Posicao no boot flow (camada 0 — infraestrutura):
```
[boot_config + model_card]   <- infra pre-requisito (camada 0)
          |
    [system_prompt]           <- papel persistente (camada 1)
          |
    [mental_model]            <- mapa cognitivo (camada 2)
          |
      [persona]               <- estilo comunicacao (camada 3)
          |
       [agent]                <- identidade completa (camada 4)
```

model_card eh dependencia de: boot_config (selecao), router (custo/capacidade), fallback_chain (priorizacao), agent_package (deploy bundle). Eh o unico tipo P02 puramente descritivo.

## Exemplo Minimo Valido

```yaml
---
id: p02_mc_anthropic_sonnet_4
kind: model_card
pillar: P02
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
model_name: claude-sonnet-4-6
provider: anthropic
model_type: text-generation
status: active
release_date: 2025-05-14
knowledge_cutoff: 2025-04
context_window: 200000
max_output: 16000
modalities:
  text_input: true
  text_output: true
  image_input: true
  audio_input: false
  pdf_input: true
features:
  tool_calling: true
  structured_output: true
  reasoning: true
  prompt_caching: true
  code_execution: true
  web_search: false
  fine_tunable: false
  batch_api: true
pricing:
  input: 3.00
  output: 15.00
  cache_read: 0.30
  cache_write: 3.75
  unit: per_1M_tokens
domain: model_selection
quality: 8.9
tags: [model-card, anthropic, claude-4, sonnet, balanced]
tldr: "Claude Sonnet 4 — Anthropic, 200K context, $3/$15 per 1M tokens, melhor custo-beneficio para analise e pesquisa"
when_to_use: "Tarefas de analise, pesquisa, marketing onde opus eh overkill e haiku insuficiente"
keywords: [anthropic, claude-sonnet-4, sonnet, balanced]
linked_artifacts:
  primary: null
  related: [p02_mc_anthropic_opus_4, p02_mc_anthropic_haiku_4]
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
---

## Boundary
model_card EH: spec tecnica do Claude Sonnet 4 (capacidades, custos, limites).
model_card NAO EH: boot_config, agent, benchmark.

## Specifications
| Spec | Value | Source |
|------|-------|--------|
| Model | claude-sonnet-4-6 | Anthropic docs |
| Provider | Anthropic | — |
| Context Window | 200K tokens | Anthropic docs |
| Max Output | 16K tokens | Anthropic docs |
| Architecture | Transformer (dense) | Anthropic system card |
| Knowledge Cutoff | Apr 2025 | Anthropic docs |

## Capabilities
| Capability | Supported | Notes |
|------------|-----------|-------|
| Tool Calling | yes | Parallel tool use supported |
| Structured Output | yes | JSON mode, schema enforcement |
| Extended Thinking | yes | Budget-controlled reasoning |
| Prompt Caching | yes | 0.1x read cost, 1.25x write |
| Vision | yes | Image + PDF input |
| Code Execution | yes | Sandbox execution |
| Web Search | no | — |
| Fine-tuning | no | Not available via API |
| Batch API | yes | 50% discount, 24h SLA |

## When to Use
| Scenario | Use Sonnet? | Why / Alternative |
|----------|-------------|-------------------|
| Research and analysis | YES | Best cost/quality for analytical tasks |
| Marketing copy generation | YES | Strong creative at 20% of opus cost |
| Complex multi-file refactoring | NO | Use opus — reasoning depth required |
| Simple formatting or classification | NO | Use haiku — 6x cheaper ($0.25/$1.25) |

## References
- source: https://docs.anthropic.com/en/docs/about-claude/models
- pricing: https://docs.anthropic.com/en/docs/about-claude/pricing
- related: p02_mc_anthropic_opus_4
```

## Anti-Exemplo (o que NAO produzir)

```yaml
---
id: mc_gpt4                    # FAIL: sem prefixo p02_mc_, sem provider
kind: model_card
model_name: GPT-4              # FAIL: nome informal, nao eh id oficial
provider: OpenAI               # FAIL: deve ser lowercase
context_window: "128K"         # FAIL: string, nao integer
max_output: "a lot"            # FAIL: vago, sem numero
quality: 9.5                   # FAIL: auto-atribuido
tags: "gpt, openai, chat"     # FAIL: string, nao lista
features: "supports tools"     # FAIL: prosa, nao booleans
pricing: "see website"         # FAIL: sem dados concretos
---
## Overview
This document describes GPT-4.    # FAIL: filler
It is a powerful model.            # FAIL: sem dados, sem fonte
## Pricing
Pricing varies by usage.          # FAIL: sem numeros
```

**Falhas**: id sem padrao, quality auto-atribuido, features como prosa (nao booleans), pricing sem dados, filler text, sem Boundary, sem References, sem Source column, sem data_source.

## TL;DR

model_card = spec tecnica de LLM para decisoes de roteamento e custo.
Schema layered: Identity (7 CEX + 6 model) > Capabilities (modalities + features como booleans) > Economics (pricing normalizado per 1M tokens) > Search (7 discovery fields).
Freshness gate 90 dias — model_cards degradam mais rapido que KCs.
CEX normaliza Mitchell 2019 + HuggingFace + LiteLLM. Nao inventa campos.

## Deep Dive

| Source | Tipo | Contribuicao para este BP | URL |
|--------|------|--------------------------|-----|
| Mitchell et al. 2019 | Paper fundacional | Origem do conceito: model name, developers, intended use, limitations, ethical considerations | https://arxiv.org/abs/1810.03993 |
| Gebru et al. 2021 | Paper adjacent | Datasheets for Datasets — mesma filosofia de documentacao | https://arxiv.org/abs/1803.09010 |
| HuggingFace Model Cards | Spec pratica | Standard mais adotado: YAML frontmatter + Markdown body, pipeline_tag, model-index, eval_results | https://huggingface.co/docs/hub/en/model-cards |
| HF Model Card Guidebook | Best practices | Ozoani, Gerchick, Mitchell — guia pratico mais completo | https://huggingface.co/docs/hub/en/model-card-guidebook |
| LiteLLM Registry | Operational registry | 2593 modelos, capability booleans (supports_*), pricing per token, routing metadata | https://github.com/BerriAI/litellm |
| Google Model Card Toolkit | JSON schema | Proto-based schema, HTML rendering, Vertex AI pipeline integration | https://www.tensorflow.org/responsible_ai/model_card_toolkit/guide |
| Anthropic SDK ModelInfo | API schema | ModelCapabilities com booleans tipados, context limits, display_name | https://github.com/anthropics/anthropic-sdk-python |
| LangChain ModelProfile | Capability abstraction | Modality booleans (text/image/audio/video), tool_calling, structured_output | https://github.com/langchain-ai/langchain |
| AI Transparency Atlas 2024 | Fragmentacao survey | 947 nomes de secao unicos — justifica necessidade de normalizacao | https://arxiv.org/html/2512.12443 |
| Blueprints of Trust 2025 | Schema consenso | Propoe 20-30 campos consensuais para system cards | https://arxiv.org/pdf/2509.20394 |
| EU AI Act GPAI Code 2025 | Regulatorio | Compliance requirements para modelos > 10^25 FLOPs | https://euperspectives.eu/2025/07 |

### CEX-Extensions (campos sem precedente industrial direto)

| Campo | Justificativa | Alternativa industrial mais proxima |
|-------|--------------|-------------------------------------|
| `status` (active/deprecated/sunset) | Freshness gate 90d — models deprecam, cards ficam stale | HF `new_version` pointer, LiteLLM `deprecation_date` |
| `fine_tunable` | Decisao de roteamento: fine-tune vs prompt engineering | Meta finetuning_recipe (narrativo, nao boolean) |
| `pricing.cache_read/write` | Prompt caching muda economia 10x — essencial para roteamento | LiteLLM nao separa cache pricing |
| `freshness gate (90d)` | model_cards degradam 4x mais rapido que KCs | Nenhum standard define freshness policy |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_card]] | related | 0.52 |
| [[bld_output_template_model_card]] | upstream | 0.51 |
| [[bld_config_model_card]] | downstream | 0.29 |
| [[model-provider-builder]] | upstream | 0.29 |
| [[model-card-builder]] | upstream | 0.27 |
| [[p03_sp_model_card_builder]] | upstream | 0.26 |
| [[bld_knowledge_card_model_card]] | upstream | 0.26 |
| [[p01_kc_model_card]] | upstream | 0.26 |
| [[bld_architecture_model_card]] | downstream | 0.26 |
| [[bld_config_model_provider]] | downstream | 0.25 |
