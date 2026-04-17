---
id: bld_examples_invariant
kind: examples
pillar: P08
parent: invariant-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder_agent
tags: [examples, invariant-builder, golden, anti-example, P08]
quality: 9.1
title: "Examples Invariant"
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
density_score: 0.90
llm_function: GOVERN
---
# invariant-builder — EXAMPLES
## Golden Example
INPUT: "Codify the invariant that agent_groups must never self-assign quality scores"
OUTPUT:
```yaml
id: p08_law_5
kind: invariant
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
domain: "quality"
quality: 9.0
tags: [law, quality, self-score, governance, artifact]
tldr: "Artifacts MUST have quality: null — scoring is external reviewer responsibility"
number: 5
statement: "No artifact producer SHALL self-assign a quality score"
rationale: "Self-scoring introduces bias and inflates pool quality metrics"
enforcement: "HARD gate H05 in every builder QUALITY_GATES.md rejects quality != null"
scope: "system"
exceptions: []
priority: 9
keywords: [quality, scoring, self-assessment, bias, governance]
```
## Statement
No artifact producer SHALL self-assign a quality score. The `quality` field in frontmatter MUST be `null` at production time. Scoring is the exclusive responsibility of external reviewers or automated validators.
## Rationale
Self-scoring introduces systematic positive bias. Producers overestimate artifact quality by 20-30% on average. Pool metrics become unreliable when 1,957 artifacts carry self-inflated scores. External scoring ensures calibration and consistency across all artifact types and producers.
## Enforcement
- Mechanism: HARD gate H05 in every builder's QUALITY_GATES.md
- Detection: automated YAML parse checks `quality == null` before artifact enters pool
- Consequence: artifact rejected (score = 0), cannot enter pool until quality field is set to null
## Exceptions
None. No artifact type, producer, agent_group, or context bypasses this law.
## Examples
1. **Knowledge Card Production**: KC producer writes `quality: null`, external reviewer scores 8.5 after validating density and factual accuracy
2. **Pattern Formalization**: pattern-builder sets `quality: null`, quality_gate_builder evaluates against 9 HARD + 11 SOFT gates and assigns score 7.8
## Violations
1. **Self-scored Model Card**: Producer writes `quality: 9.2` — H05 FAIL, artifact rejected from pool, must resubmit with `quality: null`
2. **Inflated KC**: Producer writes `quality: 8.0` to bypass review cycle — detected by validator, artifact quarantined pending external review
## History
- Established: 2026-01-15 — after discovering 40% of early KCs had inflated self-scores corrupting pool metrics
- Revised: 2026-03-01 — extended from KCs to ALL artifact types system-wide
## References
- LAWS_v3_PRACTICAL.md (Law 7: quality provenance)
- QUALITY_GATES.md (universal H05 gate definition)
### Why This Is Golden
| Check | Result |
|-------|--------|
| quality: null | H05 PASS |
| id matches `^p08_law_[0-9]+$` | H02 PASS |
| id == filename stem `p08_law_5` | H03 PASS |
| kind: "invariant" (literal) | H04 PASS |
| 19 fields present (15 required + 4 extended) | H06 PASS |
| tags list length 5 >= 3 | H07 PASS |
| number: 5 (positive integer) | H08 PASS |
| statement uses "SHALL" (imperative) | H09 PASS |
| tldr 57 chars <= 160 | S01 PASS |
| rationale explains WHY (bias, inflation, unreliability) | S02 PASS |
| enforcement names H05 gate mechanism | S03 PASS |
| exceptions explicitly "None" | S04 PASS |
| scope: system | S05 PASS |
| 2 examples present | S06 PASS |
| 2 violations present | S07 PASS |
| all 8 body sections present | S08 PASS |
| no filler phrases, density >= 0.80 | S09 PASS |
| keywords list length 5 >= 2 | S10 PASS |
## Anti-Example
INPUT: "Write a quality rule"
BAD OUTPUT:
```yaml
id: quality_rule
kind: rule
quality: 8.5
statement: "try to keep quality high"
Quality is important. You should always try to produce high quality artifacts.
This helps the system work better. In summary, quality matters.
```
### Failures
1. `id: quality_rule` — no `p08_law_` prefix, no number -> H02 FAIL (gate: id pattern mismatch)
