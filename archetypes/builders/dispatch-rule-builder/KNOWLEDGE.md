---
pillar: P01
llm_function: INJECT
purpose: Operational knowledge and patterns for dispatch_rule production
sources: P12 schema + STELLA_RULES.md routing table + codexa-core SUBAGENT_CATALOG.md
---

# Domain Knowledge: dispatch_rule

## Core Concept
`dispatch_rule` is a routing policy record in P12 orchestration.
It answers a narrow authoring question:
"Which satellite should receive tasks matching these keywords, at what priority,
with what fallback if the primary is unavailable?"

Rules are decisions, not instructions.
They are consumed by orchestrators, spawn scripts, and routing engines.

## Satellite Routing Reference
| Satellite | Domain Keywords | Default Model |
|-----------|----------------|---------------|
| shaka | pesquisar, mercado, concorrente, scrape, analise, research, market | sonnet |
| lily | anuncio, marketing, copy, titulo, vender, ads, campaign | sonnet |
| edison | criar, build, codigo, componente, hook, template, implementar | opus |
| pytha | conhecimento, documentar, indexar, embedding, knowledge, docs | sonnet |
| atlas | executar, testar, debug, validar, deploy, infra, database | opus |
| york | curso, monetizar, preco, hotmart, funil, monetize, pricing | sonnet |

## Priority Semantics
| Priority | Meaning | Example domains |
|----------|---------|-----------------|
| 9-10 | Critical: core system routing | orchestration, deploy, security |
| 7-8 | High: primary business domains | build, research, marketing |
| 5-6 | Normal: supporting tasks | docs, formatting, indexing |
| 1-4 | Low: optional or rare tasks | logging, archival, cleanup |

## Confidence Threshold Guidance
| Threshold | Behavior |
|-----------|----------|
| 0.9+ | Only fire on near-exact keyword match; very conservative |
| 0.7-0.89 | Standard precision routing; recommended for most rules |
| 0.5-0.69 | Permissive; good for broad domains with many synonyms |
| < 0.5 | Noisy; avoid unless semantic routing handles disambiguation |

## routing_strategy Selection
| Strategy | When to use |
|----------|-------------|
| `keyword_match` | Clear keyword taxonomy, small keyword set |
| `semantic` | Ambiguous domain, many paraphrases, semantic overlap |
| `hybrid` | Large bilingual keyword set, mixed precision needs |

## Fallback Logic
- `fallback` fires when primary satellite is unavailable or below confidence_threshold
- Common fallback pairs: `shaka` -> `pytha`, `edison` -> `atlas`, `lily` -> `york`
- Never use the same satellite for both `satellite` and `fallback`
- `atlas` is a common universal fallback for execution-heavy domains

## Boundary vs Nearby Types
| Type | What it is | Why it is not `dispatch_rule` |
|------|------------|-------------------------------|
| handoff | full instruction packet: context, tasks, scope, commit | tells agent WHAT to do, not WHO receives |
| signal | runtime event: status + quality_score + timestamp | reports WHAT happened, not WHERE to route |
| workflow | step graph with dependencies and sequencing | coordinates HOW work flows, not WHO receives |
| spawn_config | spawn parameters: mode, slots, timeout | configures HOW to launch, not routing policy |

Rule of thumb:
- "Route these keywords to satellite X" -> `dispatch_rule`
- "Tell satellite X what to do next" -> `handoff`
- "Satellite X just finished" -> `signal`
- "Run N satellites in parallel" -> `spawn_config`

## Naming Pattern
P12 schema defines: `p12_dr_{scope}.yaml`
Examples:
- `p12_dr_research.yaml`
- `p12_dr_build.yaml`
- `p12_dr_marketing.yaml`
- `p12_dr_orchestration.yaml`

## Operational Constraints
- Must stay under 3072 bytes
- `id` must match filename scope segment
- `quality: null` is invariant at authoring time
- Keywords should cover common abbreviations and PT/EN variants
- One rule per scope domain; do not combine unrelated scopes
