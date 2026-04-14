---
id: kc_workflow_run_crate
kind: knowledge_card
title: Workflow Run Crate
version: 1.0.0
quality: null
pillar: P01
---

# RO-Crate 1.2 Workflow Run Crate

A standardized metadata framework for scientific workflow execution provenance, enabling:

1. **CreateAction Tracking**  
   - Captures workflow execution metadata (inputs, outputs, timestamps)
   - Links to original workflow artifacts via `dc:source`

2. **ORCID Attribution**  
   - Explicit creator identification through ORCID iDs
   - Supports collaborative authorship with `foaf:maker` relationships

3. **FAIR Metadata Compliance**  
   - Findable: Unique identifiers (DOI, PID) for workflow runs
   - Accessible: Open access metadata via RO-Crate API
   - Interoperable: Standardized schema for cross-platform use
   - Reusable: Machine-readable metadata for downstream analysis

4. **Provenance Chain**  
   - Immutable audit trail of workflow execution
   - Includes computational environment metadata
   - Supports reproducibility through versioned dependencies

**Key Components**  
- `workflowRun` entity with 12+ core properties  
- `ORCID` field for creator attribution  
- `dc:creator` for human-readable authorship  
- `schema:CreativeWork` for workflow artifact linkage  
- `prov:wasGeneratedBy` for execution provenance

**Use Cases**  
- Computational research reproducibility  
- Scientific workflow auditing  
- FAIR data compliance verification  
- Collaborative authorship tracking  
- Computational experiment archiving

**Implementation**  
- JSON-LD format with RO-Crate 1.2 schema  
- Optional extension for workflow execution logs  
- Compatible with CEX 8F pipeline for automated metadata generation
