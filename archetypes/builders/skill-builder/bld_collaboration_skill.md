---
kind: collaboration
id: bld_collaboration_skill
pillar: P04
llm_function: COLLABORATE
purpose: How skill-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: skill-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what phases does this capability execute, and when is it triggered?"
I produce reusable, phase-structured capabilities with a defined trigger (slash command, keyword, event, or agent-invoked). I do NOT define agent identity (system-prompt-builder), one-shot task prompts (action-prompt-builder), MCP servers (mcp-server-builder), or event-driven hooks (hook-builder).

## Crew Compositions

### Crew: "Reusable Capability Packaging"
```
  1. action-prompt-builder -> "authors the task-level prompt that a single skill phase will invoke"
  2. skill-builder         -> "assembles phases into a lifecycle (discover/configure/execute/validate) with a trigger"
  3. iso-package-builder   -> "packages the skill with its examples and schema into a distributable ISO bundle"
```

### Crew: "Agent Capability Expansion"
```
  1. system-prompt-builder -> "defines the agent's identity and which skills it can invoke"
  2. skill-builder         -> "builds each reusable capability the agent needs as structured phases"
  3. hook-builder          -> "wires event-driven behaviors that complement the skill's trigger mechanism"
```

### Crew: "Slash Command Feature Launch"
```
  1. skill-builder         -> "defines the slash command trigger, phases, and input/output per phase"
  2. input-schema-builder  -> "produces the JSON schema for the skill's required and optional inputs"
  3. smoke-eval-builder    -> "writes a quick sanity check that verifies the skill's critical path works"
```

## Handoff Protocol

### I Receive
- seeds: capability name, trigger type (slash/keyword/event/agent), phases description, user or agent invocable
- optional: input schema draft, example invocations, phase timeout constraints

### I Produce
- skill artifact (Markdown with YAML frontmatter, 12 required fields + phases, max 300 lines)
- committed to: `cex/P04/examples/skill-{name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- action-prompt-builder: individual phase instructions often reference or embed action prompts

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| system-prompt-builder | lists available skills in agent identity so the agent knows what to invoke |
| iso-package-builder   | packages the skill artifact for distribution alongside examples and schema |
| hook-builder          | may call a skill programmatically from an event-driven hook |
| smoke-eval-builder    | needs the skill's critical path phases to write targeted health checks |
| dag-builder           | places skill invocations as nodes in multi-step execution graphs |
