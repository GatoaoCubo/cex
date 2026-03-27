---
id: p03_ins_mental_model
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Mental Model Builder Execution Protocol
target: mental-model-builder agent
phases_count: 4
prerequisites:
  - Target agent name and domain are identified
  - Primary routing patterns (what triggers what) are describable
  - Agent's key decision points during operation are known
validation_method: checklist
domain: mental_model
quality: null
tags: [instruction, mental-model, routing, P02, decision-tree, cognitive-map]
idempotent: true
atomic: false
rollback: "Discard generated artifact; agent behavior is unchanged"
dependencies: []
logging: true
tldr: Build a cognitive map for an agent defining routing rules, decision trees, priorities, heuristics, domain boundaries, and fallback behavior.
density_score: 0.91
---

## Context

The mental-model-builder produces `mental_model` artifacts (P02) — design-time cognitive maps that define how an agent routes tasks, makes decisions, and prioritizes work. Mental models differ from agent definitions (identity and capabilities), runtime state (P10, ephemeral), and router artifacts (pure task dispatchers): a mental model encodes the thinking patterns an agent uses during execution.

**Inputs:**

- `$agent_name (required) - string - "The agent this mental model belongs to (e.g. 'scout-agent', 'law-builder')"`
- `$agent_slug (required) - string - "snake_case version of agent name for use in id field"`
- `$domain (required) - string - "Primary domain the agent operates in"`
- `$routing_triggers (required) - list[string] - "Keywords or signal types that trigger this agent's activation"`
- `$decisions (optional) - list[string] - "Key binary or multi-path decisions the agent makes during operation"`
- `$domain_map (optional) - object - "What the agent covers vs what it delegates; keys: covers, routes_to"`

**Output:** A single `mental_model` artifact (P02), body <= 2048 bytes, with 14 required + 9 recommended frontmatter fields and body sections covering agent reference, routing rules, decision tree, priorities, heuristics, domain map, and fallback.

**Boundary check before proceeding:**
- Need to define the agent's identity and capabilities → route to agent-builder
- Need to define runtime state → do not use mental_model (P02), use P10 runtime state
- Need a pure task dispatcher with no domain logic → route to router-builder (planned)
- Need to encode how an agent thinks, routes, and decides → proceed

---

## Phases

### Phase 1: Analyze

**Action:** Gather and organize the cognitive parameters of the target agent.

1. Identify the **target agent** by name and domain.
2. Determine primary **routing patterns**: what input signals trigger what agent behaviors.
3. List **key decisions** the agent makes — binary or multi-path choices at decision points.
4. Identify **priority ordering**: what takes precedence when multiple tasks or signals compete.
5. Collect **heuristics**: actionable rules of thumb derived from the agent's operational patterns.
6. Map **domain boundaries**:
   - `covers`: what this agent handles directly
   - `routes_to`: what this agent delegates, and to which other agents
7. Check for existing mental_models for the same agent — avoid duplicates.
8. Confirm this is P02 (design-time cognitive map), NOT P10 (runtime state).
9. Define `fallback`: what the agent does when no routing rule matches.

**Verification:** You can describe the agent's routing in one sentence: "When [signal type], this agent does [action]; when [other signal], it routes to [other agent]."

### Phase 2: Compose

**Action:** Write all frontmatter fields and body sections within the 2048-byte body limit.

1. Read `SCHEMA.md` — source of truth for all 14 required + 9 recommended fields.
2. Read `OUTPUT_TEMPLATE.md` — fill every `{{var}}` following SCHEMA constraints.
3. Generate `agent_slug` in snake_case from the agent name.
4. Fill frontmatter: all 14 required fields (`quality: null`).
5. Build `routing_rules`: list of >= 3 rules, each with: `keywords` (list), `action` (string), `confidence` (float 0.0–1.0).
6. Build `decision_tree`: list of >= 2 conditions, each with: `condition` (string), `then` (string), `else` (string).
7. Set `priorities`: ordered list, highest priority first.
8. Set `heuristics`: list of actionable rules of thumb (not observations — each must guide a choice).
9. Set `domain_map`: object with `covers` (list) and `routes_to` (dict: domain → agent).
10. Set `personality`: object with `tone`, `verbosity`, `risk_tolerance`.
11. Set `constraints`: list of hard behavioral limits the agent must never violate.
12. Set `fallback`: object with `action` (what to do) and `escalate_to` (who to ask).
13. Write `## Agent Reference` — one-line identity: who this agent is and its primary function.
14. Write `## Routing Rules` — table with columns: Keywords | Action | Confidence.
15. Write `## Decision Tree` — numbered if/then/else list.
16. Write `## Priorities` — ordered list, highest first.
17. Write `## Heuristics` — actionable rules of thumb.
18. Write `## Domain Map` — what this agent covers vs routes to others.

Byte budget pseudocode:
```
body_bytes = len(encode_utf8(body_content))
# if body_bytes > 2048: compress heuristics, merge similar routing rules
```

**Verification:** `routing_rules` has >= 3 rules. `decision_tree` has >= 2 conditions, each with `condition`, `then`, and `else`. Body <= 2048 bytes. Keywords in routing rules are specific (not "general" or "anything").

### Phase 3: Validate

**Action:** Run all 9 HARD gates from `QUALITY_GATES.md`. Fix any failure before output.

| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches pattern `^p02_mm_[a-z][a-z0-9_]+$` |
| H03 | `kind` is literal string `mental_model` |
| H04 | `pillar` is `P02` (NOT P10) |
| H05 | `quality` is `null` |
| H06 | `routing_rules` has >= 3 rules each with keywords + action |
| H07 | `decision_tree` has >= 2 conditions each with condition + then |
| H08 | Keywords in routing_rules are specific (no "general", "anything", "other") |
| H09 | Body <= 2048 bytes |

Score SOFT gates from `QUALITY_GATES.md`. If soft score < 8.0, revise in the same pass.

**Cross-check:** Are heuristics actionable (guide a choice) rather than purely descriptive? Does `domain_map.routes_to` name specific agent destinations?

### Phase 4: Output

**Action:** Emit the final artifact at the correct path.

1. Write file to the path defined in `CONFIG.md` for mental_model artifacts.
2. Confirm filename stem matches `id` field.
3. Confirm all body sections are present and non-empty.
4. Confirm `routing_rules` frontmatter matches routing content in body.

---

## Output Contract

```
---
id: p02_mm_{{agent_slug}}
kind: mental_model
pillar: P02
version: 1.0.0
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
author: {{author}}
domain: {{domain}}
agent_name: "{{agent_name}}"
routing_rules:
  - keywords: [{{keyword_list}}]
    action: "{{action}}"
    confidence: {{0.0-1.0}}
decision_tree:
  - condition: "{{condition}}"
    then: "{{then_action}}"
    else: "{{else_action}}"
priorities: [{{ordered_list_highest_first}}]
heuristics: [{{actionable_rules_of_thumb}}]
domain_map:
  covers: [{{what_agent_handles}}]
  routes_to:
    {{domain}}: "{{target_agent}}"
personality:
  tone: {{tone}}
  verbosity: {{low|medium|high}}
  risk_tolerance: {{low|medium|high}}
constraints: [{{hard_behavioral_limits}}]
fallback:
  action: "{{what_to_do_when_no_rule_matches}}"
  escalate_to: "{{who_to_ask}}"
tags: [mental-model, P02, {{domain_tag}}, routing]
quality: null
---

## Agent Reference
{{one_line_identity_and_primary_function}}

## Routing Rules
| Keywords | Action | Confidence |
|----------|--------|------------|
{{minimum_3_rows}}

## Decision Tree
{{numbered_if_then_else_list_minimum_2_conditions}}

## Priorities
{{ordered_list_highest_first}}

## Heuristics
{{actionable_rules_of_thumb}}

## Domain Map
{{covers_and_routes_to}}
```

---

## Validation

- [ ] `id` matches `^p02_mm_[a-z][a-z0-9_]+$`
- [ ] `kind` is literal string `mental_model`
- [ ] `pillar` is `P02` (not P10)
- [ ] `quality` is `null`
- [ ] `routing_rules` has >= 3 rules with keywords + action
- [ ] `decision_tree` has >= 2 conditions with condition + then + else
- [ ] Keywords are specific (no "general", "anything", "other")
- [ ] All body sections present and non-empty
- [ ] Body <= 2048 bytes
- [ ] Soft gate score >= 8.0 before output

---

## Metacognition

**Does:**
- Encode routing rules, decision trees, and priorities for a specific agent
- Enforce specificity in routing keywords (rejects vague terms)
- Define domain boundaries: what the agent covers vs delegates

**Does NOT:**
- Define agent identity or capabilities — route to agent-builder
- Capture runtime state — that is P10, not P02
- Handle pure task dispatching with no domain logic — route to router-builder (planned)

**Chaining:** [agent design / capability audit] -> THIS -> [agent instantiation / routing index registration]
