---
pillar: P12
llm_function: COLLABORATE
purpose: How skill-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: skill-builder

## My Role in Crews
I am a CAPABILITY SPECIALIST. I answer ONE question: "what phases does this capability
execute, and when is it triggered?"
I do not define agent identity. I do not write task prompts.
I DEFINE REUSABLE CAPABILITIES so agents can invoke structured workflows consistently.

## Crew Compositions

### Crew: "Full Agent Package"
```
  1. model-card-builder      -> "LLM specs and routing decision"
  2. system-prompt-builder   -> "persona and rules"
  3. skill-builder           -> "reusable capabilities the agent invokes"
  4. quality-gate-builder    -> "validation criteria for agent output"
```

### Crew: "Workflow Bootstrap"
```
  1. knowledge-card-builder  -> "domain knowledge for the workflow"
  2. skill-builder           -> "reusable phases for each workflow step"
  3. workflow-builder        -> "orchestrates skills in sequence or parallel"
  4. signal-builder          -> "completion signals emitted after validate phase"
```

### Crew: "Tool Layer Build"
```
  1. input-schema-builder    -> "contract for skill inputs"
  2. skill-builder           -> "phase-structured capability"
  3. mcp-server-builder      -> "MCP tools the skill calls during execute phase"
  4. validator-builder       -> "quality rules for skill output"
```

## Handoff Protocol

### I Receive
- seeds: capability name, domain, invocation pattern
- optional: input_schema (P06), knowledge_cards (P01), sub-skill IDs

### I Produce
- skill artifact (YAML frontmatter + markdown body)
- committed to: `cex/P04_tools/examples/p04_skill_{name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 7.0: signal retry with failure reasons

## Builders I Depend On
- knowledge-card-builder: provides domain knowledge injected at discover phase
- input-schema-builder: provides input contracts referenced in configure phase
- mcp-server-builder: MCP tools called during execute phase

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| system-prompt-builder | References available skills in agent constraints section |
| workflow-builder | Orchestrates skill execution in workflow steps |
| agent-builder [PLANNED] | Packages skills into full agent capability set |
| spawn-config-builder | Spawn configs may trigger skills at initialization |
