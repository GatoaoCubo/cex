---
kind: quality_gate
id: p11_qg_learning_record
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of learning_record artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Learning Record"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, learning-record, experience-capture, P10, retrospective]
tldr: "Quality gate for learning_record artifacts: enforces outcome classification, impact score, and reproducible context."
domain: learning_record
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.85
related:
  - p11_qg_model_card
  - p03_ins_learning_record
  - p11_qg_mental_model
  - p11_qg_law
  - p11_qg_model_provider
  - p11_qg_embedder_provider
  - p11_qg_quality_gate
  - p11_qg_creation_artifacts
  - p03_sp_learning_record_builder
  - p11_qg_lifecycle_rule
---

## Quality Gate

# Gate: Learning Record
## Definition
A `learning_record` captures a discrete experience — a pattern that worked or an anti-pattern that failed — with enough context to reproduce the outcome. Gates prevent vague retrospectives from entering the pool and ensure every record carries a scored, classified, reproducible finding.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p10_lr_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"learning_record"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `topic`, `outcome`, `impact`, `agent_group`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `outcome` is one of: `SUCCESS`, `PARTIAL`, `FAILURE` | Enum violation — unclassifiable record |
| H08 | Pattern or Anti-Pattern classification present in body | Record lacks directional finding |
| H09 | `impact` field is a float between 0.0 and 10.0 | Impact unscored — not comparable to other records |
| H10 | Reproducibility assessment present in body | Experience cannot be transferred |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, non-empty, states the finding not just the topic |
| S02 | Context sufficient for reproduction | 1.0 | Names environment, timing, and triggering conditions |
| S03 | Pattern steps concrete | 1.0 | Pattern section has >= 2 ordered steps, not abstract principles |
| S04 | Anti-pattern failure specific | 1.0 | Anti-Pattern section names exact failure mode, not category |
| S05 | Impact score justification clear | 1.0 | Score justified with measurable delta (time, errors, quality) |
| S06 | Actionable takeaway present | 1.0 | Closes with a single directive another agent can act on immediately |
| S07 | Agent_group/domain tagged | 0.5 | `agent_group` field non-empty and matches known agent_group or `GENERAL` |
| S08 | `tags` includes record kind | 0.5 | At least one tag matches `outcome` value in lowercase |
| S09 | Density >= 0.80 | 1.0 | No filler phrases: "it is important to note", "generally speaking", "in summary" |
| S10 | Timestamps accurate | 0.5 | `created` and `updated` in ISO 8601 format, `updated` >= `created` |
| S11 | Related records linked | 0.5 | `related` field lists >= 1 record id or explicitly `[]` |
| S12 | Record is concise (<= 3 KB body) | 0.5 | Trim narrative; findings compress to essentials |
| S13 | Pattern categorization consistent | 0.5 | Uses taxonomy: performance, reliability, quality, process, or integration |
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

## Examples

# Examples: learning-record-builder
## Golden Example
INPUT: "Document the learning from continuous batching achieving 1.6x speedup with 3 agent_groups"
OUTPUT:
```yaml
id: p10_lr_continuous_batching_speedup
kind: learning_record
pillar: P10
version: "1.0.0"
created: "2026-03-05"
updated: "2026-03-05"
author: "builder"
domain: "orchestration"
quality: 8.8
tags: [learning, continuous-batching, speedup, orchestration, multi-agent_group]
tldr: "Continuous batching with 3 sats achieved 1.6x speedup; task complexity drives speed, not model tier"
topic: "Continuous batching multi-agent_group performance"
outcome: SUCCESS
score: 9.0
context: "ISOFIX mission, 7 batches across researcher+builder+knowledge-engine, 2026-03-05"
agent_group: "orchestrator"
reproducibility: HIGH
impact: "1.6x throughput increase, zero git lock contention at 3 agent_groups"
timestamp: "2026-03-05T14:30:00Z"
dependencies: []
keywords: [batching, parallel, throughput, spawn, grid]
linked_artifacts:
  primary: null
  related: [p12_spawn_grid, p08_pat_continuous_batching]
```
## Summary
Continuous batching with 3 agent_groups (researcher+builder+knowledge-engine) achieved 1.6x speedup over sequential execution. Speed was driven by task complexity, not model tier — opus finished faster than sonnet on simpler tasks. Zero git lock contention observed.
## Pattern
- Use spawn_grid.ps1 with -mode continuous for >6 tasks
- Name handoffs as {MISSION}_batch_{N}_{DOMAIN}.md for queue management
- Limit to 3 concurrent agent_groups (RAM ceiling at 4+)
- Let queue auto-refill slots as agent_groups complete
## Anti-Pattern
- Running >3 agent_groups causes BSOD risk (RAM exhaustion)
- Assuming opus is slower than sonnet — speed depends on task, not model
- Manual slot management instead of auto-refill wastes idle time
## Context
- Environment: Windows 10 Pro, 32GB RAM, 3 Claude Code terminals
- Agent_group: orchestrator orchestrating researcher+builder+knowledge-engine
- Timing: 2026-03-05, ISOFIX mission, 7 sequential batches
- Constraints: max 3 terminals (BSOD prevention), 5s spawn delay
## Impact
- 1.6x throughput vs sequential single-agent_group execution
- Zero git lock contention across 3 concurrent committers
- Queue auto-refill eliminated idle time between waves
## Reproducibility
- Conditions: 3 agent_groups, >6 tasks, independent work units
- Confidence: HIGH (tested on ISOFIX 7/7 and CBTEST mixed)
- Caveats: tasks must be independent; shared file edits cause conflicts
## References
- records/skills/continuous_batching/SKILL.md
- spawn_grid.ps1 -mode continuous
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p10_lr_ pattern (H02 pass)
- kind: learning_record (H04 pass)
- 22 fields present including all 15 required (H06 pass)
- outcome: SUCCESS (H09 pass, enum valid)
- score: 9.0 (S02 pass, float in range)
- Pattern has 4 concrete steps (S03 pass)
- Anti-Pattern has 3 specific failures (S04 pass)
- All 7 body sections present (S08 pass)
- density high, no filler (S09 pass)
## Anti-Example
INPUT: "Document what we learned about batching"
BAD OUTPUT:
```yaml
id: batching_learning
kind: learning
quality: 8.5
topic: batching
outcome: good
score: "high"
tags: batching
We learned a lot about batching. It was really useful and helped us be more productive.
Overall, the experience was positive and we recommend using it in the future.
In summary, batching works well when done correctly.
```
FAILURES:
1. id: no `p10_lr_` prefix -> H02 FAIL
2. kind: "learning" not "learning_record" -> H04 FAIL
3. quality: 8.5 (self-assigned) -> H05 FAIL
4. outcome: "good" not in enum [SUCCESS, PARTIAL, FAILURE] -> H09 FAIL
5. score: "high" is string not float -> S02 FAIL
6. tags: string not list -> H07 FAIL
7. Missing required fields: pillar, version, created, updated, author, domain, context, tldr -> H06 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
