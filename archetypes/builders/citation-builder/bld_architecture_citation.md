---
kind: architecture
id: bld_architecture_citation
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of citation — inventory, dependencies, and architectural position
quality: 9.0
title: "Architecture Citation"
version: "1.0.0"
author: n03_builder
tags: [citation, builder, examples]
tldr: "Golden and anti-examples for citation construction, demonstrating ideal structure and common pitfalls."
domain: "citation construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_citation
  - p03_sp_citation_builder
  - citation-builder
  - bld_output_template_citation
  - bld_instruction_citation
  - bld_knowledge_card_citation
  - p11_qg_citation
  - p10_lr_citation_builder
  - bld_collaboration_citation
  - bld_architecture_rag_source
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| source_type | Classification of source origin | author | required |
| reliability_tier | Trust level assessment | author | required |
| url | Direct verification link | author | required |
| date_accessed | Temporal freshness anchor | author | required |
| excerpt | Relevant passage from source | author | required |
| relevance_scope | Domain/kind mapping | author | recommended |
## Dependency Graph
```
rag_source, search_tool --> [citation] --> knowledge_card, context_doc
                                 |
                           glossary_entry, learning_record, agent output
```
| From | To | Type | Data |
|------|----|------|------|
| rag_source | citation | data_flow | source discovered via retrieval |
| search_tool | citation | data_flow | source found via web search |
| citation | knowledge_card | data_flow | provenance for claims |
| citation | context_doc | data_flow | supporting evidence |
## Boundary Table
| citation IS | citation IS NOT |
|-------------|-----------------|
| Structured source reference with provenance | The knowledge content itself (knowledge_card) |
| Tiered reliability assessment | Retrieval pipeline config (rag_source) |
| Verifiable via URL + date_accessed | Term definition (glossary_entry) |
| 1-3 sentence excerpt of key claim | Full document reproduction |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | source_type, reliability_tier | Classify and assess source |
| Content | excerpt, url, date_accessed | Carry verifiable provenance |
| Discoverability | relevance_scope, tags | Enable routing to consumers |
| Consumption | knowledge_card, context_doc | Inject provenance into artifacts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_citation]] | upstream | 0.48 |
| [[p03_sp_citation_builder]] | upstream | 0.46 |
| [[citation-builder]] | upstream | 0.45 |
| [[bld_output_template_citation]] | upstream | 0.44 |
| [[bld_instruction_citation]] | upstream | 0.41 |
| [[bld_knowledge_card_citation]] | upstream | 0.37 |
| [[p11_qg_citation]] | downstream | 0.37 |
| [[p10_lr_citation_builder]] | downstream | 0.36 |
| [[bld_collaboration_citation]] | downstream | 0.36 |
| [[bld_architecture_rag_source]] | sibling | 0.36 |
