---
kind: audit_report
8f: F7_govern
id: p08_hybrid_review_n03
pillar: P08
llm_function: GOVERN
purpose: Master audit of 4 builder families (52 ISOs) produced during HYBRID_REVIEW Wave 1+2 by qwen3:8b
quality: 9.2
title: "HYBRID_REVIEW N03 -- Master Audit: 52 ISOs across 4 builder kinds"
version: "1.0.0"
author: n03_reviewer
tags: [audit, hybrid_review, builder_family, qwen3, calibration, n03]
keywords: [audit_report, 5d_scoring, builder_governance, rewrite_log, domain_drift]
triggers: []
tldr: "Audit of 52 ISOs in 4 builder families. Family averages 4.3-5.5/10. Zero ISOs passed 9.0 floor before fixes. 12 rewritten (3 per kind). Root cause: qwen3:8b hallucinated the domain for 3/4 kinds (PID controls, corporate strategy, SIP conferencing). Recommendation: regenerate remaining 40 ISOs with opus-4-6."
domain: "builder family governance"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_config_kind
  - bld_architecture_kind
  - bld_schema_kind
  - p08_audit_agent_profile_builder
  - bld_instruction_kind
  - kind-builder
  - bld_knowledge_card_kind
  - master_systemic_defects
  - bld_collaboration_kind
  - p03_sp_kind_builder
---

# HYBRID_REVIEW N03 Master Audit

## Executive Summary

| Metric | Value |
|---|---|
| ISOs reviewed | 52 / 52 |
| Builder kinds | 4 (agent_profile, dual_loop_architecture, planning_strategy, realtime_session) |
| Pass 9.0 floor (pre-audit) | 0 / 52 |
| ISOs rewritten to >=9.0 | 12 / 52 |
| ISOs REVIEW band (7.0-8.9) | ~14 / 52 |
| ISOs REJECT (< 7.0) | ~26 / 52 |
| Family average (pre) | 4.88 / 10 |
| Family average (post-fixes) | 5.68 / 10 |

**Verdict:** Families are NOT production-ready. 12 anchor ISOs rewritten to golden standard. Remaining 40 require a second regeneration pass under opus-4-6 before promotion.

## Per-Kind Structural Completeness

All 4 kinds have the full 13-ISO structure. No missing files.

| Kind | 13 ISOs present? | Family avg (pre) | Rewrites | Audit file |
|---|---|---|---|---|
| agent_profile | yes (13/13) | 5.6 | 3 (instruction, output_template, quality_gate) | `N03_engineering/audits/audit_agent_profile_builder.md` |
| dual_loop_architecture | yes (13/13) | 5.47 | 3 (architecture, tools, config) | `N03_engineering/audits/audit_dual_loop_architecture_builder.md` |
| planning_strategy | yes (13/13) | 4.3 | 3 (manifest, output_template, schema) | `N03_engineering/audits/audit_planning_strategy_builder.md` |
| realtime_session | yes (13/13) | 4.45 | 3 (output_template, schema, quality_gate) | `N03_engineering/audits/audit_realtime_session_builder.md` |

## Naming Convention Observed

The 13-ISO family uses: `bld_{architecture, collaboration, config, examples, instruction, knowledge_card, manifest, memory, output_template, quality_gate, schema, system_prompt, tools}_{kind}.md`.

The handoff's proposed naming (bld_validation, bld_test, bld_decision, bld_metrics, bld_cache, bld_router) does NOT match the established CEX convention used by knowledge-card-builder, agent-builder, workflow-builder. The established convention was preserved.

## Top 5 Architectural Issues (Cross-Kind Patterns)

### 1. Domain hallucination (3 of 4 kinds)
qwen3:8b mis-framed the kind entirely in 3 families:
- `dual_loop_architecture` -> classical control systems (PID, Lyapunov stability, ISO 26262 actuators). Correct: LLM fast-slow architectures (Sonnet inner + Opus outer, System 1/2, Reflexion).
- `planning_strategy` -> corporate strategy (KPIs, MoSCoW, PMBOK, $500M budgets, Pandas/Backtrader). Correct: agent planning algorithms (ReAct, ToT, MCTS, HTN, Plan-and-Execute).
- `realtime_session` -> legacy SIP/WebRTC video conferencing (TLS heartbeats). Correct: OpenAI Realtime API / Gemini Live (ephemeral tokens, server_vad, barge-in, response.audio.delta).
- `agent_profile` was closest to correct domain but stayed generic (resume-style templates).

### 2. File reference drift
Cross-kind pattern: ISOs reference non-canonical paths (`SCHEMA.md`, `OUTPUT_TEMPLATE.md`, `VALIDATION_RULES.md`) instead of `bld_schema_{kind}.md`, `bld_output_template_{kind}.md`. Breaks 8F F1 CONSTRAIN because the builder cannot resolve its own schema.

### 3. Fabricated tooling
`bld_tools_{kind}.md` across 4 kinds lists 15+ nonexistent `cex_*.py` scripts (cex_analyzer.py, cex_optimizer.py, val_check.py, cex_realtime.py). Correct pattern: reference real `_tools/cex_*.py` (cex_compile, cex_score, cex_doctor, signal_writer).

### 4. Pillar mis-assignment and fake density scores
Multiple ISOs within a single family disagree on pillar (P03 / P06 / P09 / P11 co-exist for realtime_session). All 52 ISOs claim identical `density_score: 0.85` regardless of actual information density -- the model self-scored uniformly.

### 5. Weak test/example cases
`bld_examples_{kind}.md` and `bld_quality_gate_{kind}.md` use placeholders (`{{example1}}`, `name/role/credentials` for agent_profile) or abstract pseudocode rather than concrete, runnable scenarios with frontmatter + body.

## Recommendations

1. **Do NOT promote** any of these 4 builder families to main until a second regeneration pass.
2. **Regenerate the remaining ~40 REJECT/REVIEW ISOs under opus-4-6** (not qwen3:8b) using the 12 rewritten anchor ISOs as in-context examples. Estimated 2-3 waves via N03 dispatch.
3. **Seed pillar assignments** before regeneration: agent_profile=P02, dual_loop_architecture=P08, planning_strategy=P08, realtime_session=P04. Lock these in frontmatter templates.
4. **Ingest gold references** into the regenerator's context: knowledge-card-builder (content density), agent-builder (agent-architecture pattern), workflow-builder (orchestration pattern).
5. **Add domain-anchor KC** per kind before regeneration (`kc_dual_loop_architecture.md`, `kc_planning_strategy.md`, `kc_realtime_session.md`) so the builder has factual ground truth to reference.
6. **Consider quantifiable validator gates** in cex_doctor for: file-reference existence (referenced bld_*.md files must exist), tool-reference existence (cex_*.py must exist on disk), pillar uniqueness per family.

## Should These Kinds Use a Different Builder Archetype Pattern?

Assessment: The 13-ISO archetype fits all 4 kinds correctly. The failure mode was not the archetype -- it was the generator model (qwen3:8b) lacking domain knowledge of agent architectures, planning algorithms, and realtime APIs. The archetype worked as designed: structural completeness 52/52. The failure was in ISO content, not scaffold.

Recommendation: keep the 13-ISO archetype; change the generator (qwen3:8b -> opus-4-6 or sonnet-4-6 with injected KC references).

## Rewrite Log (12 ISOs)

| Kind | File | Pre | Post |
|---|---|---|---|
| agent_profile | bld_instruction_agent_profile.md | 4.4 | 9.4 |
| agent_profile | bld_output_template_agent_profile.md | 2.8 | 9.8 |
| agent_profile | bld_quality_gate_agent_profile.md | 4.2 | 9.6 |
| dual_loop_architecture | bld_architecture_dual_loop_architecture.md | 2.0 | 9.3 |
| dual_loop_architecture | bld_tools_dual_loop_architecture.md | 3.0 | 9.2 |
| dual_loop_architecture | bld_config_dual_loop_architecture.md | 3.2 | 9.2 |
| planning_strategy | bld_manifest_planning_strategy.md | 3.7 | 9.1 |
| planning_strategy | bld_output_template_planning_strategy.md | 2.1 | 9.3 |
| planning_strategy | bld_schema_planning_strategy.md | 4.2 | 9.2 |
| realtime_session | bld_output_template_realtime_session.md | 2.4 | 9.1 |
| realtime_session | bld_schema_realtime_session.md | 3.5 | 9.2 |
| realtime_session | bld_quality_gate_realtime_session.md | 3.4 | 9.2 |

## Signature

N03 Builder Nucleus - Inventive Pride. 12 ISOs now worthy of signature; 40 ISOs flagged for regeneration. This audit IS the signature on the remaining work.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_kind]] | downstream | 0.39 |
| [[bld_architecture_kind]] | related | 0.38 |
| [[bld_schema_kind]] | upstream | 0.37 |
| [[p08_audit_agent_profile_builder]] | sibling | 0.36 |
| [[bld_instruction_kind]] | upstream | 0.33 |
| [[kind-builder]] | related | 0.33 |
| [[bld_knowledge_card_kind]] | upstream | 0.32 |
| [[master_systemic_defects]] | upstream | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[p03_sp_kind_builder]] | upstream | 0.29 |
