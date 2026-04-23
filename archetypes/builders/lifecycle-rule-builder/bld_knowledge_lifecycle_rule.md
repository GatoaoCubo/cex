---
kind: knowledge_card
id: bld_knowledge_card_lifecycle_rule
pillar: P11
llm_function: INJECT
purpose: Domain knowledge for lifecycle_rule production — atomic searchable facts
sources: lifecycle-rule-builder MANIFEST.md + SCHEMA.md v1.0.0
quality: 9.1
title: "Knowledge Card Lifecycle Rule"
version: "1.0.0"
author: n03_builder
tags: [lifecycle_rule, builder, examples]
tldr: "Golden and anti-examples for lifecycle rule construction, demonstrating ideal structure and common pitfalls."
domain: "lifecycle rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_lifecycle_rule
  - bld_memory_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - bld_collaboration_lifecycle_rule
  - bld_examples_lifecycle_rule
  - p11_qg_lifecycle_rule
  - bld_manifest_lifecycle_rule
  - bld_architecture_lifecycle_rule
  - bld_schema_lifecycle_rule
  - p01_kc_lifecycle_rule
---

# Domain Knowledge: lifecycle_rule
## Executive Summary
Lifecycle rules are declarative policies governing artifact state transitions over time — from creation through review, promotion, deprecation, and sunset. Each rule defines freshness thresholds, review cycles, ownership, and automation level for a specific artifact kind. They differ from hooks (which execute code on events), runtime rules (which manage system behavior), quality gates (which score at one point), and guardrails (which prevent damage) by managing artifact freshness as a first-class temporal concern.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (governance) |
| Kind | `lifecycle_rule` (exact literal) |
| ID pattern | `p11_lc_{slug}` |
| Required frontmatter | 17 fields |
| Recommended frontmatter | 4 (freshness_days, review_cycle, ownership, automation) |
| Quality gates | 9 HARD + 8 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| States | draft, active, stale, deprecated, archived, sunset |
## Patterns
| Pattern | Application |
|---------|-------------|
| Domain-specific freshness | LLM pricing = 30 days; architectural law = 365 days |
| Measurable transitions | Days since update, score threshold, or usage count |
| Mandatory ownership | Unowned artifacts always rot — assign agent_group or agent |
| Notification on stale | Stale artifact with no alert = hidden technical debt |
| Automation levels | full (cron-driven), semi (auto-detect + human approve), manual |
| State machine | Each state has entry criteria, exit criteria, and allowed transitions |
### Freshness Reference
| Domain | Typical freshness_days | Rationale |
|--------|----------------------|-----------|
| LLM pricing/models | 30 | Providers update frequently |
| API documentation | 90 | APIs change quarterly |
| Architectural patterns | 180 | Patterns evolve slowly |
| Operational laws | 365 | Laws are stable by design |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No freshness_days specified | Cannot automate staleness detection |
| Missing ownership field | No one reviews = guaranteed rot |
| State without entry criteria | Arbitrary transitions; no enforcement possible |
| freshness_days: 999 | Effectively disables lifecycle; artifact rots silently |
| Automation: full without notification | Silent archival surprises consumers |
| One-size-fits-all freshness | Different artifact kinds decay at different rates |
## Application
1. Identify the target artifact kind and its typical update cadence
2. Define states (minimum: active, stale, archived) with entry/exit criteria
3. Set `freshness_days` based on domain-specific decay rate
4. Set `review_cycle` with periodicity and reviewer identity
5. Assign `ownership` to a specific agent or team
6. Choose `automation` level (full/semi/manual)
7. Define notification triggers for stale transitions
8. Validate: 9 HARD + 8 SOFT gates, body <= 3072 bytes
## References
- lifecycle-rule-builder SCHEMA.md v1.0.0
- ITIL Service Lifecycle (strategy, design, transition, operation, improvement)
- DAMA-DMBOK Data Governance (data quality dimensions + retention policies)
- AWS S3 Lifecycle Rules (time-based automated transitions)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_lifecycle_rule]] | upstream | 0.48 |
| [[bld_memory_lifecycle_rule]] | upstream | 0.48 |
| [[p03_sp_lifecycle_rule_builder]] | upstream | 0.46 |
| [[bld_collaboration_lifecycle_rule]] | related | 0.42 |
| [[bld_examples_lifecycle_rule]] | related | 0.41 |
| [[p11_qg_lifecycle_rule]] | related | 0.39 |
| [[bld_manifest_lifecycle_rule]] | related | 0.39 |
| [[bld_architecture_lifecycle_rule]] | upstream | 0.35 |
| [[bld_schema_lifecycle_rule]] | upstream | 0.35 |
| [[p01_kc_lifecycle_rule]] | sibling | 0.27 |
