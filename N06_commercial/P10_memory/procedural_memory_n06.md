---
id: procedural_memory_n06
kind: procedural_memory
8f: F3_inject
pillar: P10
nucleus: n06
title: "Procedural Memory -- N06 Commercial Standard Operating Procedures"
version: 1.0.0
quality: 9.0
tags: [procedural-memory, sop, commercial, deals, escalation, renewal, operations]
density_score: 0.98
related:
  - bld_instruction_renewal_workflow
  - bld_output_template_churn_prevention_playbook
  - p10_lr_renewal_workflow_builder
  - bld_config_renewal_workflow
  - bld_examples_renewal_workflow
  - bld_output_template_renewal_workflow
  - bld_knowledge_card_renewal_workflow
  - bld_instruction_churn_prevention_playbook
  - n06_funnel_cex_product
  - p12_sp_renewal_workflow_builder
---

# Procedural Memory: N06 Commercial SOPs

## Purpose

Encodes N06's repeatable commercial procedures as procedural memory. When N06 encounters a known commercial scenario (new deal, renewal, escalation, pricing question), this memory provides the exact step sequence without re-deriving it each time.

## Procedure Registry

### PROC-001: New Lead Qualification

```
Trigger: New inbound lead (form, trial signup, or outbound response)

Steps:
  1. Check lead vs ICP criteria (entity_memory icp_dimensions)
  2. Score MEDDIC: M+E+D+D+I+C (6 dimensions, 0-1 each)
  3. Route based on score:
     - Score >= 5: Hot -> CSM assignment within 2h
     - Score 3-4: Warm -> Automated nurture + follow-up in 48h
     - Score < 3: Cold -> Nurture sequence only
  4. Create customer entity (entity_memory_customer schema)
  5. Log acquisition channel + UTM
  6. Schedule discovery call (hot leads) OR enter nurture sequence

Time budget: <15 minutes for qualification decision
Responsible: N06 (automated) + CSM for hot leads
```

### PROC-002: Demo Request Handling

```
Trigger: Customer requests demo

Steps:
  1. Pre-demo prep (30 min before):
     a. Pull customer entity
     b. Research company (size, industry, recent news)
     c. Prepare ROI calculator with industry defaults for their size
     d. Select use case most relevant to their role/industry
     e. Prepare 2 objection handlers for most common in their industry
  
  2. Demo execution (45 min):
     a. SITUATION questions (5 min)
     b. PROBLEM + IMPLICATION questions (10 min)
     c. ROI calculation with their numbers (5 min)
     d. Live build (15 min) -- THEIR use case, not generic
     e. Tier recommendation (5 min)
     f. Next steps + close (5 min)
  
  3. Post-demo (within 1h):
     a. Update customer entity (pain points, decision process, timeline)
     b. Send follow-up: ROI one-pager + relevant case study
     c. Create next-step calendar invite
     d. Log in CRM

Time budget: 45 min demo + 30 min prep + 30 min follow-up
Responsible: CSM (PRO/ENTERPRISE) or automated (STARTER)
```

### PROC-003: Upgrade Offer Execution

```
Trigger: expansion_play trigger event (from expansion_play_n06)

Steps:
  1. Identify trigger type (quota / feature gate / seat / lifecycle)
  2. Select appropriate action_prompt_upsell template
  3. Populate template with customer-specific data
  4. Channel selection:
     - Quota/feature trigger: in-app first, email if not acted in 48h
     - Seat trigger: in-app modal (immediate)
     - Enterprise trigger: CSM touchpoint (no self-serve)
  5. Track: message_sent, cta_clicked, upgrade_completed, dismissed
  6. If dismissed: suppress same message for 7 days
  7. If 3 dismissals: escalate to different play or CSM

Time budget: automated (< 30 seconds to generate and send)
```

### PROC-004: Renewal Management

```
Trigger: renewal_date - 30 days

Steps:
  Day -30: Customer receives "Your renewal is coming up" email
           Content: usage recap + value summary + tier recommendation
           CTA: Annual upgrade offer ($savings prominent)
  
  Day -14: If not renewed AND annual offer not taken:
           CSM review of customer entity
           If health_score < 60: CSM proactive outreach
           If health_score >= 60: No action (self-service OK)
  
  Day -7:  If churn_risk >= "medium":
           CSM save call scheduled
           Prepare: best offer available (annual + bonus)
  
  Day -3:  Final renewal reminder
           CTA: Renew now OR contact support
  
  Day 0:   Renewal invoice sent by Stripe
  
  Day +3:  If unpaid: payment failure flow (PROC-005)
  
Post-renewal: Update entity, send "thanks for renewing" + usage tips

Responsible: Automated (day -30, -3, 0) + CSM (day -14, -7 if flagged)
```

### PROC-005: Payment Failure Recovery

```
Trigger: invoice.payment_failed Stripe webhook

Steps:
  Hour 0: Update entity (invoices_failed++, churn_risk escalated)
          Send "Payment issue" email (PLAY 2, churn_prevention_playbook)
          Generate Stripe Customer Portal link
  
  Hour 24: Reminder email if not resolved
  
  Hour 48: Account warning + SMS if available
           Log to CSM queue
  
  Hour 72: Downgrade to FREE (preserve all data)
           Email: "Account paused -- data safe for 30 days"
           Freeze: no new builds, read-only access
  
  Day 30:  Final data warning
  Day 60:  Archive data (recoverable 6 months by support)

Escalation: CSM reviews any account > $500 ARR that fails payment at Hour 48

Responsible: Automated + CSM escalation
```

### PROC-006: Refund Request Handling

```
Trigger: Customer requests refund

Steps:
  1. Retrieve customer entity + invoice history
  2. Classify:
     - Technical failure (CEX bug caused loss): auto-approve + apologize
     - Buyer's remorse within 7 days: approve once (policy)
     - Buyer's remorse > 7 days: evaluate case-by-case
     - Disputed charge: escalate to legal
  
  3. If approving:
     a. Issue refund via Stripe
     b. Update entity (refunds history)
     c. Flag for bugloop_revenue if technical failure
     d. Check if refund = churn signal -> trigger save attempt
  
  4. Response to customer: within 4 business hours
  5. Log for cohort analysis (refund_rate by plan + channel)

Responsible: Support + N06 automation for auto-approvals
```

## Procedure Update Protocol

When a procedure fails or a better sequence is discovered:
1. Document in `learning_record_n06.md`
2. Update this procedure (version + date)
3. Log update to `regression_check_n06.md` if old procedure caused revenue loss


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_renewal_workflow]] | upstream | 0.27 |
| [[bld_output_template_churn_prevention_playbook]] | upstream | 0.26 |
| [[p10_lr_renewal_workflow_builder]] | related | 0.26 |
| [[bld_config_renewal_workflow]] | upstream | 0.25 |
| [[bld_examples_renewal_workflow]] | upstream | 0.24 |
| [[bld_output_template_renewal_workflow]] | upstream | 0.23 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.22 |
| [[bld_instruction_churn_prevention_playbook]] | upstream | 0.22 |
| [[n06_funnel_cex_product]] | downstream | 0.20 |
| [[p12_sp_renewal_workflow_builder]] | downstream | 0.19 |
