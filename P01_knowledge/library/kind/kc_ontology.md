---
id: kc_ontology
kind: knowledge_card
title: Ontology (P01)
version: 1.0.0
quality: 8.8
density_score: 1.0
updated: "2026-04-13"
---

# Ontology (P01)

**About**: Formal taxonomy definitions using OWL, SKOS, and schema.org standards.

## When to Use Ontology vs Alternatives
| Use Case                  | Ontology               | Knowledge Graph        | Glossary Entry         |
|---------------------------|------------------------|------------------------|------------------------|
| Formal taxonomies         | ✅ Yes                 | ⚠️ Limited             | ❌ No                  |
| Semantic interoperability   | ✅ Yes                 | ✅ Yes (limited)       | ❌ No                  |
| Machine-readable definitions | ✅ Yes (RDF/OWL)     | ✅ Yes (RDF triples)   | ❌ No                  |
| Human-readable explanations | ⚠️ Limited           | ⚠️ Limited             | ✅ Yes                 |

## Key Standards
- **OWL (Web Ontology Language)**: For complex semantic relationships
- **SKOS (Simple Knowledge Organization System)**: For hierarchical taxonomies
- **schema.org**: For general-purpose structured data

## Implementation Patterns
1. Use OWL for domain-specific ontologies requiring logical inference
2. Use SKOS for controlled vocabularies and thesauri
3. Reference schema.org for general entity types
4. Map ontology classes to CEX knowledge cards using `@context` definitions

## Validation
Use [Ontology Validator](https://github.com/ontologyValidator) to check:
- Class hierarchy consistency
- Property domain/range validity
- RDF triple completeness
