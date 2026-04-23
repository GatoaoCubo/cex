---
kind: knowledge_card
id: bld_knowledge_card_ontology
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for ontology production -- formal taxonomy and classification engineering
sources: W3C OWL 2 Primer, W3C SKOS Reference, schema.org Vocabulary, Protege OWL Tutorial, BioPortal
quality: 9.2
title: "Knowledge Card Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, knowledge_card, OWL, SKOS, schema.org, P01]
tldr: "Domain knowledge for formal ontology engineering: OWL/SKOS/schema.org standards, class hierarchy design, axiom patterns, and interoperability."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - p10_lr_ontology_builder
  - p03_sp_ontology_builder
  - p11_qg_ontology
  - bld_instruction_ontology
  - kc_ontology
  - ontology-builder
  - bld_output_template_ontology
  - bld_tools_ontology
  - bld_examples_ontology
  - bld_schema_ontology
---

# Domain Knowledge: ontology
## Executive Summary
Ontologies define formal classification structures for knowledge domains -- specifying what categories exist, how they relate hierarchically, what properties describe them, and what logical rules constrain the model. They differ from knowledge graphs (entity instances), glossary entries (single-term definitions), and knowledge cards (atomic facts). The three primary standards are OWL (complex inference), SKOS (hierarchical vocabularies), and schema.org (web interoperability).

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| llm_function | CONSTRAIN |
| max_bytes | 8192 |
| Frontmatter fields | 15+ |
| Quality gates | 10 HARD + 12 SOFT |
| Primary standards | OWL, SKOS, schema.org, RDF, mixed |
| Class naming | PascalCase (OWL convention) |
| Property naming | camelCase (OWL convention) |

## Standards Comparison
| Standard | Strength | Best For | Inference | Tooling |
|----------|----------|----------|-----------|---------|
| OWL 2 | Full description logic | Complex domains, automated reasoning | Yes (DL reasoners) | Protege, Apache Jena, ROBOT |
| SKOS | Hierarchical vocabularies | Thesauri, library classification | Limited (SPARQL) | SKOS Editor, OntoWiki, VocBench |
| schema.org | Web interoperability | Structured data, search engines | No | Google SDTT, JSON-LD Playground |
| RDF | Data interchange | Triple stores, federated data | Via SPARQL | Apache Jena, Virtuoso, Stardog |
| Mixed | Hybrid requirements | Systems needing both inference and web visibility | Partial | Any above combination |

## Key Patterns
### Class Hierarchy Design
| Pattern | Description | Example |
|---------|-------------|---------|
| Single root | All classes ultimately extend owl:Thing | Person, Organization both subClassOf owl:Thing |
| Sibling disjointness | Mutually exclusive siblings declare DisjointClasses | PhysicalProduct DisjointWith DigitalProduct |
| Role typing | Abstract superclass + typed subclasses | Agent -> Person, Organization, SoftwareAgent |
| Reification | Modeling relationships as classes | Employment (Person hasEmployer Organization) |

### Property Patterns
| Pattern | Applies When | Declaration |
|---------|-------------|-------------|
| Functional | Property has at most 1 value per instance | FunctionalProperty |
| Inverse functional | At most 1 subject per property value | InverseFunctionalProperty |
| Transitive | A->B, B->C implies A->C | TransitiveProperty |
| Symmetric | A->B implies B->A | SymmetricProperty |
| Inverse pair | Navigation in both directions | InverseOf |

### Axiom Checklist
| Axiom Type | When to Declare | OWL Syntax |
|------------|----------------|------------|
| DisjointClasses | Sibling classes cannot share instances | DisjointClasses( :A :B ) |
| FunctionalProperty | Single-valued property | FunctionalObjectProperty( :prop ) |
| TransitiveProperty | Hierarchy traversal | TransitiveObjectProperty( :prop ) |
| InverseOf | Bi-directional navigation | InverseObjectProperties( :p1 :p2 ) |
| AllValuesFrom | All values must be of type X | ObjectAllValuesFrom( :prop :Class ) |
| SomeValuesFrom | At least one value of type X | ObjectSomeValuesFrom( :prop :Class ) |

## Anti-Patterns
| Anti-Pattern | Consequence | Fix |
|-------------|-------------|-----|
| No disjointness on siblings | Reasoner infers unintended overlaps (OWA) | Declare DisjointClasses for mutual exclusions |
| Properties without domain/range | Any class uses any property; semantic drift | Add domain and range to every object property |
| Instance data in ontology | Mixes schema with data; breaks separation | Move instances to knowledge_graph artifact |
| No schema.org mapping | Web consumers cannot parse structured data | Map root classes to schema.org equivalents |
| Bare class names (no prefix) | Ambiguity when ontologies are merged | Declare namespace, prefix all local terms |
| Overly deep OWL hierarchies | Poor reasoner performance, high maintenance | Flatten with SKOS if depth > 5 levels |
| Missing cardinality on object props | Silent many-to-many where 1-to-1 expected | Declare min/max cardinality explicitly |

## Application
1. Scope domain: name the subject area and the standard (OWL/SKOS/schema.org)
2. Enumerate root classes: 3-7 top-level concepts
3. Build hierarchy: subclass each root at least one level
4. Add properties: object + datatype, with domain/range for each
5. Declare axioms: disjointness, functional, transitive, inverse
6. Map to schema.org: check each class against schema.org vocabulary
7. Set namespace: choose prefix, apply consistently
8. Validate: no instance data, no bare names, all sections present

## References
- W3C OWL 2 Primer: https://www.w3.org/TR/owl2-primer/
- W3C SKOS Reference: https://www.w3.org/TR/skos-reference/
- schema.org: https://schema.org
- Protege OWL Tutorial: https://protegewiki.stanford.edu/wiki/Protege4Tutorials
- SNOMED CT (medical ontology): https://www.snomed.org
- BioPortal (ontology repository): https://bioportal.bioontology.org

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_ontology_builder]] | downstream | 0.45 |
| [[p03_sp_ontology_builder]] | downstream | 0.44 |
| [[p11_qg_ontology]] | downstream | 0.44 |
| [[bld_instruction_ontology]] | downstream | 0.44 |
| [[kc_ontology]] | sibling | 0.41 |
| [[ontology-builder]] | related | 0.37 |
| [[bld_output_template_ontology]] | downstream | 0.37 |
| [[bld_tools_ontology]] | downstream | 0.33 |
| [[bld_examples_ontology]] | downstream | 0.32 |
| [[bld_schema_ontology]] | downstream | 0.32 |
