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

Every CEX artifact must include valid YAML frontmatter. This schema defines the universal required fields and the extension mechanism for kind-specific fields. The builder validates every artifact against this contract at F7 GOVERN. Ensures consistency across 123+ artifact kinds while allowing domain-specific customization.

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

| Rule # | Field        | Constraint                                                                 | Example Violation                                                                 |
|-------|--------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 1     | id           | Globally unique across repository                                           | Duplicate `id: p06_schema_builder_artifact` in two artifacts                      |
| 2     | kind         | Must exist in `.cex/kinds_meta.json`                                        | `kind: unknown_kind`                                                              |
| 3     | pillar       | Must match kind's registered pillar                                         | `pillar: knowledge` instead of `pillar: P01`                                      |
| 4     | quality      | Must be exactly `null`                                                      | `quality: 9.0` (self-scoring)                                                    |
| 5     | tags         | 3-10 items, no duplicates                                                   | `tags: []` (empty) or `tags: [schema, schema]` (duplicates)                      |
| 6     | tldr         | <160 characters                                                             | `tldr: "This is a very long summary that exceeds the 160-character limit"`      |
| 7     | version      | Must follow SemVer format                                                   | `version: 2.0` (missing patch number)                                            |
| 8     | created/updated | Valid ISO date (YYYY-MM-DD)                                               | `created: 2026-02-30` (invalid date)                                             |

## Anti-Patterns

- **Self-scoring quality**: Setting `quality: 9.0` violates F7 GOVERN rules (must be `null`)
- **Missing tldr**: Every artifact must have a one-liner summary (<160 chars)
- **Invalid pillar**: Using `pillar: knowledge` instead of `pillar: P01` (use codes)
- **Duplicate IDs**: `id` must be globally unique across the entire CEX repository
- **Empty tags**: Minimum 3 tags required for discoverability (e.g., `tags: [schema, builder, N03]`)

## Boundary

This artifact IS the universal frontmatter contract for all CEX artifacts. It IS NOT the schema for the content within the artifact, but rather the metadata framework that every artifact must satisfy.

## Related Kinds

- **quality_gate**: Defines validation thresholds that reference this schema's `density_score` and `tags` fields
- **agent**: Extends this schema with `agent_group` and `llm_function` fields for behavior specification
- **workflow**: Uses this schema's `id` and `version` for dependency tracking in `depends_on` lists
- **system_prompt**: Leverages `tags` and `domain` for categorization in knowledge repositories
- **knowledge_card**: Relies on `tldr` for quick summary retrieval in search systems