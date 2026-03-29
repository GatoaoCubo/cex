---
kind: architecture
id: bld_architecture_chunk_strategy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of chunk_strategy — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| method | Splitting algorithm (fixed, recursive, semantic, structural) | chunk_strategy | required |
| chunk_size | Target size in tokens or characters | chunk_strategy | required |
| chunk_overlap | Overlap between consecutive chunks | chunk_strategy | required |
| separators | Ordered list of split characters/patterns | chunk_strategy | required |
| tokenizer | Tokenizer for accurate size counting | external | optional |
| embedding_config | Vector model that consumes chunks | P01 | consumer |
| retriever_config | Search config that queries chunks | P01 | consumer |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| method | chunk_strategy | produces | Splitting algorithm (fixed, recursive, semantic, structural) |
| chunk_size | chunk_strategy | produces | Target size in tokens or characters |
| chunk_overlap | chunk_strategy | produces | Overlap between consecutive chunks |
| separators | chunk_strategy | produces | Ordered list of split characters/patterns |
| tokenizer | external | produces | Tokenizer for accurate size counting |
| embedding_config | P01 | depends | Vector model that consumes chunks |
| retriever_config | P01 | depends | Search config that queries chunks |
## Boundary Table
| chunk_strategy IS | chunk_strategy IS NOT |
|-------------|----------------|
| Chunking method configuration — how to split documents into retrievable segments | embedding_config (vector model params) |
| Not embedding_config | embedding_config (vector model params) |
| Not retriever_config | retriever_config (search params) |
| Not knowledge_card | knowledge_card (content) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | method, chunk_size, chunk_overlap, separators | Define the artifact's core parameters |
| optional | tokenizer | Extend with recommended fields |
| external | embedding_config, retriever_config | Upstream/downstream connections |
