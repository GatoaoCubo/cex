---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for hook validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: hook

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_hook_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "hook" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 16 required fields present (id, kind, pillar, version, created, updated, author, trigger_event, script_path, execution, blocking, domain, quality, tags, tldr, timeout) | Completeness |
| H07 | trigger_event is valid enum value | Event compliance |
| H08 | timeout > 0 AND timeout <= 30000 | Timeout safety |
| H09 | If blocking: true, then timeout <= 10000 | Blocking hooks must be fast |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "hook" | 0.5 | 10 |
| S03 | Trigger Configuration section present with event and conditions | 1.0 | 10 |
| S04 | Script section present with path and language | 1.0 | 10 |
| S05 | Input/Output section present | 0.5 | 10 |
| S06 | Error Handling section present with strategy | 1.0 | 10 |
| S07 | error_handling field matches body description | 0.5 | 10 |
| S08 | script_path is a valid-looking path (not empty, has extension) | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this hook", "designed to", "various events") | 1.0 | 10 |

## Scoring Formula
```text
hard_pass = all 9 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind hook [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target event identified from enum
- [ ] Script exists or will be created at script_path
- [ ] No existing hook for this event+domain (brain_query checked)
- [ ] Blocking behavior decided (blocking hooks need fast scripts)
- [ ] Error handling strategy selected
