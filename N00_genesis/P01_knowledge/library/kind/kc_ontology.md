---
id: kc_ontology
kind: knowledge_card
pillar: P01
title: Ontology (P01)
version: 1.0.0
quality: 9.0
density_score: 1.0
updated: "2026-04-13"
---

# Ontology (P01)

**About**: Formal taxonomy definitions using OWL, SKOS, and schema.org standards.

## Boundary
This artifact defines **formal ontologies** as structured, machine-readable taxonomies with explicit semantic relationships. It is **not** a data warehouse, thesaurus, or general knowledge repository. Ontologies focus on **logical consistency** and **interoperability**, not data storage or human-readable explanations.

## Related Kinds
- **Knowledge Graph**: Ontology provides the structural framework; Knowledge Graph adds contextual relationships and triples.
- **Taxonomy**: Ontology is a formalized version of taxonomy with explicit logical rules.
- **Semantic Model**: Ontology is a subset of semantic models that includes machine-readable definitions.
- **Data Schema**: Ontology includes semantic meaning beyond structural definitions.
- **Glossary Entry**: Ontology is more detailed and formalized than a glossary entry.

## When to Use Ontology vs Alternatives
| Use Case                  | Ontology               | Knowledge Graph        | Glossary Entry         | Example Use Case |
|---------------------------|------------------------|------------------------|------------------------|------------------|
| Formal taxonomies         | ✅ Yes                 | ⚠️ Limited             | ❌ No                  | Medical terminology |
| Semantic interoperability   | ✅ Yes                 | ✅ Yes (limited)       | ❌ No                  | Cross-system data exchange |
| Machine-readable definitions | ✅ Yes (RDF/OWL)     | ✅ Yes (RDF triples)   | ❌ No                  | AI training data |
| Human-readable explanations | ⚠️ Limited           | ⚠️ Limited             | ✅ Yes                 | User documentation |
| Inference capabilities    | ✅ Yes (OWL)          | ⚠️ Limited             | ❌ No                  | Automated reasoning |
| Scalability               | ⚠️ Moderate           | ✅ High                | ⚠️ Limited             | Large enterprise systems |

## Key Standards
| Standard | Purpose | Syntax | Use Cases | Example |
|---------|---------|--------|-----------|---------|
| **OWL** | Complex semantic relationships | RDF/XML, Turtle | Medical ontologies, AI | SNOMED-CT |
| **SKOS** | Hierarchical taxonomies | RDF, XML | Library classification, thesauri | Dewey Decimal System |
| **schema.org** | General-purpose structured data | JSON-LD, RDF | Web search, e-commerce | Product schema for Google |
| **RDF** | Data representation | Turtle, JSON-LD | Semantic web, triple stores | Wikidata |
| **OWL2** | Enhanced logical reasoning | RDF/XML, OWL | Legal ontologies, scientific domains | BioPortal ontologies |

## Implementation Patterns
| Pattern | Description | Example | Tooling |
|--------|-------------|---------|---------|
| OWL for domain-specific ontologies | Enables logical inference and consistency checks | Financial risk modeling | Protégé, Apache Jena |
| SKOS for controlled vocabularies | Hierarchical taxonomies with synonyms/relations | UNESCO subject categories | SKOS Editor, OntoWiki |
| schema.org for general entities | Standardized definitions for web search | Product, Event, Organization | Google Structured Data Testing Tool |
| Mapping to CEX knowledge cards | Use `@context` definitions for alignment | Ontology class → Knowledge Card ID | CEX Validator, JSON-LD |

## Validation
Use [Ontology Validator](https://github.com/ontologyValidator) to check:
| Check Type | Description | Tool Output | Example |
|------------|-------------|-------------|---------|
| Class hierarchy | Ensure no circular dependencies | Error log | "Class A inherits from Class B which inherits from Class A" |
| Property constraints | Validate domain/range consistency | Warning list | "Property 'hasAuthor' has invalid range: 'Book'" |
| RDF completeness | Verify all triples are present | Coverage report | "Missing 15% of expected triples in 'Medical Ontology'" |
| Logical consistency | Detect contradictions in axioms | Inference report | "Contradiction: 'isSubClassOf' and 'disjointWith'" |
| Interoperability | Test alignment with schema.org | Compatibility score | "85% alignment with schema.org 'Person' class" |

## Advanced Use Cases
| Domain | Ontology Application | Benefits | Challenges |
|--------|-----------------------|----------|------------|
| Healthcare | SNOMED-CT, LOINC | Standardized diagnosis coding | High maintenance cost |
| E-commerce | Product schema | Enhanced search visibility | Schema fragmentation |
| Scientific research | BioPortal ontologies | Data integration across studies | Domain-specific complexity |
| Government | Legal ontologies | Policy alignment | Political sensitivity |
| AI training | Knowledge graphs | Better entity recognition | Data bias risks |

## Best Practices
1. **Start simple**: Use SKOS for initial taxonomies, then expand to OWL
2. **Version control**: Use Git with RDF triple stores for traceability
3. **Interoperability**: Align with schema.org and other open standards
4. **Tooling**: Use Protégé for ontology design and Apache Jena for validation
5. **Documentation**: Maintain a parallel glossary for human-readable explanations
6. **Community review**: Engage domain experts for logical consistency checks

## Common Pitfalls
| Mistake | Consequence | Solution |
|--------|-------------|----------|
| Overly complex OWL | Poor performance | Simplify with SKOS |
| Missing property ranges | Invalid inferences | Define explicit domains/ranges |
| No versioning | Data inconsistency | Use Git + RDF versioning |
| Ignoring schema.org | Reduced interoperability | Map classes to schema.org |
| No validation | Logical errors | Use Ontology Validator |
| Poor documentation | Low adoption | Maintain parallel glossary |