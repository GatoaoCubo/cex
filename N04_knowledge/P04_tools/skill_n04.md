---
id: skill_n04
kind: skill
8f: F5_call
nucleus: n04
pillar: P04
mirrors: N00_genesis/P04_tools/tpl_skill.md
mirror_version: 1.0.0
promoted_from: null
overrides:
  tone: archival, dense, citation-thick
  voice: third-person encyclopedic
  sin_lens: Knowledge Gluttony
  required_fields:
    - sources
    - retrieval_method
    - freshness
  quality_threshold: 9.2
  density_target: 0.92
  example_corpus: 3+ examples with source manifest
version: 1.0.0
quality: 7.8
tags: [mirror, n04, knowledge, skill, hermes_assimilation, citation_first, rag_aware]
related:
  - bld_collaboration_skill
  - bld_architecture_skill
  - bld_system_prompt_skill
  - bld_memory_skill
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - skill-builder
  - p03_ins_skill_builder
  - p01_kc_skill
  - bld_output_template_skill
---

## Override Rationale

N04 skills are **citation-first, retrieval-augmented, and chunk-aware**. Every skill
invocation must surface at least one source; if the skill cannot cite a retrieval
path, it must flag the output as `ungrounded` and request corpus ingestion before
proceeding. This is Knowledge Gluttony applied to tool design: every capability
must feed the knowledge loop, not merely produce output.

## N04 Skill Taxonomy

| Skill | Trigger | Retrieval Method | Output Kind |
|-------|---------|-----------------|-------------|
| `kc_retrieve` | "find KC for {{kind}}" | hybrid BM25 + vector | knowledge_card |
| `corpus_ingest` | "ingest {{source}}" | document_loader pipeline | chunk_strategy |
| `term_teach` | new metaphor detected | prompt_compiler lookup | taught_terms entry |
| `taxonomy_audit` | "check coverage for {{pillar}}" | TF-IDF cex_retriever | knowledge_index |
| `memory_persist` | curation_nudge confirmed | user_model_n04 write | entity_memory |
| `citation_trace` | claim without source | corpus search + ranking | citation |
| `freshness_check` | fact older than 90 days | retrieval_history scan | learning_record |

## Skill Contract (all N04 skills)

Every N04 skill MUST include in its output:

```yaml
sources:           # min 3
  - id: {{source_id}}
    path: {{file_or_url}}
    confidence: {{0.0-1.0}}
    retrieved_at: {{YYYY-MM-DD}}
retrieval_method: {{dense|sparse|hybrid|graph}}
freshness: {{YYYY-MM-DD}}
grounded: {{true|false}}
```

If `grounded: false`, skill appends a `corpus_gap` entry to the retrieval_history
and emits a `curation_nudge` to prompt ingestion.

## Chunk-Aware Execution

N04 skills are aware of chunk boundaries when retrieving:
- Source documents are pre-chunked via `chunk_strategy_n04.md` (semantic window)
- Retrieval returns chunk + parent document reference
- Skills cite at chunk granularity, not document granularity

## Example Skill Invocation

```
Input:  "What does CEX say about agent handoffs?"
Skill:  kc_retrieve
Query:  kind=handoff, domain=orchestration
Method: hybrid (BM25 + ada-002 dense)
Result:
  - kc_handoff.md (confidence: 0.93, chunk: §3 Protocol)
  - N04_knowledge/P12_orchestration/handoff_n04.md (confidence: 0.88)
  - N00_genesis/P12_orchestration/tpl_handoff.md (confidence: 0.82)
Output: grounded=true, sources=3, freshness=2026-04-18
```

## Links

- N00 archetype: [[N00_genesis/P04_tools/tpl_skill.md]]
- N00 KC: [[N00_genesis/P01_knowledge/library/kind/kc_skill.md]]
- Related: [[N04_knowledge/P04_tools/retriever_n04.md]]
- Related: [[N04_knowledge/P10_memory/mem_runtime_state_n04.md]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_skill]] | downstream | 0.39 |
| [[bld_architecture_skill]] | downstream | 0.36 |
| [[bld_system_prompt_skill]] | upstream | 0.33 |
| [[bld_memory_skill]] | downstream | 0.33 |
| [[procedural-memory-builder]] | downstream | 0.32 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.31 |
| [[skill-builder]] | related | 0.31 |
| [[p03_ins_skill_builder]] | upstream | 0.30 |
| [[p01_kc_skill]] | related | 0.29 |
| [[bld_output_template_skill]] | downstream | 0.26 |
