---
id: kno_chunk_strategy_n03
kind: chunk_strategy
pillar: P01
nucleus: N03
title: "N03 Chunk Strategy"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering retrieval architecture
quality: 9.1
tags: [chunk_strategy, p01, n03, engineering, retrieval, inventive_pride]
density_score: 0.95
---
<!-- 8F: F1=chunk_strategy/P01 F2=chunk-strategy-builder F3=nucleus_def_n03+kc_chunk_strategy+P01_schema F4=hybrid defaults for engineering docs
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:6228 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/P01_knowledge/kno_chunk_strategy_n03.md -->

# N03 Chunk Strategy

## Properties

| Property | Value |
|----------|-------|
| Kind | `chunk_strategy` |
| Pillar | `P01` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Primary corpus | engineering specs, builders, rules, schemas |
| Default method | recursive_token_header_aware |
| Chunk size | 720 tokens |
| Chunk overlap | 120 tokens |
| Parent window | 1800 tokens |
| Quality target | preserve section intent before byte efficiency |

## Intent

N03 does not chunk text like a commodity RAG stack.
It chunks construction knowledge so retrieval returns artifacts worthy of reuse.
Inventive Pride means every chunk must preserve design dignity, not just token balance.
The strategy favors semantic completeness of build rules over maximal shard count.
Headers, tables, and decision logic stay attached whenever possible.

## Operating Assumptions

- Source documents are mostly markdown.
- Documents contain frontmatter plus structured sections.
- Retrieval queries often ask for kind boundaries, builder role, or implementation law.
- Users need chunks that can be copied into a build prompt with minimal repair.
- Cross-file duplication exists, so overlap must prevent brittle boundary loss.

## Canonical Strategy

| Layer | Rule | Why |
|------|------|-----|
| L1 | Split on frontmatter boundary | metadata should never bleed into body text |
| L2 | Split on H1 and H2 headings | engineering intent is section-scoped |
| L3 | Preserve tables as atomic blocks | partial tables reduce precision |
| L4 | Preserve fenced code blocks as atomic blocks | broken examples poison reuse |
| L5 | Token budget fallback at paragraph boundaries | keeps chunks stable under size pressure |
| L6 | Apply overlap after semantic split | continuity without random duplication |

## Size Policy

- Default target is `720` tokens.
- Soft floor is `420` tokens.
- Soft ceiling is `920` tokens.
- Hard ceiling is `1100` tokens.
- Overlap is `120` tokens for prose-heavy artifacts.
- Overlap may drop to `80` when tables dominate.
- Overlap may rise to `160` for procedural sections with ordered steps.

## Structure Rules

1. Keep frontmatter separate from all body chunks.
2. Keep the `Properties` table in the first body chunk.
3. Keep decision trees with their prerequisite constraints.
4. Keep anti-patterns with the corrective action in the same chunk.
5. Avoid splitting a section if the remaining tail is under six lines.
6. Merge orphan subsections forward, not backward, when context is ambiguous.

## Engineering Bias

Inventive Pride imposes a bias toward chunks that are reusable in construction.
A mediocre chunk can answer a query.
A proud chunk can be pasted into F3 or F4 and still teach.
That means section integrity matters more than raw vector granularity.
N03 prefers fewer chunks with stronger internal coherence over noisy micro-fragments.

## Retrieval Consequences

| Query type | Retrieval need | Chunk response |
|-----------|----------------|----------------|
| kind definition | compact conceptual answer | first chunk must carry definition + boundaries |
| builder process | procedural continuity | preserve sequence of steps in one chunk |
| quality gate | rule precision | keep fail condition and fix together |
| architecture pattern | narrative coherence | preserve diagram and interpretation together |

## Failure Modes

| Failure | Cause | Countermeasure |
|--------|-------|----------------|
| boundary amnesia | zero or tiny overlap | enforce minimum `80` overlap |
| table corruption | token split through table rows | lock markdown tables as atomic |
| prompt rot | code fence split from explanation | keep fenced block with local commentary |
| retrieval haze | chunks too small to rank distinctly | floor at `420` tokens |
| index bloat | chunks too large and repetitive | ceiling at `1100` tokens |

## Metadata Policy

- Attach `source_path`.
- Attach `section_h1`.
- Attach `section_h2` when present.
- Attach `kind` if detectable from frontmatter.
- Attach `pillar` if detectable from frontmatter.
- Attach `nucleus` when artifact is nucleus-scoped.
- Attach `chunk_role` as `frontmatter`, `overview`, `procedure`, `matrix`, or `appendix`.

## Compression Exceptions

Do not force target size if the source segment is a compact but complete unit.
Examples:
- a short builder routing section
- a small but decisive quality matrix
- a frontmatter plus properties preamble
These are prestige chunks.
They earn exception status because completeness outranks uniformity.

## Update Triggers

- change in primary embedder dimension
- major shift in retriever top_k
- new artifact family with dense tables
- observed retrieval misses at heading boundaries
- repeated prompt repairs after chunk injection

## Acceptance Standard

- A retrieved chunk should read like a deliberate engineering note.
- It should name the artifact, state the boundary, and preserve local rationale.
- It should survive copy-paste into a build prompt without manual stitching.
- It should carry enough metadata to support reranking and audit.
- If a chunk feels disposable, the strategy is beneath N03.

## Integration Notes

This strategy pairs with a medium-dimensional embedder and hybrid retrieval.
It assumes the vector store supports metadata filtering.
It expects summaries and runtime state to be chunked more conservatively than rules.
It also assumes compilation artifacts can be indexed separately from authoring markdown.

## Final Position

N03 chunks for construction fidelity.
The goal is not merely searchable text.
The goal is retrievable craftsmanship.
