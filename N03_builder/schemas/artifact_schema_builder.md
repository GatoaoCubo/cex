---
id: p06_schema_builder_artifact
kind: schema
pillar: P06
title: "Artifact Schema — Universal Frontmatter Contract"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 9.1
tags: [schema, builder, N03, frontmatter, validation, contract]
tldr: "Universal frontmatter schema that every CEX artifact must satisfy — 11 required fields + kind-specific extensions."
density_score: 0.95
linked_artifacts:
  primary: "N03_builder/quality/quality_gate_builder.md"
  related:
    - N03_builder/agents/agent_builder.md
    - .cex/kinds_meta.json
---

# Artifact Schema — Universal Frontmatter Contract

## Purpose

Every CEX artifact must include valid YAML frontmatter. This schema defines
the universal required fields and the extension mechanism for kind-specific fields.
The builder validates every artifact against this contract at F7 GOVERN.

## Universal Required Fields

```yaml
id: string          # Unique identifier: {pillar}_{shortname}
kind: string        # One of 123 registered kinds
pillar: string      # P01-P12
title: string       # Human-readable title
version: string     # SemVer (e.g., "2.0.0")
created: date       # ISO date (YYYY-MM-DD)
updated: date       # ISO date (YYYY-MM-DD)
author: string      # "builder_agent" for N03 output
quality: null       # ALWAYS null — peer review scores
tags: list          # Keyword tags (3-10 items)
tldr: string        # One-line summary (< 160 chars)
```

## Common Optional Fields

```yaml
domain: string           # Domain scope (e.g., construction, orchestration)
density_score: float     # 0.0-1.0 information density
linked_artifacts:        # Cross-references
  primary: string        # Main related artifact
  related: list          # Secondary references
data_source: string      # Where data came from
```

## Kind-Specific Extensions

### agent (P02)
```yaml
agent_group: string
capabilities_count: integer
tools_count: integer
routing_keywords: list
llm_function: string     # BECOME, REASON, CALL, etc.
```

### system_prompt (P03)
```yaml
target_agent: string
persona: string
rules_count: integer
tone: string
knowledge_boundary: string
safety_level: string
tools_listed: boolean
output_format_type: string
```

### knowledge_card (P01)
```yaml
when_to_use: string
keywords: list
long_tails: list
axioms: list
```

### workflow (P12)
```yaml
steps_count: integer
execution: string        # sequential, parallel, mixed
agent_groups: list
timeout: integer
retry_policy: string
depends_on: list
signals: list
```

### dispatch_rule (P12)
```yaml
scope: string
keywords: list
agent_group: string
model: string
priority: integer
confidence_threshold: float
fallback: string
routing_strategy: string
conditions:
  quality_min: float
  signal_required: boolean
```

### quality_gate (P07)
```yaml
gate_count: integer
pass_threshold: float
reject_action: string
```

## Validation Rules

1. `id` must be unique across the entire repository
2. `kind` must exist in `.cex/kinds_meta.json`
3. `pillar` must match the kind's registered pillar
4. `quality` must be exactly `null` — never a number or string
5. `tags` must contain 3-10 items, no duplicates
6. `tldr` must be under 160 characters
7. `version` must follow SemVer format
8. `created` and `updated` must be valid ISO dates

## Anti-Patterns

- Setting `quality: 9.0` (builder self-scoring — forbidden)
- Omitting `tldr` (every artifact needs a one-liner)
- Using `pillar: knowledge` instead of `pillar: P01` (use codes)
- Duplicating `id` across artifacts (must be globally unique)
- Empty `tags: []` (minimum 3 tags required)

## Boundary

This artifact IS a universal frontmatter contract that defines structural requirements for all CEX artifacts. It IS NOT a specific kind's schema, nor is it a validation tool itself — it serves as the foundational contract that other schemas must extend.

## Related Kinds

- **quality_gate**: Defines validation thresholds that must align with this schema's `quality` field.
- **agent**: Extends the universal schema with agent-specific fields like `agent_group` and `capabilities_count`.
- **system_prompt**: Adds fields related to `target_agent` and `persona` for role-specific configurations.
- **knowledge_card**: Includes `when_to_use` and `keywords` to define contextual relevance.
- **workflow**: Specifies `steps_count` and `execution` type to model process logic.

## Comparison of Kind-Specific Extensions

| Kind         | Pillar | Required Fields                     | Example Values                                                                 |
|--------------|--------|-------------------------------------|----------------------------------------------------------------------------------|
| agent        | P02    | agent_group, capabilities_count     | "ops_team", 5                                                                  |
| system_prompt| P03    | target_agent, persona               | "analyst_agent", "data_scientist"                                              |
| knowledge_card| P01  | when_to_use, keywords               | "data analysis", ["statistics", "machine learning"]                            |
| workflow     | P12    | steps_count, execution              | 7, "sequential"                                                                |
| dispatch_rule| P12    | scope, keywords, agent_group        | "customer_support", ["help", "support"], "support_team"                       |