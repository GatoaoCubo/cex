---
id: n04_knowledge_memory_index
kind: memory_summary
nucleus: N04
pillar: P10
domain: knowledge_management
quality: 8.8
created: 2026-04-02
type: persistent_memory
scope: knowledge_nucleus
density_score: 1.0
---

# N04 Knowledge Memory Index

## Domain Memory
- **RAG Pipeline**: TF-IDF retriever functional, 9.5MB index, ~2184 documents
- **KC Library**: 106 knowledge cards covering all major kinds
- **Taxonomy**: 114 kinds tracked across 12 pillars
- **Embeddings**: Status unclear - mainly TF-IDF based retrieval
- **Cross-References**: Naming convention drift (hyphens vs underscores)

## Recent Learning
- Unicode corruption affects critical system files (.cex/kinds_meta.json)
- N04 memory system was empty - now being populated
- Retriever works but memory selection tools broken
- Builders (107) vs KCs (106) - mainly naming convention issues

## Knowledge Gaps Identified
- Missing semantic search capabilities
- No persistent memory accumulation patterns
- Limited cross-nucleus knowledge sharing verification
- Taxonomy consistency automation missing

## Tools Status
- ✅ cex_retriever.py: functional
- ❌ cex_memory_select.py: broken  
- ✅ cex_compile.py: functional
- ⚠️ .cex/retriever_index.json: unicode issues

## Memory Injection Points
- F3 INJECT: KCs loaded into 8F pipeline
- Handoffs: Knowledge context in task specifications  
- Cross-nucleus: Domain expertise sharing
- Retrieval: Similarity search for relevant artifacts

## Improvement Opportunities
1. Implement semantic embeddings alongside TF-IDF
2. Create automated taxonomy consistency checks
3. Fix memory selection and injection tools
4. Establish memory decay and refresh protocols
5. Create knowledge graph relationships between KCs