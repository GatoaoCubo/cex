---
id: n01_wf_intelligence
kind: workflow
pillar: P12
version: "2.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
title: "N01 Intelligence Analysis Workflows"
domain: "intelligence, research, analysis"
quality: null
tags: [workflow, n01, intelligence, research, analysis, orchestration]
tldr: "Defines the primary research and analysis workflows for the N01 nucleus, including literature review, comparative study, and solo analysis."
agent_nodes: [n01_intelligence]
timeout: 10800 # 3 hours
retry_policy: "per_step"
steps_count: 4 # Max path length
execution: "conditional"
---

## Purpose
This document orchestrates the structured, multi-step processes used by the **N01 Intelligence Nucleus** to execute its core research tasks. The workflow is conditional, branching based on the `research_type` specified in the initial user request. This ensures a tailored, efficient, and rigorous approach for each distinct analytical challenge.

## Workflow Types
The workflow is triggered by a `research_type` parameter, which can be one of the following:
- **`LITERATURE_REVIEW`**: For synthesizing knowledge on a specific topic from a wide range of academic or technical sources.
- **`COMPARATIVE_STUDY`**: For benchmarking two or more subjects (e.g., products, companies, technologies) against a set of defined criteria.
- **`SOLO_ANALYSIS`**: For conducting a deep-dive analysis into a single subject, document, or dataset.

---
## Steps

### **Step 1: Deconstruct & Plan (All Types)**
- **Agent**: `n01_intelligence`
- **Action**: Parse the user request to identify the `research_type` and key entities. Formulate a structured research plan, including sources to consult and analytical frameworks to apply.
- **Input**: User Query (`text`, `research_type`)
- **Output**: `research_plan.json`
- **Signal**: `plan_complete`

---
### **Path A: Literature Review**

#### **Step 2A: Source Identification & Retrieval**
- **Agent**: `n01_intelligence`
- **Action**: Execute the research plan to query RAG sources (`n01_rag_source_intelligence`) and external tools (e.g., `google_scholar_mcp`) for relevant documents.
- **Input**: `research_plan.json`
- **Output**: `retrieved_sources_corpus`
- **Depends on**: Step 1

#### **Step 3A: Thematic Synthesis**
- **Agent**: `n01_intelligence`
- **Action**: Read the entire `retrieved_sources_corpus`. Identify, analyze, and cluster key themes, arguments, and data points across all sources.
- **Input**: `retrieved_sources_corpus`
- **Output**: `synthesized_themes.md`
- **Depends on**: Step 2A

---
### **Path B: Comparative Study**

#### **Step 2B: Define Comparison Criteria**
- **Agent**: `n01_intelligence`
- **Action**: Based on the research plan, establish a clear, objective set of criteria for comparison (e.g., features, pricing, performance metrics, market share).
- **Input**: `research_plan.json`
- **Output**: `comparison_matrix_template.json`
- **Depends on**: Step 1

#### **Step 3B: Data Extraction (per Subject)**
- **Agent**: `n01_intelligence`
- **Action**: For each subject in the comparison, gather data corresponding to the defined criteria. This step may run in parallel for each subject.
- **Input**: `research_plan.json`, `comparison_matrix_template.json`
- **Output**: `filled_comparison_matrix.json`
- **Depends on**: Step 2B

---
### **Path C: Solo Analysis**

#### **Step 2C: Deep Dive Data Extraction**
- **Agent**: `n01_intelligence`
- **Action**: Perform an exhaustive information extraction on the single subject or document.
- **Input**: `research_plan.json`
- **Output**: `extracted_data.json`
- **Depends on**: Step 1

#### **Step 3C: Framework Application**
- **Agent**: `n01_intelligence`
- **Action**: Apply relevant analytical frameworks (e.g., SWOT, PESTLE) to the extracted data to structure the analysis.
- **Input**: `extracted_data.json`
- **Output**: `analyzed_framework_output.md`
- **Depends on**: Step 2C

---
### **Step 4: Generate Intelligence Brief (All Types)**
- **Agent**: `n01_intelligence`
- **Action**: Consolidate all intermediate outputs (`synthesized_themes`, `filled_comparison_matrix`, `analyzed_framework_output`) into a final, structured `Intelligence Brief` as defined in the system prompt.
- **Input**: Output from Step 3 (A, B, or C)
- **Output**: `final_intelligence_brief.md`
- **Signal**: `workflow_complete`
- **Depends on**: Step 3 (A, B, or C)
