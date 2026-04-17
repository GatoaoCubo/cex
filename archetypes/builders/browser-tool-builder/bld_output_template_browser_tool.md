---
kind: output_template
id: bld_output_template_browser_tool
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a browser_tool artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.0
title: "Output Template Browser Tool"
version: "1.0.0"
author: n03_builder
tags: [browser_tool, builder, examples]
tldr: "Golden and anti-examples for browser tool construction, demonstrating ideal structure and common pitfalls."
domain: "browser tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Output Template: browser_tool
```yaml
id: p04_browser_{{target_slug}}
kind: browser_tool
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_tool_name}}"
engine: {{playwright|puppeteer|selenium|browser_use|browserbase|stagehand}}
actions:
  - {{action_1}}
  - {{action_2}}
  - {{action_3}}
selectors:
  - {{css|xpath|aria|data_attr|text}}
  - {{css|xpath|aria|data_attr|text}}
output_format: {{json|html|screenshot|text}}
headless: {{true|false}}
viewport: "{{width}}x{{height}}"
timeout: {{ms_integer}}
javascript: {{true|false}}
cookies: {{true|false}}
stealth: {{true|false}}
quality: null
tags: [browser_tool, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_tool_does_max_200ch}}"
user_agent: "{{user_agent_string_or_omit}}"
proxy: "{{proxy_url_or_omit}}"
```
## Overview
`{{what_the_tool_automates_1_to_2_sentences}}`
`{{target_site_domain_and_primary_use_case}}`
## Engine
Engine: `{{engine_name}}` ({{browser_type}}). Headless: {{true|false}}. Viewport: `{{WxH}}`.
Timeout: `{{ms}}`ms per action. JavaScript: {{enabled|disabled}}.
`{{stealth_config_if_applicable}}`
## Actions
### `{{action_1}}`
`{{action_description}}`
Params: `{{param_name}}` ({{type}}, {{required|optional}}): `{{param_description}}`
`{{selector_if_applicable}}`: {{selector_string}} (`{{strategy}}`)
Fallback: `{{fallback_selector}}` (`{{fallback_strategy}}`)
Wait: `{{wait_condition}}`
Returns: `{{return_description}}`
### `{{action_2}}`
`{{action_description}}`
Params: `{{param_name}}` ({{type}}, {{required|optional}}): `{{param_description}}`
Selector: `{{selector_string}}` (`{{strategy}}`)
Fallback: `{{fallback_selector}}` (`{{fallback_strategy}}`)
Returns: `{{return_description}}`
### `{{action_3}}`
`{{action_description}}`
Params: `{{param_name}}` ({{type}}, {{required|optional}}): `{{param_description}}`
Returns: `{{return_description}}`
## Selectors
Priority order: `{{strategy_1}}` > {{strategy_2}} > `{{strategy_3}}`
1. `{{strategy_1}}` ({{example_selector}}): `{{why_this_is_primary}}`
2. `{{strategy_2}}` ({{example_selector}}): `{{why_this_is_secondary}}`
3. `{{strategy_3}}` ({{example_selector}}): `{{why_this_is_fallback}}`
Fallback rule: `{{describe_fallback_behavior_on_null_result}}`
## Output Format
Primary: {{json|html|screenshot|text}}
Schema:
```json
{
  "{{field_1}}": "{{type}}",
  "{{field_2}}": "{{type}} | null",
  "{{field_3}}": "{{type}}"
}
```
