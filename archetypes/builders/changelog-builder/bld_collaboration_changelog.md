---
kind: collaboration
id: bld_collaboration_changelog
pillar: P12
llm_function: COLLABORATE
purpose: How changelog-builder works in crews with other builders
quality: 8.9
title: "Collaboration Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, collaboration]
tldr: "How changelog-builder works in crews with other builders"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Automates generation of structured changelogs by aggregating atomic changes from version-controlled repositories and CI/CD pipelines.  

## Receives From  
| Builder       | What              | Format              |  
|---------------|-------------------|---------------------|  
| Version Control System | Commit messages   | Git commit log format |  
| CI/CD Pipeline  | Deployment events | JSON payload        |  
| Issue Tracker   | Issue resolutions | Jira API format     |  

## Produces For  
| Builder       | What              | Format              |  
|---------------|-------------------|---------------------|  
| Release Management Tool | Change summary  | YAML format         |  
| Documentation System    | Versioned history | HTML format         |  
| Artifact Repository     | Changelog file    | Markdown format     |  

## Boundary  
Does NOT write prose or rationale (handled by release_notes/decision_record). Does NOT resolve merge conflicts (handled by Release Manager).
