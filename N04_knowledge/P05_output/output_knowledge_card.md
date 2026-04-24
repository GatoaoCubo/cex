---
id: p10_out_knowledge_card
kind: output
8f: F6_produce
pillar: P10
title: "Output: Knowledge Card"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [output, n04, kc, template, standard]
tldr: "Standard KC output template matching kc_structure_contract schema."
density_score: 0.92
related:
  - p06_schema_kc_structure
  - p06_is_knowledge_data_model
  - bld_examples_response_format
  - bld_output_template_knowledge_card
  - p01_kc_pattern_extraction
  - bld_memory_runtime_state
  - bld_output_template_kind
  - bld_knowledge_card_knowledge_card
  - bld_output_template_context_doc
  - p03_sp_knowledge_card_builder
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

## Template Population Guide

| Field | Rules | Examples |
|-------|-------|----------|
| `type` | kind\|domain\|platform\|infrastructure | `react`, `authentication`, `aws`, `database` |
| `domain` | Business area, lowercase | `web-development`, `data-science`, `devops` |
| `tldr` | 20-200 chars, actionable | `React hooks for state management` |
| `when_to_use` | Specific context triggers | `Complex state logic beyond useState` |
| `keywords` | 3-5 searchable terms | `[react, hooks, state, useReducer]` |
| Core Concept | 1-3 paragraphs max | Focus on what/why, not how-to |
| Key Data | Always use tables | Commands, APIs, configs, metrics |
| Anti-Patterns | Common mistakes + why wrong | `Don't useEffect for derived state` |
| CEX Integration | Link to other artifacts | `See agent_react_helper.md` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_kc_structure]] | upstream | 0.26 |
| [[p06_is_knowledge_data_model]] | upstream | 0.22 |
| [[bld_examples_response_format]] | upstream | 0.21 |
| [[bld_output_template_knowledge_card]] | upstream | 0.19 |
| [[p01_kc_pattern_extraction]] | upstream | 0.17 |
| [[bld_memory_runtime_state]] | related | 0.16 |
| [[bld_output_template_kind]] | upstream | 0.16 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.16 |
| [[bld_output_template_context_doc]] | upstream | 0.16 |
| [[p03_sp_knowledge_card_builder]] | upstream | 0.15 |
