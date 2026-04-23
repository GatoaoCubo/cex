---
id: p11_qg_law
kind: quality_gate
pillar: P11
parent: invariant-builder
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder_agent
tags: [quality-gate, law, governance, P08, enforcement]
quality: 9.0
title: "Gate: Law"
tldr: "Quality gate for invariant artifacts: enforces imperative statement, rationale, and testsble enforcement mechanism."
domain: law
density_score: 0.85
llm_function: GOVERN
related:
  - p03_ins_law
  - bld_examples_invariant
  - bld_knowledge_card_invariant
  - bld_schema_invariant
  - p11_qg_mental_model
  - p11_qg_learning_record
  - p11_qg_model_card
  - p11_qg_model_provider
  - p11_qg_quality_gate
  - p11_qg_embedder_provider
---

## Quality Gate

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

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
