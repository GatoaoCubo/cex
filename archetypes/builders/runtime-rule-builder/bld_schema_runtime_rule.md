---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for runtime_rule
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: runtime_rule

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_rr_{rule_slug}) | YES | - | Namespace compliance |
| kind | literal "runtime_rule" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| rule_name | string | YES | - | Human-readable rule name |
| rule_type | enum: timeout, retry, rate_limit, circuit_breaker, concurrency | YES | - | Primary rule category |
| scope | string | YES | - | What component/operation this applies to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "runtime_rule" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this rule governs |
| fallback | string | REC | - | Behavior when rule triggers |
| severity | enum: critical, high, medium, low | REC | medium | Impact if rule is misconfigured |

## ID Pattern
Regex: `^p09_rr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Rule Specification` — concrete parameters: values with units, thresholds, limits
2. `## Trigger Behavior` — what happens when rule activates (timeout reached, retries exhausted, rate exceeded)
3. `## Tuning Guide` — how to adjust parameters, safe ranges, what metrics to watch

## Constraints
- max_bytes: 3072 (body only)
- naming: p09_rr_{rule_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- All numeric values MUST include units (ms, s, min, req/s, etc.)
- quality: null always
- NEVER use vague terms ("fast", "many") — always concrete numbers
