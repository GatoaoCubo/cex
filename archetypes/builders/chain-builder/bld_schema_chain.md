---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for chain
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: chain

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p03_ch_{pipeline_slug}) | YES | - | Namespace compliance |
| kind | literal "chain" | YES | - | Type integrity |
| pillar | literal "P03" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| title | string | YES | - | Human-readable chain name |
| steps_count | integer | YES | - | Number of steps in body (must match) |
| flow | enum: sequential, branching, parallel, mixed | YES | "sequential" | Step arrangement |
| input_format | string | YES | - | What the first step receives |
| output_format | string | YES | - | What the last step produces |
| context_passing | enum: full, filtered, summary | REC | "full" | Inter-step context strategy |
| error_strategy | enum: fail_fast, skip, retry, fallback | REC | "fail_fast" | Chain-level error handling |
| domain | string | YES | - | Domain this chain belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "chain" |
| tldr | string <= 160ch | YES | - | Dense summary |
| density_score | float 0.80-1.00 | REC | - | Content density |

## ID Pattern
Regex: `^p03_ch_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Purpose` — why this chain exists, what transformation it performs
2. `## Steps` — numbered steps, each with Input/Prompt/Output subsections
3. `## Data Flow` — ASCII diagram showing step connections + context strategy
4. `## Error Handling` — strategy, failure behavior, retry policy

## Constraints
- max_bytes: 6144 (body only)
- naming: p03_ch_{pipeline_slug}.md
- machine_format: yaml (frontmatter) + markdown (body)
- id == filename stem
- steps_count MUST match actual count of numbered steps in body
- Each step MUST define Input, Prompt, and Output
- Steps are TEXT transformations only — no agent spawns or tool calls
- quality: null always
