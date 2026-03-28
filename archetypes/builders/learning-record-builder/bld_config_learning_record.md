---
kind: config
id: bld_config_learning_record
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: learning_record Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p10_lr_{topic_slug}.md` | `p10_lr_continuous_batching_speedup.md` |
| Builder directory | kebab-case | `learning-record-builder/` |
| Frontmatter fields | snake_case | `linked_artifacts`, `reproducibility` |
| Slug | lowercase + underscores | `continuous_batching_speedup` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P10_memory/examples/p10_lr_{slug}.md`
- Compiled: `cex/P10_memory/compiled/p10_lr_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total: ~4000 bytes (frontmatter + body)
- Density: >= 0.80

## Learning-Specific Constraints
- Outcome enum: strictly SUCCESS, PARTIAL, or FAILURE (no synonyms)
- Score range: 0.0-10.0 (float, never string, never null)
- Pattern concreteness: each step must be actionable ("use X with Y" not "be careful")
- Anti-pattern specificity: name the failure mode, not generic warning
- Timestamp precision: ISO 8601 with timezone when available
- Satellite attribution: tag originating satellite for routing intelligence
- Deduplication: brain_query before creating (same topic + same outcome = update, not new)
