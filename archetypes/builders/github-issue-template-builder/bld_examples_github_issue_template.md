---
kind: examples
id: bld_examples_github_issue_template
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of github_issue_template artifacts
quality: 9.0
title: "Examples Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, examples]
tldr: "Golden and anti-examples of github_issue_template artifacts"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
