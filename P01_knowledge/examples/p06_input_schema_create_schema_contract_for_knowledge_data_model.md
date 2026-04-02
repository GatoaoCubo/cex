---
id: p06_is_knowledge_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
scope: "knowledge data model creation and update operations"
fields:
  - name: "model_name"
    type: "string"
    required: true
    default: null
    description: "Unique slug-style identifier for the knowledge model (e.g., 'react_hooks_patterns')"
    error_message: "model_name is required — provide a lowercase slug (e.g., 'react_hooks_patterns')"
  - name: "domain"
    type: "string"
    required: true
    default: null
    description: "Subject area this model belongs to (e.g., 'software-engineering', 'marketing')"
    error_message: "domain is required — specify the knowledge subject area"
  - name: "kind"
    type: "string"
    required: true
    default: null
    description: "CEX artifact type: knowledge_card | glossary_entry | learning_record | entity_memory"
    error_message: "kind is required — must be one of: knowledge_card, glossary_entry, learning_record, entity_memory"
  - name: "description"
    type: "string"
    required: true
    default: null
    description: "What knowledge this model captures; source material or topic definition"
    error_message: "description is required — provide a clear statement of what knowledge this model captures"
  - name: "pillar"
    type: "string"
    required: false
    default: "P01"
    description: "CEX pillar assignment; defaults to P01 (knowledge pillar)"
    error_message: null
  - name: "version"
    type: "string"
    required: false
    default: "1.0.0"
    description: "Semver version identifier for schema evolution tracking"
    error_message: null
  - name: "author"
    type: "string"
    required: false
    default: "builder_agent"
    description: "Identity of the agent or user producing this knowledge model"
    error_message: null
  - name: "quality_target"
    type: "float"
    required: false
    default: 8.0
    description: "Minimum quality score (0.0–10.0) required before publishing to pool"
    error_message: null
  - name: "tags"
    type: "list"
    required: false
    default: []
    description: "Classification tags for pool retrieval; include domain and kind tags"
    error_message: null
  - name: "keywords"
    type: "list"
    required: false
    default: []
    description: "TF-IDF search terms for brain retrieval; 3–10 terms recommended"
    error_message: null
  - name: "source_refs"
    type: "list"
    required: false
    default: []
    description: "External references used as source material: URLs, paper titles, library paths"
    error_message: null
  - name: "tldr"
    type: "string"
    required: false
    default: null
    description: "Dense one-line summary of the knowledge model; max 160 characters"
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse quality_target from numeric string (e.g., '8.5' → 8.5); reject if non-numeric"
  - from: "string"
    to: "list"
    rule: "Parse tags or keywords from comma-separated string if list not provided (e.g., 'react, hooks' → ['react', 'hooks'])"
examples:
  - {model_name: "react_hooks_patterns", domain: "frontend-engineering", kind: "knowledge_card", description: "React hooks patterns, anti-patterns, and composition strategies for state management", pillar: "P01", tags: ["react", "hooks", "frontend"], keywords: ["useState", "useEffect", "custom-hooks"], quality_target: 8.5}
  - {model_name: "brand_voice_guidelines", domain: "marketing", kind: "knowledge_card", description: "Brand voice and tone guidelines for written communication across channels"}
domain: "knowledge-management"
quality: 9.1
tags: [input-schema, knowledge-data-model, knowledge-management, P06]
tldr: "Input contract for knowledge data model ops: requires model_name, domain, kind, description; optional pillar, tags, quality_target, and keywords."
density_score: 0.89
---
# Input Schema: Knowledge Data Model

## Contract Definition

Knowledge data model creation and update operations receive structured input defining what knowledge to capture, how to classify it, and where to store it within the CEX P01 knowledge pillar. Callers must provide a slug-style model name, subject domain, artifact kind, and source description. Optional fields control pillar assignment, versioning, quality thresholds, retrieval keywords, and external source references. The receiver produces a typed knowledge artifact conforming to the CEX schema for the declared kind.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | model_name | string | YES | — | Slug-style unique identifier for the knowledge model |
| 2 | domain | string | YES | — | Subject area (e.g., software-engineering, marketing) |
| 3 | kind | string | YES | — | Artifact type: knowledge_card \| glossary_entry \| learning_record \| entity_memory |
| 4 | description | string | YES | — | What knowledge this model captures; topic or source material |
| 5 | pillar | string | NO | "P01" | CEX pillar assignment |
| 6 | version | string | NO | "1.0.0" | Semver version identifier |
| 7 | author | string | NO | "builder_agent" | Producer identity |
| 8 | quality_target | float | NO | 8.0 | Minimum quality score for pool publishing |
| 9 | tags | list | NO | [] | Classification tags for retrieval |
| 10 | keywords | list | NO | [] | TF-IDF search terms; 3–10 recommended |
| 11 | source_refs | list | NO | [] | External references used as source material |
| 12 | tldr | string | NO | null | Dense summary; max 160 characters |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| string | float | Parse `quality_target` from numeric string; reject if non-numeric |
| string | list | Parse `tags` or `keywords` from comma-separated string if caller provides a flat string |

## Examples

```json
{
  "model_name": "react_hooks_patterns",
  "domain": "frontend-engineering",
  "kind": "knowledge_card",
  "description": "React hooks patterns, anti-patterns, and composition strategies for state management",
  "pillar": "P01",
  "tags": ["react", "hooks", "frontend"],
  "keywords": ["useState", "useEffect", "custom-hooks", "react"],
  "quality_target": 8.5
}
```

```json
{
  "model_name": "brand_voice_guidelines",
  "domain": "marketing",
  "kind": "knowledge_card",
  "description": "Brand voice and tone guidelines for written communication across channels"
}
```

## References

- CEX P01 knowledge pillar schema (`P01_knowledge/_schema.yaml`)
- CEX kinds_meta.json — authoritative list of valid kind values
- JSON Schema draft-07 (`json-schema.org`) — field type vocabulary