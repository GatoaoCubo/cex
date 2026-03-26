```yaml
---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for lifecycle_rule
pattern: 3-phase pipeline (research -> compose -> validate)
---
```

# Instructions: How to Produce a lifecycle_rule

## Phase 1: RESEARCH
1. Identify the artifact kind this rule governs
2. Determine why freshness matters for this artifact (what goes wrong when stale)
3. Find existing lifecycle rules for similar domains (search P11_feedback/examples/)
4. Research industry content lifecycle patterns for the domain
5. Check brain_query [IF MCP] for duplicate lifecycle rules
6. Determine appropriate freshness_days based on domain volatility

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill template following SCHEMA constraints
3. Fill frontmatter: all 16 required + 4 recommended fields (quality: null)
4. Set freshness_days as positive integer based on domain volatility
5. Write Definition section: what it governs and why freshness matters
6. Write States table: >= 3 states with entry criteria and duration
7. Write Transitions table: >= 3 transitions with triggers and actions
8. Write Review Protocol: reviewer, cycle, checklist, outcomes
9. Write Automation section: which transitions are automated vs manual

## Phase 3: VALIDATE
1. Check against QUALITY_GATES.md (this builder's own gates)
2. HARD: id format, kind, pillar, quality==null, freshness_days is integer, review_cycle valid
3. SOFT: states >= 3, transitions >= 3, automation defined, no subjective triggers
4. Verify: every transition trigger is measurable (not "when it feels outdated")
5. If score < 8.0: revise before outputting
