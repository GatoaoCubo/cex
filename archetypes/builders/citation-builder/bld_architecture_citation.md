---
kind: architecture
id: bld_architecture_citation
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of citation — inventory, dependencies, and architectural position
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
