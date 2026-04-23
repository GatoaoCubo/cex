---
id: bld_context_sources_domain_event
kind: rag_source
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
quality: 8.1
tags: [domain_event, context, rag]
title: "Context Sources: domain_event"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p01_kc_signal
  - bld_instruction_hook
  - bld_collaboration_hook
  - bld_architecture_kind
  - bld_tools_kind
  - p08_pat_nucleus_fractal
  - bld_architecture_hook
  - bld_instruction_kind
  - bld_knowledge_card_hook_config
  - bld_collaboration_schedule
---
# Context Sources: domain_event
## Mandatory Sources (load at F3 INJECT)
| Source | Path | Why |
|--------|------|-----|
| Kind KC | N00_genesis/P01_knowledge/library/kind/kc_domain_event.md | Definition + boundary |
| Schema | archetypes/builders/domain-event-builder/bld_schema_domain_event.md | Required fields |
| Examples | archetypes/builders/domain-event-builder/bld_examples_domain_event.md | Golden patterns |
| Bounded context KC | N00_genesis/P01_knowledge/library/kind/kc_bounded_context.md | Ownership rules |

## Optional Sources (load if available)
| Source | Path | When to Load |
|--------|------|-------------|
| Existing domain events | {nucleus}/P12_*/de_*.md | Reuse + consistency check |
| Data contract | {nucleus}/P06_*/dc_*.md | If event crosses BC boundary |
| Workflow | {nucleus}/P12_*/wf_*.md | If event triggers workflow |

## Search Queries for Retrieval
- "domain event aggregate root past tense"
- "DDD event sourcing immutable record"
- "bounded context event catalog"
- "causation correlation id tracing"

## Anti-Sources (do NOT confuse with)
- signal artifacts (P11, system telemetry)
- audit_log artifacts (P11, compliance)
- workflow triggers (P12, process control)

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
| [[p01_kc_signal]] | downstream | 0.29 |
| [[bld_instruction_hook]] | upstream | 0.25 |
| [[bld_collaboration_hook]] | downstream | 0.24 |
| [[bld_architecture_kind]] | upstream | 0.23 |
| [[bld_tools_kind]] | upstream | 0.22 |
| [[p08_pat_nucleus_fractal]] | upstream | 0.21 |
| [[bld_architecture_hook]] | upstream | 0.20 |
| [[bld_instruction_kind]] | upstream | 0.20 |
| [[bld_knowledge_card_hook_config]] | upstream | 0.19 |
| [[bld_collaboration_schedule]] | downstream | 0.19 |
