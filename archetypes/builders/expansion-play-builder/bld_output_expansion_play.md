---
kind: output_template
id: bld_output_template_expansion_play
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for expansion_play production
quality: 9.1
title: "Output Template Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, output_template, upsell, NRR, land-and-expand]
tldr: "Template with vars for expansion_play production"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_expansion_play
  - bld_schema_expansion_play
  - bld_instruction_expansion_play
  - bld_knowledge_card_expansion_play
  - p03_sp_expansion_play_builder
  - p03_qg_expansion_play
  - expansion-play-builder
  - p10_mem_expansion_play_builder
  - bld_config_expansion_play
  - bld_tools_expansion_play
---

```markdown
---
id: p03_ep_{{name}}.md
kind: expansion_play
pillar: P03
title: "{{account_name}} -- {{expansion_type}} Expansion Play"
account_segment: {{segment}}           # SMB / MM / ENT
expansion_type: {{expansion_type}}     # seat_upsell / tier_upgrade / cross_sell / usage_ramp
trigger_type: {{trigger_type}}         # usage_threshold / feature_adoption / QBR_signal
NRR_target: "{{NRR_target}}"           # e.g., ">120%"
current_ARR: "{{current_ARR}}"
expansion_ARR: "{{expansion_ARR}}"
quality: null
version: "1.0.0"
created: {{date}}
updated: {{date}}
author: {{author}}
domain: "SaaS expansion -- {{segment}} segment"
tags: [expansion_play, {{expansion_type}}, NRR, upsell]
tldr: "{{expansion_type}} play for {{account_name}} targeting {{expansion_ARR}} expansion ARR"
---

## Expansion Trigger
| Signal                  | Threshold                    | Time Window | Alert Owner |
|-------------------------|------------------------------|-------------|-------------|
| {{trigger_metric}}      | {{trigger_threshold}}        | {{window}}  | {{owner}}   |
| Seat utilization        | >80% of licensed seats       | 14 days     | CSM         |
| Feature adoption rate   | >60% of target feature set   | 30 days     | CSM         |

## Account Map
| Role              | Name / Title        | Influence | Action            |
|-------------------|---------------------|-----------|-------------------|
| Economic Buyer    | {{buyer_name}}      | High      | Final approval    |
| Champion          | {{champion_name}}   | High      | Internal advocate |
| Blocker           | {{blocker_name}}    | Medium    | Address objections|
| Procurement       | {{procurement}}     | Low       | Contract sign-off |

## Expansion Motion
**Type**: {{expansion_type}}
**SKU**: {{sku_name}}
**Current**: {{current_seats_or_tier}} | **Target**: {{target_seats_or_tier}}
**Delta ARR**: {{expansion_ARR}}
**Attach Rate Benchmark**: {{attach_rate}}% for {{segment}} segment

## NRR Model
| Component          | ARR Impact       | Notes                        |
|--------------------|------------------|------------------------------|
| Beginning ARR      | {{current_ARR}}  | Contract value at period open|
| Expansion ARR      | +{{expansion_ARR}}| From this play               |
| Contraction Risk   | -{{contraction}} | Identified risk factors      |
| Projected NRR      | {{NRR_pct}}%     | (Begin + Expansion - Contraction) / Begin |

## AE/CSM Talk Track
**Hook**: "{{hook_statement}}"
**Value Statement**: "{{value_statement}}"
**Business Case**: "{{business_case}}"
**Ask**: "{{specific_ask}}"
**Next Step**: {{next_step_action}} by {{next_step_date}}

## QBR Structure
1. Value Delivered: {{metric_1}}, {{metric_2}}, {{metric_3}}
2. Expansion Opportunity: {{opportunity_statement}}
3. Success Metrics for Next Period: {{success_metric_1}}, {{success_metric_2}}

## Objection Handling
| Objection               | Response                          | Fallback               |
|-------------------------|-----------------------------------|------------------------|
| Budget freeze           | {{budget_response}}               | ROI calculation offer  |
| Contract timing         | {{timing_response}}               | Bridge amendment option|
| Competing priorities    | {{priority_response}}             | Champion re-engagement |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_expansion_play]] | downstream | 0.58 |
| [[bld_schema_expansion_play]] | downstream | 0.58 |
| [[bld_instruction_expansion_play]] | upstream | 0.57 |
| [[bld_knowledge_card_expansion_play]] | upstream | 0.47 |
| [[p03_sp_expansion_play_builder]] | upstream | 0.41 |
| [[p03_qg_expansion_play]] | downstream | 0.40 |
| [[expansion-play-builder]] | upstream | 0.37 |
| [[p10_mem_expansion_play_builder]] | downstream | 0.33 |
| [[bld_config_expansion_play]] | downstream | 0.29 |
| [[bld_tools_expansion_play]] | upstream | 0.28 |
