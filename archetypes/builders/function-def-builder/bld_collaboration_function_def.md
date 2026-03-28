---
kind: collaboration
id: bld_collaboration_function_def
pillar: P12
llm_function: COLLABORATE
purpose: How function-def-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: function-def-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what parameters does this function accept, and what does it return?"
I do not build protocol servers. I do not implement API clients.
I specify callable function schemas so LLMs can invoke external capabilities.
## Crew Compositions
### Crew: "LLM Tool Ecosystem"
```
  1. function-def-builder -> "function schema (parameters, returns)"
  2. mcp-server-builder -> "protocol server exposing functions"
  3. code-executor-builder -> "sandboxed runtime for function execution"
```
### Crew: "Agent Toolkit"
```
  1. function-def-builder -> "callable function definitions"
  2. search-tool-builder -> "search function specialization"
  3. retriever-builder -> "vector search function specialization"
```
## Handoff Protocol
### I Receive
- seeds: function purpose, parameter names, expected types, return shape
- optional: provider targets, strict mode, error conditions
### I Produce
- function_def artifact (.md + .json compiled)
- committed to: `cex/P04_tools/examples/p04_fn_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Function definitions are self-contained schemas.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| mcp-server-builder | MCP servers expose function definitions as tools |
| agent-builder | Agents reference function definitions in their tool lists |
| instruction-builder | Recipes reference functions as available actions |
