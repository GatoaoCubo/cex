---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a runtime_rule artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: runtime_rule

```yaml
---
id: p09_rr_{{rule_slug}}
kind: runtime_rule
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
rule_name: "{{human_readable_rule_name}}"
rule_type: {{timeout|retry|rate_limit|circuit_breaker|concurrency}}
scope: "{{component_or_operation}}"
quality: null
tags: [runtime_rule, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_rule_governs_max_200ch}}"
fallback: "{{behavior_when_rule_triggers}}"
severity: {{critical|high|medium|low}}
---
```

## Rule Specification
{{concrete_parameters_with_units}}

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| {{param_1}} | {{value_1}} | {{unit_1}} | {{notes_1}} |
| {{param_2}} | {{value_2}} | {{unit_2}} | {{notes_2}} |

## Trigger Behavior
{{what_happens_when_rule_activates}}
{{fallback_behavior_details}}

## Tuning Guide
{{how_to_adjust_and_safe_ranges}}
{{metrics_to_monitor}}

## References
- {{reference_1}}
