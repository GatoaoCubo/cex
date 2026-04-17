---
id: kc_kind_gap_synthesis
kind: knowledge_card
pillar: P01
title: "CEX Kind Gap Synthesis: Taxonomy + Nucleus Coverage Audit"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n07_orchestrator
domain: taxonomy-audit
quality: null
tags: [taxonomy, gap-analysis, kinds, ddd, nucleus-coverage]
tldr: "257 CEX kinds: 10 new DDD/ops kinds needed; N03 has 62/257 kinds active (13x peer gap); P0 fix = VD Wave 2A (22 blocked commerce artifacts)."
when_to_use: "Planning taxonomy expansions, prioritizing kind additions, auditing nucleus coverage, or reviewing DDD alignment of CEX 257-kind registry."
keywords: [kind-gap, taxonomy-audit, ddd-alignment, nucleus-coverage, vertical-distillation]
long_tails:
  - "which new kinds should be added to CEX taxonomy"
  - "N03 engineering nucleus artifact coverage gap"
  - "DDD ubiquitous language missing kinds in CEX"
axioms:
  - "ALWAYS distinguish taxonomy gaps (new kind needed) from coverage gaps (kind exists, nucleus has no instance)."
  - "NEVER add a new kind without reuse_score >= 7 and a builder ISOs plan."
  - "IF workflow kind is being used to model a domain_event, saga, or bounded_context THEN a new kind is warranted."
linked_artifacts:
  primary: null
  related: [kc_kind_gap_analysis, kind_gap_audit_m1]
density_score: 0.92
data_source: "N01_intelligence/P01_knowledge/kc_kind_gap_analysis.md + N03_engineering/P01_knowledge/kind_gap_audit_m1.md"
---

# CEX Kind Gap Synthesis: Taxonomy + Nucleus Coverage Audit

## Quick Reference

```yaml
topic: CEX 257-kind taxonomy gap (DDD + engineering lenses)
owner: n07_orchestrator
criticality: high
current_kinds: 257
recommended_additions: 10
blocked_artifacts: 22
source_audits: [kc_kind_gap_analysis (N01), kind_gap_audit_m1 (N03)]
```

## Two Distinct Gap Types

| Gap Type | Symptom | Fix |
|----------|---------|-----|
| **Taxonomy gap** | Pattern has no kind in kinds_meta.json | Add kind + builder + ISOs |
| **Coverage gap** | Kind exists; N03 has zero instances | Execute VERTICAL_DISTILLATION |

Conflating these causes wrong fixes: adding kinds when instances just need producing, or building without schema.

## Audit Sources

| Source | Nucleus | Lens |
|--------|---------|------|
| kc_kind_gap_analysis.md | N01 | DDD Ubiquitous Language (257 kinds vs DDD/AI) |
| kind_gap_audit_m1.md | N03 | Engineering/structural (N03 vs peer nuclei) |

## N01 Findings: DDD Alignment

65% partial; 3% true covered; 22 DDD/AI concepts missing; 6 kinds overloaded.

### Top 10 Recommended New Kinds

| Kind | Pillar | Reuse | Gap filled |
|------|--------|-------|------------|
| `domain_event` | P12 | 9 | Domain fact (vs system-level signal) |
| `data_contract` | P06 | 9 | Producer/consumer schema agreement |
| `domain_vocabulary` | P01 | 9 | UL registry per bounded context |
| `alert_rule` | P09 | 9 | Observable threshold condition |
| `bounded_context` | P08 | 8 | DDD model boundary |
| `deployment_manifest` | P09 | 8 | What/where/how to deploy |
| `slo_definition` | P09 | 8 | Measurable service objective |
| `lineage_record` | P01 | 8 | KC provenance chain |
| `saga` | P12 | 7 | Long-running distributed transaction |
| `canary_config` | P09 | 7 | Gradual rollout config |

### Overloaded Kinds

| Kind | Severity | N |
|------|----------|---|
| `workflow` | CRITICAL | 5 — process/saga/choreography/pipeline/state_machine |
| `knowledge_card` | HIGH | 5 — fact/analysis/entity/reference/vocabulary |
| `interface` | HIGH | 5 — contract/port/adapter/API spec/data_contract |
| `guardrail` | HIGH | 4 — safety_rule/policy/constraint/ethical_bound |
| `constraint_spec` | MEDIUM | 3 — business_rule/invariant/precondition |
| `cost_budget` | MEDIUM | 3 — token_budget/infra_cost/ops_budget |

## N03 Findings: Engineering Coverage

N03: 62/257 active kinds, ~120 artifacts vs ~1,650 peer average (13x gap).

### Pillar Coverage Gaps (N03)

| Pillar | N03 Active | Coverage | Severity |
|--------|-----------|----------|----------|
| P05 Output | 2/25 | 8% | CRITICAL |
| P04 Tools | 7/50 | 14% | CRITICAL |
| P11 Feedback | 3/20 | 15% | HIGH |
| P09 Config | 5/30 | 17% | HIGH |
| P06 Schema | 6/20 | 30% | MEDIUM |
| P08 Architecture | 9/22 | 41% | LOW |

### VERTICAL_DISTILLATION Wave 2A Blocked (22 artifacts)

| Category | Count | Example IDs |
|----------|-------|-------------|
| API clients | 3 | api_client_shopify/stripe/sendgrid |
| Webhooks | 4 | webhook_shopify/stripe, fulfillment_webhook, refund_handler |
| OAuth + guides | 5 | oauth_app_config_shopify, integration_guide_shopify/stripe/sendgrid (3) |
| Commerce | 4 | order_processor, cart_sync, inventory_webhook, payment_handler |
| Config/auth | 6 | retry_policy_ecommerce, token_refresh_flow, rate_limit_config_shopify (+3) |

## Priority Order: Next Actions

| Pri | Action | Effort | Impact |
|-----|--------|--------|--------|
| P0 | VERTICAL_DISTILLATION Wave 2A (N03) | 22 artifacts | Unblocks commerce vertical |
| P1 | Add `domain_vocabulary` + `domain_event` (+ ISOs) | 2 kinds | UL enforcement + Event Storming |
| P2 | Add `data_contract`, `alert_rule`, `slo_definition` | 3 kinds | Data governance + observability |
| P3 | Add `bounded_context`, `deployment_manifest`, `saga` | 3 kinds | DDD + DevOps + dist. tx |
| P4 | Refactor `workflow` (CRITICAL — 5 concepts) | Split | Semantic drift relief |

## Decision Matrix

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Industry pattern, no CEX kind | Taxonomy gap | Add kind + builder |
| Kind exists, N03 has zero instances | Coverage gap | VD wave |
| One kind covers 5 concepts | Overload | GDP split |
| Nucleus 13x below peer average | Structural gap | Distillation waves |

## Resolution Flow

```
AUDIT -> CLASSIFY: [taxonomy] add kind+ISOs | [coverage] VD wave | [overload] GDP split
```

## Golden Rules

- ALWAYS execute VD Wave 2A before adding new kinds — commerce vertical blocked.
- ALWAYS add `domain_vocabulary` first — backs UL enforcement at F2b SPEAK.
- NEVER add a kind with reuse_score < 7 — dilutes taxonomy, adds builder debt.
- IF workflow models a saga or domain_event THEN refactor — semantic drift compounds.
- N03 deficit is execution (coverage), not taxonomy — 257 kinds suffice.

## References

- `N01_intelligence/P01_knowledge/kc_kind_gap_analysis.md`
- `N03_engineering/P01_knowledge/kind_gap_audit_m1.md`
- `.cex/kinds_meta.json` (257-kind registry)
- `.claude/rules/ubiquitous-language.md`
- `archetypes/builders/{kind}-builder/` (13 ISOs per kind)
