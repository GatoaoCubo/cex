---
quality: 8.6
quality: 8.0
kind: output_template
id: bld_output_template_user_model
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a user_model artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
title: "Output Template: user_model"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, output_template, honcho]
tldr: "Fill-in-the-blank template for user_model: frontmatter + peer profile + collections + dialectic + API surface."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - p01_kc_session_state
  - bld_output_template_session_backend
  - bld_memory_session_state
  - p01_kc_session_backend
  - bld_output_template_schedule
  - bld_output_template_visual_workflow
  - bld_schema_session_state
  - bld_output_template_entity_memory
  - p10_memory_summary
  - bld_tools_session_state
---

# Output Template: user_model
```yaml
id: um_{{peer_id}}
kind: user_model
pillar: P10
title: "User Model: {{peer_id}}"
peer_id: {{unique_peer_identifier}}
workspace: {{workspace_id}}
storage:
  primary: {{sqlite|pgvector|turbopuffer|lancedb}}
  fallback_chain: [sqlite, turbopuffer, lancedb]
  pgvector_enabled: {{true|false}}
dialectic:
  pre_response_insight: {{true|false}}
  post_response_derive: {{true|false}}
  compaction_cadence_turns: {{positive_integer}}
collections:
  - name: preferences
  - name: working_style
  - name: context_history
  {{additional_collections_if_needed}}
retention:
  messages_ttl_days: {{integer_or_365}}
  derived_facts_ttl_days: {{integer_or_null}}
version: 1.0.0
quality: null
tags: [user_model, honcho, dialectic, P10, {{domain_tag}}]
tldr: "{{peer_id}} user model: {{2_key_known_facts_max_80ch}}"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_agent_id}}"
description: "{{cross_session_dialectic_model_for_peer_max_200ch}}"
```

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
| compaction | every {{N}} turns | {{YYYY-MM-DD}} |

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_session_state]] | downstream | 0.24 |
| [[bld_output_template_session_backend]] | sibling | 0.22 |
| [[bld_memory_session_state]] | downstream | 0.22 |
| [[p01_kc_session_backend]] | downstream | 0.22 |
| [[bld_output_template_schedule]] | sibling | 0.22 |
| [[bld_output_template_visual_workflow]] | sibling | 0.22 |
| [[bld_schema_session_state]] | downstream | 0.20 |
| [[bld_output_template_entity_memory]] | sibling | 0.20 |
| [[p10_memory_summary]] | downstream | 0.20 |
| [[bld_tools_session_state]] | upstream | 0.19 |
