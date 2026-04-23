---
kind: quality_gate
id: p11_qg_user_model
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of user_model artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.8
title: "Gate: user_model"
version: "1.0.0"
author: "n03_builder"
tags: [quality-gate, user-model, P10, memory, honcho, dialectic]
tldr: "Pass/fail gate for user_model artifacts: id pattern, collections minimum, dialectic config, storage declaration, boundary clarity vs entity_memory/session_state."
domain: "user model -- cross-session dialectic peer representation implementing Honcho pattern"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - p11_qg_entity_memory
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - p11_qg_memory_scope
  - p11_qg_retriever_config
  - p11_qg_handoff_protocol
  - p11_qg_output_validator
  - p11_qg_effort_profile
  - p11_qg_prompt_version
  - p11_qg_function_def
---

## Quality Gate

# Gate: user_model

## Definition
| Field | Value |
|---|---|
| metric | user_model artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: user_model` |

## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^um_[a-z][a-z0-9_]+$` | ID has hyphens, uppercase, or missing `um_` prefix |
| H03 | Tags >= 3 items, includes "user_model" and "honcho" | Fewer than 3 tags, or missing required tags |
| H04 | Kind equals literal `user_model` | `kind: entity_memory` or `kind: user_memory` or any other value |
| H05 | Quality field is null | `quality: 8.0` or any non-null value |
| H06 | All required fields present | Missing `peer_id`, `workspace`, `dialectic`, `collections`, `storage`, `retention` |
| H07 | Collections list has >= 3 named items | Fewer than 3 collections, or collections field absent |
| H08 | storage.primary is declared and in enum | `storage.primary` absent, or value not in [sqlite, pgvector, turbopuffer, lancedb] |
| H09 | Dialectic loop fully configured | Missing `pre_response_insight`, `post_response_derive`, or `compaction_cadence_turns` |
| H10 | Not entity_memory pattern | Contains `entity_type` or `attributes` map fields -- wrong kind |

## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Collection completeness | 1.0 | >= 3 collections covering preferences, working_style, context_history (or equivalent) |
| Dialectic config quality | 1.0 | All 3 dialectic fields present with sensible values; compaction_cadence positive int |
| Storage declaration | 1.0 | primary + fallback_chain + pgvector_enabled all declared explicitly |
| Retention policy | 0.75 | messages_ttl_days and derived_facts_ttl_days both declared |
| API surface completeness | 1.0 | All 5 API methods documented with signatures |
| Peer profile quality | 0.75 | 2-sentence peer profile with workspace context |
| Boundary clarity | 1.0 | Not entity_memory (no entity_type/attributes map), not session_state (not ephemeral) |
| tldr quality | 0.75 | <= 160 chars, includes peer_id and 2+ key facts |
| Update history | 0.5 | At least 1 version entry with date |
| Tags relevance | 0.5 | Tags include "honcho", "dialectic", domain keywords |

## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
| Field | Value |
|---|---|
| conditions | Stub peer record for new user with no interaction history yet |
| approver | Author self-certification with "cold_start_stub" note in frontmatter |
| audit_trail | Bypass note with expected promotion date |
| expiry | 7d -- stubs must be populated from real interactions or removed |
| never_bypass | H01 (unparseable YAML), H05 (self-scored), H10 (wrong kind pollutes memory index) |

## Examples

# Examples: user-model-builder

## Golden Example 1 -- Developer User Model

INPUT: "Create user model for gato3, developer who uses N07 orchestrator daily"
OUTPUT:
```yaml
id: um_gato3_main
kind: user_model
pillar: P10
title: "User Model: gato3"
peer_id: gato3
workspace: cex_default
storage:
  primary: sqlite
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: false
dialectic:
  pre_response_insight: true
  post_response_derive: true
  compaction_cadence_turns: 50
collections:
  - name: preferences
  - name: working_style
  - name: context_history
retention:
  messages_ttl_days: 365
  derived_facts_ttl_days: null
version: 1.0.0
quality: null
tags: [user_model, honcho, dialectic, P10, developer]
tldr: "gato3 user model: senior dev, PT-BR, prefers terse autonomous execution, CEX N07 orchestrator daily."
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
description: "Cross-session dialectic model for gato3 -- CEX developer, PT-BR, Opus-tier orchestration, autonomous mode preferred."
```
### Peer Profile
gato3 is a senior developer and CEX architect who uses N07 daily for artifact orchestration.
Workspace: cex_default (single-tenant development environment).

### Collections

#### preferences
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| response_language | PT-BR | 0.95 | 2026-04-18 |
| response_length | terse | 0.93 | 2026-04-18 |
| execution_mode | autonomous | 0.90 | 2026-04-18 |
| commit_style | descriptive_body | 0.88 | 2026-04-18 |

#### working_style
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| domain_expertise | senior_developer | 0.97 | 2026-04-18 |
| orchestration_model | opus_tier | 0.92 | 2026-04-18 |
| polling_preference | 60s_intervals | 0.85 | 2026-04-18 |

#### context_history
| Session ID | Key Insight | Derived At |
|------------|-------------|-----------|
| ses_20260418_001 | User prefers parallel dispatch over sequential; confirms terse responses | 2026-04-18 |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches `^um_` pattern (H02 pass)
- kind: user_model (H04 pass)
- collections: 3 named groups (H07 pass)
- storage.primary declared (H08 pass)
- dialectic fully configured (H09 pass)
- tags >= 3, includes "user_model" + "honcho" (H03 pass)
- All 5 API methods documented (S03 pass)
- Boundary clear: no entity attribute maps, no ephemeral flags (S06 pass)

---

## Golden Example 2 -- Customer Support User Model

INPUT: "Track customer alice_smith for support agent context"
OUTPUT:
```yaml
id: um_alice_smith
kind: user_model
pillar: P10
title: "User Model: alice_smith"
peer_id: alice_smith
workspace: support_prod
storage:
  primary: sqlite
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: false
dialectic:
  pre_response_insight: true
  post_response_derive: true
  compaction_cadence_turns: 20
collections:
  - name: preferences
  - name: support_history
  - name: product_context
retention:
  messages_ttl_days: 180
  derived_facts_ttl_days: 730
version: 1.0.0
quality: null
tags: [user_model, honcho, dialectic, P10, support]
tldr: "alice_smith support user model: 180-day msg retention, compaction every 20 turns, product_context collection."
created: "2026-04-18"
updated: "2026-04-18"
author: "n03_builder"
```

WHY THIS IS GOLDEN:
- Workspace scoped (support_prod) -- multi-tenancy correct
- compaction_cadence_turns=20 (shorter for support context)
- Custom collections (support_history, product_context) -- domain-appropriate
- Retention policy restricted (180d messages) -- GDPR-conscious
- quality: null -- never self-scored

---

## Anti-Example

INPUT: "Create user model for Alice"
BAD OUTPUT:
```yaml
id: alice-user
kind: user_memory
entity_type: person
attributes:
  name: Alice
  role: customer
quality: 8.5
tags: [memory]
```
Alice is a customer.

FAILURES:
1. id: "alice-user" has hyphens and no `um_` prefix -> H02 FAIL
2. kind: "user_memory" not "user_model" -> H04 FAIL
3. entity_type: "person" -- this is entity_memory pattern, not user_model -> wrong kind
4. quality: 8.5 (not null) -> H05 FAIL
5. No dialectic config (missing core field) -> H09 FAIL
6. No collections (missing core field) -> H07 FAIL
7. No storage declaration -> H08 FAIL
8. tags: only 1 item, missing "user_model" and "honcho" -> H03 FAIL
9. Body missing all required sections -> structure FAIL
10. attributes map = entity_memory pattern, NOT user_model (wrong kind entirely)

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
