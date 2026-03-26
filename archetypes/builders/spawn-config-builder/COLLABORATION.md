---
pillar: P12
llm_function: COLLABORATE
purpose: How spawn-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: spawn-config-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should this satellite be spawned, with what flags and settings?"
I do not write task instructions. I do not emit signals. I do not orchestrate workflows.
I CONFIGURE SPAWNS so orchestrators can launch satellites with correct parameters.

## Crew Compositions

### Crew: "Satellite Dispatch"
```
  1. dispatch_rule-builder [PLANNED] -> "routing logic: keyword -> satellite"
  2. handoff-builder [PLANNED] -> "task instructions for satellite"
  3. spawn-config-builder -> "spawn parameters: mode, flags, timeout"
  4. signal-builder -> "completion signal definition"
```

### Crew: "Grid Mission"
```
  1. workflow-builder -> "multi-satellite orchestration plan"
  2. spawn-config-builder -> "spawn config per satellite in grid"
  3. signal-builder -> "per-satellite completion signals"
```

## Handoff Protocol

### I Receive
- seeds: satellite name, mode, task domain
- optional: specific flags, timeout override, MCP requirements

### I Produce
- spawn_config artifact (YAML)
- committed to: `cex/P12_orchestration/examples/p12_spawn_{mode_slug}.yaml`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- None (spawn_config is infrastructure-level, no builder dependencies)

## Builders That Depend On Me [PLANNED]

| Builder | Why |
|---------|-----|
| workflow-builder | References spawn_config for satellite execution parameters |
| handoff-builder [PLANNED] | Needs spawn mode to size prompt strategy |
