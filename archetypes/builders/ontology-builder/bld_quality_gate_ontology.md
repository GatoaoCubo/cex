---
id: p11_qg_ontology
kind: quality_gate
pillar: P11
title: "Gate: ontology"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
domain: "ontology -- formal taxonomy and classification definitions using OWL, SKOS, and schema.org patterns"
quality: 9.1
tags: [quality-gate, ontology, taxonomy, OWL, SKOS, P11]
tldr: "Gates for ontology artifacts: validates class hierarchy completeness, property constraints, axiom declarations, and schema.org mapping."
density_score: 0.92
llm_function: GOVERN
---
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
