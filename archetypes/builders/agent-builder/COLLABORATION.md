---
pillar: P12
llm_function: COLLABORATE
purpose: How agent-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: agent-builder

## My Role in Crews
I am a PACKAGER. I answer ONE question: "who is this agent, what can it do, and how is it structured?"
I integrate outputs from identity builders (system-prompt-builder) and knowledge builders
(knowledge-card-builder) into a complete, deployable agent definition with iso_vectorstore.

## Crew Compositions

### Crew: "Agent Bootstrap" (standard)
```
  1. knowledge-card-builder -> "domain knowledge for the agent"
  2. system-prompt-builder  -> "agent identity, rules, output format"
  3. agent-builder          -> "complete agent definition + iso_vectorstore"
  4. skill-builder [PLANNED] -> "executable capabilities for the agent"
```

### Crew: "Full Agent Package"
```
  1. model-card-builder     -> "LLM spec and routing decision"
  2. system-prompt-builder  -> "persona and rules"
  3. agent-builder          -> "full definition with iso_vectorstore"
  4. quality-gate-builder   -> "validation criteria for agent output"
  5. skill-builder [PLANNED] -> "reusable skills the agent exposes"
```

### Crew: "Agent Audit"
```
  1. agent-builder (read mode) -> "parse existing agent definition"
  2. quality-gate-builder      -> "score against HARD + SOFT gates"
  3. knowledge-card-builder    -> "distill audit findings as knowledge"
```

## Handoff Protocol

### I Receive
- seeds: agent name, satellite, domain
- optional: system_prompt artifact (from system-prompt-builder)
- optional: knowledge_cards (from knowledge-card-builder)
- optional: model_card (from model-card-builder)

### I Produce
- agent artifact: `cex/P02_model/examples/p02_agent_{slug}.md`
- iso_vectorstore skeleton: `agents/{slug}/iso_vectorstore/` (10 file stubs)

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On

| Builder | Why | Wave |
|---------|-----|------|
| system-prompt-builder | Provides system_prompt artifact to embed in SYSTEM_INSTRUCTION ISO file | Wave 3 (upstream) |
| knowledge-card-builder | Provides domain knowledge to inject into agent Overview and Architecture | Wave 1 (upstream) |
| model-card-builder | Provides LLM spec for tools_count and capabilities scoping | Wave 2 (upstream) |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| skill-builder [PLANNED] | Needs agent identity to scope skill capabilities correctly |
| quality-gate-builder | Validates agent artifacts I produce |
| spawn-config-builder | References agent identity for spawn configuration |

## Cross-Reference Norm (BUILDER_NORMS Rule 12)
system-prompt-builder COLLABORATION.md lists agent-builder as a downstream dependent.
This file lists system-prompt-builder as an upstream dependency.
The cross-reference is bidirectional — both files acknowledge the relationship.
