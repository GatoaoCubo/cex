---
id: n07_memory_deep_audit
kind: memory-summary
nucleus: N07
pillar: P10
title: "Deep Architecture Audit: CEX Internals vs Industry Reality"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: N07_orchestrator
quality: 9.1
tags: [audit, architecture, 8f, sins, llm_function, terminology, deep, permanent]
tldr: "4 architectural layers audited. Found: 8F maps perfectly to industry. Sin system is valid persona engineering. 139 builder ISOs in Portuguese. 6 CEX-only terms need industry mapping."
density_score: null
source_session: SELF_BOOTSTRAP_2026-04-07
---

# Deep Architecture Audit

## Layer 1: 8F Pipeline vs Industry

The 8F pipeline is NOT arbitrary. It maps 1:1 to recognized industry patterns:

| 8F Step | CEX name | Industry pattern | Provider term | Status |
|---------|----------|-----------------|---------------|--------|
| F1 | CONSTRAIN | Schema validation | JSON Schema (OpenAI), Pydantic (LangChain), Guardrails | ✅ Aligned |
| F2 | BECOME | Agent initialization | System prompt (all), Agent config (CrewAI), Role (LangGraph) | ✅ Aligned |
| F3 | INJECT | RAG / context injection | RAG (all), Context stuffing, Few-shot injection | ✅ Aligned |
| F4 | REASON | Planning / chain-of-thought | Extended thinking (Anthropic), Reasoning (OpenAI o1/o3) | ✅ Aligned |
| F5 | CALL | Tool use / function calling | Tool use (Anthropic), Function calling (OpenAI/Google) | ✅ Aligned |
| F6 | PRODUCE | Generation / inference | Completion (all), Inference (MLOps) | ✅ Aligned |
| F7 | GOVERN | Evaluation / quality gating | Evals (OpenAI), LLM-as-judge, Quality gates (CI/CD) | ✅ Aligned |
| F8 | COLLABORATE | Artifact management / handoff | Handoff (Swarm), Observation (LangChain), Event (POSIX) | ✅ Aligned |

**Verdict: 8F is a valid abstraction of the universal LLM agent execution cycle.**
No rename needed. The names are already clear enough for any LLM.

### llm_function distribution (117 kinds)

| Function | Count | % | Health |
|----------|-------|---|--------|
| GOVERN | 38 | 32% | ⚠️ Heavy — many kinds default to GOVERN. Some may be misclassified. |
| INJECT | 19 | 16% | ✅ Healthy |
| CALL | 14 | 12% | ✅ Healthy |
| CONSTRAIN | 11 | 9% | ✅ Healthy |
| BECOME | 6 | 5% | ✅ Healthy |
| NONE/null | 4 | 3% | ❌ Must be assigned: instruction, hook_config, director, effort_profile |
| REASON | 3 | 3% | ⚠️ Low — more kinds should REASON (decision_record, dispatch_rule, router) |
| COLLABORATE | 3 | 3% | ✅ Expected (only orchestration kinds) |
| PRODUCE | 3 | 3% | ⚠️ Low — workflow, dag, chain. Maybe landing_page should be PRODUCE too? |

### 4 kinds with missing llm_function (MUST FIX)

| Kind | Should be | Rationale |
|------|-----------|-----------|
| instruction (P03) | REASON | Instructions guide reasoning, not just injection |
| hook_config (P04) | GOVERN | Config for lifecycle hooks = governance |
| director (P08) | REASON | Directors make routing decisions (being renamed to supervisor) |
| effort_profile (P09) | CONSTRAIN | Effort estimation constrains task scope |

## Layer 2: Sin System = Persona Engineering

| Industry concept | CEX implementation | Status |
|-----------------|-------------------|--------|
| **Persona engineering** | Sin lens system | ✅ Valid |
| **Role-based prompting** | prompt_injection per nucleus | ✅ Standard practice |
| **Behavioral steering** | lens text injected into system prompt | ✅ Used by all providers |
| **Multi-agent diversity** | 7 sins = 7 different reasoning styles | ✅ Innovative |

The sin system IS persona engineering — a well-documented technique where
different behavioral instructions cause the same model to produce meaningfully
different outputs. The innovation is using 7 capital sins as memorable,
orthogonal behavioral dimensions.

**Industry framing**: "persona-driven behavioral differentiation through
system prompt injection."

**Keep**: The sin system is CEX's differentiator. It doesn't need industry
renaming — it IS the brand. The metaphor dictionary already translates it.

## Layer 3: CEX-Only Terms (Leakage Audit)

Terms found across the repo that are CEX-specific and may confuse external LLMs:

| CEX term | Files | Industry equivalent | Action |
|----------|-------|-------------------|--------|
| sin (persona) | 2024 | **persona** / behavioral lens | KEEP (CEX brand, already in metaphor dict) |
| density_score | 1637 | **information density** / signal-to-noise ratio | KEEP (well-defined in frontmatter) |
| llm_function | 1629 | **pipeline_stage** / execution_phase | KEEP (maps to 8F, self-documenting) |
| nucleus | 605 | **agent** / worker agent | DOCUMENT (add to metaphor dict) |
| agent_group | 399 | **agent_group** / team / department | RENAME → Consider deprecating |
| type_builder | 382 | **archetype** / kind_builder | KEEP (self-documenting) |
| kind-builder | 382 | same as type_builder | KEEP |
| agent_group | 347 | **agent_group** / cluster | RENAME → maps to nothing in industry |
| capabilities | 141 | **capabilities** / scope_description | 🔄 RENAMING (N03 dispatched) |
| fractal | 78 | **mirrored structure** / convention | Already in metaphor dict |
| mold | 62 | **archetype** / template | Already in metaphor dict |
| deck | 45 | **agent_card** | RENAMED (N03 completed) |

### Priority renames for CEX-only terms

| Term | Rename to | Scope | Risk |
|------|-----------|-------|------|
| agent_group | agent_group | 347 files | HIGH (massive cascade) |
| agent_group | agent_group | 399 files | HIGH (massive cascade, same target) |
| capabilities | capabilities | 141 files | MEDIUM |

**DECISION**: agent_group + agent_group both mean "which group of agents does this belong to."
They should both become `agent_group`. But this is a ~700 file cascade.
Schedule for a dedicated overnight run, not this session.

## Layer 4: Builder ISOs — Portuguese Contamination

| Metric | Value |
|--------|-------|
| Total builder ISOs | 1578 |
| Files with Portuguese | 139 (9%) |
| Most contaminated ISO type | bld_manifest_*.md (102 files have "Especialista em") |
| Other PT patterns | Validar (92), Domina (69), Produzir (57) |

**Root cause**: The manifests were generated with a Portuguese template.
The identity section of each manifest says "Especialista em construir X artifacts"
instead of "Specialist in building X artifacts."

**Fix**: Batch find-replace of 5 Portuguese patterns → English:
1. "Especialista em construir" → "Specialist in building"
2. "Domina" → "Expert in"
3. "Produzir" → "Produce"
4. "Validar" → "Validate"
5. "NAO eh" → "NOT"

This is a mechanical replacement — safe for overnight evolve.

## Summary: What's Left

| Category | Status | Remaining work |
|----------|--------|---------------|
| 8F pipeline naming | ✅ GOOD | No changes needed |
| llm_function assignments | ⚠️ 4 null | Fix 4 kinds |
| Sin system | ✅ GOOD | Keep as-is (brand differentiator) |
| Kind names | 🔄 IN PROGRESS | N03 renaming 5 kinds now |
| Schema descriptions | 🔄 IN PROGRESS | N03 translating PT→EN now |
| New kinds | 🔄 IN PROGRESS | N04 adding 4 kinds now |
| Builder ISOs (PT→EN) | ⏳ SCHEDULED | 139 files, overnight batch |
| agent_group/agent_group rename | ⏳ SCHEDULED | ~700 files, dedicated overnight |
| capabilities rename | ⏳ SCHEDULED | 141 files, overnight batch |
| Research validation | 🔄 IN PROGRESS | N01 researching official docs now |
