---
kind: collaboration
id: bld_collaboration_boot_config
pillar: P12
llm_function: COLLABORATE
purpose: How boot-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: boot-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how does this agent initialize on a specific provider runtime?"
I do not define agents. I do not set environment variables.
I configure provider-specific startup so agents boot correctly on any runtime.
## Crew Compositions
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. agent-builder -> "agent definition (persona + capabilities)"
  3. instruction-builder -> "execution steps"
  4. boot-config-builder -> "provider-specific initialization config"
  5. iso-package-builder -> "portable deployable package"
```
### Crew: "Multi-Provider Deployment"
```
  1. agent-builder -> "agent definition"
  2. boot-config-builder -> "config per provider (claude, cursor, codex)"
  3. env-config-builder -> "environment variables per deployment"
  4. fallback-chain-builder -> "model degradation per provider"
```
## Handoff Protocol
### I Receive
- seeds: agent name, target provider (claude, cursor, codex), model preference
- optional: MCP list, CLI flags, token budget, timeout values
### I Produce
- boot_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P02/examples/p02_boot_{agent}_{provider}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- agent-builder: provides agent identity (name, role, capabilities) for config
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| iso-package-builder | Includes boot_config in portable agent package |
| fallback-chain-builder | Needs provider constraints to set degradation timeouts |
