---
quality: 8.8
quality: 8.2
id: p01_kc_llm_wiki
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "LLM Wiki -- Self-Maintaining Knowledge Base Pattern"
version: 1.0.0
created: "2026-04-20"
updated: "2026-04-20"
author: n04_knowledge
domain: knowledge_graph
tags: [llm-wiki, karpathy, knowledge-base, self-maintaining, wiki, ingest, summarize]
tldr: "Karpathy's LLM Wiki pattern: ingest source -> summarize -> update 10-15 related pages -> query interface -> lint for contradictions. CEX is the fullest implementation: 293 kinds, 6000+ artifacts, 12-pillar schema, 8F editorial pipeline, cross-reference graph, and autoresearch evolution loop."
when_to_use: "Designing knowledge management systems, building RAG architectures, or reasoning about how CEX compares to traditional wikis and knowledge bases"
keywords: [llm-wiki, knowledge-base, ingest, summarize, update, query, lint, self-maintaining]
density_score: 0.94
related:
  - p01_kc_cross_reference
  - p01_kc_autoresearch
  - p01_kc_autoresearch_loop
  - p01_kc_knowledge_card
  - p01_kc_knowledge_distillation
  - p01_kc_universal_llm
  - p01_kc_memory_management
  - skill_cross_reference
  - p01_kc_rag_source
  - p01_kc_pattern_extraction
---

# LLM Wiki

## Origin

Andrej Karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): a knowledge base where the LLM does not just retrieve information but actively maintains it -- ingesting new sources, summarizing, updating related pages, and linting for contradictions.

## 5-Stage Pipeline

| Stage | Action | Input | Output |
|-------|--------|-------|--------|
| 1. Ingest | Absorb new source material | URL, PDF, paper, conversation | Raw extracted text |
| 2. Summarize | Distill into structured knowledge | Raw text | New or updated wiki page |
| 3. Update | Modify 10-15 related pages | New page + graph edges | Updated neighbors |
| 4. Query | Answer questions from wiki state | User question | Grounded answer with citations |
| 5. Lint | Detect contradictions and stale claims | Full wiki scan | Contradiction report |

## CEX as LLM Wiki

CEX is not inspired by the LLM Wiki pattern -- it IS the pattern at production scale.

| LLM Wiki Concept | CEX Implementation | Scale |
|------------------|--------------------|-------|
| Wiki page | knowledge_card (.md with frontmatter) | 6000+ artifacts |
| Page schema | 12 pillar schemas (P01-P12) | 293 kinds |
| Ingest | 8F pipeline F3 INJECT | Auto on every build |
| Summarize | 8F pipeline F6 PRODUCE | Density-gated (>0.85) |
| Update 10-15 related | cex_ripple.py (post-save hook) | Spec (W4) |
| Query | cex_retriever.py (TF-IDF) | 2184 docs, 12K vocab |
| Lint | cex_semantic_lint.py | Spec (W4) |
| Graph edges | `related:` frontmatter field | 3-15 per artifact |
| Navigation | Obsidian vault + dataview dashboards | Graph view |
| Quality control | cex_score.py + S_RELATED gate | 3-layer scoring |
| Evolution | cex_evolve.py (autoresearch loop) | Overnight batch |

## Key Distinction from Traditional Wikis

| Dimension | Traditional Wiki | LLM Wiki (CEX) |
|-----------|-----------------|-----------------|
| Editor | Human writes/edits | LLM produces via 8F pipeline |
| Structure | Freeform prose | Typed artifacts (293 kinds x 12 pillars) |
| Quality | Peer review (human) | Automated scoring + quality gates |
| Cross-refs | Manual hyperlinks | Auto-populated (cex_wikilink.py) |
| Consistency | Manual enforcement | Semantic lint (contradiction detection) |
| Evolution | Stagnates without editors | Autonomous improvement (cex_evolve.py) |
| Navigation | Search + categories | Graph view + dataview + TF-IDF retrieval |

## Key Distinction from RAG

| Dimension | Standard RAG | LLM Wiki (CEX) |
|-----------|-------------|-----------------|
| Knowledge unit | Unstructured chunk | Typed artifact with schema |
| Ingestion | Chunk + embed | 8F pipeline (constrain -> produce -> govern) |
| Retrieval | Vector similarity | TF-IDF + cross-ref graph traversal |
| Freshness | Re-embed on change | Ripple propagation (10-15 neighbors) |
| Quality | None (all chunks equal) | 3-layer scoring (structural + rubric + semantic) |
| Maintenance | Manual re-indexing | Autoresearch loop + semantic lint |

## The Compound Loop

```
Source ingested -> 8F pipeline -> new artifact with related: edges
  -> cex_ripple.py fires -> 10-15 neighbors updated
    -> cex_semantic_lint.py detects contradictions -> flagged for resolution
      -> cex_evolve.py --cluster -> related artifacts improve together
        -> cex_retriever.py serves better answers
          -> next ingest benefits from richer context
            -> REPEAT (knowledge compounds exponentially)
```

## Design Principles

| Principle | Rationale |
|-----------|-----------|
| Typed over freeform | Schema enforcement prevents drift; LLMs produce more consistent output with constraints |
| Dense over verbose | Token budget is finite; every sentence must carry non-obvious information (density > 0.85) |
| Connected over isolated | Cross-refs enable graph traversal, cluster evolution, and contradiction detection |
| Scored over unscored | Quality gates prevent regression; evolution loop has a clear optimization target |
| Autonomous over manual | Overnight loops improve artifacts without human intervention |

## Anti-Patterns

| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| Flat file dump (no schema) | No quality enforcement, retrieval noise | Use 293-kind taxonomy with pillar schemas |
| No cross-references | Knowledge stays siloed, contradictions go undetected | Wire related: field (3-15 per artifact) |
| No quality gate | Low-quality pages dilute retrieval | S_RELATED + 3-layer scoring |
| No evolution loop | Wiki stagnates after initial creation | cex_evolve.py overnight runs |
| Human-only editing | Bottleneck at human throughput | LLM produces, human governs (GDP) |

## Industry Mapping

| LLM Wiki | Industry Equivalent | Domain |
|----------|-------------------|--------|
| Typed wiki page | Entity in knowledge graph | Semantic web (RDF, OWL) |
| `related:` field | Edge / triple | Graph database (Neo4j, Wikidata) |
| cex_ripple.py | Change data capture + propagation | Event sourcing |
| cex_semantic_lint.py | Consistency checker | Knowledge graph validation (SHACL) |
| cex_evolve.py | Autonomous agent loop | AutoGPT, BabyAGI lineage |
| Obsidian vault | Graph-based note system | Zettelkasten method |
| Quality scoring | Content quality assessment | Wikipedia FA/GA criteria |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cross_reference]] | sibling | 0.40 |
| [[p01_kc_autoresearch]] | sibling | 0.38 |
| [[p01_kc_autoresearch_loop]] | upstream | 0.36 |
| [[p01_kc_knowledge_card]] | upstream | 0.34 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.31 |
| [[p01_kc_universal_llm]] | sibling | 0.30 |
| [[p01_kc_memory_management]] | sibling | 0.28 |
| [[skill_cross_reference]] | upstream | 0.27 |
| [[p01_kc_rag_source]] | sibling | 0.25 |
| [[p01_kc_pattern_extraction]] | sibling | 0.24 |
