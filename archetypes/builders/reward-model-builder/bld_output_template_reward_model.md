---
kind: output_template
id: bld_output_template_reward_model
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for reward_model production
quality: 9.0
title: "Output Template Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, output_template]
tldr: "Template with vars for reward_model production"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
id: p07_rwm_{{slug}}               # e.g. p07_rwm_dialogue_quality
kind: reward_model
pillar: P07
title: "{{Reward Model Name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_team}}"
domain: "{{domain, e.g. dialogue, code generation, safety}}"
quality: null                      # NEVER self-score
tags: [reward_model, "{{domain_tag}}", "{{reward_type_tag}}"]
tldr: "{{One concrete sentence: what behavior is rewarded, via what mechanism}}"
reward_type: "{{process|outcome}}" # process=step-level, outcome=final-level
calculation_method: "{{formula or logic, e.g. weighted sum of rubric scores}}"
max_reward_amount: {{float}}       # cap limit; 0 = uncapped
```

## Overview
<!-- Purpose: what alignment objective this model encodes.
     Scope: what agent behaviors it evaluates.
     Governance: ISO/IEC 23894 or AI Act clause if applicable. -->

## Calculation Method
<!-- Mathematical expression for reward computation.
     Variables: define each term.
     Edge cases: what happens at 0, max, adversarial inputs. -->
```
R(x) = {{formula}}
where:
  {{var}} = {{definition}}
```

## Reward Parameters
| Parameter | Type | Range | Semantics |
|-----------|------|-------|-----------|
| `{{param}}` | float | [0, 1] | `{{what higher values mean}}` |
| weight_`{{criterion}}` | float | [0, 1] | Importance of `{{criterion}}` |

## Eligibility Criteria
<!-- Conditions under which the reward applies.
     Exclusions: behaviors explicitly excluded from reward. -->
- ELIGIBLE: `{{specific conditions}}`
- EXCLUDED: {{adversarial patterns, out-of-scope behaviors}}

## Distribution Schedule
<!-- When and how rewards are applied.
     Frequency: per-step, per-episode, per-evaluation.
     Normalization: z-score, clipping, scaling. -->

## Compliance and Auditing
- Explainability: `{{how reward components can be inspected}}`
- Auditability: {{logging requirements, review cadence}}
- Bias check: `{{method to detect reward hacking or proxy gaming}}`
