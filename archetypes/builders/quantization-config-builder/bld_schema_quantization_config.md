---
kind: schema
id: bld_schema_quantization_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for quantization_config
quality: null
title: "Schema Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Y | - | Unique identifier |
| kind | string | Y | quantization_config | Config type |
| pillar | string | Y | P09 | Pillar code |
| title | string | Y | - | Descriptive name |
| version | string | Y | 1.0.0 | SemVer |
| created | datetime | Y | - | Creation time |
| updated | datetime | Y |
