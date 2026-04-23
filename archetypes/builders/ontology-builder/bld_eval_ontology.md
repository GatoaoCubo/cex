---
kind: quality_gate
id: p11_qg_ontology
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of ontology artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.1
title: "Gate: ontology"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, ontology, taxonomy, OWL, SKOS, P11]
tldr: "Gates for ontology artifacts: validates class hierarchy completeness, property constraints, axiom declarations, and schema.org mapping."
domain: "ontology -- formal taxonomy and classification definitions using OWL, SKOS, and schema.org patterns"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
related:
  - bld_instruction_ontology
  - p03_sp_ontology_builder
  - bld_collaboration_ontology
  - bld_schema_ontology
  - bld_examples_ontology
  - bld_output_template_ontology
  - bld_knowledge_card_ontology
  - ontology-builder
  - bld_architecture_ontology
  - bld_tools_ontology
---

## Quality Gate

# Gate: ontology
## Definition
| Field | Value |
|-------|-------|
| metric | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator | AND (all HARD) + weighted_sum (SOFT) |
| scope | All artifacts where `kind: ontology` |

## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID | Check | Failure message |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p01_ont_[a-z][a-z0-9_]+$` | "ID fails ontology namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"ontology"` | "Kind is not 'ontology'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, standard, classes, version, created, author, tags, tldr | "Missing required field(s)" |
| H07 | Body contains all 5 required sections: Overview, Class Hierarchy, Properties, Axioms, Schema.org Mapping | "Body missing required section(s)" |
| H08 | `classes` list in frontmatter matches class names in ## Class Hierarchy section (no extras, no omissions) | "classes list and Class Hierarchy mismatch" |
| H09 | No instance data in artifact -- schema definitions only (no populated RDF triples) | "Artifact contains instance data -- use knowledge_graph instead" |
| H10 | `standard` field is one of: OWL, SKOS, schema.org, RDF, mixed | "Standard field has invalid value" |

## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Class hierarchy depth | 1.0 | At least 2 levels of hierarchy (root + subclass) for non-trivial domains |
| Property completeness | 1.0 | Every object property has domain, range, cardinality; datatype has xsd: type |
| Disjointness coverage | 1.0 | All sibling class pairs that are mutually exclusive declare DisjointClasses |
| Axiom quality | 1.0 | Functional/transitive/symmetric declared where semantically correct |
| Inverse properties | 0.5 | Inverse pairs declared where navigable bi-directionally |
| Schema.org alignment | 1.0 | All classes with schema.org equivalents have mapping declared |
| Namespace discipline | 0.5 | All local terms use declared namespace prefix |
| Cardinality precision | 1.0 | min/max cardinality specified beyond "unconstrained" where meaningful |
| Boundary clarity | 1.0 | Explicitly not knowledge_graph (instances), not glossary_entry (single term) |
| Standard justification | 0.5 | Rationale for chosen standard (OWL vs SKOS vs mixed) is stated |
| Documentation | 1.0 | tldr names domain, class count, property count, and standard |
| Reuse of prior art | 0.5 | Where established ontologies exist (schema.org, SNOMED, etc.) extends rather than reinvents |
Weight sum: 1.0+1.0+1.0+1.0+0.5+1.0+0.5+1.0+1.0+0.5+1.0+0.5 = 10.0 (100%)

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0 | REJECT | Return to author with failure report |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Rapid-prototype ontologies where full property catalog is not yet known; stub must have >= 1 class and H01-H06 pass |
| approver | Domain expert approval required (written); axiom declarations never bypassed for OWL-mode ontologies |

## Examples

# Examples: ontology-builder
## Golden Example
INPUT: "Define an ontology for an e-commerce product catalog"

OUTPUT:
```yaml
id: p01_ont_ecommerce_product
kind: ontology
pillar: P01
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "ecommerce"
standard: mixed
classes:
  - Product
  - PhysicalProduct
  - DigitalProduct
  - ProductCategory
  - Brand
  - Offer
quality: null
tags: [ontology, ecommerce, product, schema.org, P01]
tldr: "E-commerce product ontology: 6 classes, 8 properties, schema.org aligned, OWL+SKOS mixed"
description: "Formal classification for e-commerce product catalogs: products, categories, brands, offers"
namespace: "prod:"
class_count: 6
property_count: 8
axiom_count: 4
schema_org_mapping: true
```

## Overview
Formal ontology for e-commerce product catalog classification using OWL class hierarchies
and schema.org interoperability mappings. Consumed by product search, recommendation, and
structured data systems.

## Class Hierarchy
| Class | Parent | Label | Description | schema.org Equivalent |
|-------|--------|-------|-------------|----------------------|
| Product | owl:Thing | Product | Any item offered for sale | schema:Product |
| PhysicalProduct | Product | Physical Product | Tangible item with shipping requirements | schema:Product |
| DigitalProduct | Product | Digital Product | Downloadable or streamed item, no shipping | schema:DigitalDocument |
| ProductCategory | owl:Thing | Product Category | SKOS concept for classification hierarchy | schema:Thing |
| Brand | owl:Thing | Brand | Manufacturer or label identity | schema:Brand |
| Offer | owl:Thing | Offer | Price and availability for a Product | schema:Offer |

## Properties
| Property | Type | Domain | Range | Cardinality | Axiom Flags |
|----------|------|--------|-------|-------------|-------------|
| hasBrand | object | Product | Brand | 0..1 | functional |
| hasCategory | object | Product | ProductCategory | 1..* | none |
| hasOffer | object | Product | Offer | 0..* | none |
| name | datatype | Product | xsd:string | 1..1 | functional |
| sku | datatype | Product | xsd:string | 0..1 | functional |
| price | datatype | Offer | xsd:decimal | 1..1 | functional |
| broader | object | ProductCategory | ProductCategory | 0..1 | transitive |
| narrower | object | ProductCategory | ProductCategory | 0..* | inverse:broader |

## Axioms
- DisjointClasses: PhysicalProduct, DigitalProduct -- a product cannot be both physical and digital
- FunctionalProperty: hasBrand -- each product has at most one brand
- TransitiveProperty: broader -- category A broader than B, B broader than C implies A broader than C
- InverseOf: broader / narrower

## Schema.org Mapping
| Local Class/Property | schema.org URI | Notes |
|---------------------|----------------|-------|
| Product | schema:Product | Direct equivalent |
| PhysicalProduct | schema:Product | Use additionalType for physical constraint |
| DigitalProduct | schema:DigitalDocument | Approximate; schema:SoftwareApplication also relevant |
| Brand | schema:Brand | Direct equivalent |
| Offer | schema:Offer | Direct equivalent |
| hasBrand | schema:brand | Direct equivalent |
| hasOffer | schema:offers | Direct equivalent |
| name | schema:name | Direct equivalent |

## References
- schema.org/Product: https://schema.org/Product
- W3C OWL 2 Primer: https://www.w3.org/TR/owl2-primer/
- SKOS Reference: https://www.w3.org/TR/skos-reference/

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_ont_ pattern (H02 pass)
- kind: ontology (H04 pass)
- classes list in frontmatter matches ## Class Hierarchy entries exactly (H08 pass)
- standard declared (H06 pass)
- All 5 required sections present: Overview, Class Hierarchy, Properties, Axioms, Schema.org Mapping (H07 pass)
- No instance data -- schema definitions only (H09 pass)
- Disjoint axiom declared for PhysicalProduct/DigitalProduct (S04 pass)
- InverseOf declared for broader/narrower (S06 pass)
- schema.org mapping covers all 6 classes (S08 pass)
- tldr: 59 chars <= 160 (S01 pass)
- tags: 5 items, includes "ontology" (S02 pass)

## Anti-Example
INPUT: "Create product ontology"

BAD OUTPUT:
```yaml
id: product-ontology
kind: taxonomy
pillar: knowledge
domain: ecommerce
classes: Product, Category, Brand
quality: 8.5
tags: [product]
```

Product is a thing that can be bought.
Category groups products.
Brand is who makes the product.

FAILURES:
1. id: "product-ontology" uses hyphens, no `p01_ont_` prefix -> H02 FAIL
2. kind: "taxonomy" not "ontology" -> H04 FAIL
3. pillar: "knowledge" not "P01" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. classes: string not list -> H06 FAIL
6. Missing required fields: version, created, updated, author, standard, namespace -> H06 FAIL
7. tags: only 1 item, missing "ontology" -> S02 FAIL
8. Body missing ## Class Hierarchy table -> H07 FAIL
9. Body missing ## Properties section -> H07 FAIL
10. Body missing ## Axioms section -> H07 FAIL
11. Body missing ## Schema.org Mapping section -> H07 FAIL
12. No property types, domains, ranges, or cardinality -> S05 FAIL
13. No disjoint or functional axioms declared -> S04 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
