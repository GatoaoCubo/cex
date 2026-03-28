# CEX Crew Runner -- Builder Execution
**Builder**: `context-doc-builder`
**Function**: INJECT
**Intent**: reconstroi signal-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:33:56.814518

## Intent Context
- **Verb**: reconstroi
- **Object**: signal-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_context_doc.md
---
id: context-doc-builder
kind: type_builder
pillar: P01
parent: null
domain: context_doc
llm_function: BECOME
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [kind-builder, context-doc, P01, specialist, content]
---

# context-doc-builder
## Identity
Especialista em construir context_doc — documentos de contexto de dominio para hidratar prompts.
Sabe tudo sobre domain scoping, stakeholder analysis, constraint documentation, assumption
capture, and the boundary between context_doc (P01 injection), knowledge_card (P01 with
density gate), and glossary_entry (P01 single-term definition).
## Capabilities
- Produzir context_doc com frontmatter completo e todos os campos obrigatorios
- Escopo preciso de dominio: delimitar o que esta dentro/fora do contexto
- Mapear stakeholders, constraints, assumptions, e dependencies do dominio
- Validar artifact contra quality gates (7 HARD + 8 SOFT)
- Distinguir quando usar context_doc vs knowledge_card vs glossary_entry
- Produzir par .md + .yaml respeitando max_bytes: 2048
## Routing
keywords: [context, domain, scope, background, hydration, onboarding, planning]
triggers: "create domain context", "background for prompt", "what context does this domain need", "onboarding document", "hydrate prompt with context"
## Crew Role
In a crew, I handle DOMAIN CONTEXT DOCUMENTATION.
I answer: "what background context does this domain need for prompt hydration?"
I do NOT handle: knowledge_card distillation (atomic facts with density gate), glossary_entry
term definitions, instruction step-by-step composition, or embedding configuration.

### bld_instruction_context_doc.md
---
kind: instruction
id: bld_instruction_context_doc
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for context_doc
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a context_doc
## Phase 1: RESEARCH
1. Identify the domain to document (snake_case label, e.g., `ecommerce_imports`, `api_auth_jwt`)
2. Define scope boundaries: write one sentence — "This context covers [X] within [Y] for [Z] audience"
3. List what is explicitly out of scope (minimum 1-3 items)
4. Catalog stakeholders and their needs: who consumes this document and for what purpose (agent, human, or both)
5. Identify constraints: technical, business, or regulatory rules that cannot change
6. List assumptions: what is taken as given without requiring proof
7. Identify dependencies on other domains, services, or artifacts
8. Check existing context_docs for overlapping scope to avoid duplication
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields, id as `p01_cd_{{topic_slug}}` (quality: null — never self-score)
4. Write Domain Scope section: restate scope sentence, list included and excluded topics explicitly
5. Write Stakeholders section: who uses this context and why, one entry per stakeholder type
6. Write Constraints section: technical, business, and regulatory constraints that bound the domain
7. Write Assumptions section: working assumptions taken as given, one per line
8. Write Dependencies section: other domains, services, and artifacts this document references
9. Write Key Concepts section: 3-5 essential ideas required to understand this domain
10. Verify body <= 2048 bytes; if over limit, trim Key Concepts first, then Dependencies
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p01_cd_`
4. Confirm kind == context_doc
5. Confirm scope boundary is defined (Domain Scope section present and at least 3 lines)
6. Confirm at least 1 stakeholder is listed
7. Confirm constraints are listed (not empty)
8. Confirm body <= 2048 bytes
9. HARD gates: frontmatter valid, id pattern matches, scope defined, stakeholder present, constraints listed
10. SOFT gates: score against QUALITY_GATES.md
11. Cross-check: domain context for hydration (not an atomic fact = knowledge_card)? Not a single-term definition (glossary_entry)? Not step-by-step procedural guidance (instruction)?
12. Revise if score < 8.0 before outputting

### bld_knowledge_card_context_doc.md
---
kind: knowledge_card
id: bld_knowledge_card_context_doc
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for context_doc production — domain background for prompt hydration
sources: consulting discovery docs, technical context memos, onboarding packets
---

# Domain Knowledge: context_doc
## Executive Summary
Context docs are domain background documents injected into agent context before task execution. They provide situational awareness — stakeholders, constraints, assumptions, dependencies — without the density requirements of knowledge cards or the step-by-step structure of instructions. Context docs answer "what is the background?" before the agent answers "what do I do?"
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| llm_function | INJECT (loaded into context) |
| Max size | 2048 bytes |
| Density gate | None (narrative allowed) |
| Quality gates | 7 HARD + 8 SOFT |
| Output format | .md + optional .yaml pair |
| Key fields | domain, scope, stakeholders, constraints |
## Patterns
- **Scope-first writing**: define boundaries before content — what domain, what time horizon, what is excluded
- **Stakeholder focus**: tailor precision to who consumes this context and what decisions they make
- **Constraint documentation**: list what CANNOT change — constraints bound the problem space more than features
- **Time-bounded context**: include timeline and dates — context ages; stale context causes wrong decisions
- **Consumption chain**: context_docs feed into system_prompts and action_prompts as background injection
| Analog | Source | Shared pattern |
|--------|--------|----------------|
| README context | Software repos | Background before instructions |
| Project brief | Consulting | Scope, constraints, stakeholders |
| SITREP | Operations | Current state + key constraints |
| Onboarding packet | Teams | Domain background for newcomers |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No scope boundary | Document grows unbounded; includes irrelevant context |
| Duplicating knowledge cards | Context doc has no density gate; use KC for atomic facts |
| Including step-by-step instructions | That is an instruction artifact, not context |
| Missing constraints section | Agent has background but no boundaries; overreaches |
| Stale dates | Outdated context causes wrong assumptions |
| Over 2048 bytes | Exceeds token budget for injection; split or compress |
## Application
1. Define scope: one sentence — what domain, what time horizon, what is excluded
2. Identify stakeholders: who consumes this context and for what decisions
3. Document constraints: what CANNOT change in this domain
4. List assumptions: what is taken as true without verification
5. Map dependencies: what other artifacts consume this context
6. Validate: <= 2048 bytes, scope is one sentence, constraints are concrete
## References
- Consulting discovery documents: scope and constraint patterns
- Technical writing: context memos and background sections
- Agile: Definition of Done context documentation
- Prompt engineering: context injection for LLM task performance

### bld_quality_gate_context_doc.md
---
id: p11_qg_context_doc
kind: quality_gate
pillar: P11
title: "Gate: context_doc"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "domain context documentation — background documents that hydrate prompts with scope, stakeholders, constraints, and assumptions"
quality: null
tags: [quality-gate, context-doc, P01, prompt-hydration, domain-scope, constraints]
tldr: "Pass/fail gate for context_doc artifacts: domain scope precision, constraint completeness, assumption capture, and hydration readiness."
density_score: 0.91
---

# Gate: context_doc
## Definition
| Field | Value |
|---|---|
| metric | context_doc artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: context_doc` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | ID contains uppercase, spaces, or invalid chars |
| H03 | ID equals filename stem | `id: my_ctx` but file is `other_ctx.md` |
| H04 | Kind equals literal `context_doc` | `kind: knowledge_card` or `kind: glossary_entry` or any other value |
| H05 | Quality field is null | `quality: 7.0` or any non-null value |
| H06 | All required fields present | Missing `domain`, `scope`, or `constraints` |
| H07 | Body size <= 2048 bytes | Body exceeds 2048 bytes — trim or split into knowledge_card |
| H08 | Scope section states what is OUT of scope | Scope only lists what is included; exclusions absent |
| H09 | At least one constraint documented | `constraints: []` or constraints section empty |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Scope precision | 1.0 | Domain boundary is specific enough to exclude adjacent domains unambiguously |
| Out-of-scope completeness | 1.0 | Adjacent domains that could be confused are explicitly excluded |
| Constraint actionability | 1.0 | Each constraint is a specific rule a prompt can apply, not a vague guideline |
| Assumption explicitness | 1.0 | Assumptions are stated as assumptions (not facts), with source noted |
| Stakeholder relevance | 0.5 | Stakeholders listed are those whose concerns affect prompt behavior |
| Dependency mapping | 0.5 | External dependencies that constrain the domain are identified |
| Hydration readiness | 1.0 | Document structured so key facts can be injected into a prompt without editing |
| Freshness | 0.5 | `updated` date is recent; stale context docs noted as requiring review |
| Terminology consistency | 0.5 | Key terms used consistently throughout; ambiguous terms defined inline |
| Density appropriateness | 1.0 | Content is dense but readable; no padding or repeated constraints |
| Boundary from knowledge_card | 1.0 | Document is context or background, not a distilled atomic fact (that belongs in knowledge_card) |
| Domain specificity | 1.0 | Content specific to the declared domain; no generic boilerplate |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Context doc for an emerging domain where constraints are still being discovered; used only in internal experiments |
| approver | Domain owner acknowledgment that constraints are provisional |
| audit_trail | Bypass reason and list of known-incomplete constraint areas in frontmatter comment |
| expiry | 7d — context docs for active domains must reach >= 7.0 within one week of first use |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics) |

### bld_schema_context_doc.md
---
kind: schema
id: bld_schema_context_doc
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for context_doc
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: context_doc
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_ctx_{topic}) | YES | - | Namespace compliance |
| kind | literal "context_doc" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| domain | string (snake_case) | YES | - | Machine-readable domain label |
| scope | string (one sentence) | YES | - | Scope boundary statement |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "context-doc" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string], len >= 3 | REC | - | Domain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |
## ID Pattern
Regex: `^p01_ctx_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
Examples: `p01_ctx_br_import_regs`, `p01_ctx_api_auth_jwt`, `p01_ctx_marketplace_fees`
## Body Structure (required sections)
1. `## Scope` — in-scope and out-of-scope boundary, minimum 3 lines
2. `## Background` — domain history, current state, key facts
3. `## Stakeholders` — who consumes this context, what decisions it informs
4. `## Constraints & Assumptions` — hard constraints + working assumptions
5. `## Dependencies` — referenced artifacts, systems, external sources
6. `## References` — source links, related artifacts (optional but recommended)
## Constraints
- max_bytes: 2048 (body only, all sections combined)
- naming: p01_ctx_{topic}.md + p01_ctx_{topic}.yaml
- machine_format: yaml
- id == filename stem (enforced by H03)
- quality: null always (enforced by H05)
- llm_function: INJECT (context_doc is injected into prompts)
- layer: content (P01 knowledge layer)
## Boundary Rules
- context_doc is NOT knowledge_card: no single-atomic-fact constraint, no mandatory density gate
- context_doc is NOT glossary_entry: does not define a single term
- context_doc is NOT instruction: no step-by-step execution protocol
- context_doc DOES allow narrative prose (unlike knowledge_card)
- context_doc DOES allow multiple facts (unlike glossary_entry)

### bld_examples_context_doc.md
---
kind: examples
id: bld_examples_context_doc
pillar: P07
llm_function: GOVERN
purpose: Golden example and anti-example for context_doc production
---

# Examples: context_doc
## Golden Example
```markdown
id: p01_ctx_br_ecommerce_import_regs
kind: context_doc
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
domain: ecommerce_imports
scope: "Brazilian import regulations for marketplace sellers, 2025-2026 enforcement cycle"
quality: null
tags: [context-doc, ecommerce_imports, brazil, regulation]
tldr: "BR marketplace imports: ICMS 17-20%, NCM code required, Receita Federal DI threshold R$50"
keywords: [icms, ncm, receita_federal, import, brazil, marketplace, tax]
density_score: 0.87
## Scope
In scope: ICMS rates by state, NCM classification requirements, Receita Federal DI thresholds,
marketplace seller obligations under Lei 14.781/2024.
Out of scope: international shipping logistics, payment processing, consumer returns law.
## Background
Brazil levies ICMS (17-20% by state) on all imported goods sold via marketplace.
NCM codes (8-digit Nomenclatura Comum do Mercosul) are mandatory on all listings.
Receita Federal requires Declaracao de Importacao (DI) for shipments > R$50 commercial value.
Lei 14.781/2024 expanded marketplace platform liability for seller tax compliance.
## Stakeholders
- Marketplace seller agents: need tax rates and NCM requirements before listing
- Compliance agents: enforce DI threshold checks pre-shipment
- Pricing agents: require ICMS rates to compute landed cost
## Constraints & Assumptions
- ICMS rates are state-specific; this context uses SP rate (18%) as default
- NCM codes assumed valid per MDIC 2025 table (update required if MDIC revises)
- DI threshold R$50 is current as of 2026-01-01; subject to Receita Federal portaria changes
## Dependencies
- `p01_kc_ncm_classification_rules` — atomic NCM lookup facts
- `p01_kc_icms_state_rates_2025` — per-state rate table
- Receita Federal Portaria RFB 1.073/2025 (external)
## References
- Lei 14.781/2024: planalto.gov.br/lei-14781
- MDIC NCM table: mdic.gov.br/nomenclatura
```
### Why Golden (gate mapping)
| Gate | Status | Reason |
|------|--------|--------|
| H01 | PASS | YAML parses without error |
| H02 | PASS | id matches `^p01_ctx_[a-z][a-z0-9_]+$` |
| H03 | PASS | id == filename stem |
| H04 | PASS | kind == "context_doc" |
| H05 | PASS | quality == null |
| H06 | PASS | id, kind, domain, scope all present |
| H07 | PASS | body <= 2048 bytes |
| S01 | PASS | tldr <= 160ch, non-empty |
| S02 | PASS | tags len 4, includes "context-doc" |
| S03 | PASS | Scope section present, 4 lines |
| S04 | PASS | Background section non-empty, 4 dense facts |
| S05 | PASS | No filler phrases detected |
| S06 | PASS | density_score 0.87 >= 0.80 |
| S07 | PASS | Constraints section present |
| S08 | PASS | Dependencies listed with artifact ids |
## Anti-Example
```markdown
id: ctx_brazil_imports
kind: context_doc
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
domain: imports
quality: 8.5
tags: [context-doc]
tldr: "This document provides a comprehensive overview of the various regulatory frameworks
that apply to the importation of goods into Brazil through various channels including
ecommerce marketplaces and direct consumer imports."
## Overview
This document is about Brazilian imports. It covers many things related to importing
goods. Basically, there are taxes involved and you need to follow some rules.
In summary, compliance is important.
```
### Failures (gate mapping)
| Gate | Status | Failure |
|------|--------|---------|
| H02 | FAIL | id `ctx_brazil_imports` missing `p01_` prefix |
| H05 | FAIL | quality: 8.5 — self-scored, must be null |
| H06 | FAIL | scope field absent from frontmatter |
| S01 | FAIL | tldr > 160 chars (224 chars) |
| S02 | FAIL | tags len 1 (< 3 required) |
| S03 | FAIL | No `## Scope` section present |
| S05 | FAIL | Filler: "this document", "basically", "in summary" |
| S06 | FAIL | density_score absent |

### bld_config_context_doc.md
---
kind: config
id: bld_config_context_doc
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration constraints for context_doc production
---

# Config: context_doc
## Naming Rules
| Rule | Pattern | Example |
|------|---------|---------|
| Markdown file | `p01_ctx_{topic_slug}.md` | `p01_ctx_br_import_regs.md` |
| YAML companion | `p01_ctx_{topic_slug}.yaml` | `p01_ctx_br_import_regs.yaml` |
| id field | `p01_ctx_{topic_slug}` | `p01_ctx_br_import_regs` |
| topic_slug | `[a-z][a-z0-9_]+` (snake_case, no hyphens) | `br_import_regs` |
**Critical**: id MUST equal filename stem. Brain search depends on this invariant.
## File Paths
| Artifact | Canonical Path |
|----------|---------------|
| Produced context_docs | `cex/P01_knowledge/examples/` |
| Schema reference | `cex/P01_knowledge/_schema.yaml` |
| Seed bank | `cex/P01_knowledge/SEED_BANK.yaml` |
| Builder files | `cex/archetypes/builders/context-doc-builder/` |
## Size Constraints
| Constraint | Value | Scope |
|------------|-------|-------|
| max_bytes | 2048 | Body only (all sections after frontmatter) |
| tldr max | 160 chars | frontmatter.tldr field |
| tags min | 3 items | frontmatter.tags list |
| keywords min | 3 items | frontmatter.keywords list |
| scope min | 1 sentence | frontmatter.scope field |
| density_score min | 0.80 | if provided (recommended) |
## Trim Priority (if body exceeds 2048 bytes)
1. Trim `## References` section first (least dense)
2. Trim `## Background` narrative prose (keep facts, remove transitions)
3. Trim `## Stakeholders` to bullet list only
4. Never trim `## Scope` or `## Constraints & Assumptions`
## Invariants (never override)
- `quality: null` — never self-assign score
- `kind: context_doc` — literal, no variation
- `pillar: P01` — pillar assignment fixed
- id == filename stem — enforced by gate H03

### bld_output_template_context_doc.md
---
kind: output_template
id: bld_output_template_context_doc
pillar: P05
llm_function: PRODUCE
purpose: Structural template for context_doc artifacts — derives from SCHEMA.md
---

# Output Template: context_doc
## Frontmatter (copy and fill all fields)
```yaml
id: p01_ctx_{{topic_slug}}
kind: context_doc
pillar: P01
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
domain: "{{domain_value}}"
scope: "{{scope_description_one_sentence}}"
quality: null
tags: [context-doc, {{domain_tag}}, {{scope_tag}}]
tldr: "{{dense_summary_max_160ch}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
density_score: {{0.80_to_1.00}}
```
## Field Fill Guide
| Field | Format | Example |
|-------|--------|---------|
| id | `p01_ctx_` + snake_case topic | `p01_ctx_br_import_regs` |
| domain | snake_case domain label | `ecommerce_imports` |
| scope | one sentence, specific | `Brazilian import regs 2025-2026 for marketplace sellers` |
| tldr | <= 160 chars, dense | `BR import rules: ICMS 17%, NCM codes required, Receita Federal enforcement 2025` |
| keywords | 3-7 relevant terms | `[icms, ncm, receita_federal, import, brazil]` |
| density_score | float 0.80-1.00 | `0.85` |
## Body Structure
```markdown
## Scope
[Restate scope boundary. List what is in scope and what is explicitly out of scope.
Minimum 3 lines. No filler.]
## Background
[Domain background: history, current state, key facts. No filler prose.
Dense, informative. This is the context agents will INJECT before acting.]
## Stakeholders
[Who uses this context? Agents, roles, teams. What decisions does this inform?]
## Constraints & Assumptions
[Hard constraints: what cannot change.
Working assumptions: what is taken as given.
Format as bullet list.]
## Dependencies
[Other artifacts, systems, APIs, or knowledge this context references.
Format: artifact_id or URL + one-line description.]
## References
[Source links, related context_docs, version history notes.]
```
## Notes
- Body (all sections combined) MUST be <= 2048 bytes
- id MUST equal filename stem (e.g., id: p01_ctx_foo -> file: p01_ctx_foo.md)
- Produce companion .yaml with same frontmatter fields

### bld_architecture_context_doc.md
---
kind: architecture
id: bld_architecture_context_doc
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of context_doc — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| domain_scope | Explicit boundary — what the context covers and excludes | context_doc | required |
| background_narrative | Prose explanation of the domain — history, purpose, key facts | context_doc | required |
| stakeholder_map | Who is involved, their roles, and their concerns | context_doc | required |
| constraint_list | Hard limits, compliance requirements, non-negotiables | context_doc | required |
| assumption_list | Working assumptions the domain context depends on | context_doc | required |
| dependency_list | External systems, teams, or artifacts this domain relies on | context_doc | optional |
| system_prompt | Agent persona file that loads context_doc at boot | P03 | consumer |
| action_prompt | Task-level prompt that injects context_doc per invocation | P03 | consumer |
| knowledge_card | Sibling artifact — single atomic fact with density gate | P01 | sibling |
| glossary_entry | Sibling artifact — single controlled-vocabulary term definition | P01 | sibling |
## Dependency Graph
```
domain_scope        --produces-->  background_narrative
domain_scope        --produces-->  constraint_list
background_narrative --produces--> stakeholder_map
assumption_list     --depends-->   domain_scope
dependency_list     --depends-->   domain_scope
context_doc         --produces-->  system_prompt
context_doc         --produces-->  action_prompt
knowledge_card      --depends-->   context_doc
glossary_entry      --depends-->   context_doc
```
| From | To | Type | Data |
|------|----|------|------|
| domain_scope | background_narrative | produces | bounded domain as subject of narrative |
| domain_scope | constraint_list | produces | boundary that shapes what is constrained |
| background_narrative | stakeholder_map | produces | domain narrative that identifies actors |
| assumption_list | domain_scope | depends | assumptions derived from scope analysis |
| dependency_list | domain_scope | depends | external dependencies identified from scope |
| context_doc | system_prompt | produces | domain background injected into agent persona |
| context_doc | action_prompt | produces | situational context injected per task |
| knowledge_card | context_doc | depends | atomic facts scoped to same domain |
| glossary_entry | context_doc | depends | term definitions scoped to same domain |
## Boundary Table
| context_doc IS | context_doc IS NOT |
|---------------|-------------------|
| Multi-fact domain background for prompt hydration | A single atomic fact at high density (that is knowledge_card) |
| Narrative prose allowed — background, history, framing | A single controlled-vocabulary term definition (that is glossary_entry) |
| Loaded at agent boot or injected per task | A step-by-step execution protocol (that is instruction) |
| Covers stakeholders, constraints, assumptions, dependencies | An agent persona with operational rules (that is system_prompt) |
| Max 2048 bytes — concise enough for context injection | A full specification document or design artifact |
| P01 content layer — pure knowledge, no execution logic | A runtime tool or executable component |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| scoping | domain_scope | Define what the context covers and excludes |
| knowledge | background_narrative, stakeholder_map | Capture domain facts, history, and actors |
| constraints | constraint_list, assumption_list, dependency_list | Document limits, working assumptions, and external dependencies |
| injection | system_prompt, action_prompt | Downstream consumers that load context into prompts |
| siblings | knowledge_card, glossary_entry | Related P01 artifacts covering atomic facts and terms |

### bld_collaboration_context_doc.md
---
kind: collaboration
id: bld_collaboration_context_doc
pillar: P12
llm_function: COLLABORATE
purpose: How context-doc-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: context-doc-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what background context does this domain need for prompt hydration?"
I do not distill atomic facts. I do not define terms.
I document domain context so prompt builders can hydrate their prompts with relevant background.
## Crew Compositions
### Crew: "Content Foundation"
```
  1. context-doc-builder -> "domain context (scope, stakeholders, constraints)"
  2. knowledge-card-builder -> "atomic facts from the domain"
  3. glossary-entry-builder -> "term definitions for the domain"
  4. few-shot-example-builder -> "format examples grounded in context"
```
### Crew: "Prompt Hydration"
```
  1. context-doc-builder -> "domain background for injection"
  2. action-prompt-builder -> "task prompt hydrated with context"
  3. chain-builder -> "prompt pipeline with contextual grounding"
```
## Handoff Protocol
### I Receive
- seeds: domain name, scope description, target audience
- optional: stakeholder list, constraints, assumptions, dependencies
### I Produce
- context_doc artifact (.md + .yaml, max 2048 bytes)
- committed to: `cex/P01/examples/p01_context_{domain}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Context docs are authored from domain analysis.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| action-prompt-builder | Injects context_doc into task prompts |
| knowledge-card-builder | Uses context scope to bound fact distillation |
| chain-builder | Hydrates chain steps with domain background |
| instruction-builder | Grounds execution recipes in domain context |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `context-doc-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
