---
id: bld_context_sources_process_manager
kind: knowledge_card
pillar: P12
title: "Process Manager Builder -- Context Sources"
version: 1.0.0
quality: 7.4
tags: [builder, process_manager, context]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_tools_kind
  - bld_instruction_kind
  - bld_collaboration_kind
  - bld_examples_handoff
  - kind-builder
  - bld_knowledge_card_kind
  - bld_output_template_builder
  - bld_collaboration_builder
  - bld_schema_kind
---
# Context Sources: process_manager
## Mandatory Loads (F3 INJECT)
| Source | Path | Purpose |
|--------|------|---------|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_process_manager.md | Primary definition |
| Schema | archetypes/builders/process-manager-builder/bld_schema_process_manager.md | Field constraints |
| Template | archetypes/builders/process-manager-builder/bld_output_template_process_manager.md | Structure |
| Examples | archetypes/builders/process-manager-builder/bld_examples_process_manager.md | Golden patterns |
| Pillar schema | N00_genesis/P12_orchestration/_schema.yaml | Pillar constraints |
## Related Kind KCs
| KC | Relationship |
|----|-------------|
| kc_workflow.md | sequential step execution (alternative pattern) |
| kc_domain_event.md | events that process_manager subscribes to |
| kc_dispatch_rule.md | keyword routing (simpler alternative) |
| kc_schedule.md | time-triggered orchestration |
## External References
| Source | Relevance |
|--------|----------|
| Hohpe & Woolf EIP (2003) | Process Manager pattern definition |
| Garcia-Molina Sagas (1987) | Compensation / long-running transactions |
| Richardson Microservices Patterns (2019) | Saga orchestrator implementation |

## Configuration Checklist

- Verify all required fields are present in frontmatter before saving
- Validate config values against schema constraints (type, range, enum)
- Cross-reference with related configs to avoid contradictions
- Test config loading in target runtime before committing

## Validation

```yaml
# Required config validation
fields_present: true
types_valid: true
ranges_checked: true
cross_refs_verified: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope {BUILDER}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.32 |
| [[bld_tools_kind]] | upstream | 0.29 |
| [[bld_instruction_kind]] | upstream | 0.29 |
| [[bld_collaboration_kind]] | related | 0.26 |
| [[bld_examples_handoff]] | upstream | 0.25 |
| [[kind-builder]] | upstream | 0.24 |
| [[bld_knowledge_card_kind]] | sibling | 0.24 |
| [[bld_output_template_builder]] | upstream | 0.21 |
| [[bld_collaboration_builder]] | related | 0.21 |
| [[bld_schema_kind]] | upstream | 0.21 |
