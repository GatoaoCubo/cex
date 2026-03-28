---
kind: config
id: bld_config_session_state
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, limits, and operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: session_state Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact file | `p10_ss_{session}.yaml` | `p10_ss_edison_wave19_build.yaml` |
| Builder directory | kebab-case | `session-state-builder/` |
| Frontmatter fields | snake_case | `session_id`, `started_at` |
| Status values | lowercase enum | `active`, `paused`, `completed`, `aborted` |
| Agent values | lowercase slug | `edison`, `atlas`, `codex` |

Rule: use `.yaml` extension only for this builder.

## File Paths
- Output: `cex/P10_memory/compiled/p10_ss_{session}.yaml`
- Human reference: `cex/P10_memory/examples/p10_ss_{session}.md`

## Size Limits
- Preferred snapshot size: <= 2048 bytes
- Absolute max: 3072 bytes
- Optional fields should remain sparse and compact

## Payload Restrictions
- Required fields must appear exactly as defined in SCHEMA.md
- Omit optional null/unknown fields instead of writing placeholders
- `ended_at` and `duration_seconds` only meaningful for completed/aborted sessions
- `checkpoints` should be concise: label + timestamp only
- `errors` entries must have both `code` and `message`

## Boundary Restrictions
- No persistent state: routing decisions, accumulated scores belong in runtime_state
- No learning patterns: accumulated outcomes belong in learning_record
- No search configuration: index settings belong in brain_index
- No immutable rules: fundamental axioms belong in axiom
