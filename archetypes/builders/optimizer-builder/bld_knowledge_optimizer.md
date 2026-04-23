---
kind: knowledge_card
id: bld_knowledge_card_optimizer
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for optimizer production — atomic searchable facts
sources: optimizer-builder MANIFEST.md + SCHEMA.md, Google SRE, control theory, DORA metrics
quality: 9.1
title: "Knowledge Card Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_optimizer
  - bld_memory_optimizer
  - p03_sp_optimizer_builder
  - p11_qg_optimizer
  - optimizer-builder
  - bld_collaboration_optimizer
  - bld_config_optimizer
  - bld_examples_optimizer
  - bld_output_template_optimizer
  - bld_schema_optimizer
---

# Domain Knowledge: optimizer
## Executive Summary
Optimizers are continuous improvement artifacts encoding the feedback loop: measure metric, compare to threshold, fire action. Each optimizer targets ONE metric with a direction (minimize/maximize), three threshold tiers (trigger/target/critical), and a typed action (tune/prune/scale/replace/restructure). They differ from bugloops (one-time fix cycles), quality gates (single pass/fail checks), guardrails (safety boundaries), and lifecycle rules (freshness management) by implementing persistent metric-driven automation.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance) |
| Kind | `optimizer` (exact literal) |
| ID pattern | `p11_opt_{slug}` |
| Required frontmatter | 15 fields |
| Quality gates | HARD + SOFT (per QUALITY_GATES.md) |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Metric directions | minimize (lower=better), maximize (higher=better) |
| Action types | tune, prune, scale, replace, restructure |
| Automation | true (auto-fire) or false (human approval) |
## Patterns
| Pattern | Application |
|---------|-------------|
| Direction-aware thresholds | minimize: trigger > target > critical; maximize: trigger < target < critical |
| Tripartite thresholds | trigger (act now), target (goal), critical (alarm) |
| Action type selection | tune (adjust params), prune (remove low-value), scale (add capacity), replace (swap component) |
| Automation decision | automated=true only when risk=low, rollback instant, action reversible |
| Baseline documentation | Measure under NORMAL load; record date, load level, environment, config version |
| Cooldown period | Prevent action oscillation; minimum time between consecutive firings |
### Threshold Design Reference
| Strategy | trigger | target | critical |
|----------|---------|--------|----------|
| Conservative | 70% of danger | 50% of danger | 90% of danger |
| Aggressive | 50% of danger | 30% of danger | 80% of danger |
| SLO-aligned | Budget burn 10% | SLO target | SLO hard limit |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No metric direction specified | Threshold ordering becomes ambiguous |
| trigger == critical | No warning band; goes from normal to alarm instantly |
| automated=true for irreversible action | No rollback path; risk of cascading failure |
| Missing baseline | Cannot measure improvement without starting point |
| Multiple metrics in one optimizer | One optimizer = one metric; compose for multi-metric |
| No cooldown specified | Action oscillates on/off at threshold boundary |
## Application
1. Select ONE metric and its direction (minimize or maximize)
2. Measure baseline under normal conditions; document environment
3. Set three thresholds: trigger, target, critical (ordered by direction)
4. Choose action type: tune, prune, scale, replace, or restructure
5. Decide automation: true (auto-fire) vs false (human approval)
6. Set cooldown period to prevent oscillation
7. Configure monitoring: dashboard, alerts, reporting
8. Validate: body <= 4096 bytes, density >= 0.80, all HARD + SOFT gates
## References
- optimizer-builder SCHEMA.md v1.0.0
- Google SRE Book (SLO error budgets)
- Control theory (PID controllers, feedback loops)
- DORA Four Keys (deployment frequency, lead time, MTTR, CFR)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | downstream | 0.54 |
| [[bld_memory_optimizer]] | downstream | 0.47 |
| [[p03_sp_optimizer_builder]] | downstream | 0.44 |
| [[p11_qg_optimizer]] | downstream | 0.43 |
| [[optimizer-builder]] | downstream | 0.38 |
| [[bld_collaboration_optimizer]] | downstream | 0.34 |
| [[bld_config_optimizer]] | downstream | 0.33 |
| [[bld_examples_optimizer]] | downstream | 0.32 |
| [[bld_output_template_optimizer]] | downstream | 0.31 |
| [[bld_schema_optimizer]] | downstream | 0.29 |
