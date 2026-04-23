---
kind: quality_gate
id: p05_qg_github_issue_template
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for github_issue_template
quality: 9.0
title: "Quality Gate Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for github_issue_template"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_github_issue_template
  - bld_instruction_github_issue_template
  - kc_github_issue_template
  - p09_qg_marketplace_app_manifest
  - p10_mem_github_issue_template_builder
  - p11_qg_audit_log
  - p01_qg_graph_rag_config
  - p05_qg_quickstart_guide
  - bld_knowledge_card_github_issue_template
  - p07_qg_benchmark_suite
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| GitHub issue template | required fields and labels | must have | all templates |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_git_[a-z][a-z0-9_]+.md$ | invalid filename pattern |
| H03 | kind field matches 'github_issue_template' | incorrect kind value |
| H04 | title field present | missing title |
| H05 | description field present | missing description |
| H06 | labels field present | missing labels |
| H07 | type field (bug/feature/question) present | invalid or missing type |
| H08 | steps_to_reproduce field present | missing steps |
| H09 | labels include 'kind/bug', 'kind/feature', or 'kind/question' | invalid label |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity of title and description | 0.20 | 1.0 (clear, actionable) to 0.0 (vague or missing) |
| D02 | Completeness of body sections | 0.25 | 1.0 (all sections present and useful) to 0.0 (<50% present) |
| D03 | Label and assignee accuracy | 0.20 | 1.0 (labels match GitHub taxonomy) to 0.0 (invalid or absent) |
| D04 | Placeholder guidance quality | 0.20 | 1.0 (each field has clear hint/placeholder) to 0.0 (bare vars) |
| D05 | Template uniqueness vs other templates | 0.15 | 1.0 (distinct purpose, no overlap) to 0.0 (duplicate) |

## Actions
| Score | Action |
|---|---|
| GOLDEN (>=9.5) | Auto-approve and merge |
| PUBLISH (>=8.0) | Review and merge |
| REVIEW (>=7.0) | Flag for review |
| REJECT (<7.0) | Reject and request fixes |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency hotfix | CTO | PR comment + approval timestamp |

## Examples

## Golden Example
```markdown
---
title: "Bug Report: Jenkins fails to deploy to PostgreSQL on Ubuntu 22.04"
labels: bug, jenkins, postgresql
---
**Title**:
Brief summary of the issue (e.g., "Jenkins fails to deploy to PostgreSQL on Ubuntu 22.04")

**Steps to reproduce**:
1. Install Jenkins 2.346 on Ubuntu 22.04
2. Configure PostgreSQL 14 as deployment target
3. Trigger pipeline with `git commit`

**Expected behavior**:
Successful deployment with no errors in Jenkins logs

**Actual behavior**:
Pipeline fails at "Deploy to PostgreSQL" stage with error: `Connection refused`

**Environment**:
- Jenkins: 2.346
- PostgreSQL: 14.2
- OS: Ubuntu 22.04 LTS
- Docker: 24.0.5

**Additional context**:
- Error occurs only when using `pg_dump` with `--inserts` flag
- No firewall rules blocking port 5432
```

## Anti-Example 1: Missing required fields
```markdown
---
title: "Bug Report"
labels: bug
---
**Title**:
Jenkins not working

**Steps to reproduce**:
1. Use Jenkins
2. Try to deploy

**Expected behavior**:
It should work

**Actual behavior**:
It doesn't work

**Environment**:
- Jenkins: 2.346
```
## Why it fails explanation
Lacks specificity in all sections. No labels for PostgreSQL or OS. Missing critical details like PostgreSQL version, error logs, and reproduction steps. Users cannot diagnose without context.

## Anti-Example 2: Vague optional fields
```markdown
---
title: "Feature Request"
labels: feature
---
**Title**:
Add something cool

**Steps to reproduce**:
Not applicable

**Expected behavior**:
Something happens

**Actual behavior**:
Nothing happens

**Environment**:
- Maybe Linux?
```
## Why it fails explanation
Uses ambiguous language ("something cool", "nothing happens"). Optional fields like "Additional context" are missing. No clear structure for feature requests. Lacks required fields for reproducibility.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
