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
**Synonyms**: knowledge doc, fact card, atomic knowledge unit  

**Definition**: A structured Markdown document with YAML frontmatter that encodes a single domain concept at high density (≥0.8). The atomic knowledge unit in CEX. Every sentence must pass: "if I delete this, does the KC lose value?" Maximum 2KB (focused) or 4KB (comprehensive). Section order: H1 → Core → Tables → CEX Integration.  

**See**: `kc_structure_contract.md`, `knowledge-card-builder`, `density_scoring_matrix.md`  

## Boundary

A Knowledge Card is a **domain-specific, machine-parseable artifact** with strict density requirements. It is **not** a knowledge_card (without minimum density), context_doc (without scope), or general documentation. It must encode **exactly one concept** with no ambiguity.  

## 8F Pipeline Function

Primary function: **INJECT**  
- **Input**: Unstructured domain knowledge  
- **Output**: Structured KC with frontmatter, tables, and CEX integration  
- **Constraints**:  
  - Density score ≥0.8  
  - Max 4KB (comprehensive)  
  - YAML frontmatter required  
  - No markdown beyond H1 and tables  
- **Tools**: `kc_builder`, `density_analyzer`, `schema_validator`  

## Core

### Concept Encoding Principles
| Principle | Description | Example | Constraint |
|---------|-------------|---------|----------|
| Single Concept | Encodes exactly one domain concept | "Quantum Entanglement" | No multiple concepts |
| Density Optimization | Every sentence adds value | "Entanglement violates classical locality" | "If deleted, KC loses value" |
| Machine Parseability | YAML frontmatter required | `id: p01_gl_knowledge_card` | Schema validation mandatory |
| Contextual Scope | Defined by domain and pillar | "P01: Knowledge Management" | No cross-domain concepts |
| CEX Integration | Must include integration spec | `integration: cex-001` | Valid CEX version required |

### Density Optimization Techniques
1. **Eliminate redundancy**: "Entanglement is a quantum phenomenon" → "Quantum entanglement"  
2. **Use tables for data**: Replace prose with structured data (see below)  
3. **Frontmatter prioritization**: Place metadata first  
4. **Concise definitions**: "Non-local correlation between particles"  
5. **Avoid explanation**: Focus on facts, not interpretation  

## Comparison: KC vs. Other Document Types

| Document Type | Purpose | Density Score | Max Size | Primary Use Case |
|--------------|---------|----------------|----------|-------------------|
| Knowledge Card (KC) | Atomic concept encoding | ≥0.8 | 2KB (focused) | CEX integration, AI training |
| Context Document (CD) | Broad contextual explanation | 0.5-0.7 | 10KB+ | Human-readable documentation |
| Knowledge Graph Node (KGN) | Graph-based concept representation | 0.6-0.8 | 5KB | Semantic linking, visualization |
| CEX Integration Spec | CEX compatibility definition | 0.9 | 1KB | System interoperability |
| Fact Sheet | General information summary | 0.4-0.6 | 15KB+ | Public communication |

## CEX Integration

### Required Fields
- `integration`: CEX version (e.g., `cex-001`)  
- `schema`: JSON schema reference (e.g., `kc_schema_v1.0.0`)  
- `tooling`: Required tools for processing (e.g., `kc_builder`, `schema_validator`)  
- `pipeline`: 8F pipeline stage (e.g., `INJECT`)  
- `density_score`: Calculated value (≥0.8)  

### Example Integration
```yaml
integration: cex-001
schema: kc_schema_v1.0.0
tooling: ["kc_builder", "density_analyzer"]
pipeline: INJECT
density_score: 0.97
```

## Related Kinds

1. **Glossary Entry**: Provides definitions but lacks density requirements and CEX integration  
2. **Context Document**: Broader in scope but lower density (0.5-0.7)  
3. **Knowledge Graph Node**: Structured for graph linking but less focused on single concepts  
4. **CEX Integration Specification**: Defines compatibility rules but not content encoding  
5. **Fact Sheet**: General-purpose documentation with no strict density or structure  

## Use Cases

### Domain-Specific Applications
| Domain | Use Case | KC Example | Density | Size |
|-------|----------|------------|---------|------|
| Physics | Quantum Entanglement | "Quantum entanglement" | 0.97 | 2KB |
| Medicine | COVID-19 Vaccination | "mRNA vaccine mechanism" | 0.89 | 3KB |
| Finance | Black-Scholes Model | "Option pricing formula" | 0.85 | 4KB |
| Law | GDPR Compliance | "Data subject rights" | 0.82 | 3.5KB |
| Engineering | Finite Element Analysis | "Mesh discretization" | 0.88 | 3KB |

### CEX Pipeline Integration
- **Stage**: INJECT  
- **Input**: Unstructured domain knowledge (e.g., research papers, technical manuals)  
- **Output**: Structured KC with frontmatter, tables, and CEX integration  
- **Tools**: `kc_builder`, `density_analyzer`, `schema_validator`  
- **Validation**: Must pass schema checks and density scoring  

## Density Scoring Matrix

| Score Range | Description | Example | Use Case |
|------------|-------------|---------|----------|
| ≥0.9 | Highly dense, minimal redundancy | "Quantum entanglement" | AI training, CEX integration |
| 0.8-0.89 | Dense, minor redundancy | "mRNA vaccine mechanism" | Human-readable documentation |
| 0.7-0.79 | Moderate density | "Data subject rights" | Public communication |
| 0.6-0.69 | Low density | "Finite element analysis" | General reference |
| <0.6 | Not a KC | General documentation | Not applicable |

## Best Practices

1. **Start with the core concept**: "Quantum entanglement"  
2. **Add structured data**: Replace prose with tables (see above)  
3. **Validate density**: Use `density_analyzer` tool  
4. **Include CEX integration**: Ensure `integration` field is present  
5. **Use YAML frontmatter**: Mandatory for all KCs  

## Tools and Validation

- **kc_builder**: Converts unstructured knowledge to KC format  
- **density_analyzer**: Calculates density score (≥0.8 required)  
- **schema_validator**: Ensures YAML frontmatter compliance  
- **8F Pipeline**: Processes KCs through INJECT stage  
- **CEX Compatibility**: Must use valid CEX version (e.g., `cex-001`)  

## Conclusion

A Knowledge Card is the **atomic unit of knowledge in CEX**, designed for high-density encoding, machine parsing, and seamless integration. It must adhere to strict formatting, density, and CEX compatibility rules. By following best practices and using validation tools, KCs ensure consistency, interoperability, and value across the CEX ecosystem.