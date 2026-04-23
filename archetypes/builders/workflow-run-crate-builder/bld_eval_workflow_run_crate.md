---
kind: quality_gate
id: p10_qg_workflow_run_crate
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for workflow_run_crate
quality: 9.0
title: "Quality Gate Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, quality_gate, RO-Crate, workflow-run, CreateAction, provenance-graph, ORCID, Galaxy, FAIR]
tldr: "Quality gate with HARD and SOFT scoring for workflow_run_crate"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_workflow_run_crate
  - bld_knowledge_card_workflow_run_crate
  - bld_instruction_workflow_run_crate
  - p03_sp_workflow_run_crate_builder
  - workflow-run-crate-builder
  - bld_tools_workflow_run_crate
  - p10_lr_workflow_run_crate_builder
  - bld_output_template_workflow_run_crate
  - bld_collaboration_workflow_run_crate
  - bld_schema_workflow_run_crate
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| RO-Crate 1.2 Workflow Run Crate compliance | 100% | equals | All HARD gates |

## HARD Gates
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p10_wrc_[a-z][a-z0-9_]+\.md$ | ID format mismatch |
| H03 | kind field is "workflow_run_crate" | Kind field incorrect or missing |
| H04 | @context includes RO-Crate 1.2 context URL | Missing or wrong context |
| H05 | CreateAction entity present with instrument, object, result, agent | Missing or incomplete provenance graph |
| H06 | agent_orcid is valid ORCID URL format | Non-ORCID or local IRI |
| H07 | At least one input Dataset with sha256 or md5 | Missing checksum on input datasets |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | CreateAction completeness (instrument, object, result, agent, startTime, endTime) | 0.30 | All present = 1.0, partial = 0.5, missing critical = 0 |
| D02 | Dataset coverage (all inputs + outputs have checksums and encodingFormat) | 0.25 | Complete = 1.0, partial = 0.5, absent = 0 |
| D03 | Author attribution (ORCID Person entity with name and affiliation) | 0.20 | Full ORCID record = 1.0, ORCID only = 0.7, absent = 0 |
| D04 | Software environment (SoftwareApplication entities for workflow tools) | 0.15 | All tools documented = 1.0, partial = 0.5, absent = 0 |
| D05 | Domain keyword density (RO-Crate, workflow-run, provenance-graph, ORCID, Galaxy, input-dataset, output-dataset) | 0.10 | 7+ keywords = 1.0, 5-6 = 0.7, <5 = 0.3 |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN | >=9.5 | Auto-publish with no review |
| PUBLISH | >=8.0 | Auto-publish after validation |
| REVIEW  | >=7.0 | Require manual review |
| REJECT  | <7.0  | Reject and flag for correction |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Draft crate (no live run data yet) | N07 orchestrator | Escalation log with DRAFT tag |

## Examples

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
      "name": "A. Smith",
      "affiliation": {"@id": "#example-university"}
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
  "name": "J. Lee"
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
