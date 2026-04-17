---
id: p11_qg_benchmark
kind: quality_gate
pillar: P11
title: "Gate: benchmark"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "builder_agent"
domain: benchmark
quality: 9.0
tags: [quality-gate, benchmark, P11, P07, governance, performance, measurement]
tldr: "Gates for benchmark artifacts — quantitative performance measurements with methodology and reproducibility."
density_score: 0.91
llm_function: GOVERN
---
# Gate: benchmark
## Definition
| Field     | Value                                                    |
|-----------|----------------------------------------------------------|
| metric    | measurement rigor + reproducibility completeness         |
| threshold | 8.0                                                      |
| operator  | >=                                                       |
| scope     | all benchmark artifacts (P07)                            |
## HARD Gates
All must pass. Failure on any = final score 0.
| Gate | Check | Why |
|------|-------|-----|
| H01 | YAML frontmatter parses valid YAML | Broken YAML = benchmark unreachable |
| H02 | id matches `^p07_bm_[a-z][a-z0-9_]+$` | Namespace compliance |
| H03 | id == filename stem | Brain search relies on this |
| H04 | kind == "benchmark" | Type integrity |
| H05 | quality == null | Never self-score |
| H06 | All 22 required fields present | Completeness |
| H07 | unit is non-empty string | Every measurement needs a unit |
| H08 | iterations >= 10 | Statistical minimum for reliable measurement |
| H09 | warmup >= 1 | Cold-start bias prevention |
| H10 | percentiles includes at least p50 and p95 | Tail latency required for realistic assessment |
## SOFT Scoring
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr <= 160 chars, non-empty | 1.0 |
| S02 | tags is list, len >= 3, includes "benchmark" | 0.5 |
| S03 | direction in [lower_is_better, higher_is_better] — explicit | 1.0 |
| S04 | baseline and target are numeric, same unit implied | 1.0 |
| S05 | Benchmark Overview section with metric rationale | 1.0 |
| S06 | Methodology section covers iterations, warmup, and protocol | 1.0 |
| S07 | Environment section lists hardware, software, exact versions | 1.0 |
| S08 | Metrics table has baseline and target columns | 1.0 |
| S09 | Results Template includes percentile rows (p50, p95, p99) | 0.5 |
| S10 | No qualitative prose ("good performance", "acceptable latency") | 1.0 |
| S11 | density_score >= 0.80 | 1.0 |
Weights sum: 10.0. Normalize: divide each by 10.0 before scoring.
## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN — pool as canonical performance baseline |
| >= 8.0 | PUBLISH — active performance contract |
| >= 7.0 | REVIEW — add missing percentiles or environment detail |
| < 7.0  | REJECT — methodology incomplete or unit undefined |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Production incident requiring immediate performance baseline capture |
| approver | p07-chief |
| audit_trail | Log in records/audits/ with incident reference and timestamp |
| expiry | 48h — full methodology required before expiry |
| never_bypass | H01 (YAML), H05 (quality null) |
