---
kind: config
id: bld_config_ontology
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for ontology builder
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 30
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, config, builder, P09]
tldr: "Naming conventions, file paths, size limits, and operational rules for ontology artifact production."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---
# Config: ontology Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_ont_{name}.md` | `p01_ont_ecommerce_product.md` |
| Compiled artifacts | `p01_ont_{name}.yaml` | `p01_ont_ecommerce_product.yaml` |
| Builder directory | kebab-case | `ontology-builder/` |
| Frontmatter fields | snake_case | `class_count`, `schema_org_mapping` |
| Name slug | snake_case, lowercase, no hyphens | `ecommerce_product`, `medical_diagnosis` |
| Class names | PascalCase (OWL convention) | `PhysicalProduct`, `DiagnosisCode` |
| Property names | camelCase (OWL convention) | `hasBrand`, `isPartOf`, `dateCreated` |
| Namespace prefix | short lowercase | `prod:`, `med:`, `cex:`, `ex:` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
1. Output: `P01_knowledge/examples/p01_ont_{name}.md`
2. Compiled: `P01_knowledge/compiled/p01_ont_{name}.yaml`

## Size Limits (aligned with SCHEMA)
1. Body: max 8192 bytes
2. Total (frontmatter + body): ~10000 bytes
3. Density: >= 0.85 (no filler)

## Standard Selection Rules
| Condition | Recommended Standard | Rationale |
|-----------|---------------------|-----------|
| Needs automated inference (DL reasoners) | OWL 2 | Full description logic support |
| Hierarchical vocabulary, thesaurus | SKOS | Designed for broader/narrower/related |
| Web-facing structured data | schema.org | Direct Google/Bing parsing |
| Simple triple storage, no inference | RDF | Lightweight, SPARQL-queryable |
| Inference + web visibility both needed | mixed | Annotate per class; use OWL for core, schema.org for mapping |

## Namespace Conventions
| Domain | Recommended Prefix | Example |
|--------|-------------------|---------|
| E-commerce | prod: | prod:Product, prod:Offer |
| Medical | med: | med:Diagnosis, med:Drug |
| Legal | leg: | leg:Contract, leg:Party |
| Scientific | sci: | sci:Compound, sci:Experiment |
| CEX internal | cex: | cex:Agent, cex:Artifact |
| Generic/example | ex: | ex:Person, ex:Organization |

## Effort Estimation
| Ontology size | Classes | Properties | Estimated turns |
|---------------|---------|------------|----------------|
| Minimal (stub) | 1-3 | 0-2 | 5-10 |
| Small | 4-8 | 3-6 | 10-15 |
| Medium | 9-20 | 7-15 | 15-25 |
| Large | 21+ | 16+ | 25-35 |

## Metadata

```yaml
id: bld_config_ontology
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_config_ontology.md
```
