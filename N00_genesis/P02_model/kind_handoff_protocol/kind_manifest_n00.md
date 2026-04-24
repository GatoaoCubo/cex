---
id: n00_handoff_protocol_manifest
kind: knowledge_card
8f: F3_inject
pillar: P02
nucleus: n00
title: "Handoff Protocol -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, handoff_protocol, p02, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_crew_template
  - handoff-protocol-builder
  - bld_schema_handoff_protocol
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_usage_report
  - bld_schema_nucleus_def
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_handoff
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Handoff Protocol defines the agent-to-agent transfer protocol for passing work between nuclei in a multi-agent mission. It specifies the handoff document format, required fields, signal mechanism, and acceptance criteria. Well-defined handoff protocols ensure receiving nuclei have all context needed to start work without re-querying the orchestrator.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `handoff_protocol` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Protocol name and scope |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| from_nucleus | string | yes | Sending nucleus identifier |
| to_nucleus | string | yes | Receiving nucleus identifier |
| handoff_path | string | yes | File path pattern for handoff documents |
| required_fields | list | yes | Mandatory fields in handoff document |
| signal_mechanism | enum | yes | file\|api\|a2a-task\|git-commit |
| acceptance_criteria | list | yes | Conditions receiving nucleus checks on start |

## When to use
- When defining how N07 passes tasks to operational nuclei
- When establishing a2a-task signaling for crew handoffs
- When formalizing inter-nucleus communication contracts

## Builder
`archetypes/builders/handoff_protocol-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind handoff_protocol --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- N07 orchestrator and receiving nuclei
- `{{DOMAIN_CONTEXT}}` -- mission type and handoff complexity

## Example (minimal)
```yaml
---
id: handoff_protocol_n07_to_n03
kind: handoff_protocol
pillar: P02
nucleus: n07
title: "N07 to N03 Build Handoff Protocol"
version: 1.0
quality: null
---
from_nucleus: n07
to_nucleus: n03
handoff_path: ".cex/runtime/handoffs/{MISSION}_n03.md"
required_fields: [mission, task, artifacts_expected, context, decisions]
signal_mechanism: file
acceptance_criteria:
  - handoff file exists at path
  - decisions section populated
  - at least 1 expected artifact listed
```

## Related kinds
- `nucleus_def` (P02) -- formal nucleus definition including handoff rules
- `agents_md` (P02) -- project manifest declaring handoff protocols
- `role_assignment` (P02) -- crew role binding using handoff protocols

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_crew_template]] | downstream | 0.44 |
| [[handoff-protocol-builder]] | related | 0.44 |
| [[bld_schema_handoff_protocol]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.42 |
| [[bld_schema_nucleus_def]] | downstream | 0.42 |
| [[bld_schema_dataset_card]] | downstream | 0.42 |
| [[bld_schema_quickstart_guide]] | downstream | 0.41 |
| [[bld_schema_handoff]] | downstream | 0.41 |
