---
kind: examples
id: bld_examples_axiom
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of axiom artifacts
pattern: few-shot learning — LLM reads these before producing
---

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
author: "EDISON"
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
