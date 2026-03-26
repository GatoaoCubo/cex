---
id: law-builder-collaboration
kind: collaboration
pillar: P08
parent: law-builder
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [collaboration, law-builder, crew, handoff, P08]
---

# law-builder — COLLABORATION

## My Role

I am a SPECIALIST. I answer ONE question: "what operational rule MUST always be followed?"

I do not recommend solutions (pattern-builder). I do not visualize architecture (diagram-builder).
I do not define components (satellite-spec-builder). I do not restrict for safety (guardrail-builder).
I MANDATE rules so all system participants operate consistently and predictably.

## Crew: Governance Pipeline

```
1. pattern-builder  --> "proven solution (if exists)"
2. law-builder      --> "mandatory law codified from pattern or governance need"
3. quality-gate-builder --> "compliance gate that enforces the law"
```

Use when: a proven pattern warrants elevation to system-wide mandate, with an automated enforcement gate.

## Crew: Architecture Governance

```
1. satellite-spec-builder --> "spec defining satellite capabilities and constraints"
2. law-builder            --> "operational law governing satellite behavior"
3. guardrail-builder [PLANNED] --> "safety boundary complementing the operational law"
```

Use when: formalizing governance for a satellite component — spec defines what it can do, law defines what it must do.

## Crew: Architecture Design

```
1. pattern-builder      --> "reusable solution"
2. law-builder          --> "mandatory rule derived from proven pattern"
3. diagram-builder      --> "visual of law enforcement flow"
4. component-map-builder --> "inventory of components governed by the law"
```

Use when: building a complete governance artifact set for a domain (solution + mandate + visualization + inventory).

## Handoff Protocol

### I Receive

| Input | Required | Notes |
|-------|----------|-------|
| Rule statement | YES | The operational rule to formalize |
| Rationale | YES | Why this rule must be mandatory |
| Domain context | YES | Quality, operations, security, architecture |
| Enforcement idea | OPTIONAL | May develop during composition if absent |
| Known exceptions | OPTIONAL | May be "none" |
| Precedent | OPTIONAL | Existing patterns or learning records |

### I Produce

Single law artifact at: `cex/P08_architecture/examples/p08_law_{number}.md`

Contents: YAML frontmatter (19 fields) + 8 required body sections

### I Signal

On completion: signal `complete` with quality score from QUALITY_GATES.md
If score < 8.0: retry composition before signaling

## Builders I Depend On

| Builder | Why | Blocking? |
|---------|-----|-----------|
| pattern-builder | Proven patterns may be elevated to mandatory laws | NO — optional input |

## Builders That Depend On Me

| Builder | Why I am required |
|---------|------------------|
| quality-gate-builder | Gates enforce law compliance — must know law content to define gate |
| satellite-spec-builder | Specs reference applicable laws governing each satellite |
| diagram-builder | Diagrams may visualize law enforcement flows |
| component-map-builder | Maps reference which laws govern each component |
| system-prompt-builder [PLANNED] | Agents internalize laws as behavioral constraints in system prompts |

## Cross-Reference Requirement

Per BUILDER_NORMS.md: if builder A references builder B, builder B MUST reference builder A.

| I reference | They reference me |
|-------------|------------------|
| quality-gate-builder (enforces my laws) | quality-gate-builder COLLABORATION.md lists law-builder |
| pattern-builder (informs my laws) | pattern-builder COLLABORATION.md lists law-builder |
| satellite-spec-builder (references my laws) | satellite-spec-builder COLLABORATION.md lists law-builder |
| diagram-builder (visualizes my flows) | diagram-builder COLLABORATION.md lists law-builder |

## Boundary Enforcement

If a request arrives that belongs to another builder, redirect:

| Request | Redirect to |
|---------|-------------|
| "Write steps for doing X" | instruction-builder (P03) |
| "Prevent harmful output" | guardrail-builder (P11) |
| "Define abstract truth about systems" | axiom-builder (P10) |
| "Document reusable solution" | pattern-builder (P08) |
| "Visualize the architecture" | diagram-builder (P08) |
| "Define satellite capabilities" | satellite-spec-builder (P08) |
| "Score this artifact" | quality-gate-builder (P11) |
