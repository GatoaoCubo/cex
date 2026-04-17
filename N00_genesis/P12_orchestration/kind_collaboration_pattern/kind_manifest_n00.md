---
id: n00_collaboration_pattern_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Collaboration Pattern -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, collaboration_pattern, p12, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A collaboration_pattern defines a reusable multi-agent coordination topology -- the structural template for how agents communicate, share state, and coordinate decisions. It is the design pattern library for multi-agent systems, providing named topologies (sequential, hierarchical, consensus, fan-out/gather) that crew_template and dag artifacts instantiate.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `collaboration_pattern` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| pattern_name | string | yes | Named topology (e.g. sequential, hierarchical, consensus, fan_out_gather) |
| participant_roles | array | yes | Role types required by this pattern |
| communication_protocol | enum | yes | handoff \| signal \| shared_state \| direct_call |
| coordination_overhead | enum | yes | low \| medium \| high |
| suitable_for | array | yes | Scenarios where this pattern excels |
| anti_patterns | array | yes | Scenarios where this pattern should NOT be used |

## When to use
- When designing a new crew and selecting the appropriate coordination topology
- When documenting why a particular multi-agent communication style was chosen
- When training new nucleus operators on available coordination patterns

## Builder
`archetypes/builders/collaboration_pattern-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind collaboration_pattern --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cp_sequential_handoff
kind: collaboration_pattern
pillar: P12
nucleus: n07
title: "Example Collaboration Pattern"
version: 1.0
quality: null
---
# Collaboration Pattern: Sequential Handoff
pattern_name: sequential
communication_protocol: handoff
coordination_overhead: low
suitable_for: ["pipeline workflows where each step depends on prior", "4-role crew builds"]
anti_patterns: ["independent parallel tasks (use grid)", "consensus needed (use consensus pattern)"]
```

## Related kinds
- `crew_template` (P12) -- crew blueprint that instantiates a collaboration pattern
- `handoff` (P12) -- communication artifact used by sequential/hierarchical patterns
- `dag` (P12) -- dependency graph encoding parallel collaboration topology
