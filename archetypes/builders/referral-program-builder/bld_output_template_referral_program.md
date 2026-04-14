---
kind: output_template
id: bld_output_template_referral_program
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for referral_program production
quality: null
title: "Output Template Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, output_template]
tldr: "Template with vars for referral_program production"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```yaml
---
id: p11_rp_{{name}}.yaml
name: {{referral_program_name}} <!-- Program name -->
quality: null
pillars:
  - P11
description: {{program_description}} <!-- Brief overview -->
rules:
  - {{rule_1}} <!-- Rule text -->
  - {{rule_2}} <!-- Rule text -->
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
