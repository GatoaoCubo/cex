---
id: um_{{peer_id}}
kind: user_model
8f: F2_become
pillar: P10
title: "User Model: {{peer_id}}"
peer_id: {{unique_peer_identifier}}
workspace: {{workspace_id}}
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
quality: 8.1
tags: [user_model, honcho, dialectic, P10, {{domain_tag}}]
tldr: "{{peer_id}} user model: {{2_key_known_facts_max_80ch}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_agent_id}}"
---

## Peer Profile
`{{who_this_peer_is_1_sentence}}`
`{{workspace_context_and_scope}}`

## Collections

### preferences
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `{{pref_key_1}}` | {{pref_value_1}} | {{0.0-1.0}} | {{YYYY-MM-DD}} |
| `{{pref_key_2}}` | {{pref_value_2}} | {{0.0-1.0}} | {{YYYY-MM-DD}} |

### working_style
| Key | Value | Confidence | Last Updated |
|-----|-------|------------|--------------|
| `{{style_key_1}}` | {{style_value_1}} | {{0.0-1.0}} | {{YYYY-MM-DD}} |
| `{{style_key_2}}` | {{style_value_2}} | {{0.0-1.0}} | {{YYYY-MM-DD}} |

### context_history
| Session ID | Key Insight | Derived At |
|------------|-------------|-----------|
| `{{session_id}}` | {{insight_summary}} | {{YYYY-MM-DD}} |

## Dialectic Loop Status
| Phase | Status | Last Run |
|-------|--------|----------|
| pre_response_insight | {{enabled\|disabled}} | {{YYYY-MM-DD}} |
| post_response_derive | {{enabled\|disabled}} | {{YYYY-MM-DD}} |
| compaction | {{cadence_turns}} turns | {{YYYY-MM-DD}} |

## API Surface
| Method | Signature | Purpose |
|--------|-----------|---------|
| peer.chat | `peer.chat(query: str) -> str` | NL query against user model |
| session.context | `session.context(token_limit: int) -> str` | Bounded context retrieval |
| session.add_messages | `session.add_messages(msgs: list) -> None` | Ingest turn |
| search | `search(query: str, top_k: int) -> list` | Hybrid FTS + vector search |
| session.representation | `session.representation() -> str` | Static insight for context injection |

## Update History
| Version | Change | Date |
|---------|--------|------|
| 1.0.0 | Initial peer record created | {{YYYY-MM-DD}} |
