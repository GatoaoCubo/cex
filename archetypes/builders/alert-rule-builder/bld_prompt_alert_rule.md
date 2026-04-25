---
quality: 7.8
id: bld_instruction_alert_rule
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for alert_rule
version: 1.0.0
quality: 7.3
tags: [alert_rule, builder, instruction]
title: "Instruction Alert Rule Builder"
author: builder
tldr: "Step-by-step production process for alert_rule"
density_score: 0.86
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p03_ins_optimizer
  - p11_qg_validator
  - bld_instruction_golden_test
  - p03_sp_validator-builder
  - bld_instruction_instruction
  - bld_instruction_builder
  - bld_instruction_kind
  - bld_instruction_memory_scope
  - bld_instruction_action_prompt
  - bld_instruction_output_validator
---
# Instructions: How to Produce an alert_rule
## Phase 1: IDENTIFY
1. Name the condition being monitored (what metric or signal)
2. Determine the numeric threshold (>= 95%, < 100ms, > 500)
3. Select severity: critical (page now), warning (ticket), info (log only)
4. Determine for duration: how long must condition hold before firing (0s = instant)
5. Identify routing target: who or what handles this alert
6. Determine if automated response is possible (restart, scale, rollback)
## Phase 2: COMPOSE
1. Read bld_schema_alert_rule.md for required fields
2. Set id: ar_{system}_{metric}_{condition} (snake_case)
3. Write metric_expression as a PromQL-style or logical expression
4. Set severity from controlled list: critical | warning | info
5. Set for_duration: ISO duration (0s, 5m, 15m, 1h)
6. Set routing: team channel, PagerDuty policy, or webhook
7. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates:
   - id follows pattern ar_{system}_{metric}
   - kind == alert_rule
   - quality == null
   - metric_expression present with numeric threshold
   - severity from controlled list
   - routing target present
2. SOFT gates:
   - for_duration prevents flapping (>= 1m recommended for non-critical)
   - runbook_url or remediation_steps present
   - automated_response defined (auto-scale, restart, etc.)
   - labels/annotations for Prometheus compatibility


## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | sibling | 0.25 |
| [[p11_qg_validator]] | downstream | 0.24 |
| [[bld_instruction_golden_test]] | sibling | 0.24 |
| [[p03_sp_validator-builder]] | related | 0.23 |
| [[bld_instruction_instruction]] | sibling | 0.22 |
| [[bld_instruction_builder]] | sibling | 0.21 |
| [[bld_instruction_kind]] | sibling | 0.21 |
| [[bld_instruction_memory_scope]] | sibling | 0.20 |
| [[bld_instruction_action_prompt]] | sibling | 0.20 |
| [[bld_instruction_output_validator]] | sibling | 0.20 |
