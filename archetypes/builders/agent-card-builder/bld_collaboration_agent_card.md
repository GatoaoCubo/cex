---
kind: collaboration
id: bld_collaboration_agent_card
pillar: P08
llm_function: COLLABORATE
purpose: How agent-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: agent-card-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is this agent_node's role, model, tools, and constraints?"
I define the full architecture of an autonomous agent_node — its domain, LLM model, MCPs, boot sequence, dispatch rules, and scaling. I do NOT define individual agents inside the agent_node (agent-builder), boot configuration per provider (boot-config-builder), or reusable patterns (pattern-builder).
## Crew Compositions
### Crew: "New Satellite Onboarding"
```
  1. mental-model-builder   -> "defines the agent_node's domain map, personality, and cognitive constraints"
  2. agent-card-builder -> "produces the full agent_card: role, model, MCPs, boot sequence, dispatch rules"
  3. boot-config-builder    -> "generates provider-specific boot configuration from the agent_node spec"
```
### Crew: "Satellite Architecture Documentation"
```
  1. agent-card-builder -> "produces agent_card with all 24+ frontmatter fields"
  2. system-prompt-builder  -> "authors the agent_node's system prompt using the spec's role and constraints"
  3. diagram-builder        -> "renders the agent_node's architecture and dependency graph visually"
```
### Crew: "Multi-Satellite Orchestration Design"
```
  1. agent-card-builder -> "specs each agent_node's role, model, and MCPs independently"
  2. dispatch-rule-builder  -> "defines routing rules between agent_nodes based on their specs"
  3. dag-builder            -> "assembles the execution graph connecting agent_nodes into a workflow"
```
## Handoff Protocol
### I Receive
- seeds: agent_node name, domain description, intended role, available MCPs, model preference
- optional: scaling requirements, existing agent list, known constraints, monitoring needs
### I Produce
- agent_card artifact (YAML frontmatter + Markdown body, 24+ fields, max 300 lines)
- committed to: `cex/P08/examples/agent-card-{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- mental-model-builder: provides the domain map and cognitive constraints that shape the spec
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| boot-config-builder | needs the agent_node spec to generate provider-specific boot configs |
| system-prompt-builder | uses role and constraints from the spec to author the agent_node prompt |
| dispatch-rule-builder | uses agent_node boundaries from the spec to define routing rules |
| dag-builder | uses agent_node capabilities to place them correctly in execution graphs |
