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
