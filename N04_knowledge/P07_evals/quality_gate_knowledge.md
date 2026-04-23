---
id: n04_qg_knowledge
kind: quality_gate
pillar: P07_evals
version: 3.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge_nucleus
title: "N04 Knowledge Artifact Quality Gate"
gates_count: 9
target_kinds: [knowledge_card, chunk_strategy, embedding_config, rag_source, retriever_config]
linked_artifacts:
  primary:
    - n04_sr_knowledge
quality: 9.1
tags: [quality-gate, n04, knowledge, evals, p07]
tldr: "Defines the 9 quality gates (5 Hard, 4 Soft) for all N04-domain knowledge artifacts, ensuring structural integrity, atomicity, and discoverability."
density_score: 0.92
domain: knowledge
related:
  - bld_knowledge_card_quality_gate
  - bld_collaboration_quality_gate
  - bld_memory_quality_gate
  - p01_kc_artifact_quality_evaluation_methods
  - n01_qg_intelligence
  - p11_qg_quality_gate
  - p03_ins_quality_gate
  - p11_qg_creation_artifacts
  - p11_qg_kind_builder
  - quality-gate-builder
---

# N04 Knowledge Artifact Quality Gate

## 1. Overview
This document defines the official set of quality gates that all knowledge artifacts within the N04 domain must pass before they can be published and integrated into the CEX knowledge base. The system is divided into two distinct types of checks: Hard Gates and Soft Gates.

-   **Hard Gates (H1-H5)**: These are absolute, binary (pass/fail) checks that are fully automated. An artifact failing any hard gate is immediately rejected and cannot proceed.
-   **Soft Gates (S1-S4)**: These are nuanced, qualitative checks that are evaluated using the associated `n04_sr_knowledge` scoring rubric. The resulting score determines if an artifact is published, requires review, or is rejected.

## 2. Hard Gates: Structural & Schema Integrity
These gates are executed automatically on commit or via `cex_doctor.py`. Failure is not permitted.

| Gate ID | Name | Description | Automation |
| :--- | :--- | :--- |:--- |
| **H1** | **Valid Frontmatter** | The artifact's frontmatter must be valid YAML and parse without errors. All required fields for its `kind` must be present. | Fully Automated |
| **H2** | **Valid Kind & Pillar** | The `kind` must be a registered CEX kind, and the `pillar` must be a valid P-level pillar from the taxonomy. | Fully Automated |
| **H3** | **Unique ID** | The `id` field must be unique across all artifacts in the CEX ecosystem. | Fully Automated |
| **H4** | **Valid Taxonomy Tags** | All entries in the `tags` list must be valid, registered tags within the CEX master taxonomy. | Fully Automated |
| **H5** | **No Placeholder Content**| Key fields like `tldr` and `title` must not contain generic placeholder text (e.g., "...", "Pending finalization", "Lorem Ipsum"). | Fully Automated |

## 3. Soft Gates: Semantic & Relational Quality
These gates are evaluated by an LLM-assisted scorer using the `n04_sr_knowledge` rubric. The combined weighted score determines the final quality level.

| Gate ID | Name | Description | Scored By |
| :--- | :--- | :--- | :--- |
| **S1** | **Atomicity** | Does the artifact represent a single, cohesive, and self-contained concept? (Weight: 40%) | `n04_sr_knowledge` |
| **S2** | **Connectivity** | Is the artifact well-integrated into the Knowledge Graph via the `linked_artifacts` field? (Weight: 30%) | `n04_sr_knowledge` |
| **S3** | **Discoverability**| Is the metadata (`keywords`, `long_tails`, `tldr`) high-quality and representative of the content? (Weight: 20%) | `n04_sr_knowledge` |
| **S4** | **Clarity** | Is the content's language and structure precise, unambiguous, and easy to parse for another agent? (Weight: 10%) | `n04_sr_knowledge` |

## 4. Execution & Enforcement
- **Trigger**: This quality gate is automatically triggered by a `git pre-commit` hook for any changes within the `N04_knowledge/` directory.
- **Process**:
  1. The `cex_hooks.py` script executes the 5 Hard Gates. If any fail, the commit is rejected with an error message indicating the failed gate.
  2. If Hard Gates pass, the script calls the `n04_quality_scorer` tool (LLM-assisted) to evaluate the 4 Soft Gates using the rubric.
  3. The final weighted score is calculated.
     - `score >= 9.0`: Artifact is published.
     - `7.5 <= score < 9.0`: Artifact is marked for review.
     - `score < 7.5`: Commit is rejected.
- **Manual Execution**: The gate can be run manually on any file or directory using `python _tools/cex_doctor.py --gate n04_qg_knowledge`.

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish as exemplar |
| >= 8.0 | PUBLISH | Ready for runtime |
| >= 7.0 | REVIEW | Flag for review |
| < 7.0  | REJECT | Rework required |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental knowledge artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_quality_gate]] | related | 0.36 |
| [[bld_collaboration_quality_gate]] | related | 0.34 |
| [[bld_memory_quality_gate]] | related | 0.34 |
| [[p01_kc_artifact_quality_evaluation_methods]] | related | 0.33 |
| [[n01_qg_intelligence]] | sibling | 0.33 |
| [[p11_qg_quality_gate]] | sibling | 0.32 |
| [[p03_ins_quality_gate]] | related | 0.32 |
| [[p11_qg_creation_artifacts]] | sibling | 0.30 |
| [[p11_qg_kind_builder]] | sibling | 0.28 |
| [[quality-gate-builder]] | related | 0.28 |
