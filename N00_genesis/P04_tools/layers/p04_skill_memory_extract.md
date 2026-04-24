---
id: p04_skill_memory_extract
kind: skill
8f: F5_call
pillar: P04
title: "Skill: Memory Extraction"
version: 1.0.0
quality: 9.0
tags: [skill, memory, extraction, learning, persistence]
tldr: "Memory extraction skill for identifying and persisting valuable information from conversation context into long-term memory files."
domain: "tools"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.90
related:
  - bld_collaboration_memory_type
  - bld_manifest_memory_type
  - p01_kc_memory_scope
  - SPEC_04_memory_system
  - bld_collaboration_memory_scope
  - bld_knowledge_card_memory_scope
  - bld_system_prompt_memory_type
  - bld_config_memory_type
  - bld_knowledge_card_memory_architecture
  - atom_22_memory_taxonomy
---

# Memory Extraction Procedures

## Trigger Conditions

Memory extraction runs periodically (every 5 tool executions) and at
conversation end. It scans recent context for persistable knowledge.

## What to Extract

### User Preferences (type: feedback)
- Corrections to approach: "don't do X, do Y instead"
- Confirmed approaches: "yes, that's exactly right"
- Style preferences: terse vs verbose, formal vs casual
- Tool preferences: preferred editors, frameworks, workflows

### Project Context (type: project)
- Ongoing initiatives and their status
- Deadlines and milestones (convert relative dates to absolute)
- Team members and their responsibilities
- Technical decisions and their rationale

### User Profile (type: user)
- Role and expertise level
- Domain knowledge areas
- Technologies they work with
- How they prefer to collaborate

### External References (type: reference)
- URLs to dashboards, docs, or tools mentioned
- External system locations (Linear, Slack, Grafana)
- API endpoints and service locations
- Documentation sources

## Extraction Protocol

1. Scan recent conversation turns for extractable information
2. Check existing memory files for duplicates
3. Categorize by memory type (user/feedback/project/reference)
4. Write memory file with frontmatter (name, description, type)
5. Update MEMORY.md index with one-line pointer

## Quality Rules

- Do not extract ephemeral task state (use tasks instead)
- Do not extract information derivable from code or git
- Always include WHY context for feedback and project memories
- Convert relative dates to absolute dates before saving

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.31 |
| [[bld_manifest_memory_type]] | upstream | 0.25 |
| [[p01_kc_memory_scope]] | upstream | 0.24 |
| [[SPEC_04_memory_system]] | upstream | 0.24 |
| [[bld_collaboration_memory_scope]] | downstream | 0.22 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.22 |
| [[bld_system_prompt_memory_type]] | upstream | 0.22 |
| [[bld_config_memory_type]] | downstream | 0.20 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.20 |
| [[atom_22_memory_taxonomy]] | related | 0.20 |
