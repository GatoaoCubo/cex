---
id: p06_bp_knowledge_card
kind: artifact_blueprint
8f: F4_reason
pillar: P06
llm_function: CONSTRAIN
title: "Blueprint: knowledge_card — Meta-Template para Producao de KCs"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: orchestrator
quality: 9.1
tags: [blueprint, knowledge-card, meta-template, production-mold]
tldr: "Meta-template que define COMO gerar KCs validos — frontmatter, body, quality gates, naming"
when_to_use: "Antes de gerar qualquer KC — este blueprint eh o molde"
synthesis: "Edison (builder) + Gemini (knowledge arch) + orchestrator (boundary/pragmatic)"
related:
  - bld_examples_knowledge_card
  - bld_schema_knowledge_card
  - bld_examples_response_format
  - p06_bp_model_card
  - p01_kc_knowledge_best_practices
  - bld_knowledge_card_knowledge_card
  - bld_schema_integration_guide
  - bld_output_template_kind
  - bld_output_template_knowledge_card
  - bld_examples_validation_schema
---

# Blueprint: knowledge_card

## Boundary

KC eh conhecimento destilado, estatico, versionado.
KC NAO eh: instrucao (P03), configuracao (P09), template (P06), teste (P07).
Se tem `def/class` executavel → skill (P04). Se tem `faça X` → instruction (P03).

## Format

Arquivo `.md` com frontmatter YAML + body Markdown.
Motivo: brain search so indexa .md; LLMs geram MD melhor que YAML; frontmatter validavel por schema.

## Naming

`p01_kc_{{topic_slug}}.md` — id == filename stem.
topic_slug: snake_case, sem agent_group prefix, descritivo.

## Frontmatter

```yaml
---
# REQUIRED (13) — vazio = KC INVALIDO
id: p01_kc_{{topic_slug}}       # == filename stem
kind: knowledge_card
pillar: P01
title: "{{5-100 chars}}"        # BM25 primary signal
version: "{{semver}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{quem PRODUZIU}}"     # quem escreveu, NAO quem roteou
domain: "{{domain}}"
quality: null                    # null ate validacao externa
tags: [t1, t2, t3]              # lista, NUNCA string; cada tag = pesquisavel
tldr: "{{1 frase, <160 chars}}" # search snippet — funciona sozinho
when_to_use: "{{condicao}}"     # outra LLM le isto pra decidir se carrega

# EXTENDED (6) — melhora recall ~30%
keywords: [kw1, kw2]
long_tails: ["{{pergunta natural}}"]
axioms: ["{{SEMPRE/NUNCA regra}}"]
linked_artifacts:
  primary: "{{id ou null}}"      # min 1 link ou explicitar null
  related: ["{{id}}"]
density_score: null              # preenchido pelo validador
data_source: "{{url ou null}}"   # facts precisam fonte
---
```

## Body — Variante A: meta_kc (tecnico/API/spec)

```markdown
## Summary
1-2 frases com dados especificos. Nunca "This document describes...".

## Spec
| Campo | Valor | Nota |
Tabela de specs exatos: precos, limites, configs.

## Patterns
| Trigger | Action |
O que funciona, com evidencia.

## Anti-Patterns
- Bullet imperativo: o que falha e por que.

## Code
<!-- source: path/file.py | lang: python | purpose: X -->
```python
def real_code(): ...
```

## References
- related: {{kc_id}}
- source: {{url}}
```

## Body — Variante B: domain_kc (negocio/estrategia)

```markdown
## Quick Reference
topic: X | scope: Y | criticality: high

## Conceitos Chave
- Min 3 bullets, max 80 chars cada.

## Fases
1. Fase com outcome esperado.

## Regras de Ouro
- SEMPRE/NUNCA imperativo.

## Comparativo
| Opcao A | Opcao B |
Tabela comparando alternativas (>= 2 linhas).

## Flow
Diagrama ASCII do fluxo.
```

## Quality Gates (automatizaveis)

```yaml
structural:
  - id == filename_stem
  - tags is list, not string
  - 200 <= body_bytes <= 5120
  - bullets <= 80 chars
  - sections com < 3 linhas: FAIL

density:
  - sem filler: "This document", "In summary", "As mentioned"
  - sem frases duplicadas (jaccard > 0.8)
  - density_score >= 0.80

completeness:
  - 13 required fields preenchidos (quality=null OK)
  - body >= 4 secoes da variante escolhida
  - maior secao >= 30% do body

scoring:
  quality = mean(density_sub, completeness_sub, accuracy_sub)
  # density_sub = 10 * density_score
  # completeness_sub = 10 * (filled_sections / total_sections)
  # accuracy_sub = LLM-verified ou manual (0-10)
```

## Cross-References (grafo de conhecimento)

```yaml
linked_artifacts:
  primary: "{{kc que este ESTENDE ou DEPENDE}}"
  related: ["{{kcs no mesmo dominio}}"]
# Relacoes validas: extends, depends_on, contradicts, replaces
```

KC → embedding → vector index → retrieval → LLM context.
Cada KC eh um no no grafo. linked_artifacts sao as arestas.
title + tldr sao os campos primarios de BM25 ranking.
## headers definem os chunks de embedding.

## Exemplo Minimo Valido

```yaml
---
id: p01_kc_prompt_caching_basics
kind: knowledge_card
pillar: P01
title: "Prompt Caching Reduces LLM Cost by 90%"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: llm_engineering
quality: 8.9
tags: [prompt-caching, cost-optimization, anthropic]
tldr: "Cache reutiliza prefixos, cortando custo 90% e latencia 85% para contextos > 1024 tokens"
when_to_use: "Sistema LLM repete contexto longo entre chamadas"
keywords: [prompt-caching, cache-control]
long_tails: ["Como configurar prompt caching na Anthropic"]
axioms: ["SEMPRE coloque conteudo estatico ANTES do dinamico"]
linked_artifacts:
  primary: p02_agent_llm_specialist
  related: [p01_kc_rag_fundamentals]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/prompt-caching"
---

## Summary
Prompt caching reutiliza prefixos pre-processados entre chamadas LLM. Reduz custo em 90% (Anthropic: read 0.1x) e latencia em 85% para prefixos >= 1024 tokens.

## Spec
| Provider | Min Tokens | Write Cost | Read Cost | TTL |
|----------|-----------|------------|-----------|-----|
| Anthropic | 1024 | 1.25x | 0.1x | 5 min |
| OpenAI | 1024 | 1.0x | 0.5x | 5-60 min |

## Patterns
| Trigger | Action |
|---------|--------|
| >50% contexto estatico | Ativar cache no prefixo |
| Hit rate < 80% | Aumentar bloco cacheavel |

## Anti-Patterns
- Cachear contexto que muda a cada request (invalida e AUMENTA custo)
- Blocos pequenos demais (overhead por bloco > economia)

## References
- source: https://docs.anthropic.com/en/docs/prompt-caching
- related: p01_kc_rag_fundamentals
```

## Anti-Exemplo (o que NAO produzir)

```yaml
---
id: kc_caching           # FAIL: sem prefixo p01_kc_, != filename
title: "Caching"          # FAIL: < 5 chars
author: orchestrator      # FAIL: routed, did not produce
quality: 9.5              # FAIL: auto-atribuido
tags: "caching, api"      # FAIL: string, nao lista
tldr: "This document describes caching."  # FAIL: filler
---
## TL;DR
This document describes how caching works.  # FAIL: repete tldr
## Deep Dive
Caching is important.  # FAIL: sem dados, sem fonte, < 200B
```

**Falha**: cookie-cutter, sem density, self-scored, author errado, sem source.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_knowledge_card]] | downstream | 0.26 |
| [[bld_schema_knowledge_card]] | related | 0.25 |
| [[bld_examples_response_format]] | downstream | 0.24 |
| [[p06_bp_model_card]] | sibling | 0.24 |
| [[p01_kc_knowledge_best_practices]] | upstream | 0.23 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.23 |
| [[bld_schema_integration_guide]] | related | 0.22 |
| [[bld_output_template_kind]] | upstream | 0.21 |
| [[bld_output_template_knowledge_card]] | upstream | 0.21 |
| [[bld_examples_validation_schema]] | downstream | 0.21 |
