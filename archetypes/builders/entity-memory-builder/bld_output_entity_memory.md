---
kind: output_template
id: bld_output_template_entity_memory
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an entity_memory artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Entity Memory"
version: "1.0.0"
author: n03_builder
tags: [entity_memory, builder, examples]
tldr: "Golden and anti-examples for entity memory construction, demonstrating ideal structure and common pitfalls."
domain: "entity memory construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_entity_memory
  - p03_sp_entity_memory_builder
  - bld_instruction_entity_memory
  - bld_architecture_entity_memory
  - p11_qg_entity_memory
  - bld_knowledge_card_entity_memory
  - bld_examples_entity_memory
  - entity-memory-builder
  - p10_lr_entity_memory_builder
  - bld_config_entity_memory
---

# Output Template: entity_memory
```yaml
id: p10_em_{{entity_slug}}
kind: entity_memory
pillar: P10
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_entity_name}}"
entity_type: {{person|tool|concept|organization|project|service}}
attributes:
  {{attribute_key_1}}: "{{attribute_value_1}}"
  {{attribute_key_2}}: "{{attribute_value_2}}"
  {{attribute_key_3}}: "{{attribute_value_3}}"
update_policy: {{append|overwrite|merge|versioned}}
source: "{{where_entity_info_came_from}}"
relationships:
  - entity: "{{related_entity_id}}"
    relation: "{{relation_type}}"
  - entity: "{{related_entity_id_2}}"
    relation: "{{relation_type_2}}"
confidence: {{0.0_to_1.0}}
last_referenced: "{{YYYY-MM-DD}}"
expiry: {{YYYY-MM-DD|null}}
quality: null
tags: [entity_memory, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_entity_this_tracks_max_200ch}}"
```
## Overview
`{{what_entity_this_memory_tracks_1_to_2_sentences}}`
`{{purpose_and_scope_of_this_entity_record}}`
## Attributes
| Key | Value | Type | Source |
|-----|-------|------|--------|
| `{{attribute_key_1}}` | {{attribute_value_1}} | {{string|date|url|enum}} | `{{source}}` |
| `{{attribute_key_2}}` | {{attribute_value_2}} | {{string|date|url|enum}} | `{{source}}` |
| `{{attribute_key_3}}` | {{attribute_value_3}} | {{string|date|url|enum}} | `{{source}}` |
## Relationships
| Entity | Relation | Direction | Notes |
|--------|----------|-----------|-------|
| `{{related_entity}}` | {{relation_type}} | {{outbound|inbound|bidirectional}} | `{{context}}` |
## Update Policy
Policy: {{append|overwrite|merge|versioned}}
`{{conflict_resolution_rule}}`
`{{staleness_handling_rule}}`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_entity_memory]] | downstream | 0.50 |
| [[p03_sp_entity_memory_builder]] | downstream | 0.45 |
| [[bld_instruction_entity_memory]] | upstream | 0.43 |
| [[bld_architecture_entity_memory]] | downstream | 0.37 |
| [[p11_qg_entity_memory]] | downstream | 0.36 |
| [[bld_knowledge_card_entity_memory]] | upstream | 0.34 |
| [[bld_examples_entity_memory]] | downstream | 0.34 |
| [[entity-memory-builder]] | downstream | 0.33 |
| [[p10_lr_entity_memory_builder]] | downstream | 0.28 |
| [[bld_config_entity_memory]] | downstream | 0.27 |
