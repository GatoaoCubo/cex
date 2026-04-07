---
id: "p08_cmap_{{SCOPE_SLUG}}"
kind: component_map
pillar: P08
version: 1.0.0
title: Template - Component Map
tags: [template, component, map, architecture, deps]
tldr: Visual map of system components, technologies, responsibilities, and data flow between them.
quality: 9.0
updated: "2026-04-07"
domain: "system architecture"
author: n03_builder
created: "2026-04-07"
density_score: 1.0
---

# Component Map: [NAME]

## Purpose
[WHAT this component_map does]
## Components
| Component | Technology | Responsibility |
|-----------|-----------|---------------|
| [COMP_1] | [TECH] | [WHAT_IT_DOES] |
| [COMP_2] | [TECH] | [WHAT_IT_DOES] |
| [COMP_3] | [TECH] | [WHAT_IT_DOES] |
## Diagram
```
[COMP_1] --HTTP--> [COMP_2] --SQL--> [COMP_3]
    ^                   |
    +-----Signal--------+
```
## Dependencies
| From | To | Protocol | Critical |
|------|------|----------|---------|
| API | Database | SQL/TCP | Yes |
| API | Cache | Redis | No |
| Worker | Queue | AMQP | Yes |
## Quality Gate
1. [ ] Every component has tech + responsibility
2. [ ] Data flow shows direction
3. [ ] Dependencies include protocol
4. [ ] Criticality assessed

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
