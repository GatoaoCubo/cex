---
id: cn_{{trigger}}
kind: curation_nudge
pillar: P11
nucleus: "{{nucleus}}"
title: "Curation Nudge: {{trigger}}"
trigger:
  type: "{{trigger_type}}"
  threshold: 10
cadence:
  min_interval_turns: 5
  max_per_session: 3
prompt_template: "Notei {{observation}}. Quero persistir em MEMORY.md?"
target_memory:
  destination: MEMORY.md
  auto_write_if_confirmed: true
version: 1.0.0
quality: null
tags: [hermes_origin, nudge, proactive, memory]
upstream_source: "NousResearch/hermes-agent"
related:
  - bld_examples_memory_summary
  - memory-summary-builder
  - p01_kc_session_backend
  - bld_memory_session_state
  - bld_collaboration_memory_summary
  - p01_kc_session_state
  - p01_kc_memory_summary
  - bld_memory_optimizer
  - p01_kc_memory_scope
  - session-backend-builder
density_score: 1.0
updated: "2026-04-22"
---

## Nudge: {{trigger}}

### Trigger Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Trigger type | {{trigger_type}} | When to fire: turn_count \| density_threshold \| tool_call_count \| user_correction |
| Threshold | {{threshold}} | Count at which nudge fires |
| Min interval | {{min_interval_turns}} turns | Prevents nudge spam in rapid sessions |
| Max per session | {{max_per_session}} | Hard cap on nudge frequency |

### Prompt Template

```
{{prompt_template}}
```

Replace `{{observation}}` at runtime with the observed knowledge to persist.
Example: "Notei que o usuario prefere testes de integracao. Persistir em MEMORY.md?"

### Target Memory

| Field | Value | Description |
|-------|-------|-------------|
| Destination | {{destination}} | Where confirmed knowledge lands |
| Auto-write | {{auto_write_if_confirmed}} | Persist on confirmation without extra steps |

### Boundaries

- NOT `guardrail` (P11): guardrails block actions; nudges ASK
- NOT `quality_gate` (P11): quality_gate is pass/fail; nudge is informational
- NOT `notifier` (P04): notifiers broadcast externally; nudge is in-session self-prompt
- NOT `memory_summary` (P10): summary compresses; nudge triggers persistence decision

### Usage in agent session

```yaml
curation_nudge:
  nudge_ref: cn_{{trigger}}
  fire_every: {{threshold}} {{trigger_type}}
  on_confirm: write_to {{destination}}
  on_reject: increment_counter, check_next_threshold
```

## Trigger Type Reference

| Trigger type | Fires when | Good for | Threshold range |
|-------------|-----------|----------|----------------|
| `turn_count` | N conversation turns elapsed | Long sessions losing context | 10-30 turns |
| `density_threshold` | Knowledge density reaches N observations | Sessions with many learnings | 3-10 observations |
| `tool_call_count` | N tool calls executed | Build-heavy sessions | 15-50 calls |
| `user_correction` | User corrects the agent N times | Preference learning | 2-5 corrections |

## Nudge Lifecycle

```
1. Agent tracks trigger metric during session
2. Metric reaches threshold -> nudge fires
3. Agent presents observation to user
4. User confirms or rejects
   |-- CONFIRM: write to {{destination}}, reset counter
   |-- REJECT: increment counter, wait for next threshold
5. After max_per_session reached -> no more nudges this session
```

## Prompt Template Patterns

Effective nudge prompts follow these patterns:

| Pattern | Template | When to use |
|---------|----------|-------------|
| Observation | "Notei {{observation}}. Persistir?" | Default, most situations |
| Preference | "Voce parece preferir {{preference}}. Gravar?" | After repeated corrections |
| Convention | "Essa convencao apareceu N vezes: {{convention}}. Salvar?" | Repeated patterns |
| Context | "Info relevante para futuras sessoes: {{context}}. Manter?" | Domain knowledge |

## Nudge Trigger Taxonomy (Extended)

Beyond the basic trigger types, these advanced triggers detect more specific knowledge patterns.

| Trigger type | Detection method | What it captures | Typical threshold | False positive rate |
|-------------|-----------------|------------------|-------------------|-------------------|
| `turn_count` | Count conversation turns | General session knowledge | 10-20 turns | Medium |
| `density_threshold` | Track unique entities/facts per turn | Dense information exchanges | 5+ entities in 3 turns | Low |
| `tool_call_count` | Count tool invocations | Procedural knowledge | 5-10 tool calls | Low |
| `user_correction` | Detect user correcting agent | Preferences, corrections | 1 correction | Very low |
| `repeated_pattern` | Detect same question/task asked twice | Undocumented conventions | 2 repetitions | Low |
| `error_recovery` | Detect error-then-fix sequences | Troubleshooting knowledge | 1 recovery cycle | Low |
| `preference_signal` | Detect "I prefer", "always use" | User preferences | 1 signal | Very low |
| `session_end` | Session is about to close | Session summary | End of session | Medium |

## Timing Strategy

Nudge timing determines user experience. Too frequent = annoying. Too rare = knowledge loss.

| Strategy | When to nudge | Pros | Cons | Best for |
|----------|--------------|------|------|----------|
| Immediate | As soon as trigger fires | Captures context while fresh | Interrupts flow | Corrections, errors |
| Batched | After N triggers accumulate | Less disruptive | Context may be stale | Turn count, tool calls |
| End-of-session | Before session closes | Non-disruptive | May miss details | General knowledge |
| Deferred | Next session start | Zero disruption | Context is cold | Low-priority patterns |
| Adaptive | Based on user response history | Learns user tolerance | Complex to implement | Long-term deployments |

### Timing Configuration

```yaml
timing:
  strategy: adaptive
  rules:
    - trigger: user_correction
      timing: immediate
      reason: "corrections are always urgent"
    - trigger: preference_signal
      timing: immediate
      reason: "explicit preferences must be captured"
    - trigger: tool_call_count
      timing: batched
      batch_size: 3
    - trigger: turn_count
      timing: end_of_session
  adaptive:
    initial_interval_turns: 10
    min_interval_turns: 3
    max_interval_turns: 50
    adjust_on_confirm: decrease_by_20pct
    adjust_on_reject: increase_by_50pct
```

## Escalation Levels

When a nudge is rejected, the system must decide whether to try again later or accept it.

| Level | Behavior | When triggered | Max attempts | After max |
|-------|----------|---------------|-------------|-----------|
| L0 Silent | Log observation, no nudge | Below threshold | 0 | Stay at L0 |
| L1 Soft nudge | Single in-line suggestion | Threshold reached | 1 | Drop to L0 |
| L2 Persistent | Re-nudge after N more turns | User rejected L1 but pattern continues | 2 | Escalate to L3 |
| L3 Session summary | Include in end-of-session summary | Pattern persisted across rejections | 1 | Archive |
| L4 Cross-session | Mention at next session start | Pattern spans multiple sessions | 1 | Permanent archive |

### Escalation Flow

```
Observation detected
  |
  v
Below threshold? --YES--> L0 (log silently, increment counter)
  |
  NO
  v
L1: Soft nudge -> "Notei {{observation}}. Persistir em MEMORY.md?"
  |
  User confirms? --YES--> Write to {{destination}}, reset counter
  |
  NO (rejected)
  v
Pattern continues? --NO--> Drop to L0, archive as "user-rejected"
  |
  YES (within same session)
  v
L2: Persistent nudge -> "Pattern appeared {{count}} times. Worth persisting?"
  |
  User confirms? --YES--> Write to {{destination}}, reset counter
  |
  NO (rejected again)
  v
L3: Session summary -> Include in end-of-session knowledge review
  |
  Regardless -> Archive to .cex/runtime/nudges/rejected_patterns.jsonl
```

## Metrics and Observability

| Metric | Description | Target | Source |
|--------|-------------|--------|--------|
| Confirmation rate | Nudges accepted by user | > 60% | Nudge response log |
| False positive rate | Nudges where user says "not useful" | < 15% | User feedback |
| Knowledge retention | Confirmed nudges still in MEMORY.md after 30 days | > 80% | Memory decay audit |
| Nudge-to-action latency | Time between nudge and user response | < 10s | Timing log |
| Session coverage | Sessions with at least 1 nudge | 30-70% | Session log |
| Trigger distribution | Which triggers fire most often | Balanced | Trigger counter |

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `guardrail` | P11 | Guardrails block; nudges ask |
| `quality_gate` | P11 | Quality gates are pass/fail; nudges are informational |
| `memory_summary` | P10 | Summary compresses memory; nudge triggers persistence decision |
| `learning_record` | P11 | Learning records are the output of confirmed nudges |
| `entity_memory` | P10 | Entity memories may be created from confirmed nudges |
| `user_model` | P10 | User model tracks preferences; nudge discovers new ones |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_memory_summary]] | upstream | 0.20 |
| [[memory-summary-builder]] | upstream | 0.18 |
| [[p01_kc_session_backend]] | upstream | 0.17 |
| [[bld_memory_session_state]] | upstream | 0.17 |
| [[bld_collaboration_memory_summary]] | downstream | 0.17 |
| [[p01_kc_session_state]] | upstream | 0.17 |
| [[p01_kc_memory_summary]] | upstream | 0.16 |
| [[bld_memory_optimizer]] | upstream | 0.16 |
| [[p01_kc_memory_scope]] | upstream | 0.16 |
| [[session-backend-builder]] | upstream | 0.15 |
