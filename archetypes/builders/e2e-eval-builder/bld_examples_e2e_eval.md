---
kind: examples
id: bld_examples_e2e_eval
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of e2e_eval artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: e2e-eval-builder
## Golden Example
INPUT: "Create e2e eval for the research-to-knowledge pipeline"
OUTPUT:
```yaml
id: p07_e2e_research_to_kc
kind: e2e_eval
pillar: P07
title: "E2E: Research to Knowledge Card Pipeline"
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
pipeline: "research-to-knowledge-card"
stages:
  - name: "research"
    agent: "research-agent"
    input: "query about prompt caching"
    expected_output: "research report with >= 3 sources"
    assertion: "output.sources.length >= 3"
  - name: "distill"
    agent: "knowledge-card-builder"
    input: "research report from stage 1"
    expected_output: "knowledge_card with all required sections"
    assertion: "output.kind == 'knowledge_card'"
  - name: "validate"
    agent: "quality-gate-builder"
    input: "knowledge_card from stage 2"
    expected_output: "quality score >= 8.0"
    assertion: "output.score >= 8.0"
input: "Research and distill knowledge about prompt caching techniques"
expected_output: "Validated knowledge_card scoring >= 8.0 with research sources"
timeout: 300
environment: "local-dev"
data_fixtures:
  - "seed_query: 'prompt caching techniques for LLM cost optimization'"
  - "expected_sources: ['anthropic docs', 'openai docs']"
cleanup: "Remove generated artifacts from P07_evals/scratch/"
parallel: false
reporting: "stdout summary with stage pass/fail"
domain: "knowledge"
quality: null
tags: [e2e-eval, research-pipeline, knowledge-card, integration]
tldr: "300s e2e: research->distill->validate pipeline produces quality KC >= 8.0"
density_score: 0.90
## Pipeline Overview
[research-agent] -> research report -> [kc-builder] -> knowledge_card -> [qg-builder] -> score >= 8.0
## Stages
### Stage 1: Research
- Agent: research-agent
- Input: "prompt caching techniques for LLM cost optimization"
- Expected: research report with >= 3 sources
- Assertion: output.sources.length >= 3
### Stage 2: Distill
- Agent: knowledge-card-builder
- Input: research report from Stage 1
- Expected: knowledge_card with all required sections
- Assertion: output.kind == "knowledge_card" AND all sections present
### Stage 3: Validate
- Agent: quality-gate-builder
- Input: knowledge_card from Stage 2
- Expected: quality score >= 8.0
- Assertion: output.score >= 8.0
## Data Fixtures
- Seed query: "prompt caching techniques for LLM cost optimization"
- Expected sources: anthropic docs, openai docs (minimum)
- KC template: standard knowledge_card with 6 sections
## Expected Output
Validated knowledge_card with:
- All required sections (Conceitos, Quando Usar, Economia, Limitacoes, Comparativo, References)
- Quality score >= 8.0 from quality gate
- Research sources cited in References section
## Cleanup
1. Remove scratch artifacts from P07_evals/scratch/
2. Clear any cached research results
3. Reset quality gate state
```
WHY THIS IS GOLDEN:
- quality: null (never self-scored)
- id matches p07_e2e_ pattern, kind: e2e_eval
- 21 frontmatter fields (all required + recommended)
- 3 connected stages with agent/input/output/assertion
- Pipeline Overview, data_fixtures, cleanup all present
- Expected Output is concrete, timeout: 300s
## Anti-Example
INPUT: "E2E test for research pipeline"
BAD OUTPUT:
```yaml
id: e2e_test
kind: e2e
quality: 8.5
pipeline: research
## Test
Run the research pipeline end to end. Should work correctly and produce good results.
```
FAILURES:
1. id: no p07_e2e_ prefix -> H02 FAIL
2. kind: "e2e" not "e2e_eval" -> H04 FAIL
3. pillar: missing -> H05 FAIL
4. quality: self-scored 8.5 instead of null -> H06 FAIL
5. stages: missing entirely -> H08 FAIL
6. timeout: missing -> H10 FAIL
7. environment: missing -> H11 FAIL
8. expected_output: vague "good results" -> S04 FAIL
9. data_fixtures: missing -> S05 FAIL
10. cleanup: missing -> S06 FAIL
11. tags: missing -> S02 FAIL
12. tldr: missing -> S01 FAIL
