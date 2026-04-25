---
id: enterprise_sla_cex_platform
kind: enterprise_sla
8f: F8_collaborate
pillar: P11
nucleus: N06
domain: commercial
title: "Enterprise SLA — CEX Platform"
version: "1.0.0"
quality: 8.5
tags: [sla, enterprise, uptime, support, platform]
author: N06_contrib_stress_test
created: "2026-04-19"
effective_date: "2026-05-01"
review_cycle: annual
related:
  - kc_enterprise_sla
  - n06_intent_resolution_depth_spec
  - bld_examples_enterprise_sla
  - enterprise-sla-builder
  - n06_report_intent_resolution_moat
  - bld_knowledge_card_enterprise_sla
  - n06_roi_content_factory
  - bld_tools_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - n06_api_access_pricing
density_score: 1.0
updated: "2026-04-22"
---

## Scope

This SLA governs CEX platform delivery to enterprise customers. Applies to:
- CEX SaaS runtime (nuclei N01-N07 API access)
- Builder pipeline (8F artifact production)
- SDK (`cex_sdk` Python package, versioned releases)
- Knowledge system (300 kinds, 3647 ISOs, quality gate)

## Uptime Commitments

| Tier | Uptime Target | Monthly Downtime Allowance | Credit Trigger |
|------|--------------|--------------------------|----------------|
| Free | 95.0% | 36.5 hours | None |
| Pro | 99.0% | 7.3 hours | <99.0% in calendar month |
| Enterprise | 99.5% | 3.6 hours | <99.5% in calendar month |
| Enterprise+ | 99.9% | 43.8 minutes | <99.9% in calendar month |

Uptime = (total minutes - downtime minutes) / total minutes x 100

**Exclusions from downtime calculation:**
- Scheduled maintenance (48h advance notice)
- Force majeure events
- Customer-caused outages (misconfigured API keys, quota exhaustion)
- Third-party LLM provider outages (Anthropic, OpenAI, Google)

## Latency SLA (API Endpoints)

| Endpoint Type | P50 Target | P95 Target | P99 Target |
|--------------|-----------|-----------|-----------|
| Intent resolution | <100ms | <300ms | <500ms |
| Builder artifact (cached) | <200ms | <500ms | <1s |
| Builder artifact (fresh 8F) | <30s | <60s | <120s |
| Nucleus dispatch (async) | <5s queue | <30s start | <120s start |
| Compile + validate | <10s | <30s | <60s |

## Quality Gate SLA

| Metric | Target | Measurement |
|--------|--------|-------------|
| Artifact quality (8F output) | >= 8.5/10 avg | Monthly sample of 100 artifacts |
| Builder coverage | >= 95% of 300 kinds | Monthly cex_doctor.py run |
| ISO completeness | 13/13 ISOs per builder | Automated check |
| Compile success rate | >= 99% | Post-write compile hook |

## Support Commitments

| Tier | Response SLA | Resolution SLA | Channel |
|------|-------------|----------------|---------|
| Free | 72 hours | Best effort | GitHub Issues |
| Pro | 24 hours (business) | 72 hours | Email + GitHub |
| Enterprise | 4 hours (24/7) | 24 hours | Slack + Email |
| Enterprise+ | 1 hour (24/7) | 8 hours | Dedicated Slack + PagerDuty |

**Support ticket classification:**

| Severity | Definition | Response |
|----------|-----------|----------|
| P1 — Critical | Platform down, data loss, security breach | 1 hour (Enterprise+) |
| P2 — High | Core feature broken, >50% quality degradation | 4 hours (Enterprise) |
| P3 — Medium | Feature degraded, workaround exists | 24 hours |
| P4 — Low | Enhancement, documentation, cosmetic | 72 hours |

## Service Credits

| Actual Uptime | Credit (% monthly fee) |
|---------------|----------------------|
| 99.0% - 99.5% | 10% |
| 95.0% - 99.0% | 25% |
| 90.0% - 95.0% | 50% |
| < 90.0% | 100% |

Credit claim window: 30 days after incident. Max credit: 100% of monthly fee.
Credits are account credits only — no cash refunds.

## Escalation Path

```
L1: Support engineer (24h response)
  |-- if unresolved in response SLA
L2: Senior engineer + product owner (4h response)
  |-- if P1/P2 unresolved in 4h
L3: CTO-level escalation + incident war room
  |-- post-incident: 5-day RCA report
```

## Data Retention and Portability

| Data Type | Retention | Export Format |
|-----------|-----------|--------------|
| Artifact files (.md) | 90 days post-termination | ZIP archive |
| Compile outputs (.yaml) | 90 days post-termination | ZIP archive |
| Audit logs | 2 years | JSON/CSV |
| Quality scores | 1 year | CSV |

## Planned Maintenance Window

- Standard: Sundays 02:00-06:00 UTC (4-hour window)
- Emergency: minimum 6-hour notice via status page + email
- Major releases: 48-hour advance notice; 30-minute maintenance window target

## SLA Review Cycle

Annual review with customer. Metrics tracked via:
- `N06_commercial/P05_output/commercial_readiness_*.md` (monthly snapshots)
- `_tools/cex_quality_monitor.py` (quality regression detection)
- Status page: to be provisioned at launch

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_enterprise_sla]] | upstream | 0.33 |
| [[n06_intent_resolution_depth_spec]] | related | 0.32 |
| [[bld_examples_enterprise_sla]] | upstream | 0.32 |
| [[enterprise-sla-builder]] | related | 0.31 |
| [[n06_report_intent_resolution_moat]] | related | 0.31 |
| [[bld_knowledge_card_enterprise_sla]] | upstream | 0.30 |
| [[n06_roi_content_factory]] | related | 0.29 |
| [[bld_tools_enterprise_sla]] | upstream | 0.29 |
| [[p03_sp_enterprise_sla_builder]] | upstream | 0.28 |
| [[n06_api_access_pricing]] | related | 0.26 |
