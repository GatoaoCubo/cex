---
id: p01_kc_cicd_llm_pipeline
kind: knowledge_card
pillar: P01
title: "CI/CD Pipeline for LLM Applications"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder_agent"
domain: llm_engineering
quality: 9.1
tags: [ci-cd, llm, pipeline, deployment, prompt-regression, eval-gate, canary, knowledge]
tldr: "CI/CD for LLM apps adds prompt regression evals, LLM-as-judge gates, and canary model deployments to standard DevOps; eval failure blocks merge."
when_to_use: "When deploying or updating LLM-powered services where prompt changes, model upgrades, or RAG pipeline changes require automated quality gates before production."
keywords: [cicd-llm, prompt-regression, eval-gate, canary-deployment, model-versioning]
long_tails:
  - How to run automated prompt regression tests in GitHub Actions for LLM apps
  - How to deploy a new LLM model version with canary release and auto-rollback
  - What quality gates to add to a CI pipeline to block prompt regressions
axioms:
  - ALWAYS run golden-dataset eval before merging any prompt or model change
  - NEVER deploy a model upgrade without a shadow traffic comparison step
  - IF eval score drops > 5% vs baseline THEN block merge and alert on-call
linked_artifacts:
  primary: null
  related: [p01_kc_prompt_caching, p01_kc_rag_fundamentals]
density_score: 0.88
data_source: "https://docs.github.com/en/actions/use-cases-and-examples/deploying"
---
# CI/CD Pipeline for LLM Applications

## Quick Reference
```yaml
topic: cicd_llm_pipeline
scope: Automated build, test, eval, and deploy for LLM-powered services
owner: builder_agent
criticality: high
gate_threshold: baseline_score - 5% (never absolute)
golden_pairs_minimum: 100 before enabling eval gate
```

## Key Concepts
- **Prompt Regression Test**: Runs golden dataset (50–500 input/output pairs) against new prompt; pass threshold = `baseline_score - 5%`
- **LLM-as-Judge**: Secondary LLM (GPT-4o / Claude Sonnet) scores outputs; requires calibration against human labels (Pearson r >= 0.70)
- **Eval Gate**: CI step returning exit code 1 on regression; blocks merge without explicit manual override
- **Shadow Deploy**: Old and new model run in parallel on 100% real traffic; outputs compared without serving new to users
- **Model Canary**: Routes 5% → 25% → 100% traffic to new model; auto-promotes if `error_rate < 1%` and `p99_latency < SLA` over 30-min window
- **Prompt Versioning**: Prompt templates treated as code — SemVer-tagged, stored in VCS alongside app code and eval dataset

## Strategy Phases
1. **Instrument**: Log 1% of prod requests + label via LLM-as-judge; target >= 500 golden pairs/month before enabling hard gates
2. **Gate**: Add eval step to CI (GitHub Actions / GitLab CI); threshold = `p95_baseline - 5%`; cost guard: fail if `avg_tokens` increases > 20%
3. **Stage**: Deploy to staging with 24h traffic replay; diff quality score, latency, and cost vs current prod
4. **Canary**: `5% → 25% → 100%` over 2h windows; auto-rollback if `quality_score < gate` or `error_rate` spikes
5. **Observe**: Emit per-request quality signals to Datadog/Grafana; alert on 7-day rolling quality degradation > 3%

## Golden Rules
- `EVAL_GATE`: set threshold at `baseline - 5%`, never at an arbitrary absolute (e.g., 80%) — baselines drift
- `PROMPT_COMMIT`: store prompt template + eval dataset together in the same PR so regressions are reproducible
- `COST_GUARD`: add token budget check to CI — a prompt that doubles token usage is a regression even if quality holds
- `ROLLBACK_FAST`: keep previous model artifact warm in serving layer; rollback must complete in < 60s
- `SEED_FIRST`: minimum 100 golden pairs before enabling hard eval gate, or gate produces false positives

## Flow
```text
[PR Open]
   |
   +-> [Lint + Unit Tests]
   |
   +-> [Prompt Regression Eval]
          |
     PASS: score >= baseline-5%      FAIL: block merge, post eval diff report
          |
   [Staging Deploy + Traffic Replay (24h)]
          |
   [Quality Gate: score + cost + latency]
          |
   [Canary 5% -> 25% -> 100% / 2h windows]
          |
   PROMOTE to 100%    or    AUTO-ROLLBACK -> alert
```

## Comparativo

| Pattern | Trigger | Traffic Scope | Key Tooling |
|---------|---------|---------------|-------------|
| Prompt Regression | Any prompt/model PR | Golden dataset 50–500 pairs | promptfoo, Braintrust, Azure PromptFlow |
| LLM-as-Judge | Eval step in CI | Sampled prod traffic | GPT-4o, Claude Sonnet as scorer |
| Shadow Deploy | Model upgrade | 100% real traffic, not served | Custom proxy, MLflow serving |
| Canary Release | Model upgrade | 5→25→100% over 2h | Kubernetes, AWS CodeDeploy |
| A/B Test | Strategic experiment | 50/50 split, >= 7 days | LaunchDarkly, Statsig, GrowthBook |

## References
- promptfoo eval framework: https://www.promptfoo.dev/docs/ci-cd/
- Braintrust CI integration: https://www.braintrustdata.com/docs/guides/ci
- GitHub Actions LLM deploy patterns: https://docs.github.com/en/actions/use-cases-and-examples/deploying
- Related: p01_kc_prompt_caching (cost optimization), p01_kc_rag_fundamentals (retrieval pipeline testing)