---
kind: collaboration
id: bld_collaboration_code_executor
pillar: P12
llm_function: COLLABORATE
purpose: How code-executor-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: code-executor-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what languages can run here, how is it isolated, and what are the limits?"
I do not build CLI commands. I do not define protocol servers.
I specify sandboxed execution environments so agents can safely run LLM-generated code.
## Crew Compositions
### Crew: "Code Execution Pipeline"
```
  1. function-def-builder -> "function interface (what to call)"
  2. code-executor-builder -> "execution environment (where it runs)"
  3. retriever-builder -> "data access (what data is available)"
```
### Crew: "Agent Runtime"
```
  1. code-executor-builder -> "sandboxed code execution"
  2. cli-tool-builder -> "terminal command execution"
  3. daemon-builder -> "persistent background processes"
```
## Handoff Protocol
### I Receive
- seeds: execution use case, language requirements, isolation needs
- optional: resource limits, network policy, session model
### I Produce
- code_executor artifact (.md + .yaml compiled)
- committed to: `cex/P04_tools/examples/p04_exec_{runtime}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Code executors are self-contained environment specs.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents reference code executors for running generated code |
| function-def-builder | Functions may specify code_executor as their runtime |
| mcp-server-builder | MCP servers may use code executors for dynamic operations |
