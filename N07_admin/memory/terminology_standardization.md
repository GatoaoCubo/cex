---
id: n07_memory_terminology
kind: memory-summary
nucleus: N07
pillar: P10
title: "Terminology Standardization -- Metaphors vs Industry Terms"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: N07_orchestrator
quality: 9.1
tags: [terminology, naming, metaphors, industry, standards, permanent]
tldr: "CEX uses game metaphors internally. Artifacts must use industry terms. This maps one to the other and tracks the rename cascade."
density_score: null
source_session: SELF_BOOTSTRAP_2026-04-07
linked_artifacts:
  primary: "_docs/specs/spec_metaphor_dictionary.md"
  related:
    - .cex/kinds_meta.json
    - _docs/specs/spec_n07_bootstrap_context.md
---

# Terminology: What to Use Where

## Rule (INVIOLABLE)

| Context | Use |
|---------|-----|
| User talking to system | Accept metaphors, translate silently |
| Artifacts (frontmatter, body) | Industry terms ONLY |
| Code (tools, scripts) | Industry terms ONLY |
| Docs (specs, KCs) | Industry terms ONLY |
| Boot prompts / rules | Industry terms ONLY |
| This memory file | Both (for translation) |

## Canonical Term Map

| Metaphor | Industry Term | Where it leaks in repo |
|----------|--------------|----------------------|
| card | artifact | Mostly clean — spec_metaphor_dictionary uses "card" |
| deck (file) | agent_card | RENAMED: agent_card_n0{1-7}.md, boot/*.cmd, rules, compiled |
| deck (concept) | context_assembly | spec_metaphor_dictionary, spec_n07_bootstrap_context |
| hand | working_context | spec_metaphor_dictionary only |
| draw | retrieval (RAG) | spec_metaphor_dictionary only |
| play | generation / inference | spec_metaphor_dictionary only |
| round | pipeline_run | spec_metaphor_dictionary only |
| table | multi_agent_orchestration | spec_metaphor_dictionary only |
| dealer | orchestrator | spec_metaphor_dictionary only |
| genesis | archetype_layer | N00_genesis/ dir name, multiple docs |
| mold | archetype | Multiple docs, rules |
| filled mold | instance | Multiple docs |
| fractal | mirrored_structure | CLAUDE.md, docs |
| building | system | spec_metaphor_dictionary |
| floor | agent_domain | spec_metaphor_dictionary |
| superintendent | agent | spec_metaphor_dictionary |
| blank brain | unconfigured_instance | CLAUDE.md, brand docs |
| handoff (doc) | task_spec | Entire runtime layer uses "handoff" — acceptable as CEX convention |

## Rename Priority

| Priority | What | Scope | Risk |
|----------|------|-------|------|
| DONE | deck_n0X.md → agent_card_n0X.md | 7 files + boot/*.cmd + rules + specs + compiled + archives | Executed 2026-04-07 by N03 |
| LOW | N00_genesis/ → keep | Directory name is fine — "genesis" in path is clear enough | — |
| SKIP | handoff | Too deeply wired — rename would break runtime. "Handoff" is acceptable as CEX-specific term. | — |
| SKIP | signal | Already industry standard | — |

## Teaching Notes (for user)

1. RAG = Retrieval Augmented Generation. Your "draw" is the R in RAG.
2. Agent Card = Google A2A protocol standard. Your "deck file" IS an agent card.
3. Context Assembly = the process of building the prompt from multiple sources. Your "deck concept."
4. Orchestrator = LangGraph "supervisor", CrewAI "manager". Your "dealer."
5. Instance = OOP pattern. archetype (class) → instance (object). Your "filled mold."
6. Convention over Configuration = Rails pattern. Every agent has same structure. Your "fractal."
