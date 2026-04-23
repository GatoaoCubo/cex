---
quality: 8.6
quality: 8.0
kind: tools
id: bld_tools_user_model
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for user_model production
title: "Tools: user-model-builder"
version: "1.0.0"
author: n03_builder
tags: [user_model, builder, tools, honcho, P04]
tldr: "Tools for user_model: honcho SDK for peer/session management, SQLite for storage, cex_compile for artifact compilation."
domain: "user model construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_tools_session_state
  - bld_tools_kind
  - bld_tools_runtime_state
  - bld_tools_session_backend
  - bld_tools_validation_schema
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_memory_scope
  - bld_tools_knowledge_graph
  - bld_tools_prompt_version
---

# Tools: user-model-builder

## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| honcho SDK | Create/query Peer, Session, Collection, Document | Runtime (not build time) | CONDITIONAL |
| brain_query [MCP] | Search existing user_model artifacts to avoid duplication | Phase 1 (check duplicates) | CONDITIONAL |
| cex_compile.py | Compile .md artifact to .yaml | F8 COLLABORATE | REQUIRED |
| cex_doctor.py | Health check after build | F8 COLLABORATE | REQUIRED |
| json.tool | Validate kinds_meta.json after patch | F7 GOVERN | REQUIRED |

## Runtime APIs (Honcho SDK)
| API | Method | Purpose |
|-----|--------|---------|
| Peer creation | `app.peers.get_or_create(peer_id=peer_id)` | Create or retrieve peer record |
| Session management | `app.sessions.create(peer_id=peer_id)` | New interaction session |
| Insight query | `peer.chat(query)` | NL query against user model Collections |
| Context extraction | `session.context(token_limit=500)` | Bounded context for prompt injection |
| Turn ingestion | `session.add_messages([{is_user: True, content: msg}])` | Store turn in session |
| Fact search | `session.search(query)` | Hybrid FTS + vector search |
| Representation | `session.representation()` | Static insight string for pre-response injection |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | N00_genesis/P10_memory/_schema.yaml | Field definitions, user_model kind |
| Template | N00_genesis/P10_memory/tpl_user_model.md | Canonical template |
| Examples | archetypes/builders/user-model-builder/bld_examples_user_model.md | Golden examples |
| KC | N00_genesis/P01_knowledge/library/kind/kc_user_model.md | Domain knowledge |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Validation Commands
```bash
# Validate JSON after kinds_meta.json patch
python -m json.tool .cex/kinds_meta.json

# Compile artifact
python _tools/cex_compile.py N00_genesis/P10_memory/tpl_user_model.md

# Health check
python _tools/cex_doctor.py

# Verify id pattern
python -c "import re; print(re.match(r'^um_[a-z][a-z0-9_]+$', 'um_gato3_main'))"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_session_state]] | sibling | 0.45 |
| [[bld_tools_kind]] | sibling | 0.35 |
| [[bld_tools_runtime_state]] | sibling | 0.35 |
| [[bld_tools_session_backend]] | sibling | 0.35 |
| [[bld_tools_validation_schema]] | sibling | 0.35 |
| [[bld_tools_cli_tool]] | sibling | 0.34 |
| [[bld_tools_retriever_config]] | sibling | 0.33 |
| [[bld_tools_memory_scope]] | sibling | 0.32 |
| [[bld_tools_knowledge_graph]] | sibling | 0.32 |
| [[bld_tools_prompt_version]] | sibling | 0.32 |
