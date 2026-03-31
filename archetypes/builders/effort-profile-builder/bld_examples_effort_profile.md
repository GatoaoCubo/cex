---
kind: examples
id: bld_examples_effort_profile
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of effort_profile artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: effort-profile-builder
## Golden Example
INPUT: "Create effort profile for the agent-builder (complex reasoning tasks)"
OUTPUT:
```yaml
id: p09_effort_agent_builder_opus
kind: effort_profile
pillar: P09
version: "1.0.0"
created: "2026-03-31"
updated: "2026-03-31"
author: "builder_agent"
name: "Agent Builder Opus High"
model: "opus"
thinking_level: "high"
target_builder: "agent-builder"
quality: null
tags: [effort_profile, P09, agent-builder]
tldr: "Opus with high thinking for agent-builder — complex multi-step reasoning requires deep inference"
```
## Overview
Effort profile for agent-builder, which constructs P02 agent artifacts requiring multi-step
reasoning, persona design, and tool integration. High complexity justifies opus + high thinking.

## Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| model | opus | Agent construction requires nuanced reasoning and long-range coherence |
| thinking_level | high | Multi-step planning (persona + tools + rules) needs extended thinking |
| cost_tier | high | Justified by artifact complexity and downstream impact |
| fallback_model | sonnet | Acceptable degradation for simpler agent definitions |
| max_tokens | 8192 | Agent artifacts average 3-5KB; buffer for thinking |
| temperature | 0.3 | Low temperature for consistent, reliable output |

## Levels
| Scenario | Model | Thinking | Rationale |
|----------|-------|----------|-----------|
| Simple agent (1 tool, basic persona) | sonnet | medium | Reduced complexity allows lighter model |
| Standard agent (3+ tools, full persona) | opus | high | Default profile for most agent builds |
| Critical agent (orchestrator, multi-crew) | opus | max | Maximum reasoning for highest-impact agents |

## Integration
- Consumed by: dispatch.sh (selects CLI + model flags)
- References: agent-builder ISOs (determines build complexity)
- Pairs with: p09_rr_agent_builder (runtime rules for agent builds)
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_effort_ pattern (H02 pass)
- kind: effort_profile (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Configuration, Levels, Integration (H07 pass)
- Configuration table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "effort_profile" (S02 pass)
## Anti-Example
INPUT: "Create effort profile for formatting tasks"
BAD OUTPUT:
```yaml
id: format-effort
kind: effort
quality: 9.0
tags: [effort]
```
FAILURES:
1. id has hyphens and no p09_effort_ prefix -> H02 FAIL
2. kind: 'effort' not 'effort_profile' -> H04 FAIL
3. Missing fields: model, thinking_level, target_builder -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. No ## Configuration section in body -> H07 FAIL
6. No configuration table -> S03 FAIL
