---
id: kno_chunk_strategy_n05
kind: chunk_strategy
pillar: P01
nucleus: N05
title: "N05 Operations Chunk Strategy"
version: "1.0.0"
quality: null
tags: [n05, operations, chunk_strategy, gating_wrath, rag, ci_cd, deploy]
---
<!-- 8F: F1=chunk_strategy/P01 F2=chunk-strategy-builder F3=nucleus_def_n05+P01_schema+kc_chunk_strategy+N05_W1+examples F4=hybrid fail_closed ops chunking
     F5=shell+apply_patch+cex_compile F6=approx-6KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/P01_knowledge/kno_chunk_strategy_n05.md -->

# N05 Operations Chunk Strategy

## Intent

This chunk strategy defines how N05 indexes operations knowledge without losing the evidence chain that matters during code review, CI triage, release gating, deploy recovery, and post-incident analysis.

The Gating Wrath lens changes the default chunking stance:

- preserve decision-critical evidence before narrative filler
- fail closed on malformed inputs instead of producing noisy chunks
- separate durable policy from volatile runtime output
- keep retrieval units small enough to cite, large enough to hold a complete failure

## Properties

| Property | Value |
|----------|-------|
| Kind | `chunk_strategy` |
| Pillar | `P01` |
| Nucleus | `N05` |
| Primary domain | `code review, testing, CI/CD, deploy` |
| Method | `structure_aware_recursive` |
| Default chunk size | `700 tokens` |
| Default overlap | `120 tokens` |
| Log mode | `event_bounded` |
| Failure stance | `fail_closed` |

## Operational Scope

The corpus is not generic prose. N05 stores mixed operational evidence:

- runbooks and deploy checklists
- CI logs and test failures
- incident timelines and rollback notes
- quality gate definitions
- schema and config contracts from Wave 1
- memory summaries and learning records about repeated breakpoints

Each class needs a different boundary rule because operations retrieval fails when a stack trace is split from its triggering command, or when a rollback rule is merged with unrelated background text.

## Strategy Table

| Source class | Target size | Overlap | Split anchors | Guardrail |
|--------------|-------------|---------|---------------|-----------|
| runbook | 700 | 120 | headings, lists, code fences | never split numbered procedure mid-step |
| checklist | 450 | 80 | heading, checklist item groups | keep pass/fail gate with rationale |
| CI log | 320 | 40 | timestamp, job section, traceback start | keep full failure event intact |
| test output | 380 | 60 | test case, assertion, traceback | keep assertion plus expected/actual together |
| deploy log | 420 | 60 | phase marker, health check marker | keep deploy phase and verdict together |
| schema/config | 600 | 100 | heading, table, yaml block | keep field definition with boundary notes |
| incident report | 750 | 140 | timeline block, action block | keep cause, impact, mitigation together |
| memory artifact | 500 | 80 | section header | keep one retrieval decision per chunk |

## Gating Wrath Rules

The N05 lens adds hard gates beyond ordinary recursive chunking:

1. A chunk may not contain more than one deploy verdict.
2. A traceback may not be split across chunks unless it exceeds the emergency cap.
3. A checklist chunk must preserve the gate name, condition, and failure action together.
4. A chunk that loses its source file, line span, or timestamp metadata is discarded.
5. Narrative explanation never outranks evidence blocks during boundary selection.

These rules matter because release gating depends on auditable evidence, not on approximate summaries.

## Boundary Heuristics

Use this boundary order:

1. major heading
2. subheading
3. fenced code block
4. traceback block
5. checklist cluster
6. blank line
7. sentence

If a document includes both prose and machine output, split at the seam and index them as separate logical units with shared source metadata.

## Log Handling

Operational logs are noisy. N05 should not chunk them like markdown essays.

Required behavior:

- detect repeated boilerplate lines and compress them into metadata counts
- preserve the first error, last retry, and final verdict as separate evidence chunks
- keep timestamps and job names in every derived chunk
- stop ingest if log encoding is broken or line order cannot be trusted

Emergency cap:

- max chunk size for logs: `1200 tokens`
- if a single traceback exceeds the cap, emit one oversize chunk flagged `oversize_evidence=true`
- do not split the traceback into semantically meaningless fragments

## Metadata Contract

Every chunk must carry these fields in the ingest layer even if the markdown body does not show them inline:

- `source_path`
- `source_kind`
- `pillar`
- `nucleus`
- `document_class`
- `chunk_index`
- `total_chunks`
- `heading_context`
- `evidence_type`
- `ts_start`
- `ts_end`

Without this contract, N05 cannot filter retrieval to the failing job, relevant pillar, or most recent deploy window.

## Retrieval Implications

This strategy is tuned for downstream hybrid retrieval:

- BM25 benefits from preserved commands, error strings, test names, and env keys
- dense retrieval benefits from intact causal narratives and rollback notes
- rerankers benefit when each chunk contains one operational event, not a mixed transcript

The strategy deliberately avoids giant context slabs because those bury the gating signal.

## Failure Modes

| Failure mode | Symptom | Countermeasure |
|--------------|---------|----------------|
| overlarge policy chunk | retriever returns broad handbook instead of exact gate | split by section and table block |
| oversplit log | missing root cause in retrieval | event-bounded stitching with timestamp anchors |
| mixed evidence and commentary | reranker prefers polished prose | prioritize evidence-first chunk order |
| stale chunk metadata | wrong deploy cited | freshness stamp and source hash required |
| code fence split | unusable command snippet | code fence treated as atomic unit |

## Validation Checklist

- chunk size stays near target for the source class
- overlap is present but does not duplicate whole events
- evidence blocks remain self-contained
- one chunk maps to one operational decision whenever possible
- malformed logs are rejected rather than guessed
- chunks preserve the exact strings operators grep for during incidents

## Default Decision

Adopt `structure_aware_recursive` for policy and runbook content, with `event_bounded` overrides for logs and test output.

This is the right default for N05 because operations retrieval serves a gatekeeper role. The system should return the precise failing proof, the relevant procedure, and the exact rollback trigger, not a fuzzy thematic summary.

## Related N05 Artifacts

- `kno_embedder_provider_n05.md` encodes the resulting chunks
- `kno_retriever_config_n05.md` searches them with strict filters
- `kno_vector_store_n05.md` persists them in an auditable store
- `mem_knowledge_index_n05.md` governs refresh and hybrid ranking
- `mem_learning_record_n05.md` captures where chunk boundaries helped or hurt
