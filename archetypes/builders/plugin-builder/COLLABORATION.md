---
pillar: P12
llm_function: COLLABORATE
purpose: How plugin-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: plugin-builder

## My Role in Crews
I am an EXTENDER. I answer ONE question: "how should this capability be added as a pluggable module?"
I do not intercept events. I do not define multi-phase workflows.
I EXTEND so the system gains new capabilities without modifying core code.

## Crew Compositions

### Crew: "Extension System" (standard)
```
  1. interface-builder [PLANNED]   -> "define the contract plugins must implement"
  2. plugin-builder                -> "build the pluggable extension"
  3. quality-gate-builder          -> "validate plugin meets contract"
  4. golden-test-builder           -> "create test cases for plugin"
```

### Crew: "Observability Stack"
```
  1. hook-builder                  -> "intercept events for metric collection"
  2. plugin-builder                -> "export collected metrics to monitoring"
  3. signal-builder                -> "emit signals on metric thresholds"
```

### Crew: "Tool Extension"
```
  1. plugin-builder                -> "build pluggable tool capability"
  2. mcp-server-builder            -> "expose plugin API via MCP protocol"
  3. skill-builder                 -> "wrap plugin in multi-phase workflow"
```

## Handoff Protocol

### I Receive
- seeds: interface contract, domain, required capabilities
- optional: config requirements (what should be configurable)
- optional: dependency list (other plugins/systems needed)

### I Produce
- plugin artifact: `cex/P04_tools/examples/p04_plug_{slug}.md`
- committed to: archetypes or pool depending on quality score

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
- interface-builder [PLANNED]: provides the contract that plugin implements

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| mcp-server-builder | May wrap plugin API surface as MCP tools |
| skill-builder | May compose plugin capabilities into multi-phase workflows |
| hook-builder | Plugin may register hooks during on_load lifecycle |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
hook-builder may reference plugin as hook registrar (plugins register hooks at on_load).
mcp-server-builder may wrap plugin API as MCP tools.
skill-builder may compose plugin capabilities into workflow phases.
