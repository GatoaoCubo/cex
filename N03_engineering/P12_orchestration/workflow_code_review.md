---
id: p12_wf_code_review
kind: workflow
pillar: P12
title: "Workflow — Code Review"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [workflow, code-review, n03, github, pull-request]
tldr: "5-step code review workflow: fetch PR → analyze diff → apply 7D rubric → write inline comments → submit review decision. Uses GitHub MCP for all operations."
density_score: 0.89
---

# Workflow: Code Review

## Trigger

```yaml
trigger: "review PR #N" | "review latest PRs" | automated (PR opened)
input:
  repo: owner/repo
  pr_number: N (optional — if omitted, review all open PRs)
```

## Steps

### Step 1: Fetch PR Details (30s)

```yaml
action: Get PR metadata + diff
mcp_calls:
  - github_get_pull_request(repo, pr_number)
  - github_get_pull_request_diff(repo, pr_number)
  - github_list_commits(repo, pr_number)
output:
  title, description, author, files_changed, additions, deletions, diff
```

### Step 2: Analyze Diff (2min)

```yaml
action: Parse diff, identify changes by category
analysis:
  - files_added: list of new files
  - files_modified: list of changed files
  - files_deleted: list of removed files
  - change_categories: [logic, tests, config, docs, deps]
  - pr_size: small (<100) | medium (100-500) | large (500-1000) | xl (>1000)
  - breaking_changes: boolean
```

### Step 3: Apply 7D Rubric (3min)

```yaml
action: Score each dimension
reads:
  - kc_code_review (7-dimension rubric)
  - kc_security_practices (security checks)
  - kc_error_handling_python (error patterns)
dimensions:
  correctness: { weight: 25%, checks: [logic, edge_cases, null_handling] }
  security: { weight: 20%, checks: [injection, auth, secrets, xss] }
  performance: { weight: 15%, checks: [n_plus_1, unbounded, memory] }
  readability: { weight: 15%, checks: [naming, function_size, comments] }
  tests: { weight: 10%, checks: [coverage, edge_cases, mocks] }
  documentation: { weight: 10%, checks: [docstrings, readme, api_docs] }
  architecture: { weight: 5%, checks: [layer_violation, circular_deps, patterns] }
output:
  scores: { correctness: 8, security: 9, ... }
  overall: 8.3
  issues: [{ file, line, dimension, severity, message, suggestion }]
```

### Step 4: Write Comments (2min)

```yaml
action: Create inline comments for each issue
mcp_calls:
  - github_add_comment(repo, pr_number, file, line, comment)
comment_format: |
  **[{dimension}]** {severity}: {message}
  
  Suggestion: {suggestion}
  
  Reference: {kc_or_pattern}
```

### Step 5: Submit Review (30s)

```yaml
action: Submit overall review
mcp_calls:
  - github_create_review(repo, pr_number, event, body)
decision_matrix:
  overall >= 8.0: APPROVE
  overall >= 6.0: COMMENT (suggestions, no blocking)
  overall >= 4.0: REQUEST_CHANGES (specific fixes required)
  overall < 4.0: REQUEST_CHANGES (major redesign needed)
body: |
  ## Code Review — {overall}/10
  
  | Dimension | Score |
  |-----------|-------|
  | Correctness | {scores.correctness}/10 |
  | Security | {scores.security}/10 |
  | ... | ... |
  
  ### Issues Found: {issue_count}
  ### Summary: {decision_reason}
```

## Total Time: ~8min per PR
