---
kind: examples
id: bld_examples_lifecycle_rule
pillar: P00
quality: 9.1
title: "Examples Lifecycle Rule"
version: "1.0.0"
author: n03_builder
tags: [lifecycle_rule, builder, examples]
tldr: "Golden and anti-examples for lifecycle rule construction, demonstrating ideal structure and common pitfalls."
domain: "lifecycle rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
```yaml
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of lifecycle_rule artifacts
pattern: few-shot learning — LLM reads these before producing
```
# Examples: lifecycle-rule-builder
## Golden Example
INPUT: "Define lifecycle rule for knowledge_cards — when do they go stale and get archived?"
OUTPUT:
```yaml
id: p11_lc_kc_freshness
kind: lifecycle_rule
pillar: P11
title: "Lifecycle: KC Freshness"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
scope: "knowledge_card"
freshness_days: 90
review_cycle: "quarterly"
ownership: "knowledge-engine"
domain: "knowledge"
quality: null
tags: [lifecycle-rule, knowledge-card, freshness, quarterly]
tldr: "KCs become stale after 90 days; quarterly review by knowledge-engine promotes, refreshes, or archives"
notification: "signal"
automation: "semi"
density_score: 0.93
linked_artifacts:
  primary: "p11_qg_kc_publish"
  related: [p01_kc_schema, p10_knowledge_index]
## Definition
Knowledge cards lose accuracy as domains evolve. LLM pricing changes monthly,
framework APIs break quarterly, and research findings get superseded. A KC
cited confidently today may mislead an agent 6 months from now. This rule
ensures KCs are reviewed before staleness degrades downstream decisions.
## States
| State | Entry Criteria | Duration | Next |
|-------|---------------|----------|------|
| draft | Created, not yet reviewed | <= 7 days | active, rejected |
| active | Passes quality_gate >= 8.0 | <= 90 days | stale, promoted |
| promoted | Score >= 9.5 (golden) | <= 180 days | stale |
| stale | freshness_days exceeded without update | <= 30 days | refreshed, archived |
| refreshed | Stale KC updated and re-validated | <= 90 days | stale, promoted |
| archived | No longer relevant or superseded | permanent | sunset |
| sunset | Removed from active indexes | terminal | — |
## Transitions
| From | To | Trigger | Action | Automated |
|------|----|---------|--------|-----------|
| draft | active | quality_gate pass >= 8.0 | Index in brain, notify owner | yes |
| draft | rejected | quality_gate fail < 7.0 | Return to author with report | yes |
| active | stale | 90 days since last updated | Emit staleness signal, notify knowledge-engine | yes |
| active | promoted | quality_gate pass >= 9.5 | Tag as golden, priority index | yes |
| promoted | stale | 180 days since last updated | Emit staleness signal | yes |
| stale | refreshed | Owner updates and re-validates | Re-index, reset freshness timer | semi |
| stale | archived | 30 days stale with no action | Remove from active index | yes |
| archived | sunset | 365 days archived, no references | Delete from pool | manual |
## Review Protocol
| Aspect | Value |
|--------|-------|
| Reviewer | knowledge-engine (knowledge agent_group) |
| Cycle | quarterly (every 90 days) |
| Checklist | facts still accurate, sources still valid, density >= 0.80 |
| Outcome | refresh (update + re-validate) or archive (remove from index) |
## Automation
| Transition | Method | Trigger |
|------------|--------|---------|
| active -> stale | cron (daily scan of updated field) | freshness_days exceeded |
| stale -> archived | cron (daily scan of stale entries) | 30 days in stale state |
| draft -> active | hook (post-validation) | quality_gate pass signal |
| archived -> sunset | manual review | annual cleanup cycle |
## References
- Content lifecycle management: https://www.contentful.com/help/content-lifecycle/
- CEX quality thresholds: GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0
```
WHY THIS IS GOLDEN:
- quality: null (H06 pass)
- id matches p11_lc_ pattern (H02 pass)
- kind: lifecycle_rule (H04 pass)
- pillar: P11 (H05 pass)
- freshness_days: 90, positive integer (H07 pass)
- review_cycle: "quarterly", valid enum (H08 pass)
- 7 states in States table >= 3 (S03 pass)
- 8 transitions in Transitions table >= 3 (S04 pass)
- Automation section with 4 concrete entries (S05 pass)
- All triggers are measurable: days, scores, signals (S07 pass)
## Anti-Example
