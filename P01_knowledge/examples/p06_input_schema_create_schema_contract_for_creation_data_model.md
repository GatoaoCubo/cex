---
id: p06_is_creation_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "creation operations requiring structured data model inputs"
fields:
  - name: "artifact_type"
    type: "string"
    required: true
    default: null
    description: "Type of artifact to create (agent, knowledge_card, prompt_template, etc.)"
    error_message: "artifact_type is required — specify what kind of artifact to create"
  - name: "content_description"
    type: "string"
    required: true
    default: null
    description: "Natural language description of the desired content"
    error_message: "content_description is required — describe what should be created"
  - name: "target_audience"
    type: "string"
    required: false
    default: "general"
    description: "Intended audience for the created content"
    error_message: null
  - name: "domain_context"
    type: "string" 
    required: false
    default: "generic"
    description: "Domain or specialization context for the content"
    error_message: null
  - name: "quality_requirements"
    type: "object"
    required: false
    default: {"min_score": 8.0, "density_target": 0.85}
    description: "Quality constraints including minimum score and density targets"
    error_message: null
  - name: "format_preferences"
    type: "object"
    required: false
    default: {"style": "professional", "length": "standard"}
    description: "Formatting and style preferences for the output"
    error_message: null
  - name: "dependencies"
    type: "list"
    required: false
    default: []
    description: "List of existing artifacts or resources this creation depends on"
    error_message: null
  - name: "constraints"
    type: "object"
    required: false
    default: {}
    description: "Additional constraints like max_length, must_include, cannot_include"
    error_message: null
coercion:
  - from: "string"
    to: "object"
    rule: "Parse JSON string to object for quality_requirements, format_preferences, constraints"
  - from: "string"
    to: "list"  
    rule: "Split comma-separated string to list for dependencies field"
examples:
  - {artifact_type: "knowledge_card", content_description: "Create knowledge card about React hooks patterns", target_audience: "frontend developers", domain_context: "web development"}
  - {artifact_type: "agent", content_description: "Build agent for automated code reviews", quality_requirements: {"min_score": 9.0}, constraints: {"max_turns": 20}}
domain: "creation-operations"
quality: 8.9
tags: [input-schema, creation, data-model, artifacts, P06]
tldr: "Input contract for creation operations: requires artifact_type and content_description, with optional audience, quality, and constraint parameters."
density_score: 0.87
---
## Contract Definition
Creation operations receive structured requests from users or other agents to generate new artifacts, content, or resources. This schema defines the required and optional data that creators need to produce high-quality outputs that meet user specifications and quality standards.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | artifact_type | string | YES | - | Type of artifact to create (agent, knowledge_card, etc.) |
| 2 | content_description | string | YES | - | Natural language description of desired content |
| 3 | target_audience | string | NO | "general" | Intended audience for the created content |
| 4 | domain_context | string | NO | "generic" | Domain or specialization context |
| 5 | quality_requirements | object | NO | {"min_score": 8.0, "density_target": 0.85} | Quality constraints and targets |
| 6 | format_preferences | object | NO | {"style": "professional", "length": "standard"} | Formatting and style preferences |
| 7 | dependencies | list | NO | [] | List of existing artifacts or resources this depends on |
| 8 | constraints | object | NO | {} | Additional constraints like length limits or content requirements |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | object | Parse JSON string to object for quality_requirements, format_preferences, constraints |
| string | list | Split comma-separated string to list for dependencies field |

## Examples
```json
{
  "artifact_type": "knowledge_card",
  "content_description": "Create knowledge card about React hooks patterns",
  "target_audience": "frontend developers", 
  "domain_context": "web development"
}
```

```json
{
  "artifact_type": "agent",
  "content_description": "Build agent for automated code reviews",
  "quality_requirements": {"min_score": 9.0},
  "constraints": {"max_turns": 20}
}
```

## References
- CEX artifact type registry: `.cex/kinds_meta.json`
- Quality scoring system: P11 quality gates
- Domain contexts: P01 knowledge pillar taxonomy