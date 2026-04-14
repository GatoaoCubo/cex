---
kind: collaboration
id: bld_collaboration_edit_format
pillar: P12
llm_function: COLLABORATE
purpose: How edit_format-builder works in crews with other builders
quality: null
title: "Collaboration Edit Format"
version: "1.0.0"
author: wave1_builder_gen
tags: [edit_format, builder, collaboration]
tldr: "How edit_format-builder works in crews with other builders"
domain: "edit_format construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Structures and standardizes edit operations for consistent application across systems.  

## Receives From  
| Builder     | What               | Format      |  
|-------------|--------------------|-------------|  
| Parser      | Raw user edits     | JSON        |  
| Validator   | Edit rules         | YAML        |  
| Merger      | Conflicting edits  | XML         |  

## Produces For  
| Builder     | What                  | Format      |  
|-------------|-----------------------|-------------|  
| Formatter   | Structured edits      | JSON        |  
| Merger      | Resolved edit conflicts | XML       |  
| Tracker     | Edit audit logs       | CSV         |  

## Boundary  
Does NOT handle diff algorithms (handled by diff_strategy) or output formatting (handled by formatter). Conflict resolution logic is managed by merger, not this builder.
