---
kind: knowledge_card
id: bld_knowledge_card_decision_record
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for decision_record production — Architecture Decision Records
sources: Nygard 2011 (original ADR format), AWS Decision Log, Lightweight ADR (ladr), adr-tools CLI, Michael Keeling "Design It!"
---

# Domain Knowledge: decision_record
## Executive Summary
Architecture Decision Records (ADRs) are short documents capturing significant architectural choices. Originated by Michael Nygard (2011), an ADR records the context forcing a decision, the options evaluated, what was chosen, and the consequences. ADRs are permanent records — even deprecated or superseded ADRs are kept so the reasoning history is preserved. They are NOT laws (inviolable), NOT patterns (reusable prescriptions), and NOT implementation guides.
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
| Format | Source | Structure | When to use |
|--------|--------|-----------|-------------|
| Nygard 2011 | github.com/joelparkerhenderson/architecture-decision-record | Title, Status, Context, Decision, Consequences | Classic, minimal — best default |
| MADR | adr.github.io/madr | Title, Status, Context, Decision Drivers, Options, Decision Outcome | When options need structured comparison |
| AWS Decision Log | AWS team docs | Title, Status, Date, Deciders, Context, Decision, Consequences | Enterprise teams with named deciders |
| Lightweight ADR (ladr) | thoughtworks.com | Title, Status, Context, Decision, Consequences, Compliance | Adds compliance check for regulated domains |
CEX uses Nygard 2011 as base, extended with options list and deciders fields.
## Status Lifecycle
```
proposed --> accepted --> deprecated
                    \--> superseded --> (new ADR accepted)
```
| Status | Meaning | Can transition to |
|--------|---------|------------------|
| proposed | Under consideration, not yet in effect | accepted, deprecated |
| accepted | Decision is in effect and binding | deprecated, superseded |
| deprecated | Was accepted, no longer valid (context changed) | - (terminal) |
| superseded | Replaced by a newer ADR | - (terminal, superseded_by required) |
Rule: superseded ADRs MUST link to their replacement via superseded_by field.
Rule: deprecated ADRs do NOT require a replacement — the decision area was abandoned.
## Patterns
- **Immutable history**: never delete or overwrite an ADR — change status instead. Future engineers need the full decision trail
- **Short and honest**: ADR body should fit one page. If it exceeds 4096 bytes, extract deep design to a separate document and link
- **Options first**: always document at least 2 options considered before stating the decision — this proves alternatives were evaluated
- **Consequences both ways**: list what becomes easier AND what becomes harder. An ADR with only positive consequences is incomplete
- **Link chain**: related ADRs should reference each other via related_to; supersession chain must be traversable forward and back
| Pattern | Example | When to use |
|---------|---------|-------------|
| Minimal ADR | Context + Decision + Consequences only | Well-understood decision with obvious options |
| Options matrix | 3+ options with pros/cons table | Contentious or high-stakes decisions |
| Supersession chain | ADR-001 superseded_by ADR-042 | Technology migrations, paradigm shifts |
- **Numbering**: adr-tools CLI auto-increments. CEX uses slug-based ids (p08_adr_{slug}) for readability over sequence numbers
- **Decision granularity**: one significant choice per ADR. Do not bundle multiple independent decisions in one record
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Missing context | Reader cannot evaluate if decision still applies in their situation |
| No alternatives listed | Signals the decision was made without evaluating options |
| Only positive consequences | Hides technical debt and known tradeoffs from future maintainers |
| Editing accepted ADR to change decision | Destroys audit trail — create a new ADR with supersedes link instead |
| Treating ADR as a law | ADRs document choices teams CAN revisit; laws are inviolable constraints |
| Treating ADR as a pattern | ADRs are single-instance records; patterns are reusable prescriptions |
| Vague decision text | "We decided to use microservices" — too vague. State which services, why, and what boundary |
| No status assigned | An ADR with no status cannot be acted upon or superseded |
## Application
1. Identify: what significant choice was made or is being proposed?
2. Context: what problem, constraint, or force made this decision necessary?
3. Options: list at least 2 alternatives considered with honest pros and cons
4. Decision: state the chosen option in one clear sentence, then explain the primary rationale
5. Consequences: list positive, negative, and neutral effects — include what becomes harder
6. Status: assign proposed (if not yet ratified) or accepted (if already in effect)
7. Links: reference superseded ADRs, related ADRs, and external design documents
## References
- Nygard 2011: "Documenting Architecture Decisions" — cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR: adr.github.io/madr — Markdown Architecture Decision Records
- adr-tools: github.com/npryce/adr-tools — CLI for managing ADR collections
- AWS Decision Log: internal AWS team practice, popularized by "Working Backwards"
- Michael Keeling: "Design It!" — chapter on lightweight decision documentation
