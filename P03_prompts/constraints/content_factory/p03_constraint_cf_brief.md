---
id: p03_constraint_cf_brief
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
name: "Content Factory Brief Format Constraints"
constraint_type: "input_schema"
pattern: "required_fields"
quality: null
tags: [constraint_spec, content-factory, brief, input-validation]
tldr: "Brief constraints: required fields (topic, audience, formats, brand_ref), validation rules, completeness gate"
description: "Governs the content brief input that initiates the entire Content Factory pipeline"
provider_compat: "json_schema, yaml_validation"
fallback: "Interactive prompt to collect missing fields from user"
temperature_override: "0.2"
max_tokens: "1024"
---

## Overview

Constrains the content brief — the input document that initiates the entire Content Factory master pipeline (dag_cf_master). A valid brief is the prerequisite for any content production. The ingest_brief node in dag_cf_master validates against this spec before allowing the pipeline to proceed.

## Constraint Definition

### Required Fields
| Field | Type | Description | Example |
|-------|------|-------------|---------|
| topic | string | Primary subject of the content | "AI agents for small business automation" |
| audience | string | Target audience persona | "Solo entrepreneurs, 25-45, non-technical" |
| formats | list[string] | Output formats to produce | ["video", "course", "ebook", "social"] |
| brand_ref | string | Path to brand_config.yaml or brand name | ".cex/brand/brand_config.yaml" |
| tone | enum | Brand voice register | "professional" / "casual" / "educational" |
| goal | string | Business objective for this content | "Lead generation for Q2 product launch" |

### Recommended Fields
| Field | Type | Description | Default |
|-------|------|-------------|---------|
| keywords | list[string] | SEO/discovery keywords | Auto-extracted from topic |
| competitors | list[string] | Competitor URLs to research | [] |
| deadline | date | Target completion date | null (no deadline) |
| budget_tier | enum | Resource allocation tier | "standard" |
| language | string | Content language | "pt-BR" |
| distribution | list[string] | Target channels | Auto from formats |

### MUST Rules
- Brief MUST contain all 6 required fields before pipeline starts
- topic MUST be a non-empty string with minimum 10 characters
- audience MUST describe at least: age range OR role OR industry
- formats MUST contain at least 1 valid format from: video, course, ebook, presentation, social, podcast
- brand_ref MUST point to an existing brand_config.yaml or recognized brand name
- tone MUST be one of: professional, casual, educational, inspirational, technical

### MUST NOT Rules
- MUST NOT start pipeline with incomplete required fields
- MUST NOT accept formats not in the supported list
- MUST NOT proceed without valid brand_ref (pipeline produces generic output)
- MUST NOT allow topic shorter than 10 characters

### Validation Flow
```
brief_submitted → validate_required → validate_types → validate_brand_ref → PASS/FAIL
  FAIL → return missing_fields list → prompt user → re-validate
  PASS → inject into dag_cf_master.ingest_brief node
```

### Quality Metrics
| Metric | Min | Target | Max |
|--------|-----|--------|-----|
| required_fields_present | 6/6 | 6/6 | 6/6 |
| audience_specificity | low | medium | high |
| format_count | 1 | 3 | 6 |

## Provider Compatibility

| Provider | Support | Method |
|----------|---------|--------|
| JSON Schema | native | Validate brief against JSON schema definition |
| YAML | native | Parse and validate YAML-formatted briefs |
| CLI prompt | native | Interactive collection of missing fields |
| Web form | partial | Form-based brief input with client-side validation |

## Integration

- Consumed by: dag_cf_master (ingest_brief node, first gate)
- Blocks: entire pipeline if validation fails
- Cross-references: brand_config.yaml (validates brand_ref field)
- Feeds: research node (topic, keywords) + strategy node (audience, goal, tone)
