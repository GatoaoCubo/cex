---
kind: collaboration
id: bld_collaboration_spawn_config
pillar: P12
llm_function: COLLABORATE
purpose: How spawn-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: spawn-config-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this satellite be spawned, with what flags and settings?"
I configure CLI flags, MCP profiles, timeout policies, prompt sizing, and handoff file references for automated satellite launch. I do NOT design what happens after spawn (workflow-builder), emit runtime signals (signal-builder), or write the task instructions the satellite receives.

## Crew Compositions

### Crew: "Multi-Satellite Mission Setup"
```
  1. workflow-builder -> "defines which satellites run, in what order, with what dependencies"
  2. spawn-config-builder -> "produces spawn_config for each satellite referenced in the workflow"
  3. signal-builder -> "defines completion/error signals emitted at the end of each satellite run"
```

### Crew: "New Satellite Onboarding"
```
  1. system-prompt-builder -> "defines the satellite identity, rules, and response format"
  2. spawn-config-builder -> "produces the spawn_config: mode, flags, MCP profile, timeout"
  3. validation-schema-builder -> "enforces the spawn_config output contract post-generation"
```

## Handoff Protocol

### I Receive
- seeds: satellite name, spawn mode (solo/grid/continuous), task domain description
- optional: timeout override, interactive flag, handoff file path, MCP requirements, model preference

### I Produce
- spawn_config artifact (YAML, frontmatter 19 fields, max 120 lines)
- committed to: `cex/P12_orchestration/examples/p12_spawn_{mode_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- None. spawn-config is infrastructure-level and requires no upstream builder artifacts.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| workflow-builder | references spawn_config per satellite step to know how to launch each agent |
| validation-schema-builder | may enforce spawn_config field contracts post-generation |
