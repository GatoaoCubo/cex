---
kind: architecture
id: bld_architecture_ontology
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of ontology -- inventory, dependencies, and architectural position in P01
quality: 9.1
title: "Architecture Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, architecture, P01, taxonomy, OWL, SKOS]
tldr: "Component map for ontology artifacts: class hierarchy, properties, axioms, namespace, and schema.org mapping -- with dependency graph in P01."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| domain | Subject area this ontology classifies (medical, legal, ecommerce, agents) | ontology-builder | required |
| standard | Primary ontology standard: OWL, SKOS, schema.org, RDF, mixed | ontology-builder | required |
| classes | Top-level concept names declared in frontmatter and body | ontology-builder | required |
| class_hierarchy | Inheritance tree: class, parent, label, description, schema.org mapping | ontology-builder | required |
| properties | Object and datatype properties with domain, range, cardinality, axiom flags | ontology-builder | required |
| axioms | Logical declarations: disjointness, functional, transitive, symmetric, inverse | ontology-builder | required |
| schema_org_mapping | Table linking local classes/properties to schema.org URIs | ontology-builder | required |
| namespace | Prefix for all local terms (e.g., "prod:", "med:", "cex:") | ontology-builder | required |
| metadata | id, version, pillar, domain, standard, author, created date | ontology-builder | required |

## Dependency Graph
```
guardrail (P11) --constrains--> ontology (logical consistency rules)
ontology --consumed_by--> knowledge_graph (P01) (ontology provides schema; KG adds instances)
ontology --consumed_by--> rag_source (P01) (RAG uses ontology classes for chunk categorization)
ontology --consumed_by--> embedding_config (P01) (embeddings may use ontology classes as namespaces)
ontology --consumed_by--> retriever_config (P01) (retriever may filter by ontology class)
ontology --referenced_by--> glossary_entry (P01) (glossary entries link to ontology classes)
glossary_entry (P01) --complements--> ontology (human-readable definitions for ontology terms)
knowledge_card (P01) --independent--> ontology (KCs capture facts; ontology captures structure)
```

| From | To | Type | Data |
|------|----|------|------|
| guardrail | ontology | constrains | logical consistency rules (no circular inheritance, no instance data) |
| ontology | knowledge_graph | consumed_by | class schema that KG populates with entity instances |
| ontology | rag_source | consumed_by | class hierarchy used to categorize and filter document chunks |
| ontology | embedding_config | consumed_by | namespace prefixes used as metadata filters in vector stores |
| ontology | retriever_config | consumed_by | class labels used as retrieval filters |
| ontology | glossary_entry | referenced_by | glossary terms link to their parent class in ontology |

## Boundary Table
| ontology IS | ontology IS NOT |
|-------------|-----------------|
| A formal classification structure: classes, subclasses, properties, axioms | A knowledge_graph (P01) -- KG stores entity instances and their relations |
| Defines the SCHEMA of a knowledge domain | A glossary_entry (P01) -- glossary defines one term in human-readable language |
| Uses OWL, SKOS, schema.org, or RDF standards | A knowledge_card (P01) -- KC captures an atomic factual claim, not a classification |
| Machine-readable with inference capabilities (OWL) | A chunk_strategy (P01) -- chunk_strategy governs how text is segmented for RAG |
| Provides semantic interoperability across systems | A rag_source (P01) -- rag_source is the document corpus, not its schema |
| Scoped to one domain (medical, ecommerce, agents) | A type_def (P06) -- type_def is a code-level type, not a semantic classification |
| Versioned classification structure | An embedding_config (P01) -- embedding_config governs vector representation |

## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Safety | guardrail, axiom declarations | Enforce logical consistency; prevent circular inheritance |
| Schema | class_hierarchy, properties, namespace | Define the classification structure |
| Interop | schema_org_mapping, standard selection | Enable cross-system semantic alignment |
| Meta | frontmatter fields, quality gate | Track versioning, ownership, and publication status |

## Position in P01
| Kind | Relationship to ontology | Direction |
|------|--------------------------|-----------|
| knowledge_graph | Consumes ontology as schema; adds entity instances | downstream |
| glossary_entry | Human-readable companion to ontology classes | sibling |
| knowledge_card | Atomic facts that may reference ontology classes | independent |
| rag_source | Document corpus that ontology helps categorize | downstream |
| embedding_config | Vector config may use ontology namespaces as metadata | downstream |
| chunk_strategy | Document segmentation -- precedes ontology classification | upstream |
