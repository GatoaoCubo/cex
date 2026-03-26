---
pillar: P12
llm_function: COLLABORATE
purpose: How boot-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: boot-config-builder

## My Role in Crews
I am an INITIALIZER. I answer ONE question: "how does this agent boot on this specific provider?"
I do not define agents. I do not select models. I do not orchestrate spawns.
I CONFIGURE so agents can initialize correctly on their target provider runtime.

## Crew Compositions

### Crew: "Agent Deployment" (standard)
```
  1. model-card-builder     -> "LLM spec for model selection"
  2. agent-builder          -> "canonical agent definition"
  3. boot-config-builder    -> "provider-specific initialization"
  4. spawn-config-builder [PLANNED] -> "orchestration parameters"
```

### Crew: "Multi-Provider Setup"
```
  1. agent-builder          -> "one canonical agent definition"
  2. boot-config-builder    -> "boot config for provider A"
  3. boot-config-builder    -> "boot config for provider B"
  4. quality-gate-builder   -> "validation for both configs"
```

### Crew: "Full Agent Pipeline"
```
  1. knowledge-card-builder -> "domain knowledge"
  2. system-prompt-builder [PLANNED] -> "agent persona and rules"
  3. agent-builder          -> "complete agent definition"
  4. boot-config-builder    -> "initialization per provider"
  5. iso-package-builder    -> "portable bundle"
```

## Handoff Protocol

### I Receive
- seeds: provider name, agent identity, target domain
- optional: model_card (from model-card-builder) for constraints reference
- optional: agent artifact (from agent-builder) for identity block

### I Produce
- boot_config artifact: `cex/P02_model/examples/p02_boot_{provider_slug}.md`
- committed to: `cex/P02_model/examples/`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On

| Builder | Why | Wave |
|---------|-----|------|
| agent-builder | Provides agent identity for identity block | Upstream |
| model-card-builder | Provides LLM spec for constraints reference | Upstream |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| spawn-config-builder [PLANNED] | Uses boot_config for spawn parameters |
| iso-package-builder | May include boot_config reference in package |
| quality-gate-builder | Validates boot_config artifacts |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
agent-builder COLLABORATION.md lists boot-config-builder in Architecture dependency graph.
This file lists agent-builder as an upstream dependency.
The cross-reference is bidirectional.
