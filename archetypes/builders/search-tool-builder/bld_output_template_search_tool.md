---
kind: output_template
id: bld_output_template_search_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a search_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: search_tool
```yaml
id: p04_search_{{provider_slug}}
kind: search_tool
pillar: P04

version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"

name: "{{human_readable_tool_name}}"
provider: "{{tavily|serper|perplexity|brave|exa|google}}"
search_type: {{web|semantic|hybrid|news|images}}
max_results: {{integer_default_10}}

result_fields:
  - title
  - url
  - snippet

  - {{additional_field}}
date_range: {{true|false}}
domain_filter: {{true|false}}
language: [{{lang_code_1}}, {{lang_code_2}}]

cost_per_query: "{{cost_estimate}}"
rate_limit: "{{requests_per_unit_time}}"
quality: null
tags: [search_tool, {{tag_2}}, {{tag_3}}]

tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
```
## Overview
`{{what_this_search_tool_does_1_to_2_sentences}}`
`{{primary_use_case_and_when_to_use}}`
## Query
### Parameters
1. `query` (string, required): `{{query_description}}`
2. `max_results` (integer, optional, default: {{N}}): `{{max_results_description}}`
3. `search_type` (enum, optional): `{{search_type_options}}`
### Filtering
1. Date range: `{{date_filtering_description}}`
2. Domain filter: `{{domain_filtering_description}}`
3. Language: `{{language_filtering_description}}`
## Results
### Structure
Each result contains:
1. `title` (string): `{{title_description}}`
2. `url` (string): `{{url_description}}`
3. `snippet` (string): `{{snippet_description}}`
4. `{{additional_field}}`: `{{field_description}}`
### Ranking
`{{how_results_are_ranked}}`
### Pagination
`{{pagetion_support_description}}`
## Provider
1. API: `{{api_endpoint_pattern}}`
2. Auth: env var `{{ENV_VAR_NAME}}` (NEVER hardcode)
3. Rate limit: `{{rate_limit_detail}}`
4. Cost: `{{cost_per_query_detail}}`
5. Free tier: `{{free_tier_availability}}`

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | search tool construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
