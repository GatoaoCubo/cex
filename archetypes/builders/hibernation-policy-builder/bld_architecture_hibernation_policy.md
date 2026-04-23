---
kind: decision_record
id: bld_architecture_hibernation_policy
pillar: P08
llm_function: CONSTRAIN
purpose: F1 CONSTRAIN structural decisions for hibernation_policy
quality: 8.8
title: "Architecture: hibernation_policy"
version: "1.0.0"
author: n03_engineering
tags: [hibernation_policy, builder, architecture]
tldr: "F1 CONSTRAIN structural decisions for hibernation_policy"
domain: "hibernation_policy construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p03_ins_vector_store
  - bld_collaboration_session_backend
  - spec_seed_words
  - bld_architecture_webinar_script
  - bld_architecture_dataset_card
  - bld_instruction_kind
  - p03_sp_session_backend_builder
  - bld_tools_session_backend
  - bld_instruction_session_backend
  - p01_kc_8f_pipeline
---

## Structural Decisions

### D1: Pillar placement in P09 (not P11)
Hibernation is a configuration artifact (WHEN to sleep, HOW to persist), not a feedback artifact. P11 handles learning and correction loops. P09 is the correct home for runtime configuration including idle-state policy.

### D2: llm_function = GOVERN
The hibernation_policy expresses RULES that govern workload lifecycle -- it does not produce content (PRODUCE), transform data (CALL), or inject context (INJECT). GOVERN is the correct function for policy artifacts that enforce operating constraints.

### D3: max_bytes = 2048
The policy is intentionally compact: idle trigger (2 fields), wake conditions (list), state persistence (3 fields), SLA (2 fields). A 2048-byte ceiling prevents over-engineering while accommodating backend-specific notes.

### D4: target_backend as enum (not free-form string)
Constraining to daytona|modal|singularity|generic enables automated routing in N07: the orchestrator can check `target_backend` to know which backend API to call for hibernate/wake operations. Free-form strings would require NLP parsing.

### D5: sibling relationship with terminal_backend (shared backend slug)
Both `p09_tb_modal` and `p09_hp_modal` describe the Modal backend from different angles. The shared naming convention makes the relationship discoverable by tooling without requiring an explicit foreign-key field.

## File Layout
```
N00_genesis/P09_config/
  kind_hibernation_policy/
    kind_manifest_n00.md       -- canonical manifest
  tpl_hibernation_policy.md    -- instantiation template

N00_genesis/P01_knowledge/library/kind/
  kc_hibernation_policy.md     -- knowledge card

archetypes/builders/hibernation-policy-builder/
  bld_manifest_hibernation_policy.md
  bld_instruction_hibernation_policy.md
  bld_system_prompt_hibernation_policy.md
  bld_schema_hibernation_policy.md
  bld_examples_hibernation_policy.md
  bld_architecture_hibernation_policy.md
  bld_config_hibernation_policy.md
  bld_knowledge_card_hibernation_policy.md
  bld_memory_hibernation_policy.md
  bld_output_template_hibernation_policy.md
  bld_quality_gate_hibernation_policy.md
  bld_tools_hibernation_policy.md
  bld_collaboration_hibernation_policy.md

.claude/agents/
  hibernation-policy-builder.md  -- sub-agent stub
```

## Dependency Graph
```
hibernation_policy
  |-- depends on: terminal_backend (same backend slug)
  |-- complements: cost_budget (spend cap)
  |-- distinct from: runtime_rule (active timeout)
  |-- distinct from: rate_limit_config (throughput)
  |-- referenced by: N07 orchestrator routing logic
```

## 8F Anchor Points
| 8F Step | hibernation_policy specific action |
|---------|-----------------------------------|
| F1 CONSTRAIN | Resolve backend from user intent; check backend support matrix |
| F2 BECOME | Load this manifest + instruction ISOs |
| F3 INJECT | Load kc_hibernation_policy.md + sibling terminal_backend example |
| F4 REASON | Determine idle trigger type based on workload pattern |
| F5 CALL | No external tool calls required (pure config artifact) |
| F6 PRODUCE | Write YAML frontmatter + 4-table body |
| F7 GOVERN | Validate H01-H05 gates; check threshold >= 0 and wake_on non-empty |
| F8 COLLABORATE | Save to environments/; compile; commit with [N05] tag |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_vector_store]] | upstream | 0.25 |
| [[bld_collaboration_session_backend]] | downstream | 0.24 |
| [[spec_seed_words]] | upstream | 0.23 |
| [[bld_architecture_webinar_script]] | related | 0.22 |
| [[bld_architecture_dataset_card]] | related | 0.21 |
| [[bld_instruction_kind]] | upstream | 0.21 |
| [[p03_sp_session_backend_builder]] | upstream | 0.21 |
| [[bld_tools_session_backend]] | upstream | 0.20 |
| [[bld_instruction_session_backend]] | upstream | 0.20 |
| [[p01_kc_8f_pipeline]] | upstream | 0.20 |
