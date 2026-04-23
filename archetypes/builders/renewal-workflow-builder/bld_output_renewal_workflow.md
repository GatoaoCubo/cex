---
kind: output_template
id: bld_output_template_renewal_workflow
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for renewal_workflow production
quality: 9.1
title: "Output Template Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, output_template, renewal, GRR, Gainsight]
tldr: "Template with vars for renewal_workflow production"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_renewal_workflow
  - bld_examples_renewal_workflow
  - bld_knowledge_card_renewal_workflow
  - bld_config_renewal_workflow
  - p12_sp_renewal_workflow_builder
  - renewal-workflow-builder
  - p10_lr_renewal_workflow_builder
  - bld_schema_renewal_workflow
  - bld_collaboration_renewal_workflow
  - bld_tools_renewal_workflow
---

```yaml
---
id: p12_rw_{{name}}.yaml
kind: renewal_workflow
pillar: P12
title: "{{account_name}} Renewal Workflow -- {{contract_end_date}}"
contract_id: {{contract_id}}
renewal_stage: {{stage}}              # 90_day / 60_day / 30_day / closed
days_to_renewal: {{days}}
GRR_impact: {{grr_impact}}            # full / contraction_{{pct}} / churn
multi_year_flag: {{multi_year}}       # true / false
current_ARR: "{{current_ARR}}"
renewal_ARR: "{{renewal_ARR}}"
health_score: {{health_score}}        # 0-100 Gainsight score
price_increase_pct: "{{price_pct}}"
auto_renewal: {{auto_renewal}}        # true / false
notice_period_days: {{notice_days}}
quality: null
version: "1.0.0"
created: {{date}}
updated: {{date}}
author: {{author}}
domain: "SaaS renewal -- {{segment}} segment"
tags: [renewal_workflow, renewal, GRR, {{stage}}]
tldr: "{{stage}} renewal workflow for {{account_name}}, {{days}} days to {{contract_end_date}}"
---

# Renewal Stage Map
## 90-Day Stage (Owner: {{owner_90}})
Tasks:
  - Send renewal intent email -- relationship-first, no commercial pressure
  - Review health score and flag accounts <60 for escalation
  - Identify multi-year opportunity: tenure >2yr + health >75
  - Confirm economic buyer and procurement contact
Automation Triggers:
  - Gainsight CTA: "Renewal 90 Days" fires when days_to_renewal = 90
  - Salesforce Opportunity Stage: set to "Renewal Identified"
  - Alert: health score <60 -> escalate to {{escalation_owner_1}}

## 60-Day Stage (Owner: {{owner_60}})
Tasks:
  - Send formal renewal proposal with price-increase notice
  - Present multi-year incentive if flagged ({{multi_year_discount}}% for 2yr)
  - Run QBR or business review to reinforce value
  - Negotiate contract terms and discount authority check
Automation Triggers:
  - Gainsight CTA: "Renewal 60 Days" fires when days_to_renewal = 60
  - Salesforce Opportunity Stage: set to "Renewal Proposed"
  - Alert: no response in 7 days -> escalate to {{escalation_owner_2}}

## 30-Day Stage (Owner: {{owner_30}})
Tasks:
  - Final close call with economic buyer
  - Legal redlines and contract amendment review
  - Confirm auto-renewal opt-out window compliance
  - Initiate procurement PO process
Automation Triggers:
  - Gainsight CTA: "Renewal 30 Days -- URGENT" fires when days_to_renewal = 30
  - Salesforce Opportunity Stage: set to "Renewal Close Expected"
  - Alert: no signed contract in 10 days -> escalate to {{escalation_owner_3}}

# Price Increase Playbook
Announcement Timing: 90-day stage
Price Increase: {{price_pct}}% uplift on base ARR
Approval Authority: CSM up to {{csm_discount}}%, Manager up to {{mgr_discount}}%, VP up to {{vp_discount}}%
Objection: "Budget constraints" -> Response: "{{budget_objection_response}}"
Objection: "No value increase" -> Response: "{{value_objection_response}}"
Objection: "Competitor pricing" -> Response: "{{competitor_objection_response}}"

# Multi-Year Offer
2-Year: {{discount_2yr}}% discount on Year 2 (approval: {{approval_2yr}})
3-Year: {{discount_3yr}}% discount on Years 2-3 (approval: {{approval_3yr}})
Incentive Framing: "Lock in current pricing and avoid annual increases."

# Escalation Path
| Health Score | Stage Failure         | Escalate To          | SLA     |
|--------------|-----------------------|----------------------|---------|
| <75          | 90-day no response    | CSM Manager          | 48 hours|
| <60          | 60-day no proposal    | VP Customer Success  | 24 hours|
| <40          | 30-day no close       | CRO + CFO            | Same day|

# Auto-Renewal Compliance
| Jurisdiction | Notice Period | Opt-Out Method        | Audit Trail        |
|--------------|---------------|-----------------------|--------------------|
| California   | 30 days       | Written notice to CS  | Email + CRM log    |
| EU (GDPR)    | 30 days       | Written or electronic | Contract amendment |
| Australia    | 21 days       | Written notice        | Signed acknowledgment|

# GRR Model
| Scenario        | ARR Impact          | Notes                            |
|-----------------|---------------------|----------------------------------|
| Full Renewal    | {{current_ARR}}     | + {{price_pct}}% uplift if applied|
| Contraction     | -{{contraction_pct}}%| Scope reduction scenario         |
| Churn           | -{{current_ARR}}    | Full account loss scenario       |
| Net GRR         | {{grr_pct}}%        | (Retained ARR) / (Beginning ARR) |
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_renewal_workflow]] | upstream | 0.66 |
| [[bld_examples_renewal_workflow]] | downstream | 0.61 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.60 |
| [[bld_config_renewal_workflow]] | downstream | 0.57 |
| [[p12_sp_renewal_workflow_builder]] | downstream | 0.57 |
| [[renewal-workflow-builder]] | downstream | 0.57 |
| [[p10_lr_renewal_workflow_builder]] | downstream | 0.55 |
| [[bld_schema_renewal_workflow]] | downstream | 0.54 |
| [[bld_collaboration_renewal_workflow]] | downstream | 0.48 |
| [[bld_tools_renewal_workflow]] | upstream | 0.43 |
