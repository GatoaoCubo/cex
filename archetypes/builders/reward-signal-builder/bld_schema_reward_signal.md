---
kind: schema
id: bld_schema_reward_signal
pillar: P11
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for reward_signal
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: reward_signal
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_rs_{slug}) | YES | - | Namespace compliance |
| kind | literal "reward_signal" | YES | - | Type integrity |
| pillar | literal "P11" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable signal name |
| signal_type | enum: scalar, preference, critique, comparative, implicit | YES | - | Reward computation mechanism |
| scale | string | YES | - | e.g. "0-1", "0-10", "binary", "-1_to_1" |
| model | string | YES | - | Model producing reward, or "human" |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "reward_signal" |
| tldr | string <= 160ch | YES | - | Dense summary |
| criteria | list[string] | REC | - | Dimensions scored |
| frequency | enum: per_turn, per_task, per_session, on_demand | REC | - | Evaluation cadence |
| aggregation | enum: mean, weighted_mean, min, max, last | REC | - | How scores combine |
| baseline | float | REC | - | Minimum acceptable score |
| description | string <= 200ch | REC | - | What signal measures |
## ID Pattern
Regex: `^p11_rs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what this reward signal measures, purpose
2. `## Signal Design` — type, scale, model, computation method
3. `## Criteria` — dimensions scored, weights, examples
4. `## Application` — how the signal drives improvement (RLHF, DPO, filtering)
## Constraints
- max_bytes: 2048 (body only — dense signal spec)
- naming: p11_reward_{scope}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- signal_type MUST match one of the five defined enum values
- quality: null always
- NO implementation code in body — spec only
- baseline MUST be within declared scale range
