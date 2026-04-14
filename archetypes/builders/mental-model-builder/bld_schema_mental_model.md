---
kind: schema
id: bld_schema_mental_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for mental_model (P02)
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Mental Model"
version: "1.0.0"
author: n03_builder
tags: [mental_model, builder, examples]
tldr: "Golden and anti-examples for mental model construction, demonstrating ideal structure and common pitfalls."
domain: "mental model construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Schema: mental_model

This ISO operationalizes a mental model -- a compact analogy or abstraction that guides reasoning.
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p02_mm_{agent_slug}) | YES | - | Namespace compliance |
| kind | literal "mental_model" | YES | - | Type integrity |
| pillar | literal "P02" | YES | - | Pillar assignment — NOT P10 |
| version | semver string | YES | "1.0.0" | Semantic versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| agent | string | YES | - | Target agent this model belongs to |
| routing_rules | object | YES | - | Keyword-to-action mappings |
| decision_tree | object | YES | - | If-then branching logic |
| domain | string | YES | - | Agent primary domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "mental-model" |
| tldr | string <= 160ch | YES | - | Dense one-liner |
| priorities | list[string] | REC | - | Ordered priority list (highest first) |
| heuristics | list[string] | REC | - | Rules of thumb for edge cases |
| domain_map | object | REC | - | Scope of knowledge domains with boundaries |
| tools_available | list[string] | REC | - | Tools this agent can invoke |
| personality | object | REC | - | Behavioral traits (tone, verbosity, risk) |
| constraints | list[string] | REC | - | Hard limits on behavior |
| fallback | object | REC | - | What to do when routing fails |
| llm_function | literal "BECOME" | REC | "BECOME" | Identity artifact |
| density_score | float 0.80-1.00 | OPT | - | Content density |
## Routing Rules Object
```yaml
routing_rules:
  - keywords: [list, of, trigger, words]
    action: "what to do"
    confidence: float  # 0.0-1.0 threshold
  - keywords: [...]
    action: "..."
```
## Decision Tree Object
```yaml
decision_tree:
  - condition: "if X"
    then: "action A"
    else: "action B"
  - condition: "if Y"
    then: "action C"
```
## ID Pattern
Regex: `^p02_mm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Agent Reference` — which agent, one-line identity
2. `## Routing Rules` — table of keyword-to-action mappings with confidence
3. `## Decision Tree` — if-then branching logic as structured list
4. `## Priorities` — ordered priority list (highest first)
5. `## Heuristics` — rules of thumb for ambiguous cases
6. `## Domain Map` — scope boundaries (what agent covers vs routes away)
## Constraints
- max_bytes: 2048 (body only)
- naming: p02_mm_{agent_slug}.yaml
- machine_format: yaml
- id == filename stem
- quality: null always
- pillar: P02 (NOT P10 — P02 is design-time, P10 is runtime)
- routing_rules: minimum 3 rules
- decision_tree: minimum 2 conditions
- llm_function: BECOME (identity artifact)
