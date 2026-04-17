---
id: p11_lr_n04_knowledge
kind: learning_record
pillar: P11
nucleus: n04
title: "Learning Record -- N04 Knowledge Nucleus"
version: "1.0.0"
quality: null
tags: [learning_record, n04, knowledge, rag, retrieval, P11]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Persistent learning record for N04: what has been learned from sessions, what source each insight came from, and how that learning changed N04 behavior. Append-only log -- never delete entries."
density_score: null
---

# Learning Record: N04 Knowledge Nucleus

## About This File

Append-only learning journal. Each session that produces a learning appends an entry.
N04 reads this at session start to avoid re-learning what it already knows.
`cex_memory_update.py` manages freshness decay and archive.

---

## Learning Log

### 2026-04-17 | SELF_ASSEMBLY W1

**Mission**: Portfolio Construction -- build missing artifacts across P06, P10, P11, P04, P07, P12, P02

**Learnings**:

1. **P10 was the largest gap** (8 artifacts vs. 18+ target). Memory architecture is what separates
   a knowledge BASE from a knowledge SYSTEM. N04 had knowledge but not memory infrastructure.
   - Impact: built 6 P10 artifacts in this session (memory_architecture, consolidation_policy,
     procedural_memory, memory_summary, entity_memory, memory_scope, memory_type, memory_benchmark)

2. **P06 gap was blocking** (0 proper input_schema/api_reference/type_def). Without typed contracts,
   retrieval requests were untyped and the RAG pipeline had no schema enforcement at boundaries.
   - Impact: built 3 P06 artifacts establishing the knowledge query contract

3. **Document type taxonomy was implicit, not explicit**. N04 had been treating all documents
   the same (embedding each as text) without differentiating type-specific strategies.
   type_def_document_types.md makes chunking and retrieval behavior per type explicit.
   - Impact: type_def built; chunk strategies now mapped per type

4. **Procedural memory must be explicit for SOPs to be reproducible**. N04 had knowledge of HOW
   to do things but it was scattered across multiple files. Consolidating into SOPs
   makes the procedures reliable and version-controlled.
   - Impact: procedural_memory_n04.md built with 7 SOPs

5. **Self-improvement loop was missing from P11**. Without it, N04 could not evolve its own
   knowledge quality autonomously. The loop closes the feedback cycle.
   - Impact: self_improvement_loop_n04.md built this session

**Sources**: n04_task.md handoff, spec_nucleus_self_assembly.md, N04 prior session history

**Artifacts produced**: 17+ files across P01, P02, P04, P06, P07, P10, P11, P12

---

## Learning Template (for future entries)

```markdown
### {date} | {session_type}

**Mission**: brief description

**Learnings**:
1. **{finding title}**: {description}
   - Impact: {how behavior changed}

**Sources**: {files, sessions, or tools that informed the learning}
**Artifacts produced**: {list}
```

---

## Aggregate Insights (cross-session synthesis)

| Domain | Insight | First Learned | Confidence |
|--------|---------|--------------|-----------|
| Retrieval | Hybrid beats dense-only by +12% MRR | session ~2026-04-07 | HIGH |
| Memory | P10 is the most under-built pillar in all nuclei | 2026-04-17 | HIGH |
| Architecture | Memory types (correction/preference/convention/context) cleanly partition all learnings | 2026-04-17 | HIGH |
| Quality | KC whole-document embedding outperforms chunk-based for docs < 8KB | session ~2026-04-14 | MEDIUM |
| Tooling | cex_retriever.py TF-IDF fallback is always reliable (no external deps) | early sessions | HIGH |
