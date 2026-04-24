---
id: p01_gl_knowledge_card
kind: glossary_entry
8f: F3_inject
pillar: P01
title: "Knowledge Card (KC)"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-management
quality: 9.1
tags: [glossary, knowledge-card, kc, p01]
tldr: "A dense, structured document encoding a single concept with mandatory frontmatter, density ≥0.8, and machine-parseable format."
density_score: 0.97
updated: "2026-04-13"
related:
  - p01_kc_knowledge_card
  - bld_collaboration_knowledge_card
  - p08_kc_capability_registry
  - knowledge-card-builder
  - p01_gl_taxonomy
  - bld_knowledge_card_knowledge_card
  - bld_examples_response_format
  - agent_card_n04
  - n04_kc_knowledge_management
  - n04_knowledge
---

# Knowledge Card (KC)

**Term**: Knowledge Card  
**Abbreviation**: KC  
**Synonyms**: knowledge doc, fact card  

**Definition**: A structured Markdown document with YAML frontmatter that encodes a single domain concept at high density (≥0.8). The atomic knowledge unit in CEX. Every sentence must pass: "if I delete this, does the KC lose value?" Maximum 2KB (focused) or 4KB (comprehensive). Section order: H1 → Core → Tables → CEX Integration.  

**See**: `kc_structure_contract.md`, `knowledge-card-builder`  

## Boundary

Short definition of domain term. NOT a knowledge_card (without minimum density) or context_doc (without scope).  

## Core Content

### Key Properties
- **Single Concept Focus**: Encodes one idea, entity, or process (e.g., "quantum entanglement" vs. "quantum mechanics").
- **Machine-Readable**: YAML frontmatter enables automated indexing, search, and integration.
- **Density Constraint**: ≥0.8 information density (no fluff, no redundancy).
- **Versioning**: Tracks updates via `version` field (e.g., 1.0.0 → 1.1.0).
- **Scoping**: Explicitly defines boundaries (e.g., "applies to P01 only").

### Technical Constraints
- **Size Limits**: Focused (2KB) vs. Comprehensive (4KB).
- **Format**: Strict Markdown with YAML frontmatter (no HTML, no images).
- **Encoding**: UTF-8, ASCII-compatible.
- **Validation**: Must pass `kc_validator` tool (see `kc_structure_contract.md`).
- **Licensing**: CC-BY-4.0 unless otherwise specified.

### Use Cases
- **Knowledge Injection**: Populates CEX knowledge graphs.
- **Training Data**: Feeds AI models with precise, structured data.
- **API Documentation**: Serves as schema for REST/GraphQL endpoints.
- **Onboarding**: Accelerates new team member learning curves.
- **Cross-System Sync**: Ensures consistency across CEX tools.

## 8F Pipeline Function

Primary function: **INJECT**  

**Inputs**:  
- Raw domain knowledge (e.g., technical specs, business rules).  
- Existing KCs for alignment.  

**Process**:  
1. **Extract**: Identify core concept from source material.  
2. **Transform**: Apply density constraints, structure, and validation.  
3. **Load**: Inject into CEX knowledge graph via API or CLI.  

**Outputs**:  
- Validated KC file (`.md`).  
- Graph database updates.  
- Audit trail for versioning.  

**Example**:  
A KC on "blockchain consensus" would inject nodes into the "distributed systems" graph, linking to "Proof of Work," "Proof of Stake," and "Smart Contracts."  

**Constraints**:  
- No circular references in graph.  
- All links must exist in CEX.  
- No duplicate concepts (enforced by `kc_validator`).  

## Comparison: KC vs. Document Types

| Document Type      | Purpose                        | Density Score | Format           | Use Case                          |
|--------------------|--------------------------------|---------------|------------------|-----------------------------------|
| Knowledge Card (KC) | Atomic concept encoding        | ≥0.8          | Markdown + YAML  | CEX integration, AI training      |
| Context Doc        | Broad contextual explanation   | 0.5–0.7       | Markdown         | Background reading, documentation |
| Knowledge Article  | Detailed tutorial or guide     | 0.6–0.8       | Markdown         | User onboarding, process guides   |
| Concept Map        | Visual relationship overview   | 0.4–0.6       | Diagram + text   | Learning, brainstorming           |
| Taxonomy Entry     | Hierarchical classification    | 0.7–0.9       | Structured JSON  | Metadata tagging, search indexing |

## Related Kinds

- **Context Document**: Provides broader context for KCs (e.g., "blockchain in finance" vs. "blockchain consensus").  
- **Knowledge Article**: Expands on KC concepts with tutorials or workflows (e.g., "Implementing Proof of Work").  
- **Concept Map**: Visualizes relationships between KCs (e.g., linking "quantum entanglement" to "quantum computing").  
- **Taxonomy Entry**: Defines classification hierarchies (e.g., "P01 > Physics > Quantum Mechanics").  
- **Integration Specification**: Describes how KCs connect to external systems (e.g., API endpoints, databases).  

## Examples

### Example 1: Focused KC (2KB)
```markdown
---
id: p01_gl_kc_quantum_entanglement
kind: glossary_entry
pillar: P01
title: "Quantum Entanglement"
version: 1.0.0
author: n04_physics
domain: quantum-mechanics
density_score: 0.92
tags: [quantum, entanglement, p01]
---

# Quantum Entanglement

**Term**: Quantum Entanglement  
**Synonyms**: EPR paradox, spooky action  

**Definition**: A phenomenon where particles become correlated such that the state of one instantly influences the state of another, regardless of distance.  

**See**: `p01_gl_kc_quantum_superposition`  

## Core Content

- **Key Properties**: Non-local correlations, no faster-than-light signaling.  
- **Mathematical Basis**: Bell's theorem, entangled state equations.  
- **Applications**: Quantum cryptography, quantum teleportation.  
```

### Example 2: Comprehensive KC (4KB)
```markdown
---
id: p01_gl_kc_blockchain_consenus
kind: glossary_entry
pillar: P01
title: "Blockchain Consensus"
version: 1.2.1
author: n04_blockchain
domain: distributed-systems
density_score: 0.85
tags: [blockchain, consensus, p01]
---

# Blockchain Consensus

**Term**: Blockchain Consensus  
**Synonyms**: Consensus algorithm, distributed agreement  

**Definition**: Mechanisms ensuring all nodes in a blockchain network agree on the validity of transactions and the state of the ledger.  

**See**: `p01_gl_kc_proof_of_work`, `p01_gl_kc_proof_of_stake`  

## Core Content

### Key Properties
- **Types**: Proof of Work (PoW), Proof of Stake (PoS), Delegated Proof of Stake (DPoS).  
- **Security**: Prevents double-spending, Sybil attacks.  
- **Scalability**: Varies by algorithm (e.g., PoW: low; PoS: high).  

### Technical Constraints
- **Latency**: PoW (10+ mins), PoS (seconds).  
- **Energy Use**: PoW (high), PoS (low).  
- **Validator Requirements**: PoW (computing power), PoS (staked tokens).  

### Use Cases
- **Bitcoin**: PoW.  
- **Ethereum 2.0**: PoS.  
- **EOS**: DPoS.  

## CEX Integration
- **Graph Nodes**: "Consensus Algorithm" → "Proof of Work," "Proof of Stake."  
- **API Endpoints**: `/v1/consensus/validate`, `/v1/consensus/ledger`.  
```

## Best Practices

1. **Frontmatter First**: Always include `id`, `kind`, `pillar`, `version`, `author`, `domain`, `density_score`, `tags`.  
2. **Density Checks**: Use `kc_validator` to ensure ≥0.8 density.  
3. **Linking**: Reference related KCs via `See` field.  
4. **Versioning**: Update `version` for changes (e.g., 1.0.0 → 1.1.0).  
5. **Validation**: Run through `kc_structure_contract.md` before publishing.  

## Common Pitfalls

- **Too Broad**: "Blockchain" instead of "Blockchain Consensus."  
- **Low Density**: Fluffy explanations without actionable data.  
- **Invalid Format**: Missing YAML frontmatter or incorrect Markdown.  
- **Circular Links**: KCs referencing each other without clear hierarchy.  
- **Outdated Info**: Failing to update `version` or `density_score`.  

## Tools

- **kc_validator**: Validates structure, density, and format.  
- **kc_builder**: GUI tool for creating KCs.  
- **kc_grapher**: Visualizes KC relationships in CEX.  
- **kc_search**: Full-text search across all KCs.  
- **kc_exporter**: Exports KCs to JSON, XML, or CSV.  

## Future Work

- **AI-Generated KCs**: Automate creation from unstructured text.  
- **Multilingual Support**: Translate KCs into 10+ languages.  
- **Real-Time Sync**: Auto-update KCs from live data streams.  
- **Interactive KCs**: Embed videos, code snippets, or simulations.  
- **Density Optimization**: Use NLP to refine prose for higher density.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_knowledge_card]] | related | 0.32 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.30 |
| [[p08_kc_capability_registry]] | downstream | 0.29 |
| [[knowledge-card-builder]] | downstream | 0.28 |
| [[p01_gl_taxonomy]] | sibling | 0.23 |
| [[bld_knowledge_card_knowledge_card]] | related | 0.23 |
| [[bld_examples_response_format]] | downstream | 0.23 |
| [[agent_card_n04]] | related | 0.23 |
| [[n04_kc_knowledge_management]] | related | 0.22 |
| [[n04_knowledge]] | related | 0.22 |
