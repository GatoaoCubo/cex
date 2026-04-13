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
**Domain**: Knowledge Management  
**Pillar**: P01  
**Version**: 1.0.0  

**Definition**: A structured Markdown document with YAML frontmatter that encodes a single domain concept at high density (≥0.8). The atomic knowledge unit in CEX. Every sentence must pass: "if I delete this, does the KC lose value?" Maximum 2KB (focused) or 4KB (comprehensive). Section order: H1 → Core → Tables → CEX Integration.  

**See**: `kc_structure_contract.md`, `knowledge-card-builder`  

## Boundary

A Knowledge Card is a **focused, machine-parseable knowledge artifact** that encodes a single concept with unambiguous boundaries. It is NOT a knowledge card without minimum density (≤0.7), nor a context document without explicit scope. It is NOT a narrative, a report, or a process flow. It is NOT a container for multiple concepts. It is NOT a living document with versioning.  

## 8F Pipeline Function

Primary function: **INJECT**  
**Input**: Unstructured domain knowledge (text, diagrams, interviews)  
**Output**: Structured KC with YAML frontmatter and Markdown body  
**Process**:  
1. Concept extraction (via NLP or manual curation)  
2. Density validation (≥0.8)  
3. Frontmatter injection (id, kind, pillar, etc.)  
4. Section ordering (H1 → Core → Tables → CEX Integration)  
5. Machine-parseable formatting (YAML + Markdown)  
**Example**: A 300-word interview transcript is distilled into a 250-byte KC with 4 sections and 3 tables.  

## Structure Requirements

| Section | Required | Format | Content Type | Example |
|--------|----------|--------|--------------|---------|
| H1 | Yes | Markdown | Concept title | `# Knowledge Card: Quantum Entanglement` |
| Core | Yes | Markdown | Definition, use cases | "Quantum entanglement is a physical phenomenon..." |
| Tables | Optional | Markdown | Data, comparisons | "Comparison of Entanglement Theories" |
| CEX Integration | Optional | YAML | Links to CEX artifacts | `see: kc_structure_contract.md` |

## Comparison: KC vs. Document Types

| Attribute | Knowledge Card (KC) | Context Document | Knowledge Article | Data Sheet | Process Map |
|----------|---------------------|------------------|-------------------|------------|-------------|
| Purpose | Encode single concept | Provide contextual background | Explain complex topics | Store structured data | Visualize workflows |
| Density Requirement | ≥0.8 | N/A | ≤0.6 | N/A | N/A |
| Structure | YAML + Markdown | Free-form text | Headings + paragraphs | Tables + charts | Diagrams |
| Use Case | CEX integration | Background reading | Training materials | Data reference | Process automation |
| Example | `# Quantum Entanglement` | "History of Quantum Mechanics" | "How to Build a Quantum Computer" | "Particle Mass Table" | "Entanglement Experiment Flow" |

## Related Kinds

1. **Context Document**: Provides broader background for KCs but lacks density requirements.  
2. **Knowledge Article**: Explains complex topics with lower density (≤0.6) and narrative structure.  
3. **Data Sheet**: Stores structured data (tables, charts) without conceptual encoding.  
4. **Process Map**: Visualizes workflows or procedures, often linked to KCs for context.  
5. **Glossary Entry**: Defines terms but lacks the structured format and density of KCs.  

## Density Validation

**Rule**: Every sentence must contribute to concept encoding.  
**Validation Method**: Remove sentence → KC loses value?  
**Examples**:  
- "Quantum entanglement is a physical phenomenon" → Valid (core definition).  
- "This is a very important concept" → Invalid (vague, no value added).  
- "Entanglement occurs between particles" → Valid (specific detail).  
- "Some people find this confusing" → Invalid (subjective, no value).  
- "Entanglement is used in quantum computing" → Valid (application context).  

## CEX Integration

**Purpose**: Enable machine-readable integration with CEX systems.  
**Methods**:  
- YAML frontmatter for metadata (id, kind, pillar, etc.)  
- Markdown body for content (H1, Core, Tables)  
- Links to related artifacts (`see:` field)  
**Example**:  
```yaml
see: 
  - kc_structure_contract.md
  - knowledge-card-builder
```  
**Outcome**: KCs become searchable, linkable, and reusable across CEX platforms.  

## Use Cases

1. **Training**: KCs encode core concepts for AI training (e.g., "Quantum Entanglement").  
2. **Integration**: KCs link to CEX artifacts via `see:` field (e.g., `kc_structure_contract.md`).  
3. **Automation**: KCs enable process automation by encoding rules (e.g., "Data Validation Rules").  
4. **Search**: KCs are indexed by CEX search engines for fast retrieval.  
5. **Collaboration**: KCs standardize knowledge sharing across teams (e.g., "API Design Principles").  

## Limitations

- **Size**: Max 2KB (focused) or 4KB (comprehensive).  
- **Scope**: Single concept only (no multiple topics).  
- **Format**: YAML + Markdown only (no diagrams or videos).  
- **Language**: English only (no multilingual support).  
- **Versioning**: No versioning (static content only).  

## Best Practices

1. **Start with H1**: Use concise title (e.g., `# Knowledge Card: Quantum Entanglement`).  
2. **Write Core First**: Define the concept in 1-2 sentences.  
3. **Add Tables**: Use tables for data, comparisons, or examples.  
4. **Link to CEX**: Use `see:` field to connect to related artifacts.  
5. **Validate Density**: Ensure every sentence adds value (≥0.8 density).  

## Example KC

```markdown
---
id: p01_gl_quantum_entanglement
kind: glossary_entry
pillar: P01
title: "Quantum Entanglement"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: physics
quality: 8.9
tags: [glossary, quantum, physics]
tldr: "A physical phenomenon where particles become correlated, affecting each other instantaneously."
density_score: 0.95
updated: "2026-04-13"
---

# Quantum Entanglement

**Term**: Quantum Entanglement  
**Abbreviation**: QE  
**Synonyms**: entanglement, spooky action at a distance  

**Definition**: A physical phenomenon where pairs or groups of particles become correlated, such that the quantum state of each particle cannot be described independently of the state of the others, even when the particles are separated by large distances.  

**See**: `kc_structure_contract.md`, `quantum-computing-basics`  

## Boundary

Quantum entanglement is a **specific physical phenomenon**. It is NOT a general theory of quantum mechanics, nor a philosophical interpretation. It is NOT a process or a tool.  

## 8F Pipeline Function

Primary function: **INJECT**  
**Input**: Research papers, experimental data  
**Output**: Structured KC with YAML frontmatter and Markdown body  
**Example**: A 500-word paper on entanglement is distilled into a 350-byte KC with 3 sections and 2 tables.  

## Structure Requirements

| Section | Required | Format | Content Type | Example |
|--------|----------|--------|--------------|---------|
| H1 | Yes | Markdown | Concept title | `# Quantum Entanglement` |
| Core | Yes | Markdown | Definition, use cases | "Quantum entanglement is a physical phenomenon..." |
| Tables | Optional | Markdown | Data, comparisons | "Comparison of Entanglement Theories" |
| CEX Integration | Optional | YAML | Links to CEX artifacts | `see: kc_structure_contract.md` |

## Use Cases

1. **Training**: KCs encode core concepts for AI training (e.g., "Quantum Entanglement").  
2. **Integration**: KCs link to CEX artifacts via `see:` field (e.g., `kc_structure_contract.md`).  
3. **Automation**: KCs enable process automation by encoding rules (e.g., "Data Validation Rules").  
4. **Search**: KCs are indexed by CEX search engines for fast retrieval.  
5. **Collaboration**: KCs standardize knowledge sharing across teams (e.g., "API Design Principles").  
```