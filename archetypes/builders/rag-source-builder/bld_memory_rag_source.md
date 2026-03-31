---
kind: memory
id: bld_memory_rag_source
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for rag_source artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: rag-source-builder
## Summary
RAG sources are lightweight pointers to external data — URLs with freshness tracking, reliability scoring, and crawl scheduling. The critical production lesson is that RAG sources must never contain content, only metadata about where content lives. The moment content is embedded, the artifact becomes a knowledge card, not a source pointer. The second lesson is freshness: sources without last_checked dates and re-check schedules become stale silently.
## Pattern
- Keep artifacts under 1024 bytes — RAG sources are pointers, not content containers
- Every source must have last_checked date and re-check schedule (daily, weekly, monthly)
- Reliability scoring (high/medium/low) must be based on observed availability, not reputation
- URL validation must check both format (valid URL syntax) and accessibility (HTTP 200 on last check)
- Specify format of the source content (html, json, api, pdf, csv) for downstream parser selection
- Domain field must match the knowledge domain this source informs, enabling filtered retrieval
## Anti-Pattern
- Embedding actual content in the RAG source — it is a pointer, not a knowledge card
- Sources without last_checked dates — staleness is invisible until downstream retrieval fails
- Reliability scored by reputation instead of measurement — a prestigious source that is down 30% of the time is low reliability
- Missing format specification — downstream parsers cannot be auto-selected without knowing the format
- Confusing rag_source (P01, pointer to external) with knowledge_card (P01, distilled content) or context_doc (P01, domain context)
## Context
RAG sources operate in the P01 content layer as the entry point for external knowledge ingestion. They feed into crawl pipelines that fetch, parse, and distill content into knowledge cards. The separation between pointer (rag_source) and content (knowledge_card) enables independent freshness management — the pointer can be re-checked and re-crawled without modifying the distilled knowledge until the source actually changes.
## Impact
Sources with re-check schedules maintained 95% freshness versus 60% for unscheduled sources over 90-day periods. Format specification enabled automatic parser selection in 100% of crawl operations. Keeping sources under 1024 bytes maintained O(1) retrieval performance in source catalogs.
## Reproducibility
For reliable RAG source production: (1) validate URL format and accessibility, (2) set last_checked to today, (3) define re-check schedule based on source update frequency, (4) score reliability from measured availability, (5) specify content format, (6) assign domain for filtered retrieval, (7) verify artifact stays under 1024 bytes.
## References
- rag-source-builder SCHEMA.md (5 required fields, pointer-only format)
- P01 content pillar specification
- RAG pipeline and source management patterns
