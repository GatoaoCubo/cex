---
quality: 8.9
quality: 8.2
id: kc_lens_technical
kind: knowledge_card
8f: F3_inject
kc_type: meta_kc
pillar: P01
nucleus: n04
version: 1.0.0
created: "2026-04-21"
updated: "2026-04-21"
author: n04_knowledge
title: "Lens: Technical -- CEX as Multi-Agent Engineering Infrastructure"
domain: didactic_engine
subdomain: lens_system
tags: [lens, technical, DDD, CI-CD, agents, developer]
tldr: "Direct mapping of CEX concepts to industry-standard engineering terms. No metaphors -- exact equivalents from DDD, CI/CD, MLOps, multi-agent frameworks. For developers who want the real terminology."
density_score: null
related:
  - kc_lens_factory
  - kc_lens_index
  - spec_metaphor_dictionary
  - p01_kc_8f_pipeline
  - ctx_cex_new_dev_guide
---

# Lens: Technical

> Unlike the other lenses (factory, city, biology, game), this lens maps CEX concepts directly to industry-standard equivalents. No analogy -- the actual terms.

## Core Mapping

| CEX Concept | Technical Equivalent |
|-------------|---------------------|
| CEX system | Multi-agent orchestration framework (293 schemas, 12 bounded contexts, 8 agents) |
| 8F pipeline | 8-stage build pipeline: Constrain->Become->Inject->Reason->Call->Produce->Govern->Collaborate |
| 12 pillars | DDD bounded contexts (P01 Knowledge -> P12 Orchestration) |
| nucleus | Autonomous agent with specialized role, domain, tools, sin-driven objective |
| N07 orchestrator | Workflow orchestrator (Temporal/Airflow); dispatches + consolidates, never builds |
| kind | Schema type / artifact class (293 registered; naming, max bytes, pillar, builder) |
| builder | Code generator: 12 ISOs per kind (1 per pillar); schema + context -> artifact |
| ISO | Config file per concern (model, prompt, knowledge, tools, output, schema, eval, arch, config, memory, feedback, orchestration) |
| artifact | .md + YAML frontmatter following kind schema; compiled to .yaml |
| GDP | Configuration wizard: collect subjective preferences before autonomous generation |
| sin lens | Optimization objective / loss function (envy=coverage, lust=creativity, pride=craft) |
| quality gate (F7) | CI gate: 7 hard gates + 5D scoring; min 8.0; max 2 retries |
| signal (F8) | Event / webhook: JSON payload with nucleus id, status, quality score |
| handoff | Task spec / work item: Markdown brief with artifact refs + constraints |
| dispatch | Task queue: solo (1), grid (N parallel), swarm (N same-kind) |
| wave | Pipeline stage: sequential group; gate required before next stage |
| grid | Parallel execution pool (max 6 agents, isolated sessions) |
| RAG | TF-IDF + Haiku reranking on 2184-doc corpus; Phase 0 MCP for external context |

## Top 20 Kinds: Industry Equivalents

| Kind | Industry Equivalent |
|------|---------------------|
| `knowledge_card` | Structured KB article (schema-enforced, compiled to YAML) |
| `agent` | Autonomous agent def (CrewAI Agent / LangGraph node) |
| `prompt_template` | Parameterized prompt / DSPy signature (Mustache slots) |
| `system_prompt` | LLM system message / RLHF instruction set |
| `workflow` | DAG / state machine (Airflow DAG, GitHub Actions) |
| `quality_gate` | CI gate: 7 hard gates + 5D rubric |
| `knowledge_index` | TF-IDF / vector search index (2184 docs) |
| `guardrail` | Policy enforcement / content filter (halts before F6) |
| `env_config` | 12-factor environment config (keys, limits, routing) |
| `entity_memory` | Persistent entity store (shared across sessions + agents) |
| `crew_template` | Multi-agent workflow: N roles + topology + handoff protocol |
| `decision_record` | Architecture Decision Record (ADR) |
| `chain` | Prompt chain with conditional routing (LangChain equivalent) |
| `router` | Load balancer / intent classifier (kind + domain) |
| `scoring_rubric` | Evaluation rubric for F7 GOVERN 5-dimension scoring |

## 5 Developer Entry Points

1. **DDD.** 12 pillars = 12 bounded contexts. Cross-pillar refs are explicit artifact IDs. Each context owns its schema + builder registry.
2. **CI/CD.** 8F is a typed build pipeline: F7 gate (min 8.0), retry budget = 2, F8 compiles `.md` to `.yaml`.
3. **Typed registry.** 293 kinds with JSON schema + naming rule + max bytes. `cex_doctor.py` = corpus-wide linter.
4. **Sin = loss function.** Sin lens = RLHF behavioral prior. N05 (Wrath) maximizes rejection. N07 (Sloth) minimizes direct work, delegates all.
5. **Self-indexing RAG.** Phase 0: MCP (N07). Phase 1: TF-IDF. Phase 2: Haiku rerank. F8 re-indexes each artifact -- every build compounds the corpus.

## Sources

- `spec_metaphor_dictionary.md`: industry term column (canonical)
- `CLAUDE.md`: nucleus defs, 8F pipeline, pillar structure, dispatch modes
- DDD (Evans 2003): bounded contexts, ubiquitous language
- CrewAI / LangGraph / Temporal: multi-agent orchestration equivalents

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_lens_factory]] | sibling | 0.82 |
| [[kc_lens_index]] | upstream | 0.78 |
| [[spec_metaphor_dictionary]] | upstream | 0.75 |
| [[p01_kc_8f_pipeline]] | related | 0.60 |
| [[ctx_cex_new_dev_guide]] | related | 0.45 |
