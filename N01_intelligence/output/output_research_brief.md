---
id: p10_out_research_brief
kind: output
pillar: P10
title: "Output: Research Brief"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.1
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

## Complete Example
```markdown
# Research Brief: SaaS Pricing Models in Fintech
**Requested by**: N02_marketing | **Date**: 2026-04-01 | **Depth**: L2

## Question
What pricing strategies do fintech SaaS companies use for SMB customers, and how do they compare to our current model?

## Scope
- Geography: North America, UK
- Timeframe: 2022-2026 data
- Competitors: Stripe, Plaid, Dwolla, Mercury, Ramp

## Constraints
- Sources preferred: Company websites, SEC filings, industry reports
- Sources excluded: Social media speculation
- Max sources: 20
- Deadline: 2026-04-03

## Brand Context
- Company: PayFlow Pro
- Market: B2B payment processing
- ICP: 10-500 employee companies

## Expected Output
- Format: 3-page summary with pricing comparison table
- Language: English
```

## Usage Guidelines

| When to Use | When NOT to Use |
|-------------|-----------------|
| Multi-source research needed | Single Google search sufficient |
| Competitor intelligence required | Internal data analysis only |
| Market trend analysis | Quick fact checking |
| Strategic planning inputs | Routine operational questions |

## Example Requests

| Category | Good Example | Bad Example | Why |
|----------|-------------|-------------|-----|
| **Competitor Analysis** | "Analyze SaaS pricing models in fintech (2022-2026) for Series A companies targeting SMBs" | "Research competitors" | Specific scope vs vague |
| **Market Research** | "US market size for AI coding tools, enterprise segment, with 3-year growth projections" | "How big is the AI market?" | Defined geography, segment, timeframe |
| **Trend Analysis** | "Remote work adoption rates by industry (2020-2026) focusing on retention metrics" | "Research remote work trends" | Specific metrics and timeline |
| **Quick Facts** | Use Google directly | "Find the CEO of Stripe" | Too simple for research brief |

## Anti-Patterns
- Vague questions: "Research competitors" → Specify which aspects, geography, timeframe
- Impossible scope: "All AI companies worldwide" → Define market segment
- No constraints: Missing deadlines, source preferences, or output format