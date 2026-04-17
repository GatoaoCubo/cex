---
mission: VERTICAL_DENSIFICATION
nucleus: n04
wave: W2
created: 2026-04-17
priority: HIGH
effort: opus_high
---

# N04 VERTICAL_DENSIFICATION W2: Karpathy Quality Sweep + Cross-Synthesis

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W2 (parallel with N01-N03, N05-N06)

## TASK 1: Karpathy Sweep -- 117 quality:null artifacts in N04_knowledge/

Knowledge Gluttony lens: every artifact must hold genuine epistemic value -- not just
exist, but contribute to the knowledge retrieval surface.

```bash
# Heuristic pass:
python _tools/cex_evolve.py sweep --nucleus n04 --target 8.5 --max-rounds 1 --mode heuristic

# Agent pass on worst 20:
python _tools/cex_evolve.py sweep --nucleus n04 --target 8.5 --max-rounds 2 --mode agent --limit 20
```

## TASK 2: Cross-Nucleus Knowledge Synthesis

N04 is the knowledge management nucleus. Your job in W2 is to synthesize
the controlled vocabularies planted by all 6 nuclei in SELF_ASSEMBLY into
a unified, portable mental model artifact.

### Artifact 1: mental_model_cex_architecture.md
Save: `N04_knowledge/P01_knowledge/mental_model_cex_architecture.md`
Kind: mental_model
Content: CEX architecture as a mental model -- the key analogy, the primary
components, how they relate, and how to reason about the system. Target audience:
any LLM or engineer who encounters CEX for the first time. Must convey:
- The factory floor metaphor (8F x 12 pillars x 257 kinds)
- The nucleus sin-lens system
- The CoC principle (N00_genesis as archetype mold)
- The ubiquitous language layer (L0/L1/L2 transmutation pipeline)
Source: CLAUDE.md + .claude/rules/ubiquitous-language.md + all kc_*_vocabulary.md files

### Artifact 2: few_shot_examples_rag_queries.md
Save: `N04_knowledge/P01_knowledge/few_shot_examples_rag_queries.md`
Kind: knowledge_card (type: few_shot_examples)
Content: 5 complete RAG query examples showing how N04 handles retrieval:
  1. "find all quality_gate artifacts" -- semantic search trace
  2. "which nuclei cover P06 schema?" -- cross-nucleus query
  3. "what kind handles pricing?" -- intent resolution -> kind lookup
  4. "show me 8F examples" -- few-shot retrieval pattern
  5. "find artifacts below 8.0 in N03" -- quality-filtered query
Source: N04_knowledge/P04_tools/ + N04_knowledge/P06_schema/ artifacts

## COMPLETION SEQUENCE

```bash
python _tools/cex_compile.py --all
git add N04_knowledge/ && git commit -m "[N04] VERTICAL_DENSIFICATION W2: quality sweep 117 artifacts + mental model + RAG few-shots"
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'vert_dens_w2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] cex_evolve.py sweep completed on N04_knowledge/
- [ ] quality:null reduced >= 80%
- [ ] mental_model_cex_architecture.md created
- [ ] few_shot_examples_rag_queries.md created
- [ ] signal sent: n04 -> vert_dens_w2_complete
