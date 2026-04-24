---
id: handoff_n06
kind: handoff
8f: F8_collaborate
nucleus: n06
pillar: P12
title: "Handoff N06: Commercial Deal Context"
mirrors: N00_genesis/P12_orchestration/templates/tpl_handoff.md
overrides:
  tone: ROI-focused, conversion-driven
  voice: consultative, numbers-first
  sin_lens: AVAREZA ESTRATEGICA
  required_fields:
    - revenue_impact
    - conversion_target
    - cost_model
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with revenue impact projections
version: 1.0.0
quality: 8.7
tags: [mirror, n06, commercial, handoff, deal_context, stakeholders, pricing, objections, hermes_assimilation]
tldr: "N06 commercial handoff template: structured deal-context transfer covering stakeholders, pricing history, objections, and next action"
created: "2026-04-18"
updated: "2026-04-18"
author: n06_commercial
related:
  - discovery-questions-builder
  - p03_sp_discovery_questions_builder
  - bld_instruction_discovery_questions
  - bld_knowledge_card_discovery_questions
  - bld_output_template_sales_playbook
  - bld_output_template_renewal_workflow
  - pricing_optimization_memory
  - bld_instruction_expansion_play
  - bld_output_template_churn_prevention_playbook
  - p01_qg_discovery_questions
---

# COMMERCIAL HANDOFF — N06 DEAL CONTEXT TRANSFER
**Autonomy Level**: Full | **Quality Minimum**: 9.0+
**RULE: Every handoff must contain revenue_impact, conversion_target, and cost_model — non-negotiable.**

---

## DEAL CONTEXT

`{{2-3 sentences: what is being sold, to whom, and why this deal matters now}}`

**Example**: "Expanding Pro tier to Acme Corp (Mid-Market SaaS, $800K ARR) following 90-day pilot. Champion is VP Sales, economic buyer is CFO. Deal size $24K ACV; Q2 close critical for quota attainment."

---

## REVENUE SIGNALS

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| Deal ACV | ${{annual_contract_value}} | CRM | 0.95 |
| Expansion potential | ${{upsell_potential_yr1}} | Usage analytics | 0.8 |
| LTV estimate | ${{ltv_usd}} | Cohort model | 0.75 |
| CAC for this deal | ${{cac_usd}} | Finance | 0.9 |
| Payback period | {{months}} months | LTV/CAC calc | 0.8 |
| revenue_impact | ${{projected_12mo_revenue}} | Forecast | 0.85 |
| conversion_target | {{pct}}% SQL-to-close | Pipeline model | 0.8 |
| cost_model | {{pricing_structure_and_tiers}} | Pricing sheet | 0.95 |

---

## STAKEHOLDER MAP

| Name | Title | Role | Sentiment | Last Contact | Owner |
|------|-------|------|-----------|--------------|-------|
| {{name_1}} | {{title}} | Economic Buyer | {{positive/neutral/negative}} | {{date}} | AE |
| {{name_2}} | {{title}} | Champion | {{positive}} | {{date}} | CSM |
| {{name_3}} | {{title}} | Legal/Procurement | {{neutral}} | {{date}} | AE |
| {{name_4}} | {{title}} | End User / Influencer | {{positive}} | {{date}} | CSM |

**Multi-thread status**: {{single/multi-threaded}} — `{{risk note if single-threaded}}`

---

## PRICING HISTORY

| Date | Offer | Discount | Outcome | Notes |
|------|-------|----------|---------|-------|
| {{date}} | ${{amount}}/mo | {{0%}} | Sent | Initial proposal |
| {{date}} | ${{amount}}/mo | {{5%}} | Countered | Buyer asked for annual option |
| {{date}} | ${{amount}}/yr | {{10%}} | Pending | CFO approval needed |

**Current ask**: ${{final_ask}} | **Walk-away floor**: ${{floor}} (GM threshold: {{gm_pct}}%)
**Approval required**: {{yes/no}} — {{who}} up to ${{limit}}

---

## OBJECTION LOG

| Objection | Category | Status | Response Used | Outcome |
|-----------|----------|--------|---------------|---------|
| "Too expensive vs. [Competitor]" | Price | Resolved | TCO comparison shared | Moved to ROI discussion |
| "Need IT sign-off on security" | Process | Open | Security questionnaire sent | Awaiting IT review |
| "Not sure on timing" | Urgency | Pending | Cost-of-delay calc presented | Follow-up in 5 days |

---

## MUST HAVES (success criteria)
```yaml
truths:
  - "Deal ACV documented in CRM with signed quote"
  - "Economic buyer has received and acknowledged pricing"
  - "Champion confirmed internally sponsoring this deal"
artifacts:
  - path: "N06_commercial/P12_orchestration/deal_{{account_slug}}.md"
    check: "exists AND contains:revenue_impact"
  - path: ".cex/runtime/handoffs/crm_sync_{{account_slug}}.yaml"
    check: "exists AND size > 0"
key_links:
  - "CRM opportunity: {{crm_url}}"
  - "Pricing sheet: N06_commercial/P11_feedback/pricing_{{sku}}.md"
  - "Champion enablement deck: N06_commercial/P05_output/deck_{{account_slug}}.md"
```

---

## TASKS (for receiving agent/nucleus)

### Step 1: Load deal context
Read CRM opportunity + this handoff. Confirm revenue_impact and cost_model are current.

### Step 2: Stakeholder update
Verify all stakeholders are correctly mapped. Flag any unmapped buyers identified in last 7 days.

### Step 3: Resolve open objections
Check objection log. For each open item: select response from skill_n06.md objection library and schedule follow-up.

### Step 4: Advance to next stage
If all blockers resolved and champion confirmed: send mutual action plan (skill_n06.md closing sequence, Step 1).

### Step 5: Update forecast
Log updated conversion probability in CRM. Recalculate revenue_impact with current deal stage x ACV.

---

## SELF-REVIEW CHECKLIST
- [ ] revenue_impact in USD documented
- [ ] conversion_target as % defined
- [ ] cost_model structure confirmed
- [ ] Stakeholder map covers economic buyer
- [ ] All open objections have assigned owner + due date
- [ ] Next action has date + owner
- [ ] Quality score >= 9.0

---

## SCOPE FENCE
- ONLY: `N06_commercial/` and CRM sync files
- DO NOT TOUCH: Pricing floor without AE + Manager sign-off

---

## COMMIT
```bash
git add N06_commercial/P12_orchestration/
git commit -m "[N06] commercial handoff: {{account_slug}} — {{stage}} → {{next_stage}}"
```

---

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n06', 'complete', 9.0, task='handoff_n06_{{account_slug}}')"
```

---

## STOPPED AT
```yaml
stopped_at:
  step: 0
  status: NOT_STARTED
  reason: "Template — fill when deal requires transfer"
  resume_from: "Step 1: Load deal context"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[discovery-questions-builder]] | upstream | 0.21 |
| [[p03_sp_discovery_questions_builder]] | upstream | 0.19 |
| [[bld_instruction_discovery_questions]] | upstream | 0.18 |
| [[bld_knowledge_card_discovery_questions]] | upstream | 0.18 |
| [[bld_output_template_sales_playbook]] | upstream | 0.18 |
| [[bld_output_template_renewal_workflow]] | upstream | 0.18 |
| [[pricing_optimization_memory]] | upstream | 0.17 |
| [[bld_instruction_expansion_play]] | upstream | 0.17 |
| [[bld_output_template_churn_prevention_playbook]] | upstream | 0.17 |
| [[p01_qg_discovery_questions]] | upstream | 0.17 |
