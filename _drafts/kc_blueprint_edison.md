# KC Meta-Template Blueprint — Edison (Builder Perspective)

**Author**: EDISON | **Version**: 1.0.0 | **Date**: 2026-03-25
**Basis**: 668 KCs analyzed, 757 produced, 7 golden distilled

## Design Principles

1. **Fields that get filled > fields that exist** — cut any field with >50% empty rate
2. **Body scales via variant** — domain_kc (7 sections) vs meta_kc (6 sections), not one-size-fits-all
3. **Validation runs without humans** — every gate is a machine-checkable rule
4. **Brain-searchable first** — title + tldr are the primary BM25 ranking signals

---

## Frontmatter Spec (YAML)

```yaml
# --- REQUIRED (13 fields) — must be non-empty or KC is INVALID ---
id: p01_kc_{{topic_slug}}          # MUST == filename stem
type: knowledge_card
lp: P01
title: "{{5-100 chars, descriptive}}"
version: "{{semver}}"
created: "{{ISO date}}"
updated: "{{ISO date}}"
author: "{{who PRODUCED content}}"  # P1: producer, NOT router
domain: "{{domain_name}}"
quality: null                       # P2: null until validated externally
tags: [tag1, tag2, tag3]            # list of strings, NEVER string
tldr: "{{1 dense sentence, <160 chars}}"
when_to_use: "{{retrieval condition}}"

# --- CEX EXTENDED (6 fields) — improve Brain recall ~30% ---
keywords: [kw1, kw2, kw3]
long_tails:
  - "{{natural language question 1}}"
  - "{{natural language question 2}}"
axioms:
  - "{{SEMPRE/NUNCA imperative rule}}"
linked_artifacts:                   # P3: min 1 link OR explicit null
  primary: "{{artifact_id OR null}}"
  related: "{{artifact_id OR null}}"
density_score: "{{0.80-1.00}}"
data_source: "{{url OR experiment OR null}}"  # P4: facts need source
```

### Rules that solve the 6 problems

| # | Problem | Rule in template |
|---|---------|-----------------|
| P1 | author ambiguous | `author` = who PRODUCED content (satellite/human), not who routed |
| P2 | quality self-assigned | `quality: null` at creation; set ONLY by external validator post-generation |
| P3 | linked_kcs empty | `linked_artifacts.primary` required; explicit `null` if truly standalone |
| P4 | facts without source | `data_source` field required; `null` only for axiomatic/self-evident facts |
| P5 | scoring no method | Quality = avg(density, completeness, accuracy) — 3 sub-scores, reproducible |
| P6 | main section too short | Body variant enforces: largest section >= 30% of total body bytes |

---

## Body Variants

### Variant A: domain_kc (business/strategy)
```markdown
## Quick Reference        # yaml block: metrics, scope, criticality
## Conceitos Chave        # min 3 bullets, max 80 chars each
## Fases                  # numbered steps with outcomes
## Regras de Ouro         # SEMPRE/NUNCA imperatives
## Flow                   # ASCII diagram (required)
## Comparativo            # table comparing options (>= 2 rows)
```

### Variant B: meta_kc (technical/API/config)
```markdown
## Executive Summary      # 1-2 sentences with specific data
## Spec Table             # exact values: prices, limits, configs
## Patterns               # what works, with evidence
## Anti-Patterns          # what fails, with reason
## Application            # current state + next action
## References             # URLs + related KCs
```

### Code Snippets (either variant)
```markdown
## Code
<!-- source_file: path/to/file.py | lang: python | purpose: show X -->
\```python
def example():
    return "real code, not pseudocode"
\```
```
Rule: every code block needs `source_file`, `lang`, `purpose` in HTML comment above it.

---

## Quality Gates (automated)

```yaml
gates:
  structural:
    - id == filename_stem
    - tags is list[str], not str
    - len(body) >= 200 bytes
    - len(total) <= 5120 bytes
    - each bullet <= 80 chars
    - sections with < 3 lines: FAIL
  density:
    - density_score >= 0.80
    - no filler phrases: "This document", "In summary", "As mentioned"
    - no duplicate sentences (jaccard > 0.8 = duplicate)
  completeness:
    - all 13 required frontmatter fields non-empty (except quality=null)
    - body has >= 4 sections from chosen variant
    - largest section >= 30% of body bytes (P6)
  scoring:  # P5: reproducible method
    quality = round(mean(density_sub, completeness_sub, accuracy_sub), 1)
    # density_sub: 10 * density_score
    # completeness_sub: 10 * (filled_sections / total_sections)
    # accuracy_sub: manual or LLM-verified (0-10)
```

---

## Minimal Valid Example (meta_kc variant)

```yaml
---
id: p01_kc_prompt_caching_basics
type: knowledge_card
lp: P01
title: "Prompt Caching Reduces LLM API Cost by 90%"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: EDISON
domain: llm_engineering
quality: null
tags: [prompt-caching, cost-optimization, anthropic]
tldr: "Prompt caching reutiliza prefixos pre-processados, cortando custo em 90% e latencia em 85% para contextos > 1024 tokens"
when_to_use: "Sistema LLM repete contexto longo entre chamadas"
keywords: [prompt-caching, cache-control, token-cost]
long_tails:
  - "Como configurar prompt caching na API Anthropic"
axioms:
  - "SEMPRE coloque conteudo estatico ANTES do dinamico no prompt"
linked_artifacts:
  primary: p02_agent_llm_application_specialist
  related: null
density_score: 0.91
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
---
```

## Anti-Example (what NOT to produce)

```yaml
---
id: kc_caching  # FAIL: missing p01_kc_ prefix, won't match filename
type: knowledge_card
lp: P01
title: "Caching"  # FAIL: < 5 chars, not descriptive
author: STELLA  # FAIL: STELLA routed, didn't produce
quality: 9.5  # FAIL: self-assigned at creation
tags: "caching, api, llm"  # FAIL: string, not list
tldr: "This document describes caching."  # FAIL: filler phrase
# missing: when_to_use, keywords, linked_artifacts, data_source
---

# Caching

## TL;DR
This document describes how caching works.  # FAIL: repeats tldr

## Deep Dive
Caching is important. It helps save money.  # FAIL: no specific data
# FAIL: body < 200 bytes, largest section < 30%, no tables/code
```

**Why it fails**: cookie-cutter structure (TL;DR/Deep Dive), no density, self-scored, author is router not producer, tags as string, no source for claims.
