---
kind: quality_gate
id: p11_qg_referral_program
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for referral_program
quality: 9.0
title: "Quality Gate Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for referral_program"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_referral_program
  - p03_sp_referral_program_builder
  - bld_instruction_referral_program
  - referral-program-builder
  - bld_knowledge_card_referral_program
  - bld_collaboration_referral_program
  - p10_mem_referral_program_builder
  - kc_referral_program
  - bld_schema_referral_program
  - bld_output_template_referral_program
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| Metric | Threshold | Operator | Scope |
|---|---|---|---|
| Viral coefficient | ≥1.5 | ≥ | Program design |
| Reward conversion rate | ≥10% | ≥ | User engagement |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid or missing YAML metadata |
| H02 | ID matches pattern ^p11_rp_[a-z][a-z0-9_]+.yaml$ | ID format mismatch |
| H03 | kind field matches 'referral_program' | Kind field incorrect |
| H04 | Referral link uniqueness enforced | Duplicate referral links allowed |
| H05 | Reward cap per user defined | No maximum reward limit |
| H06 | Program cooldown period ≥7 days | Cooldown period <7 days |
| H07 | Referral tracking system implemented | No tracking mechanism |
| H08 | Terms of use compliance checked | Missing legal compliance checks |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Viral coefficient design | 0.20 | 1.0-1.5 (1.0), 0.5-1.0 (0.5), <0.5 (0) |
| D2 | Reward clarity | 0.15 | Clear (1.0), Ambiguous (0.5), Missing (0) |
| D3 | User experience | 0.15 | Seamless (1.0), Moderate (0.5), Poor (0) |
| D4 | Legal compliance | 0.15 | Fully compliant (1.0), Partial (0.5), Non-compliant (0) |
| D5 | Scalability | 0.10 | Scalable (1.0), Limited (0.5), Non-scalable (0) |
| D6 | Conversion rate | 0.10 | >=10% (1.0), 5-10% (0.5), <5% (0) |
| D7 | Tracking accuracy | 0.15 | 100% (1.0), 75-99% (0.5), <75% (0) |

## Actions
(Table: Score | Action)
| Score | Action |
|---|---|
| ≥9.5 | GOLDEN: Deploy immediately |
| ≥8.0 | PUBLISH: Launch with monitoring |
| ≥7.0 | REVIEW: Fix minor issues |
| <7.0 | REJECT: Revise and resubmit |

## Bypass
(Table: conditions, approver, audit trail)
| Conditions | Approver | Audit Trail |
|---|---|---|
| Urgent business need | CTO | Documented approval + timestamp |

## Examples

## Golden Example  
```yaml  
kind: referral_program  
name: "Dropbox Referral Program"  
vendor: Dropbox Inc.  
description: "Incentivizes users to invite peers via tiered rewards and viral sharing mechanics."  
spec:  
  viral_coefficient: 2.5  
  reward_structure:  
    - level: 1  
      condition: "Invite 1 user"  
      reward: "5GB of storage"  
    - level: 5  
      condition: "Invite 5 users"  
      reward: "100GB of storage + $10 credit"  
  tracking:  
    - method: "Unique referral links with UTM parameters"  
    - attribution: "First-click model for credit assignment"  
  metrics:  
    - "Referral conversion rate"  
    - "Average number of referrals per user"  
```  

## Anti-Example 1: Missing Viral Coefficient  
```yaml  
kind: referral_program  
name: "FakeApp Referral Program"  
vendor: FakeApp LLC.  
description: "Users earn points for referrals, but no clear viral mechanics."  
spec:  
  reward_structure:  
    - level: 1  
      condition: "Invite 1 user"  
      reward: "10 points"  
  tracking:  
    - method: "Email-based referral codes"  
```  
## Why it fails  
No viral coefficient defined; users have no incentive to share beyond minimal rewards. Points system lacks scalability or urgency, leading to low participation.  

## Anti-Example 2: Unaligned Reward Structure  
```yaml  
kind: referral_program  
name: "BrokenReferral Program"  
vendor: BrokenCo Inc.  
description: "Rewards are given only after 100 referrals, deterring early engagement."  
spec:  
  viral_coefficient: 1.2  
  reward_structure:  
    - level: 100  
      condition: "Invite 100 users"  
      reward: "Free premium subscription"  
```  
## Why it fails  
Reward structure is too distant (100 invites) to motivate participation. High threshold creates friction, making the program ineffective for viral growth.

## Golden Example 2 -- B2B SaaS Cash Referral Program (CTO/VP Persona)

```yaml
kind: referral_program
id: rp_stackflow_b2b_saas_2026
name: "StackFlow B2B Referral Program"
vendor: "StackFlow Inc."
segment: B2B SaaS
target_personas: [CTO, VP Engineering, VP Product]
ACV_range: "$18,000 - $60,000"
description: >
  Cash reward referral program for StackFlow's CI/CD platform targeting
  technical leaders. Referrer receives $500 cash. Referee receives $200
  account credit. Attribution via HubSpot CRM with 90-day window.
  Viral coefficient target 1.8 within 12 months of launch.
spec:
  viral_coefficient_target: 1.8
  viral_coefficient_current: 0.0
  measurement_period_months: 12
  reward_structure:
    referrer:
      type: cash
      amount: "$500"
      trigger: "referee closes paid contract (not trial)"
      payout_method: "ACH via Tipalti"
      payout_delay_days: 30
      cap_per_referrer: "$5,000/yr (10 successful referrals)"
    referee:
      type: account_credit
      amount: "$200"
      applied_to: "first invoice"
      trigger: "contract signed and first payment processed"
      expiry_days: 90
  eligibility:
    referrer: "active paid customer, contract >= 6 months old"
    referee: "net-new logo -- no prior StackFlow contract, no open opportunity in HubSpot"
    excluded: "existing leads in HubSpot pipeline older than 30 days"
  tracking:
    crm: HubSpot
    attribution_window_days: 90
    attribution_model: "first-touch -- referrer link click or referrer-named email"
    referral_link_format: "https://stackflow.io/ref/{{referrer_hubspot_contact_id}}"
    utm_params:
      utm_source: referral
      utm_medium: customer
      utm_campaign: b2b_referral_2026
    hubspot_workflow: "Referral Attribution -- set Referred_By contact property on lead"
    hubspot_deal_property: "deal.referral_source (picklist: organic|referral|partner|paid)"
  persona_activation:
    primary_channel: "CSM outreach at 6-month health check (health score >= 75)"
    secondary_channel: "in-app banner on admin dashboard (dismissible, shown 1x/quarter)"
    email_sequence:
      - day: 0
        from: "CSM (named sender)"
        subject: "You could earn $500 -- and help a peer solve [pain point]"
        body_hook: >
          "You know the frustration of slow deploys better than anyone.
          If you know another CTO or VP Eng dealing with the same problem,
          they will thank you -- and so will we. $500 cash when they sign."
      - day: 7
        from: "CSM (named sender)"
        subject: "Quick reminder -- your referral link expires in 83 days"
        send_condition: "no referral link click in last 7 days"
  fraud_prevention:
    - rule: "referee domain must differ from referrer domain"
    - rule: "referee email must not appear in HubSpot contacts created before referral link click"
    - rule: "manual CSM review required if referrer and referee share same LinkedIn company"
    - rule: "payout held if referee churns within 90 days of contract start"
  metrics:
    primary:
      - name: viral_coefficient
        formula: "referrals_converted / active_referrers"
        target: 1.8
      - name: referral_CAC
        formula: "total_referral_rewards_paid / new_logos_from_referral"
        target: "< $1,200 (vs. $8,500 blended CAC)"
    secondary:
      - name: referral_participation_rate
        formula: "customers_with_1_referral_click / total_eligible_customers"
        target: "25% within 90 days of program launch"
      - name: referral_conversion_rate
        formula: "referrals_converted_to_paid / referrals_submitted"
        target: "> 20%"
      - name: referral_ACV
        target: "within 10% of organic ACV ($24,000 avg)"
  review_cadence: "monthly -- RevOps reviews HubSpot referral pipeline report"
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
