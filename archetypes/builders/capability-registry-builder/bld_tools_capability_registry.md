---
kind: tools
id: bld_tools_capability_registry
pillar: P04
llm_function: CALL
purpose: Tools available for capability_registry production
quality: 9.0
title: "Tools Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, tools, agent-discovery]
tldr: "Tools available for capability_registry production"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_kind
  - bld_collaboration_agent
  - bld_instruction_agent
  - capability-registry-builder
  - agent-builder
  - bld_tools_agent
  - p01_kc_agent
  - bld_knowledge_card_capability_registry
  - bld_tools_agent_package
  - bld_instruction_kind
---

## Production Tools
| Tool                  | Purpose                                             | When                        |
|-----------------------|-----------------------------------------------------|-----------------------------|
| cex_query.py          | TF-IDF agent discovery (--list-agents flag)         | Phase 1: RESEARCH           |
| cex_retriever.py      | Semantic similarity search across agent definitions  | Phase 1: RESEARCH           |
| cex_compile.py        | Validates YAML frontmatter after save               | Phase 3: VALIDATE           |
| cex_doctor.py         | Checks for phantom agent references                 | Phase 3: VALIDATE           |
| cex_score.py          | Reads quality_baseline from scored artifacts        | Phase 2: COMPOSE            |
| cex_materialize.py    | Generates sub-agent .md from builder ISOs           | Pre-build context loading   |

## Discovery Tools
| Tool                  | Purpose                                             | When                        |
|-----------------------|-----------------------------------------------------|-----------------------------|
| Glob *.claude/agents/ | List all 252 builder sub-agent files                | Phase 1: enumerate sources  |
| Glob N0x_*/agents/    | List all nucleus domain agent files                 | Phase 1: enumerate sources  |
| Grep capabilities:    | Extract capability lists from agent files           | Phase 1: field extraction   |
| Grep domain:          | Extract domain keywords from agent frontmatter      | Phase 1: keyword derivation |

## Validation Tools
| Tool                  | Purpose                                             | When                        |
|-----------------------|-----------------------------------------------------|-----------------------------|
| cex_compile.py        | Schema validation, frontmatter check               | Post-build                  |
| cex_doctor.py         | Builder health check -- catches phantom references  | Post-build                  |
| cex_hooks.py          | Pre-commit ASCII check for any generated .py       | On git commit               |

## External References
- A2A Protocol v0.3 spec (agent-card schema): `https://a2a-protocol.org/latest/specification/`
- OpenAI function-calling JSON Schema: referenced in N01_intelligence/research/ai2ai_exhaustive_scan_20260414.md
- LangChain ToolRegistry: referenced in kc_agent.md (P02 knowledge card)
- kinds_meta.json: `.cex/kinds_meta.json` -- kind-to-pillar-to-domain mapping used for keyword derivation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | sibling | 0.33 |
| [[bld_collaboration_agent]] | downstream | 0.32 |
| [[bld_instruction_agent]] | upstream | 0.31 |
| [[capability-registry-builder]] | downstream | 0.31 |
| [[agent-builder]] | upstream | 0.31 |
| [[bld_tools_agent]] | sibling | 0.30 |
| [[p01_kc_agent]] | upstream | 0.29 |
| [[bld_knowledge_card_capability_registry]] | upstream | 0.29 |
| [[bld_tools_agent_package]] | sibling | 0.29 |
| [[bld_instruction_kind]] | upstream | 0.28 |
