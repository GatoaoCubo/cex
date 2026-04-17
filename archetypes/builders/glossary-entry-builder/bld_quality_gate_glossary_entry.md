---
id: p11_qg_glossary_entry
kind: quality_gate
pillar: P11
title: "Gate: glossary_entry"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: "glossary_entry — concise domain term definitions with synonyms, disambiguation, and usage context"
quality: 9.0
tags: [quality-gate, glossary-entry, terminology, definition, P11]
tldr: "Validates glossary_entry artifacts: 3-line definition constraint, synonym presence, disambiguation clarity, and no circular references."
density_score: 0.89
llm_function: GOVERN
---
# Gate: glossary_entry
## Definition
| Field     | Value |
|-----------|-------|
| metric    | composite score across SOFT dimensions |
| threshold | >= 7.0 to publish; >= 9.5 for golden |
| operator  | weighted average after all HARD gates pass |
| scope     | all artifacts where `kind: glossary_entry` |
All HARD gates are AND-logic: one failure rejects the artifact regardless of SOFT score.
## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Any YAML syntax error |
| H02 | ID matches `^p01_gl_[a-z][a-z0-9_]+$` | Wrong format or namespace |
| H03 | ID equals filename stem (no extension) | Mismatch between id field and file name |
| H04 | Kind equals literal `glossary_entry` | Any other value |
| H05 | `quality` field is null | Any non-null value |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, term, domain, quality, tags, tldr | Any missing field |
| H07 | `definition` body section is <= 3 lines | Exceeds the conciseness constraint for this kind |
| H08 | `synonyms` is a list with len >= 1 | Missing or empty synonyms list |
| H09 | `term` is non-empty string | Missing or blank term field |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| S01 | `tldr` IS the definition (not meta-commentary about the entry) | 0.12 | Is the definition=1.0, meta-comment=0.2 |
| S02 | Tags list len >= 3, includes `glossary` | 0.05 | Met=1.0, partial=0.5 |
| S03 | Definition section present in body (not just frontmatter) | 0.10 | Present=1.0, absent=0.0 |
| S04 | Definition includes a concrete usage example | 0.10 | Present=1.0, absent=0.0 |
| S05 | `term` is lowercase unless it is a proper noun | 0.05 | Correct=1.0, wrong case=0.3 |
| S06 | Disambiguation section present and references at least one similar term | 0.12 | Present+reference=1.0, absent=0.0 |
| S07 | No circular reference (term not used to define itself) | 0.13 | No circular ref=1.0, circular=0.0 |
| S08 | Related Terms section with cross-references to other entries | 0.08 | Present=1.0, absent=0.0 |
| S09 | Boundary from `knowledge_card` and `context_doc` stated | 0.10 | Both stated=1.0, one=0.5, absent=0.0 |
| S10 | No filler phrases ("very important", "basically", "in summary") | 0.10 | Clean=1.0, filler present=0.0 |
| S11 | `density_score` >= 0.80 | 0.05 | Met=1.0, below=0.0 |
**Weight sum: 1.00**
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — reference artifact for glossary_entry calibration |
| >= 8.0 | PUBLISH — pool-eligible; definition concise and disambiguated |
| >= 7.0 | REVIEW — usable but missing usage example or disambiguation |
| < 7.0  | REJECT — redo; likely circular definition, oversized, or no synonyms |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Term is a proper noun (product name, acronym) where synonyms are genuinely N/A |
| approver | Domain owner who manages the target glossary namespace |
| audit trail | Required: justification for N/A synonyms, glossary namespace, approver name |
| expiry | Permanent; terminology bypass does not expire |
| never bypass | H01 (corrupt YAML), H05 (self-scored quality invalid), H07 (3-line limit is the defining constraint of this kind — bypass makes it a knowledge_card) |
