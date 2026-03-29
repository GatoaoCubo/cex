---
id: quality_gate_sales
kind: quality_gate
pillar: P07
nucleus: N02
title: Sales Content Quality Gate
tags: [quality, gate, sales, marketing]
references:
  - agent_sales_assistant
  - prompt_template_sales_pitch
  - ex_quality_gate_copy
---

# Sales Content Quality Gate

> Skeleton: L2 quality instance — inherits from L1 gate

| Criterion | Min | Source |
|-----------|-----|--------|
| Clarity | >= 8 | [[ex_quality_gate_copy]] |
| Persuasion | >= 9 | [[ex_quality_gate_copy]] |
| Brand alignment | >= 8 | Company-specific |
| CTA actionable | >= 9 | Company-specific |

## Links

- Inherits from: [[ex_quality_gate_copy]] (L1)
- Validates: [[agent_sales_assistant]]
- Checks: [[prompt_template_sales_pitch]]
