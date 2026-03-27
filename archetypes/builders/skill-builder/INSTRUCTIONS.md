---
id: p03_ins_skill_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Skill Builder Instructions
target: skill-builder agent
phases_count: 4
prerequisites:
  - Capability name is defined (non-empty string, kebab-case)
  - Invocation pattern is known (slash command, keyword, event, or agent-invoked)
  - At least two distinct execution phases can be identified
  - Input and output for the skill are described
validation_method: checklist
domain: skill
quality: null
tags: [instruction, skill, phases, reusable, P04]
idempotent: true
atomic: false
rollback: Delete generated skill artifact and restart from Phase 1
dependencies: []
logging: true
tldr: Build a reusable skill artifact with a precise trigger, 2-6 atomic phases each with explicit input/output, and when-to-use contrast.
density_score: 0.90
---

## Context

The skill-builder produces `skill` artifacts — reusable capabilities defined as ordered
phases with a trigger that activates them. A skill encapsulates a repeatable process:
it has a clear entry point (trigger), a structured execution path (phases), and a defined
output. Skills are distinct from agents (which have identity) and action prompts (which are
single-turn instructions).

**Input contract**:
- `{{skill_name}}`: kebab-case capability name (e.g. `web-search`, `code-review`)
- `{{trigger_type}}`: one of `slash_command`, `keyword`, `event`, `agent-invoked`
- `{{trigger_value}}`: the exact trigger string (e.g. `/search`, `"review this"`, `on_deploy`)
- `{{user_invocable}}`: boolean — can a human trigger this directly?
- `{{phases_raw}}`: comma-separated phase names or free-text describing the process
- `{{input_description}}`: what the skill receives
- `{{output_description}}`: what the skill produces

**Output contract**: A single `skill` Markdown file with YAML frontmatter, 2-6 atomic
phases each with Input/Action/Output blocks, when_to_use and when_not_to_use lists,
concrete invocation examples, anti-patterns section, and metrics section.

**Boundaries**:
- Skill handles reusable phase-based capabilities only.
- Agent identity (who the agent IS) belongs in a system-prompt artifact.
- Single-turn task instructions belong in an action_prompt artifact.
- Event-driven hooks (triggered by file/tool events) are a separate hook artifact.
- MCP server tool exposure belongs in an mcp_server artifact.

---

## Phases

### Phase 1: Analyze Capability and Trigger

**Primary action**: Understand the capability's domain, decompose it into executable
phases, and define the precise trigger.

```
INPUT: skill_name, trigger_type, trigger_value, user_invocable, phases_raw

1. Validate skill_name:
   Must be kebab-case, lowercase: ^[a-z][a-z0-9-]+$
   Derive id: p04_skill_{{skill_name_with_underscores}}

2. Classify the capability domain:
   domain_type = "data" | "code" | "communication" | "analysis" | "orchestration"

3. Trigger specification:
   trigger = {
     type: {{trigger_type}},
     value: {{trigger_value}},
     user_invocable: {{user_invocable}},
     description: one sentence — "Activates when [condition]"
   }

   Trigger precision rules:
     slash_command: must start with "/" and be unique in the system
     keyword:       must be specific enough to not trigger accidentally
     event:         must be an observable system event (not a vague condition)
     agent-invoked: must name the calling agent and the invocation condition

4. Phase decomposition from phases_raw:
   phase_list = parse phases_raw into named phases (2-6 required)
   for each phase:
     phase_entry = {
       name: short verb phrase (e.g. "Discover", "Configure", "Execute", "Validate"),
       position: integer (1-based),
       atomic: true  # each phase does ONE primary action
     }

   Validate atomicity: if a phase does two distinct things, split it.
   Validate sequence: phases must be ordered (each builds on previous output).

OUTPUT: validated_id, domain_type, trigger{}, phase_list[] (2-6 phases, atomic)
```

Verification: `phase_list` has 2-6 entries. Each phase has a single primary action.
Trigger value is specific and unambiguous.

---

### Phase 2: Define Phase Input/Output

**Primary action**: For each phase, write explicit Input, Action, and Output blocks
that make the data flow unambiguous.

```
INPUT: phase_list[], input_description, output_description

1. Map data flow across phases:
   Phase 1 Input  = skill's overall {{input_description}}
   Phase N Output = Phase N+1 Input (chaining)
   Last Phase Output = skill's overall {{output_description}}

2. For each phase in phase_list:
   phase_spec = {
     name: phase.name,
     input: what data this phase receives (concrete, not vague),
     action: the single primary action (imperative verb phrase),
     output: what data this phase produces (concrete, not vague),
     tools: list of tools/commands used (empty list if none)
   }

   Action verb rules:
     Use active imperative: "Search for...", "Parse...", "Write..."
     Do NOT use: "Handle", "Process", "Deal with" (too vague)

3. Validate phase chain continuity:
   for each consecutive pair (phase_N, phase_N+1):
     if phase_N.output does not match phase_N+1.input:
       add an explicit transformation note between phases

4. Identify sub-skills this skill may delegate to:
   sub_skills = [] (list any existing skills this skill calls)

OUTPUT: phase_specs[] with input/action/output for each, sub_skills[]
```

Verification: every phase has non-empty input, action, and output. Output of phase N
is compatible with input of phase N+1.

---

### Phase 3: Write Usage Guidance and Examples

**Primary action**: Produce the when_to_use and when_not_to_use lists, at least 3
concrete invocation examples, anti-patterns, and metrics.

```
INPUT: trigger{}, phase_specs[], domain_type, skill_name

1. when_to_use (list of conditions, parallel grammatical structure):
   - At least 3 concrete conditions
   - Each condition is observable (not "when you feel like it")
   - Pattern: "When [observable condition]..."

2. when_not_to_use (list of exclusions, same abstraction level):
   - At least 3 exclusions
   - Each references a competing artifact or simpler alternative
   - Pattern: "When [condition] — use [alternative] instead"

3. Invocation examples (minimum 3, concrete):
   example = {
     trigger_call: exact string the user or agent types/sends,
     context: one sentence describing the situation,
     expected_output: what the skill produces
   }

4. Anti-patterns section (minimum 3 named failures):
   anti_pattern = {
     name: short label (e.g. "Skipping Phase 2"),
     description: what goes wrong when this happens,
     symptom: how to recognize it,
     fix: how to avoid it
   }

5. Metrics section (minimum 2 measurable success criteria):
   metric = {
     name: short label,
     measurement: how to measure it (specific, not "check quality"),
     threshold: numeric or boolean success value
   }

OUTPUT: when_to_use[], when_not_to_use[], examples[], anti_patterns[], metrics[]
```

Verification: `when_to_use` has >= 3 entries. `when_not_to_use` has >= 3 entries.
`examples` has >= 3 concrete invocations. `anti_patterns` has >= 3 entries.
`metrics` has >= 2 measurable criteria.

---

### Phase 4: Assemble Artifact and Validate

**Primary action**: Combine all phase outputs into the final skill Markdown file and run
quality gates.

```
INPUT: validated_id, trigger, phase_specs, when_to_use, when_not_to_use,
       examples, anti_patterns, metrics, sub_skills

1. Assemble frontmatter (12+ required fields):
   id: p04_skill_{{skill_name_underscored}}
   kind: skill
   pillar: P04
   version: 1.0.0
   trigger_type: {{trigger_type}}
   trigger_value: {{trigger_value}}
   user_invocable: {{user_invocable}}
   phases: [list of phase names in order]
   domain: {{domain_type}}
   sub_skills: {{sub_skills}}
   quality: null

2. Write body sections in order:
   ## Overview        — 2-3 sentences: what, when triggered, what it produces
   ## When to Use     — when_to_use list
   ## When NOT to Use — when_not_to_use list
   ## Workflow Phases — one subsection per phase with Input/Action/Output
   ## Examples        — numbered invocation examples
   ## Anti-Patterns   — named failure modes
   ## Metrics         — measurable success criteria

3. Size check: body must be <= 5120 bytes.
   If over: trim examples to 3, trim anti_patterns to 3, trim metrics to 2.

4. Run HARD quality gates (all must pass):
   HARD_1: id matches ^p04_skill_[a-z][a-z0-9_]+$
   HARD_2: kind == "skill"
   HARD_3: quality == null
   HARD_4: phases frontmatter list matches ## Workflow Phases subsections exactly
   HARD_5: phase count is between 2 and 6 inclusive
   HARD_6: trigger_value is non-empty and specific
   HARD_7: body <= 5120 bytes

5. Run SOFT quality gates (>= 7 of 10 must pass):
   when_to_use has >= 3 entries, when_not_to_use has >= 3 entries,
   examples has >= 3, anti_patterns has >= 3, metrics has >= 2,
   each phase has non-empty input/action/output, no identity language in body,
   trigger is unambiguous, phases are non-overlapping, sub_skills documented.

OUTPUT: skill Markdown file, gate_results{}, size_bytes
```

Verification: all 7 HARD gates pass. Body <= 5120 bytes.

---

## Output Contract

```markdown
---
id: p04_skill_{{skill_name_underscored}}
kind: skill
pillar: P04
version: 1.0.0
created: {{created_date}}
updated: {{updated_date}}
author: skill-builder
trigger_type: {{trigger_type}}
trigger_value: {{trigger_value}}
user_invocable: {{user_invocable}}
phases: [{{phase_1_name}}, {{phase_2_name}}, {{phase_N_name}}]
domain: {{domain_type}}
sub_skills: [{{sub_skill_1_or_empty}}]
quality: null
---

# {{skill_name}} Skill

## Overview
{{overview_2_to_3_sentences}}

## When to Use
- {{when_to_use_1}}
- {{when_to_use_2}}
- {{when_to_use_3}}

## When NOT to Use
- {{when_not_to_use_1}}
- {{when_not_to_use_2}}
- {{when_not_to_use_3}}

## Workflow Phases

### Phase 1: {{phase_1_name}}
**Input**: {{phase_1_input}}
**Action**: {{phase_1_action}}
**Output**: {{phase_1_output}}

### Phase N: {{phase_N_name}}
**Input**: {{phase_N_input}}
**Action**: {{phase_N_action}}
**Output**: {{phase_N_output}}

## Examples

1. **{{example_1_trigger}}**
   Context: {{example_1_context}}
   Output: {{example_1_output}}

[repeat for examples 2 and 3]

## Anti-Patterns

### {{anti_pattern_1_name}}
{{description}} | Symptom: {{symptom}} | Fix: {{fix}}

[repeat for anti-patterns 2 and 3]

## Metrics

| Metric | Measurement | Threshold |
|--------|-------------|-----------|
| {{metric_1_name}} | {{measurement_1}} | {{threshold_1}} |
| {{metric_2_name}} | {{measurement_2}} | {{threshold_2}} |
```

---

## Validation

- [ ] HARD: `id` matches `^p04_skill_[a-z][a-z0-9_]+$`
- [ ] HARD: `kind` equals `skill`
- [ ] HARD: `quality` equals `null`
- [ ] HARD: `phases` frontmatter list matches `## Workflow Phases` subsections exactly
- [ ] HARD: phase count is between 2 and 6 inclusive
- [ ] HARD: `trigger_value` is non-empty and specific
- [ ] HARD: body size is <= 5120 bytes
- [ ] SOFT: `when_to_use` has >= 3 entries
- [ ] SOFT: `when_not_to_use` has >= 3 entries
- [ ] SOFT: `examples` has >= 3 concrete invocations
- [ ] SOFT: `anti_patterns` has >= 3 named failure modes
- [ ] SOFT: `metrics` has >= 2 measurable success criteria
- [ ] SOFT: each phase has non-empty input, action, and output
- [ ] SOFT: no identity language in body (no "I am", "my role is")
- [ ] SOFT: trigger is unambiguous and cannot fire accidentally
- [ ] SOFT: phases are non-overlapping (each does exactly one thing)
- [ ] SOFT: `sub_skills` field is documented (empty list if none)

**Score threshold**: All 7 HARD gates must pass. >= 7 of 10 SOFT gates for pool eligibility.

---

## Metacognition

**Does**:
- Build reusable capabilities with structured phases and precise triggers
- Define clear input/output contracts for every phase
- Distinguish user-invocable (slash command) from agent-invoked (programmatic) triggers
- Enforce phase atomicity — each phase does exactly one thing
- Produce usage guidance: when to use, when not to use, anti-patterns

**Does NOT**:
- Author agent identity or system prompts (system-prompt artifact)
- Create single-turn task instructions (action_prompt artifact)
- Define event-driven hooks triggered by file or tool events (hook artifact)
- Expose tools via a protocol (mcp_server artifact)

**Chaining**:
- Before: capability analysis or user request identifies what skill is needed
- After: agents invoke this skill by its trigger during task execution
- After: other skills may list this skill in their `sub_skills` dependency
- After: an action_prompt may reference this skill for multi-phase tasks
