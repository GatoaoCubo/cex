---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for handoff validation
pattern: HARD gates block publish, SOFT gates improve delegation quality
---

# Quality Gates: handoff

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | filename matches `p12_ho_{task}.md` | namespace compliance |
| H02 | frontmatter parses as valid YAML | machine readability |
| H03 | all required frontmatter fields present: id, kind, lp, version, created, updated, author, satellite, mission, autonomy, quality_target, domain, quality, tags, tldr | completeness |
| H04 | `kind` is literal `handoff` | type integrity |
| H05 | `quality` is null | never self-score |
| H06 | `autonomy` in (`full`, `supervised`, `assisted`) | contract compliance |
| H07 | payload size <= 4096 bytes | schema constraint |
| H08 | no prompt fields: no `persona`, no `response_format`, no `temperature` | boundary against action_prompt |
| H09 | tasks are specific: each step starts with action verb | actionability |
| H10 | all 5 body sections present: Context, Tasks, Scope Fence, Commit, Signal | structural completeness |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | satellite value is lowercase slug | 0.5 | 10 |
| S02 | scope fence has both SOMENTE and NAO TOQUE | 1.0 | 10 |
| S03 | optional fields are omitted when unknown | 0.5 | 10 |
| S04 | tasks have 3-7 steps | 0.5 | 10 |
| S05 | commit paths match scope fence SOMENTE | 1.0 | 10 |
| S06 | signal section has concrete mechanism | 1.0 | 10 |
| S07 | payload stays <= 3072 bytes when feasible | 0.5 | 10 |
| S08 | context section explains WHY not just WHAT | 0.5 | 10 |
| S09 | seeds are present and relevant to domain | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 10 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5
PUBLISH: >= 8.0
REVIEW:  >= 7.0
REJECT:  < 7.0 or any HARD fail
```

## Pre-Publish Checklist
- [ ] filename uses `p12_ho_` prefix
- [ ] required frontmatter fields present
- [ ] all 5 body sections present
- [ ] scope fence has SOMENTE + NAO TOQUE
- [ ] no action_prompt or signal drift
- [ ] payload under 4096 bytes
