---
id: p11_qg_lens
kind: quality_gate
pillar: P11
title: "Gate: Lens"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
domain: lens
quality: 9.0
tags: [quality-gate, lens, perspective, P02, filter]
tldr: "Quality gate for lens artifacts: enforces declared bias, scoped focus, and explicit applies_to list."
density_score: 0.85
llm_function: GOVERN
---
# Gate: Lens
## Definition
A `lens` is a perspective filter applied to artifact evaluation or routing. It amplifies certain attributes and suppresses others without executing logic. Gates here prevent lenses from claiming capabilities (which belong to agents), enforce honest bias declaration, and require a concrete `applies_to` scope so the lens is never applied indiscriminately.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p02_lens_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"lens"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | All required fields present and non-empty (`id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `perspective`, `applies_to`, `bias`, `tags`, `tldr`) | Incomplete artifact |
| H07 | `Focus` section present in body | Lens has no defined focus — unusable |
| H08 | `applies_to` is a list with >= 1 item | Lens has no target scope — unsafe to apply |
| H09 | `bias` field is explicitly declared (string value or `null` for neutral) | Hidden bias corrupts evaluations |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, states what the lens amplifies, not just its name |
| S02 | Focus narrowly scoped | 1.0 | Focus section targets one concern — not "quality in general" |
| S03 | Bias declaration honest | 1.0 | Bias names what the lens systematically over- or under-weights |
| S04 | `applies_to` types valid | 1.0 | Each item matches a known artifact `kind` in the registry |
| S05 | Interpretation criteria clear | 1.0 | Body defines what score high vs. low on this lens means |
| S06 | Weight or priority defined | 0.5 | `weight` or `priority` field present and numeric |
| S07 | Examples of lens application | 1.0 | >= 2 worked examples showing lens applied to a real artifact |
| S08 | `tags` includes `"lens"` | 0.5 | Minimum tag for routing |
| S09 | Complementary lenses referenced | 0.5 | `related` field names >= 1 lens that pairs with this one |
| S10 | No capability claims | 1.0 | Body contains no phrases like "this lens will execute", "performs", "runs" |
| S11 | Density >= 0.80 | 1.0 | No filler phrases: "provides a way to", "helps us understand", "in summary" |
| S12 | Limitations section present | 0.5 | Documents conditions where lens should not be applied |
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
| condition | Lens is experimental — `applies_to` scope cannot be confirmed until integration testing complete |
| approver | P02 domain owner |
| audit_log | Entry required in `records/governance/bypass_log.md` with gate ID, lens id, and test plan reference |
| expiry | 7 days — `applies_to` must be confirmed or lens moves to DRAFT state |
H01 and H05 cannot be bypassed under any condition.
