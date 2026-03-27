---
pillar: P12
llm_function: COLLABORATE
purpose: How permission-builder works in crews
---

# Collaboration: permission-builder

## My Role
I define WHO can READ/WRITE/EXECUTE what resources.
I do not prevent DAMAGE (guardrail-builder).
I do not measure QUALITY (quality-gate-builder).

## Crew: "Security Setup for New Agent"
```
  1. guardrail-builder         -> defines safety boundaries
  2. permission-builder        -> defines access controls
  3. quality-gate-builder      -> defines quality thresholds
```

## Crew: "Resource Access Governance"
```
  1. permission-builder        -> defines who can access what
  2. env-config-builder        -> defines environment variables access
  3. path-config-builder       -> defines filesystem path access
```

## Handoff Protocol
### I Receive
- seeds: scope (what resource), roles (who needs access), domain
- optional: existing guardrails, role hierarchy, compliance requirements

### I Produce
- permission artifact in P09_config/examples/
- committed to: cex/P09_config/examples/p09_perm_{scope_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
| Builder | Why |
|---------|-----|
| guardrail-builder | Guardrails define safety scope; permissions complement with access control |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| hook-builder | Implements permission enforcement in code |
| env-config-builder | May need permission checks for sensitive env vars |
