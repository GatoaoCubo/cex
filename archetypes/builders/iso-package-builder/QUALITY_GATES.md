---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for iso_package validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: iso_package

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML manifest parses | Broken YAML = broken package |
| H02 | id matches `^p02_iso_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id prefix matches directory name | Discovery relies on this |
| H04 | kind == "iso_package" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 14 required fields present (id, kind, pillar, version, created, updated, author, agent_name, tier, files_count, domain, quality, tags, tldr) | Completeness |
| H07 | 3 required files exist (manifest.yaml, system_instruction.md, instructions.md) | Minimal tier compliance |
| H08 | files_count matches actual file count in directory | Inventory integrity |
| H09 | system_instruction.md <= 4096 tokens | Context window safety |
| H10 | No hardcoded paths in any file | Portability guarantee |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "iso-package" | 0.5 | 10 |
| S03 | tier matches actual file count threshold | 1.0 | 10 |
| S04 | Each file has correct pillar in lp_mapping | 1.0 | 10 |
| S05 | examples.md has >= 2 examples | 1.0 | 10 |
| S06 | density >= 0.80 across all files | 1.0 | 10 |
| S07 | All files <= 4096 bytes | 0.5 | 10 |
| S08 | lp_mapping present with all included files | 0.5 | 10 |
| S09 | No filler phrases in any file | 1.0 | 10 |
| S10 | File Inventory table in manifest lists all files | 0.5 | 10 |
| S11 | portable == true and no path violations found | 0.5 | 10 |
| S12 | instructions.md has 3-phase structure (research/compose/validate) | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 10 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Automation
Primary: validate_artifact.py --kind iso_package [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target agent identified with clear domain
- [ ] No existing iso_package for this agent (brain_query checked)
- [ ] Tier selected based on deployment needs
- [ ] Source agent definition available for reference
- [ ] All required files drafted before packaging
