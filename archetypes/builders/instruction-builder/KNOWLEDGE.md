---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for instruction production
sources: runbook engineering, SRE playbooks, IEC 62443, CEX operational patterns
---

# Domain Knowledge: instruction

## Foundational Concept
Instructions are operational recipes — step-by-step procedures that transform a
defined starting state into a defined ending state. The concept draws from SRE
runbooks, manufacturing SOPs, and military operations orders. Key principle:
each step must be atomic (one action), verifiable (can confirm completion),
and reversible (can undo if needed).

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| SRE Runbooks (Google) | Step-by-step incident response | Direct: numbered steps + validation |
| Ansible Playbooks | Declarative task sequences | Informs: idempotent + atomic fields |
| GitHub Actions workflows | Sequential job steps | Informs: prerequisites + dependencies |
| IEC 62443 procedures | Industrial control system SOPs | Informs: rollback + safety |
| Kubernetes operators | Reconciliation loops | Informs: idempotent re-execution |

## Key Patterns
- One action per step: compound steps cause ambiguous failures
- Verifiable prerequisites: "Python 3.10+ installed" not "environment ready"
- Idempotent when possible: re-running should produce same result
- Explicit rollback: if atomic: false, every step needs an undo
- Validation at end: checklist of verifiable outcomes
- Dependencies upfront: tools, files, services, permissions listed before steps
- No persona: instructions say WHAT to do, not WHO you are

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| steps_count | Integrity check: count matches body | Ansible task count |
| idempotent | Safe re-execution flag | Ansible idempotency |
| atomic | All-or-nothing execution flag | Database transaction |
| validation_method | How to verify completion | SRE verification step |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT instruction |
|------|------------|--------------------------|
| action_prompt | Conversational task prompt with I/O | Has input/output spec, no prerequisites |
| system_prompt | Agent identity and rules | Defines WHO, not HOW |
| workflow | Multi-agent orchestration (P12) | Coordinates agents, not single-agent steps |
| skill | Reusable capability with trigger (P04) | Has lifecycle phases, not just steps |
| handoff | Dispatch instruction to satellite (P12) | Coordination artifact, not execution recipe |

## References
- Google SRE Book: Chapter 14 — Managing Incidents
- Ansible docs: Playbook best practices
- IEC 62443: Industrial automation security procedures
