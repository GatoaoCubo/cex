---
kind: instruction
id: bld_instruction_churn_prevention_playbook
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for churn_prevention_playbook
quality: 8.9
title: "Instruction Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, instruction]
tldr: "Step-by-step production process for churn_prevention_playbook"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - churn-prevention-playbook-builder
  - bld_output_template_churn_prevention_playbook
  - p03_qg_churn_prevention_playbook
  - p03_sp_churn_prevention_playbook_builder
  - bld_instruction_renewal_workflow
  - bld_collaboration_churn_prevention_playbook
  - p10_lr_renewal_workflow_builder
  - bld_knowledge_card_churn_prevention_playbook
  - bld_config_renewal_workflow
  - bld_knowledge_card_renewal_workflow
---

## Phase 1: RESEARCH
1. Identify churn signals: map health score components (usage, NPS, support tickets, QBR cadence).
2. Define at-risk thresholds: red (<40), yellow (40-60), green (>60) on 100-point scale.
3. Inventory churn reason taxonomy: product gap, budget cut, competitor switch, champion departure.
4. Audit historical saves: what interventions worked, what failed, at what health score range.
5. Map escalation chain: CSM -> CS Manager -> VP CS -> executive sponsor.
6. Identify win-back window: 30/60/90-day post-churn re-engagement viability.

## Phase 2: COMPOSE
1. Reference bld_schema_churn_prevention_playbook.md for required frontmatter (id, kind, pillar, health_score_model).
2. Write health score definition: components, weights, thresholds.
3. Define intervention triggers: score delta, days-inactive, days-to-renewal.
4. Write save-the-account script sections: opening, discovery, objection handlers, close.
5. Write win-back sequence: 30-day (acknowledge), 60-day (new value prop), 90-day (final offer).
6. Map Gainsight CTAs: trigger conditions, assignee, due date SLA.
7. Define success criteria: what constitutes a "save" (renewal signed, health restored).
8. Reference bld_output_template_churn_prevention_playbook.md for section structure.
9. Cross-reference nps_survey kind for detractor signal integration.

## Phase 3: VALIDATE
- [ ] Health score model covers all 5 components (usage, NPS, support, engagement, contract).
- [ ] Intervention triggers cover all three risk bands (red, yellow, at-contract-renewal).
- [ ] Save script has opening, discovery, objection handling, and close sections.
- [ ] Win-back sequence has at least 3 touchpoints (30/60/90-day).
- [ ] Escalation path is fully defined (CSM -> VP CS minimum).
- [ ] Domain keywords present: churn, retention, health-score, save, win-back, at-risk.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[churn-prevention-playbook-builder]] | related | 0.40 |
| [[bld_output_template_churn_prevention_playbook]] | downstream | 0.40 |
| [[p03_qg_churn_prevention_playbook]] | downstream | 0.39 |
| [[p03_sp_churn_prevention_playbook_builder]] | related | 0.36 |
| [[bld_instruction_renewal_workflow]] | sibling | 0.33 |
| [[bld_collaboration_churn_prevention_playbook]] | downstream | 0.30 |
| [[p10_lr_renewal_workflow_builder]] | downstream | 0.27 |
| [[bld_knowledge_card_churn_prevention_playbook]] | upstream | 0.27 |
| [[bld_config_renewal_workflow]] | downstream | 0.27 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.25 |
