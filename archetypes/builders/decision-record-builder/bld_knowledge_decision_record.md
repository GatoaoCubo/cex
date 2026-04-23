---
kind: knowledge_card
id: bld_knowledge_card_decision_record
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for decision_record production — Architecture Decision Records
sources: Nygard 2011 (original ADR format), AWS Decision Log, Lightweight ADR (ladr), adr-tools CLI, Michael Keeling "Design It!"
quality: 9.2
title: "Knowledge Card Decision Record"
version: "1.0.0"
author: n03_builder
tags: [decision_record, builder, examples]
tldr: "Golden and anti-examples for decision record construction, demonstrating ideal structure and common pitfalls."
domain: "decision record construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - decision-record-builder
  - p10_lr_decision_record_builder
  - p03_sp_decision_record_builder
  - p01_kc_decision_record
  - bld_architecture_decision_record
  - bld_collaboration_decision_record
  - bld_instruction_decision_record
  - bld_schema_decision_record
  - bld_tools_decision_record
  - bld_config_decision_record
---

# Domain Knowledge: decision_record
## Executive Summary
Architecture Decision Records (ADRs) are short documents capturing significant architectural choices. Originated by Michael Nygard (2011), an ADR records the context forcing a decision, the options evaluated, what was chosen, and the consequences. ADRs are permanent — even deprecated or superseded records are kept so reasoning history is preserved. They are NOT laws, NOT patterns, and NOT implementation guides.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (Architecture) |
| llm_function | REASON (deliberative) |
| Status values | proposed, accepted, deprecated, superseded |
| Required fields | id, title, status, context, decision |
| Recommended fields | consequences, options |
| Max body | 4096 bytes |
| Naming | p08_adr_{slug}.md |
| ID pattern | `^p08_adr_[a-z][a-z0-9_]+$` |

## ADR Format Variants
| Format | Structure | When to use |
|--------|-----------|-------------|
| Nygard 2011 | Title, Status, Context, Decision, Consequences | Classic minimal — best default |
| MADR | + Decision Drivers, Options, Decision Outcome | Structured options comparison |
| AWS Decision Log | + Date, Deciders | Enterprise with named deciders |
| Lightweight ADR | + Compliance | Regulated domains |

CEX uses Nygard 2011 extended with options list and deciders fields.

## Status Lifecycle
```
proposed --> accepted --> deprecated
                    \--> superseded --> (new ADR accepted)
```
- superseded ADRs MUST link to replacement via superseded_by
- deprecated ADRs do NOT require a replacement (decision area abandoned)

## Patterns
- **Immutable history**: never delete — change status instead
- **Short and honest**: fit one page; if > 4096 bytes, extract to linked document
- **Options first**: document >= 2 alternatives before stating decision
- **Consequences both ways**: list what becomes easier AND harder
- **Link chain**: related ADRs reference each other; supersession chain traversable forward and back
- **One decision per ADR**: do not bundle independent decisions

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Missing context | Reader cannot evaluate if decision still applies |
| No alternatives listed | Signals decision made without evaluating options |
| Only positive consequences | Hides technical debt from future maintainers |
| Editing accepted ADR | Destroys audit trail — create superseding ADR instead |
| Treating ADR as a law | ADRs are revisable; laws are inviolable |
| Vague decision text | "Use microservices" — state which, why, and what boundary |
| No status assigned | ADR cannot be acted upon or superseded |

## Application
1. Identify the significant choice made or being proposed
2. Context: what problem or force made this decision necessary?
3. Options: list >= 2 alternatives with honest pros and cons
4. Decision: state chosen option in one sentence, then primary rationale
5. Consequences: positive, negative, neutral — include what becomes harder
6. Status: proposed (not yet ratified) or accepted (already in effect)
7. Links: reference superseded ADRs, related ADRs, external design docs

## References
- Nygard 2011: cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR: adr.github.io/madr
- adr-tools: github.com/npryce/adr-tools
- Michael Keeling: "Design It!" — lightweight decision documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[decision-record-builder]] | downstream | 0.64 |
| [[p10_lr_decision_record_builder]] | downstream | 0.62 |
| [[p03_sp_decision_record_builder]] | downstream | 0.60 |
| [[p01_kc_decision_record]] | sibling | 0.58 |
| [[bld_architecture_decision_record]] | downstream | 0.56 |
| [[bld_collaboration_decision_record]] | downstream | 0.55 |
| [[bld_instruction_decision_record]] | downstream | 0.54 |
| [[bld_schema_decision_record]] | downstream | 0.51 |
| [[bld_tools_decision_record]] | downstream | 0.47 |
| [[bld_config_decision_record]] | downstream | 0.47 |
