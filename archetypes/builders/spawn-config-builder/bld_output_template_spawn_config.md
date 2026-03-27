---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a spawn_config
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: spawn_config

```yaml
---
id: p12_spawn_{{mode_slug}}
kind: spawn_config
pillar: P12
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
title: "{{human_readable_title}}"
mode: {{solo|grid|continuous}}
satellite: {{satellite_name_or_list}}
model: "{{opus|sonnet|haiku}}"
flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  - "-p"
  {{...additional_flags}}
mcp_config: "{{path_to_mcp_json}}"
timeout: {{seconds}}
interactive: {{true|false}}
prompt_strategy: {{inline|handoff}}
domain: "{{domain_value}}"
quality: null
tags: [spawn_config, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
---
```

## Spawn Command
```powershell
{{spawn_command_powershell}}
```

## Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| mode | {{mode}} | {{why_this_mode}} |
| satellite | {{satellite}} | {{why_this_satellite}} |
| model | {{model}} | {{why_this_model}} |
| timeout | {{timeout}}s | {{why_this_timeout}} |
| interactive | {{interactive}} | {{why_interactive_or_not}} |

## Constraints
- {{constraint_1}}
- {{constraint_2}}
- {{constraint_3}}

## References
- {{reference_1}}
