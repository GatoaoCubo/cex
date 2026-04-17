---
id: p10_entity_memory
kind: entity_memory
pillar: P10
version: 1.0.0
title: "Template — Entity Memory"
tags: [template, entity, memory, knowledge-graph, persistence]
tldr: "Tracks named entities (people, products, companies) across conversations. Stores attributes, relationships, and confidence scores for context injection."
quality: 9.1
updated: "2026-04-07"
domain: "memory and state"
author: n03_builder
created: "2026-04-07"
density_score: 0.98
---

# Entity Memory: [ENTITY_STORE_NAME]

## Purpose
[WHAT entities are tracked — customers, products, team members, competitors]

## Entity Schema
```yaml
entity:
  id: "[UUID]"
  name: "[Entity Name]"
  type: [person | company | product | concept | location]
  attributes:
    - key: "[ATTR_NAME]"
      value: "[ATTR_VALUE]"
      confidence: [0.0-1.0]
      source: "[WHERE_LEARNED]"
      updated: "[ISO8601]"
  relationships:
    - target: "[OTHER_ENTITY_ID]"
      relation: [works_at | owns | competes_with | part_of]
      confidence: [0.0-1.0]
```

## Storage

| Backend | Use Case | Capacity |
|---------|----------|----------|
| In-memory dict | Development, tests | ~1000 entities |
| SQLite | Single-user, local | ~100K entities |
| Supabase/Postgres | Multi-user, production | Unlimited |

## Operations

| Operation | Trigger | Example |
|-----------|---------|---------|
| Create | New entity mentioned | "João works at ACME" → create person + company |
| Update | New info about entity | "João is now CTO" → update role attribute |
| Merge | Duplicate detected | "João Silva" = "J. Silva" → merge entries |
| Decay | No mention for 90 days | Lower confidence by 0.1/month |

## Context Injection
```
## Known Entities
- João Silva (person, confidence: 0.95)
  - Role: CTO at ACME Corp
  - Last mentioned: 2026-03-15
- ACME Corp (company, confidence: 0.90)
  - Industry: SaaS
  - Employees: 50
```

## Quality Gate
- [ ] Entity types defined (not open-ended)
- [ ] Confidence scores tracked per attribute
- [ ] Merge/dedup strategy documented
- [ ] Decay policy prevents stale entities
