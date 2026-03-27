---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for path_config validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: path_config

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p09_path_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "path_config" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, scope, paths, platform, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Path Catalog, ## Directory Hierarchy, ## Platform Notes | Core sections required |
| H08 | No user-specific absolute paths (use expandable vars like {{HOME}}) | Portability |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "path_config" | 0.5 | 10 |
| S03 | paths names match path names in ## Path Catalog (zero drift) | 1.0 | 10 |
| S04 | Each path has: type, platform, default, required in catalog | 1.0 | 10 |
| S05 | Directory hierarchy shows parent-child relationships | 0.5 | 10 |
| S06 | Platform compatibility specified for each path | 0.5 | 10 |
| S07 | Forward slashes in all path templates | 0.5 | 10 |
| S08 | description <= 200 chars and non-generic | 0.5 | 10 |
| S09 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S10 | dir_count + file_count matches total paths in catalog | 0.5 | 10 |

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

## Pre-Production Checklist
- [ ] Scope identified (global, satellite, or service)
- [ ] All paths enumerated with concrete names
- [ ] Platform compatibility determined
- [ ] No existing path_config for this scope (brain_query checked)
- [ ] No user-specific absolute paths
