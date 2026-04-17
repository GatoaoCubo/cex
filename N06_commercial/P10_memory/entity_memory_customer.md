---
id: entity_memory_customer
kind: entity_memory
pillar: P10
nucleus: n06
title: "Entity Memory -- Customer Entity Schema and ICP Attributes"
version: 1.0.0
quality: 8.9
tags: [entity-memory, customer, icp, health-score, churn-risk, commercial, memory]
density_score: 1.0
---

# Entity Memory: Customer Entity Schema

## Purpose

Defines the canonical customer entity that N06 maintains per account. This is the commercial brain's memory of each customer -- not just contact data, but the full commercial intelligence picture: health, risk, potential, relationship history, and signals.

## Customer Entity Schema

```yaml
customer_entity:
  # Identity
  id: cus_stripe_id_or_internal
  name: string
  email: string
  company: string
  domain: string                    # email domain for org matching
  country: string                   # ISO 2-letter
  
  # Commercial Position
  plan_tier: free | starter | pro | enterprise | custom
  billing_cycle: monthly | annual
  mrr_cents: integer               # current monthly recurring revenue
  arr_cents: integer               # annual equivalent
  plan_start_date: date
  renewal_date: date
  trial_end_date: date | null
  
  # ICP Scoring
  icp_score: 0-100                 # ideal customer profile match
  icp_dimensions:
    company_size: 1-10 | 11-50 | 51-200 | 201-1000 | 1000+
    industry: string               # edtech | fintech | agency | saas | ecommerce | other
    role: founder | marketing | sales | operations | engineering | other
    use_case: brand | content | commercial | knowledge | all
    budget_signal: low | medium | high | enterprise
  
  # Health Score (0-100)
  health_score: integer
  health_components:
    builds_per_week: integer       # weight: 30%
    login_frequency_per_week: integer  # weight: 20%
    feature_breadth: integer       # nuclei used, out of available  # weight: 20%
    support_ticket_count: integer  # weight: 10% (negative)
    nps_score: integer | null      # weight: 20%
  health_trend: improving | stable | declining
  
  # Churn Risk
  churn_risk: low | medium | high | critical
  churn_risk_signals:
    - signal_type: string
      detected_at: datetime
      severity: low | medium | high
  days_since_last_build: integer
  cancel_intent_detected: boolean
  
  # Revenue Potential
  expansion_potential: low | medium | high
  expansion_plays_eligible:
    - play_name: string
      trigger_met: boolean
      recommended_tier: string
  estimated_lifetime_value_cents: integer
  
  # Acquisition
  acquisition_channel: organic | paid_search | paid_social | referral | outbound | event | other
  referral_code_used: string | null
  utm_source: string | null
  utm_campaign: string | null
  
  # Relationship
  csm_assigned: string | null
  last_csm_touchpoint: datetime | null
  qbr_scheduled: boolean
  case_study_candidate: boolean
  champion_name: string | null
  economic_buyer_name: string | null
  
  # Interaction History
  support_tickets: list[ticket_id]
  last_support_ticket_date: datetime | null
  nps_responses: list[{score: int, date: date, verbatim: string}]
  upgrade_attempts: list[{date: date, from_tier: str, to_tier: str, outcome: str}]
  
  # Commercial History
  invoices_paid: integer
  invoices_failed: integer
  refunds: list[{amount_cents: int, date: date, reason: str}]
  lifetime_revenue_cents: integer
```

## Health Score Calculation

```python
def calculate_health_score(customer: dict) -> int:
    score = 0
    
    # Builds per week (30 points)
    builds = customer["builds_per_week"]
    if builds >= 10:   score += 30
    elif builds >= 5:  score += 22
    elif builds >= 2:  score += 12
    elif builds >= 1:  score += 5
    else:              score += 0   # dormant
    
    # Login frequency (20 points)
    logins = customer["login_frequency_per_week"]
    if logins >= 5:    score += 20
    elif logins >= 3:  score += 15
    elif logins >= 1:  score += 8
    else:              score += 0   # inactive
    
    # Feature breadth (20 points)
    max_nuclei = {"free": 1, "starter": 4, "pro": 6, "enterprise": 7}
    available = max_nuclei.get(customer["plan_tier"], 1)
    used = customer["feature_breadth"]
    breadth_pct = used / available
    score += int(breadth_pct * 20)
    
    # Support tickets (10 points, negative)
    tickets = customer["support_ticket_count"]
    if tickets == 0:   score += 10
    elif tickets <= 2: score += 5
    elif tickets <= 5: score += 0
    else:              score -= 5   # chronic issues
    
    # NPS score (20 points)
    nps = customer.get("nps_score")
    if nps is None:    score += 10   # neutral (no data)
    elif nps >= 9:     score += 20   # promoter
    elif nps >= 7:     score += 12   # passive
    else:              score += 0    # detractor
    
    return min(100, max(0, score))
```

## Churn Risk Classification

```python
def classify_churn_risk(customer: dict) -> str:
    risk_points = 0
    
    if customer["days_since_last_build"] > 14:     risk_points += 3
    if customer["health_score"] < 40:               risk_points += 3
    if customer["cancel_intent_detected"]:          risk_points += 5
    if customer["invoices_failed"] > 0:             risk_points += 4
    if customer["health_trend"] == "declining":     risk_points += 2
    if customer["nps_score"] and customer["nps_score"] < 7: risk_points += 2
    
    if risk_points >= 8:   return "critical"
    elif risk_points >= 5: return "high"
    elif risk_points >= 2: return "medium"
    else:                  return "low"
```

## Memory Update Triggers

```yaml
update_on:
  - stripe_event: any      # billing status always current
  - build_completed        # health score recalculated
  - login                  # frequency tracking
  - support_ticket_opened  # ticket count + health impact
  - nps_survey_response    # NPS + health update
  - cancel_intent_detected # churn risk escalated
  - upgrade_completed      # tier and MRR updated
```

## Related Artifacts

- `churn_prevention_playbook_n06.md` -- acts on churn_risk signals
- `expansion_play_n06.md` -- acts on expansion_plays_eligible
- `referral_program_n06.md` -- uses referral_code_used for attribution
- `eval_metric_commercial.md` -- aggregated health score distribution tracked
