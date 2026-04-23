---
id: bld_context_sources_bounded_context
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.3
tags: [bounded_context, context, rag]
title: "Context Sources: bounded_context"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_kind
  - bld_instruction_kind
  - kc_model_context_protocol
  - bld_tools_kind
  - bld_collaboration_context_doc
  - bld_collaboration_citation
  - output_sdk_validation_knowledge_audit
  - bld_tools_context_window_config
  - spec_context_assembly
  - bld_collaboration_kind
---
# Context Sources: bounded_context
## Mandatory Sources (load at F3 INJECT)
| Source | Path | Why |
|--------|------|-----|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_bounded_context.md | Definition + boundary |
| Schema | archetypes/builders/bounded-context-builder/bld_schema_bounded_context.md | Required fields |
| Examples | archetypes/builders/bounded-context-builder/bld_examples_bounded_context.md | Golden patterns |

## Optional Sources (load if relevant)
| Source | Path | When to Load |
|--------|------|-------------|
| domain_vocabulary KC | N00_genesis/P01_knowledge/library/kind/kc_domain_vocabulary.md | Vocabulary governance |
| domain_event KC | N00_genesis/P01_knowledge/library/kind/kc_domain_event.md | Published events |
| data_contract KC | N00_genesis/P01_knowledge/library/kind/kc_data_contract.md | Integration contracts |
| Nucleus defs | N0X_*/P08_architecture/nucleus_def_n0X.md | BC maps to nucleus |

## Search Queries for Retrieval
- "DDD bounded context context map integration pattern"
- "Anti-Corruption Layer Open Host Service Conformist"
- "domain model boundary team ownership aggregate"
- "Evans context mapping upstream downstream"

## Anti-Sources (do NOT confuse with)
- component_map (deployment topology, not semantic boundary)
- namespace (code organization, not domain model)
- agent_card (capability definition, not domain boundary)

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
| [[bld_architecture_kind]] | upstream | 0.27 |
| [[bld_instruction_kind]] | upstream | 0.25 |
| [[kc_model_context_protocol]] | upstream | 0.24 |
| [[bld_tools_kind]] | upstream | 0.22 |
| [[bld_collaboration_context_doc]] | downstream | 0.21 |
| [[bld_collaboration_citation]] | downstream | 0.20 |
| [[output_sdk_validation_knowledge_audit]] | upstream | 0.20 |
| [[bld_tools_context_window_config]] | upstream | 0.20 |
| [[spec_context_assembly]] | related | 0.20 |
| [[bld_collaboration_kind]] | downstream | 0.20 |
