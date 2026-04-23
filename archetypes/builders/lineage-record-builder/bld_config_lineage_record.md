---
id: bld_context_sources_lineage_record
kind: knowledge_card
pillar: P01
title: "Context Sources: lineage_record Builder"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: 7.8
tags: [context_sources, lineage_record, P01]
llm_function: CONSTRAIN
tldr: "Ordered context sources for F3 INJECT in lineage_record builds."
density_score: null
related:
  - bld_tools_kind
  - bld_architecture_kind
  - bld_examples_handoff
  - bld_collaboration_builder
  - bld_collaboration_kind
  - kind-builder
  - bld_instruction_kind
  - bld_knowledge_card_builder
  - bld_collaboration_citation
  - p10_lr_kind_builder
---

# Context Sources: lineage_record Builder

## Injection Order (F3 INJECT)
| Priority | Source | Path | Why |
|----------|--------|------|-----|
| 1 | Schema | archetypes/builders/lineage-record-builder/bld_schema_lineage_record.md | Field constraints |
| 2 | Knowledge Card | N00_genesis/P01_knowledge/library/kind/kc_lineage_record.md | PROV-O vocabulary |
| 3 | Examples | archetypes/builders/lineage-record-builder/bld_examples_lineage_record.md | Golden reference |
| 4 | Quality Gate | archetypes/builders/lineage-record-builder/bld_quality_gate_lineage_record.md | Validation rules |
| 5 | citation KC | N00_genesis/P01_knowledge/library/kind/kc_citation.md | Boundary clarification |
| 6 | Memory | archetypes/builders/lineage-record-builder/bld_memory_lineage_record.md | Recalled corrections |

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
| [[bld_tools_kind]] | downstream | 0.39 |
| [[bld_architecture_kind]] | downstream | 0.37 |
| [[bld_examples_handoff]] | downstream | 0.34 |
| [[bld_collaboration_builder]] | downstream | 0.32 |
| [[bld_collaboration_kind]] | downstream | 0.32 |
| [[kind-builder]] | downstream | 0.30 |
| [[bld_instruction_kind]] | downstream | 0.28 |
| [[bld_knowledge_card_builder]] | sibling | 0.25 |
| [[bld_collaboration_citation]] | downstream | 0.24 |
| [[p10_lr_kind_builder]] | downstream | 0.24 |
