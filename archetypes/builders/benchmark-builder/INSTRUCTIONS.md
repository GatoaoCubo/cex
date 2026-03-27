---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for benchmark
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a benchmark

## Phase 1: RESEARCH
1. Identify the metric: what performance aspect needs measurement?
2. Define unit and direction (lower_is_better or higher_is_better)
3. Gather current baseline data (existing measurements, logs, APM tools)
4. Determine target: SLA requirement, competitor data, or improvement goal
5. Check brain_query [IF MCP] for existing benchmarks on this metric (avoid duplicates)
6. Research methodology: appropriate iterations, warmup, statistical tests
7. Document environment: hardware specs, software versions, config settings

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill following SCHEMA constraints
3. Fill frontmatter: all 22 required fields (quality: null)
4. Set metric, unit, direction, baseline, target with concrete numbers
5. Write Benchmark Overview section: what is measured and business impact
6. Write Methodology section: iterations, warmup, measurement protocol
7. Write Metrics section: table with all metrics, baselines, targets
8. Write Environment section: exact hardware/software/config for reproduction
9. Write Results Template section: percentile table structure

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, iterations >= 10, warmup >= 1
3. HARD: percentiles include p50+p95, baseline and target same unit
4. SOFT: methodology is reproducible, environment is specific
5. Verify: still measuring PERFORMANCE? Not drifting into correctness (eval)?
6. Verify: not defining criteria (scoring_rubric)? Not providing examples (golden_test)?
7. If score < 8.0: revise before outputting
