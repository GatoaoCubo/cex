---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema definition for dispatch_rule - SINGLE SOURCE OF TRUTH
pattern: TEMPLATE derives from this. CONFIG restricts this. Never the inverse.
---

# Schema: dispatch_rule

## Artifact Identity
| Field | Value |
|-------|-------|
| Pillar | `P12` |
| Type | literal `dispatch_rule` |
| Machine format | `yaml` (frontmatter yaml + md body) |
| Naming | `p12_dr_{scope}.yaml` |
| Max bytes | 3072 |

## Required Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string, matches `^p12_dr_[a-z][a-z0-9_]+$` | YES | - | unique rule identifier |
| kind | literal `dispatch_rule` | YES | - | type discriminator |
| pillar | literal `P12` | YES | - | pillar anchor |
| version | string, semver `x.y.z` | YES | - | rule version |
| created | string, ISO 8601 date | YES | - | creation date |
| updated | string, ISO 8601 date | YES | - | last update date |
| author | string, non-empty | YES | - | rule author |
| domain | string, non-empty | YES | - | subject domain of this rule |
| quality | null | YES | null | always null at authoring time |
| tags | list[string], min 1 | YES | - | searchable labels |
| tldr | string, <= 120 chars | YES | - | one-line summary |
| scope | string, non-empty | YES | - | routing domain scope |
| keywords | list[string], min 1 | YES | - | trigger words for matching |
| satellite | string, lowercase slug | YES | - | target satellite name |
| model | enum (`sonnet`, `opus`, `haiku`, `flash`) | YES | - | target model |
| priority | integer, 1-10 | YES | - | dispatch priority (10=highest) |
| confidence_threshold | float, 0.0-1.0 | YES | - | min confidence to trigger |
| fallback | string, lowercase slug | YES | - | fallback satellite if primary unavailable |

## Optional Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| conditions | object | NO | omitted | extra match conditions |
| load_balance | boolean | NO | false | distribute load across instances |
| routing_strategy | enum (`keyword_match`, `semantic`, `hybrid`) | NO | `keyword_match` | matching algorithm |

## Semantic Rules
1. One dispatch_rule routes one scope domain to one satellite
2. `keywords` are the primary match signal; all items are OR-matched
3. `priority` resolves conflicts when multiple rules match the same input
4. `confidence_threshold` gates whether the match fires; below threshold routes to `fallback`
5. `fallback` must differ from `satellite`
6. `conditions` may add AND-conditions on top of keyword match
7. `routing_strategy=hybrid` combines keyword and semantic scoring
8. `quality: null` is mandatory at authoring time; scored only after deployment

## Boundary Rules
`dispatch_rule` IS:
- keyword-to-satellite routing policy
- priority-aware match rule
- lightweight routing decision record

`dispatch_rule` IS NOT:
- `handoff`: no task list, no scope fence, no commit instructions
- `workflow`: no step graph, no sequencing or dependency logic
- `signal`: no runtime status, no quality_score for an event
- `router` (P02): no complex multi-step task-to-model routing

## Canonical Minimal Example
```yaml
---
id: p12_dr_build
kind: dispatch_rule
pillar: P12
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: codex
domain: build
quality: null
tags: [dispatch, build, edison]
tldr: Route build and code tasks to EDISON satellite
scope: build
keywords: [build, code, component, criar, implementar]
satellite: edison
model: opus
priority: 8
confidence_threshold: 0.75
fallback: atlas
---
```
