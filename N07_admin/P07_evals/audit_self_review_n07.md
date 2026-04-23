---
quality: 8.2
quality: 7.8
id: audit_self_review_n07
kind: audit_report
pillar: P07
nucleus: n07
mission: SELF_AUDIT
title: "N07 Orchestrator Self-Audit: Pillars, Kinds, 8F Wiring, Collaboration"
version: 1.0.0
tags: [self-audit, orchestration, pillars, kinds, 8f, collaboration, architecture]
related:
  - bld_collaboration_kind
  - p01_kc_cex_project_overview
  - p01_ctx_cex_project
  - p03_sp_n03_creation_nucleus
  - p12_wf_create_orchestration_agent
  - bld_knowledge_card_nucleus_def
  - p02_agent_creation_nucleus
  - agent_card_engineering_nucleus
  - p01_kg_cex_system_architecture
  - ctx_cex_new_dev_guide
density_score: 1.0
updated: "2026-04-22"
---

# N07 Orchestrator Self-Audit

## Pillar Coverage Matrix

| Pillar | Kinds Registered | Builders in archetypes/ | N07 Admin Artifacts | Coverage |
|--------|-----------------|------------------------|---------------------|----------|
| P01 Knowledge | 30 | 3 | 8 | PARTIAL |
| P02 Model | 23 | 5 | 5 | PARTIAL |
| P03 Prompt | 21 | 3 | 3 | SPARSE |
| P04 Tools | 36 | 8 | 2 | MINIMAL |
| P05 Output | 23 | 2 | 3 | SPARSE |
| P06 Schema | 13 | 2 | 6 | PARTIAL |
| P07 Evals | 23 | 1 | 1 | MINIMAL |
| P08 Architecture | 14 | 4 | 3 | PARTIAL |
| P09 Config | 37 | 1 | 6 | PARTIAL |
| P10 Memory | 22 | 0 | 13 | STRONG |
| P11 Feedback | 31 | 3 | 4 | SPARSE |
| P12 Orchestration | 20 | 7 | 15 | STRONG |

**Total:** 293 kinds | 39 builders (13%) | 69 N07 artifacts across 12 pillars

**System-wide builder gap:** 254 kinds registered with no executable builder. Largest gaps: P09 Config (36/37), P10 Memory (22/22), P04 Tools (28/36).

## 8F Wiring Status

| Function | Wired? | Where | Tooling | Gap |
|----------|--------|-------|---------|-----|
| F1 CONSTRAIN | YES | `.cex/kinds_meta.json` + `P{xx}/_schema.yaml` | `cex_intent_resolver.py` | None |
| F2 BECOME | YES | `archetypes/builders/{kind}-builder/` (13 ISOs) | `cex_skill_loader.py` | Only 39/293 builders exist |
| F2b SPEAK | YES | `kc_{domain}_vocabulary.md` per nucleus | `p03_pc_cex_universal.md` | Not all nuclei have vocab KC |
| F3 INJECT | YES | `N00_genesis/P01_knowledge/library/` | `cex_retriever.py`, `cex_memory_select.py` | F3b persist rarely triggered |
| F3b PERSIST | PARTIAL | `entity_memory`, `learning_record` kinds | `cex_memory_update.py` | No auto-persist hook in 8F runs |
| F3c GROUND | PARTIAL | `agent_grounding_record` kind | Retriever confidence score | No explicit provenance file written |
| F4 REASON | IMPLICIT | GDP skill + decision manifest | `cex_gdp.py` | No structured reasoning trace per run |
| F5 CALL | YES | `cex_compile.py`, `cex_doctor.py`, `cex_query.py` | 158 _tools/ scripts | Tool-to-kind mapping undocumented |
| F6 PRODUCE | DELEGATED | Nucleus LLM (8F trace in output) | None (implicit) | No production quality pre-check |
| F7 GOVERN | YES | 7 gates + 12LP + 5D scoring | `cex_score.py`, `cex_hooks.py` | Automated scoring rate low |
| F7b LEARN | PARTIAL | `reward_signal`, `regression_check` kinds | `cex_feedback.py` | Not triggered per run automatically |
| F8 COLLABORATE | YES | git + compile + signal | `signal_writer.py`, `cex_compile.py` | No ACK from receiving nucleus |

**8F adoption score:** 6/8 functions explicitly wired. F4 and F6 remain nucleus-LLM-implicit.

## Collaboration Map

| Nucleus | Direction | Trigger | Artifact Type | Return Protocol |
|---------|-----------|---------|---------------|-----------------|
| N01 Intelligence | N07 -> N01 | Research, competitive analysis, large doc processing | knowledge_card, research_pipeline | signal + KC written |
| N02 Marketing | N07 -> N02 | Copy, campaigns, brand voice, taglines | prompt_template, landing_page, tagline | signal + artifact path |
| N03 Engineering | N07 -> N03 | Any artifact build, code, scaffold, schema | any kind via 8F builder | signal + commit hash |
| N04 Knowledge | N07 -> N04 | RAG setup, indexing, documentation, KCs | rag_source, knowledge_index, entity_memory | signal + indexed doc count |
| N05 Operations | N07 -> N05 | Tests, CI/CD, code review, MCP servers, config | quality_gate, env_config, mcp_server | signal + test results |
| N06 Commercial | N07 -> N06 | Pricing, monetization, sales playbooks, funnels | content_monetization, sales_playbook | signal + revenue spec |
| N01 -> N02 | Cross-nucleus | Research output feeds copy creation | knowledge_card -> landing_page | via grid wave sequencing |
| N03 -> N05 | Cross-nucleus | Built artifacts need test/deploy | artifact -> quality_gate | via handoff in grid |
| N01 -> N04 | Cross-nucleus | Research surfaces knowledge to persist | knowledge_card -> knowledge_index | via F8 signal chain |

**Signal protocol:** `.cex/runtime/signals/signal_{nucleus}_{timestamp}.json`
**Handoff protocol:** `.cex/runtime/handoffs/{MISSION}_{nucleus}.md` + `n0X_task.md`
**271 completed signals** across 105 missions since inception.

## N07 Admin Pillar Gap Analysis

| Pillar | Strongest Gap | Priority |
|--------|--------------|----------|
| P05 Output | N07 has no output formatters for orchestration reports | MEDIUM |
| P07 Evals | Only 1 eval artifact (this file); no benchmark for dispatch efficiency | HIGH |
| P11 Feedback | No learning records for orchestration decisions | HIGH |
| P04 Tools | No tool registry for 158 _tools/ scripts | MEDIUM |
| P03 Prompt | Only 3 prompts; no orchestration-specific prompt templates | LOW |

## Top 5 System Gaps

1. **Builder coverage: 87% dark** (254/293 kinds have no builder). F2 BECOME falls back to generic for most kinds -- no sin lens, no specialized ISOs. Impact: every non-covered kind gets generic output instead of specialist output. Severity: HIGH.

2. **F3b auto-persist not wired** -- every 8F run surfaces new entities and learnings, but `cex_memory_update.py` is only called manually. The institutional memory compounds only when a nucleus explicitly decides to persist. Severity: HIGH.

3. **No inter-nucleus ACK protocol** -- N07 polls signals to detect completion, but there is no handshake confirming the nucleus received its handoff or is acting on the correct task file. Race conditions exist when n0X_task.md is overwritten before the nucleus reads it. Severity: MEDIUM.

4. **P09 Config infrastructure: 1 builder for 37 kinds** -- only env_config has a builder. The other 36 config kinds (rate_limit_config, secret_config, feature_flag, canary_config, etc.) are orphaned. F1 CONSTRAIN for config tasks falls back to generic. Severity: HIGH.

5. **Tool-to-kind mapping undocumented** -- 158 tools in _tools/ have no canonical mapping to kinds_meta.json. N07 cannot programmatically discover which tool supports which kind. F5 CALL relies on N07's training data. Severity: MEDIUM.

## Recommendations

1. **`_tools/cex_kind_tool_map.py`** -- auto-generate a `kind_tool_registry.json` by parsing `_tools/cex_*.py` docstrings for `kind:` annotations. Assign each tool to its pillar+kind. Closes F5 gap. Owner: N03. Effort: 1 session.

2. **`_tools/cex_hooks_native.py` F3b hook** -- after every F8 signal, auto-call `cex_memory_update.py --from-signal {signal_path}` to extract entities and learnings from the completed artifact. Closes F3b gap. Owner: N05. Effort: 1 session.

3. **Builder backfill sprint** -- prioritize the 22 P10 (Memory) builders and top 10 P09 (Config) builders. These are the most-used kinds that currently have no specialist ISO. Run as a FRACTAL_FILL_W7 wave. Owner: N03 grid. Effort: 2-3 sessions.

4. **`cex_handoff_ack.py`** -- nucleus writes `.cex/runtime/handoffs/.ack/{nucleus}_{mission}.json` at session start (after reading handoff). N07 checks for ACK before assuming nucleus is working. Closes race condition. Owner: N03 + N05. Effort: 1 session.

5. **N07 P07 benchmark** -- create `N07_admin/P07_evaluation/benchmark_dispatch_efficiency.md` tracking: avg dispatch-to-signal time, % missions with 0 FAIL, % artifacts reaching quality >= 9.0. Closes orchestration eval gap. Owner: N07 (self). Effort: 0.5 session.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_kind]] | downstream | 0.41 |
| [[p01_kc_cex_project_overview]] | upstream | 0.40 |
| [[p01_ctx_cex_project]] | upstream | 0.40 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.36 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.35 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.34 |
| [[p02_agent_creation_nucleus]] | upstream | 0.34 |
| [[agent_card_engineering_nucleus]] | upstream | 0.34 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.33 |
| [[ctx_cex_new_dev_guide