---
kind: quality_gate
id: p11_qg_lifecycle_rule
pillar: P11
quality: 9.0
title: "Gate: Lifecycle Rule"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, lifecycle-rule, governance, P11, state-machine]
tldr: "Quality gate for lifecycle_rule artifacts: enforces state list, measurable transitions, and periodic review cycle."
domain: lifecycle_rule
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
llm_function: GOVERN
related:
  - p03_ins_lifecycle_rule
  - bld_memory_lifecycle_rule
  - p11_qg_quality_gate
  - bld_knowledge_card_lifecycle_rule
  - p03_sp_lifecycle_rule_builder
  - p11_qg_learning_record
  - bld_architecture_lifecycle_rule
  - p11_qg_mental_model
  - bld_collaboration_lifecycle_rule
  - bld_manifest_lifecycle_rule
---

## Quality Gate

# Gate: Lifecycle Rule
## Definition
A `lifecycle_rule` governs how an artifact kind moves through states from creation to sunset. It defines valid states, the measurable criteria that permit transitions, and the review cadence that keeps the rule current. Gates here ensure no rule is published with vague triggers, missing ownership, or an unverifiable review cycle.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p11_lc_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"lifecycle_rule"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `scope`, `ownership`, `freshness_days`, `review_cycle`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `States` section present with >= 3 named states | Lifecycle incomplete — cannot govern transitions |
| H08 | `Transitions` section present with entry criteria per transition | Transitions without criteria are unenforceable |
| H09 | `Review Cycle` section present with explicit periodicity | No cadence means rule decays silently |
| H10 | `review_cycle` value is one of: `weekly`, `monthly`, `quarterly`, `yearly` | Free-text cycle cannot be scheduled |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the governed artifact kind |
| S02 | States exhaustive for domain | 1.0 | No reachable real state missing from States table |
| S03 | Transitions have measurable criteria | 1.0 | Each transition criterion is checkable without human judgment |
| S04 | Review cycle realistic | 1.0 | Cycle matches actual volatility of governed domain |
| S05 | Ownership assigned per state | 1.0 | Each state has a named owner role or agent_group |
| S06 | Freshness threshold justified | 0.5 | `freshness_days` rationale present (not arbitrary) |
| S07 | Sunset conditions explicit | 1.0 | Defines what triggers end-of-life and who approves it |
| S08 | `tags` includes artifact `kind` name | 0.5 | Enables filtering by governed kind |
| S09 | Edge cases documented | 1.0 | Handles: orphaned artifacts, failed transitions, emergency overrides |
| S10 | Compatible with quality gate tiers | 0.5 | States map to: DRAFT, REVIEW, PUBLISH, GOLDEN, SUNSET |
| S11 | Density >= 0.80 | 1.0 | No filler: "when apownte", "as needed", "feels outdated" |
| S12 | Automation section present | 0.5 | Names at least one automated check or script for transition validation |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
| condition | New artifact kind with no prior lifecycle precedent; states are draft and under active definition |
| approver | P11 governance owner (human) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
