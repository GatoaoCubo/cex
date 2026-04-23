---
id: p06_enum_def
kind: enum_def
pillar: P06
version: 1.0.0
title: "Template — Enum Definition"
tags: [template, enum, type, schema, validation]
tldr: "Defines a controlled vocabulary for a field. Lists allowed values, descriptions, deprecation status, and default. Prevents free-text drift in typed fields."
quality: 9.0
related:
  - p11_qg_enum_def
  - bld_output_template_enum_def
  - bld_instruction_enum_def
  - bld_schema_enum_def
  - bld_architecture_enum_def
  - p10_lr_enum_def_builder
  - bld_knowledge_card_enum_def
  - p03_sp_enum_def_builder
  - bld_config_enum_def
  - enum-def-builder
---

# Enum Definition: [ENUM_NAME]

## Purpose
[WHAT field this enum constrains — e.g., pillar codes, quality levels, status values]

## Values

| Value | Description | Status |
|-------|-------------|--------|
| [VALUE_1] | [What this value means] | active |
| [VALUE_2] | [What this value means] | active |
| [VALUE_3] | [What this value means] | deprecated |

## Usage
```yaml
# In frontmatter
field_name: [VALUE_1]  # Must be one of the enum values

# In schema validation
allowed: [VALUE_1, VALUE_2, VALUE_3]
default: [VALUE_1]
```

## Properties
| Property | Value |
|----------|-------|
| Field | [FIELD_NAME in frontmatter] |
| Default | [VALUE or null] |
| Required | [yes \| no] |
| Case sensitive | [yes \| no — typically no] |
| Extensible | [yes \| no — can new values be added?] |

## Deprecation Policy
When a value is deprecated:
1. Mark as `deprecated` in status column
2. Add `deprecated_since: YYYY-MM-DD` metadata
3. Keep accepting for 90 days (backward compat)
4. After 90 days: reject with "use [REPLACEMENT] instead"

## Validation
```python
def validate_enum(value: str, enum_name: str) -> bool:
    allowed = ENUM_REGISTRY[enum_name]
    active = [v for v in allowed if v["status"] == "active"]
    return value in [v["value"] for v in active]
```

## Quality Gate
- [ ] At least 2 values defined
- [ ] Each value has a description (not just the label)
- [ ] Default value specified
- [ ] Deprecation policy documented

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_enum_def]] | downstream | 0.36 |
| [[bld_output_template_enum_def]] | upstream | 0.33 |
| [[bld_instruction_enum_def]] | upstream | 0.32 |
| [[bld_schema_enum_def]] | related | 0.31 |
| [[bld_architecture_enum_def]] | downstream | 0.30 |
| [[p10_lr_enum_def_builder]] | downstream | 0.27 |
| [[bld_knowledge_card_enum_def]] | upstream | 0.26 |
| [[p03_sp_enum_def_builder]] | related | 0.25 |
| [[bld_config_enum_def]] | downstream | 0.23 |
| [[enum-def-builder]] | related | 0.23 |
