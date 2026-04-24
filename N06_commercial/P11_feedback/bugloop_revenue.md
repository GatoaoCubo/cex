---
id: bugloop_revenue
kind: bugloop
8f: F7_govern
pillar: P11
nucleus: n06
title: "Revenue Bugloop -- Automated Revenue Anomaly Detection and Remediation"
version: 1.0.0
quality: 9.0
tags: [bugloop, revenue, anomaly, remediation, feedback, commercial]
density_score: 1.0
updated: "2026-04-17"
related:
  - p06_security_validation_schema
  - extraction_gate_severity
  - p11_qg_validator
  - bld_knowledge_card_guardrail
  - p11_qg_ai_rmf_profile
  - bld_memory_validator
  - p03_ins_validator
  - p10_lr_guardrail_builder
  - bld_output_template_validator
  - bld_output_template_safety_policy
---

# Revenue Bugloop: Automated Anomaly Detection and Remediation

## Purpose

Catches revenue-impacting defects in real time: billing errors, checkout failures, webhook misses, and pricing calculation bugs. Every hour of undetected revenue bug = compounding loss. This loop runs continuously and self-remediates where safe.

## Detection Layer

### Revenue Anomaly Signals

```python
ANOMALY_RULES = {
    # Billing errors
    "double_charge": {
        "condition": "customer charged twice within 10 minutes for same product",
        "severity": "CRITICAL",
        "auto_remediate": True,
        "action": "issue_refund_second_charge + alert_ops"
    },
    "wrong_price": {
        "condition": "charge_amount != expected_price_from_enum_def",
        "severity": "HIGH",
        "auto_remediate": True,
        "action": "hold_payment + create_corrected_invoice"
    },
    "trial_expired_still_free": {
        "condition": "subscription.trial_end < now AND status == trialing",
        "severity": "MEDIUM",
        "auto_remediate": True,
        "action": "force_subscription_status_update"
    },
    
    # Checkout failures
    "checkout_session_abandoned": {
        "condition": "checkout.session.expired without checkout.session.completed",
        "severity": "LOW",
        "auto_remediate": False,
        "action": "send_cart_abandonment_email"
    },
    "webhook_missed": {
        "condition": "stripe_event not processed within 30 seconds",
        "severity": "HIGH",
        "auto_remediate": True,
        "action": "replay_event + alert_eng"
    },
    
    # Referral bugs
    "referral_credit_not_applied": {
        "condition": "referee converted AND referral_code valid AND credit not issued within 1 hour",
        "severity": "MEDIUM",
        "auto_remediate": True,
        "action": "backfill_referral_credit + notify_referrer"
    },
    
    # Churn system bugs
    "cancel_sequence_not_triggered": {
        "condition": "subscription.cancel_at_period_end=true AND no cancel_play started within 1 hour",
        "severity": "MEDIUM",
        "auto_remediate": True,
        "action": "trigger_churn_prevention_playbook"
    },
    
    # MRR calculation bugs
    "mrr_spike_30pct": {
        "condition": "calculated_mrr differs from previous period by >30%",
        "severity": "HIGH",
        "auto_remediate": False,
        "action": "alert_ops + freeze_mrr_report + manual_audit"
    }
}
```

## Remediation Confidence Levels

| Level | Definition | Action |
|-------|-----------|--------|
| AUTO | Low risk, reversible, clear fix | Execute without human review |
| SUPERVISED | Higher risk, needs audit trail | Execute + notify ops within 15 min |
| MANUAL | Irreversible or unclear | Block + alert ops immediately |

```yaml
remediation_confidence_map:
  double_charge: SUPERVISED      # financial impact, needs audit trail
  wrong_price: SUPERVISED        # financial impact
  trial_expired: AUTO            # no financial risk, idempotent
  webhook_missed: AUTO           # idempotent replay
  referral_credit: SUPERVISED    # billing impact
  cancel_not_triggered: AUTO     # starts a workflow, reversible
  mrr_spike: MANUAL              # data integrity concern
```

## Monitoring Schedule

```
Real-time: webhook processing health (< 30 sec lag)
Every 5 min: active checkout sessions scan
Every 15 min: trial expiry check
Every hour: referral credit reconciliation
Every 6 hours: MRR calculation vs Stripe source-of-truth
Daily: full billing reconciliation audit
Weekly: churn prevention sequence audit
```

## Remediation Audit Log Schema

```json
{
  "bug_id": "BUG_2026_04_17_001",
  "anomaly_type": "referral_credit_not_applied",
  "detected_at": "2026-04-17T10:15:00Z",
  "severity": "MEDIUM",
  "confidence_level": "SUPERVISED",
  "affected_customers": ["cus_abc123"],
  "revenue_impact_cents": 4900,
  "auto_remediated": true,
  "remediation_action": "backfill_referral_credit",
  "remediated_at": "2026-04-17T10:16:30Z",
  "human_reviewed": false,
  "ops_notified": true
}
```

## Escalation Matrix

```
CRITICAL: page oncall immediately, freeze affected revenue flows
HIGH: alert ops via Slack + email within 5 minutes
MEDIUM: Slack notification, ops reviews within 1 hour
LOW: daily digest, reviewed by EOD
```

## Integration with Self-Improvement Loop

Bugs that occur >3 times trigger a hypothesis in `self_improvement_loop_n06.md`:
- Root cause analysis
- Schema update proposal
- Test case addition to prevent recurrence


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_security_validation_schema]] | upstream | 0.29 |
| [[extraction_gate_severity]] | related | 0.23 |
| [[p11_qg_validator]] | upstream | 0.23 |
| [[bld_knowledge_card_guardrail]] | upstream | 0.22 |
| [[p11_qg_ai_rmf_profile]] | related | 0.22 |
| [[bld_memory_validator]] | upstream | 0.20 |
| [[p03_ins_validator]] | upstream | 0.19 |
| [[p10_lr_guardrail_builder]] | upstream | 0.18 |
| [[bld_output_template_validator]] | upstream | 0.18 |
| [[bld_output_template_safety_policy]] | upstream | 0.18 |
