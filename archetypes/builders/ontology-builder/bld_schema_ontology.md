---
kind: schema
id: bld_schema_ontology
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for ontology
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, schema, P01, taxonomy, OWL, SKOS]
tldr: "Field definitions and body structure for ontology artifacts: formal taxonomy and classification definitions."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Schema: ontology
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_ont_{name}) | YES | - | Namespace compliance |
| kind | literal "ontology" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| domain | string | YES | - | Subject domain (e.g., "medical", "ecommerce", "legal") |
| standard | enum: OWL, SKOS, schema.org, RDF, mixed | YES | - | Primary ontology standard used |
| classes | list[string], len >= 1 | YES | - | Top-level class names defined |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "ontology" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this ontology covers |
| namespace | string | REC | - | Base URI or prefix (e.g., "ex:", "schema:") |
| class_count | integer | REC | - | Total number of classes defined |
| property_count | integer | REC | - | Total number of properties defined |
| axiom_count | integer | REC | - | Total number of axioms defined |
| schema_org_mapping | boolean | REC | false | Whether schema.org equivalents are provided |
## ID Pattern
Regex: `^p01_ont_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` -- what domain, what standard, who consumes, why this classification
2. `## Class Hierarchy` -- tree or table showing class inheritance (subClassOf chains)
3. `## Properties` -- table: property name, type (object/data), domain, range, cardinality, axioms
4. `## Axioms` -- disjointness, functional, transitive, symmetric, inverse declarations
5. `## Schema.org Mapping` -- mapping of local classes/properties to schema.org equivalents
## Constraints
- max_bytes: 8192 (body only)
- naming: p01_ont_{name}.md
- machine_format: yaml (compiled artifact)
- id == filename stem
- classes list MUST match class names defined in ## Class Hierarchy
- quality: null always
- NEVER include actual instance data -- schema definitions only
- Standard Turtle/OWL snippets in code blocks must be ASCII-safe
