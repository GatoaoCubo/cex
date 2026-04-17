---
id: p06_is_engineering_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
owner: "n03_builder_nucleus"
scope: "engineering data model creation and validation operations"
fields:
  - name: "project_name"
    type: "string"
    required: true
    default: null
    description: "Unique name identifying the engineering project requiring the data model"
    error_message: "project_name is required — provide a unique project identifier"
  - name: "engineering_domain"
    type: "string"
    required: true
    default: null
    description: "Engineering discipline: software, mechanical, electrical, civil, or chemical"
    error_message: "engineering_domain is required — must be one of: software, mechanical, electrical, civil, chemical"
  - name: "model_type"
    type: "string"
    required: true
    default: null
    description: "Data model architecture: relational, entity-relationship, dimensional, document, or graph"
    error_message: "model_type is required — must be one of: relational, entity-relationship, dimensional, document, graph"
  - name: "requirements"
    type: "list"
    required: true
    default: null
    description: "Ordered list of functional requirements the data model must satisfy"
    error_message: "requirements is required — provide at least one functional requirement as a list item"
  - name: "constraints"
    type: "object"
    required: false
    default: null
    description: "Technical constraints: {max_entities, normalization_level, storage_backend}"
    error_message: null
  - name: "quality_metrics"
    type: "object"
    required: false
    default: null
    description: "Target quality thresholds: {min_normalization, max_redundancy, coverage_pct}"
    error_message: null
  - name: "data_sources"
    type: "list"
    required: false
    default: []
    description: "Source systems the model must integrate: [{name, format, volume}]"
    error_message: null
  - name: "scale_parameters"
    type: "object"
    required: false
    default: null
    description: "Scale expectations: {expected_rows, growth_rate_pct, peak_qps, retention_days}"
    error_message: null
  - name: "validation_rules"
    type: "list"
    required: false
    default: []
    description: "Domain-specific validation rules applied during model generation"
    error_message: null
  - name: "output_format"
    type: "string"
    required: false
    default: "yaml"
    description: "Output format for the generated model artifact: yaml, json, or sql-ddl"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Single string requirement parsed as single-item list via [value]"
  - from: "string"
    to: "object"
    rule: "JSON-encoded string parsed via json.loads() — reject if not valid JSON"
  - from: "string"
    to: "integer"
    rule: "Numeric strings in scale_parameters parsed via int() — reject if non-numeric"
examples:
  - project_name: "logistics_platform"
    engineering_domain: "software"
    model_type: "relational"
    requirements:
      - "Track shipment lifecycle from order to delivery"
      - "Support multi-warehouse inventory allocation"
      - "Enforce referential integrity across order, shipment, and warehouse entities"
    constraints:
      max_entities: 20
      normalization_level: "3NF"
      storage_backend: "PostgreSQL"
    output_format: "yaml"
  - project_name: "sensor_telemetry"
    engineering_domain: "electrical"
    model_type: "dimensional"
    requirements:
      - "Store time-series readings from IoT sensors at 1-second resolution"
      - "Enable aggregation by sensor type, location, and time window"
    scale_parameters:
      expected_rows: 50000000
      growth_rate_pct: 20
      peak_qps: 5000
      retention_days: 365
    output_format: "json"
domain: "engineering-data-modeling"
quality: 9.1
tags: [input-schema, engineering-data-model, data-modeling, P06, contract]
tldr: "Input contract for engineering data model creation: requires project name, domain, model type, and requirements list."
keywords: [input_schema, engineering, data_model, requirements, constraints, relational, dimensional, schema_contract]
density_score: 0.92
---
## Contract Definition

Engineering data model creation and validation operations receive structured input defining the project context, domain requirements, architectural constraints, and quality expectations. Callers provide project identification, specify the engineering discipline and data model architecture type, list functional requirements, and optionally supply technical constraints, quality metrics, source system references, and scale parameters. The receiver produces a complete data model artifact in the requested output format.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | project_name | string | YES | — | Unique project identifier |
| 2 | engineering_domain | string | YES | — | Discipline: software, mechanical, electrical, civil, chemical |
| 3 | model_type | string | YES | — | Architecture: relational, entity-relationship, dimensional, document, graph |
| 4 | requirements | list | YES | — | Functional requirements the model must satisfy (min 1) |
| 5 | constraints | object | NO | null | Technical limits: max_entities, normalization_level, storage_backend |
| 6 | quality_metrics | object | NO | null | Quality thresholds: min_normalization, max_redundancy, coverage_pct |
| 7 | data_sources | list | NO | [] | Source systems: [{name, format, volume}] |
| 8 | scale_parameters | object | NO | null | Scale: expected_rows, growth_rate_pct, peak_qps, retention_days |
| 9 | validation_rules | list | NO | [] | Domain-specific validation rules for generation |
| 10 | output_format | string | NO | "yaml" | Output format: yaml, json, or sql-ddl |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| string | list | Single requirement string wrapped as `[value]` |
| string | object | JSON-encoded string parsed via `json.loads()` — reject if invalid JSON |
| string | integer | Numeric strings in `scale_parameters` parsed via `int()` — reject if non-numeric |

## Examples

```json
{
  "project_name": "logistics_platform",
  "engineering_domain": "software",
  "model_type": "relational",
  "requirements": [
    "Track shipment lifecycle from order to delivery",
    "Support multi-warehouse inventory allocation"
  ],
  "constraints": {"max_entities": 20, "normalization_level": "3NF", "storage_backend": "PostgreSQL"},
  "output_format": "yaml"
}
```

```json
{
  "project_name": "sensor_telemetry",
  "engineering_domain": "electrical",
  "model_type": "dimensional",
  "requirements": ["Store time-series IoT readings at 1-second resolution"],
  "scale_parameters": {"expected_rows": 50000000, "peak_qps": 5000, "retention_days": 365},
  "output_format": "json"
}
```

## References

- JSON Schema draft-07: json-schema.org
- OpenAPI requestBody specification: spec.openapis.org
- Entity-Relationship modeling: Chen (1976), ISO/IEC 9075