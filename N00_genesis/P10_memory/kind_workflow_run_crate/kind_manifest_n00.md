---
id: n00_workflow_run_crate_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Workflow Run Crate -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, workflow_run_crate, p10, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A workflow_run_crate is an RO-Crate 1.2 Workflow Run Crate that packages the complete provenance of a scientific or enterprise workflow execution: inputs, outputs, tool versions, parameters, and timing. It enables reproducibility by providing a self-describing, FAIR-compliant archive of exactly what ran and what it produced.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `workflow_run_crate` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| ro_crate_version | string | yes | RO-Crate spec version (e.g. "1.2") |
| workflow_id | string | yes | Reference to the workflow artifact that ran |
| run_id | string | yes | Unique execution identifier |
| inputs | array | yes | List of input files/parameters with checksums |
| outputs | array | yes | List of output files with checksums and locations |
| tools_used | array | yes | Tool names, versions, and container references |
| started_at | datetime | yes | Execution start time |
| ended_at | datetime | yes | Execution end time |
| exit_code | integer | yes | Workflow exit code (0 = success) |

## When to use
- When archiving a completed CEX mission for scientific reproducibility
- When building compliance artifacts that require full workflow execution provenance
- When sharing a workflow execution record with external collaborators or auditors

## Builder
`archetypes/builders/workflow_run_crate-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind workflow_run_crate --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: wrc_mission_fractal_fill_w2
kind: workflow_run_crate
pillar: P10
nucleus: n07
title: "Example Workflow Run Crate"
version: 1.0
quality: null
---
# RO-Crate 1.2: FRACTAL_FILL Wave 2
ro_crate_version: "1.2"
workflow_id: wf_fractal_fill
run_id: run_20260415_w2
exit_code: 0
outputs: [{file: "49 artifacts", checksum: "sha256:..."}]
```

## Related kinds
- `workflow` (P12) -- the workflow definition this crate records execution of
- `agent_grounding_record` (P10) -- per-inference provenance nested within a run
- `audit_log` (P11) -- compliance audit trail that references workflow run crates
