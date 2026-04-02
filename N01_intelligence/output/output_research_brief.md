---
id: p10_out_research_brief
kind: output
pillar: P10
title: "Output: Research Brief"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.6
tags: [output, n01, research, brief, request]
tldr: "Research request document — what to research, at what depth, for whom."
density_score: 0.91
---

# Output: Research Brief

## Template
```markdown
# Research Brief: {{TOPIC}}
**Requested by**: {{NUCLEUS}} | **Date**: {{DATE}} | **Depth**: {{L1|L2|L3}}

## Question
{{RESEARCH_QUESTION}}

## Scope
- Geography: {{SCOPE_GEO}}
- Timeframe: {{SCOPE_TIME}}
- Competitors: {{COMPETITORS_LIST}}

## Constraints
- Sources preferred: {{SOURCE_TYPES}}
- Sources excluded: {{EXCLUDED}}
- Max sources: {{MAX_SOURCES}}
- Deadline: {{DEADLINE}}

## Brand Context
- Company: {{BRAND_NAME}}
- Market: {{BRAND_CATEGORY}}
- ICP: {{BRAND_ICP}}

## Expected Output
- Format: {{OUTPUT_TEMPLATE}}
- Language: {{LANGUAGE}}
```

## Usage Guidelines

| When to Use | When NOT to Use |
|-------------|-----------------|
| Multi-source research needed | Single Google search sufficient |
| Competitor intelligence required | Internal data analysis only |
| Market trend analysis | Quick fact checking |
| Strategic planning inputs | Routine operational questions |

## Example Requests

**Good**: "Analyze SaaS pricing models in fintech (2022-2026) for Series A companies targeting SMBs"
**Bad**: "Find the CEO of Stripe" (too simple, use Google)

## Anti-Patterns
- Vague questions: "Research competitors" → Specify which aspects, geography, timeframe
- Impossible scope: "All AI companies worldwide" → Define market segment
- No constraints: Missing deadlines, source preferences, or output format