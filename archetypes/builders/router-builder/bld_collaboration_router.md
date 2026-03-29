---
kind: collaboration
id: bld_collaboration_router
pillar: P02
llm_function: COLLABORATE
purpose: How router-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: router-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should tasks be routed to agents/satellites based on patterns and confidence?"
I produce route tables with confidence thresholds, fallback routes, and escalation policies. I do not handle simple keyword dispatch or multi-step orchestration.
## Crew Compositions
### Crew: "Task Dispatch System"
```
  1. agent-builder            -> "agent identities and capability declarations"
  2. router-builder           -> "route table mapping task patterns to agents with confidence thresholds"
  3. dispatch-rule-builder    -> "simple keyword-to-destination rules for unambiguous cases"
```
### Crew: "Resilient Routing Layer"
```
  1. router-builder           -> "primary route table with confidence scoring"
  2. fallback-chain-builder   -> "ordered fallback sequence when primary route confidence is low"
  3. runtime-rule-builder     -> "timeout and retry rules applied during routing decisions"
```
### Crew: "Multi-Agent Orchestration Pack"
```
  1. agent-card-builder   -> "satellite capability specs that define valid routing targets"
  2. router-builder           -> "routing logic directing tasks to correct satellites"
  3. workflow-builder         -> "multi-step orchestration after routing resolves the first agent"
  4. spawn-config-builder     -> "spawn parameters for the resolved routing target"
```
## Handoff Protocol
### I Receive
- seeds: task domains, available agents/satellites, routing criteria, confidence threshold requirements
- optional: existing dispatch rules to extend, load balancing requirements, escalation policy
### I Produce
- router artifact (YAML frontmatter 14 fields + route table + fallback routes + escalation policy, max 4096 bytes)
- committed to: `cex/P02/examples/p02_router_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides agent capability declarations used as routing targets
- model-card-builder: provides LLM capability profiles that inform routing decisions
- agent-card-builder: provides satellite domain specs that define valid route destinations
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dispatch-rule-builder | Handles simple cases; defers confidence-based routing to me |
| fallback-chain-builder | Chains fallbacks after my route table fails to match with sufficient confidence |
| workflow-builder | Uses my routing output to determine which agent executes each workflow step |
| spawn-config-builder | Configures spawn parameters for the satellite I resolved as the target |
