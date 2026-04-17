---
id: bld_output_template_canary_config
kind: knowledge_card
pillar: P05
title: "Output Template: canary_config"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: 7.0
tags: [output_template, canary_config, P09]
llm_function: PRODUCE
tldr: "Canonical output template for canary_config artifacts."
density_score: null
---

# Output Template: canary_config

## Frontmatter Template
```yaml
---
id: p09_cc_{{name_slug}}
kind: canary_config
pillar: P09
version: 1.0.0
service_name: "{{service_name}}"
canary_version: "{{canary_version}}"
stable_version: "{{stable_version}}"
stages_count: {{stages_count}}
rollback_trigger_metric: "{{metric_name}}"
rollback_trigger_threshold: {{threshold}}
provider: {{provider}}
domain: "{{domain}}"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
quality: null
tags: [canary_config, {{domain}}]
tldr: "{{service_name}} canary: {{canary_version}} -> 100% over {{stages_count}} stages; rollback on {{metric_name}} > {{threshold}}"
---
```

## Body Template
```markdown
# {{service_name}} Canary Rollout

## Traffic Stages
| Stage | Canary % | Pause (min) | Analysis Interval (min) |
|-------|---------|-------------|------------------------|
| initial | 5 | {{pause_1}} | {{interval_1}} |
| phase_1 | 25 | {{pause_2}} | {{interval_2}} |
| phase_2 | 50 | {{pause_3}} | {{interval_3}} |
| complete | 100 | - | - |

## Rollback Triggers
- **Metric**: {{rollback_trigger_metric}}
- **Threshold**: > {{rollback_trigger_threshold}}
- **Action**: Rollback to {{stable_version}}

## Analysis Configuration
- **Provider**: {{provider}}
- **Metric Provider**: {{metric_provider}}
- **Success Condition**: `{{success_condition}}`
```
