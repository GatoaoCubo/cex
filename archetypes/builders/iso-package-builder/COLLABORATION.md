---
pillar: P12
llm_function: COLLABORATE
purpose: How iso-package-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: iso-package-builder

## My Role in Crews
I am a PACKAGER. I answer ONE question: "how do I bundle this agent into a portable, tier-validated ISO package?"
I do not define agents. I do not write system prompts. I do not validate quality gates.
I PACKAGE so deployment tools and sharing workflows can consume a self-contained bundle.

## Crew Compositions

### Crew: "Agent Distribution" (standard)
```
  1. agent-builder          -> "canonical agent definition with iso_vectorstore"
  2. iso-package-builder    -> "portable ISO bundle at declared tier"
  3. quality-gate-builder   -> "validation criteria for the package"
```

### Crew: "Full Agent Pipeline"
```
  1. knowledge-card-builder -> "domain knowledge for the agent"
  2. system-prompt-builder [PLANNED] -> "agent identity and rules"
  3. agent-builder          -> "complete agent definition"
  4. iso-package-builder    -> "portable ISO bundle"
  5. quality-gate-builder   -> "package quality validation"
```

### Crew: "Package Audit"
```
  1. iso-package-builder (read mode) -> "parse existing package manifest"
  2. quality-gate-builder             -> "score against HARD + SOFT gates"
  3. knowledge-card-builder           -> "distill audit findings as knowledge"
```

## Handoff Protocol

### I Receive
- seeds: agent name, domain, target tier
- optional: agent artifact (from agent-builder)
- optional: system_prompt artifact (becomes system_instruction.md)
- optional: existing iso_vectorstore to repackage

### I Produce
- iso_package: `cex/agents/{agent_slug}/manifest.yaml` + tiered file set
- committed to: `cex/agents/{agent_slug}/`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On

| Builder | Why | Wave |
|---------|-----|------|
| agent-builder | Provides canonical agent definition as packaging source | Upstream |
| knowledge-card-builder | Provides domain knowledge for quick_start.md content | Upstream |
| system-prompt-builder [PLANNED] | Provides system_prompt to embed as system_instruction.md | Upstream |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| quality-gate-builder | Validates iso_package artifacts I produce |
| spawn-config-builder [PLANNED] | References packaged agent for spawn configuration |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
agent-builder COLLABORATION.md lists iso-package-builder as a downstream consumer.
This file lists agent-builder as an upstream dependency.
The cross-reference is bidirectional.
