---
kind: output_template
id: bld_output_template_referral_program
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for referral_program production
quality: 8.8
title: "Output Template Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, output_template]
tldr: "Template with vars for referral_program production"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_referral_program
  - bld_examples_referral_program
  - kc_referral_program
  - bld_examples_reward_model
  - bld_config_referral_program
  - bld_knowledge_card_reward_model
  - bld_output_template_reward_model
  - reward-model-builder
  - bld_schema_referral_program
  - bld_output_template_integration_guide
---

```yaml
---
id: p11_rp_{{name}}.yaml
kind: referral_program
pillar: P11
quality: null
title: {{program_title}}
name: {{referral_program_name}}
description: {{program_description}}
viral_coefficient_target: {{k_factor_float}}
reward_model: {{double_sided|single_sided|tiered}}
tags: [referral_program, {{product_name}}, plg]
tldr: "{{one_sentence_summary}}"
domain: referral_program construction
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author_name}}
rules:
  - {{rule_1}}
  - {{rule_2}}
---
## Referral Tiers
| Tier | Referrals Required | Reward |
|------|-------------------|--------|
| {{tier_1}} <!-- Tier name --> | {{number}} <!-- Minimum referrals --> | {{reward}} <!-- Bonus amount --> |
| {{tier_2}} <!-- Tier name --> | {{number}} <!-- Minimum referrals --> | {{reward}} <!-- Bonus amount --> |

## API Integration Example
```python
def create_referral(code):
    # {{api_endpoint}} <!-- API URL -->
    payload = {
        "referral_code": code,
        "user_id": "{{user_id}}" <!-- Target user ID -->
    }
    return requests.post("{{api_url}}", json=payload)
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_referral_program]] | upstream | 0.26 |
| [[bld_examples_referral_program]] | downstream | 0.26 |
| [[kc_referral_program]] | upstream | 0.25 |
| [[bld_examples_reward_model]] | downstream | 0.22 |
| [[bld_config_referral_program]] | downstream | 0.21 |
| [[bld_knowledge_card_reward_model]] | upstream | 0.21 |
| [[bld_output_template_reward_model]] | sibling | 0.21 |
| [[reward-model-builder]] | downstream | 0.20 |
| [[bld_schema_referral_program]] | downstream | 0.20 |
| [[bld_output_template_integration_guide]] | sibling | 0.19 |
