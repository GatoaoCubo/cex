---
kind: output_template
id: bld_output_template_ontology
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce an ontology artifact
pattern: every field here exists in SCHEMA.md -- template derives, never invents
quality: 9.1
title: "Output Template Ontology"
version: "1.0.0"
author: n03_builder
tags: [ontology, builder, output_template, P01]
tldr: "Fill-in template for ontology artifacts: frontmatter + 5 required body sections."
domain: "ontology construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Output Template: ontology
```yaml
id: p01_ont_{{name}}
kind: ontology
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{subject_domain}}"
standard: {{OWL|SKOS|schema.org|RDF|mixed}}
classes:
  - {{ClassName1}}
  - {{ClassName2}}
  - {{ClassName3}}
quality: null
tags: [ontology, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_ontology_covers_max_200ch}}"
namespace: "{{prefix}}:"
class_count: {{N}}
property_count: {{N}}
axiom_count: {{N}}
schema_org_mapping: {{true|false}}
```

## Overview
`{{what_domain_and_why_this_classification_1_to_2_sentences}}`
`{{primary_standard_and_intended_consumers}}`

## Class Hierarchy
| Class | Parent | Label | Description | schema.org Equivalent |
|-------|--------|-------|-------------|----------------------|
| `{{ClassName1}}` | owl:Thing | {{human_label}} | {{brief_description}} | `{{schema_org_uri_or_none}}` |
| `{{ClassName2}}` | {{ClassName1}} | {{human_label}} | {{brief_description}} | `{{schema_org_uri_or_none}}` |
| `{{ClassName3}}` | {{ClassName1}} | {{human_label}} | {{brief_description}} | `{{schema_org_uri_or_none}}` |

## Properties
| Property | Type | Domain | Range | Cardinality | Axiom Flags |
|----------|------|--------|-------|-------------|-------------|
| `{{propName1}}` | {{object|datatype}} | `{{DomainClass}}` | {{RangeClass_or_xsd:type}} | {{min..max_or_unconstrained}} | {{functional|transitive|symmetric|inverse:propName|none}} |
| `{{propName2}}` | {{object|datatype}} | {{DomainClass}} | {{RangeClass_or_xsd:type}} | {{min..max_or_unconstrained}} | `{{flags_or_none}}` |

## Axioms
{{axiom_declarations_or_"none"}}
- DisjointClasses: `{{ClassName_A}}`, {{ClassName_B}} -- `{{reason}}`
- FunctionalProperty: `{{propName}}` -- at most one value per instance
- TransitiveProperty: `{{propName}}` -- if A->B and B->C then A->C
- InverseOf: `{{propName1}}` / `{{propName2}}`

## Schema.org Mapping
`{{not_applicable_or_mapping_table}}`
| Local Class/Property | schema.org URI | Notes |
|---------------------|----------------|-------|
| `{{ClassName1}}` | schema:{{SchemaOrgClass}} | `{{alignment_notes}}` |
| `{{propName1}}` | schema:{{schemaOrgProp}} | `{{alignment_notes}}` |

## References
- `{{standard_spec_or_prior_art_1}}`
- `{{standard_spec_or_prior_art_2}}`
