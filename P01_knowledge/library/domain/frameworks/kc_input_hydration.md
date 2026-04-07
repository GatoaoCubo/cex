---
id: p01_kc_input_hydration
kind: knowledge_card
type: domain
pillar: P01
title: "Input Hydration Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 9.0
tags: [framework, architecture, llm]
tldr: "Raw user input is incomplete. Hydrate with brand, memory, KC context before any nucleus processes it."
keywords: [hydration, enrichment, context-injection, preprocessing]
density_score: 0.92
updated: "2026-04-07"
---

# Input Hydration Framework

## Hydration Layers
| Layer | Source | What it Adds |
|-------|--------|-------------|
| 1. Brand | brand_config.yaml | Identity, voice, colors |
| 2. Memory | builder memory files | Past learnings, preferences |
| 3. Knowledge | P01 KCs | Domain expertise |
| 4. Decisions | decision_manifest.yaml | User choices |
| 5. Examples | compiled/ artifacts | Reference patterns |

## CEX Implementation
wf_auto_hydrate.md chains all 5 layers.
compose_prompt() in cex_crew_runner.py assembles the hydrated prompt.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_input_hydration`
- **Tags**: [framework, architecture, llm]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_input_hydration`
- **Tags**: [framework, architecture, llm]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Input Hydration Framework"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Input Hydration Framework" --top 5
```
