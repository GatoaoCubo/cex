---
id: p06_is_intelligence_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "Intelligence data collection and analysis operations requiring structured input parameters"
fields:
  - name: "query"
    type: "string"
    required: true
    default: null
    description: "Primary research topic or intelligence question to investigate"
    error_message: "query is required — provide a specific research topic or intelligence question"
  - name: "sources"
    type: "list"
    required: false
    default: ["open_source", "academic", "news"]
    description: "List of source types to query: open_source, academic, news, social, government, commercial"
    error_message: null
  - name: "depth"
    type: "string"
    required: false
    default: "medium"
    description: "Analysis depth level: surface, medium, deep"
    error_message: "depth must be one of: surface, medium, deep"
  - name: "max_results"
    type: "integer"
    required: false
    default: 50
    description: "Maximum number of intelligence items to collect and analyze"
    error_message: "max_results must be a positive integer"
  - name: "geographic_scope"
    type: "string"
    required: false
    default: "global"
    description: "Geographic focus area: global, region name, or country code"
    error_message: null
  - name: "language"
    type: "string"
    required: false
    default: "en"
    description: "Primary language for sources and analysis (ISO 639-1 code)"
    error_message: "language must be a valid ISO 639-1 language code"
  - name: "time_horizon"
    type: "string"
    required: false
    default: "current"
    description: "Temporal focus: current, recent, historical, or specific date range"
    error_message: "time_horizon must be: current, recent, historical, or YYYY-YYYY format"
  - name: "output_format"
    type: "string"
    required: false
    default: "structured"
    description: "Desired output format: brief, detailed, structured, or raw_data"
    error_message: "output_format must be one of: brief, detailed, structured, raw_data"
  - name: "confidence_threshold"
    type: "float"
    required: false
    default: 0.7
    description: "Minimum confidence score for included intelligence items (0.0-1.0)"
    error_message: "confidence_threshold must be between 0.0 and 1.0"
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse max_results from string if numeric, fail if non-numeric"
  - from: "string"
    to: "float"
    rule: "Parse confidence_threshold from string if numeric, fail if non-numeric or outside 0.0-1.0 range"
  - from: "string"
    to: "list"
    rule: "Split comma-separated sources string into list, trim whitespace"
examples:
  - query: "emerging AI threats in cybersecurity"
    sources: ["academic", "news", "government"]
    depth: "deep"
    geographic_scope: "US"
    time_horizon: "current"
  - query: "supply chain vulnerabilities semiconductor industry"
    max_results: 25
    depth: "medium"
    output_format: "structured"
    confidence_threshold: 0.8
domain: "intelligence-analysis"
quality: 8.9
tags: [input-schema, intelligence, data-model, research, analysis]
tldr: "Input contract for intelligence operations: requires query, optional sources/depth/geography/language/time parameters with defaults."
density_score: 0.87
---
## Contract Definition
Intelligence data model operations receive research requests from analysts, researchers, and automated systems. Callers provide a research query and optional parameters controlling source selection, analysis depth, geographic scope, temporal focus, and output formatting. The system collects and analyzes intelligence based on these parameters.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | query | string | YES | - | Primary research topic or intelligence question |
| 2 | sources | list | NO | ["open_source", "academic", "news"] | Source types to query |
| 3 | depth | string | NO | "medium" | Analysis depth: surface/medium/deep |
| 4 | max_results | integer | NO | 50 | Maximum intelligence items to collect |
| 5 | geographic_scope | string | NO | "global" | Geographic focus area |
| 6 | language | string | NO | "en" | Primary language (ISO 639-1) |
| 7 | time_horizon | string | NO | "current" | Temporal focus |
| 8 | output_format | string | NO | "structured" | Desired output format |
| 9 | confidence_threshold | float | NO | 0.7 | Minimum confidence score (0.0-1.0) |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | integer | Parse max_results from string if numeric |
| string | float | Parse confidence_threshold from string if numeric and 0.0-1.0 |
| string | list | Split comma-separated sources into list, trim whitespace |

## Examples
```json
{
  "query": "emerging AI threats in cybersecurity",
  "sources": ["academic", "news", "government"],
  "depth": "deep",
  "geographic_scope": "US",
  "time_horizon": "current"
}
```

```json
{
  "query": "supply chain vulnerabilities semiconductor industry",
  "max_results": 25,
  "depth": "medium", 
  "output_format": "structured",
  "confidence_threshold": 0.8
}
```

## References
- Intelligence analysis frameworks and OSINT methodologies
- ISO 639-1 language codes for multilingual intelligence collection
- Geographic classification standards for regional intelligence scoping