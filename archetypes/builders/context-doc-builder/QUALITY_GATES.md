---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for context_doc validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: context_doc

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses without error | Broken YAML = broken artifact |
| H02 | id matches `^p01_ctx_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this invariant |
| H04 | kind == "context_doc" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, domain, scope | Kind contract compliance |
| H07 | Body <= 2048 bytes (sections after frontmatter) | Size constraint from _schema.yaml |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "context-doc" | 0.5 | 10 |
| S03 | `## Scope` section present and >= 3 lines | 1.0 | 10 |
| S04 | `## Background` section non-empty | 1.0 | 10 |
| S05 | No filler phrases ("this document", "in summary", "basically") | 1.0 | 10 |
| S06 | density_score >= 0.80 (if provided) | 0.5 | 10 |
| S07 | `## Constraints & Assumptions` section present | 1.0 | 10 |
| S08 | `## Dependencies` section lists at least one item | 0.5 | 10 |

## Scoring Formula

```text
hard_pass = all 7 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: `validate_artifact.py --kind context_doc` [PLANNED]
Interim: validate manually against this file, checking each gate in order.

## Pre-Production Checklist
- [ ] Domain identified and scope sentence written
- [ ] brain_query run — no duplicate context_doc for same domain+scope
- [ ] id set before writing body (id drives filename)
- [ ] Body byte count checked after compose (<= 2048)
- [ ] quality: null confirmed in frontmatter
- [ ] Companion .yaml produced with same frontmatter
