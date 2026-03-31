---
kind: config
id: bld_config_benchmark
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for benchmark production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: high
max_turns: 25
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: benchmark Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_bm_{metric_slug}.md | p07_bm_ttft_sonnet4.md |
| Builder dir | kebab-case | benchmark-builder/ |
| Fields | snake_case | comparison_subjects, statistical_test |
| Metric slugs | lowercase_underscores | ttft, tps, cost_per_1m_input |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/examples/p07_bm_{metric_slug}.md
- Compiled: cex/P07_evals/compiled/p07_bm_{metric_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
- Metrics table: >= 1 row (no upper limit)
## Measurement Policy
- iterations >= 10 (prefer >= 30 for statistical significance)
- warmup >= 1 (prefer >= 5 for JIT/caching warmup)
- Percentiles MUST include p50 + p95 (p75 and p99 recommended)
- No dimension below p50 (median is minimum granularity)
- Baseline MUST be measured, not estimated or assumed
