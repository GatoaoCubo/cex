---
id: bld_context_sources_deployment_manifest
kind: knowledge_card
pillar: P01
title: "Context Sources: deployment_manifest Builder"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: 7.8
tags: [context_sources, deployment_manifest, P09]
llm_function: CONSTRAIN
tldr: "Ordered list of context sources to inject at F3 INJECT for deployment_manifest builds."
density_score: null
related:
  - bld_architecture_kind
  - bld_tools_kind
  - bld_collaboration_kind
  - kind-builder
  - bld_collaboration_builder
  - bld_examples_handoff
  - bld_instruction_kind
  - bld_manifest_memory_type
  - bld_knowledge_card_builder
  - bld_knowledge_card_kind
---

# Context Sources: deployment_manifest Builder

## Injection Order (F3 INJECT)

| Priority | Source | Path | Why |
|----------|--------|------|-----|
| 1 | Schema | archetypes/builders/deployment-manifest-builder/bld_schema_deployment_manifest.md | Field names + constraints |
| 2 | Knowledge Card | N00_genesis/P01_knowledge/library/kind/kc_deployment_manifest.md | Domain definition |
| 3 | Examples | archetypes/builders/deployment-manifest-builder/bld_examples_deployment_manifest.md | Golden reference |
| 4 | Quality Gate | archetypes/builders/deployment-manifest-builder/bld_quality_gate_deployment_manifest.md | Validation rules |
| 5 | env_config KC | N00_genesis/P01_knowledge/library/kind/kc_env_config.md | Config override context |
| 6 | canary_config KC | N00_genesis/P01_knowledge/library/kind/kc_canary_config.md | Boundary clarification |
| 7 | Memory | archetypes/builders/deployment-manifest-builder/bld_memory_deployment_manifest.md | Recalled corrections |

## Similarity Scan (F5 CALL)
Run retriever against: `N0X_*/P09_config/p09_dm_*.md` to find existing manifests for the same domain.

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
| [[bld_collaboration_kind]] | downstream | 0.32 |
| [[kind-builder]] | downstream | 0.31 |
| [[bld_collaboration_builder]] | downstream | 0.31 |
| [[bld_examples_handoff]] | downstream | 0.30 |
| [[bld_instruction_kind]] | downstream | 0.29 |
| [[bld_manifest_memory_type]] | downstream | 0.28 |
| [[bld_knowledge_card_builder]] | sibling | 0.25 |
| [[bld_knowledge_card_kind]] | sibling | 0.25 |
