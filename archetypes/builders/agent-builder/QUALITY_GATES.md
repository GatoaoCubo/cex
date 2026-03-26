---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for agent validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: agent

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p02_agent_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "agent" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | 10 required fields present (id, kind, pillar, title, version, satellite, domain, quality, tags, tldr) | Completeness |
| H07 | llm_function == "BECOME" | Agent is identity, not callable |
| H08 | satellite field is set (not blank or null) | Every agent belongs to a satellite |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty, not filler | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "agent" | 0.5 | 10 |
| S03 | iso_vectorstore section lists >= 10 ISO files | 1.0 | 10 |
| S04 | routing_keywords is list, len >= 4 | 0.5 | 10 |
| S05 | body has ## File Structure with correct ISO naming | 1.0 | 10 |
| S06 | capabilities_count matches actual bullets in Architecture | 1.0 | 10 |
| S07 | domain is specific (not "general" or "everything") | 0.5 | 10 |
| S08 | body has ## When to Use with NOT when exclusions | 0.5 | 10 |
| S09 | density_score >= 0.80 | 0.5 | 10 |
| S10 | No filler phrases ("this document", "in summary", "can help with") | 1.0 | 10 |

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
Primary: validate_artifact.py --kind agent [PLANNED]
Interim: validate manually against this file, checking each gate.

## Pre-Production Checklist
- [ ] Target agent identified with clear domain and satellite
- [ ] No existing agent for this identity (brain_query checked)
- [ ] Capabilities scoped to 4-8 concrete bullets
- [ ] ISO vectorstore file list complete (10 required files)
- [ ] Boundary defined (what agent does NOT handle)
