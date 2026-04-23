---
id: p12_ct_rag_pipeline.md
kind: crew_template
pillar: P12
llm_function: CALL
crew_name: rag_pipeline
purpose: Coordinate a 3-role sequential crew that builds end-to-end RAG pipeline configs from source discovery through chunking to retrieval index
process: sequential
crewai_equivalent: "Process.sequential"
autogen_equivalent: "GroupChat.round_robin"
swarm_equivalent: "source_harvester -> chunker -> index_builder"
handoff_protocol_id: a2a-task-sequential
quality: null
density_score: null
title: "RAG Pipeline Crew Template"
version: "1.0.0"
author: n04_knowledge
tags: [crew_template, rag_pipeline, rag, knowledge, composable, n04]
tldr: "3-role sequential crew: source harvest -> chunk strategy design -> retrieval index build"
domain: "RAG pipeline orchestration"
created: "2026-04-23"
updated: "2026-04-23"
related:
  - p02_ra_source_harvester.md
  - p02_ra_chunker.md
  - p02_ra_index_builder.md
  - p12_ct_knowledge_synthesis.md
  - bld_instruction_crew_template
  - bld_collaboration_crew_template
  - p11_qg_crew_template
  - p03_sp_crew_template_builder
  - bld_output_crew_template
  - rag_pipeline_architecture
---

## Overview
Instantiate when standing up a new RAG pipeline for a domain, migrating an
existing corpus to vector retrieval, or upgrading chunking/embedding configs.
Producer is N04; consumers are any nucleus that queries the retrieval layer
(N01 research, N03 builder context injection, N07 preflight).

Three roles run in strict sequence; each emits typed configs that the next
role grounds on. The final deliverable is a validated end-to-end pipeline
config linking sources -> chunks -> embeddings -> vector store -> retriever.

## Roles
| Role | Role Assignment ID | Reason |
|------|---------------------|--------|
| source_harvester | p02_ra_source_harvester.md | Scan domain, evaluate sources, produce rag_source configs |
| chunker | p02_ra_chunker.md | Design chunking strategies per source type, validate against embedding limits |
| index_builder | p02_ra_index_builder.md | Wire embedding + vector store + retriever, validate pipeline end-to-end |

## Process
Topology: `sequential`. Rationale: strict data dependency -- chunker cannot
design strategies without knowing source types and token estimates from
source_harvester; index_builder cannot configure retrieval without knowing
chunk sizes and overlap from chunker. Parallelism would break the
source-to-index provenance chain.

## Memory Scope
| Role | Scope | Retention |
|------|-------|-----------|
| source_harvester | shared | persistent (rag_source configs committed to P01) |
| chunker | shared | persistent (chunk_strategy configs committed to P01) |
| index_builder | shared | persistent (knowledge_index config committed to P10) |

## Handoff Protocol
`a2a-task-sequential` -- each role writes a completion signal under
`.cex/runtime/signals/` with fields `artifact_paths`, `quality_score`,
`config_count`. Next role reads that signal before starting F1 CONSTRAIN.

## Success Criteria
- [ ] All 3 role deliverables exist under `.cex/runtime/crews/{instance_id}/`
- [ ] source_harvester produced >= 3 rag_source configs with relevance_score > 0.7
- [ ] chunker produced chunk_strategies compatible with target embedding model
- [ ] index_builder produced knowledge_index linking all pipeline stages
- [ ] pipeline_validation_report shows no dimension mismatches or config conflicts
- [ ] Handoff signals present for 3/3 roles with no quality_score below 8.0
- [ ] No artifact produced without reading upstream output (provenance enforced)

## Instantiation
```bash
python _tools/cex_crew.py run rag_pipeline \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_rag_pipeline.md

python _tools/cex_crew.py run rag_pipeline \
    --charter N04_knowledge/P12_orchestration/crews/team_charter_rag_pipeline.md \
    --execute
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_ra_source_harvester.md]] | upstream | 0.50 |
| [[p02_ra_chunker.md]] | upstream | 0.48 |
| [[p02_ra_index_builder.md]] | upstream | 0.46 |
| [[p12_ct_knowledge_synthesis.md]] | sibling | 0.40 |
| [[rag_pipeline_architecture]] | upstream | 0.38 |
| [[bld_instruction_crew_template]] | upstream | 0.32 |
| [[bld_collaboration_crew_template]] | related | 0.29 |
| [[p11_qg_crew_template]] | upstream | 0.26 |
| [[p03_sp_crew_template_builder]] | upstream | 0.25 |
| [[bld_output_crew_template]] | upstream | 0.22 |
