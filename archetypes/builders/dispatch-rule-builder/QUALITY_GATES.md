---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for dispatch_rule validation
pattern: HARD gates block publish, SOFT gates improve routing quality
---

# Quality Gates: dispatch_rule

## HARD Gates

| Gate | Check | Why |
|------|-------|-----|
| H01 | filename matches `p12_dr_{scope}.yaml` | namespace compliance |
| H02 | frontmatter parses as valid YAML | machine readability |
| H03 | `id` matches `^p12_dr_[a-z][a-z0-9_]+$` | ID contract |
| H04 | `kind` is literal `dispatch_rule` | type discriminator |
| H05 | `pillar` is literal `P12` | pillar anchor |
| H06 | `quality` is literal `null` | score integrity at authoring time |
| H07 | `keywords` is a non-empty list | routing requires at least one trigger |
| H08 | `satellite` is non-empty lowercase slug | dispatch target required |
| H09 | `model` in (`sonnet`, `opus`, `haiku`, `flash`) | valid model enum |
| H10 | `priority` is integer 1-10 | priority contract |
| H11 | `confidence_threshold` is float 0.0-1.0 | threshold contract |
| H12 | `fallback` differs from `satellite` | fallback must be distinct |
| H13 | file size <= 3072 bytes | schema constraint |
| H14 | no runtime status fields (`status`, `timestamp`, `quality_score`) | boundary against signal |
| H15 | no task/step/scope_fence fields | boundary against handoff |

## SOFT Gates

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | `scope` slug matches filename scope segment | 1.0 | 10 |
| S02 | `keywords` contains 3+ distinct terms | 0.5 | 10 |
| S03 | `tldr` is <= 120 chars and descriptive | 0.5 | 10 |
| S04 | `tags` includes satellite slug | 0.5 | 10 |
| S05 | `priority` reflects domain criticality (8+ for core domains) | 0.5 | 10 |
| S06 | `confidence_threshold` >= 0.6 (avoids noisy routing) | 1.0 | 10 |
| S07 | `routing_strategy` present and appropriate for keyword count | 0.5 | 10 |
| S08 | body sections present with rationale commentary | 0.5 | 10 |
| S09 | `conditions` omitted when no AND-conditions needed | 0.5 | 10 |
| S10 | keywords include both EN and PT variants for bilingual coverage | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 15 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5
PUBLISH: >= 8.0
REVIEW:  >= 7.0
REJECT:  < 7.0 or any HARD fail
```

## Pre-Publish Checklist
- [ ] filename uses `p12_dr_` prefix
- [ ] `id` matches filename scope
- [ ] `quality: null` present
- [ ] `fallback` != `satellite`
- [ ] no signal, handoff, or workflow drift
- [ ] keywords bilingual where relevant
