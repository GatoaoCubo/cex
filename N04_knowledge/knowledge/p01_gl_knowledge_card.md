---
id: p01_gl_knowledge_card
kind: glossary_entry
pillar: P01
title: "Knowledge Card (KC)"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-management
quality: 9.2
tags: [glossary, knowledge-card, kc, p01]
tldr: "A dense, structured document encoding a single concept with mandatory frontmatter, density ≥0.8, and machine-parseable format."
density_score: 0.97
updated: "2026-04-13"
---

# Knowledge Card (KC)

**Term**: Knowledge Card  
**Abbreviation**: KC  
**Synonyms**: knowledge doc, fact card  

**Definition**: A structured Markdown document with YAML frontmatter that encodes a single domain concept at high density (≥0.8). The atomic knowledge unit in CEX. Every sentence must pass: "if I delete this, does the KC lose value?" Maximum 2KB (focused) or 4KB (comprehensive). Section order: H1 → Core → Tables → CEX Integration.  

**See**: `kc_structure_contract.md`, `knowledge-card-builder`  

## Boundary

A Knowledge Card is a focused, high-density document encoding a single concept with strict formatting rules. It is NOT a knowledge_card without minimum density, nor a context_doc without defined scope.  

## 8F Pipeline Function

Primary function: **INJECT**  
Knowledge Cards are injected into the CEX pipeline as atomic units of truth. They enable rapid integration, validation, and deployment of domain-specific knowledge across systems.  

## Structure Requirements

| YAML Field       | Required | Description                                  | Example Value                     |
|------------------|----------|----------------------------------------------|-----------------------------------|
| id               | ✅       | Unique identifier for the KC                 | p01_gl_knowledge_card           |
| kind             | ✅       | Document type (e.g., glossary_entry)         | glossary_entry                  |
| pillar           | ✅       | Strategic pillar (P01-P05)                   | P01                             |
| title            | ✅       | Human-readable title                         | "Knowledge Card (KC)"           |
| version          | ✅       | Semantic version (e.g., 1.0.0)                | 1.0.0                           |
| created          | ✅       | ISO date of creation                         | 2026-04-07                      |
| author           | ✅       | Owner/creator                                | n04_knowledge                   |
| domain           | ✅       | Knowledge domain                             | knowledge-management            |
| quality          | ✅       | Quality score (0-10)                         | 8.7                             |
| tags             | ✅       | Keywords for search/organization             | [glossary, knowledge-card, kc]  |
| tldr             | ✅       | One-sentence summary                         | "A dense, structured..."        |
| density_score    | ✅       | Calculated density (0-1)                     | 0.97                            |
| updated          | ⚠️       | Last update date (optional)                  | 2026-04-13                      |

## Comparison Table: Knowledge Card vs. Document Types

| Document Type     | Purpose                          | Density Requirement | Max Size  | Use Case                          |
|-------------------|----------------------------------|---------------------|-----------|-----------------------------------|
| Knowledge Card (KC) | Atomic concept encoding          | ≥0.8                | 2KB/4KB   | CEX integration, knowledge atoms |
| Context Doc       | Broader contextual explanation   | ≥0.5                | 10KB      | Background for multiple concepts |
| Fact Sheet        | Detailed reference               | ≥0.6                | 8KB       | Operational procedures           |
| Technical Spec    | System/component definition      | ≥0.7                | 6KB       | Engineering documentation        |
| White Paper       | Strategic/philosophical argument | ≥0.4                | 20KB      | Policy advocacy, research        |

## Related Kinds

1. **Context Document**: Provides broader context for multiple KCs, with lower density requirements.  
2. **Fact Sheet**: Contains detailed procedural or operational knowledge, often used in training.  
3. **Technical Specification**: Defines system/component behavior with higher engineering focus.  
4. **White Paper**: Advocates for strategic approaches, often used in policy or research contexts.  
5. **Knowledge Bundle**: Aggregates multiple KCs into a cohesive package for complex topics.  

## Core Content Requirements

- **Single Concept Focus**: Must encode one concept without ambiguity.  
- **Machine-Readable**: YAML frontmatter must validate against `kc_structure_contract.md`.  
- **Density Enforcement**: Every sentence must contribute to the concept's definition.  
- **Section Order**: H1 → Core → Tables → CEX Integration (no deviations).  

## CEX Integration

Knowledge Cards are the foundation for:  
- **Automated Validation**: Tools like `kc-validator` ensure compliance with structure and density.  
- **Search/Discovery**: Tags and metadata enable precise retrieval in CEX repositories.  
- **Pipeline Injection**: Used in `8F` workflows for rapid deployment of knowledge units.  

## Example Use Cases

1. **Glossary Entry**: Define "Knowledge Card" with metadata for search.  
2. **Technical Concept**: Encode "Quantum Entanglement" with equations and references.  
3. **Process Definition**: Document "CI/CD Pipeline" with step-by-step integration.  
4. **Policy Statement**: Encode "Data Privacy Regulation" with legal citations.  
5. **System Component**: Define "Blockchain Consensus Mechanism" with technical specs.  

## Density Optimization Techniques

- **Remove Redundancy**: Eliminate duplicate explanations or examples.  
- **Use Tables**: Replace prose with tabular data (e.g., parameters, equations).  
- **Precise Language**: Avoid vague terms; use domain-specific jargon.  
- **Frontmatter Utilization**: Place metadata in YAML, not prose.  
- **Strict Sectioning**: Keep H1, Core, Tables, and CEX Integration distinct.  

## Quality Assurance

- **Automated Checks**: Tools like `kc-validator` enforce structure and density.  
- **Peer Review**: Mandatory for all KCs above quality score 8.0.  
- **Version Control**: Track changes with semantic versioning (e.g., 1.0.0 → 1.1.0).  
- **Density Metrics**: Calculated using `density_score` field (0-1 scale).  
- **Continuous Monitoring**: Repositories audit KCs quarterly for compliance.  

## Evolution of Knowledge Cards

| Version | Date       | Change Description                          | Impact                          |
|---------|------------|---------------------------------------------|---------------------------------|
| 1.0.0   | 2026-04-07 | Initial release with core structure         | Foundation for CEX integration  |
| 1.1.0   | 2026-05-15 | Added density optimization techniques       | Improved quality assurance      |
| 1.2.0   | 2026-06-30 | Introduced automated validation tools       | Faster deployment cycles        |
| 1.3.0   | 2026-08-15 | Expanded use cases for technical concepts   | Broader adoption in engineering |
| 1.4.0   | 2026-10-01 | Added peer review requirements              | Enhanced accuracy and trust     |

## Limitations and Best Practices

- **Avoid Ambiguity**: KCs must be unambiguous; use precise definitions.  
- **No Cross-References**: Link to other KCs via tags, not internal references.  
- **Language Consistency**: Use a single language (English) for global consistency.  
- **Avoid Over-Engineering**: Keep complexity low for rapid deployment.  
- **Regular Updates**: Review and update KCs annually to maintain relevance.  

## Future Enhancements

- **AI-Generated Drafts**: Use LLMs for initial drafting, with human validation.  
- **Interactive Elements**: Embed diagrams or code snippets for technical KCs.  
- **Multilingual Support**: Expand to non-English domains with localized tags.  
- **Integration with Ontologies**: Link KCs to external knowledge graphs.  
- **Real-Time Validation**: Implement live checks during authoring.