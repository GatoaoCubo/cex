---
# TEMPLATE: Axiom — Privacy Controls (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.axiom)
# Max 3072 bytes

id: p10_ax_{{RULE_SLUG}}
type: axiom
lp: P10
title: "Axiom: Edge-Layer Privacy Controls"
quality: {{QUALITY_8_TO_10}}
---

# Axiom: Edge-Layer Privacy Controls

## Rule
Privacy enforcement happens at the edge (hook layer), not at the center (daemon/DB). Content tagged as private never reaches the persistence layer.

## Tag Types

| Tag | Controlled By | Stripped At | Purpose |
|-----|--------------|------------|---------|
| `<private>` | User | Hook layer (before HTTP send) | User-controlled exclusion from memory |
| `<context>` | System | Worker layer (before re-storage) | Injected context — prevent re-storage loops |

## Privacy Flow
```
User message → Hook strips <private> → HTTP to daemon → Worker strips <context> → DB write
```

## Worker Skip Signal
When the daemon determines an observation should not be stored (duplicate, low-value, or flagged), it returns a `skipped: true` response. The hook aborts the observation pipeline without error.

## Exit Codes

| Code | Meaning | Effect |
|------|---------|--------|
| 0 | Success / graceful skip | Continue |
| 1 | Non-blocking (tag parse warning) | Log, continue |
| 2 | Blocking (privacy violation detected) | Halt, do NOT persist |

## Rationale
- Why: Privacy must be enforced before data leaves the client boundary
- Protects: User trust — tagged content never reaches storage or external services

## Examples
- Correct: Hook detects `<private>API_KEY=abc123</private>`, strips it, sends sanitized text to daemon
- Incorrect: Hook sends full text to daemon, daemon filters `<private>` tags (data already transmitted)
