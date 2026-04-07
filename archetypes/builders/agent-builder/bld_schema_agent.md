---
kind: schema
id: bld_schema_agent
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for agent
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Agent"
version: "1.0.0"
author: n03_builder
tags: [agent, builder, examples]
tldr: "Golden and anti-examples for agent construction, demonstrating ideal structure and common pitfalls."
domain: "agent construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: agent
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_agent_{slug}) | YES | - | Namespace compliance |
| kind | literal "agent" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment |
| title | string | YES | - | Human-readable agent name |
| version | semver string | YES | "1.0.0" | Versionamento |
| agent_group | string | YES | - | Owning agent_group or "agnostic" |
| domain | string | YES | - | Primary domain of expertise |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "agent" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| created | date YYYY-MM-DD | REC | - | Creation date |
| updated | date YYYY-MM-DD | REC | - | Last update |
| author | string | REC | - | Producer identity |
| llm_function | literal "BECOME" | REC | "BECOME" | Always BECOME for agents |
| capabilities_count | integer | REC | - | Number of capability bullets |
| tools_count | integer | REC | - | Number of tools listed |
| iso_files_count | integer | REC | - | builder specs in vectorstore |
| routing_keywords | list[string] | REC | - | Brain search triggers |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## ID Pattern
Regex: `^p02_agent_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — one paragraph: who, domain, primary function
2. `## Architecture` — capabilities list, tools, agent_group position
3. `## File Structure` — agent_package listing with all builder specs
4. `## When to Use` — triggers and routing keywords
5. `## Input / Output` — what the agent receives and produces
6. `## Integration` — how agent connects to agent_groups, routers, chains
7. `## Quality Gates` — HARD + SOFT gate references
8. `## Common Issues` — 3-5 known failure modes with remediation
9. `## Invocation` — how to spawn or invoke this agent
10. `## Related Agents` — sibling agents, upstream, downstream
11. `## Footer` — version, author, quality: null
## Constraints
- max_bytes: 5120 (body only)
- naming: p02_agent_{slug}.md + p02_agent_{slug}.yaml
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- quality: null always
- agent_package min 10 files required
- capabilities_count MUST match actual bullets in Architecture section
- llm_function: BECOME (never REASON, CALL, or PRODUCE)
- agent_group: required — no "unassigned" agents
