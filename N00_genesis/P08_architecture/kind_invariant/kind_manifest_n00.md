---
id: n00_invariant_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Invariant -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, invariant, p08, n00, archetype, template]
density_score: 0.99
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An invariant is an operational law that is inviolable: a constraint that must always hold true regardless of which nucleus, model, or workflow is executing. Invariants are loaded at F1 CONSTRAIN to prevent builders from violating system-level rules. Examples include "N07 never builds artifacts directly" and "quality: null until peer-reviewed."

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `invariant` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable invariant name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| law | string | yes | The invariant stated as an imperative rule |
| scope | list | yes | Which nuclei or pillars this applies to (use [all] for global) |
| rationale | string | yes | Why this cannot be violated |
| enforcement | enum | yes | automated \| manual \| pre-commit \| f1-constrain |
| violation_consequence | string | no | What happens if the invariant is broken |

## When to use
- Encoding a system rule that must survive model updates, nucleus upgrades, and mission changes
- Constraining autonomous execution to prevent quality or safety regressions
- Formalizing the "4 Rules" from CLAUDE.md as machine-checkable artifacts

## Builder
`archetypes/builders/invariant-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind invariant --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: inv_n07_never_builds
kind: invariant
pillar: P08
nucleus: n07
title: "N07 never builds artifacts directly"
version: 1.0
quality: null
---
law: N07 MUST route all artifact construction to a specialist nucleus via dispatch.sh
scope: [n07]
rationale: Mixing orchestration with production collapses quality gates and creates circular dependencies
enforcement: f1-constrain
violation_consequence: Dispatch rejected; N07 self-audit triggered
```

## Related kinds
- `decision_record` (P08) -- records the reasoning that led to an invariant being established
- `naming_rule` (P08) -- naming invariants expressed as enforceable patterns
- `guardrail` (P11) -- runtime enforcement of invariants during agent execution
