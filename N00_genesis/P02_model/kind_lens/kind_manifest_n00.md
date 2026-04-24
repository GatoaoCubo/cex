---
id: n00_lens_manifest
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "Lens -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, lens, p02, n00, archetype, template]
density_score: 0.0
related:
  - bld_schema_lens
  - lens-builder
  - bld_architecture_lens
  - p03_ins_lens
  - p03_sp_lens_builder
  - p01_kc_lens
  - bld_collaboration_lens
  - p11_qg_lens
  - bld_knowledge_card_lens
  - bld_memory_lens
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Lens defines a specialized perspective through which an agent analyzes a domain, problem, or dataset. A lens filters perception and reasoning toward a specific analytical angle (e.g., revenue optimization, security risk, user experience). Injected via F3 INJECT, a lens shapes how an agent interprets ambiguous input without changing its core identity.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `lens` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Lens name and analytical angle |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus |
| perspective | string | yes | Core analytical angle this lens applies |
| filters | list | yes | What this lens amplifies or attenuates |
| activation_trigger | string | yes | Condition that activates this lens |
| sin_lens | string | yes | Cultural DNA (sin) this lens channels |

## When to use
- When an agent needs to analyze data from a specific vantage point
- When creating role-specific analytical perspectives for crew members
- When specializing a general nucleus for a domain task

## Builder
`archetypes/builders/lens-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind lens --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- the sin that shapes this analytical perspective
- `{{TARGET_AUDIENCE}}` -- agent or analyst applying the lens
- `{{DOMAIN_CONTEXT}}` -- analytical domain and problem space

## Example (minimal)
```yaml
---
id: lens_n06_revenue_optimization
kind: lens
pillar: P02
nucleus: n06
title: "Revenue Optimization Lens"
version: 1.0
quality: null
---
nucleus: n06
perspective: Every feature, decision, and artifact is evaluated through revenue impact
filters:
  amplifies: [conversion paths, upsell opportunities, pricing leverage]
  attenuates: [aesthetic concerns without revenue link]
activation_trigger: Any task involving pricing, packaging, or monetization
sin_lens: Strategic Greed
```

## Related kinds
- `agent_profile` (P02) -- persona that applies this lens
- `mental_model` (P02) -- reasoning framework the lens shapes
- `nucleus_def` (P02) -- nucleus definition including lens specifications

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_lens]] | downstream | 0.63 |
| [[lens-builder]] | related | 0.56 |
| [[bld_architecture_lens]] | downstream | 0.54 |
| [[p03_ins_lens]] | downstream | 0.52 |
| [[p03_sp_lens_builder]] | downstream | 0.50 |
| [[p01_kc_lens]] | sibling | 0.48 |
| [[bld_collaboration_lens]] | related | 0.47 |
| [[p11_qg_lens]] | downstream | 0.44 |
| [[bld_knowledge_card_lens]] | sibling | 0.44 |
| [[bld_memory_lens]] | downstream | 0.40 |
