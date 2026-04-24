---
id: p01_kc_enterprise_sla
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Enterprise SLA — Service Level Agreement Kind"
version: 1.1.0
created: "2026-04-22"
updated: "2026-04-22"
author: knowledge-card-builder
domain: reliability_engineering
quality: 8.7
tags: [enterprise_sla, sla, reliability, uptime, P09, contracts, kind-kc]
tldr: "Contractual uptime/latency/support commitments to external parties with penalty clauses; SLA >= SLO always."
when_to_use: "Building, reviewing, or reasoning about enterprise_sla artifacts; generating customer-facing SLA documents or API contracts."
keywords: [sla, uptime, service-credits, penalty, slo]
long_tails:
  - "How to write an enterprise SLA with service credits and penalty clauses"
  - "SLA vs SLO difference: when to use each and how they relate"
axioms:
  - ALWAYS set SLA targets looser than internal SLOs (SLA >= SLO; never invert)
  - NEVER promise 100% uptime — use 99.99% as the ceiling
  - ALWAYS define the measurement window (monthly vs quarterly vs annual)
  - IF no penalty/credit clause THEN it is an SLO, not an SLA
linked_artifacts:
  primary: null
  related:
    - kc_slo_definition
    - p01_kc_quality_gate
    - p01_kc_incident_report
density_score: 0.91
data_source: "Google SRE Book (2016); ITIL 4; ISO/IEC 20000-1:2018"
---

# Enterprise SLA

## Quick Reference
```yaml
kind: enterprise_sla
pillar: P09
llm_function: GOVERN
max_bytes: 5120
naming: p09_sla_{{service_name}}.md + .yaml
core: false
```

## What It Is
An enterprise SLA (Service Level Agreement) is a **contractual** commitment between a service provider and an external party defining measurable targets, remedies, and exclusions. It differs from an SLO (internal engineering target) by being legally enforceable, carrying monetary penalties or service credits, and being scoped to customer-facing guarantees.

It is NOT:
- `slo_definition` (internal engineering target — no contract, no penalty)
- `quality_gate` (build-time scoring gate — governs CI/CD, not runtime reliability)
- `benchmark` (point-in-time measurement — not an ongoing commitment)

## Key Concepts
- **Uptime %** — measured as good_minutes / total_minutes in the window; excludes scheduled maintenance
- **Error budget** — (100% - SLA%) * window; the allowed downtime before credits trigger
- **Service credit** — percentage of monthly fee refunded per SLA breach; typically 10–50%
- **Measurement window** — monthly (most common), quarterly, or annual; window affects error budget math
- **Exclusions** — force majeure, customer-caused incidents, scheduled maintenance, beta features
- **Response SLA** — separate from uptime; defines P1/P2/P3 ticket response times
- **Reporting** — SLA compliance dashboard; monthly or quarterly reports to customer

## SLA Tier Table
| Tier | Uptime | Downtime/month | Latency p99 | Support | Credits |
|------|--------|---------------|-------------|---------|---------|
| Standard | 99.9% | 43.2 min | < 500 ms | 8x5, 4h response | 10% per 0.1% below |
| Business | 99.95% | 21.6 min | < 250 ms | 16x5, 2h response | 25% per 0.05% below |
| Enterprise | 99.99% | 4.3 min | < 100 ms | 24x7, 1h response | 50% per breach |
| Mission-Critical | 99.999% | 26 sec | < 50 ms | 24x7, 15 min response | 100% month credit |

## Structure (Required Fields)
```yaml
id: p09_sla_{service_name_slug}
kind: enterprise_sla
pillar: P09
service_name: "..."
uptime_target_percent: 99.9      # monthly window, excludes scheduled maint
latency_p99_ms: 250
support_tier: standard | business | enterprise | mission_critical
penalty_clause:
  breach_threshold_percent: 0.1  # downtime % above SLA triggers credit
  credit_percent: 10             # of monthly invoice per breach increment
measurement_window: monthly | quarterly | annual
exclusions: [scheduled_maintenance, force_majeure, customer_caused]
owner: "..."
quality: null
```

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| SLA target == SLO target | No buffer; any ops incident immediately breaches contract | SLA >= SLO + 0.05% buffer minimum |
| No exclusions clause | Scheduled maint counts as downtime; legally dangerous | Always list exclusions explicitly |
| Credit cap missing | Unlimited credits; financially unviable in cascade failures | Cap at 1 month invoice value |
| 100% uptime promised | Unachievable; immediate breach | Use 99.99% as ceiling |
| No measurement method | Customer and provider disagree on numbers | Define SLI query and data source |
| Response SLA undefined | Support expectations unset; customer escalations | Include P1/P2/P3 response times |

## Integration Graph
```
[slo_definition] <-- internal target (SLA >= SLO always)
      |
[enterprise_sla] --> [incident_report] (breach evidence)
      |               --> [service_credit] calculation
      |               --> [compliance_report] (quarterly)
      v
[quality_gate] -- gates SLA document completeness before publishing
```

## Decision Tree
- IF target_percent = 100 -> REJECT: unachievable; maximum is 99.999%
- IF no penalty_clause -> RECLASSIFY as slo_definition (not a contract)
- IF SLA_target > SLO_target -> BLOCK: SLA must be <= SLO (looser or equal)
- IF no exclusions listed -> WARN: add scheduled_maintenance + force_majeure
- IF measurement_window missing -> DEFAULT monthly (most common for billing)
- IF credit_cap missing -> WARN: unbounded liability; add max 1 month invoice

## Quality Criteria
- GOOD: uptime_target, penalty_clause, measurement_window, exclusions all present
- GREAT: SLI query explicit; credit calculation formula defined; breach notification SLA; report cadence
- FAIL: 100% target; no penalty clause; SLA tighter than SLO; no exclusions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_slo_definition]] | sibling | 0.72 |
| [[p01_kc_quality_gate]] | sibling | 0.45 |
| [[p01_kc_incident_report]] | downstream | 0.41 |
| [[bld_examples_enterprise_sla]] | downstream | 0.47 |
| [[enterprise-sla-builder]] | downstream | 0.44 |
| [[p10_mem_enterprise_sla_builder]] | downstream | 0.40 |
| [[p03_sp_enterprise_sla_builder]] | downstream | 0.38 |
| [[bld_collaboration_enterprise_sla]] | downstream | 0.22 |
