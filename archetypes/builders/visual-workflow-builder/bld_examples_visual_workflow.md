---
kind: examples
id: bld_examples_visual_workflow
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of visual_workflow artifacts
quality: 9.0
title: "Examples Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, examples]
tldr: "Golden and anti-examples of visual_workflow artifacts"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
