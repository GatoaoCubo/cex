---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for benchmark validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: benchmark

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p07_bm_ |
| H03 | id == filename stem |
| H04 | kind == benchmark |
| H05 | pillar == P07 |
| H06 | quality == null |
| H07 | unit is non-empty string |
| H08 | iterations >= 10 |
| H09 | warmup >= 1 |
| H10 | percentiles includes at least 50 and 95 |
| H11 | direction in [lower_is_better, higher_is_better] |
| H12 | baseline and target are numeric, same unit implied |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3 | 0.5 |
| S03 | Benchmark Overview section present | 1.0 |
| S04 | Methodology section with iterations, warmup, protocol | 1.0 |
| S05 | Environment section with hardware, software, config | 1.0 |
| S06 | Metrics table with baseline and target columns | 1.0 |
| S07 | No filler prose (no "acceptable", "good performance") | 1.0 |
| S08 | Results Template with percentile rows | 0.5 |
| S09 | density >= 0.80 | 1.0 |

## Scoring
```text
hard_pass = all 12 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind benchmark [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Metric identified with unit and direction
- [ ] Baseline measured (not estimated)
- [ ] Environment documented with exact versions
- [ ] No existing benchmark for same metric+environment
