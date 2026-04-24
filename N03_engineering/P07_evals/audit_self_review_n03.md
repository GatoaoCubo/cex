---
quality: 8.3
quality: 7.9
id: audit_self_review_n03
kind: audit_report
8f: F7_govern
pillar: P07
nucleus: n03
mission: SELF_AUDIT
title: "N03 Engineering Self-Audit: Builders, Schema, 8F Wiring, Pipeline Gaps"
version: 1.0.0
tags: [self-audit, engineering, builders, schema, 8f, infrastructure]
created: 2026-04-18
density_score: 0.91
related:
  - wave2_quality_report
  - bld_architecture_kind
  - bld_collaboration_kind
  - kind-builder
  - system_health_20260413
  - bld_architecture_memory_architecture
  - polish_fixes_20260413
  - self_audit_newpc_2026_04_12
  - bld_knowledge_card_kind
  - bld_config_kind
updated: "2026-04-22"
---

# N03 Engineering Self-Audit: Builders, Schema, 8F Wiring, Pipeline Gaps

## Executive Summary

Full scan of the builder infrastructure against the 293-kind registry.
All 293 kinds have complete 13-ISO builders (100% coverage).
`cex_doctor.py` reports 200 PASS / 94 WARN / 0 FAIL.
Critical gaps cluster in three areas: (1) 8F wiring depth in ISO instructions,
(2) N03 schema artifacts missing for 6 P06 kinds, and
(3) 13 P12 orchestration kinds with no N03 implementation artifacts.

---

## Builder Completeness Matrix

| Pillar | Kinds Registered | Builders Complete | Avg ISOs | Gap Count |
|--------|-----------------|-------------------|----------|-----------|
| P01    | 30              | 30                | 13.0     | 0         |
| P02    | 23              | 23                | 13.0     | 0         |
| P03    | 21              | 21                | 13.0     | 0         |
| P04    | 36              | 36                | 13.0     | 0         |
| P05    | 23              | 23                | 13.0     | 0         |
| P06    | 13              | 13                | 13.0     | 0         |
| P07    | 23              | 23                | 13.0     | 0         |
| P08    | 14              | 14                | 13.0     | 0         |
| P09    | 37              | 37                | 13.0     | 0         |
| P10    | 22              | 22                | 13.0     | 0         |
| P11    | 31              | 31                | 13.0     | 0         |
| P12    | 20              | 20                | 13.0     | 0         |
| **Total** | **293**      | **293**           | **13.0** | **0**     |

**Finding**: All 293 registered kinds have exactly 13 ISO files per builder.
No structural gaps in builder coverage. The 13 canonical ISOs per builder are:
`bld_manifest`, `bld_instruction`, `bld_schema`, `bld_examples`, `bld_architecture`,
`bld_system_prompt`, `bld_quality_gate`, `bld_collaboration`, `bld_config`,
`bld_knowledge_card`, `bld_memory`, `bld_output_template`, `bld_tools`.

---

## Top 10 Builders with ISO Quality Issues

No builder has structural missing ISOs (all at 13). Quality issues are density/size violations,
not structural gaps. From `cex_doctor.py` — worst offenders by warning density:

| Builder              | WARNs | Primary Issue    | Affected ISOs                              |
|----------------------|-------|------------------|--------------------------------------------|
| voice-pipeline       | 5     | density + size   | bld_examples, bld_memory, bld_tools, bld_output_template |
| white-label-config   | 1     | size (7037B)     | bld_knowledge_card                         |
| usage-report         | 1     | size (6162B)     | bld_knowledge_card                         |
| value-object         | 1     | density (0.74)   | bld_tools                                  |
| usage-quota          | 1     | density (0.71)   | bld_examples                               |
| dual-loop-architecture | 1   | density          | bld_examples                               |
| slo-definition       | 1     | density          | bld_tools                                  |
| saga                 | 1     | density          | bld_tools                                  |
| revision-loop-policy | 1     | density          | bld_tools                                  |
| process-manager      | 1     | density          | bld_tools                                  |

**System health**: 200 PASS / 94 WARN / 0 FAIL.
94 WARNs decompose as: 81 density violations (min 0.78 floor), 13 size violations (>6144B std).
ISO types most affected: `bld_examples` (37 violations), `bld_tools` (19), `bld_memory` (10),
`bld_config` (6), `bld_collaboration` (5), `bld_output_template` (2), `bld_manifest` (2).

---

## P06 Schema Coverage

P06 has 13 kinds. All 13 have builders. N03's `P06_schema/` directory holds
implementation artifacts for 7 of 13 kinds. Six kinds have builders but no N03 schema doc.

| Kind               | Builder | N03 Schema Artifact | Builder Examples | Gap                     |
|--------------------|---------|---------------------|------------------|-------------------------|
| aggregate_root     | yes     | no                  | 1                | no N03 implementation   |
| api_reference      | yes     | yes                 | 1                | complete                |
| data_contract      | yes     | no                  | 1                | no N03 implementation   |
| edit_format        | yes     | no                  | 1                | no N03 implementation   |
| enum_def           | yes     | yes                 | 1                | complete                |
| event_schema       | yes     | no                  | 1                | no N03 implementation   |
| input_schema       | yes     | yes                 | 1                | complete                |
| interface          | yes     | yes                 | 1                | complete                |
| openapi_spec       | yes     | no                  | 1                | no N03 implementation   |
| type_def           | yes     | yes                 | 1                | complete                |
| validation_schema  | yes     | yes                 | 1                | complete                |
| validator          | yes     | yes                 | 1                | complete                |
| value_object       | yes     | no                  | 1                | no N03 implementation   |

**Coverage**: 7/13 P06 kinds have N03 implementation artifacts (54%).
Missing: `aggregate_root`, `data_contract`, `edit_format`, `event_schema`, `openapi_spec`, `value_object`.
Each missing kind lacks a concrete domain schema (`sch_*.md`) in `N03_engineering/P06_schema/`.

---

## 8F Adoption in Builders

Measured against all 293 `bld_instruction_*.md` files and cross-checked against
`bld_manifest`, `bld_system_prompt`, `bld_quality_gate`, `bld_architecture`, and `bld_collaboration`.

| Function           | Adoption % | Evidence Pattern                         | Gap                                      |
|--------------------|-----------|------------------------------------------|------------------------------------------|
| F1 CONSTRAIN       | 100%      | All instructions reference kind/pillar   | None                                     |
| F2 BECOME          | 20%       | Explicit "load builder ISOs" in 60/294   | 80% do not declare builder identity      |
| F3 INJECT          | 28%       | KC + context source refs in 83/294       | 72% skip context injection docs          |
| F4 REASON          | 100%      | Reasoning/approach section universal     | None                                     |
| F5 CALL            | 31%       | Tool call docs in 90/294                 | 69% do not list tool execution steps     |
| F6 PRODUCE         | 66%       | Draft generation steps in 193/294        | 34% lack explicit produce guidance       |
| F7 GOVERN          | 56%       | Quality gate refs in 166/294             | 44% do not document validation criteria  |
| F8 COLLABORATE     | 26%       | Signal/compile/commit in 77/294          | 74% do not document F8 handoff steps     |

**Critical finding**: F2 BECOME (20%) and F8 COLLABORATE (26%) are severely underrepresented.
F2 gap means builders do not explicitly load their own ISO stack — they execute but do not
declare identity. F8 gap means 74% of instruction files omit signal, compile, and commit steps.
F7 GOVERN at 56% is a quality enforcement risk: nearly half of builders lack documented
validation criteria in their instructions.

**By ISO type (F7/F8 cross-check)**:
- `bld_quality_gate`: 100% F7 refs (100% coverage — expected, as this IS the gate)
- `bld_collaboration`: 100% F8 refs (signal/handoff baked in)
- `bld_manifest`: 89% F8 refs — strong handoff documentation
- `bld_instruction`: 56% F7, 30% F8 — mid-tier
- `bld_system_prompt`: 26% F7, 12% F8 — sparse governance wiring

---

## Collaboration Map

| Nucleus | Direction | Artifact Types                                  |
|---------|-----------|-------------------------------------------------|
| N03 -> N01 | dispatch | audit_report, knowledge_card (research requests) |
| N03 -> N04 | produce  | knowledge_card, glossary_entry, learning_record  |
| N03 -> N05 | dispatch | workflow, deployment_manifest, validation_schema |
| N03 -> N07 | signal   | complete signal + quality score on every build   |
| N07 -> N03 | handoff  | n03_task.md with kind, pillar, scope, constraints |
| N01 -> N03 | context  | knowledge_card refs injected at F3 INJECT        |
| N04 -> N03 | context  | KC library search results at F3 INJECT           |

N03 is a producer nucleus (not a coordinator). Inbound = task handoffs from N07.
Outbound = completed artifacts + signals. N03 never dispatches grids; it receives them.

---

## Top 5 Infrastructure Gaps

**GAP 1 — F2 BECOME / F8 COLLABORATE not wired in 74-80% of bld_instruction files** (CRITICAL)
The 8F pipeline requires F2 to load builder identity and F8 to signal completion.
Only 20% of instructions document F2; only 26% document F8.
Without explicit F8 in the instruction, a builder may produce the artifact but omit
`signal_writer`, `cex_compile.py`, and `git commit` — leaving N07 with no completion signal.
**File target**: all 294 `bld_instruction_*.md` need F2 + F8 sections.

**GAP 2 — 6 P06 schema kinds have no N03 implementation artifact** (HIGH)
`aggregate_root`, `data_contract`, `edit_format`, `event_schema`, `openapi_spec`, `value_object`
all have builders but no domain schema in `N03_engineering/P06_schema/`.
This means real-world use cases for DDD aggregates, OpenAPI generation, and event contracts
lack verified N03 examples to anchor builder context injection (F3).
**File target**: `N03_engineering/P06_schema/sch_{kind}_n03.md` for each of 6 kinds.

**GAP 3 — 13 P12 orchestration kinds with no N03 artifacts** (HIGH)
Only 7/20 P12 kinds have N03 implementation artifacts.
Missing: `checkpoint`, `collaboration_pattern`, `crew_template`, `domain_event`,
`process_manager`, `renewal_workflow`, `saga`, `schedule`, `state_machine`,
`team_charter`, `visual_workflow`, `workflow_node`, `workflow_primitive`.
P12 is the orchestration pillar — N03's builders cover it but N03 has not produced
canonical examples for 65% of the pillar's kinds.
**File target**: `N03_engineering/P12_orchestration/` — 13 missing kind artifacts.

**GAP 4 — bld_examples density floor failures (37 violations)** (MEDIUM)
`bld_examples` is the most density-violated ISO type (37/294 below 0.78 floor).
Examples are the primary source for F3 INJECT template matching. Low-density examples
reduce retrieval signal quality — builders trained on sparse examples produce shallow artifacts.
**File target**: 37 specific `bld_examples_*.md` files identified by `cex_doctor.py`.

**GAP 5 — cex_compile.py not kind-aware for reverse compilation** (MEDIUM)
The compiler targets `{claude-md, cursorrules, customgpt, mcp}` but does not route by
artifact `kind`. All 293 kinds compile through a single parse path. When a kind has
domain-specific serialization requirements (e.g., `openapi_spec` -> JSON, `validation_schema`
-> JSONSchema), the generic compiler produces flat YAML without schema validation.
**File target**: `_tools/cex_compile.py` — add kind-dispatch for P06 schema kinds.

---

## Recommendations

1. **F8 COLLABORATE sweep across all bld_instruction files**
   Path: `archetypes/builders/*/bld_instruction_*.md`
   Action: append standard F8 block — `signal_writer`, `cex_compile.py {path}`,
   `git add + git commit -m "[N03] {kind}: ..."` — to all 294 instruction files.
   Priority: CRITICAL — without this, 74% of builders cannot signal N07 on completion.

2. **Create 6 missing P06 schema artifacts in N03**
   Paths: `N03_engineering/P06_schema/sch_aggregate_root_n03.md`,
   `sch_data_contract_n03.md`, `sch_edit_format_n03.md`,
   `sch_event_schema_n03.md`, `sch_openapi_spec_n03.md`, `sch_value_object_n03.md`
   Action: produce each via 8F pipeline using the builder's existing bld_schema ISO as seed.
   Priority: HIGH — these are DDD/API core contracts missing from N03's domain.

3. **Create 13 missing P12 orchestration kind artifacts in N03**
   Path: `N03_engineering/P12_orchestration/{kind}_engineering.md` for each missing kind.
   Start with highest-value: `crew_template`, `state_machine`, `saga`, `process_manager`.
   Priority: HIGH — crew and orchestration patterns are core to WAVE8 protocol.

4. **Density remediation for top 37 bld_examples violations**
   Run: `python _tools/cex_doctor.py 2>&1 | grep "bld_examples.*density"` to get exact file list.
   Action: expand each to >= 0.85 density by adding golden + anti-examples.
   Priority: MEDIUM — retrieval quality degrades linearly with example sparsity.

5. **Add kind-dispatch to cex_compile.py for P06 schema kinds**
   Path: `_tools/cex_compile.py`
   Action: add `if kind in P06_SCHEMA_KINDS: compile_as_jsonschema(path)` branch.
   Priority: MEDIUM — `openapi_spec`, `validation_schema`, `data_contract` artifacts
   should emit machine-readable contracts, not flat YAML summaries.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[wave2_quality_report]] | related | 0.42 |
| [[bld_architecture_kind]] | downstream | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[kind-builder]] | downstream | 0.30 |
| [[system_health_20260413]] | related | 0.28 |
| [[bld_architecture_memory_architecture]] | downstream | 0.28 |
| [[polish_fixes_20260413]] | downstream | 0.27 |
| [[self_audit_newpc_2026_04_12]] | upstream | 0.27 |
| [[bld_knowledge_card_kind]] | upstream | 0.26 |
| [[bld_config_kind]] | downstream | 0.26 |
