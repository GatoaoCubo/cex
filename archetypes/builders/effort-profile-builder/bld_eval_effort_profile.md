---
kind: quality_gate
id: p11_qg_effort_profile
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of effort_profile artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: effort_profile"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, effort-profile, P09]
tldr: "Pass/fail gate for effort_profile artifacts: required fields, id pattern, body sections, configuration completeness."
domain: "effort and thinking level configuration for builder execution"
created: "2026-03-31"
updated: "2026-03-31"
density_score: 1.0
related:
  - bld_examples_effort_profile
  - p11_qg_chunk_strategy
  - p11_qg_constraint_spec
  - p03_sp_effort_profile_builder
  - p11_qg_retriever_config
  - p11_qg_memory_scope
  - p10_lr_effort_profile_builder
  - p11_qg_output_validator
  - p11_qg_handoff_protocol
  - bld_instruction_effort_profile
---

## Quality Gate

# Gate: effort_profile
## Definition
| Field | Value |
|---|---|
| metric | effort_profile artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: effort_profile` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_effort_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | id field != filename without extension |
| H04 | Kind equals literal `effort_profile` | Any other kind value |
| H05 | Quality field is null | Any non-null value |
| H06 | All required fields present | Missing model, thinking_level, target_builder, quality, tags, tldr or other required fields |
| H07 | All required body sections present | Missing ## Overview or ## Configuration or ## Levels or ## Integration |
| H08 | Body <= 4096 bytes | Body exceeds size limit |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Configuration completeness | 1.0 | Model + thinking level have concrete values (no placeholders) |
| Rationale quality | 1.0 | Each configuration value has clear rationale |
| Level mapping | 1.0 | Correct model/thinking chosen for the builder complexity |
| Boundary clarity | 1.0 | Explicitly states what this IS and IS NOT |
| Integration mapping | 0.5 | Upstream and downstream connections documented |
| Density | 1.0 | Information density >= 0.8, no filler content |
| Tags quality | 0.5 | Tags >= 3, includes "effort_profile", relevant to content |
| Tldr quality | 0.5 | Tldr <= 160 chars, dense, accurate summary |
| Domain specificity | 1.0 | Model and thinking values specific to target builder |
| Testability | 0.5 | Configuration can be validated against dispatch system |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |

## Bypass
| Field | Value |
|-------|-------|
| conditions | Experimental effort and thinking level configuration for builder execution artifact under active A/B testing |
| approver | Nucleus lead (written approval required) |
| audit_trail | Log in records/audits/ with bypass reason and timestamp |
| expiry | 48h — must pass all gates before expiry |
| never_bypass | H01 (YAML parse), H05 (quality null) |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
