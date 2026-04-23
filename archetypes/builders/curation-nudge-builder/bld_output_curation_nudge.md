---
quality: 8.4
quality: 8.0
id: p11_out_tpl_curation_nudge
kind: output_template
pillar: P05
llm_function: PRODUCE
purpose: P05 output shape for curation_nudge artifacts
title: "Output Template: Curation Nudge"
version: "1.0.0"
author: n03_hermes_w1_8
tags: [output_template, curation_nudge, builder, p05, p11, memory]
domain: "curation_nudge construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.89
related:
  - p03_ins_router
  - bld_examples_memory_summary
  - bld_collaboration_memory_type
  - p06_is_quality_audit
  - p03_ins_prompt_template
  - p10_lr_input_schema_builder
  - schema_prompt_template_builder
  - bld_output_template_input_schema
  - bld_memory_session_state
  - p01_kc_server_tools
---

## Output Shape

Every `curation_nudge` artifact must follow this exact structure:

### Frontmatter (required)

```yaml
---
id: cn_{{trigger_type}}
kind: curation_nudge
pillar: P11
title: "Curation Nudge: {{trigger_label}}"
trigger:
  type: {{trigger_type}}
  threshold: {{threshold}}
cadence:
  min_interval_turns: {{min_interval_turns}}
  max_per_session: {{max_per_session}}
prompt_template: "Notei {{observation}}. {{action_question}}"
target_memory:
  destination: {{destination}}
  auto_write_if_confirmed: {{auto_write}}
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory]
upstream_source: "NousResearch/hermes-agent"
---
```

### Body (required sections)

```markdown
## Nudge: {{trigger_label}}

### Trigger Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Trigger type | {{trigger_type}} | {{trigger_semantics}} |
| Threshold | {{threshold}} | {{threshold_rationale}} |
| Min interval | {{min_interval_turns}} turns | Prevents nudge spam |
| Max per session | {{max_per_session}} | Hard session cap |

### Prompt Template

```
{{prompt_template}}
```

Replace `{{observation}}` at runtime with the specific observation text.
Example: "Notei que o usuario prefere {{specific_preference}}. Persistir?"

### Target Memory

| Field | Value | Description |
|-------|-------|-------------|
| Destination | {{destination}} | {{destination_rationale}} |
| Auto-write | {{auto_write}} | {{auto_write_description}} |

### Boundaries

- NOT `guardrail` (P11): guardrails BLOCK actions; nudges ASK
- NOT `quality_gate` (P11): quality_gate is pass/fail; nudge is informational
- NOT `notifier` (P04): notifiers broadcast externally; nudge is in-session self-prompt
- NOT `memory_summary` (P10): summary compresses; nudge triggers persistence decision

### Usage in agent session

```yaml
curation_nudge:
  nudge_ref: cn_{{trigger_type}}
  fire_every: {{threshold}} {{trigger_type}}
  on_confirm: write_to {{destination}}
  on_reject: increment_counter, check_next_threshold
```
```

## Variable Reference

| Variable | Type | Source |
|----------|------|--------|
| `{{trigger_type}}` | enum | turn_count \| density_threshold \| tool_call_count \| user_correction |
| `{{trigger_label}}` | string | Human-readable trigger name (e.g., "Every 10 Turns") |
| `{{threshold}}` | int | From input or trigger-type default (minimum 5) |
| `{{min_interval_turns}}` | int | Default 5 (anti-spam) |
| `{{max_per_session}}` | int | Default 3 (context cap) |
| `{{observation}}` | runtime | Substituted by agent at fire time |
| `{{destination}}` | enum | MEMORY.md \| entity_memory \| knowledge_card |
| `{{auto_write}}` | bool | Default true |

## Size Budget
- Target: 600-1400 bytes
- Maximum: 2048 bytes
- Density target: >= 0.85 (structured content preferred)
- Naming: `p11_cn_{{trigger_type}}.yaml` (H02 enforces pattern match)
- Required tag: `hermes_origin` (provenance marker for HERMES-derived artifacts)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_router]] | upstream | 0.19 |
| [[bld_examples_memory_summary]] | downstream | 0.19 |
| [[bld_collaboration_memory_type]] | downstream | 0.18 |
| [[p06_is_quality_audit]] | downstream | 0.18 |
| [[p03_ins_prompt_template]] | upstream | 0.17 |
| [[p10_lr_input_schema_builder]] | downstream | 0.16 |
| [[schema_prompt_template_builder]] | downstream | 0.16 |
| [[bld_output_template_input_schema]] | sibling | 0.16 |
| [[bld_memory_session_state]] | downstream | 0.16 |
| [[p01_kc_server_tools]] | upstream | 0.16 |
