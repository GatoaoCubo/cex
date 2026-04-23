---
kind: quality_gate
id: p12_qg_visual_workflow
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for visual_workflow
quality: 9.1
title: "Quality Gate Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for visual_workflow"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_visual_workflow
  - visual-workflow-builder
  - kc_visual_workflow
  - p01_kc_workflow
  - bld_collaboration_visual_workflow
  - bld_architecture_workflow
  - workflow-builder
  - p11_qg_workflow
  - p09_qg_marketplace_app_manifest
  - bld_collaboration_workflow
---

## Quality Gate

## Definition
| metric          | threshold | operator | scope        |
|-----------------|-----------|----------|--------------|
| Config Validity | 100%      | >=       | per workflow |

## HARD Gates
| ID        | Check                     | Fail Condition                                      |
|-----------|---------------------------|-----------------------------------------------------|
| H01       | YAML frontmatter valid    | Invalid YAML syntax or missing required fields      |
| H02       | ID matches pattern        | ID does not match ^p12_vw_[a-z][a-z0-9_]+.md$      |
| H03       | kind field matches        | kind != 'visual_workflow'                           |
| H04       | Required fields present   | Missing 'name' or 'description' in metadata         |
| H05       | Workflow steps valid      | Invalid step type or missing required attributes    |
| H06       | Tool compatibility        | Unsupported tool referenced in workflow             |
| H07       | UI responsiveness         | Workflow editor fails to render on mobile devices   |

## SOFT Scoring
| Dim       | Dimension         | Weight | Scoring Guide                                      |
|-----------|-------------------|--------|----------------------------------------------------|
| D01       | Usability         | 0.15   | Intuitive drag-and-drop, clear error messages      |
| D02       | Correctness       | 0.20   | Workflow logic matches business rules              |
| D03       | Performance       | 0.10   | Load time < 2s, no lag during editing              |
| D04       | Compatibility     | 0.15   | Works across supported OS and browsers             |
| D05       | Error Handling    | 0.10   | Clear guidance for invalid configurations          |
| D06       | UI/UX             | 0.15   | Consistent with CEX design system                  |
| D07       | Accessibility     | 0.10   | WCAG 2.1 AA compliance                             |
| D08       | Data Integrity    | 0.15   | No data loss during workflow execution             |

## Actions
| Score  | Action                          |
|--------|---------------------------------|
| >=9.5  | GOLDEN -- automated approval    |
| >=8.0  | PUBLISH -- manual review        |
| >=7.0  | REVIEW -- QA validation needed  |
| <7.0   | REJECT -- fix critical issues   |

## Bypass
| conditions                          | approver   | audit trail              |
|------------------------------------|------------|--------------------------|
| Critical production fix required   | CTO        | Bypass logged with reason |
| Legacy workflow migration          | Architect  | Bypass logged with reason |

## Examples

## Golden Example
```markdown
---
kind: visual_workflow
name: CustomerOnboardingProcess
description: End-to-end customer onboarding workflow using Apache NiFi
---

**Tool**: Apache NiFi  
**Workflow Steps**:
1. **GetFile** - Ingest CSV data from SFTP server
2. **ConvertRecord** - Parse CSV to JSON using Avro schema
3. **ExecuteSQL** - Validate customer data against PostgreSQL database
4. **PutDatabase** - Insert validated records into MongoDB cluster
5. **EmailProcessor** - Send confirmation email via SendGrid API
```

## Anti-Example 1: Code-Defined Workflow
```markdown
---
kind: visual_workflow
name: FraudDetectionPipeline
description: Fraud detection using Apache Airflow
---

**Tool**: Apache Airflow  
**Workflow Steps**:
- [PythonOperator] Load data from S3
- [BashOperator] Run Spark job on EMR
- [EmailOperator] Notify results via SMTP
```
## Why it fails
Apache Airflow is a code-defined workflow system, not a visual editor. The artifact violates the boundary by using a tool that requires code configuration rather than GUI-based drag-and-drop interface.

## Anti-Example 2: DAG-Based Workflow
```markdown
---
kind: visual_workflow
name: DataProcessingPipeline
description: ETL process using Apache Luigi
---

**Tool**: Apache Luigi  
**Workflow Steps**:
- Task1: Extract data from MySQL
- Task2: Transform data with Pandas
- Task3: Load to Redshift
```
## Why it fails
Apache Luigi is a DAG-based system that requires code configuration. The artifact incorrectly categorizes a directed acyclic graph (DAG) workflow as a visual workflow, which is a fundamentally different paradigm.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
