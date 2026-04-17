---
id: p10_msc_n04_knowledge
kind: memory_scope
pillar: P10
nucleus: n04
title: "Memory Scope -- N04 Context Boundary Definitions"
version: "1.0.0"
quality: 9.1
tags: [memory_scope, n04, context_boundary, working_memory, session, P10]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Defines the scope boundaries for each N04 memory layer: what enters working memory, what qualifies for episodic storage, what belongs in the semantic corpus, and what never enters any memory layer."
density_score: null
---

# Memory Scope: N04 Context Boundary Definitions

## Purpose

Memory scope prevents working memory bloat, episodic noise, and semantic corpus pollution.
Every piece of information has a place -- or no place at all.

---

## Working Memory Scope

**Definition**: information held in the active context window for the current session.

### ALWAYS included at session start
- N04 identity: `nucleus_def_n04.md` (P08)
- Active handoff: `n04_task.md` or most recent handoff
- Procedural memory: `procedural_memory_n04.md` (P10) -- top 3 SOPs relevant to task
- Brand context: `.cex/brand/brand_config.yaml` (if bootstrapped)

### Loaded on demand (F3 INJECT)
- Relevant KCs (top 5 by semantic similarity to task)
- Builder ISOs for the target kind (13 files per builder)
- Examples from compiled/ matching the target kind
- Entity memory for entities explicitly mentioned in task

### NEVER in working memory
- Full P01_knowledge/ directory (2184+ documents -- too large)
- Session history beyond the current session
- Binary files, images, compiled YAML (source .md is canonical)
- Audit logs, git history (use Bash tool to fetch on demand)

### Overflow protocol
When context > 80% full:
1. Identify least-recently-accessed context chunks (LRU)
2. Compress each to 1-sentence summary + source path
3. Store compressed summaries in episodic layer
4. Keep: task context, current artifact draft, active tool results

---

## Episodic Memory Scope

**Definition**: per-session compressed records stored in pgvector `session_memory`.

### ALWAYS stored after session
- Session summary (memory_summary_n04.md format)
- Learning record entries for this session
- Any decisions made during session (GDP outcomes)

### Conditionally stored
- Interesting retrieval patterns: queries that surprised N04 (unexpected results)
- New entity discoveries not yet in entity_memory_n04.md
- Quality gate failures and their resolutions

### NEVER in episodic
- Full tool outputs (too large, store only findings)
- Intermediate drafts (only final saved artifacts)
- Repeated routine operations (SOP execution without novel findings)
- Conversation pleasantries, meta-commentary

---

## Semantic Corpus Scope

**Definition**: permanent indexed knowledge in pgvector `cex_artifacts` and `external_docs`.

### ALWAYS indexed
- All KCs after compilation (via post-compile hook)
- All CEX artifacts with frontmatter (kind, pillar, nucleus present)
- External documents explicitly ingested via RAG source workflow

### Conditionally indexed
- Long-form context docs (>512 tokens): chunk then index
- External web pages: only if trust_level >= 3
- PDFs: only if extracted text quality >= 0.7 (no garbled OCR)

### NEVER indexed
- Private/confidential documents (no brand secrets in shared corpus)
- Low-quality drafts (quality < 7.0 if known)
- Temporary files (session outputs, debug logs)
- Duplicate content (deduplication check before index)

---

## Procedural Memory Scope

**Definition**: stable SOPs stored as Markdown files in P10_memory/.

### Criteria for procedural storage
1. Operation performed >= 3 times in sessions
2. Has a reproducible step sequence (not ad-hoc judgment)
3. N04 is the primary actor (not a procedure for N07 or N03)
4. Steps are stable (unlikely to change within 3 months)

### Not procedural (use other memory types)
- One-time configurations -> episodic
- Facts about systems -> semantic (KC or entity_memory)
- Decisions with rationale -> decision_manifest.yaml

---

## Boundary Violations (Anti-Patterns)

| Anti-Pattern | Problem | Correct Action |
|-------------|---------|---------------|
| Loading all P01 KCs into context | Burns 100K+ tokens, most irrelevant | Use semantic search (top-5 by similarity) |
| Storing debug output in episodic | Noise, no learning value | Discard; only store resolutions |
| Indexing uncompiled drafts | Stale content in corpus | Compile first, then index |
| Keeping full session in working memory | Context bloat | Compress at 80% threshold |
| Treating entity_memory as KC | Wrong layer | Entity memory = tracker, KC = definition |
