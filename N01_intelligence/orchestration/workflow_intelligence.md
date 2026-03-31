---
id: n01_wf_intelligence
kind: workflow
pillar: P12
title: "N01 Standard Operating Workflows for Intelligence Analysis"
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "N01_rebuild_8F"
quality: null
tags: [workflow, orchestration, n01, research, analysis]
tldr: "Defines the structured, multi-step workflows for the N01 agent, covering literature reviews, comparative analysis, and trend analysis."
agent_node: "n01_intelligence"
timeout_seconds: 7200 # 2 hours
max_retries: 2
---

## 1. WORKFLOW OVERVIEW
This document defines the primary operational workflows for the **N01 Research & Intelligence Nucleus**. These are not linear scripts but conditional paths that adapt based on the `research_type` of the user's request.

**Supported `research_type` values:**
- `LITERATURE_REVIEW`: Synthesizing knowledge from a body of academic or technical documents.
- `COMPARATIVE_ANALYSIS`: Benchmarking two or more subjects (products, companies, etc.) against a set of criteria.
- `TREND_ANALYSIS`: Identifying and analyzing patterns, momentum, and trajectories in data over time.

---

## 2. META-WORKFLOW (ALL TYPES)

### **Step 0: Deconstruct & Plan**
- **Description**: The initial, mandatory step for all research tasks. The agent interprets the user's goal, identifies the correct workflow path, and creates a detailed execution plan.
- **Input**: `User_Query`
- **Action**:
    1.  Identify `research_type` (`LITERATURE_REVIEW`, `COMPARATIVE_ANALYSIS`, or `TREND_ANALYSIS`).
    2.  Extract key entities, research questions, and constraints.
    3.  Formulate a step-by-step `Research_Plan.json`.
- **Output**: `Research_Plan.json`, `Selected_Workflow_Path`

### **Final Step: Synthesize & Report**
- **Description**: The final, mandatory step. The agent takes the structured output from the specific workflow path and synthesizes it into the final deliverable.
- **Input**: `Structured_Analysis_Output` (from a completed workflow path)
- **Action**:
    1.  Validate the structured output against quality gates.
    2.  Draft the `Intelligence_Brief.md` per the system prompt's format.
    3.  Populate Executive Summary, Detailed Analysis, Gaps, and Appendix.
- **Output**: `Final_Report.md` (the Intelligence Brief)

---

## 3. WORKFLOW PATHS

### **Path A: Literature Review**

#### **Step A1: Source Aggregation**
- **Depends On**: Step 0
- **Input**: `Research_Plan.json`
- **Action**: Execute queries against RAG sources and future MCPs (e.g., ArXiv, Scholar) to gather all relevant documents.
- **Output**: `Corpus.zip` (A collection of source documents)

#### **Step A2: Thematic Synthesis**
- **Depends On**: Step A1
- **Input**: `Corpus.zip`
- **Action**: Ingest and analyze the entire corpus. Identify, tag, and cluster core themes, arguments, evidence, and contradictions across all sources.
- **Output**: `Structured_Analysis_Output.json` (A map of themes to supporting evidence and citations)

### **Path B: Comparative Analysis**

#### **Step B1: Establish Benchmarking Matrix**
- **Depends On**: Step 0
- **Input**: `Research_Plan.json`
- **Action**: Define a precise, objective, and justifiable set of comparison criteria. Create a blank `Comparison_Matrix.json` template.
- **Output**: `Comparison_Matrix_Template.json`

#### **Step B2: Data Extraction per Subject**
- **Depends On**: Step B1
- **Input**: `Research_Plan.json`, `Comparison_Matrix_Template.json`
- **Action**: For each subject being compared, systematically extract the required data points from sources to fill a copy of the matrix. This step can be parallelized.
- **Output**: `Filled_Matrices.json[]` (An array of filled matrices, one for each subject)

#### **Step B3: Normalize & Compare**
- **Depends On**: Step B2
- **Input**: `Filled_Matrices.json[]`
- **Action**: Consolidate the filled matrices. Normalize data where necessary (e.g., currency, units). Generate a comparative summary with key differences and insights.
- **Output**: `Structured_Analysis_Output.json` (Contains the final comparison table and summary insights)

### **Path C: Trend Analysis**

#### **Step C1: Time-Series Data Extraction**
- **Depends On**: Step 0
- **Input**: `Research_Plan.json`
- **Action**: Extract time-stamped data points, events, and metrics from the source material.
- **Output**: `Time_Series_Data.json`

#### **Step C2: Signal & Vector Analysis**
- **Depends On**: Step C1
- **Input**: `Time_Series_Data.json`
- **Action**: Analyze the time-series data to identify key vectors (direction, velocity, acceleration) of change. Identify leading and lagging indicators.
- **Output**: `Structured_Analysis_Output.json` (A summary of key trends, their momentum, and a forecast with confidence intervals)
