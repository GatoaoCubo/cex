---
id: p06_is_intelligence_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "builder_agent"
scope: "Intelligence analysis operations requiring structured data input"
fields:
  - name: "query"
    type: "string"
    required: true
    default: null
    description: "Research question or intelligence topic to analyze"
    error_message: "query is required — provide a research question or topic"
  - name: "data_sources"
    type: "list"
    required: false
    default: ["papers", "web", "internal_knowledge"]
    description: "List of data sources to search: papers, web, internal_knowledge, databases"
    error_message: null
  - name: "analysis_depth"
    type: "string"
    required: false
    default: "medium"
    description: "Analysis depth: shallow, medium, deep, comprehensive"
    error_message: "analysis_depth must be one of: shallow, medium, deep, comprehensive"
  - name: "time_constraint_hours"
    type: "integer"
    required: false
    default: 24
    description: "Maximum time allowed for analysis in hours"
    error_message: "time_constraint_hours must be a positive integer"
  - name: "min_confidence_threshold"
    type: "float"
    required: false
    default: 0.7
    description: "Minimum confidence score for included findings (0.0-1.0)"
    error_message: "min_confidence_threshold must be between 0.0 and 1.0"
  - name: "output_format"
    type: "string"
    required: false
    default: "structured_report"
    description: "Desired output format: structured_report, executive_summary, data_points, full_analysis"
    error_message: "output_format must be one of: structured_report, executive_summary, data_points, full_analysis"
  - name: "geographic_scope"
    type: "list"
    required: false
    default: null
    description: "Geographic regions to focus on, if applicable"
    error_message: null
  - name: "temporal_scope"
    type: "object"
    required: false
    default: null
    description: "Time period constraints: {start_date, end_date, relative_period}"
    error_message: null
coercion:
  - from: "string"
    to: "integer" 
    rule: "Parse time_constraint_hours from string if numeric"
  - from: "string"
    to: "float"
    rule: "Parse min_confidence_threshold from string if numeric between 0.0-1.0"
  - from: "string"
    to: "list"
    rule: "Split comma-separated data_sources string into list"
examples:
  - query: "Analyze emerging AI safety research trends in 2026"
    data_sources: ["papers", "web"]
    analysis_depth: "deep"
    time_constraint_hours: 48
    min_confidence_threshold: 0.8
    output_format: "structured_report"
  - query: "Competitor analysis for enterprise RAG solutions"
    analysis_depth: "medium"
    geographic_scope: ["North America", "Europe"]
    temporal_scope: {relative_period: "last_6_months"}
domain: "intelligence-analysis"
quality: 8.9
tags: [input-schema, intelligence, data-model, analysis, research]
tldr: "Input contract for intelligence analysis: requires query, optional sources/depth/format/constraints for structured research operations."
density_score: 0.92
---
## Contract Definition
Intelligence analysis operations receive research requests from agents, users, or automated systems. Callers provide a research query and optional parameters for data sources, analysis depth, time constraints, confidence thresholds, and output formatting. The system uses these inputs to scope and execute structured intelligence gathering and analysis.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | query | string | YES | - | Research question or intelligence topic to analyze |
| 2 | data_sources | list | NO | ["papers", "web", "internal_knowledge"] | Data sources to search |
| 3 | analysis_depth | string | NO | "medium" | Analysis depth level (shallow/medium/deep/comprehensive) |
| 4 | time_constraint_hours | integer | NO | 24 | Maximum time allowed for analysis |
| 5 | min_confidence_threshold | float | NO | 0.7 | Minimum confidence score for findings (0.0-1.0) |
| 6 | output_format | string | NO | "structured_report" | Desired output format type |
| 7 | geographic_scope | list | NO | null | Geographic regions to focus analysis |
| 8 | temporal_scope | object | NO | null | Time period constraints for data collection |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | integer | Parse time_constraint_hours from numeric string |
| string | float | Parse min_confidence_threshold from numeric string (0.0-1.0) |
| string | list | Split comma-separated data_sources into list |

## Examples
```json
{
  "query": "Analyze emerging AI safety research trends in 2026",
  "data_sources": ["papers", "web"],
  "analysis_depth": "deep",
  "time_constraint_hours": 48,
  "min_confidence_threshold": 0.8,
  "output_format": "structured_report"
}
```

```json
{
  "query": "Competitor analysis for enterprise RAG solutions",
  "analysis_depth": "medium", 
  "geographic_scope": ["North America", "Europe"],
  "temporal_scope": {"relative_period": "last_6_months"}
}
```

## References
- N01 Intelligence Nucleus data requirements
- RAG source configuration patterns
- Intelligence analysis workflow standards