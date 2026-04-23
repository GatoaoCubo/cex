---
id: p01_kc_code_review
kind: knowledge_card
pillar: P01
title: "Code Review — GitHub MCP + Review Rubric"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.2
tags: [code-review, github, pull-request, rubric, quality]
tldr: "Structured code review via GitHub MCP: PR size checks, 7-dimension rubric (correctness, security, performance, readability, tests, docs, architecture), review checklist, automated PR validation."
density_score: 0.88
related:
  - p12_wf_code_review
  - p03_ins_code_review
  - p02_agent_code_review
  - bld_sp_quality_gate_software_project
  - p03_sp_code_review
  - p07_sr_engineering_quality
  - p12_wf_auto_review
  - p04_qg_sdk_example
  - p12_wf_auto_security
  - bld_output_template_contributor_guide
---

# Code Review

## GitHub MCP Tools

N03 uses `@anthropic/mcp-server-github` for PR review.

### Available Operations

```
github_get_pull_request       # Get PR details
github_list_pull_requests     # List open PRs
github_get_pull_request_diff  # Get diff
github_create_review          # Submit review
github_add_comment            # Comment on PR
github_list_commits           # PR commit history
```

### Review Workflow

```
1. github_list_pull_requests → find open PRs
2. github_get_pull_request_diff → read changes
3. Apply 7D rubric (below)
4. github_create_review → APPROVE / REQUEST_CHANGES / COMMENT
5. github_add_comment → inline comments on specific lines
```

## 7-Dimension Review Rubric

| Dimension | Weight | Checks |
|-----------|--------|--------|
| **Correctness** | 25% | Logic correct? Edge cases? Null handling? |
| **Security** | 20% | SQL injection? XSS? Secrets exposed? Auth bypassed? |
| **Performance** | 15% | N+1 queries? Unbounded loops? Memory leaks? |
| **Readability** | 15% | Clear naming? Small functions? Comments where needed? |
| **Tests** | 10% | New code has tests? Edge cases covered? Mocks appropriate? |
| **Documentation** | 10% | Docstrings? README updated? API docs? |
| **Architecture** | 5% | Right layer? No circular deps? Follows existing patterns? |

### Scoring

```
9-10: Exemplary — merge immediately
7-8:  Good — minor suggestions, approve
5-6:  Needs work — request specific changes
3-4:  Major issues — requires redesign discussion
1-2:  Reject — security vuln or fundamental flaw
```

## PR Size Check

```python
# Automated in CI (pr-validation.yaml)
CHANGES = git diff --shortstat | total_lines
if CHANGES > 1000:
    warn("Large PR — consider splitting")
```

| Size | Lines | Action |
|------|-------|--------|
| Small | <100 | Auto-approve eligible |
| Medium | 100-500 | Standard review |
| Large | 500-1000 | Request split if possible |
| XL | >1000 | Must split or justify |

## Review Checklist

### Before Reviewing

```
[ ] Read PR description and linked issue
[ ] Check PR size (prefer <500 lines)
[ ] Check if CI passed
[ ] Check if tests included
```

### During Review

```
[ ] Correctness: Does it do what it claims?
[ ] Security: Any input validation missing? Secrets exposed?
[ ] Performance: Any N+1 queries? Unbounded operations?
[ ] Tests: New tests for new code? Edge cases?
[ ] Naming: Variables/functions clearly named?
[ ] Error handling: Failures handled gracefully?
[ ] Breaking changes: API contract preserved?
```

### After Review

```
[ ] Summary comment with overall assessment
[ ] Specific inline comments on issues
[ ] Clear APPROVE / REQUEST_CHANGES decision
[ ] If REQUEST_CHANGES: actionable suggestions (not just "fix this")
```

## Review Comment Patterns

### Good

```
# Specific, actionable, explains WHY
"This query runs inside a loop (N+1). Consider using a single query
with `WHERE id IN (...)` to fetch all records at once. This will
reduce DB round-trips from N to 1."
```

### Bad

```
# Vague, not actionable
"This doesn't look right."
"Fix this."
"I wouldn't do it this way."
```

## Automated Review (CI)

PR validation workflow runs 5 checks automatically:

1. **Lint**: `ruff check` + `ruff format --check`
2. **Tests**: `pytest -m "not slow"` (fast tests only)
3. **Docker**: Build test (no push)
4. **PR size**: Warn if >1000 lines
5. **Dependencies**: `pip-audit` vulnerability scan

## Anti-Patterns

- ❌ Reviewing >1000-line PRs (too much to reason about)
- ❌ Nitpicking style when linter exists (Ruff handles it)
- ❌ Blocking on preferences vs requirements
- ❌ No inline comments (just "LGTM" or "needs changes")
- ❌ Reviewing without running the code

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_code_review]] | downstream | 0.44 |
| [[p03_ins_code_review]] | downstream | 0.37 |
| [[p02_agent_code_review]] | downstream | 0.28 |
| [[bld_sp_quality_gate_software_project]] | downstream | 0.24 |
| [[p03_sp_code_review]] | downstream | 0.24 |
| [[p07_sr_engineering_quality]] | downstream | 0.22 |
| [[p12_wf_auto_review]] | downstream | 0.21 |
| [[p04_qg_sdk_example]] | downstream | 0.20 |
| [[p12_wf_auto_security]] | downstream | 0.19 |
| [[bld_output_template_contributor_guide]] | downstream | 0.19 |
