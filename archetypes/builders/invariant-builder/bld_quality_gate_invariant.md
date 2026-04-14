---
id: p11_qg_law
kind: quality_gate
pillar: P11
title: "Gate: Law"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: law
quality: 9.0
tags: [quality-gate, law, governance, P08, enforcement]
tldr: "Quality gate for invariant artifacts: enforces imperative statement, rationale, and testsble enforcement mechanism."
density_score: 0.85
llm_function: GOVERN
---
# Gate: Law
## Definition
A `law` artifact encodes an inviolable operational rule. It must carry a mandatory statement, the reasoning behind it, a concrete enforcement mechanism, and documented exceptions. Gates here prevent advisory rules from masquerading as laws and ensure every law is traceable, enforceable, and scoped.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p08_law_[0-9]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"invariant"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `number`, `statement`, `rationale`, `enforcement`, `scope`, `exceptions`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `statement` contains at least one of: `MUST`, `SHALL`, `NEVER`, `ALWAYS` | Rule is advisory, not mandatory |
| H08 | `number` is a positive integer | Law unidentifiable — routing breaks |
| H09 | `Statement` section present in body | Core content missing |
| H10 | `Rationale` section present in body | Missing justification — law cannot be audited |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, non-empty, not a restatement of `statement` |
| S02 | Rationale explains WHY | 1.0 | Does not merely restate the statement; explains consequence of violation |
| S03 | Enforcement mechanism named | 1.0 | Names a specific detection method: automated check, review step, or runtime guard |
| S04 | Exceptions documented | 1.0 | `exceptions` field present: list of conditions or explicitly `"None"` |
| S05 | Scope boundary clear | 1.0 | `scope` specifies system, agent_group, or domain — not "everything" |
| S06 | Violation examples concrete | 1.0 | `Violations` section has >= 2 breach scenarios with named consequences |
| S07 | Correct-use examples present | 1.0 | `Examples` section has >= 2 applications showing compliant behavior |
| S08 | All 8 body sections present | 1.0 | `Statement`, `Rationale`, `Enforcement`, `Exceptions`, `Examples`, `Violations`, `History`, `References` |
| S09 | Density >= 0.80 | 1.0 | No filler phrases: "is important", "helps the system", "in summary", "basically" |
| S10 | `priority` field present | 0.5 | Numeric priority or named tier (critical, high, medium) |
| S11 | `tags` includes `"invariant"` | 0.5 | Minimum tag set for routing |
| S12 | `keywords` field present with >= 2 terms | 0.5 | Improves brain search recall |
| S13 | `enforcement` is testsble | 0.5 | Can be verified by a script or checklist item — not "team awareness" |
| S14 | Cross-references valid | 0.5 | Any `references` items point to real artifacts or URLs |
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
| condition | Law covers a new domain with no precedent and rationale cannot be pre-filled |
