---
kind: schema
id: bld_schema_unit_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for unit_eval
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: unit_eval
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_ue_{target_slug}) | YES | — | Namespace compliance |
| kind | literal "unit_eval" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target | string | YES | — | Agent/prompt being tested |
| target_kind | string | YES | — | Artifact kind of the target |
| input | string | YES | — | Exact input to feed the target |
| expected_output | string | YES | — | Correct output for this input |
| assertions | list[object] | YES | — | Gate-mapped checks |
| timeout | integer (seconds) | YES | 60 | Max execution time |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| setup | string | REC | — | Preconditions before test |
| teardown | string | REC | — | Cleanup after test |
| edge_case | boolean | REC | false | Edge case flag |
| coverage_scope | string | REC | — | What this test covers |
| score | float | REC | — | Expected minimum score |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_ue_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Assertion Object Schema
```yaml
- gate_ref: "H01"
  check: "YAML parses without error"
  expected: true
  severity: "HARD"
```
## Body Structure (required sections)
1. `## Input` — exact input/prompt (verbatim)
2. `## Expected Output` — correct output
3. `## Assertions` — gate-mapped checks with expected values
4. `## Setup` — preconditions
5. `## Teardown` — cleanup
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_ue_{target_slug}.md + .yaml
- id == filename stem
- quality: null always
- assertions must be non-empty list
- each assertion must have gate_ref
