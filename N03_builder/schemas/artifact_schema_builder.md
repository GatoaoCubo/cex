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

## Comparison of Kind-Specific Fields

| Kind          | Pillar | Required Fields                         | Example Use Case                          |
|---------------|--------|-----------------------------------------|-------------------------------------------|
| agent         | P02    | agent_group, capabilities_count         | Define agent capabilities for P02 tasks   |
| system_prompt | P03    | target_agent, persona, rules_count      | Configure agent behavior for P03 prompts  |
| knowledge_card| P01    | when_to_use, keywords, axioms           | Create knowledge cards for P01 queries    |
| workflow      | P12    | steps_count, execution, agent_groups    | Orchestrate P12 workflows with agents     |
| quality_gate  | P07    | gate_count, pass_threshold              | Implement P07 quality checks for artifacts|

## Validation Rules

1. `id` must be unique across the entire repository
2. `kind` must exist in `.cex/kinds_meta.json`
3. `pillar` must match the kind's registered pillar
4. `quality` must be exactly `null` — never a number or string
5. `tags` must contain 3-10 items, no duplicates
6. `tldr` must be under 160 characters
7. `version` must follow SemVer format
8. `created` and `updated` must be valid ISO dates

## Boundary

This artifact defines the universal frontmatter contract for all CEX artifacts. It is NOT a data format itself, nor does it govern the content beyond YAML frontmatter. It establishes structural requirements but does not enforce semantic meaning of fields.

## Related Kinds

- **quality_gate**: Enforces schema validation rules through automated checks
- **agent**: Uses schema fields to define capabilities and routing parameters
- **kinds_meta**: Maintains registry of valid `kind` values referenced by this schema
- **workflow**: Relies on schema for agent_group and execution parameters
- **dispatch_rule**: Uses schema-defined `kind` and `pillar` for routing decisions

## Anti-Patterns

- Setting `quality: 9.0` (builder self-scoring — forbidden)
- Omitting `tldr` (every artifact needs a one-liner)
- Using `pillar: knowledge` instead of `pillar: P01` (use codes)
- Duplicating `id` across artifacts (must be globally unique)
- Empty `tags: []` (minimum 3 tags required)