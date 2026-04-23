---
kind: quality_gate
id: p11_qg_axiom
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of axiom artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: axiom"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, axiom, P11, P10, governance, immutable, fundamental-truth]
tldr: "Gates for axiom artifacts — immutable fundamental rules that govern a domain permanently."
domain: axiom
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.89
related:
  - bld_examples_axiom
  - bld_examples_invariant
  - p11_qg_builder
  - p11_qg_naming_rule
  - bld_instruction_axiom
  - bld_knowledge_card_quality_gate
  - bld_output_template_axiom
  - bld_config_axiom
  - tpl_axiom
  - p11_qg_quality_gate
---

## Quality Gate

# Gate: axiom
## Definition
| Field     | Value                                          |
|-----------|------------------------------------------------|
| metric    | immutability rigor + scope boundary precision  |
| threshold | 8.0                                            |
| operator  | >=                                             |
| scope     | all axiom artifacts (P10)                      |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = axiom invisible to system |
| H02 | id matches `^p10_ax_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "axiom" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 13 required fields present | Completeness |
| H07 | tags is list, len >= 3 | Searchability minimum |
| H08 | rule field is ONE sentence (no period-separated compound rules) | Atomicity — one axiom, one truth |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | rationale present with >= 2 distinct reasons | 1.0 |
| S03 | scope names concrete domain boundary (not "everything") | 1.0 |
| S04 | enforcement describes detection mechanism, not just intent | 1.0 |
| S05 | immutable == true field present | 0.5 |
| S06 | body has all 7 required sections | 1.0 |
| S07 | Examples section has >= 2 cases (valid and invalid) | 1.0 |
| S08 | Violations section has >= 1 concrete breach scenario | 1.0 |
| S09 | density_score >= 0.80 | 1.0 |
| S10 | keywords present, len >= 2 | 0.5 |
Weights sum: 9.0. Normalize: divide each by 9.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical axiom |
| >= 8.0 | PUBLISH — active governance enforcement |
| >= 7.0 | REVIEW — sharpen rule atomicity or add violation scenarios |
| < 7.0  | REJECT — rule is not immutable, or scope is underdefined |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Axiom required to block active system violation in production |
| approver | p10-chief |
| audit_trail | Log in records/audits/ with violation evidence and timestamp |
| expiry | 24h — axioms must be fully specified before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |

## Examples

# Examples: axiom-builder
## Golden Example
INPUT: "Formalize the CEX rule that quality scores must never be self-assigned"
OUTPUT:
```yaml
id: p10_ax_quality_never_self_scored
kind: axiom
pillar: P10
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
domain: "quality_assurance"
quality: null
tags: [axiom, quality, self-score, integrity, evaluation]
tldr: "No artifact may assign its own quality score; external validation required"
rule: "An artifact producer MUST NOT assign a quality score to its own output"
scope: "All CEX artifacts across all pillars (P01-P12)"
rationale: "Self-scoring creates unfalsifiable feedback loops that erode trust"
enforcement: "HARD gate H05 in every builder rejects quality != null"
immutable: true
priority: 10
dependencies: []
keywords: [quality, self-score, validation, integrity]
linked_artifacts:
  primary: null
  related: [p11_qg_knowledge_card, p11_qg_model_card]
```
## Rule Statement
An artifact producer MUST NOT assign a quality score to its own output.
## Rationale
- Self-scoring creates circular validation — the producer judges itself
- External scoring enables calibration across producers and domains
- Every quality framework (peer review, ISO 9001) separates production from evaluation
## Scope
- Domain: All artifact production in CEX
- System: Every builder, every pillar (P01-P12)
- Layer: Governance (quality gate enforcement)
## Enforcement
- Detection: HARD gate H05 in every quality_gate checks quality == null
- Response: Artifact rejected at publish; builder must output quality: null
## Examples
1. knowledge-card-builder sets quality: null; external reviewer scores 8.5
2. signal-builder emits signal with quality_score from monitor, not from self
## Violations
1. Builder outputs quality: 9.0 on its own artifact
   - Impact: Score inflation, pool contamination, trust erosion
   - Resolution: Reject artifact, re-validate with external scorer
## References
- CEX BUILDER_NORMS.md rule 2
- ISO 9001 separation of production and inspection
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p10_ax_ pattern (H02 pass)
- kind: axiom (H04 pass)
- 20 fields present including all 13 required (H06 pass)
- rule is ONE atomic sentence (H08 pass)
- tldr <= 160 chars (S01 pass)
- rationale has 3 reasons (S02 pass)
- scope names concrete boundary (S03 pass)
- enforcement describes detection mechanism (S04 pass)
- 7 body sections present (S06 pass)
## Anti-Example
INPUT: "Document the quality scoring rule"
BAD OUTPUT:
```yaml
id: quality_rule
kind: rule
pillar: P10
version: 1
quality: 9.5
tags: quality
rule: "Quality scores should generally not be self-assigned by the producer, and when they are, they should be reviewed by someone else afterwards"
Quality is important. This document describes how quality works in our system.
In summary, we believe that quality should be externally validated.
```
FAILURES:
1. id: no `p10_ax_` prefix -> H02 FAIL
2. kind: "rule" not "axiom" -> H04 FAIL
3. quality: 9.5 (self-assigned) -> H05 FAIL
4. version: integer not semver -> H06 FAIL
5. tags: string not list -> H07 FAIL
6. rule: compound sentence with "and" -> H08 FAIL
7. Missing required fields: created, updated, author, domain, scope, tldr -> H06 FAIL
8. Body is filler prose ("Quality is important") -> S09 FAIL
9. No body sections (Rule Statement, Rationale, etc.) -> S06 FAIL
10. No examples or violations sections -> S07, S08 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
