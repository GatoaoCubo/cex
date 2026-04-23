---
quality: 8.2
quality: 7.7
id: bld_output_template_lineage_record
kind: knowledge_card
pillar: P05
title: "Output Template: lineage_record"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
tags: [output_template, lineage_record, P01]
llm_function: PRODUCE
tldr: "Canonical output template for lineage_record artifacts."
density_score: null
related:
  - bld_output_template_dataset_card
  - bld_collaboration_prompt_template
  - role-assignment-builder
  - bld_output_template_prompt_template
  - bld_output_template_memory_type
  - bld_output_template_input_schema
  - bld_output_template_kind
  - bld_examples_role_assignment
  - bld_output_template_type_def
  - bld_output_template_capability_registry
---

# Output Template: lineage_record

## Frontmatter Template
```yaml
---
id: p01_lr_{{name_slug}}
kind: lineage_record
pillar: P01
version: 1.0.0
target_artifact: "{{target_artifact_id}}"
sources_count: {{sources_count}}
activities_count: {{activities_count}}
derivation_type: {{derivation_type}}
domain: "{{domain}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: null
tags: [lineage_record, {{domain}}]
tldr: "Provenance chain for {{target_artifact_id}}: {{sources_count}} sources, {{activities_count}} activities"
---
```

## Body Template
```markdown
# Lineage: {{target_artifact_id}}

## Entities
| ID | Type | Location | Retrieved |
|----|------|----------|-----------|
| {{entity_id}} | {{type}} | {{path_or_url}} | {{iso_timestamp}} |

## Activities
| ID | Label | Used | Generated | Agent | Timestamp |
|----|-------|------|-----------|-------|-----------|
| {{activity_id}} | {{label}} | {{entity_ids}} | {{output_id}} | {{agent_id}} | {{iso_timestamp}} |

## Agents
| ID | Type | Role |
|----|------|------|
| {{agent_id}} | {{nucleus|tool|human}} | {{role}} |

## Derivation Relations
- {{target_artifact_id}} {{derivation_type}} {{source_entity_id}}
- {{target_artifact_id}} wasGeneratedBy {{primary_activity_id}}
- {{target_artifact_id}} wasAttributedTo {{primary_agent_id}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_dataset_card]] | related | 0.19 |
| [[bld_collaboration_prompt_template]] | upstream | 0.18 |
| [[role-assignment-builder]] | upstream | 0.18 |
| [[bld_output_template_prompt_template]] | related | 0.18 |
| [[bld_output_template_memory_type]] | related | 0.18 |
| [[bld_output_template_input_schema]] | related | 0.17 |
| [[bld_output_template_kind]] | related | 0.17 |
| [[bld_examples_role_assignment]] | downstream | 0.17 |
| [[bld_output_template_type_def]] | related | 0.17 |
| [[bld_output_template_capability_registry]] | related | 0.16 |
