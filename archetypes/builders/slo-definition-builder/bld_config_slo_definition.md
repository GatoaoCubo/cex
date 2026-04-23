---
id: bld_context_sources_slo_definition
kind: knowledge_card
pillar: P01
title: "Context Sources: slo_definition Builder"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: 7.8
tags: [context_sources, slo_definition, P09]
llm_function: CONSTRAIN
tldr: "Ordered context sources for F3 INJECT in slo_definition builds."
density_score: null
related:
  - bld_architecture_kind
  - bld_tools_kind
  - bld_examples_handoff
  - bld_collaboration_kind
  - bld_collaboration_builder
  - kind-builder
  - bld_instruction_kind
  - bld_collaboration_knowledge_card
  - bld_knowledge_card_builder
  - bld_collaboration_context_doc
---

# Context Sources: slo_definition Builder

## Injection Order (F3 INJECT)
| Priority | Source | Path | Why |
|----------|--------|------|-----|
| 1 | Schema | archetypes/builders/slo-definition-builder/bld_schema_slo_definition.md | Field constraints |
| 2 | Knowledge Card | N00_genesis/P01_knowledge/library/kind/kc_slo_definition.md | Domain knowledge + error budget math |
| 3 | Examples | archetypes/builders/slo-definition-builder/bld_examples_slo_definition.md | Golden reference |
| 4 | Quality Gate | archetypes/builders/slo-definition-builder/bld_quality_gate_slo_definition.md | Validation rules |
| 5 | trace_config KC | N00_genesis/P01_knowledge/library/kind/kc_trace_config.md | Observability context |
| 6 | Memory | archetypes/builders/slo-definition-builder/bld_memory_slo_definition.md | Recalled corrections |

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
| [[bld_architecture_kind]] | downstream | 0.38 |
| [[bld_tools_kind]] | downstream | 0.38 |
| [[bld_examples_handoff]] | downstream | 0.33 |
| [[bld_collaboration_kind]] | downstream | 0.32 |
| [[bld_collaboration_builder]] | downstream | 0.32 |
| [[kind-builder]] | downstream | 0.30 |
| [[bld_instruction_kind]] | downstream | 0.28 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.27 |
| [[bld_knowledge_card_builder]] | sibling | 0.25 |
| [[bld_collaboration_context_doc]] | downstream | 0.24 |
