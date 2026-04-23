---
kind: collaboration
id: bld_collaboration_github_issue_template
pillar: P12
llm_function: COLLABORATE
purpose: How github_issue_template-builder works in crews with other builders
quality: 8.7
title: "Collaboration Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, collaboration]
tldr: "How github_issue_template-builder works in crews with other builders"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - github-issue-template-builder
  - bld_collaboration_code_of_conduct
  - p03_sp_github_issue_template_builder
  - bld_collaboration_faq_entry
  - bld_collaboration_prompt_technique
  - bld_collaboration_contributor_guide
  - bld_collaboration_integration_guide
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_safety_policy
  - bld_collaboration_changelog
---

## Crew Role  
Creates standardized GitHub issue templates to guide users in reporting bugs, requesting features, or asking questions. Ensures consistency, clarity, and alignment with project workflows.  

## Receives From  
Builder | What | Format  
--- | --- | ---  
User | Issue reports | Markdown  
Product Team | Requirements | Document  
Community | Feedback | Comments  

## Produces For  
Builder | What | Format  
--- | --- | ---  
GitHub Repo | Issue templates | Markdown  
Contributors | Guidelines | Markdown  
Project Lead | Usage report | CSV  

## Boundary  
Does NOT handle pull request templates (handled by `pull_request_template-builder`) or FAQ entries (handled by `faq_entry-builder`). Excludes code changes, which are managed by developers.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[github-issue-template-builder]] | upstream | 0.42 |
| [[bld_collaboration_code_of_conduct]] | sibling | 0.33 |
| [[p03_sp_github_issue_template_builder]] | upstream | 0.32 |
| [[bld_collaboration_faq_entry]] | sibling | 0.29 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.29 |
| [[bld_collaboration_contributor_guide]] | sibling | 0.27 |
| [[bld_collaboration_integration_guide]] | sibling | 0.26 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.26 |
| [[bld_collaboration_safety_policy]] | sibling | 0.25 |
| [[bld_collaboration_changelog]] | sibling | 0.25 |
