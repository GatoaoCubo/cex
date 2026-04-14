---
id: kc_workflow_run_crate
kind: knowledge_card
title: Workflow Run Crate (RO-Crate 1.2)
version: 1.0.0
quality: null
pillar: P01
---

# Workflow Run Crate (RO-Crate 1.2)

## Overview
The Workflow Run Crate is a RO-Crate 1.2 implementation for capturing scientific workflow execution provenance. It enables reproducible research by tracking CreateAction metadata, ORCID attribution, and FAIR-compliant metadata across computational workflows.

## Core Components
- **CreateAction**: Records workflow execution metadata (inputs, outputs, parameters)
- **ORCID Attribution**: Links workflows to researchers via ORCID identifiers
- **FAIR Metadata**: Ensures findability, accessibility, interoperability, and reusability
- **Provenance Tracking**: Captures full execution lineage for reproducibility

## Technical Specification
```json
{
  "@context": "https://w3id.org/ro/crate/1.2/context",
  "about": {
    "type": "SoftwareSourceCode",
    "name": "WorkflowRunner",
    "description": "Scientific workflow execution engine",
    "creator": [
      {
        "name": "Researcher",
        "identifier": {
          "type": "ORCID",
          "value": "0000-0000-0000-0000"
        }
      }
    ],
    "dateCreated": "2023-10-15",
    "softwareVersion": "1.2.0"
  }
}
```

## Key Features
- **Execution Provenance**: Full traceability of workflow runs
- **Metadata Enrichment**: Automatic FAIR metadata generation
- **ORCID Integration**: Persistent researcher attribution
- **Reproducibility**: Immutable record of computational processes
- **Interoperability**: RO-Crate standard for cross-platform use

## Use Cases
- Computational research reproducibility
- Scientific workflow auditing
- Data provenance tracking
- Collaborative research validation
