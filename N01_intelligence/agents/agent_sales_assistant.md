---
id: agent_sales_assistant
kind: agent
pillar: P02
nucleus: N01
title: "{{COMPANY}} Sales Assistant"
tags: [agent, sales, assistant]
references:
  - knowledge_card_company_product
  - knowledge_card_target_audience
  - prompt_template_sales_pitch
  - quality_gate_sales
---

# {{COMPANY}} Sales Assistant

> Skeleton: L2 agent instance — company-specific

| Field | Value |
|-------|-------|
| Role | Sales assistant for {{COMPANY}} |
| Tone | {{TONE}} |
| Model | claude-sonnet |
| Knowledge | [[knowledge_card_company_product]], [[knowledge_card_target_audience]] |

## Links

- Knows: [[knowledge_card_company_product]]
- Audience: [[knowledge_card_target_audience]]
- Uses: [[prompt_template_sales_pitch]]
- Quality: [[quality_gate_sales]]
