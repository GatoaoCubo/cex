---
quality: 7.9
id: bld_architecture_default
kind: builder_default
pillar: P08
source: shared
title: "Architecture Default: Component Map (kind -> pillar -> nucleus)"
llm_function: CONSTRAIN
version: 1.1.0
quality: 7.7
tags: [architecture, component_map, P08, shared, default]
related:
  - bld_schema_kind
  - bld_architecture_kind
  - bld_knowledge_card_kind
  - bld_architecture_memory_architecture
  - p06_schema_taxonomy
  - bld_architecture_dataset_card
  - spec_mission_100pct_coverage
  - bld_collaboration_kind
  - bld_architecture_agent_name_service_record
  - bld_instruction_kind
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-22"
---

# P08 Architecture — Default Component Map

## Kind -> Pillar -> Nucleus Routing

| Pillar | Domain | Primary Nucleus | Example Kinds |
|--------|--------|-----------------|---------------|
| P01 Knowledge | storage, retrieval | N04 | knowledge_card, chunk_strategy, embedding_config |
| P02 Model | agent definitions | N03 | agent, model_provider, boot_config |
| P03 Prompt | templates, chains | N03 | prompt_template, system_prompt, chain |
| P04 Tools | external capabilities | N05 | cli_tool, browser_tool, mcp_server |
| P05 Output | production artifacts | N03 | landing_page, formatter, parser |
| P06 Schema | data contracts | N03 | input_schema, type_def, interface |
| P07 Evaluation | quality, scoring | N05 | quality_gate, scoring_rubric, benchmark |
| P08 Architecture | system structure | N03 | agent_card, component_map, decision_record |
| P09 Config | runtime settings | N05 | env_config, rate_limit_config, secret_config |
| P10 Memory | state, context | N04 | knowledge_index, memory_scope, entity_memory |
| P11 Feedback | learning, correction | N03 | bugloop, learning_record, guardrail |
| P12 Orchestration | workflows, dispatch | N07 | workflow, dispatch_rule, schedule |

## 8F -> Pillar Alignment

| 8F Function | Primary Pillar | Secondary Pillar |
|-------------|----------------|-----------------|
| F1 CONSTRAIN | P06 Schema | P09 Config |
| F2 BECOME | P02 Model | P03 Prompt |
| F3 INJECT | P01 Knowledge | P10 Memory |
| F4 REASON | P08 Architecture | -- |
| F5 CALL | P04 Tools | -- |
| F6 PRODUCE | P05 Output | P03 Prompt |
| F7 GOVERN | P07 Evaluation | P11 Feedback |
| F8 COLLABORATE | P12 Orchestration | -- |

## Builder ISOs -> Pillars (12P fractal)

Each builder ISO corresponds to one pillar:

| ISO File | Pillar | 8F Stage |
|----------|--------|---------|
| `bld_knowledge_{kind}.md` | P01 | F3 INJECT |
| `bld_model_{kind}.md` | P02 | F2 BECOME |
| `bld_prompt_{kind}.md` | P03 | F6 PRODUCE |
| `bld_tools_{kind}.md` | P04 | F5 CALL |
| `bld_output_{kind}.md` | P05 | F6 PRODUCE |
| `bld_schema_{kind}.md` | P06 | F1 CONSTRAIN |
| `bld_eval_{kind}.md` | P07 | F7 GOVERN |
| `bld_architecture_{kind}.md` | P08 | F4 REASON |
| `bld_config_{kind}.md` | P09 | F1 CONSTRAIN |
| `bld_memory_{kind}.md` | P10 | F3 INJECT |
| `bld_feedback_{kind}.md` | P11 | F7 GOVERN |
| `bld_orchestration_{kind}.md` | P12 | F8 COLLABORATE |

## When to Override

Override `bld_architecture_{kind}.md` when the kind has non-standard:
- Cross-nucleus dependencies (kind produced by N03 but consumed by N01)
- Multi-pillar artifacts (spans P01+P02 like an agent with built-in KC)
- External system integrations (kind wraps an external API or platform)

## Architecture Checklist

- Verify component inventory is complete (no orphans)
- Validate dependency graph has no cycles
- Cross-reference with boundary table for scope correctness
- Test layer map against actual codebase structure

## Architecture Pattern

```yaml
# Architecture validation
components: inventoried
dependencies: acyclic
boundaries: defined
layers: mapped
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope architecture
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_kind]] | upstream | 0.38 |
| [[bld_architecture_kind]] | related | 0.35 |
| [[bld_knowledge_card_kind]] | upstream | 0.34 |
| [[bld_architecture_memory_architecture]] | related | 0.33 |
| [[p06_schema_taxonomy]] | upstream | 0.32 |
| [[bld_architecture_dataset_card]] | related | 0.31 |
| [[spec_mission_100pct_coverage]] | related | 0.31 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[bld_architecture_agent_name_service_record]] | related | 0.29 |
| [[bld_instruction_kind]] | upstream | 0.29 |
