---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for embedding_config validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: embedding_config

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p01_emb_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "embedding_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 13+ required fields present | Completeness |
| H07 | dimensions is positive integer | Vector space must be numeric |
| H08 | chunk_size is positive integer | Chunking must be numeric |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "embedding" | 0.5 | 10 |
| S03 | Model section present in body | 1.0 | 10 |
| S04 | Chunking section with concrete numbers | 1.0 | 10 |
| S05 | model_name is specific identifier (not vague) | 0.5 | 10 |
| S06 | Integration section present | 0.5 | 10 |
| S07 | No filler phrases ("good model", "optimal", "comprehensive") | 1.0 | 10 |
| S08 | Performance section with latency/cost data | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 8 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind embedding_config [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Model identified with provider and specs
- [ ] Dimensions confirmed from model documentation
- [ ] Chunk size chosen for use case (retrieval vs summarization)
- [ ] Distance metric selected (cosine default)
- [ ] Cost known (null if local/free)
