---
id: p12_ct_knowledge_synthesis.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: knowledge_synthesis
purpose: Research a domain, produce knowledge cards, build retriever and embedding configs, and assemble a wired knowledge graph with index
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "researcher -> architect -> indexer -> orchestrator"
handoff_protocol_id: a2a-task-sequential
quality: 8.8
density_score: high
title: "Knowledge Synthesis Crew Template"
version: "1.0.0"
author: n07_crewwiring
tags: [crew_template, knowledge_synthesis, rag, knowledge_graph, composable, crewai, karpathy_loop]
tldr: "4-role sequential crew: deep research -> retriever+embedding config -> knowledge graph+index -> wired compiled package"
domain: "knowledge pipeline orchestration"
created: "2026-04-22"
updated: "2026-04-22"
related:
  - p02_ra_deep_researcher.md
  - p02_ra_knowledge_architect.md
  - p02_ra_knowledge_indexer.md
  - p02_ra_knowledge_orchestrator.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p12_ct_product_launch.md
  - bld_schema_crew_template
  - p01_kc_rag_patterns
---

## Overview
Instantiate when a domain must be fully ingested into CEXAI's knowledge
infrastructure: from raw research through to a wired, indexed, cross-referenced
knowledge graph. This crew is the canonical Karpathy loop -- research feeds
structure, structure feeds retrieval, retrieval feeds synthesis. Producer is
N01 (intelligence); consumers are N04 (knowledge) and any RAG-enabled nucleus.
Four roles run in strict sequence; each emits a typed artifact package that the
next role grounds on before starting its own 8F pipeline.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| deep_researcher | p02_ra_deep_researcher.md | Query domain "RAG patterns for structured knowledge"; emit 3 knowledge_cards covering concepts, implementation patterns, and trade-offs |
| knowledge_architect | p02_ra_knowledge_architect.md | Read 3 KCs; design and emit retriever_config + embedding_config tuned to the domain vocabulary |
| knowledge_indexer | p02_ra_knowledge_indexer.md | Read KCs + configs; assemble knowledge_graph (entity-relation map) + knowledge_index (TF-IDF + vector manifest) |
| knowledge_orchestrator | p02_ra_knowledge_orchestrator.md | Read all upstream artifacts; cross-reference, compile, verify coherence, emit final wired package |

## Process
Topology: `sequential`. Rationale: each role has a hard input dependency on the
prior role's artifact. The architect cannot design retrieval config without the
domain vocabulary the researcher surfaces. The indexer cannot build the graph
without the embedding space the architect defines. The orchestrator cannot wire
a coherent package without the completed graph and index. Parallelism introduces
consistency risk (embedding mismatch, broken entity refs) with zero throughput gain.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| deep_researcher | shared | persistent (KCs saved to P01_knowledge library) |
| knowledge_architect | shared | per-crew-instance (configs scoped to this domain run) |
| knowledge_indexer | shared | persistent (knowledge_graph + index saved to P10_memory) |
| knowledge_orchestrator | shared | persistent (compiled package archived; cross-refs survive session) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal with
`artifact_path` list + `quality_score`. The receiving role reads every
upstream artifact listed in the signal before starting its own F1 CONSTRAIN.
Signals are written to `.cex/runtime/signals/` with crew instance id prefix.
No role may start until the prior signal is present and `quality_score >= 8.0`.

## Success Criteria
- [ ] All 4 role artifact packages exist under `.cex/runtime/crews/{instance_id}/`
- [ ] 3 knowledge_cards present, each quality >= 8.0 (gate p11_qg_crew_template)
- [ ] retriever_config + embedding_config both compile without errors
- [ ] knowledge_graph has >= 10 entity nodes with typed edges
- [ ] knowledge_index covers 100% of KC content (no orphan chunks)
- [ ] Final wired package compiles clean: `python _tools/cex_compile.py --all`
- [ ] Handoff signals present for 4/4 roles

## Instantiation
```bash
python _tools/cex_crew.py run knowledge_synthesis \
    --charter N01_intelligence/crews/team_charter_ks_demo.md

python _tools/cex_crew.py run knowledge_synthesis \
    --charter N01_intelligence/crews/team_charter_ks_demo.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_deep_researcher.md]] | upstream | 0.41 |
| [[p02_ra_knowledge_architect.md]] | upstream | 0.39 |
| [[p02_ra_knowledge_indexer.md]] | upstream | 0.37 |
| [[p02_ra_knowledge_orchestrator.md]] | upstream | 0.35 |
| [[bld_instruction_crew_template]] | upstream | 0.33 |
| [[bld_collaboration_crew_template]] | related | 0.31 |
| [[p11_qg_crew_template]] | upstream | 0.29 |
| [[p12_ct_product_launch.md]] | sibling | 0.27 |
| [[bld_schema_crew_template]] | upstream | 0.25 |
| [[p01_kc_rag_patterns]] | downstream | 0.23 |
