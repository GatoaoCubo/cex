---
kind: schema
id: bld_schema_github_issue_template
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for github_issue_template
quality: 9.1
title: "Schema Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for github_issue_template"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes                              |
|------------|--------|----------|---------|------------------------------------|
| id         | string | yes      | null    | Must match ID Pattern              |
| kind       | string | yes      | null    | Always "github_issue_template"     |
| pillar     | string | yes      | null    | Always "P05"                       |
| title      | string | yes      | null    | Descriptive title                  |
| version    | string | yes      | "1.0"   | Template version                   |
| created    | date   | yes      | null    | ISO 8601 date                      |
| updated    | date   | yes      | null    | ISO 8601 date                      |
| author     | string | yes      | null    | Creator’s GitHub username          |
| domain     | string | yes      | null    | Repository or project name         |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | list   | yes      | []      | Keywords for categorization        |
| tldr       | string | yes      | null    | One-sentence summary               |
| template_type | string | yes | null | "bug_report", "feature_request", etc. |
| labels     | list   | yes      | []      | GitHub labels                      |

### Recommended
| Field         | Type   | Notes                          |
|---------------|--------|--------------------------------|
| assignees     | list   | Default assignees              |
| issue_category| string | "enhancement", "bug", "discussion" |

## ID Pattern
^p05_git_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Template Type and Purpose**
   Define the issue category (e.g., bug report, feature request).

2. **Labels and Assignees**
   Specify default GitHub labels and assignees for triage.

3. **Issue Category and Priority**
   Categorize the issue and assign priority (high/medium/low).

4. **Related Issues and Dependencies**
   Link to related issues or dependencies (e.g., blocked_by, related_issues).

5. **TLDR Summary**
   Concise one-sentence summary of the issue.

## Constraints
- ID must match ^p05_git_[a-z][a-z0-9_]+.md$ exactly.
- All required fields must be present and valid.
- File size must not exceed 3072 bytes.
- Domain-specific fields (template_type, labels) are mandatory.
- Quality field must be peer-reviewed; no self-scoring.
