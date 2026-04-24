---
id: user_model_n06
kind: user_model
8f: F2_become
nucleus: n06
pillar: P10
title: "User Model N06: Ideal Customer Profile (ICP)"
mirrors: N00_genesis/P10_memory/tpl_user_model.md
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
peer_id: "{{icp_segment_id}}"
workspace: n06_commercial
storage:
  primary: sqlite
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: false
dialectic:
  pre_response_insight: true
  post_response_derive: true
  compaction_cadence_turns: 25
collections:
  - name: icp_profile
  - name: revenue_signals
  - name: churn_risk
  - name: upsell_fit
retention:
  messages_ttl_days: 730
  derived_facts_ttl_days: 365
version: 1.0.0
quality: 8.4
tags: [mirror, n06, commercial, user_model, icp, ltv, cac, hermes_assimilation]
tldr: "ICP user model for N06: tracks LTV, CAC, churn-risk, upsell-fit per customer segment"
created: "2026-04-18"
updated: "2026-04-18"
author: n06_commercial
related:
  - n06_monetization_audit_2026_04_08
  - bld_knowledge_card_churn_prevention_playbook
  - bld_knowledge_card_expansion_play
  - bld_knowledge_card_customer_segment
  - customer-segment-builder
  - bld_instruction_expansion_play
  - bld_collaboration_customer_segment
  - expansion-play-builder
  - p03_sp_churn_prevention_playbook_builder
  - p03_sp_expansion_play_builder
---

## Peer Profile (ICP Lens)

`Commercial customer profile optimized for revenue signal extraction and conversion scoring.`
`Workspace: N06_commercial — every data point maps to a revenue impact or churn risk.`

## Collections

### icp_profile
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `segment_name` | {{e.g., Mid-Market SaaS}} | 0.9 | 2026-04-18 |
| `company_size` | {{headcount range}} | 0.85 | 2026-04-18 |
| `annual_revenue_range` | {{e.g., $1M-$10M ARR}} | 0.8 | 2026-04-18 |
| `decision_maker_title` | {{e.g., VP Sales, CRO}} | 0.9 | 2026-04-18 |
| `buying_trigger` | {{e.g., team expansion, quota miss}} | 0.75 | 2026-04-18 |
| `sales_cycle_days` | {{e.g., 45}} | 0.8 | 2026-04-18 |

### revenue_signals
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `ltv_usd` | {{lifetime value in USD}} | 0.85 | 2026-04-18 |
| `cac_usd` | {{customer acquisition cost}} | 0.8 | 2026-04-18 |
| `ltv_cac_ratio` | {{target >= 3.0}} | 0.85 | 2026-04-18 |
| `avg_deal_size_usd` | {{e.g., $12,000}} | 0.9 | 2026-04-18 |
| `mrr_expansion_rate` | {{e.g., 15% annual}} | 0.75 | 2026-04-18 |
| `payback_period_months` | {{e.g., 14}} | 0.8 | 2026-04-18 |
| `revenue_impact` | {{projected 12-month revenue from segment}} | 0.85 | 2026-04-18 |
| `conversion_target` | {{e.g., 22% SQL-to-close}} | 0.8 | 2026-04-18 |
| `cost_model` | {{variable: $X/seat, fixed: $Y/mo}} | 0.9 | 2026-04-18 |

### churn_risk
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `churn_rate_annual` | {{e.g., 8%}} | 0.8 | 2026-04-18 |
| `churn_signal_1` | {{e.g., 30d login gap}} | 0.75 | 2026-04-18 |
| `churn_signal_2` | {{e.g., support tickets > 3}} | 0.75 | 2026-04-18 |
| `health_score_threshold` | {{e.g., < 60 triggers CSM}} | 0.85 | 2026-04-18 |
| `at_risk_revenue_usd` | {{current ARR at risk this quarter}} | 0.7 | 2026-04-18 |

### upsell_fit
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `upsell_trigger` | {{e.g., usage > 80% of tier limit}} | 0.85 | 2026-04-18 |
| `expansion_mrr_potential_usd` | {{e.g., $2,400/yr per account}} | 0.8 | 2026-04-18 |
| `cross_sell_products` | {{list of complementary SKUs}} | 0.75 | 2026-04-18 |
| `upgrade_propensity_score` | {{0-100}} | 0.7 | 2026-04-18 |

## Revenue Impact Summary
| Metric | Value | Calculation |
|--------|-------|-------------|
| Segment LTV | ${{ltv_usd}} | ARPA x avg retention months |
| Segment CAC | ${{cac_usd}} | Total S&M / new customers |
| LTV:CAC | {{ratio}} | Target >= 3.0 |
| Conversion target | {{pct}}% | SQL-to-closed-won |
| At-risk ARR | ${{at_risk}} | Churn-score < threshold |

## Dialectic Loop Status
| Phase | Status | Last Run |
|-------|--------|----------|
| pre_response_insight | enabled | 2026-04-18 |
| post_response_derive | enabled | 2026-04-18 |
| compaction | 25 turns | 2026-04-18 |

## API Surface
| Method | Signature | Purpose |
|--------|-----------|---------|
| peer.chat | `peer.chat(query: str) -> str` | NL revenue-signal query |
| session.context | `session.context(token_limit: int) -> str` | Bounded context retrieval |
| icp.score | `icp.score(lead: dict) -> float` | 0-100 ICP fit score |
| churn.risk | `churn.risk(account_id: str) -> dict` | Churn probability + signals |
| upsell.candidates | `upsell.candidates(min_score: int) -> list` | Ranked expansion targets |

## Update History
| Version | Change | Date |
|---------|--------|------|
| 1.0.0 | Initial ICP user model — N06 commercial overlay | 2026-04-18 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_monetization_audit_2026_04_08]] | upstream | 0.24 |
| [[bld_knowledge_card_churn_prevention_playbook]] | upstream | 0.23 |
| [[bld_knowledge_card_expansion_play]] | upstream | 0.22 |
| [[bld_knowledge_card_customer_segment]] | upstream | 0.21 |
| [[customer-segment-builder]] | upstream | 0.21 |
| [[bld_instruction_expansion_play]] | upstream | 0.19 |
| [[bld_collaboration_customer_segment]] | downstream | 0.19 |
| [[expansion-play-builder]] | upstream | 0.19 |
| [[p03_sp_churn_prevention_playbook_builder]] | upstream | 0.18 |
| [[p03_sp_expansion_play_builder]] | upstream | 0.18 |
