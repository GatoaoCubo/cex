---
id: schedule_n06
kind: schedule
nucleus: n06
pillar: P12
title: "Schedule N06: Sales Cadence (Follow-up / Renewal / QBR)"
mirrors: N00_genesis/P12_orchestration/templates/tpl_schedule.md
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
tags: [mirror, n06, commercial, schedule, cadence, renewal, qbr, follow_up, hermes_assimilation]
tldr: "N06 sales cadence schedules: outbound follow-up sequences, renewal windows, and QBR timing — all ROI-justified"
created: "2026-04-18"
updated: "2026-04-18"
author: n06_commercial
related:
  - p10_lr_renewal_workflow_builder
  - renewal-workflow-builder
  - bld_knowledge_card_renewal_workflow
  - p12_sp_renewal_workflow_builder
  - bld_output_template_renewal_workflow
  - bld_instruction_renewal_workflow
  - bld_examples_renewal_workflow
  - bld_collaboration_renewal_workflow
  - bld_config_renewal_workflow
  - bld_tools_renewal_workflow
---

## Cadence Registry

| Cadence | Type | Frequency | Revenue Impact | Cost Model |
|---------|------|-----------|---------------|------------|
| outbound_followup | lead nurture | Day 1/3/7/14/21/30 | +28% reply rate vs. no sequence | $0 marginal (rep time) |
| renewal_window | retention | 90d/60d/30d before expiry | -22% churn vs. no proactive renewal | rep time + discount budget |
| qbr | expansion | Quarterly | +19% expansion MRR per account | 1.5h rep time per account |

---

## Cadence 1: Outbound Follow-up Sequence

**Purpose**: Multi-touch lead nurture from first contact to meeting booked. No single-touch abandonment.

**Revenue Impact**: 6-touch sequences yield 28% higher reply rate and 2.3x more meetings vs. 1-touch (SalesLoft 2024).
**Conversion Target**: 15% reply rate, 8% meeting-booked rate per sequence launched.
**Cost Model**: Rep time only — no paid media; amortized over pipeline ARR.

### Schedule Definition
```yaml
id: "cadence_outbound_followup_n06"
name: "Outbound Follow-up Sequence"
type: event_triggered
trigger: new_lead_assigned OR sql_created
timezone: "America/Sao_Paulo"
enabled: true
```

### Touch Schedule
| Day | Channel | Message Type | Goal |
|-----|---------|--------------|------|
| 0 | Email | Value intro — pain hypothesis | Open rate > 45% |
| 1 | LinkedIn | Connection request + brief | Connect rate > 30% |
| 3 | Email | Case study — same segment | Reply rate > 8% |
| 7 | Phone | Direct call — decision maker | Connect rate > 20% |
| 14 | Email | ROI calculator attached | Reply rate > 6% |
| 21 | LinkedIn | Comment on their content | Warm signal |
| 30 | Email | Break-up / final value offer | Reply or disqualify |

### Task Configuration
```yaml
task:
  command: "python _tools/cex_cadence_runner.py --cadence outbound_followup"
  working_dir: "N06_commercial/"
  timeout_s: 120
  env:
    CEX_NUCLEUS: "n06"
  on_success: log_crm_activity
  on_failure: alert_rep
```

---

## Cadence 2: Renewal Window

**Purpose**: Proactive renewal outreach to prevent churn and lock multi-year commitments before expiry.

**Revenue Impact**: Proactive renewal at 90d reduces churn by 22%; multi-year commit offers at 60d yield 31% take rate.
**Conversion Target**: 85% renewal rate; 20% upgrade-at-renewal rate; 15% multi-year lock rate.
**Cost Model**: Discount budget capped at 15% for annual, 20% for 2-year; ROI positive above 12-month retention.

### Schedule Definition
```yaml
id: "cadence_renewal_window_n06"
name: "Renewal Window Sequence"
type: date_relative
reference: contract_expiry_date
timezone: "America/Sao_Paulo"
enabled: true
```

### Renewal Touch Schedule
| Days to Expiry | Action | Owner | Goal |
|----------------|--------|-------|------|
| -90 | QBR + renewal preview | CSM | Health score check; flag at-risk |
| -60 | Renewal proposal sent | AE | Lock pricing; present multi-year option |
| -45 | Follow-up: legal/finance loop | AE | Paper process started |
| -30 | Executive sponsor call | AE + CSM | Remove blockers; confirm intent |
| -14 | Final terms sent | AE | Signature in this window |
| -7 | Urgent: deadline communication | AE | Close or escalate |
| -1 | Last call / escalation | AE + Manager | Auto-renewal or deal save |
| +1 | Post-close: kickoff or offboard | CSM | Ensure transition is clean |

### Task Configuration
```yaml
task:
  command: "python _tools/cex_renewal_monitor.py --days-ahead 90"
  cron: "0 8 * * 1"    # Every Monday 8AM
  working_dir: "N06_commercial/"
  timeout_s: 300
  env:
    CEX_NUCLEUS: "n06"
  on_success: update_renewal_dashboard
  on_failure: alert_revenue_ops
```

---

## Cadence 3: Quarterly Business Review (QBR)

**Purpose**: Structured account review to demonstrate ROI, uncover expansion opportunities, and reinforce retention.

**Revenue Impact**: Accounts with regular QBRs show +19% expansion MRR and 14% lower churn vs. reactive support-only accounts.
**Conversion Target**: 90% QBR acceptance rate; 30% of QBRs generate expansion opportunity.
**Cost Model**: 1.5h AE/CSM time per account; prioritize top 20% of ARR base (covers 80% of expansion opportunity).

### Schedule Definition
```yaml
id: "cadence_qbr_n06"
name: "Quarterly Business Review"
cron: "0 9 1 1,4,7,10 *"   # 1st of Jan/Apr/Jul/Oct at 9AM
timezone: "America/Sao_Paulo"
enabled: true
```

### QBR Agenda Template
| Section | Duration | Owner | Revenue Signal |
|---------|----------|-------|---------------|
| ROI recap (last quarter) | 10m | CSM | Justify renewal; anchor expansion |
| Usage analytics | 10m | CSM | Usage > 80% = upgrade trigger |
| Business goals (next quarter) | 15m | Customer | Uncover new pain = new deal |
| Product roadmap preview | 10m | AE | Land expansion seeds |
| Expansion proposal (if fit) | 10m | AE | Present if usage/goals indicate fit |
| Action items + next QBR date | 5m | CSM | Lock next touchpoint |

### Monitoring
- **QBR acceptance rate**: target >= 90%
- **Expansion pipeline from QBRs**: target >= $50K/quarter
- **NPS delta post-QBR**: target >= +8 points
- **Alert on**: 2+ QBRs missed for top-20% ARR accounts

## Retry Policy (all cadences)
| Attempt | Delay | Action |
|---------|-------|--------|
| 1st failure | 60s | Retry automatically |
| 2nd failure | 300s | Retry + alert revenue ops |
| 3rd failure | — | Skip + create manual CRM task |

## Quality Gate
- [x] All cron expressions validated
- [x] Timezones explicitly set (America/Sao_Paulo)
- [x] Revenue impact quantified per cadence
- [x] Conversion targets defined and measurable
- [x] Cost model documented

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_renewal_workflow_builder]] | upstream | 0.36 |
| [[renewal-workflow-builder]] | related | 0.35 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.33 |
| [[p12_sp_renewal_workflow_builder]] | related | 0.33 |
| [[bld_output_template_renewal_workflow]] | upstream | 0.32 |
| [[bld_instruction_renewal_workflow]] | upstream | 0.30 |
| [[bld_examples_renewal_workflow]] | upstream | 0.30 |
| [[bld_collaboration_renewal_workflow]] | related | 0.29 |
| [[bld_config_renewal_workflow]] | upstream | 0.28 |
| [[bld_tools_renewal_workflow]] | upstream | 0.26 |
