---
id: p01_kc_gap_detection
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Gap Detection"
version: 2.0.0
created: 2026-03-31
updated: 2026-04-07
author: n01_research
domain: patterns
quality: 9.1
tags: [pattern, skill, llm, gap-detection, audit, completeness, coverage]
tldr: "Systematically find missing knowledge, tools, or artifacts. Compare current state vs desired state across schemas, builders, queries, coverage, and user feedback."
when_to_use: "Before a mission (pre-flight check), after a build wave (coverage audit), or when quality scores plateau."
keywords: [gap-detection, audit, completeness, missing, coverage, delta-analysis]
density_score: 0.95
related:
  - leverage_map_v2_n05_verify
  - p10_out_gap_report
  - bld_architecture_kind
  - self_audit_newpc_2026_04_12
  - n05_self_review_2026-04-02
  - p08_dm_n03_leverage_v2_verification
  - bld_collaboration_kind
  - output_sdk_validation_self_audit
  - self_audit_newpc
  - self_review_2026-04-02
---

# Gap Detection

## Quick Reference

| Aspect | Detail |
|--------|--------|
| Core idea | Compare current inventory against required inventory; find deltas |
| Trigger | Pre-mission, post-wave, quality plateau, user report |
| Benefit | Prevents building on incomplete foundations |
| Risk if skipped | Missing artifacts discovered late → rework, cascading failures |

## Detection Methods

| Method | What It Detects | Tool | Cost |
|--------|----------------|------|------|
| Schema diff | Missing required fields in artifacts | `cex_compile.py` | Free |
| Builder audit | Missing ISOs per builder (13 required) | `cex_doctor.py` | Free |
| Query miss | KC topics with no matching artifact | `cex_query.py` | Free |
| Coverage analysis | Untested tools, uncovered code paths | `pytest --cov` | Free |
| Cross-reference scan | Broken links between artifacts | `cex_retriever.py` | Free |
| User feedback | Missing capabilities reported in conversation | Manual | Free |
| Pillar completeness | Pillars with < N artifacts vs expected | Script | Free |

## Gap Severity Classification

| Severity | Definition | Action | Timeline |
|----------|-----------|--------|----------|
| Critical | Blocks current mission or pipeline | Fix immediately | This session |
| High | Degrades quality of dependent artifacts | Fix in next wave | Next dispatch |
| Medium | Limits but doesn't block functionality | Backlog with priority | Next mission |
| Low | Nice-to-have, cosmetic completeness | Backlog | Eventually |

## Systematic Audit Protocol

| Step | Action | Output |
|------|--------|--------|
| 1 | Run `cex_doctor.py` | Builder health report (118+ checks) |
| 2 | Run `cex_compile.py --all` | Schema validation errors |
| 3 | Compare kinds_meta.json vs builders/ | Missing builder directories |
| 4 | Scan P01 library vs known domains | Missing knowledge cards |
| 5 | Check N01-N07 nucleus directories | Missing pillar subdirectories |
| 6 | Cross-reference linked artifacts | Broken `## Linked Artifacts` refs |
| 7 | Classify gaps by severity | Prioritized gap list |

## Gap Report Format

```yaml
gap_id: GAP_001
detected_by: cex_doctor.py
severity: high
location: archetypes/builders/webhook-builder/
missing: bld_quality_gate_webhook.md
impact: "Webhook artifacts cannot be quality-gated"
fix: "Create quality gate ISO using shared template"
```

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|-------------|--------------|
| Manual-only detection | Misses structural gaps that tools catch instantly |
| Ignoring low-severity gaps | They accumulate and become critical mass |
| Fixing gaps without logging | Same gaps re-emerge in future missions |
| Over-auditing during build | Slows momentum — audit between waves, not during |
| Coverage metrics without action | 85% coverage means nothing if the 15% is critical path |

## CEX Integration

| Concept | CEX artifact / tool |
|---------|-------------------|
| Builder health | `cex_doctor.py` (118 PASS target) |
| Schema validation | `cex_compile.py --all` |
| Artifact discovery | `cex_query.py` (TF-IDF search) |
| Gap tracking | `.cex/runtime/plans/` mission plans |
| Learning from gaps | `.cex/learning_records/` |

## Linked Artifacts

- `p01_kc_self_healing_skill` — auto-fix detected gaps when possible
- `p01_kc_iterative_refinement_skill` — multi-pass to close gaps systematically
- `p01_kc_qa_validation` — validation framework that detects quality gaps

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[leverage_map_v2_n05_verify]] | downstream | 0.30 |
| [[p10_out_gap_report]] | downstream | 0.29 |
| [[bld_architecture_kind]] | downstream | 0.23 |
| [[self_audit_newpc_2026_04_12]] | related | 0.22 |
| [[n05_self_review_2026-04-02]] | downstream | 0.22 |
| [[p08_dm_n03_leverage_v2_verification]] | downstream | 0.22 |
| [[bld_collaboration_kind]] | downstream | 0.22 |
| [[output_sdk_validation_self_audit]] | downstream | 0.21 |
| [[self_audit_newpc]] | related | 0.21 |
| [[self_review_2026-04-02]] | downstream | 0.21 |
