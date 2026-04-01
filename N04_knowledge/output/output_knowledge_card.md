---
id: p10_out_knowledge_card
kind: output
pillar: P10
title: "Output: Knowledge Card"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 8.7
tags: [output, n04, kc, template, standard]
tldr: "Standard KC output template matching kc_structure_contract schema."
density_score: 0.92
---

# Output: Knowledge Card

## Template
```markdown
---
id: p01_kc_{{slug}}
kind: knowledge_card
type: {{kind|domain|platform|infrastructure}}
pillar: P01
title: "{{Title}}"
version: 1.0.0
created: {{DATE}}
author: {{AUTHOR}}
domain: {{DOMAIN}}
quality: 8.7
tags: [{{tag1}}, {{tag2}}, {{tag3}}]
tldr: "{{20-200 chars}}"
when_to_use: "{{context}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
density_score: {{0.85-1.0}}
---

# {{Title}}

## Core Concept
{{1-3 paragraphs, no filler}}

## Key Data
| {{Column}} | {{Column}} | {{Column}} |
|---|---|---|
| {{data}} | {{data}} | {{data}} |

## When to Use / When NOT
- Use: {{conditions}}
- Don't use: {{conditions}}

## Anti-Patterns
- {{common mistake and why}}

## CEX Integration
- {{how this KC connects to the system}}
```
