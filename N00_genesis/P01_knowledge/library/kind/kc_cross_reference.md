---
quality: 8.8
quality: 8.2
id: p01_kc_cross_reference
kind: knowledge_card
type: domain
pillar: P01
title: "Cross-Reference Wiring -- Knowledge Graph Edges for Artifact Compounding"
version: 1.0.0
created: "2026-04-20"
updated: "2026-04-20"
author: n04_knowledge
domain: knowledge_graph
tags: [cross-reference, wikilinks, knowledge-graph, related, compounding, karpathy]
tldr: "Every artifact declares its neighbors via a related: frontmatter field (3-15 IDs) + ## Related Artifacts body section. Auto-populated by cex_wikilink.py, enforced by S_RELATED gate, propagated by cex_ripple.py. Transforms 6000+ isolated files into a connected knowledge graph."
when_to_use: "Producing, reviewing, or wiring any CEX artifact -- cross-refs are mandatory at F6 PRODUCE"
keywords: [cross-reference, related, wikilink, backlink, knowledge-graph, compounding, ripple]
density_score: 0.95
related:
  - p01_kc_autoresearch_loop
  - p01_kc_llm_wiki
  - skill_cross_reference
  - p01_kc_knowledge_card
  - p01_kc_knowledge_distillation
  - dash_orphan_detector
  - p01_kc_gap_detection
  - bld_collaboration_knowledge_card
  - p01_kc_autoresearch
  - dash_cross_ref_health
---

# Cross-Reference Wiring

## The Problem

6000+ artifacts with zero systematic links. Each artifact is a dot. Dots accumulate; knowledge does not. A knowledge card cited from 15 directions becomes canonical and stops being rewritten from scratch. An isolated card rots.

## The Solution: `related:` Field

Every CEX artifact carries a `related:` frontmatter field -- a list of artifact IDs representing graph edges.

```yaml
related:
  - p01_kc_rag_patterns          # upstream: knowledge this artifact consumes
  - p03_pt_retrieval_query        # downstream: artifacts that consume this one
  - p10_ki_faiss_index            # sibling: same domain, different scope
  - p04_search_tavily             # alternative: different kind, overlapping use case
```

Schema spec: `N00_genesis/P{01-12}/_schema.yaml` -- `frontmatter_cex.related` (all 12 pillars).

## Relationship Types

| Type | Direction | Meaning | Example |
|------|-----------|---------|---------|
| upstream | A consumes B | Input dependency | knowledge_card feeds prompt_template |
| downstream | A produces for B | Output consumer | prompt_template feeds system_prompt |
| sibling | Peer | Same kind, same domain, different scope | Two KCs on competing RAG strategies |
| alternative | Substitutable | Different kind, overlapping use case | retriever vs search_tool |
| supersedes | Replaces | New version replaces old | v2 KC replacing v1 |

## Quantity Targets

| Kind Category | Target | Min | Max |
|---------------|--------|-----|-----|
| knowledge_card | 8-10 | 3 | 15 |
| agent, agent_card | 8-12 | 5 | 15 |
| prompt_template, system_prompt | 5-8 | 3 | 15 |
| orchestration (workflow, handoff) | 6-10 | 3 | 15 |
| config kinds (env_config, secret_config) | 3-5 | 1 | 10 |
| eval kinds (unit_eval, benchmark) | 4-6 | 2 | 12 |

## Tool Chain

| Tool | Function | Status |
|------|----------|--------|
| `cex_wikilink.py` | Auto-populate related: via TF-IDF similarity | Deployed |
| `cex_ripple.py` | Propagate changes to related artifacts on save | Spec (W4) |
| `cex_semantic_lint.py` | Detect contradictions, stale refs, orphans | Spec (W4) |
| `cex_retriever.py` | TF-IDF similarity engine (2184 docs, 12K vocab) | Deployed |

### cex_wikilink.py Usage

```bash
python _tools/cex_wikilink.py --sweep --dry-run          # preview
python _tools/cex_wikilink.py --sweep --apply --max-refs 10  # apply
python _tools/cex_wikilink.py --path N01_intelligence/P01_knowledge/kc_competitor.md  # single
```

Auto-populated entries are tagged `# auto` for curator review.

## Quality Gate: S_RELATED

Soft gate in F7 GOVERN (penalty, not blocker):

| Check | Result | Penalty |
|-------|--------|---------|
| `related:` field populated (3+ entries) | PASS/WARN | -0.3 if empty |
| `## Related Artifacts` section in body | PASS/FAIL | -0.2 if absent |
| At least 1 upstream reference | PASS/WARN | informational |
| At least 1 downstream reference | PASS/WARN | informational |

Penalties do not stack below 8.0 quality floor.

## 8F Integration

Cross-refs activate at two pipeline stages:

| Stage | Action |
|-------|--------|
| F6 PRODUCE | Builder injects `## Related Artifacts` section using skill_cross_reference.md |
| F7 GOVERN | S_RELATED gate validates related: field populated |

## Industry Mapping

| CEX Concept | Industry Term | Framework |
|-------------|--------------|-----------|
| `related:` field | Edge list / adjacency list | Graph theory |
| `## Related Artifacts` | Backlinks panel | Obsidian, Notion, Roam |
| `[[wikilink]]` | Bidirectional link | Wiki systems |
| cex_wikilink.py | Link suggestion engine | Obsidian, Logseq |
| cex_ripple.py | Change propagation | Event sourcing, CQRS |
| S_RELATED gate | Link density metric | Knowledge graph quality |

## The Compounding Effect

```
Artifact created -> related: populated (3-15 edges)
  -> Save triggers cex_ripple.py -> 10-15 neighbors updated
    -> Overnight cex_evolve.py --cluster -> related artifacts improve together
      -> Obsidian graph shows new connections
        -> Next artifact benefits from denser neighborhood
```

Isolated knowledge decays. Connected knowledge compounds. Cross-reference wiring is the mechanism that converts CEX from a file collection into a knowledge graph.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_autoresearch_loop]] | sibling | 0.41 |
| [[p01_kc_llm_wiki]] | sibling | 0.40 |
| [[skill_cross_reference]] | upstream | 0.38 |
| [[p01_kc_knowledge_card]] | upstream | 0.35 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.32 |
| [[dash_orphan_detector]] | downstream | 0.30 |
| [[p01_kc_gap_detection]] | sibling | 0.28 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.27 |
| [[p01_kc_autoresearch]] | sibling | 0.26 |
| [[dash_cross_ref_health]] | downstream | 0.25 |
