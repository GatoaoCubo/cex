---
kind: output_template
id: bld_output_template_scraper
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a scraper artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: scraper
```yaml
id: p04_scraper_{{target_slug}}
kind: scraper
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_scraper_name}}"
target: "{{target_site_url}}"
selectors:
  - {{field_name_1}}
  - {{field_name_2}}
output_format: {{json|csv|yaml}}
quality: null
tags: [scraper, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_scraper_extracts_max_200ch}}"
pagination: {{next_page|infinite_scroll|numbered|none}}
rate_limit: "{{N_requests_per_unit}}"
anti_bot: {{none|basic|cloudflare|captcha}}
proxy: {{true|false}}
scheduling: "{{cron_or_interval}}"
validation: [{{rule_1}}, {{rule_2}}]
freshness: "{{staleness_threshold}}"
```
## Overview
{{what_data_is_extracted_1_to_2_sentences}}
{{who_consumes_it_and_primary_use_case}}
## Selectors
### {{field_name_1}}
Selector: `{{css_or_xpath}}` ({{CSS|XPath}})
Type: {{string|float|int|url|boolean}}
Rule: {{extraction_and_cleaning_rule}}
### {{field_name_2}}
Selector: `{{css_or_xpath}}` ({{CSS|XPath}})
Type: {{string|float|int|url|boolean}}
Rule: {{extraction_and_cleaning_rule}}
## Pagination & Rate Limiting
Pagination: {{strategy_and_selector_or_pattern}}
Rate limit: {{requests_per_unit_and_delay}}
Anti-bot: {{awareness_level_and_techniques}}
Proxy: {{required_or_not_and_rotation_policy}}
## Output
Format: {{format_and_record_structure}}
Validation: {{data_validation_rules}}
Freshness: {{staleness_threshold_and_reschedule}}
