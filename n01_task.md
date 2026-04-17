---
mission: VERTICAL_DENSIFICATION
nucleus: n01
wave: W2
created: 2026-04-17
priority: HIGH
effort: opus_high
---

# N01 VERTICAL_DENSIFICATION W2: Karpathy Quality Sweep + Cross-Synthesis

## SPEC REFERENCE
Read first: `_docs/specs/spec_vertical_densification.md`
Your wave: W2 (parallel with N02-N06)

## TASK 1: Karpathy Sweep -- 162 quality:null artifacts in N01_intelligence/

The Karpathy loop: for each quality:null artifact, score it, improve if < 8.5, keep if >= 8.5.

```bash
# Run heuristic sweep first (free, no LLM tokens):
python _tools/cex_evolve.py sweep --nucleus n01 --target 8.5 --max-rounds 1 --mode heuristic

# Check what's still below 8.5 after heuristic:
python _tools/cex_score.py --nucleus n01 --show-below 8.5 | head -30

# For stubborn artifacts (still null or < 7.0), agent mode on worst 20:
python _tools/cex_evolve.py sweep --nucleus n01 --target 8.5 --max-rounds 2 --mode agent --limit 20
```

## TASK 2: Cross-Nucleus Synthesis -- Knowledge Graph + Ontology

N01 is the intelligence nucleus. You have the broadest cross-domain view.
After the quality sweep, create 2 synthesis artifacts that distill patterns
found ACROSS multiple nuclei's KCs into reusable inference-ready structures.

### Artifact 1: knowledge_graph_cex_taxonomy.md
Save: `N01_intelligence/P10_memory/knowledge_graph_cex_taxonomy.md`
Kind: knowledge_graph
Content: CEX taxonomy as a knowledge graph -- 257 kinds, 12 pillars, 8 nuclei as nodes;
edges = dependency (kind A requires kind B), co-occurrence (kinds built together),
and pillar membership. Use adjacency list or edge table format (no invented tools).
Source: `.cex/kinds_meta.json` + your own artifact scan.

### Artifact 2: ontology_cex_vocabulary.md
Save: `N01_intelligence/P01_knowledge/ontology_cex_vocabulary.md`
Kind: knowledge_card (type: ontology)
Content: formal ontology of CEX domain -- classes (kind, pillar, nucleus, pipeline),
properties (quality, density, pillar_code), relationships (produces, governs, routes_to).
Map each class to its industry equivalent (OWL/RDF terms where applicable).
Source: ubiquitous-language.md + kc_{domain}_vocabulary.md files across all nuclei.

## COMPLETION SEQUENCE

```bash
python _tools/cex_compile.py --all
git add N01_intelligence/ && git commit -m "[N01] VERTICAL_DENSIFICATION W2: quality sweep 162 artifacts + knowledge_graph + ontology"
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'vert_dens_w2_complete', 9.0)"
```

## COMPLETION CRITERIA
- [ ] cex_evolve.py sweep completed on N01_intelligence/ (all artifacts scored)
- [ ] quality:null count in N01_intelligence/ reduced by >= 80%
- [ ] knowledge_graph_cex_taxonomy.md created with >= 50 nodes
- [ ] ontology_cex_vocabulary.md created with >= 3 classes, >= 10 properties
- [ ] signal sent: n01 -> vert_dens_w2_complete
