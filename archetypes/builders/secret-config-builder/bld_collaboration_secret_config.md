---
kind: collaboration
id: bld_collaboration_secret_config
pillar: P12
llm_function: COLLABORATE
purpose: How secret-config-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: secret-config-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what provider stores these secrets, how do they rotate, and how do agents retrieve them?"
I do not define who is allowed to access secrets — that is permission-builder.
I do not define generic environment variables — that is env-config-builder.
I specify credential management contracts so agents can safely retrieve sensitive values at runtime.
## Crew Compositions
### Crew: "Agent Runtime Security"
```
  1. secret-config-builder  -> "credential management spec (provider, rotation, access)"
  2. permission-builder      -> "who can access which secrets (RBAC, policies)"
  3. env-config-builder      -> "non-sensitive environment variables (URLs, feature names)"
```
### Crew: "Secure Agent Deployment"
```
  1. secret-config-builder  -> "secrets spec (Vault/K8s/AWS paths, rotation policy)"
  2. boot-config-builder     -> "startup parameters referencing secret paths"
  3. guardrail-builder       -> "execution constraints on secret operations"
```
### Crew: "LLM Provider Governance"
```
  1. secret-config-builder  -> "API key management spec (Portkey vault or Vault)"
  2. rate-limit-config-builder -> "token and request throttling"
  3. model-card-builder      -> "model capabilities and usage policy"
```
## Handoff Protocol
### I Receive
- seeds: credential type, consuming agent/service, runtime platform
- optional: provider preference, rotation frequency, compliance requirements
### I Produce
- secret_config artifact (.md + .yaml frontmatter)
- committed to: `cex/P09_config/examples/p09_sec_{slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures
- if plaintext secret detected: signal BLOCKED — do not commit
## Builders I Depend On
None — independent builder (layer 0). Secret configs can be defined standalone.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| boot-config-builder | Boot configs reference secret paths for startup credential injection |
| agent-builder | Agents declare which secret_config governs their credential retrieval |
| guardrail-builder | Guardrails may constrain which secret paths an agent can access |
| instruction-builder | Agent instructions reference secret retrieval steps from access_pattern |
## Boundary Enforcement
When a request arrives that is NOT secret_config, redirect explicitly:
- "I need env vars for the API URL" -> env-config-builder (non-sensitive, no rotation)
- "I need to control who can read these secrets" -> permission-builder (access control)
- "I need to turn this feature on/off" -> feature-flag-builder (toggle, not credential)
- "I need to throttle API calls" -> rate-limit-config-builder (not a credential)
