---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for brain_index artifacts
---

# Quality Gates: brain_index

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses |
| H02 | id starts with p10_bi_ |
| H03 | id == filename stem |
| H04 | kind == brain_index |
| H05 | pillar == P10 |
| H06 | quality == null |
| H07 | algorithm in [bm25, faiss, hybrid] |
| H08 | scope is non-empty string |
| H09 | corpus_type in [text, vector, structured] |
| H10 | rebuild_schedule in [on_change, hourly, daily, weekly, manual] |
| H11 | freshness_max_days is non-negative integer |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items | 0.5 |
| S03 | Algorithm Config has parameters for chosen algorithm | 1.0 |
| S04 | Filters has >= 2 entries with type and condition | 1.0 |
| S05 | Ranking has >= 2 factors with weights | 1.0 |
| S06 | Rebuild section has schedule and trigger | 1.0 |
| S07 | Monitoring has >= 2 metrics with thresholds | 0.5 |
| S08 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0
