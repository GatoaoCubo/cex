---
pillar: P02
llm_function: INJECT
purpose: Domain knowledge for router production — atomic searchable facts
sources: router-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: router

## Executive Summary

A router is a dense rule table that maps task patterns to satellite or agent destinations using confidence thresholds, priority ranking, and fallback logic. Unlike dispatch_rule (single keyword-satellite map with no logic) or workflow (multi-step sequence), a router handles the full decision algorithm — confidence gating, priority sorting, load balancing, and escalation for ambiguous or low-confidence matches.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P02 (agents) |
| ID pattern | `^p02_router_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 14 (includes `routes_count`, `fallback_route`, `confidence_threshold`) |
| Recommended fields | 5 (timeout_ms, retry_count, load_balance, keywords, density_score) |
| Default `confidence_threshold` | 0.7 |
| Default `timeout_ms` | 5000 |
| Max body | 4096 bytes |
| Body sections | 6 (Routes, Decision Logic, Fallback, Escalation, Integration, References) |
| Naming | `p02_router_{slug}.md` |

## Patterns

| Pattern | Rule |
|---------|------|
| Route object fields | pattern (regex or keyword list), destination, priority (1–100), confidence_min |
| Priority ordering | Higher integer = preferred; router selects highest-priority matching route first |
| Confidence gating | Match confidence < `confidence_threshold` falls through to fallback |
| `routes_count` integrity | Must equal exact number of rows in Routes table — enforced by HARD gate |
| `fallback_route` requirement | Must be a valid satellite name or literal `"escalate"`; never empty |
| Pattern uniqueness | No two routes may share the same pattern |
| Load balancing options | `priority` (default) / `round_robin` / `weighted` / `none` |
| Escalation trigger | Ambiguous multi-match or confidence tie — must have explicit resolution policy |

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| `routes_count` != actual route rows | HARD gate failure — count integrity is enforced |
| Duplicate route patterns | Ambiguous dispatch; selection behavior is undefined |
| Missing or invalid `fallback_route` | Unmatched tasks have no safe landing; system hangs |
| `confidence_threshold` outside 0.0–1.0 | Out of range; validation rejects the artifact |
| Router for single keyword mapping | Overkill; use dispatch_rule (simpler, lower overhead) |
| Router for multi-step orchestration | Wrong abstraction; use workflow for sequenced steps |
| Missing `## Escalation` section | Low-confidence ties have no resolution path |
| `quality` non-null | Self-scoring forbidden; always `null` |

## Application

1. Identify the routing domain and enumerate all task pattern categories
2. Write frontmatter: 14 required fields; set `confidence_threshold` (default 0.7), `fallback_route`; `quality: null`
3. Write `## Routes` table — one row per unique pattern; assign destination, priority (1–100), confidence_min
4. Set `routes_count` = exact number of rows in Routes table
5. Write `## Decision Logic` — algorithm: priority sort → confidence check → tie-breaking rule
6. Write `## Fallback` — behavior when no pattern matches or confidence < threshold
7. Write `## Escalation` — policy for ambiguous multi-match (same priority or same confidence_min)
8. Write `## Integration` and `## References`; verify body <= 4096 bytes; `id` equals filename stem

## References

- router-builder MANIFEST.md v1.0.0
- router SCHEMA.md (no version declared)
- Boundary: router (full decision algorithm, P02) vs dispatch_rule (P12, single keyword map) vs workflow (P12, multi-step sequence) vs agent (P02, runtime identity) vs fallback_chain (P02, model degradation sequence)
