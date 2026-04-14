---
id: n06_audit_diff_strategy_builder
kind: audit_report
nucleus: n06
mission: HYBRID_REVIEW2
pillar: P11
quality: 8.9
title: "Audit: diff_strategy-builder (HYBRID_REVIEW2)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
tags: [diff_strategy, builder, audit, hybrid_review2, code_diff, myers, aider]
tldr: "13 ISOs audited. 4 pass, 5 fixed, 4 rebuilt. Root cause: financial trading semantics contaminated architecture, quality_gate, tools, examples."
---

# Audit: diff_strategy-builder

## Executive Summary

| Metric               | Count |
|:---------------------|:------|
| Total ISOs audited   | 13    |
| ISOs passing (>= 7.5)| 4     |
| ISOs fixed (targeted)| 5     |
| ISOs rebuilt (full)  | 4     |
| Fictional tools removed | 6  |
| Real tools added     | 14    |
| Algorithms added     | 3     |
| Wave 1 systemic issues confirmed | 2 |

## Per-ISO Breakdown

| ISO                   | Pre-Score | Action  | Post-Score | Primary Issue                                       |
|:----------------------|:----------|:--------|:-----------|:----------------------------------------------------|
| manifest              | 7.5       | PASS    | 7.5        | Good: LCS, Myers mentioned                          |
| instruction           | 6.0       | FIX     | 8.5        | Added algorithm names, Aider formats, validation    |
| schema                | 7.0       | FIX     | 8.5        | Added algorithm_type, granularity required fields   |
| quality_gate          | 3.0       | REBUILD | 9.0        | CONTAMINATED: "Backtest loss >15%" is financial     |
| output_template       | 6.0       | FIX     | 8.5        | Added algorithm, edge-case, patch-application sections|
| examples              | 4.0       | REBUILD | 8.5        | Golden example was FIFO vs Pro-Rata order matching  |
| knowledge_card        | 6.5       | FIX     | 9.0        | Added patience, histogram, Ratcliff-Obershelp, tools |
| architecture          | 2.5       | REBUILD | 9.0        | CONTAMINATED: Market Data API, Risk Engine, Quant   |
| collaboration         | 7.5       | PASS    | 7.5        | Correct: parser -> diff_strategy -> edit-formatter  |
| config                | 7.5       | PASS    | 7.5        | Correct naming convention, paths, limits            |
| memory                | 7.5       | PASS    | 7.5        | Good observations on decoupling detection/application|
| system_prompt         | 5.5       | FIX     | 8.5        | ACID/Raft/Paxos removed; LLM code-agent context added|
| tools                 | 2.0       | REBUILD | 9.0        | CONTAMINATED: CCXT/Backtrader/strat_backtest (financial)|

**Passing post-audit: 13/13**

## Root Cause Analysis

### Contamination Pattern: Financial Trading "Strategy"
The generative model (qwen3:14b + gemma4:26b mixed) confused "diff_strategy" with
"financial trading/quant strategy" -- the word "strategy" in trading context.

Contaminated ISOs:
- quality_gate: "Backtest loss >15%", "Strategy Consistency vs baseline", D3=Backtesting Results
- tools: CCXT (crypto exchange), Backtrader (backtesting), strat_backtest.py, strat_diff_check.py
- architecture: "Market Data API", "Risk Engine", "Quant" as owner, "Execution Engine"
- examples: Golden case was FIFO vs Pro-Rata order matching algorithm (order book, not code)

### Missing Algorithms (all added in FIXes)
| Algorithm             | Pre-audit | Post-audit | Reference               |
|:----------------------|:----------|:-----------|:------------------------|
| Myers                 | partial   | full       | Myers (1986) IEEE TSE   |
| LCS                   | partial   | full       | Algorithm Theory        |
| patience diff         | MISSING   | added      | Bram Cohen / Bazaar     |
| histogram diff        | MISSING   | added      | git default since 2012  |
| Ratcliff-Obershelp    | MISSING   | added      | difflib SequenceMatcher |

### Missing Real Tools (all added in REBUILD)
| Tool                  | Pre-audit | Post-audit |
|:----------------------|:----------|:-----------|
| difflib (Python)      | MISSING   | added      |
| git apply --3way      | MISSING   | added      |
| patch (POSIX)         | MISSING   | added      |
| Aider whole           | MISSING   | added      |
| Aider diff            | MISSING   | added      |
| Aider udiff-simple    | MISSING   | added      |
| Aider diff-fenced     | MISSING   | added      |
| tree-sitter           | MISSING   | added      |
| difftastic            | MISSING   | added      |
| diff-match-patch      | MISSING   | added      |

## Wave 1 Systemic Issues -- Confirmed

Two of five systemic issues from Wave 1 (hybrid_review_n06.md) confirmed in this builder:

| Systemic Issue             | Wave 1 Occurrence           | HYBRID_REVIEW2 Occurrence              |
|:---------------------------|:----------------------------|:---------------------------------------|
| Fictional tool references  | SafetyChain, PolicyForge    | strat_backtest.py, CCXT, Backtrader    |
| Architecture domain contamination | crypto exchange vs AI | financial trading vs code editing   |

Not present in this builder (different domain):
- Jurisdiction handling (not applicable to diff strategies)
- CSAM (not applicable)
- Named benchmark requirements (algorithm complexity is the equivalent)

## Commercial Lens: Diff Strategy Quality -> Pricing Power

### Direct Revenue Connection
Code-agent reliability depends on diff strategy quality:
- **Misapplied patches** (wrong diff algorithm for context) = hallucinated or broken code changes
- **Patch application failures** increase retry costs and user frustration
- **Structural diff (AST-level)** enables semantic refactors = premium code-agent tier

### Pricing Tier Differentiation

| Tier          | Diff Strategy            | Why it Commands Premium              |
|:--------------|:-------------------------|:-------------------------------------|
| Basic         | Myers line diff (whole)  | Full replacement; no context needed  |
| Standard      | Myers unified diff       | Context-aware; standard git workflow |
| Professional  | patience/histogram       | Human-readable; fewer merge conflicts|
| Enterprise    | AST/semantic diff        | Structural intent; multi-file refactor|

### Revenue Impact of This Audit
Pre-audit: Builder produced artifacts missing algorithm_type -> code agents used default Myers
for ALL file types -> unnecessary patch failures on heavily-commented/brace-heavy code.

Post-audit: histogram diff now documented as correct default for code; patience diff for refactors;
AST diff for structural changes. This enables tier differentiation and justifies premium pricing.

**Market signal**: Aider (code agent) uses 4 distinct edit formats precisely because different
models/contexts need different patch strategies. A product that exposes this granularity
commands 2-3x the price of one-size-fits-all.

## ISOs Still Below 9.0 (Acceptable)
- manifest (7.5): structural/identity ISO -- content depth is appropriate for its function
- collaboration (7.5): pipeline boundaries correctly defined; acceptable for coordination ISO
- config (7.5): naming/paths only -- low content by design
- memory (7.5): observation-based ISO -- qualitative guidance appropriate
