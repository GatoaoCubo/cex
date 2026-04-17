---
kind: examples
id: bld_examples_workflow_run_crate
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of workflow_run_crate artifacts
quality: 9.0
title: "Examples Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, examples, RO-Crate, workflow-run, CreateAction, ORCID, Galaxy, provenance-graph]
tldr: "Golden and anti-examples of workflow_run_crate artifacts"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```json
{
  "@context": [
    "https://www.researchobject.org/ro-crate/1.2/context",
    "https://w3id.org/ro/terms/workflow-run"
  ],
  "@graph": [
    {
      "@type": "CreativeWork",
      "@id": "ro-crate-metadata.json",
      "about": {"@id": "./"},
      "conformsTo": [
        {"@id": "https://w3id.org/ro/crate/1.2"},
        {"@id": "https://w3id.org/workflowhub/workflow-ro-crate/1.0"}
      ]
    },
    {
      "@type": "Dataset",
      "@id": "./",
      "name": "RNA-seq Alignment Pipeline Run 20260414",
      "datePublished": "2026-04-14",
      "license": {"@id": "https://spdx.org/licenses/CC-BY-4.0"}
    },
    {
      "@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"],
      "@id": "rna-seq-alignment.ga",
      "name": "RNA-seq Alignment Workflow",
      "programmingLanguage": {"@id": "#galaxy"},
      "url": "https://workflowhub.eu/workflows/123",
      "version": "2.1"
    },
    {
      "@type": "CreateAction",
      "@id": "#run-20260414-001",
      "name": "RNA-seq alignment run 20260414-001",
      "startTime": "2026-04-14T09:00:00Z",
      "endTime": "2026-04-14T11:32:00Z",
      "instrument": {"@id": "rna-seq-alignment.ga"},
      "object": [{"@id": "input/sample_reads.fastq.gz"}],
      "result": [{"@id": "output/aligned.bam"}],
      "agent": {"@id": "https://orcid.org/0000-0002-1825-0097"}
    },
    {
      "@type": "Person",
      "@id": "https://orcid.org/0000-0002-1825-0097",
      "name": "Josiah Carberry",
      "affiliation": {"@id": "#brown-university"}
    },
    {
      "@type": "Dataset",
      "@id": "input/sample_reads.fastq.gz",
      "name": "Sample FASTQ reads",
      "encodingFormat": "application/gzip",
      "contentSize": "2048000000",
      "sha256": "a1b2c3d4e5f6789012345678901234567890abcd",
      "license": {"@id": "https://spdx.org/licenses/CC0-1.0"}
    }
  ]
}
```

## Anti-Example 1: Missing CreateAction
```json
{
  "@context": ["https://www.researchobject.org/ro-crate/1.2/context"],
  "@graph": [
    {"@type": "Dataset", "@id": "./", "name": "My Workflow Run"},
    {"@type": "File", "@id": "workflow.ga"}
  ]
}
```
**Why it fails**: No CreateAction entity. The CreateAction is the provenance graph spine -- it links the workflow (instrument) to inputs (object) and outputs (result) with the executing researcher (agent/ORCID). Without it, the crate cannot be used for reproducibility or provenance verification.

## Anti-Example 2: Non-ORCID Person ID
```json
{
  "@type": "Person",
  "@id": "author",
  "name": "John Smith"
}
```
**Why it fails**: Person @id must be a full ORCID URL (https://orcid.org/XXXX-XXXX-XXXX-XXXX). Local IRI "author" is not resolvable, breaks FAIR Signposting, and prevents cross-crate author deduplication.

## Anti-Example 3: No Dataset Checksums
```json
{
  "@type": "Dataset",
  "@id": "input/data.csv",
  "name": "Input Data"
}
```
**Why it fails**: Missing sha256/md5 checksum. Without content hashes, input and output datasets cannot be verified for integrity, defeating the reproducibility purpose of Workflow Run Crate. RO-Crate 1.2 recommends sha256 for all file entities.
