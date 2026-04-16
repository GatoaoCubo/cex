---
kind: tools
id: bld_tools_ontology
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for ontology artifact production
quality: 9.2
title: "Tools Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, builder, tools, P01]
tldr: "Tools for ontology production: brain_query for dedup, schema.org lookup, CEX compiler for validation."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Tools: ontology-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing ontology artifacts for the same domain | Phase 1 (check duplicates and prior art) | CONDITIONAL |
| cex_retriever.py | Find similar ontologies in compiled/ by TF-IDF similarity | Phase 1 (reuse existing class hierarchies) | AVAILABLE |
| cex_compile.py | Compile .md to .yaml for indexing | Phase 3 (post-save) | AVAILABLE |
| cex_score.py | Score artifact quality across 3 layers | Phase 3 (validation) | AVAILABLE |
| schema_org_lookup [PLANNED] | Look up schema.org class/property definitions | Phase 2 (schema.org mapping section) | [PLANNED] |
| owl_validator [PLANNED] | Check OWL axiom consistency (via Apache Jena or ROBOT) | Phase 3 (axiom validation) | [PLANNED] |
| skos_validator [PLANNED] | Validate SKOS hierarchy integrity | Phase 3 (SKOS-mode only) | [PLANNED] |

## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions, ontology kind |
| CEX Examples | P01_knowledge/compiled/ | Compiled ontology artifacts |
| CEX KC | P01_knowledge/library/kind/kc_ontology.md | Domain knowledge for ontology construction |
| kinds_meta.json | .cex/kinds_meta.json | Kind boundary, max_bytes, naming convention |
| schema.org Vocabulary | https://schema.org | Class/property lookup for mapping section |
| W3C OWL 2 | https://www.w3.org/TR/owl2-primer/ | OWL axiom reference |
| W3C SKOS | https://www.w3.org/TR/skos-reference/ | SKOS hierarchy reference |
| BioPortal | https://bioportal.bioontology.org | Domain ontology prior art (medical, life sciences) |

## Tool Permissions
| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated OWL/SKOS validator is integrated yet. Manually check each QUALITY_GATES.md
gate against the produced artifact. Key checks: YAML frontmatter parses, id pattern
`^p01_ont_[a-z][a-z0-9_]+$`, classes list matches ## Class Hierarchy entries, body <= 8192 bytes,
quality == null, no instance data in artifact, all 5 required body sections present.

## Pipeline Integration
1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_ontology
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_ontology.md
```
