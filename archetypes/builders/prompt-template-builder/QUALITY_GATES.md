---
id: qg_prompt_template_builder
kind: quality_gates
pillar: P11
llm_function: GOVERN
domain: prompt_template
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [quality-gates, prompt-template, P03, hard-gates, soft-gates]
---

# Quality Gates — prompt-template-builder

## HARD Gates (H01-H08) — Blocking

All HARD gates must PASS before delivery. A single FAIL blocks the artifact.

| Gate | ID | Check | How to verify |
|---|---|---|---|
| ID pattern | H01 | `id` matches `^p03_pt_[a-z][a-z0-9_]+$` | Regex match on frontmatter id field |
| Required fields | H02 | All 5 required fields present: id, kind, title, variables, quality | Scan frontmatter keys |
| No undeclared vars | H03 | Every `{{var}}` in template body appears in variables list | Extract all `{{...}}` from body; diff against declared names |
| No unused vars | H04 | Every declared variable appears at least once in template body | Extract declared names; check each against body text |
| Size limit | H05 | File size <= 8192 bytes | `wc -c` or equivalent byte count |
| Valid syntax tier | H06 | `variable_syntax` is either `"mustache"` or `"bracket"` | Enum check on frontmatter field |
| Variable fields complete | H07 | Every variable object has: name, type, required, default, description | Iterate variables list; check all 5 fields present |
| Body non-empty | H08 | Template body section exists, is non-empty, contains >= 1 `{{variable}}` | Parse body section; check for at least one slot |

## SOFT Gates (S01-S10) — Scoring

Each SOFT gate contributes to the quality score. Score = (passed soft gates / 10) * 1.0.

| Gate | ID | Check | Weight |
|---|---|---|---|
| TLDR present and concise | S01 | `tldr` field is a single sentence, <= 120 chars | 0.10 |
| Tags populated | S02 | `tags` list has >= 3 items | 0.10 |
| Keywords populated | S03 | `keywords` list has >= 3 items distinct from tags | 0.10 |
| Composable declared | S04 | `composable` field is explicitly set (not absent) | 0.05 |
| Domain declared | S05 | `domain` field is non-empty string | 0.10 |
| Purpose section complete | S06 | `## Purpose` section is >= 2 sentences | 0.10 |
| Variables table matches list | S07 | Variables Table in body has same rows as frontmatter variables list | 0.15 |
| Examples section present | S08 | `## Examples` section has >= 1 filled example with rendered output | 0.15 |
| Density score set | S09 | `density_score` field is a float (not null) | 0.05 |
| Version follows semver | S10 | `version` matches `^\d+\.\d+\.\d+$` | 0.10 |

## Scoring Formula

```
hard_score  = 1.0 if ALL H01-H08 PASS else 0.0  (blocking)
soft_score  = sum(weight_i for each passing S gate) / sum(all weights)
final_score = hard_score * soft_score
```

Write `final_score` (rounded to 2 decimal places) into the `quality` field before delivery.

Pool submission requires: `quality >= 0.80`

## Automation

Gate checks can be automated with a validator script:

```python
# Pseudocode — implement in records/core/python/validators/prompt_template_validator.py
def validate(artifact_path):
    data = parse_frontmatter(artifact_path)
    body = parse_body(artifact_path)
    hard_results = run_hard_gates(data, body)   # H01-H08
    soft_results = run_soft_gates(data, body)   # S01-S10
    score = compute_score(hard_results, soft_results)
    return ValidationResult(hard=hard_results, soft=soft_results, score=score)
```

## Pre-Production Checklist

Before writing a single line of the artifact:

- [ ] Purpose identified and confirmed as prompt_template (not a sibling kind)
- [ ] All dynamic slots extracted from the raw request
- [ ] Every slot typed (string/list/integer/boolean/object)
- [ ] Every slot marked required or optional with default
- [ ] topic_slug chosen and ID pattern pre-validated
- [ ] variable_syntax tier chosen (mustache default)
- [ ] Output path confirmed (pool vs draft)

Before delivery:

- [ ] H01 id pattern check PASS
- [ ] H02 required fields check PASS
- [ ] H03 no undeclared vars PASS
- [ ] H04 no unused vars PASS
- [ ] H05 size <= 8192 bytes PASS
- [ ] H06 valid syntax tier PASS
- [ ] H07 variable fields complete PASS
- [ ] H08 body non-empty PASS
- [ ] quality field updated with final_score
- [ ] updated date set to today
