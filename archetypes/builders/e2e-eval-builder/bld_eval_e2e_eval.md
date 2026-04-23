---
kind: quality_gate
id: p11_qg_e2e_eval
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of e2e_eval artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: e2e_eval"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, e2e-eval, pipeline-testing, integration-test, P11]
tldr: "Gates for e2e_eval artifacts: validates pipeline coverage, stage completeness, fixture validity, assertion specificity, and cleanup protocol."
domain: "e2e_eval — end-to-end pipeline tests verifying full flow from input to final output"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.91
related:
  - bld_examples_e2e_eval
  - bld_instruction_e2e_eval
  - p03_sp_e2e_eval_builder
  - bld_architecture_e2e_eval
  - p10_lr_e2e_eval_builder
  - bld_output_template_e2e_eval
  - e2e-eval-builder
  - p01_kc_e2e_eval
  - p11_qg_unit_eval
  - bld_knowledge_card_e2e_eval
---

## Quality Gate

# Gate: e2e_eval
## Definition
| Field     | Value |
|-----------|-------|
| metric    | Composite score from SOFT dimensions + all HARD gates pass |
| threshold | >= 7.0 to publish; >= 9.5 golden |
| operator  | AND (all HARD) + weighted_sum (SOFT) |
| scope     | All artifacts where `kind: e2e_eval` |
## HARD Gates
All must pass. Any single failure = REJECT regardless of SOFT score.
| ID  | Check | Failure message |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | "Frontmatter YAML syntax error" |
| H02 | `id` matches `^p07_e2e_[a-z][a-z0-9_]+$` | "ID fails e2e_eval namespace regex" |
| H03 | `id` value equals filename stem | "ID does not match filename" |
| H04 | `kind` equals literal `"e2e_eval"` | "Kind is not 'e2e_eval'" |
| H05 | `quality` field is `null` | "Quality must be null at authoring time" |
| H06 | All required fields present: id, kind, pillar, domain, pipeline, stages, data_fixtures, expected_output, cleanup, version, created, author, tags | "Missing required field(s)" |
| H07 | `stages` list contains >= 2 stages (single-stage is a unit test, not e2e) | "e2e_eval must have >= 2 stages" |
| H08 | Each stage has both `name` and `expected` fields | "Stage missing 'name' or 'expected' assertion" |
| H09 | `data_fixtures` is non-empty and each fixture has a resolvable path or inline value | "Fixtures empty or unresolvable" |
| H10 | `cleanup` block defines post-run teardown actions (not empty) | "No cleanup protocol defined" |
## SOFT Scoring
Dimensions sum to 100%. Score each 0.0-10.0; multiply by weight.
| Dimension | Weight | What to assess |
|-----------|--------|----------------|
| Pipeline coverage | 1.0 | All named agents/steps in the pipeline appear in stages |
| Stage assertion quality | 1.0 | Assertions are specific (not just "non-empty output") |
| Fixture realism | 1.0 | Input fixtures represent real-world data, not trivial stubs |
| Intermediate output checking | 1.0 | Intermediate stage outputs verified, not just final output |
| Environment specification | 1.0 | Required environment (model, API keys, infra) documented |
| Failure scenario coverage | 1.0 | At least one negative test case (bad input, timeout, error) |
| Cleanup completeness | 0.5 | Teardown covers files, DB state, and API side effects |
| Reproducibility | 1.0 | Test can be run multiple times with identical results |
| Boundary clarity | 0.5 | Explicitly not unit_eval (single component) or benchmark (perf) |
| Execution time estimate | 0.5 | Expected runtime documented so CI can set apownte timeout |
| Documentation | 0.5 | tldr states which pipeline and what behavior is being verified |
Weight sum: 1.0+1.0+1.0+1.0+1.0+1.0+0.5+1.0+0.5+0.5+0.5 = 9.0 -> normalize to 100%
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool as golden exemplar |
| >= 8.0 | PUBLISH | Publish to pool |
| >= 7.0 | REVIEW | Flag for human review before publish |
| < 7.0  | REJECT | Return to author with failure report |
## Bypass
| Field | Value |
|-------|-------|
| conditions | Pipeline under active development where stages are not yet stable |
| approver | QA lead approval required with written justification |
| audit_trail | Bypass logged to `records/audits/e2e_eval_bypass_{date}.md` |
| expiry | 48h; eval must be stabilized before pipeline ships to production |
| never_bypass | H01 (YAML parse failure), H05 (quality null invariant), H07 (single-stage eval is by definition not e2e) |

## Examples

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
quality: 8.8
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
- All required sections (Conceitos, Quando Usar, Economia, Limitactions, Comparativo, References)
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
