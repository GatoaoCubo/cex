---
id: p11_qg_skill
kind: quality_gate
pillar: P11
title: "Gate: Skill"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: skill
quality: null
density_score: 0.85
tags:
  - quality-gate
  - skill
  - reusable-capability
  - p11
tldr: "Gates ensuring skill files define a specific trigger, two or more typed workflow phases, and phase-level error handling without claiming agent identity."
---

## Definition
A skill is a reusable capability: a named sequence of phases that can be invoked by a trigger and composed with other skills. A skill passes this gate when the trigger is specific enough to avoid false activations, each phase has typed input and output, error handling is defined at the phase level (not just globally), and the skill makes no claims about being an agent — it is a procedure, not an identity.
## HARD Gates
Failure on any HARD gate = immediate REJECT regardless of score.
| ID  | Check | Rationale |
|-----|-------|-----------|
| H01 | Frontmatter parses as valid YAML with no syntax errors | Unparseable file cannot be indexed or validated |
| H02 | `id` matches the file's directory namespace (`skill-builder/...`) | Mismatched IDs cause routing failures |
| H03 | `id` value equals the filename stem (slug portion) | Filename and ID must be the same addressable key |
| H04 | `kind` is exactly `skill` (literal match, no variation) | Kind drives the loader; wrong literal silently misroutes |
| H05 | `quality` field is `null` (not filled by author) | Quality is assigned by this gate, not self-reported |
| H06 | All required frontmatter fields present: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | Incomplete frontmatter breaks downstream consumers |
| H07 | Spec contains a **Trigger definition** (slash command name, keyword pattern, or event type that activates the skill) | Without a trigger, the skill cannot be invoked programmatically or by convention |
| H08 | Spec contains >= 2 **Workflow Phases** (each phase is a named step in the execution sequence) | A single-phase skill is a function, not a skill; phased structure enables partial retry and composition |
| H09 | Spec contains **Input and Output** per phase (field names and types, not just prose descriptions) | Typed per-phase I/O is the contract that enables composition with other skills |
## SOFT Scoring
Dimensions are weighted; total normalized weight = 100%.
| # | Dimension | Weight | 1 (Poor) | 5 (Good) | 10 (Excellent) |
|---|-----------|--------|----------|----------|----------------|
| 1 | density >= 0.80 (content per token ratio) | 1.0 | Padded with filler prose | Mostly substantive | No filler; every sentence carries information |
| 2 | Trigger is specific not generic (trigger will not fire on unrelated inputs) | 1.0 | Generic keyword like "do" or "run" | Moderately specific | Exact slash command or narrow keyword pattern with exclusion rules |
| 3 | Phases have clear boundaries (entry condition, exit condition, and handoff artifact per phase) | 1.0 | Phases blend together | Start/end noted | Explicit entry condition, exit condition, and handoff artifact per phase |
| 4 | Input/output typed per phase (not just final output typed) | 1.0 | Only final output typed | Partial typing | Every phase has named fields with types for both input and output |
| 5 | user_invocable flag correct (`true` if user can trigger it, `false` if internal-only) | 0.5 | Missing | Present but unchecked | Present and verified against trigger type |
| 6 | Tags include `skill` | 0.5 | Missing | Present but misspelled | Exactly `skill` in tags list |
| 7 | Error handling per phase (each phase has its own error class, retry rule, and fallback) | 1.0 | No error handling | Global handler only | Each phase has error class, retry rule, and fallback |
| 8 | Phase dependencies documented (which phases must complete before the next; parallel-eligible phases noted) | 1.0 | No dependencies stated | Sequential assumed | Explicit dependency graph including any parallel-eligible phases |