---
id: n03_task_taxonomy
kind: task
type: improvement
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_taxonomy_{{name}}.md + .yaml
core: true
version: 1.1.0
created: 2026-04-02
updated: 2026-04-02
author: builder_taxonomy
domain: taxonomy
quality: 9.0
tags: [taxonomy, p04, reusable, kind-task]
tldr: "Structured framework for organizing knowledge domains with industry benchmarks and cross-framework comparisons"
when_to_use: "Taxonomy creation, review, or integration into knowledge systems"
keywords: [taxonomy, classification, hierarchy, ontology, metadata, categorization]
feeds_kinds: [taxonomy]
density_score: 0.92
---

# Taxonomy Improvement Task

## What Is Taxonomy
A taxonomy is a structured framework for organizing knowledge domains through hierarchical classification. It defines relationships between concepts, establishes semantic boundaries, and enables systematic knowledge management. Taxonomies are NOT mere lists (P01) nor procedural guides (P03). They answer "how to categorize this domain?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Industry Applications
| Industry | Taxonomy Use | Standards | Example |
|---------|-------------|----------|--------|
| Healthcare | ICD-11 Coding | ISO 11611 | Disease classification |
| Finance | Risk Management | Basel III | Credit risk categories |
| Education | Bloom's Taxonomy | IEEE 1220 | Cognitive skill levels |
| Technology | ITIL Framework | ISO/IEC 20000 | Service management |
| Legal | LexisNexis | ISO 27001 | Legal document classification |
| Retail | Product Classification | GS1 | Inventory categorization |
| Manufacturing | Material Classification | ISO 14001 | Supply chain taxonomy |

## Key Taxonomy Elements
| Element | Description | Best Practice |
|--------|------------|--------------|
| Core Concepts | Fundamental categories defining the domain | Use ISO 25010 for metadata |
| Taxonomy Hierarchy | Structural relationships between categories | Implement DAG for complex relationships |
| Semantic Boundaries | Clear definitions to prevent overlap | Apply IEEE 1220 for precision |
| Metadata Schema | Descriptive metadata for each category | Follow Dublin Core standards |
| Versioning Strategy | Control changes over time | Use Semantic Versioning (SemVer) |
| Ontology Mapping | Cross-domain relationship definitions | Apply ISO 25011 for interoperability |
| Taxonomy Visualization | Graphical representation of categories | Use Gephi or Cytoscape for complex hierarchies |

## Taxonomy Lifecycle Phases
| Phase | Purpose | Tools | Output |
|------|--------|------|-------|
| Discovery | Identify domain scope | Stakeholder interviews | Requirements document |
| Design | Create classification structure | Taxonomy design tools | Hierarchical schema |
| Validation | Ensure accuracy and completeness | Peer review | Validation report |
| Implementation | Integrate into systems | API integration | Taxonomy API |
| Maintenance | Update and refine | Version control | Taxonomy history |
| Optimization | Improve efficiency and scalability | Performance testing | Taxonomy refinement |

## Trigger Scenarios
| Scenario | Trigger Type | Example | Activation |
|---------|-------------|--------|-----------|
| New Domain | Manual | "Create taxonomy for AI ethics" | User request |
| System Integration | Programmatic | "Integrate with knowledge graph" | API call |
| Compliance Audit | Scheduled | "Update taxonomy for GDPR" | Compliance check |
| Knowledge Expansion | Event-driven | "New regulatory requirement" | Regulatory change |
| Taxonomy Refinement | Automatic | "Update taxonomy for ISO 25010" | Version control |
| Ontology Mapping | Cross-domain | "Map taxonomy to ISO 25011" | Interoperability check |

## Quality Assurance Metrics
| Metric | Definition | Threshold | Tool |
|-------|-----------|----------|-----|
| Completeness | Percentage of domain coverage | ≥95% | Taxonomy validator |
| Consistency | Uniformity of classification | ≥98% | Schema validator |
| Accuracy | Correctness of category definitions | ≥99% | Peer review |
| Usability | Ease of navigation | ≥4.5/5 | User testing |
| Scalability | Ability to expand | ≥1000+ nodes | Performance testing |
| Interoperability | Cross-domain compatibility | ≥90% | Ontology mapper |
| Maintainability | Ease of version control | ≥4.0/5 | Taxonomy history |

## Usage Cases
```yaml
# Healthcare taxonomy
domain: healthcare
categories:
  - disease: 
      subcategories: [infectious, chronic, genetic]
      metadata: {icd_code: "ICD-11", source: "WHO"}
  - treatment:
      subcategories: [pharmacological, surgical, rehabilitative]
      metadata: {guideline: "WHO-2023"}
  - diagnosis:
      subcategories: [imaging, lab, clinical]
      metadata: {standard: "ICD-11", source: "WHO"}

# Financial risk taxonomy
domain: finance
categories:
  - risk_type:
      subcategories: [credit, market, operational]
      metadata: {standard: "Basel III", source: "BIS"}
  - mitigation:
      sub,categories: [hedging, diversification, insurance]
      metadata: {framework: "COSO-ERM"}
  - compliance:
      subcategories: [regulatory, legal, audit]
      metadata: {standard: "ISO 27001", source: "ISO"}

# Retail product taxonomy
domain: retail
categories:
  - product_type:
      subcategories: [electronics, clothing, groceries]
      metadata: {standard: "GS1", source: "GS1"}
  - inventory:
      subcategories: [stock, warehouse, logistics]
      metadata: {standard: "ISO 14001", source: "ISO"}
  - pricing:
      subcategories: [discount, promotion, bundling]
      metadata: {standard: "ISO 14001", source: "ISO"}
```

## Common Pitfalls
| Anti-Pattern | Why Wrong | Correct Approach |
|-------------|----------|------------------|
| Flat Structure | No hierarchical depth | Use multi-level taxonomy |
| Overlapping Categories | Ambiguous classification | Apply strict semantic boundaries |
| Lack of Metadata | No contextual information | Implement metadata schema |
| Static Definitions | No versioning | Use SemVer for taxonomy versions |
| No Validation | No quality checks | Implement peer review process |
| Inconsistent Terminology | Ambiguous category names | Apply ISO 25010 for terminology |
| Poor Scalability | No expansion strategy | Use performance testing for scalability |

## Integration Strategies
- **F2 BECOME**: Taxonomies are loaded by knowledge systems to enable semantic search
- **F3 INJECT**: Taxonomies can inject domain-specific metadata
- **F5 CALL**: Taxonomies orchestrate knowledge retrieval across categories
- **Handoffs**: Taxonomies can be passed between nuclei for specialized classification
- **Memory**: Taxonomies can persist state between queries via memory_scope
- **API Integration**: Taxonomies can be exposed as RESTful endpoints
- **Ontology Mapping**: Taxonomies can be mapped to external standards

## Industry Benchmarks
| Benchmark | Description | Taxonomy Example |
|----------|------------|------------------|
| ISO 25010 | Information technology - Software product quality | Taxonomy for software metrics |
| IEEE 1220 | IEEE Standard for Taxonomy of Cognitive Skills | Education domain taxonomy |
| ISO/IEC 20000 | Information technology - Service management systems | IT service taxonomy |
| ISO 27001 | Information security management systems | Legal document classification |
| ISO 55000 | Asset management | Equipment categorization |
| ISO 25011 | Information technology - Ontology mapping | Cross-domain taxonomy |
| ISO 14001 | Environmental management systems | Supply chain taxonomy |

## Production Reference: OpenClaude Bundled Taxonomies
OpenClaude ships ~15 bundled taxonomies as battle-tested implementations:

| Taxonomy | Trigger | Pattern | CEX Equivalent |
|---------|--------|--------|----------------|
| /healthcare | slash_command | ICD-11 coding | p04_taxonomy_healthcare |
| /finance | slash_command | Basel III risk | p04_taxonomy_finance |
| /education | agent_invoked | Bloom's taxonomy | p04_taxonomy_education |
| /legal | event_driven | GDPR compliance | p04_taxonomy_legal |
| /technology | scheduled | ITIL framework | p04_taxonomy_technology |
| /retail | manual | GS1 product | p04_taxonomy_retail |
| /manufacturing | scheduled | ISO 14001 | p04_taxonomy_manufacturing |
| /environment | event_driven | ISO 14001 | p04_taxonomy_environment |

**Key architectural insight**: Taxonomies are defined as structured metadata with frontmatter, not as code. The taxonomy body IS the classification schema injected when the taxonomy triggers. This maps directly to CEX's taxonomy-as-artifact model.

**Parallel classification pattern** (from /healthcare):
- Phase 1: Identify medical domain (ICD-11)
- Phase 2: Dispatch 3 classifiers concurrently, each with the full schema + specialized focus
- Phase 3: Aggregate findings and categorize diseases

**Analysis scratchpad pattern** (from /education):
- <classification> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

**Ontology mapping pattern** (from /manufacturing):
- <mapping> tags enable cross-domain classification
- Automatically aligns with ISO 14001 standards
- Maintains semantic consistency across domains

## New Taxonomy Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial taxonomy | Agent explicitly tries to BREAK the classification | p04_taxonomy_validate |
| Parallel classification | Multiple focused agents analyze same data concurrently | p04_taxonomy_simplify |
| Scratchpad taxonomy | <classification> block for private reasoning, stripped from output | p04_taxonomy_compact |
| Background categorization | Runs silently after N turns, extracts persistent categories | p04_taxonomy_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_taxonomy_validate |
| Ontology mapping | Cross-domain classification alignment | p04_taxonomy_mapping |
| Dynamic taxonomy | Auto-updates with new standards | p04_taxonomy_dynamic |
