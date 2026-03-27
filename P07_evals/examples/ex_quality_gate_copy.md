---
id: ex_quality_gate_copy
kind: quality_gate
pillar: P07
title: Copywriting Quality Gate
tags: [quality, gate, copy, evaluation]
references:
  - tpl_quality_gate
  - ex_agent_copywriter
  - ex_response_format_ad_copy
  - ex_prompt_template_aida
---

# Copywriting Quality Gate

> Skeleton: quality_gate kind (self-evaluation criteria)

| Criterion | Minimum | Weight |
|-----------|---------|--------|
| Clarity | >= 8 | 25% |
| Persuasion | >= 9 | 30% |
| Specificity | >= 8 | 20% |
| CTA strength | >= 9 | 25% |

Fail action: regenerate with feedback on weakest criterion.

## Links

- Evaluates: [[ex_agent_copywriter]]
- Checks format: [[ex_response_format_ad_copy]]
- Checks method: [[ex_prompt_template_aida]]
- Function: GOVERN (is it good enough?)
