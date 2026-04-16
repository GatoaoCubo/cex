---
kind: knowledge_card
id: bld_knowledge_card_github_issue_template
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for github_issue_template production
quality: 9.1
title: "Knowledge Card Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, knowledge_card]
tldr: "Domain knowledge for github_issue_template production"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
GitHub issue templates standardize bug reports, feature requests, and questions by enforcing structured input. They reduce noise, improve triage efficiency, and ensure reproducibility through required fields like title, steps to reproduce, and environment details. Industry adoption emphasizes alignment with project workflows, such as linking to documentation or using labels for prioritization. Templates also support community-driven projects by fostering consistency and reducing onboarding friction for contributors.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Required Fields | Mandatory inputs (e.g., "Steps to reproduce") to ensure completeness | GitHub Docs |
| Labels | Categorization tags (e.g., "bug," "enhancement") for filtering and prioritization | GitHub Docs |
| Issue Type | Classification (bug/feature/question) to route issues appropriately | GitHub Docs |
| Triage Labels | Metadata (e.g., "needs triage," "blocked") for workflow automation | Atlassian |
| Reproducibility | Steps to reproduce an issue, aligned with OSI's reproducibility standards | OSI |
| Environment Details | System-specific info (OS, browser) to diagnose issues | RFC 7841 |
| Code of Conduct | Reference to contributor guidelines (e.g., Contributor Covenant) | Contributor Covenant |
| Linking to Docs | Direct links to relevant documentation for self-service resolution | GitHub Docs |

## Industry Standards
- GitHub Issue Template Guidelines
- Contributor Covenant (Code of Conduct)
- GitFlow (Workflow Standards)
- RFC 7841 (Problem Details for HTTP APIs)
- OSDI 2018 (Reproducibility in Research)
- IEEE 830 (Software Requirements Specifications)
- DORA Metrics (DevOps Performance)
- SRE Book (Google's Site Reliability Engineering)
- PSR-12 (PHP Coding Standards)
- Markdown 1.0.1 (Syntax Specification)

## Common Patterns
1. Use required fields for critical data (e.g., "Title," "Steps to reproduce").
2. Apply labels for categorization and automation (e.g., "bug," "question").
3. Include issue type selection (bug/feature/question) for routing.
4. Reference triage labels (e.g., "needs triage") for team workflows.
5. Link to documentation for self-service resolution.

## Pitfalls
- Omitting required fields leads to incomplete reports.
- Inconsistent label usage across teams or projects.
- Failing to align templates with project-specific workflows.
- Overloading templates with unnecessary fields.
- Ignoring markdown syntax, causing formatting errors.
