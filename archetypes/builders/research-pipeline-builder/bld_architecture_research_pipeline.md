---
kind: architecture
id: bld_architecture_research_pipeline
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of research pipeline — 7 stages, multi-model, data flow
---

# Architecture: research_pipeline in the CEX

## 7-Stage Pipeline
```
QUERY → S1 INTENT (classify) → S2 PLAN/STORM (5 perspectives × 5-7 sub-Qs)
  → S3 RETRIEVE/CRAG (30+ sources parallel, quality gate ≥0.7)
  → S4 RESOLVE (entity dedup cross-source)
  → S5 SCORE (Gartner 7-dim per result)
  → S6 SYNTHESIZE/GoT (domain models merge data)
  → S7 VERIFY/CRITIC (thinking model, max 3 iter)
  → REPORT [HTML + PPTX + JSON]
```

## Data Flow
```
config.yaml ──► intent_classifier ──► storm_planner
                                          │
                              5 perspectives × 5-7 Qs
                                          │
                            ┌─────────────┼─────────────┐
                            ▼             ▼             ▼
                     inbound_src    search_src    outbound_src
                     (marketplace)  (web search)  (social/review)
                            │             │             │
                            └──────┬──────┘─────────────┘
                                   ▼
                           crag_scorer (0.0-1.0)
                                   │ (≥0.7 pass)
                                   ▼
                          entity_resolver (dedup)
                                   │
                                   ▼
                         gartner_scorer (7-dim)
                                   │
                                   ▼
                        got_synthesizer (multi-model)
                                   │
                                   ▼
                         critic_verifier (max 3 iter)
                                   │
                            ┌──────┼──────┐
                            ▼      ▼      ▼
                          HTML   PPTX   JSON
```

## Component Inventory
| Component | Stage | Model | External |
|-----------|-------|-------|----------|
| intent_classifier | S1 | regex+embed | none |
| storm_planner | S2 | reasoning | LLM API |
| parallel_retriever | S3 | APIs | 30+ sources |
| crag_scorer | S3 | fast | LLM API |
| entity_resolver | S4 | deterministic | Embedding API |
| gartner_scorer | S5 | fast | LLM API |
| got_synthesizer | S6 | multi-model | Multi-LLM |
| critic_verifier | S7 | thinking | Thinking model |
| report_renderer | Out | template | Jinja2 |

## Position in CEX
| Layer | Location |
|-------|----------|
| Template + Examples | P04_tools/{templates,examples}/ |
| Nucleus instance | N01_intelligence/{tools,knowledge,orchestration}/ |
| Company config | _instances/{co}/N01_intelligence/ |

## Boundaries
| This builder | Other builder |
|-------------|---------------|
| Pipeline architecture | Python runtime → cli-tool-builder |
| Source catalog | API client code → api-client-builder |
| Config schema | DB schema → db-connector-builder |
| Report structure | HTML/CSS → formatter-builder |
