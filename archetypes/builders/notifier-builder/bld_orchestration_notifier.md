---
kind: collaboration
id: bld_collaboration_notifier
pillar: P04
llm_function: COLLABORATE
purpose: Crew roles, dependencies, and collaboration patterns for notifier-builder
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [collaboration, notifier, P04, crew, dependencies]
quality: 9.1
tldr: "notifier-builder is PUSH DELIVERY SPECIALIST. Depends on: webhook-builder (events trigger notifications). Used by: instruction-builder, agent-builder, code-gen."
density_score: 1.0
domain: "collaboration artifact construction"
title: "Collaboration Notifier"
related:
  - bld_collaboration_webhook
  - p03_sp_notifier_builder
  - notifier-builder
  - bld_architecture_notifier
  - bld_architecture_kind
  - bld_collaboration_builder
  - p01_kc_notifier
  - kind-builder
  - bld_memory_notifier
  - bld_instruction_notifier
---
# Collaboration: notifier-builder

## Crew Role
**PUSH NOTIFICATION DELIVERY SPECIALIST**
I define how systems deliver outbound notifications to users or other systems.
I answer: "Which channel? Which provider? What template? What priority? What rate limit?"

## Dependency Map
```
webhook-builder ──triggers──> notifier-builder
                              (events fire notifications)

template-builder ──provides──> notifier-builder
                               (message template patterns)

notifier-builder ──consumed by──> instruction-builder
                                  (how-to docs reference notifiers)
                 ──consumed by──> agent-builder
                                  (agents call notifiers)
                 ──consumed by──> code-gen
                                  (generates delivery implementation)
```

## Crew Compositions

### Alert Pipeline Crew
```
webhook-builder   -> defines inbound event endpoint
notifier-builder  -> defines outbound notification on event
dag-builder       -> wires webhook trigger to notifier delivery
```
Use case: CI/CD deploy events -> Slack alerts

### Communication System Crew
```
notifier-builder  -> push delivery channel definitions
api-client-builder -> external API integrations
template-builder   -> shared message template library
```
Use case: User onboarding communication suite

### User Engagement Crew
```
notifier-builder  -> push channels (email, push, in-app)
agent-builder     -> orchestrates engagement logic
chain-builder     -> sequences notification flows
```
Use case: Re-engagement campaign with multi-channel fallback

## Handoff Protocol
**Receiving from webhook-builder**:
- Input: event type, payload schema, trigger condition
- My output: notifier artifact with matching template_vars

**Handing off to code-gen**:
- Provide: id, channel, provider, template, template_vars, rate_limit, retry_policy
- Code-gen produces: provider SDK implementation using notifier spec as contract

**Handing off to instruction-builder**:
- Provide: finalized notifier artifact path
- instruction-builder references it in how-to documentation

## Boundary Enforced in Crew
- If task involves receiving HTTP: delegate to webhook-builder
- If task involves full API auth flow: delegate to api-client-builder
- If task involves background polling: delegate to daemon-builder
- If task involves protocol server: delegate to mcp-server-builder

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `collaboration`
- **Artifact ID**: `bld_collaboration_notifier`
- **Tags**: [collaboration, notifier, P04, crew, dependencies]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `collaboration` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_webhook]] | sibling | 0.45 |
| [[p03_sp_notifier_builder]] | related | 0.39 |
| [[notifier-builder]] | related | 0.39 |
| [[bld_architecture_notifier]] | related | 0.38 |
| [[bld_architecture_kind]] | downstream | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.36 |
| [[p01_kc_notifier]] | upstream | 0.35 |
| [[kind-builder]] | downstream | 0.33 |
| [[bld_memory_notifier]] | related | 0.33 |
| [[bld_instruction_notifier]] | upstream | 0.31 |
