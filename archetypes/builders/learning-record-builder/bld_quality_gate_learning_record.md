---
id: p11_qg_learning_record
kind: quality_gate
pillar: P11
title: "Gate: Learning Record"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: learning_record
quality: 9.0
tags: [quality-gate, learning-record, experience-capture, P10, retrospective]
tldr: "Quality gate for learning_record artifacts: enforces outcome classification, impact score, and reproducible context."
density_score: 0.85
llm_function: GOVERN
---
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
