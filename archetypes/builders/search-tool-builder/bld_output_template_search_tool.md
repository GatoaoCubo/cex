---
kind: output_template
id: bld_output_template_search_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a search_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
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
{{what_this_search_tool_does_1_to_2_sentences}}
{{primary_use_case_and_when_to_use}}
## Query
### Parameters
- `query` (string, required): {{query_description}}
- `max_results` (integer, optional, default: {{N}}): {{max_results_description}}
- `search_type` (enum, optional): {{search_type_options}}
### Filtering
- Date range: {{date_filtering_description}}
- Domain filter: {{domain_filtering_description}}
- Language: {{language_filtering_description}}
## Results
### Structure
Each result contains:
- `title` (string): {{title_description}}
- `url` (string): {{url_description}}
- `snippet` (string): {{snippet_description}}
- {{additional_field}}: {{field_description}}
### Ranking
{{how_results_are_ranked}}
### Pagination
{{pagetion_support_description}}
## Provider
- API: {{api_endpoint_pattern}}
- Auth: env var `{{ENV_VAR_NAME}}` (NEVER hardcode)
- Rate limit: {{rate_limit_detail}}
- Cost: {{cost_per_query_detail}}
- Free tier: {{free_tier_availability}}
