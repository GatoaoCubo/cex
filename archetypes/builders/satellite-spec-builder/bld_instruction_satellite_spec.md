---
id: p03_ins_satellite_spec_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Satellite Spec Builder Instructions
target: satellite-spec-builder agent
phases_count: 4
prerequisites:
  - Satellite name is defined (non-empty string, kebab-case)
  - Primary domain or responsibility is stated
  - At least one tool or MCP server is identified
  - Target LLM model family is known (e.g. opus, sonnet, haiku)
validation_method: checklist
domain: satellite_spec
quality: null
tags: [instruction, satellite-spec, architecture, P08]
idempotent: true
atomic: false
rollback: Delete generated satellite_spec file and restart from Phase 1
dependencies: []
logging: true
tldr: Build a complete satellite_spec covering role, model, MCPs, boot sequence, constraints, dispatch rules, and scaling.
density_score: 0.91
---

## Context

The satellite-spec-builder produces `satellite_spec` artifacts — complete architectural
specifications for an autonomous agent satellite. A satellite_spec defines everything needed
to instantiate, operate, and monitor a satellite: its role, model, MCP servers, boot sequence,
constraints, dispatch rules, and scaling configuration.

**Input contract**:
- `{{satellite_name}}`: kebab-case identifier (e.g. `research-sat`, `build-sat`)
- `{{domain}}`: primary operational domain (e.g. `web_research`, `code_generation`)
- `{{model}}`: LLM model identifier (e.g. `claude-opus-4`, `claude-sonnet-4`)
- `{{tools_list}}`: comma-separated list of MCP servers or built-in tools
- `{{constraints_raw}}`: free-text description of operational boundaries

**Output contract**: A single `satellite_spec` YAML file with 24+ frontmatter fields,
a narrative identity section, and structured subsections for boot sequence, dispatch rules,
constraints, and monitoring.

**Boundaries**:
- Handles full satellite architecture only.
- Individual agent identity belongs in a separate agent artifact.
- Per-provider boot configuration belongs in a boot_config artifact.
- Reusable operation patterns belong in pattern artifacts.

---

## Phases

### Phase 1: Analyze Role and Boundary

**Primary action**: Define the satellite's operational role and establish what it does
versus what it explicitly does not do.

```
INPUT: satellite_name, domain, constraints_raw

1. Express the satellite's single primary function:
   role_statement = "{{satellite_name}} is responsible for [ONE THING]"
   Reject vague roles like "general purpose" or "multi-domain"

2. Map the NOT-domain boundary:
   for each adjacent domain in [research, build, execute, monitor, orchestrate, store]:
     if domain != satellite's primary domain:
       add to NOT_HANDLES list with brief reason
   Minimum 2 entries required.

3. Determine LLM function type:
   if satellite makes decisions     -> BECOME
   if satellite calls external tools -> CALL
   if satellite coordinates others  -> COLLABORATE
   if satellite injects context     -> INJECT

4. Extract capability_keywords (5-10 terms) from domain description.

OUTPUT: role_statement, not_handles[], llm_function, capability_keywords[]
```

Verification: `role_statement` is one sentence. `not_handles` has >= 2 entries.

---

### Phase 2: Specify Model and Tools

**Primary action**: Select and document the model configuration and MCP server bindings.

```
INPUT: model, tools_list, role_statement

1. Model specification:
   model_config = {
     id: {{model}},
     context_window: lookup by family (opus=200k, sonnet=200k, haiku=200k),
     temperature: 0.3 for deterministic tasks | 0.7 for creative tasks,
     max_tokens: sized to expected output
   }

2. MCP server binding for each tool in tools_list:
   mcp_entry = {
     name: tool_name,
     transport: "stdio" | "http",
     required: true | false,
     fallback: null | alternative_tool
   }

3. Boot sequence (ordered list):
   boot_steps = [
     "load system prompt",
     "initialize MCP connections",
     "verify tool availability",
     "load domain context",
     "ready"
   ]
   Add satellite-specific steps between generic ones.
   Assign estimated duration in seconds to each step.

4. boot_time_seconds = sum(step durations)

OUTPUT: model_config{}, mcp_bindings[], boot_sequence[], boot_time_seconds
```

Verification: each MCP entry has `transport` and `required` fields.
`boot_sequence` has >= 4 steps.

---

### Phase 3: Define Dispatch and Constraints

**Primary action**: Specify how the satellite receives work, what it accepts or rejects,
and its operational limits.

```
INPUT: constraints_raw, capability_keywords[], role_statement

1. Dispatch rules:
   dispatch = {
     triggers: [keywords that route tasks here],  # >= 3 required
     input_format: "handoff_file" | "inline_prompt" | "both",
     max_prompt_chars: 200 if inline else null,
     priority: "normal" | "high" | "low"
   }

2. Constraint extraction from constraints_raw:
   hard_constraints = []   # things the satellite MUST NEVER do
   soft_constraints = []   # things the satellite SHOULD prefer
   for each sentence in constraints_raw:
     if NEVER/MUST NOT/FORBIDDEN -> hard_constraint
     if PREFER/AVOID/MINIMIZE    -> soft_constraint

3. Scaling configuration:
   scaling = {
     max_parallel_instances: 1 | 2 | 3,
     shared_resources: [resources that conflict if parallel],
     cooldown_seconds: wait time between sequential runs
   }

4. Monitoring spec:
   monitoring = {
     signal_on_complete: true,
     signal_on_error: true,
     heartbeat_interval_seconds: null | integer,
     log_level: "info" | "debug" | "error"
   }

OUTPUT: dispatch{}, hard_constraints[], soft_constraints[], scaling{}, monitoring{}
```

Verification: `dispatch.triggers` has >= 3 keywords. `hard_constraints` is non-empty.

---

### Phase 4: Assemble and Validate Artifact

**Primary action**: Combine all phase outputs into the final satellite_spec YAML and run
quality gates.

```
INPUT: all outputs from Phases 1-3

1. Assemble frontmatter with 24+ required fields (id, kind, pillar, version,
   created, domain, model, llm_function, boot_time_seconds, context_window,
   temperature, max_tokens, dispatch_triggers, input_format, max_prompt_chars,
   max_parallel_instances, cooldown_seconds, signal_on_complete, signal_on_error,
   log_level, tags, quality=null, and remaining fields from phase outputs).

2. Write narrative identity section (3-5 sentences):
   Include domain, model, primary capability, and not_handles boundary.

3. Run HARD quality gates (all must pass):
   HARD_1:  id matches ^[a-z][a-z0-9-]*-spec$
   HARD_2:  kind == "satellite_spec"
   HARD_3:  model field is non-empty string
   HARD_4:  boot_sequence has >= 4 steps
   HARD_5:  dispatch.triggers has >= 3 entries
   HARD_6:  hard_constraints is non-empty list
   HARD_7:  monitoring.signal_on_complete == true
   HARD_8:  not_handles list has >= 2 entries
   HARD_9:  mcp_bindings list is non-empty
   HARD_10: version matches semantic version pattern X.Y.Z

4. Run SOFT quality gates (>= 7 of 10 must pass):
   boot_time_seconds estimated, temperature set, max_tokens set,
   max_parallel_instances defined, cooldown_seconds set,
   capability_keywords present, fallback defined for required tools,
   log_level specified, heartbeat configured or explicitly null,
   domain matches recognized domain taxonomy.

5. score = (HARD_passed/10 * 0.7 + SOFT_passed/10 * 0.3) * 10
   if score < 7.0: identify failed gates and rework before output.

OUTPUT: satellite_spec YAML file, gate_results{}, score
```

Verification: all 10 HARD gates pass. Score >= 7.0.

---

## Output Contract

```yaml
---
id: {{satellite_name}}-spec
kind: satellite_spec
pillar: P08
version: 1.0.0
created: {{created_date}}
updated: {{updated_date}}
author: satellite-spec-builder
domain: {{domain}}
model: {{model}}
llm_function: {{llm_function}}
boot_time_seconds: {{boot_time_seconds}}
context_window: {{context_window}}
temperature: {{temperature}}
max_tokens: {{max_tokens}}
dispatch_triggers: [{{trigger_1}}, {{trigger_2}}, {{trigger_3}}]
input_format: {{input_format}}
max_prompt_chars: {{max_prompt_chars}}
max_parallel_instances: {{max_parallel_instances}}
cooldown_seconds: {{cooldown_seconds}}
signal_on_complete: true
signal_on_error: true
log_level: {{log_level}}
tags: [satellite-spec, {{domain}}, {{model_family}}]
quality: null
---

# {{satellite_name}}

## Identity
{{narrative_identity_3_to_5_sentences}}

## Capabilities
{{capability_keywords_as_bullet_list}}

## Does NOT Handle
{{not_handles_as_bullet_list}}

## MCP Servers
{{mcp_bindings_as_yaml_list}}

## Boot Sequence
{{boot_steps_numbered_with_durations}}

## Dispatch Rules
{{dispatch_as_structured_block}}

## Constraints

### Hard Constraints
{{hard_constraints_as_bullet_list}}

### Soft Constraints
{{soft_constraints_as_bullet_list}}

## Scaling
{{scaling_as_yaml_block}}

## Monitoring
{{monitoring_as_yaml_block}}
```

---

## Validation

- [ ] HARD: `id` matches `^[a-z][a-z0-9-]*-spec$`
- [ ] HARD: `kind` equals `satellite_spec`
- [ ] HARD: `model` field is a non-empty string
- [ ] HARD: `boot_sequence` contains >= 4 ordered steps
- [ ] HARD: `dispatch_triggers` contains >= 3 keyword entries
- [ ] HARD: `hard_constraints` list is non-empty
- [ ] HARD: `signal_on_complete` is `true`
- [ ] HARD: `not_handles` section has >= 2 documented exclusions
- [ ] HARD: `mcp_bindings` list has >= 1 entry
- [ ] HARD: `version` matches semantic version format `X.Y.Z`
- [ ] SOFT: `boot_time_seconds` is a non-zero integer estimate
- [ ] SOFT: `temperature` is explicitly set
- [ ] SOFT: `max_tokens` is explicitly set
- [ ] SOFT: `max_parallel_instances` is defined
- [ ] SOFT: `cooldown_seconds` is defined or null with justification
- [ ] SOFT: `capability_keywords` section is present
- [ ] SOFT: required MCP tools have fallback documented
- [ ] SOFT: `log_level` is specified
- [ ] SOFT: `heartbeat_interval_seconds` is configured or explicitly `null`
- [ ] SOFT: `domain` maps to a recognized domain category

**Score threshold**: All 10 HARD gates must pass. Score >= 7.0 for experimental use.
Score >= 8.0 for production use.

---

## Metacognition

**Does**:
- Produce complete architectural specifications for autonomous satellites
- Define operational boundaries (what it handles vs. does not handle)
- Specify all 24+ required frontmatter fields
- Validate against 10 HARD and 10 SOFT quality gates
- Distinguish satellite_spec from agent, boot_config, and pattern artifacts

**Does NOT**:
- Author the satellite's system prompt (agent artifact in P02)
- Create per-provider boot configurations (boot_config artifact)
- Document reusable operation patterns (pattern artifact in P08)
- Execute or deploy the satellite

**Chaining**:
- After: system-prompt-builder uses the role definition to author agent identity
- After: boot_config-builder uses MCP bindings to generate provider configs
- After: pattern-builder uses dispatch rules to document operational patterns
