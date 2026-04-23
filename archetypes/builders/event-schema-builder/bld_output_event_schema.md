---
kind: output_template
id: bld_output_template_event_schema
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an event_schema artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 8.6
title: "Output Template Event Schema"
version: "1.0.0"
author: n03_builder
tags: [event_schema, builder, output_template]
tldr: "Fill-in template for event_schema: CloudEvents envelope, JSON Schema payload, versioning strategy, consumer table."
domain: "event schema construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_schema_validation_schema
  - bld_schema_input_schema
  - bld_schema_audit_log
  - bld_schema_reranker_config
  - bld_schema_function_def
  - bld_schema_search_strategy
  - bld_schema_thinking_config
  - bld_schema_voice_pipeline
  - bld_schema_app_directory_entry
  - bld_schema_usage_report
---

# Output Template: event_schema

```yaml
id: p06_evs_{{event_slug}}
kind: event_schema
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
event_type: "{{reverse_domain}}.{{aggregate}}.{{event}}.v{{major}}"
schema_version: "1.0.0"
source: "/{{service-name}}"
datacontenttype: "application/json"
quality: null
tags: [event_schema, {{aggregate}}, {{domain_tag}}]
tldr: "{{EventName}} v{{major}}: {{list_required_fields}}. CloudEvents 1.0. Source: /{{service}}."
```

## CloudEvents Attributes

| Attribute | Value | Required | Notes |
|-----------|-------|----------|-------|
| specversion | "1.0" | YES | CloudEvents spec version |
| id | UUID | YES | Unique per event |
| type | "{{event_type}}" | YES | Reverse-DNS + version |
| source | "{{source}}" | YES | Producer URI |
| subject | {{subject_field_description}} | REC | Entity identifier |
| time | RFC3339 timestamp | REC | Event occurrence time |
| datacontenttype | "application/json" | YES | Payload format |

## Payload Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "type": "object",
  "required": ["{{required_field_1}}", "{{required_field_2}}"],
  "properties": {
    "{{field_1}}": {
      "type": "{{string|number|integer|boolean}}",
      "format": "{{uuid|date-time|email|optional}}",
      "description": "{{field_description}}"
    },
    "{{field_2}}": {
      "type": "{{type}}",
      "description": "{{description}}"
    }
  }
}
```

## Versioning

| Strategy | {{ADDITIVE_ONLY|VERSIONED_TYPE}} | Notes |
|----------|----------------------------------|-------|
| Add optional field | ALLOWED | Bump schema_version minor |
| Add required field | PROHIBITED | Create v{{major+1}} event_type |
| Remove/rename field | PROHIBITED | Create v{{major+1}} event_type |

## Consumers

| Consumer | Context | Action |
|----------|---------|--------|
| {{ConsumerService}} | {{context}} | {{what_consumer_does}} |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_validation_schema]] | downstream | 0.36 |
| [[bld_schema_input_schema]] | downstream | 0.35 |
| [[bld_schema_audit_log]] | downstream | 0.35 |
| [[bld_schema_reranker_config]] | downstream | 0.34 |
| [[bld_schema_function_def]] | downstream | 0.33 |
| [[bld_schema_search_strategy]] | downstream | 0.33 |
| [[bld_schema_thinking_config]] | downstream | 0.33 |
| [[bld_schema_voice_pipeline]] | downstream | 0.33 |
| [[bld_schema_app_directory_entry]] | downstream | 0.32 |
| [[bld_schema_usage_report]] | downstream | 0.31 |
