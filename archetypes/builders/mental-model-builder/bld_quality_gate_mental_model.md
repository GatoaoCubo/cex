---
id: p11_qg_mental_model
kind: quality_gate
pillar: P11
title: "Gate: Mental Model"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: mental_model
quality: 9.0
tags: [quality-gate, mental-model, routing, P02, cognitive-map]
tldr: "Quality gate for mental_model artifacts: enforces routing rules, decision tree, domain map, and design-time-only scope."
density_score: 0.85
llm_function: GOVERN
---
# Gate: Mental Model

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Definition
A `mental_model` is a design-time cognitive map that tells an agent how to route, prioritize, and decide. It carries no runtime state and executes no logic. Gates here enforce that routing rules have confidence thresholds, decisions have if/then/else structure, and the artifact never encodes live session data — which belongs in runtime state artifacts.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_mm_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"mental_model"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `agent`, `domain`, `routing_rules`, `decision_tree`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `Routing Rules` section present in body | Model has no routing — central purpose missing |
| H08 | `Decision Tree` or `Priorities` section present in body | No decision structure — model cannot guide choices |
| H09 | `Domain Map` section present in body | Domain boundaries undefined — routing leaks |
| H10 | `routing_rules` list has >= 3 entries, each with `keywords` and `action` | Routing table too sparse to be useful |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names the agent and its primary routing concern |
| S02 | Routing rules have confidence thresholds | 1.0 | Each rule specifies a match confidence or keyword specificity level |
| S03 | Decisions have if/then/else structure | 1.0 | Decision tree entries follow: condition → then action → else action |
| S04 | Priorities ordered with rationale | 1.0 | `priorities` list is ranked and each rank has a one-line justification |
| S05 | Heuristics testsble | 0.5 | Each heuristic can be verified with a specific input example |
| S06 | Domain boundaries explicit | 1.0 | Domain Map states what the agent covers AND what it routes away |
| S07 | Personality traits defined | 0.5 | `personality` object with `tone`, `verbosity`, `risk_tolerance` |
| S08 | `tags` includes `"mental-model"` | 0.5 | Minimum tag for routing |
| S09 | Conflict resolution rules present | 1.0 | Documents what happens when two routing rules match simultaneously |
| S10 | No runtime state encoded | 1.0 | No session counters, active task lists, or live flags in body |
| S11 | Fallback action defined | 0.5 | `fallback` specifies action and escalation target when no rule matches |
| S12 | Density >= 0.80 | 0.5 | No filler: "this model helps", "generally speaking", "in most cases" |
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
| condition | New agent bootstrapping — routing rules are provisional and under observation from live sessions |
