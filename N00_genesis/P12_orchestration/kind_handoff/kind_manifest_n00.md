---
id: n00_handoff_manifest
kind: knowledge_card
pillar: P12
nucleus: n00
title: "Handoff -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, handoff, p12, n00, archetype, template]
density_score: 0.99
---

<!-- 8F: F1=knowledge_card P12 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A handoff is the task instruction and context package that N07 writes to transfer work to a nucleus. It contains the task description, pre-loaded artifact references, expected outputs, decision manifest reference, and commit format specification. The handoff is the contract between the orchestrator and the receiving nucleus -- everything the nucleus needs, nothing it should have to discover.

## Pillar
P12 -- orchestration

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `handoff` |
| pillar | string | yes | Always `P12` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_nucleus | string | yes | Nucleus receiving this handoff |
| mission | string | yes | Mission or wave name this handoff belongs to |
| task_description | string | yes | Clear, deep task description (see dispatch-depth rule) |
| artifact_references | array | yes | Pre-loaded artifact paths the nucleus must read |
| expected_outputs | array | yes | Exact files to produce with paths and kinds |
| decision_manifest_ref | string | yes | Path to decision_manifest.yaml |
| commit_format | string | yes | Required git commit message format |
| signal_on_complete | string | yes | Signal type to emit on completion |

## When to use
- Every time N07 dispatches a task to a nucleus (mandatory, no exceptions)
- When transferring work between nuclei in a crew sequential pattern
- When creating the n0X_task.md file read by boot scripts

## Builder
`archetypes/builders/handoff-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind handoff --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: handoff_n03_agent_card_build
kind: handoff
pillar: P12
nucleus: n07
title: "Example Handoff"
version: 1.0
quality: null
---
# Handoff: N03 Build Agent Cards
target_nucleus: n03
mission: FRACTAL_FILL_W3
task_description: "Build agent_card for N05. Read all 34 N05 artifacts first."
expected_outputs: [{file: "N05_operations/P08_architecture/agent_card_n05.md", kind: agent_card}]
decision_manifest_ref: ".cex/runtime/decisions/decision_manifest.yaml"
signal_on_complete: complete
```

## Related kinds
- `dispatch_rule` (P12) -- rules that determine which nucleus receives this handoff
- `signal` (P12) -- signal emitted by nucleus upon completing this handoff
- `checkpoint` (P12) -- state snapshot taken before handoff to enable rollback
