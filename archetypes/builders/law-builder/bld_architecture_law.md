---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of law — inventory, dependencies, and architectural position
---

# Architecture: law in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 19-field metadata header (id, kind, pillar, domain, scope, severity, etc.) | law-builder | active |
| statement | The inviolable rule expressed as a single declarative sentence | author | active |
| rationale | Why this law exists — the incident, risk, or principle behind it | author | active |
| enforcement_mechanism | How the system detects and prevents violations at runtime | author | active |
| exceptions | Narrow, documented cases where the law may be bypassed with audit | author | active |
| violations | Catalog of known violation scenarios with severity and response | author | active |
| history | Changelog of amendments, additions, and scope changes over time | author | active |
| conflict_resolution | Priority rules when this law conflicts with other laws or instructions | author | active |

## Dependency Graph

```
knowledge_card  --produces-->  law  --consumed_by-->  agent
pattern         --produces-->  law  --enforced_by-->  validator
instruction     --depends-->   law
guardrail       --depends-->   law  --signals-->      violation_event
```

| From | To | Type | Data |
|------|----|------|------|
| knowledge_card (P01) | law | data_flow | domain context supporting rationale |
| pattern (P08) | law | data_flow | recurring failure pattern formalized as mandate |
| law | agent (P02) | dependency | agent must obey law constraints during execution |
| law | validator (P06) | produces | enforcement rules consumed by pre-commit checks |
| law | instruction (P03) | dependency | instructions must not contradict active laws |
| law | guardrail (P11) | dependency | guardrails implement safety subset of laws |
| law | violation_event (P12) | signals | emitted when enforcement detects a breach |

## Boundary Table

| law IS | law IS NOT |
|--------|------------|
| An inviolable operational mandate with enforcement | A flexible guideline (instruction P03) |
| Scoped to a specific domain with clear boundaries | An abstract philosophical truth (axiom P10) |
| Backed by rationale from incidents or principles | A safety restriction without operational mandate (guardrail P11) |
| Enforced automatically or via audit trail | A reusable solution recommendation (pattern P08) |
| Amended through formal history with versioning | A visual representation of architecture (diagram P08) |
| Prioritized via conflict-resolution ordering | A runtime configuration parameter (runtime_rule P09) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Context | knowledge_card, pattern | Supply domain facts and recurring failures that justify the law |
| Definition | frontmatter, statement, rationale | Specify what the law mandates and why |
| Enforcement | enforcement_mechanism, violations, conflict_resolution | Define how violations are detected, reported, and prioritized |
| Governance | exceptions, history | Document approved bypasses and amendment trail |
| Downstream | agent, validator, guardrail | Consumers that must comply with or implement the law |
