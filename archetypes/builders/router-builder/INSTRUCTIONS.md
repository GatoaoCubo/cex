---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for router artifact
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a router

## Phase 1: RESEARCH
1. Identify the routing domain (what category of tasks are being routed)
2. List all possible destinations (satellites, agents, or services)
3. Define patterns that distinguish each destination (keywords, regex, intent)
4. Determine priority ordering among routes
5. Set confidence thresholds per route (stricter for critical destinations)
6. Define fallback destination for unmatched tasks
7. Search for existing routers via brain_query [IF MCP] (avoid duplicates)
8. Identify escalation scenarios (ambiguous matches, low confidence, conflicts)

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Generate router_slug in snake_case (e.g., satellite_task_router)
4. Fill frontmatter: all 14 required fields (quality: null, never self-score)
5. Set fallback_route to a valid destination
6. Set confidence_threshold (default 0.7)
7. Write Routes section: table with pattern, destination, priority, confidence_min
8. Write Decision Logic section: algorithm description
9. Write Fallback section: what happens when no route matches
10. Write Escalation section: ambiguous match handling
11. Write Integration section: how router connects to dispatch_rules and agents
12. Set routes_count to match actual rows in Routes table
13. Check body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. Verify all 8 HARD gates pass
3. Score each SOFT gate against QUALITY_GATES.md
4. Confirm id matches p02_router_ pattern
5. Confirm kind == router
6. Confirm quality == null
7. Confirm routes_count matches actual route table rows
8. Confirm confidence_threshold is between 0.0 and 1.0
9. Confirm fallback_route is set (not blank)
10. If score < 8.0: revise before outputting
