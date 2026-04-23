---
id: p06_is_intelligence_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
scope: "intelligence data model creation and analysis operations"
fields:
  - name: "model_name"
    type: "string"
    required: true
    default: null
    description: "Unique identifier name for the intelligence data model"
    error_message: "model_name is required — provide a unique slug (e.g. 'competitor_landscape_q2')"
  - name: "domain"
    type: "string"
    required: true
    default: null
    description: "Intelligence domain: market_research | competitor_analysis | trend_analysis | threat_intelligence | benchmarking"
    error_message: "domain is required — must be one of: market_research, competitor_analysis, trend_analysis, threat_intelligence, benchmarking"
  - name: "entity_types"
    type: "list"
    required: true
    default: null
    description: "List of entity types to model (e.g. ['company', 'product', 'signal', 'paper', 'actor'])"
    error_message: "entity_types is required — provide at least one entity type as a list of strings"
  - name: "relationship_types"
    type: "list"
    required: false
    default: []
    description: "Relationship types between entities (e.g. ['competes_with', 'cites', 'employs'])"
    error_message: null
  - name: "source_formats"
    type: "list"
    required: false
    default: ["text", "json"]
    description: "Accepted input formats for raw intelligence data: text | json | pdf | html | csv"
    error_message: null
  - name: "time_horizon"
    type: "string"
    required: false
    default: "current"
    description: "Temporal scope of the intelligence: current | historical | predictive | all"
    error_message: null
  - name: "confidence_threshold"
    type: "float"
    required: false
    default: 0.7
    description: "Minimum confidence score (0.0–1.0) to include a finding in the model"
    error_message: null
  - name: "max_depth"
    type: "integer"
    required: false
    default: 3
    description: "Maximum relationship traversal depth when resolving entity graphs"
    error_message: null
  - name: "output_format"
    type: "string"
    required: false
    default: "structured"
    description: "Output representation: structured | narrative | hybrid | graph"
    error_message: null
  - name: "tags"
    type: "list"
    required: false
    default: []
    description: "Metadata tags for downstream indexing and retrieval"
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse confidence_threshold from numeric string via float(); reject if non-numeric or outside [0.0, 1.0]"
  - from: "string"
    to: "integer"
    rule: "Parse max_depth from numeric string via int(); reject if non-numeric or < 1"
  - from: "string"
    to: "list"
    rule: "Coerce entity_types and relationship_types from comma-separated string to list[string] when a flat string is received"
examples:
  - model_name: "saas_competitor_q2_2026"
    domain: "competitor_analysis"
    entity_types: ["company", "product", "feature", "pricing_tier"]
    relationship_types: ["competes_with", "offers", "targets"]
    source_formats: ["text", "json", "pdf"]
    time_horizon: "current"
    confidence_threshold: 0.75
    max_depth: 2
    output_format: "structured"
    tags: ["saas", "q2-2026", "b2b"]
  - model_name: "ai_trends_2026"
    domain: "trend_analysis"
    entity_types: ["paper", "technique", "organization"]
    relationship_types: ["cites", "develops"]
    time_horizon: "historical"
    confidence_threshold: 0.6
    max_depth: 4
    output_format: "hybrid"
domain: "intelligence-data-modeling"
quality: 9.1
tags: [input-schema, intelligence, data-model, research, P06]
tldr: "Input contract for intelligence data model ops: requires model_name, domain, entity_types; optional depth, confidence, time horizon, and output format."
density_score: 0.92
keywords: [input_schema, intelligence, data_model, entity_types, relationship_types, confidence_threshold, domain, time_horizon]
related:
  - p06_is_knowledge_data_model
  - p06_is_creation_data
  - p06_is_engineering_data_model
  - bld_schema_input_schema
  - bld_schema_model_registry
  - bld_schema_knowledge_graph
  - bld_schema_reranker_config
  - bld_schema_research_pipeline
  - bld_schema_action_paradigm
  - bld_schema_vision_tool
---
## Contract Definition

Intelligence data model creation and analysis operations receive structured input defining the model identity, intelligence domain, entity taxonomy, and operational parameters. Callers must provide a unique model name, the intelligence domain (e.g. competitor analysis, trend analysis), and at least one entity type to model. Optionally, callers configure relationship types between entities, accepted source formats, temporal scope, confidence threshold for findings inclusion, traversal depth for graph resolution, output representation style, and indexing tags. The receiver produces a fully typed intelligence data model artifact ready for ingestion by N01 pipelines and retriever configurations.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | model_name | string | YES | — | Unique model slug identifier |
| 2 | domain | string | YES | — | Intelligence domain enum (market_research, competitor_analysis, trend_analysis, threat_intelligence, benchmarking) |
| 3 | entity_types | list | YES | — | Entity types to include (min 1) |
| 4 | relationship_types | list | NO | [] | Relationship edges between entities |
| 5 | source_formats | list | NO | ["text","json"] | Accepted raw data formats |
| 6 | time_horizon | string | NO | "current" | Temporal scope: current / historical / predictive / all |
| 7 | confidence_threshold | float | NO | 0.7 | Minimum confidence to include a finding (0.0–1.0) |
| 8 | max_depth | integer | NO | 3 | Max relationship traversal depth (>= 1) |
| 9 | output_format | string | NO | "structured" | Output style: structured / narrative / hybrid / graph |
| 10 | tags | list | NO | [] | Indexing metadata tags |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| string | float | Parse `confidence_threshold` via `float()`; reject if non-numeric or outside [0.0, 1.0] |
| string | integer | Parse `max_depth` via `int()`; reject if non-numeric or < 1 |
| string | list | Split `entity_types` / `relationship_types` on comma when a flat string is received |

## Examples

```json
{
  "model_name": "saas_competitor_q2_2026",
  "domain": "competitor_analysis",
  "entity_types": ["company", "product", "feature", "pricing_tier"],
  "relationship_types": ["competes_with", "offers", "targets"],
  "source_formats": ["text", "json", "pdf"],
  "time_horizon": "current",
  "confidence_threshold": 0.75,
  "max_depth": 2,
  "output_format": "structured",
  "tags": ["saas", "q2-2026", "b2b"]
}
```

```json
{
  "model_name": "ai_trends_2026",
  "domain": "trend_analysis",
  "entity_types": ["paper", "technique", "organization"],
  "time_horizon": "historical",
  "confidence_threshold": 0.6,
  "output_format": "hybrid"
}
```

## References

- JSON Schema draft-07: json-schema.org
- OpenAPI requestBody specification: spec.openapis.org/oas/v3.1.0
- CEX P06 Schema: `P06_schema/_schema.yaml`
- Related: `p06_is_intelligence_analysis.yaml`, `N01_intelligence/` pipeline configs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_is_knowledge_data_model]] | sibling | 0.43 |
| [[p06_is_creation_data]] | sibling | 0.40 |
| [[p06_is_engineering_data_model]] | sibling | 0.36 |
| [[bld_schema_input_schema]] | related | 0.32 |
| [[bld_schema_model_registry]] | related | 0.30 |
| [[bld_schema_knowledge_graph]] | related | 0.30 |
| [[bld_schema_reranker_config]] | related | 0.29 |
| [[bld_schema_research_pipeline]] | related | 0.29 |
| [[bld_schema_action_paradigm]] | related | 0.29 |
| [[bld_schema_vision_tool]] | related | 0.29 |
