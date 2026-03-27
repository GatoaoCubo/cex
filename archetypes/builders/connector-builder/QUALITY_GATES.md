---
pillar: P11
llm_function: GOVERN
purpose: Automated quality gates for connector validation
pattern: HARD gates block publish, SOFT gates contribute to 0-10 score
---

# Quality Gates: connector

## HARD Gates (block publish if ANY fails)

| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses | Broken YAML = broken artifact |
| H02 | id matches `^p04_conn_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "connector" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | Required fields present: id, kind, pillar, version, created, updated, author, name, service, protocol, auth, endpoints, quality, tags, tldr | Completeness |
| H07 | body has ## Overview, ## Endpoints, ## Data Mapping, ## Health & Errors | Core sections required |
| H08 | body <= 1024 bytes | Compact connector spec |

## SOFT Gates (contribute to score)

| Gate | Check | Weight | Score if pass |
|------|-------|--------|---------------|
| S01 | tldr <= 160 chars, non-empty | 1.0 | 10 |
| S02 | tags is list, len >= 3, includes "connector" | 0.5 | 10 |
| S03 | endpoints names match endpoint names in ## Endpoints section (zero drift) | 1.0 | 10 |
| S04 | Each endpoint has direction annotation (inbound/outbound) | 1.0 | 10 |
| S05 | auth field present and valid enum value | 0.5 | 10 |
| S06 | Each endpoint has data shape defined | 1.0 | 10 |
| S07 | ## Data Mapping has inbound + outbound rules + idempotency | 1.0 | 10 |
| S08 | health_check field present with concrete strategy | 0.5 | 10 |
| S09 | description <= 200 chars and non-generic | 0.5 | 10 |
| S10 | density_score >= 0.80 (no filler phrases) | 0.5 | 10 |
| S11 | retry and rate_limit fields present | 0.5 | 10 |
| S12 | protocol field matches integration pattern described in body | 0.5 | 10 |

## Scoring Formula
```text
hard_pass = all 8 HARD gates pass
soft_score = sum(gate_score * weight) / sum(weights)
final = hard_pass ? soft_score : 0

GOLDEN:  >= 9.5 (all HARD + 95% SOFT)
PUBLISH: >= 8.0 (all HARD + 80% SOFT)
REVIEW:  >= 7.0 (all HARD + 70% SOFT)
REJECT:  < 7.0 or any HARD fail
```

## Pre-Production Checklist
- [ ] Target service identified with integration pattern (webhook, stream, sync)
- [ ] All endpoints enumerated with direction (inbound/outbound)
- [ ] Protocol selected matching service capabilities
- [ ] No existing connector for this service (brain_query checked)
- [ ] Data mapping rules documented for both directions
