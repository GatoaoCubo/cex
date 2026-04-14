---
kind: schema
id: bld_schema_changelog
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for changelog
quality: null
title: "Schema Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for changelog"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field     | Type             | Required | Default | Notes                              |  
|-----------|------------------|----------|---------|------------------------------------|  
| id        | string           | yes      |         | Must match ID Pattern              |  
| kind      | string           | yes      |         | Always "changelog"                 |  
| pillar    | string           | yes      |         | P01                                |  
| title     | string           | yes      |         | Human-readable name                |  
| version   | string           | yes      |         | Semantic version (e.g., v1.2.3)    |  
| created   | datetime         | yes      |         | ISO 8601                           |  
| updated   | datetime         | yes      |         | ISO 8601                           |  
| author    | string           | yes      |         | Maintainer username                |  
| domain    | string           | yes      |         | CEX-specific context               |  
| quality   | null             | yes      | null    | Never self-score; peer review assigns |  
| tags      | list<string>     | yes      |         | Keywords (e.g., "security", "feature") |  
| tldr      | string           | yes      |         | Summary of changes (≤200 chars)    |  
| changes   | list<string>     | yes      |         | List of updates/fixes              |  
| impact    | string           | yes      |         | User-facing effect (e.g., "minor") |  

### Recommended  
| Field           | Type             | Notes                          |  
|------------------|------------------|--------------------------------|  
| related_issues   | list<string>     | Linked issue IDs (e.g., "CEX-123") |  
| reviewers        | list<string>     | Peer reviewers                 |  
| deprecated       | boolean          | Whether prior versions are deprecated |  

## ID Pattern  
^p01_ch_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview** – Summary of the changelog’s scope.  
2. **Changes** – Detailed list of updates, features, or fixes.  
3. **Impact** – Analysis of user or system implications.  
4. **Deprecations** – Removed features or APIs.  
5. **Reviewers** – Names and roles of peer reviewers.  

## Constraints  
- All required fields must be present and valid.  
- ID must match exact regex pattern.  
- Version must follow semantic versioning.  
- Quality must be assigned by peer review, not self-assigned.  
- TLDR must be ≤200 characters and ASCII-only.  
- Body sections must be ordered and non-empty.
