---
id: "p08_cmap_{{SCOPE_SLUG}}"
kind: component_map
pillar: P08
version: 1.0.0
title: Template - Component Map
tags: [template, component, map, architecture, deps]
tldr: Visual map of system components, technologies, responsibilities, and data flow between them.
quality: null
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
- [ ] Every component has tech + responsibility
- [ ] Data flow shows direction
- [ ] Dependencies include protocol
- [ ] Criticality assessed
