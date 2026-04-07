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
