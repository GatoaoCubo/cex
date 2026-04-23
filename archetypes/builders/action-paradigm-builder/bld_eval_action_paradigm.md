---
kind: quality_gate
id: p11_qg_action_paradigm
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for action_paradigm artifacts
quality: 9.1
title: "Quality Gate: Action Paradigm"
version: "1.0.0"
author: n02_reviewer
tags: [action_paradigm, builder, quality_gate, P11]
tldr: "Quality gate for action execution paradigm artifacts defining state-action mappings, preconditions, and failure recovery."
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - p11_qg_collaboration_pattern
  - p11_qg_quality_gate
  - p11_qg_response_format
  - p11_qg_voice_pipeline
  - p11_qg_runtime_state
  - p03_sp_action_paradigm_builder
  - p11_qg_thinking_config
  - p11_qg_prompt_template
  - bld_examples_action_paradigm
  - p11_qg_creation_artifacts
---

## Quality Gate
## Definition
An `action_paradigm` artifact defines how an autonomous agent translates high-level goals
into executable actions within dynamic environments. It specifies state-action mappings,
preconditions, postconditions, failure recovery, and concurrency rules -- not runtime
performance metrics.

Scope: files with `kind: action_paradigm`. Does NOT apply to agent definitions (agent),
workflow sequences (workflow), or tool wrappers (cli_tool).

## HARD Gates
Failure on any single gate means REJECT regardless of soft score.

| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p04_act_*` | `id.startswith("p04_act_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `action_paradigm` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr all present |
| H07 | Body contains `action_type` field or section | at least one action classification declared |
| H08 | At least one precondition or postcondition defined | `re.search(r'precondition|postcondition|pre_condition|post_condition', body, re.I)` matches |

## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.

| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Action space explicitly defined (discrete, continuous, or symbolic classification) | 1.0 |
| 3  | Failure recovery or error handling mechanism documented | 1.0 |
| 4  | State transition logic present (preconditions + postconditions) | 1.0 |
| 5  | Execution model specified (reactive, deliberative, or hybrid) | 0.5 |
| 6  | Concurrency rules or conflict resolution documented | 0.5 |
| 7  | Tags include `action_paradigm` | 0.5 |
| 8  | Boundary note: distinguishes from workflow (sequential) and cli_tool (interface) | 1.0 |
| 9  | At least one concrete use case or domain example | 1.0 |
| 10 | Resource constraints or execution limits declared | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |

**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 9.0. Score range: 0.0 to 10.0.

## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool; add to curated paradigm library |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required |

## Bypass
| Field | Value |
|-------|-------|
| condition | Paradigm is a one-off proof-of-concept with documented lifespan under 30 days |
| approver | Domain lead must approve in writing |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, reason |
| expiry | 30 days from bypass grant; paradigm must be retired or brought to full compliance |

## Properties
| Property | Value |
|----------|-------|
| Kind | `quality_gate` |
| Pillar | P11 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Examples
## Evaluation Criteria
| Dimension | Floor | Target | How to Measure |
|-----------|-------|--------|---------------|
| action_type declared | required | explicit enum value | present in frontmatter or section header |
| preconditions per action | >=1 | >=2 | count guard conditions per action entry |
| postconditions per action | >=1 | >=2 | count state-change assertions per action |
| failure recovery present | required | per-action | at least one fallback per action defined |
| concurrency model | required | explicit | conflict resolution policy stated |
| state machine completeness | >=80% | 100% | all reachable states have transitions |

## Paradigm Type Reference
| Type | Decision Latency | Planning Horizon | Best For |
|------|-----------------|-----------------|----------|
| Reactive | <10ms | None (sensor-direct) | Safety-critical real-time systems |
| Deliberative | 100ms-10s | Full plan before act | Complex goal-directed tasks |
| Hybrid | 10-100ms | Short lookahead | Robots, game agents, autonomous vehicles |
| Hierarchical | Variable per layer | Per abstraction level | Multi-goal, multi-agent coordination |

---

## Golden Example 1: Reactive Autonomous Navigation
```markdown
---
id: p04_act_autonomous_nav_v1
kind: action_paradigm
title: "Reactive Navigation for Mobile Robot"
paradigm_type: reactive
version: 1.0.0
---

## Paradigm Overview
Reactive control loop with prioritized action selection.
Decision cycle: 100ms. Safety actions always override efficiency actions.

## State-Action Table
| State | Precondition | Action | Postcondition | Priority |
|-------|-------------|--------|--------------|----------|
| obstacle_detected | distance < 0.5m | emergency_brake | velocity = 0, alert_sent | P0 (safety) |
| obstacle_detected | 0.5m <= distance < 2m | reduce_speed | velocity <= 0.3 m/s | P1 |
| path_blocked | obstacle_static > 3s | replan_route | new_path_loaded | P2 |
| path_clear | distance > 2m | navigate_forward | position_updated | P3 |
| battery_low | charge < 15% | return_to_dock | dock_requested | P2 |

## Concurrency Model
Conflict resolution: Priority-order wins. If two actions have equal priority,
the one with lower estimated execution time executes first.
Resource lock: motor_controller held for duration of any movement action.

## Failure Recovery
| Failure Mode | Detection | Recovery Action | Timeout |
|-------------|-----------|----------------|---------|
| sensor_timeout | no data > 500ms | halt + alert ops | 5s |
| motor_fault | encoder mismatch | stop + diagnostic | immediate |
| replan_failure | no path found in 3 attempts | request_human_handoff | 30s |
| comms_lost | heartbeat missing > 2s | safe_stop + local_nav | 10s |
```

---

## Golden Example 2: Deliberative Content Moderation Agent
```markdown
---
id: p04_act_content_mod_v2
kind: action_paradigm
title: "Deliberative Content Moderation Paradigm"
paradigm_type: deliberative
version: 2.1.0
---

## Paradigm Overview
Full content analysis before any action. Every decision is logged.
Latency budget: 800ms. Accuracy target: 99.2% precision on policy violations.

## State-Action Table
| State | Precondition | Action | Postcondition | Confidence Threshold |
|-------|-------------|--------|--------------|---------------------|
| content_received | score unavailable | run_classifier | score in [0.0, 1.0] | n/a |
| low_risk | score < 0.30 | approve_content | content_visible=true, log_entry=created | n/a |
| medium_risk | 0.30 <= score < 0.70 | queue_human_review | review_queued, content_hidden | >0.65 auto-approve |
| high_risk | score >= 0.70 | auto_remove | content_visible=false, appeal_created | n/a |
| appeal_submitted | human_reviewed=false | escalate_review | reviewer_assigned, sla_timer_started | n/a |

## Failure Recovery
| Failure Mode | Detection | Recovery | Max Retries |
|-------------|-----------|----------|-------------|
| classifier_timeout | >800ms elapsed | fallback to human_review queue | 1 |
| model_unavailable | HTTP 503 | queue all items, alert on-call | 0 (immediate alert) |
| false_positive_spike | FP rate > 0.02 in 5min window | pause auto_remove, alert team | 0 |
| appeal_backlog | queue depth > 500 | auto-approve low_medium pending | n/a |
```

---

## Golden Example 3: Hybrid Game Agent
```markdown
---
id: p04_act_game_agent_v1
kind: action_paradigm
title: "Hybrid FPS Game Agent Paradigm"
paradigm_type: hybrid
version: 1.0.0
---

## Paradigm Overview
Two-tier: reactive layer (combat, sub-50ms) + deliberative layer (strategy, 200ms).
Reactive layer can interrupt deliberative actions. Deliberative layer runs in background.

## Layer Interaction
| Layer | Trigger | Max Latency | Can Interrupt | Interrupted By |
|-------|---------|-------------|--------------|----------------|
| Reactive | enemy_sighted, damage_taken | 50ms | Deliberative | Never |
| Deliberative | idle > 1s, objective_updated | 200ms | Nothing | Reactive |

## State-Action Table (Reactive Layer)
| State | Precondition | Action | Postcondition |
|-------|-------------|--------|--------------|
| enemy_sighted | health > 20% | engage_combat | target_locked, weapon_drawn |
| enemy_sighted | health <= 20% | retreat_to_cover | cover_position_reached |
| damage_taken | cover_available | take_cover | damage_exposure reduced 70% |
| damage_taken | no_cover | zigzag_retreat | distance_from_enemy += 10m |

## Failure Recovery
| Mode | Detection | Recovery |
|------|-----------|----------|
| pathfinding_fail | no_path in 3 attempts | random_walk + re-query in 500ms |
| target_lost | enemy_not_visible > 2s | patrol_last_known_position |
| stuck | position_delta < 0.1m over 2s | jump + direction_change |
```

---

## Anti-Example 1: Overly Vague
```markdown
---
title: "Generic Action Paradigm"
kind: action_paradigm
description: "Agents do things in environments."
---

**Paradigm**: "Do actions when needed."

**Steps**:
1. Wait
2. Do something
3. Repeat
```

**Why it fails**

| Deficiency | Missing Element | Required Instead |
|-----------|----------------|-----------------|
| No action_type | paradigm_type field absent | one of: reactive/deliberative/hybrid/hierarchical |
| No preconditions | "when needed" is not a guard condition | explicit state checks for each action |
| No postconditions | no state change defined | what is true after action executes |
| No failure recovery | no fallback for any action | at least one recovery path per action |
| No concurrency model | parallel actions undefined | conflict resolution policy required |

---

## Anti-Example 2: Protocol Confusion
```markdown
---
title: "REST API Action Paradigm"
kind: action_paradigm
description: "Agents use HTTP requests to perform actions."
---

**Paradigm**: Send POST to `/act` with JSON payload.

**Steps**:
1. Client sends `{"action": "move", "params": {}}`
2. Server returns `200 OK` or error code
3. Client waits for response
```

**Why it fails**

| Deficiency | Root Cause | Correct Kind |
|-----------|-----------|-------------|
| Describes transport protocol, not agent behavior | action_paradigm != agent_computer_interface | Use agent_computer_interface (P08) for protocol |
| No agent reasoning model | how the agent decides "move" is unspecified | action_paradigm must describe decision logic |
| No state machine | input/output pairs are not state transitions | must define states, not just API calls |
| No failure recovery | HTTP error code != behavioral fallback | define what agent does on each failure mode |

---

## Scoring Checklist
| Gate | Passing Condition | Weight |
|------|-----------------|--------|
| H01: paradigm_type declared | field present, value in enum | 15% |
| H02: state-action table | >= 4 rows with preconditions + postconditions | 20% |
| H03: failure recovery | >= 3 failure modes documented | 20% |
| H04: concurrency model | conflict resolution policy stated | 15% |
| H05: no protocol confusion | paradigm describes behavior, not transport | 15% |
| H06: portable design | no environment-specific hardcoding | 15% |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
