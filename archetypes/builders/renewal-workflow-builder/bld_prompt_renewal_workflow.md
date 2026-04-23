---
kind: instruction
id: bld_instruction_renewal_workflow
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for renewal_workflow
quality: 8.9
title: "Instruction Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, instruction, renewal, GRR, Gainsight]
tldr: "Step-by-step production process for renewal_workflow"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_renewal_workflow
  - p10_lr_renewal_workflow_builder
  - bld_knowledge_card_renewal_workflow
  - p12_sp_renewal_workflow_builder
  - bld_config_renewal_workflow
  - renewal-workflow-builder
  - bld_examples_renewal_workflow
  - bld_schema_renewal_workflow
  - bld_collaboration_renewal_workflow
  - bld_instruction_churn_prevention_playbook
---

## Phase 1: RESEARCH
1. Identify contract end dates and segment them by ARR tier (strategic >$100K, growth $25-100K, velocity <$25K).
2. Extract customer health signals from Gainsight: health score, product adoption, support ticket volume, NPS.
3. Review renewal history: on-time renewals, late renewals, contraction events, churn risk flags.
4. Identify multi-year contract opportunities: customer tenure > 2 years + health score > 75.
5. Flag accounts for price-increase eligibility: contractual escalation clauses, CPI triggers, tier thresholds.
6. Map renewal decision-makers: economic buyer, procurement, legal sign-off authority.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for required fields (contract_id, renewal_stage, days_to_renewal, owner, GRR_impact).
2. Design 90/60/30-day stage workflow: assign owners, set tasks, define automation triggers.
3. Write renewal outreach templates for each stage (90-day relationship check, 60-day negotiation, 30-day close).
4. Build price-increase playbook: announce at 90-day, negotiate at 60-day, finalize at 30-day.
5. Configure Salesforce Opportunity fields: renewal_amount, contract_end_date, renewal_probability, multi_year_flag.
6. Set Gainsight CTA automation: health-score-driven renewal alerts, escalation triggers for <60 score.
7. Define escalation path: CSM -> CSM Manager -> VP CS at each stage failure point.
8. Structure multi-year incentive offer: 5-10% discount for 2-year, 10-15% for 3-year commitment.
9. Add compliance checkpoints: auto-renewal notice periods (30-90 days depending on jurisdiction).

## Phase 3: VALIDATE
- [ ] 90/60/30-day stages have defined owners, tasks, and automation triggers.
- [ ] Price-increase playbook specifies percentage, timing, and objection responses.
- [ ] Multi-year offer has discount range and approval authority defined.
- [ ] Escalation path covers all three tiers (CSM, Manager, VP).
- [ ] Auto-renewal compliance includes jurisdiction-specific notice periods.
- [ ] GRR impact calculated for each renewal scenario (full renewal, contraction, churn).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_renewal_workflow]] | downstream | 0.57 |
| [[p10_lr_renewal_workflow_builder]] | downstream | 0.56 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.55 |
| [[p12_sp_renewal_workflow_builder]] | downstream | 0.54 |
| [[bld_config_renewal_workflow]] | downstream | 0.51 |
| [[renewal-workflow-builder]] | downstream | 0.50 |
| [[bld_examples_renewal_workflow]] | downstream | 0.49 |
| [[bld_schema_renewal_workflow]] | downstream | 0.43 |
| [[bld_collaboration_renewal_workflow]] | downstream | 0.39 |
| [[bld_instruction_churn_prevention_playbook]] | sibling | 0.38 |
