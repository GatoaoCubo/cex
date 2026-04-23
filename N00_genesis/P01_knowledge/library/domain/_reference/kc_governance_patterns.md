---
id: p01_kc_governance_patterns
kind: knowledge_card
type: domain
pillar: P01
title: Governance -- Laws, Component Maps, Diagrams, Decision Records
version: 1.0.0
created: '2026-03-29'
author: orchestrator
domain: governance
origin: manual
quality: 9.0
tags:
- governance
- adr
- c4-diagram
- law
- architecture
tldr: 'Governance-as-code: architectural laws, C4 diagrams, component maps, ADR decision records'
when_to_use: Documenting decisions, mapping components, enforcing governance
feeds_kinds:
- law
- component_map
- diagram
- decision_record
density_score: 0.85
updated: "2026-04-07"
related:
  - p01_kc_input_hydration
  - p01_kc_qa_validation
  - p01_kc_schema_validation
  - p01_kc_context_scoping
  - p01_kc_spawn_patterns
  - p01_kc_output_formatting
  - p01_kc_workflow_orchestration
  - p01_kc_pattern_extraction
  - p01_kc_test_automation
  - p01_kc_eval_testing
---

## Quick Reference
| Pattern | Source | CEX Kind |
|---------|--------|----------|
| ADR (Nygard 2011) | Industry | decision_record |
| C4 Diagrams | Simon Brown | diagram, component_map |
| Governance-as-Code | Platform Eng | law |

## Key Concepts
- **Law**: prescriptive rule that MUST be followed (enforced constraint)
- **Pattern**: reusable solution to recurring problem (recommended)
- **Component Map**: map of system components and relationships
- **Diagram**: architectural visualization (C4 levels)
- **Decision Record**: ADR with context, options, decision, consequences

## Patterns
| Trigger | Action |
|---------|--------|
| Architectural choice | Write decision_record |
| New component | Update component_map |
| Recurring solution | Extract pattern |
| Non-negotiable rule | Encode as law |

## Anti-Patterns
- Decisions without records (tribal knowledge)
- Diagrams without updates (stale maps)
- Laws without enforcement (governance theater)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_governance_patterns`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_governance_patterns`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_input_hydration]] | sibling | 0.35 |
| [[p01_kc_qa_validation]] | sibling | 0.35 |
| [[p01_kc_schema_validation]] | sibling | 0.34 |
| [[p01_kc_context_scoping]] | sibling | 0.34 |
| [[p01_kc_spawn_patterns]] | sibling | 0.33 |
| [[p01_kc_output_formatting]] | sibling | 0.33 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.32 |
| [[p01_kc_pattern_extraction]] | sibling | 0.31 |
| [[p01_kc_test_automation]] | sibling | 0.30 |
| [[p01_kc_eval_testing]] | sibling | 0.28 |
