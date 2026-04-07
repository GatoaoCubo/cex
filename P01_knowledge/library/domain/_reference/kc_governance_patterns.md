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
