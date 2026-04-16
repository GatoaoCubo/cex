---
kind: instruction
id: bld_instruction_ontology
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for ontology artifacts
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, builder, instruction, P01, taxonomy]
tldr: "3-phase build process for ontology: domain scoping, class/property/axiom composition, and structural validation."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce an ontology
## Phase 1: RESEARCH
1. Identify the domain: what subject area does this ontology cover? (medical, legal, ecommerce, agents, etc.)
2. Choose the primary standard: OWL (complex inference), SKOS (hierarchical vocabularies), schema.org (web interoperability), or mixed
3. Enumerate top-level classes: what are the root concepts that everything else classifies under?
4. Build the class hierarchy: for each top-level class, identify subclasses recursively (depth >= 2 for non-trivial domains)
5. Identify properties: what attributes describe each class? What relations link classes?
6. Classify properties by type: datatype property (literal value) vs object property (links to another class)
7. Determine axioms needed: which classes are disjoint? Which properties are functional, transitive, or symmetric?
8. Check existing ontologies via brain_query [IF MCP] -- do not reinvent SNOMED, schema.org Person, etc.; extend instead
9. Identify schema.org overlap: map local classes to schema.org equivalents where the domain overlaps
10. Define namespace prefix: choose a short namespace (e.g., "cex:", "med:", "prod:") for all local terms

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all required frontmatter fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: domain scope, primary standard, intended consumers, version rationale
5. Write **Class Hierarchy** section: tree structure or table with columns (class, parent, label, description, schema.org equivalent)
6. Write **Properties** section: table with columns (property, type, domain, range, cardinality, axiom flags)
7. Write **Axioms** section: explicit declarations for disjointness, functional, transitive, symmetric, inverse properties
8. Write **Schema.org Mapping** section: table mapping local classes/properties to schema.org URIs
9. Add optional Turtle/RDF snippet to illustrate key patterns (ASCII-only, no Unicode)
10. Confirm body <= 8192 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p01_ont_[a-z][a-z0-9_]+$`
4. Confirm `classes` list in frontmatter matches class names in ## Class Hierarchy section
5. Confirm `standard` field is set to one of: OWL, SKOS, schema.org, RDF, mixed
6. Confirm at least one property is defined in ## Properties section
7. Confirm ## Axioms section is present (may say "none" if domain has no axiom requirements)
8. Confirm ## Schema.org Mapping section is present (may say "not applicable" for purely internal ontologies)
9. Confirm no instance data in artifact -- only structural definitions
10. Confirm `quality` is null
11. Confirm body <= 8192 bytes
12. Cross-check boundary: is this a classification structure? If it contains entity instances it belongs in knowledge_graph. If it defines one term it belongs in glossary_entry. If it states a fact it belongs in knowledge_card.
13. If score < 8.0: revise in the same pass before outputting
