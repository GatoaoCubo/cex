---
id: p06_is_creation_data
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "creation operations requiring structured data input across CEX system"
fields:
  - name: "name"
    type: "string"
    required: true
    default: null
    description: "Unique identifier or title for the creation target"
    error_message: "name is required — provide a non-empty string identifier"
  - name: "kind"
    type: "string"
    required: true
    default: null
    description: "CEX artifact kind (agent, knowledge_card, prompt_template, etc.)"
    error_message: "kind is required — specify valid CEX artifact type"
  - name: "description"
    type: "string"
    required: false
    default: ""
    description: "Human-readable description of creation purpose and scope"
    error_message: null
  - name: "pillar"
    type: "string"
    required: false
    default: "P01"
    description: "Target pillar (P01-P12) for artifact placement"
    error_message: null
  - name: "domain"
    type: "string"
    required: false
    default: "generic"
    description: "Domain specialization for the created artifact"
    error_message: null
  - name: "config"
    type: "object"
    required: false
    default: {}
    description: "Creation-specific configuration parameters and overrides"
    error_message: null
  - name: "tags"
    type: "list"
    required: false
    default: []
    description: "Categorization tags for searchability and organization"
    error_message: null
  - name: "quality_target"
    type: "float"
    required: false
    default: 8.0
    description: "Minimum quality score target (0.0-10.0)"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Split comma-separated string into list for tags field"
  - from: "integer"
    to: "float"
    rule: "Convert integer quality target to float precision"
  - from: "string"
    to: "float"
    rule: "Parse numeric string to float for quality_target"
examples:
  - name: "research_agent"
    kind: "agent"
    description: "Agent specialized in competitive intelligence gathering"
    pillar: "P02"
    domain: "research"
    config: {"model": "opus", "max_turns": 50}
    tags: ["research", "intelligence", "analysis"]
    quality_target: 9.0
  - name: "api_knowledge_card"
    kind: "knowledge_card" 
    pillar: "P01"
    tags: ["api", "integration"]
domain: "creation-operations"
quality: 9.1
tags: [input-schema, creation, data-model, cex-system]
tldr: "Input contract for CEX creation operations: requires name and kind, optional pillar, domain, config, tags, and quality target."
density_score: 0.89
related:
  - p06_is_knowledge_data_model
  - bld_schema_model_registry
  - bld_schema_input_schema
  - bld_schema_experiment_tracker
  - bld_schema_kind
  - bld_schema_optimizer
  - bld_schema_prompt_compiler
  - bld_schema_action_paradigm
  - bld_schema_dataset_card
  - p06_is_builder_specification
---
# Contract Definition
This input schema serves creation operations across the CEX system. Any nucleus or builder performing creation tasks accepts this standardized data shape to produce artifacts. Callers provide required identification (name, kind) and optional placement metadata for consistent artifact generation.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | name | string | YES | - | Unique identifier or title for the creation target |
| 2 | kind | string | YES | - | CEX artifact kind (agent, knowledge_card, prompt_template, etc.) |
| 3 | description | string | NO | "" | Human-readable description of creation purpose and scope |
| 4 | pillar | string | NO | "P01" | Target pillar (P01-P12) for artifact placement |
| 5 | domain | string | NO | "generic" | Domain specialization for the created artifact |
| 6 | config | object | NO | {} | Creation-specific configuration parameters and overrides |
| 7 | tags | list | NO | [] | Categorization tags for searchability and organization |
| 8 | quality_target | float | NO | 8.0 | Minimum quality score target (0.0-10.0) |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Split comma-separated string into list for tags field |
| integer | float | Convert integer quality target to float precision |
| string | float | Parse numeric string to float for quality_target |

## Examples
```json
{
  "name": "research_agent",
  "kind": "agent",
  "description": "Agent specialized in competitive intelligence gathering",
  "pillar": "P02",
  "domain": "research",
  "config": {"model": "opus", "max_turns": 50},
  "tags": ["research", "intelligence", "analysis"],
  "quality_target": 9.0
}
```

```json
{
  "name": "api_knowledge_card",
  "kind": "knowledge_card",
  "pillar": "P01",
  "tags": ["api", "integration"]
}
```

## References
- CEX artifact schema definitions (P{01-12}/_schema.yaml)
- 8F pipeline creation workflow
- Builder dispatch protocol for artifact generation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_is_knowledge_data_model]] | sibling | 0.49 |
| [[bld_schema_model_registry]] | related | 0.39 |
| [[bld_schema_input_schema]] | related | 0.38 |
| [[bld_schema_experiment_tracker]] | related | 0.36 |
| [[bld_schema_kind]] | related | 0.33 |
| [[bld_schema_optimizer]] | related | 0.33 |
| [[bld_schema_prompt_compiler]] | related | 0.33 |
| [[bld_schema_action_paradigm]] | related | 0.33 |
| [[bld_schema_dataset_card]] | related | 0.32 |
| [[p06_is_builder_specification]] | sibling | 0.32 |
