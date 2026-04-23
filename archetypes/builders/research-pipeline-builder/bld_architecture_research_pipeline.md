---
kind: architecture
id: bld_architecture_research_pipeline
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of research pipeline — 7 stages, multi-model, data flow
quality: 9.1
title: "Architecture Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_research_pipeline_builder
  - bld_instruction_research_pipeline
  - n01_tool_research_pipeline
  - bld_collaboration_research_pipeline
  - research-pipeline-builder
  - p02_agent_research_pipeline_intelligence
  - bld_architecture_social_publisher
  - bld_knowledge_card_research_pipeline
  - bld_collaboration_model_provider
  - bld_collaboration_model_card
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_research_pipeline_builder]] | upstream | 0.38 |
| [[bld_instruction_research_pipeline]] | upstream | 0.35 |
| [[n01_tool_research_pipeline]] | upstream | 0.33 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.32 |
| [[research-pipeline-builder]] | upstream | 0.30 |
| [[p02_agent_research_pipeline_intelligence]] | upstream | 0.29 |
| [[bld_architecture_social_publisher]] | sibling | 0.28 |
| [[bld_knowledge_card_research_pipeline]] | upstream | 0.27 |
| [[bld_collaboration_model_provider]] | upstream | 0.26 |
| [[bld_collaboration_model_card]] | upstream | 0.26 |
