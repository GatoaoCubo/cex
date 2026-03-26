---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for spawn_config validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: spawn_config

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p12_spawn_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "spawn_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 19 required fields present | Completeness |
| H07 | body has ## Spawn Command section | Core content |
| H08 | mode in (solo, grid, continuous) | Valid enum value |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "spawn_config" | 0.5 | 10 |
| S03 | flags includes baseline (--dangerously-skip-permissions, --no-chrome) | 1.0 | 10 |
| S04 | satellite name is lowercase | 0.5 | 10 |
| S05 | timeout is reasonable (300-7200 seconds) | 0.5 | 10 |
| S06 | Parameters section present with rationale | 0.5 | 10 |
| S07 | No task instructions in body (boundary check) | 1.0 | 10 |
| S08 | No filler phrases ("this document", "in summary") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind spawn_config [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Spawn scenario identified (solo/grid/continuous)
- [ ] Satellite-model pairing confirmed from routing table
- [ ] Required MCP servers identified for target satellite
