---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for fallback_chain artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a fallback_chain

## Phase 1: RESEARCH
1. Identify the domain requiring model fallback (what tasks need resilience)
2. List candidate models from highest to lowest capability
3. Gather cost per 1M tokens for each model
4. Determine acceptable quality thresholds per step
5. Define timeout requirements (latency-sensitive vs batch-tolerant)
6. Identify circuit breaker conditions (when to stop trying)
7. Search for existing fallback_chains via brain_query [IF MCP] (avoid duplicates)
8. Check model_cards for capability and pricing data

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate fc_slug in snake_case (e.g., research_model_fallback)
4. Fill frontmatter: all 15 required fields (quality: null, never self-score)
5. Set timeout_per_step_ms (default 30000)
6. Set quality_threshold (default 7.0)
7. Write Chain section: ordered step table (position, model, provider, timeout, quality_min, cost)
8. Write Degradation Logic section: trigger conditions for each step transition
9. Write Circuit Breaker section: threshold and halt behavior
10. Write Cost Analysis section: per-step and total cost projection
11. Write Integration section: how chain connects to routers and agents
12. Set steps_count to match actual rows in Chain table
13. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 8 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p02_fc_ pattern
5. Confirm kind == fallback_chain
6. Confirm quality == null
7. Confirm steps_count matches actual chain table rows
8. Confirm steps are ordered by decreasing capability
9. Confirm timeout_per_step_ms > 0
10. If score < 8.0: revise before outputting
