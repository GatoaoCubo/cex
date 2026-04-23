---
kind: output_template
id: bld_output_template_product_tour
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for product_tour production
quality: 9.1
title: "Output Template Product Tour"
version: "1.0.1"
author: n02_marketing
tags: [product_tour, builder, output_template]
tldr: "Template with vars for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_product_tour
  - product-tour-builder
  - bld_instruction_product_tour
  - bld_schema_product_tour
  - p03_sp_product_tour_builder
  - kc_product_tour
  - bld_tools_product_tour
  - bld_knowledge_card_product_tour
  - bld_config_product_tour
  - bld_instruction_chain
---

<!-- Product tour spec template. In-app tooltip/step structure. Replace all {{vars}}. -->

```yaml
---
id: p05_pt_{{name}}
kind: product_tour
pillar: P05
quality: null
title: {{title}}
product: {{product_name}}
trigger_event: {{trigger_event}}
target_persona: {{target_persona}}
activation_goal: {{activation_goal}}
platform: {{platform}}
---

## Tour Metadata
| Field | Value |
|---|---|
| tour_id | p05_pt_{{name}} |
| version | {{version}} |
| locale_default | {{locale}} |
| estimated_duration | {{duration_seconds}}s |
| skip_allowed | {{skip_allowed}} |
| analytics_event_prefix | {{analytics_prefix}} |

## Tour Steps
| step_id | title | target_element | tooltip_position | content | trigger_condition | analytics_event |
|---|---|---|---|---|---|---|
| step_1 | {{step1_title}} | {{step1_selector}} | {{step1_position}} | {{step1_content}} | {{step1_trigger}} | {{step1_event}} |
| step_2 | {{step2_title}} | {{step2_selector}} | {{step2_position}} | {{step2_content}} | {{step2_trigger}} | {{step2_event}} |
| step_3 | {{step3_title}} | {{step3_selector}} | {{step3_position}} | {{step3_content}} | {{step3_trigger}} | {{step3_event}} |
| step_4 | {{step4_title}} | {{step4_selector}} | {{step4_position}} | {{step4_content}} | {{step4_trigger}} | {{step4_event}} |
| step_5 | {{step5_title}} | {{step5_selector}} | {{step5_position}} | {{step5_content}} | {{step5_trigger}} | {{step5_event}} |

## Trigger Configuration
| Trigger Type | Condition | Priority |
|---|---|---|
| entry | {{entry_trigger}} | high |
| exit | {{exit_trigger}} | medium |
| skip | user clicks skip or presses Esc | low |
| completion | all steps viewed | high |

## Accessibility
| Requirement | Value |
|---|---|
| aria_role | tooltip |
| aria_live | polite |
| keyboard_nav | Tab/Shift+Tab between steps, Esc to skip |
| focus_trap | enabled during spotlight overlay |
| color_contrast | WCAG 2.1 AA (4.5:1 minimum) |

## Localization
| locale | title | cta_label |
|---|---|---|
| {{locale_1}} | {{title_locale_1}} | {{cta_locale_1}} |
| {{locale_2}} | {{title_locale_2}} | {{cta_locale_2}} |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_product_tour]] | downstream | 0.31 |
| [[product-tour-builder]] | related | 0.30 |
| [[bld_instruction_product_tour]] | upstream | 0.29 |
| [[bld_schema_product_tour]] | downstream | 0.28 |
| [[p03_sp_product_tour_builder]] | upstream | 0.27 |
| [[kc_product_tour]] | upstream | 0.26 |
| [[bld_tools_product_tour]] | upstream | 0.26 |
| [[bld_knowledge_card_product_tour]] | upstream | 0.26 |
| [[bld_config_product_tour]] | downstream | 0.24 |
| [[bld_instruction_chain]] | upstream | 0.18 |
