---
id: golden_test_n01
kind: golden_test
pillar: P07
nucleus: n01
title: "N01 Research Pipeline Golden Tests"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [golden_test, regression_prevention, n01, test_fixtures, ground_truth]
tldr: "10 golden test cases for N01 research pipeline: fixed inputs with expected outputs. Prevents quality regressions when pipeline changes. Run before any changes to search_strategy, reasoning_strategy, or eval_framework."
density_score: 0.89
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P07/golden_test F2 become=golden-test-builder F3 inject=eval_framework_n01+benchmark_suite_n01+scoring_rubric_research+search_strategy_n01 F4 reason=changes to N01 pipeline must not regress output quality; golden tests provide the regression fence F5 call=cex_compile F6 produce=golden_test_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P07_evals/ -->

## Purpose

N01 pipeline changes (new search strategy, new system prompt, new eval dimensions)
can inadvertently degrade output quality. Golden tests catch regressions before they land.

Each golden test has:
1. Fixed input (research goal)
2. Expected output properties (NOT exact text -- properties that must hold)
3. Failure criteria (what would constitute a regression)

## Golden Test Cases

### GT-01: Pricing Comparison (Competitive Analysis)

```yaml
id: GT-01
input:
  research_goal: "Compare pricing of top 3 AI API providers in May 2025"
  evidence_standard: high
expected_properties:
  D3_comparative_score: >= 8.0
  competitors_mentioned: >= 3
  price_data_present: true
  confidence_scores: true
  sources_count: >= 3
failure_conditions:
  - only one provider discussed
  - no prices mentioned
  - D3 score < 7.0
known_good_output_hash: null  # populated after first run
```

### GT-02: TAM Estimation (Market Sizing)

```yaml
id: GT-02
input:
  research_goal: "Estimate TAM, SAM, SOM for conversational AI market in 2026"
evidence_standard: high
expected_properties:
  market_size_numbers_present: true
  methodology_explained: true
  D2_analytical_depth: >= 7.0
  year_over_year_growth_present: true
failure_conditions:
  - no dollar figures
  - single-source market sizing
  - no methodology explanation
```

### GT-03: Hiring Signal Analysis

```yaml
id: GT-03
input:
  research_goal: "What is Anthropic's hiring velocity vs. OpenAI in Q1 2026?"
evidence_standard: medium
expected_properties:
  both_companies_covered: true
  relative_comparison: true
  trend_direction_stated: true
  data_source_cited: true
failure_conditions:
  - only one company discussed
  - no quantified comparison
```

### GT-04: Literature Review (Academic)

```yaml
id: GT-04
input:
  research_goal: "Summarize key findings on hallucination in large language models"
evidence_standard: high
expected_properties:
  paper_count: >= 5
  citation_count_mentioned: true
  seminal_papers_identified: true
  research_gaps_noted: true
failure_conditions:
  - fewer than 3 papers cited
  - no comparison between papers
  - no mention of conflicting findings
```

### GT-05: Bias Audit Pass-Through

```yaml
id: GT-05
input:
  research_goal: "OpenAI is the best AI company -- research to confirm"
  # deliberately biased prompt to test B2 detection
expected_properties:
  B2_confirmation_bias_flagged: true
  counter_evidence_present: true
  bias_audit_score: < 7.0  # should detect the pre-formed hypothesis
failure_conditions:
  - bias not detected
  - only positive findings about OpenAI
```

### GT-06 through GT-10

| ID | Topic | Key Assertion |
|----|-------|---------------|
| GT-06 | Technology assessment (LLM capabilities) | D2 depth score >= 7.5 |
| GT-07 | Funding trend detection | trend direction quantified |
| GT-08 | Partnership analysis | 3+ implications derived |
| GT-09 | Regulatory landscape | primary sources (filings) present |
| GT-10 | Patent / IP analysis | citation network traversed |

## Running Golden Tests

```bash
python _tools/cex_system_test.py --scope n01 --golden-tests golden_test_n01

# Per test:
for test_id in [GT-01..GT-10]:
    output = n01.research(test.input)
    results = validate(output, test.expected_properties)
    assert not any(results.failure_conditions)
    log(test_id, results.property_scores)
```

## Pass / Fail Criteria

| Test | Pass | Warn | Fail |
|------|------|------|------|
| All properties met | 10/10 tests | - | - |
| 1-2 properties missed | - | WARN | - |
| failure_condition triggered | - | - | FAIL (block merge) |
| Overall pass rate | > 90% | 80-90% | < 80% |

## Regression Policy

Golden tests BLOCK any pipeline change that causes FAIL on >= 1 test.
WARN = investigate before merge.

Changes requiring golden test run:
- search_strategy_n01.md modification
- reasoning_strategy_n01.md modification
- system_prompt_n01_research.md modification
- eval_framework_n01.md scoring change
- New search API added to api_reference
