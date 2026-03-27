---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for fallback_chain
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a fallback_chain

## Phase 1: RESEARCH

1. Identify the primary model and the use case it serves (what tasks require this chain to be resilient)
2. List candidate fallback models in descending quality order — primary first, cheapest or smallest last
3. Define timeout per step in milliseconds, balancing latency requirements against model response time
4. Set the quality threshold: the minimum acceptable output score at which a step result is accepted rather than escalated to the next step
5. Determine circuit breaker parameters: how many consecutive failures trigger the breaker, the half-open test interval, and the reset conditions
6. Calculate cost per call for each model step so the chain documents the cost trade-off at each degradation level
7. Check existing fallback_chains via brain_query [IF MCP] for the same domain — do not duplicate a chain that already covers this use case

## Phase 2: COMPOSE

1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints
3. Fill all 15 required frontmatter fields; set `quality: null` — never self-score
4. Write **Chain Steps** section: ordered table with columns position, model, provider, timeout (ms), quality_min, cost per call — ordered from highest to lowest capability
5. Write **Circuit Breaker** section: failure threshold count, half-open test interval, reset conditions
6. Write **Quality Gate** section: minimum score to accept output at each step vs escalate to the next; what happens when all steps are exhausted
7. Write **Cost Control** section: maximum cost per request, budget alert thresholds
8. Write **Monitoring** section: metrics to track — step hit rate, fallback frequency, quality distribution per step
9. Set `steps_count` in frontmatter to match the exact number of rows in the Chain Steps table
10. Confirm body <= 4096 bytes

## Phase 3: VALIDATE

1. Check QUALITY_GATES.md manually
2. HARD gates: YAML parses, `id` matches `^p02_fc_[a-z][a-z0-9_]+$`, `kind` is the literal string `fallback_chain`, `quality` is null, at least 2 steps present, every step has a timeout value, quality threshold is numeric, circuit breaker is defined
3. SOFT gates: score each gate from QUALITY_GATES.md against the artifact
4. Confirm `steps_count` matches the actual number of rows in the Chain Steps table
5. Confirm steps are ordered by decreasing capability (most capable first)
6. Confirm all timeout values are greater than zero
7. Cross-check: is this a model degradation sequence? If it chains prompt transformations it belongs in a `chain` artifact (P03). If it routes by task type it belongs in a `router`. If it sequences satellite tasks it belongs in a workflow (P12). This artifact degrades model quality gracefully, nothing more.
8. If score < 8.0: revise in the same pass before outputting
