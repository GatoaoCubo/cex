---
kind: examples
id: bld_examples_fallback_chain
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of fallback_chain artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: fallback-chain-builder
## Golden Example
INPUT: "Create fallback chain for research tasks: opus->sonnet->haiku"
OUTPUT:
```yaml
id: p02_fc_research_model
kind: fallback_chain
pillar: P02
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
steps_count: 3
timeout_per_step_ms: 30000
quality_threshold: 7.0
domain: "research_resilience"
quality: null
tags: [fallback_chain, research, resilience, P02, model-degradation]
tldr: "3-step research fallback: opus(30s)->sonnet(20s)->haiku(10s) with 7.0 quality gate"
retry_count: 1
circuit_breaker_threshold: 3
cost_ceiling_usd: 0.50
logging_level: "errors"
alert_on_final_fallback: true
keywords: [research, fallback, degradation, opus, sonnet, haiku]
density_score: 0.90
```
## Chain
| Position | Model | Provider | Timeout (ms) | Quality Min | Cost/1M tokens (USD) | Retry |
|----------|-------|----------|-------------|-------------|---------------------|-------|
| 1 | claude-opus-4-6 | anthropic | 30000 | 8.0 | 15.00 | 1 |
| 2 | claude-sonnet-4-6 | anthropic | 20000 | 7.0 | 3.00 | 1 |
| 3 | claude-haiku-4-5 | anthropic | 10000 | 5.0 | 0.25 | 2 |
## Degradation Logic
Step transition trigger: timeout exceeded OR quality below quality_min OR 5xx error.
Quality evaluation: automatic scoring via quality_gate after each response.
Transition: exhaust retry_count at current step, then move to next step immediately.
## Circuit Breaker
Threshold: 3 consecutive failures across all steps.
State when tripped: open (reject all new requests for cooldown period).
Recovery: automatic after 60 seconds cooldown, test with step 1.
Cooldown: 60 seconds.
## Cost Analysis
| Step | Cost/1M tokens | Expected usage | Projected cost |
|------|---------------|----------------|----------------|
| opus | $15.00 | 80% of requests | $0.30/request |
| sonnet | $3.00 | 15% of requests | $0.06/request |
| haiku | $0.25 | 5% of requests | $0.005/request |
| Total | - | - | ~$0.27/request avg |
Ceiling: $0.50 per request chain execution.
## Integration
- Activated by: agent request with model_preference or router timeout
- Provides to: researcher (research agent), any agent needing resilient model selection
- Signals: `p12_sig_model_degraded` on step transition, `p12_sig_chain_exhausted` on final fail
## References
- Anthropic pricing page — model costs
- CEX TAXONOMY_LAYERS.yaml — fallback_chain in runtime layer
WHY THIS IS GOLDEN:
- quality: null (H05 pass) | id p02_fc_ pattern (H02 pass) | kind: fallback_chain (H04 pass)
- 21 fields present (H06 pass) | steps_count: 3 matches table (H07 pass)
- Steps ordered opus->sonnet->haiku descending capability (H08 pass)
- timeout_per_step_ms: 30000 > 0 (H06 pass) | quality_threshold: 7.0 valid (H06 pass)
- tldr: 75ch (S01 pass) | tags: 5 items includes "fallback_chain" (S02 pass)
- Chain table 3 rows (S03 pass) | Cost Analysis present (S06 pass) | density: 0.90 (S09 pass)
## Anti-Example
INPUT: "Make a fallback for when things fail"
BAD OUTPUT:
```yaml
id: my_fallback
kind: chain
pillar: P03
steps_count: 1
quality: 8.0
tags: [fallback]
tldr: "This fallback chain provides a robust mechanism for handling failures gracefully in the system."
```
If the model fails, try again. If it fails again, use a smaller model.
FAILURES:
1. id: no `p02_fc_` prefix -> H02 FAIL
2. kind: "chain" not "fallback_chain" -> H04 FAIL
3. pillar: "P03" not "P02" (chain is P03; fallback_chain is P02) -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. steps_count: 1 (minimum is 2 for a chain) -> H07 FAIL
6. Missing fields: version, created, updated, author, timeout_per_step_ms, quality_threshold, domain -> H06 FAIL
7. tags: only 1 item, missing "fallback_chain" -> S02 FAIL
8. tldr: 91 chars of filler ("provides a robust mechanism") -> S10 FAIL
9. No ## Chain table in body -> S03 FAIL
10. No ## Cost Analysis section -> S06 FAIL
