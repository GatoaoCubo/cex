---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a dispatch_rule
pattern: every field here exists in SCHEMA.md; template derives, never invents
---

# Output Template: dispatch_rule

Naming pattern: `p12_dr_{scope}.yaml`
Filename: `p12_dr_{{scope}}.yaml`

```yaml
---
id: p12_dr_{{scope}}
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: {{ISO_8601_date}}
updated: {{ISO_8601_date}}
author: {{author_slug}}
domain: {{domain_name}}
quality: null
tags: [{{tag_1}}, {{tag_2}}, {{satellite_slug}}]
tldr: {{one_line_summary_max_120_chars}}
scope: {{scope_slug}}
keywords: [{{keyword_1}}, {{keyword_2}}, {{keyword_3}}]
satellite: {{satellite_slug}}
model: {{sonnet|opus|haiku|flash}}
priority: {{1_to_10}}
confidence_threshold: {{0.0_to_1.0}}
fallback: {{fallback_satellite_slug}}
conditions: {{object_or_omit}}
load_balance: {{true|false_or_omit}}
routing_strategy: {{keyword_match|semantic|hybrid_or_omit}}
---

# {{scope}} Dispatch Rule

## Purpose
{{one_paragraph_explaining_what_this_rule_routes_and_why}}

## Keyword Rationale
{{brief_explanation_of_why_these_keywords_trigger_this_satellite}}

## Fallback Logic
{{brief_explanation_of_when_fallback_fires_and_what_it_handles}}
```

## Derivation Notes
- All frontmatter fields derive from SCHEMA.md required or optional fields
- Omit `conditions`, `load_balance`, `routing_strategy` if not needed
- Body sections are human commentary only; routing logic lives in frontmatter
- `quality: null` must never be changed at authoring time
- `fallback` must be a different satellite slug than `satellite`
