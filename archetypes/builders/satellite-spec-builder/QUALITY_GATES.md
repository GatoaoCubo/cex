---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for satellite_spec validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: satellite_spec

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p08_sat_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "satellite_spec" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 15+ required fields present | Completeness |
| H07 | name is non-empty string | Must identify a satellite |
| H08 | model is valid identifier (opus, sonnet, haiku, gpt-*) | Model must be actionable |
| H09 | mcps is list (empty OK) | Type safety for MCP list |
| H10 | role is non-empty string | Must define primary function |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "satellite" | 0.5 | 10 |
| S03 | Role section present in body | 1.0 | 10 |
| S04 | Model & MCPs section with concrete specs | 1.0 | 10 |
| S05 | Boot Sequence section with ordered steps | 1.0 | 10 |
| S06 | Dispatch section with keywords | 0.5 | 10 |
| S07 | No filler phrases ("various", "many things", "comprehensive") | 1.0 | 10 |
| S08 | Constraints section with concrete limits | 1.0 | 10 |
| S09 | Scaling & Monitoring section present | 0.5 | 10 |
| S10 | Dependencies explicitly listed (or "none") | 0.5 | 10 |

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
Primary: validate_artifact.py --kind satellite_spec [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Satellite name identified and not duplicate (brain_query checked)
- [ ] Model selected based on task complexity
- [ ] MCP servers identified with purpose
- [ ] Boot sequence documented and ordered
- [ ] Constraints and scaling limits defined
