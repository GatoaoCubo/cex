---
id: p06_is_creation_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "Creation operations requiring structured input for artifact generation"
fields:
  - name: "intent"
    type: "string"
    required: true
    default: null
    description: "Natural language description of what to create"
    error_message: "intent is required — provide a clear description of what to create"
  - name: "kind"
    type: "string"
    required: true
    default: null
    description: "Artifact type to create (agent, knowledge_card, prompt_template, etc.)"
    error_message: "kind is required — specify the artifact type from CEX taxonomy"
  - name: "domain"
    type: "string"
    required: false
    default: "generic"
    description: "Domain context for specialized creation (research, marketing, technical, etc.)"
    error_message: null
  - name: "quality_target"
    type: "float"
    required: false
    default: 8.0
    description: "Target quality score for the artifact (7.0-10.0 scale)"
    error_message: "quality_target must be between 7.0 and 10.0"
  - name: "context"
    type: "object"
    required: false
    default: null
    description: "Additional context: audience, use_case, constraints, examples"
    error_message: null
  - name: "constraints"
    type: "object"
    required: false
    default: null
    description: "Creation constraints: max_bytes, required_fields, style_guide"
    error_message: null
  - name: "brand_context"
    type: "boolean"
    required: false
    default: true
    description: "Whether to inject brand context from .cex/brand/brand_config.yaml"
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse quality_target from string if numeric (7.0-10.0 range)"
  - from: "integer"
    to: "float"
    rule: "Cast quality_target integer to float"
examples:
  - intent: "Create a knowledge card about React patterns"
    kind: "knowledge_card"
    domain: "technical"
    quality_target: 8.5
  - intent: "Build an agent for research tasks"
    kind: "agent"
    domain: "research"
    context:
      audience: "data scientists"
      use_case: "market analysis"
    constraints:
      max_bytes: 4096
domain: "creation-pipeline"
quality: 8.9
tags: [input-schema, creation, data-model, pipeline]
tldr: "Input contract for creation operations: requires intent and kind, optional domain/quality/context/constraints with sensible defaults."
density_score: 0.91
---
# Contract Definition
Creation operations across CEX nuclei require structured input to generate high-quality artifacts. This schema defines the unilateral contract between creation requesters (users, orchestrators, other agents) and creation processors (builders, nuclei). Requesters provide intent and artifact type; processors use domain context, quality targets, and constraints to guide the 8F pipeline execution.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | intent | string | YES | - | Natural language description of what to create |
| 2 | kind | string | YES | - | Artifact type from CEX taxonomy (99 kinds available) |
| 3 | domain | string | NO | "generic" | Domain specialization context |
| 4 | quality_target | float | NO | 8.0 | Target quality score (7.0-10.0 scale) |
| 5 | context | object | NO | null | Additional context: audience, use_case, constraints, examples |
| 6 | constraints | object | NO | null | Creation limits: max_bytes, required_fields, style_guide |
| 7 | brand_context | boolean | NO | true | Whether to inject brand identity from config |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | float | Parse quality_target from string if numeric (7.0-10.0 range) |
| integer | float | Cast quality_target integer to float for consistent typing |

## Examples
```json
{
  "intent": "Create a knowledge card about React patterns",
  "kind": "knowledge_card", 
  "domain": "technical",
  "quality_target": 8.5
}
```

```json
{
  "intent": "Build an agent for research tasks",
  "kind": "agent",
  "domain": "research",
  "context": {
    "audience": "data scientists",
    "use_case": "market analysis"
  },
  "constraints": {
    "max_bytes": 4096
  }
}
```

## Validation Rules
- intent: minimum 10 characters, no pure whitespace
- kind: must exist in .cex/kinds_meta.json registry
- quality_target: 7.0 ≤ value ≤ 10.0
- domain: alphanumeric with underscores, max 50 characters
- context: if provided, must be valid JSON object
- constraints: if provided, must be valid JSON object with recognized constraint keys

## References
- CEX Taxonomy: .cex/kinds_meta.json (99 registered kinds)
- Quality Gates: P11_quality/library/ (scoring rubrics)
- 8F Pipeline: .claude/rules/n03-8f-enforcement.md
- Brand Context: .cex/brand/brand_config.yaml