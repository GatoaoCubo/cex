---
kind: instruction
id: bld_instruction_workflow_run_crate
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for workflow_run_crate
quality: 8.9
title: "Instruction Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, instruction, RO-Crate, provenance-graph, CreateAction, BioSchemas]
tldr: "Step-by-step production process for workflow_run_crate"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Identify workflow definition: Galaxy workflow file (.ga), Nextflow script, CWL document, or Snakemake file.
2. Collect execution metadata: run ID, start time, end time, executor agent (ORCID).
3. List input datasets: files, URLs, checksums (SHA-256 or MD5), formats, licenses.
4. List output datasets: files, URLs, checksums, formats.
5. Enumerate software environment: tool name, version, container image (Docker/Singularity) for each step.
6. Identify institutional affiliation for ORCID-linked author entities.

## Phase 2: COMPOSE
1. Reference SCHEMA.md for RO-Crate 1.2 Workflow Run Crate required entities.
2. Create ro-crate-metadata.json with @context including RO-Crate and BioSchemas contexts.
3. Add root Dataset entity: RO-Crate root descriptor with name, description, datePublished, license.
4. Add ComputationalWorkflow entity: url, programmingLanguage, version, BioSchemas profile.
5. Add CreateAction entity: instrument (workflow IRI), object (input IRIs), result (output IRIs), agent (ORCID), startTime, endTime.
6. Add Dataset entities for each input: @id, name, contentSize, sha256, encodingFormat, license.
7. Add Dataset entities for each output: @id, name, contentSize, sha256, encodingFormat, dateCreated.
8. Add SoftwareApplication entities for each tool: name, version, url, softwareVersion.
9. Add Person entities for each author with @id as ORCID URL.
10. Add Organization entity with affiliation data.
11. Add FAIR Signposting Link header declarations.
12. Validate JSON-LD syntax and RO-Crate profile conformance.

## Phase 3: VALIDATE
- [ ] ro-crate-metadata.json includes @context with RO-Crate 1.2 URL
- [ ] Root Dataset entity present with datePublished and license
- [ ] ComputationalWorkflow entity has programmingLanguage
- [ ] CreateAction links instrument, object[], result[], agent (ORCID)
- [ ] All input/output Datasets have sha256 or md5 checksum
- [ ] Author Person entities use ORCID URL as @id
- [ ] Domain keywords present: RO-Crate, workflow-run, provenance-graph, ORCID
