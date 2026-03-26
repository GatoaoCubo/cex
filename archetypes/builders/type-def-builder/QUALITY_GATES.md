---
id: type-def-builder-quality-gates
kind: quality_gates
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [quality-gates, type-def, P11, governance]
---

## HARD Gates (H-series) — All must pass; any failure = reject

| Gate | Field / Rule | Pass Condition | Failure Action |
|---|---|---|---|
| H01 | `id` pattern | Matches `^p06_td_[a-z][a-z0-9_]*$` | Reject — fix id |
| H02 | `kind` value | Exactly `type_def` | Reject — wrong kind |
| H03 | `pillar` + `layer` | `pillar: P06` AND `layer: spec` | Reject — wrong placement |
| H04 | `base_type` vocabulary | Value in controlled enum (see CONFIG.md) | Reject — use controlled value |
| H05 | `constraints` structure | Object with keyed entries, not free text | Reject — restructure |
| H06 | `nullable` explicit | Boolean `true` or `false`, not absent | Reject — add field |
| H07 | `quality` on draft | Value is `null` | Reject — remove assigned score |
| H08 | `examples` present | At least one example in body | Reject — add example |
| H09 | `type_name` PascalCase | Matches `^[A-Z][A-Za-z0-9]*$` | Reject — fix casing |
| H10 | Byte count | Artifact <= 3072 bytes | Reject — reduce size |

## SOFT Gates (S-series) — Failures lower score but do not reject

| Gate | Field / Rule | Target | Score Impact |
|---|---|---|---|
| S01 | `tldr` quality | Single sentence, <= 120 chars, domain-precise | -0.5 if missing or vague |
| S02 | `domain` clarity | Specific module/domain, not generic | -0.3 if absent or "general" |
| S03 | `tags` count | >= 4 tags for pool eligibility | -0.2 if < 4 |
| S04 | `keywords` section | >= 5 discovery terms in body | -0.3 if absent |
| S05 | Definition prose | Explains domain role, not just field names | -0.4 if tautological |
| S06 | Examples coverage | Spans semantically distinct values (not just valid/invalid) | -0.3 if only one example |
| S07 | `version` SemVer | Matches `^\d+\.\d+\.\d+$` | -0.5 if malformed |
| S08 | `composition` when needed | Present when base_type is union/intersection/tuple | -0.5 if absent for composite |
| S09 | `serialization` for wire types | Present for types used in protocol buffers or wire formats | -0.2 if absent |
| S10 | `density_score` | >= 0.80 (information per byte ratio) | -0.3 if below threshold |

## Scoring Formula

```
base_score = 10.0
hard_failures: each hard gate failure = artifact rejected (no score)
soft_deductions: sum of all S-gate deductions
final_score = base_score - soft_deductions

Tiers:
  >= 9.5 → Golden (pool promotion + remember())
  >= 8.0 → Skilled (pool eligible)
  >= 7.0 → Learning (experimental)
  <  7.0 → Rejected (redo required)
```

## Automation

| Check | Tool | When |
|---|---|---|
| H01-H10 structural | `validate_artifact` [PLANNED] | Post-compose, pre-register |
| Byte count | byte counter (local) | During VALIDATE phase step 2 |
| Pattern match | regex check (local) | During VALIDATE phase step 1 |
| Brain dedup | `brain_query` [IF MCP] | During DISCOVER phase step 6 |

## Pre-Production Checklist

- [ ] H01: id matches `^p06_td_[a-z][a-z0-9_]*$`
- [ ] H02: `kind: type_def`
- [ ] H03: `pillar: P06`, `layer: spec`
- [ ] H04: `base_type` from controlled vocabulary
- [ ] H05: `constraints` is a structured object
- [ ] H06: `nullable` is explicit boolean
- [ ] H07: `quality: null`
- [ ] H08: at least one example in body
- [ ] H09: `type_name` is PascalCase
- [ ] H10: artifact <= 3072 bytes
- [ ] S01: `tldr` is a single precise sentence
- [ ] S08: `composition` present if base_type is union/intersection/tuple
