# CEX Crew Runner -- Builder Execution
**Builder**: `knowledge-card-builder`
**Function**: INJECT
**Intent**: reconstroi director-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:20.964812

## Intent Context
- **Verb**: reconstroi
- **Object**: director-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_knowledge_card.md
---
id: knowledge-card-builder
kind: type_builder
pillar: P02
parent: null
domain: knowledge_card
llm_function: BECOME
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: EDISON
tags: [kind-builder, knowledge-card, P01, specialist]
---

# knowledge-card-builder
## Identity
Especialista em construir knowledge_cards — fatos atomicos pesquisaveis.
Sabe tudo sobre densidade informacional, destilacao de conhecimento,
frontmatter semantico, e validacao via validate_kc.py v2.0.
Produz cards com dados concretos, alta densidade (>0.8), max 5KB.
## Capabilities
- Pesquisar e destilar conhecimento de qualquer dominio em fato atomico
- Produzir knowledge_card com frontmatter completo (19 campos)
- Validar card contra validate_kc.py v2.0 (10 HARD + 20 SOFT gates)
- Classificar KC como domain_kc ou meta_kc e aplicar body structure correto
## Routing
keywords: [knowledge-card, kc, fato, destilacao, densidade, conhecimento]
triggers: "documenta conhecimento X", "cria KC sobre Y", "destila fato Z"
## Crew Role
In a crew, I handle KNOWLEDGE DISTILLATION.
I answer: "what is the essential, searchable fact about this topic?"
I do NOT handle: model_card, boot_config, agent, benchmark, router.

### bld_instruction_knowledge_card.md
---
kind: instruction
id: bld_instruction_knowledge_card
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for knowledge_card
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a knowledge_card
## Phase 1: RESEARCH
1. Identify the topic: what single atomic fact or pattern needs capturing?
2. Gather sources: official documentation, URLs, code references, or established expert knowledge
3. Extract key facts — concrete data points (numbers, dates, names, measurements), not opinions or vague claims
4. Determine the KC type:
   - domain_kc: external knowledge about a tool, API, protocol, or domain
   - meta_kc: internal pattern or lesson learned from operating this system
5. Check existing knowledge_cards via brain_query [IF MCP] for the same topic — avoid duplicates
6. Assess information density: can you reach >= 0.80 density (tables, code, concrete bullets over filler prose)?
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all frontmatter fields and body constraints
2. Read OUTPUT_TEMPLATE.md — fill the template following SCHEMA constraints exactly
3. Fill frontmatter: 14 required fields + 5 CEX extended fields (null is acceptable for recommended fields)
4. Set quality: null — never self-score
5. Write the body following the structure for the KC type:
   - domain_kc: Quick Reference, Key Concepts, Strategy Phases, Golden Rules, Flow, Comparativo, References
   - meta_kc: Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References
6. Prefer high-density formats: tables and code blocks over paragraphs
7. Keep every bullet at or below 80 characters
8. Include at least one external URL in the References section
9. Write axioms in frontmatter as ALWAYS / NEVER / IF-THEN rules — at least one required
10. Keep body between 200 and 5120 bytes
## Phase 3: VALIDATE
1. Run `python _tools/validate_kc.py <file>` if available — this is an active automated tool
2. HARD gates (all must pass):
   - YAML frontmatter parses without errors
   - id matches pattern `p01_kc_[a-z][a-z0-9_]+`
   - kind == knowledge_card
   - quality == null
   - density >= 0.80
   - at least 3 concrete facts present (numbers, dates, named entities)
   - body is between 200 and 5120 bytes
   - no internal paths in body (records/, .claude/, /home/)
   - no filler sentences ("this document covers", "as mentioned above")
3. SOFT gates (score each against QUALITY_GATES.md):
   - tldr contains concrete data, not generic description
   - axioms are in ALWAYS / NEVER / IF-THEN form
   - at least 4 sections with at least 3 non-empty lines each
   - keywords and long_tails present for search
4. Cross-check scope boundaries:
   - atomic searchable fact, not a broad domain overview (context_doc)?
   - not a term definition (glossary_entry)?
   - not an embedding configuration file?
   - are the facts concrete (numbers, dates, names) rather than vague claims?
5. If a HARD gate fails: fix immediately and re-run the validator
6. If score < 8.0: expand thin sections, replace prose with tables or code blocks, remove filler

### bld_architecture_knowledge_card.md
---
kind: architecture
id: bld_architecture_knowledge_card
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of knowledge_card — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| title | Short searchable label identifying the fact | author | required |
| body | Distilled atomic fact content, high information density >= 0.8 | author | required |
| domain_tags | Topic labels enabling retrieval routing | author | required |
| card_type | Classification: domain_kc or meta_kc | author | required |
| sources | Origin references for the distilled fact | author | required |
| confidence_score | Reliability rating of the fact (0.0–1.0) | author | required |
| version | Revision counter for fact updates | author | required |
| linked_artifacts | Other cards or artifacts this fact connects to | author | optional |
| expiry_hint | Signal that the fact may become stale after a date | author | optional |
## Dependency Graph
```
rag_source     --produces--> knowledge_card
knowledge_card --queried_by--> brain_index
brain_index    --injects_into--> system_prompt
knowledge_card --informs--> few_shot_example
knowledge_card --referenced_by--> context_doc
knowledge_card --referenced_by--> agent
```
| From | To | Type | Data |
|------|----|------|------|
| rag_source | knowledge_card | data_flow | raw source text to distill |
| knowledge_card | brain_index | data_flow | title, body, tags for BM25 and vector indexing |
| brain_index | system_prompt | data_flow | retrieved facts injected into prompt context |
| knowledge_card | few_shot_example | data_flow | factual grounding for input/output pairs |
| knowledge_card | context_doc | data_flow | referenced as supporting evidence |
| knowledge_card | agent | data_flow | linked domain knowledge in agent definition |
## Boundary Table
| knowledge_card IS | knowledge_card IS NOT |
|-------------------|----------------------|
| Atomic searchable fact with density >= 0.8 | Broad reference document without density gate |
| Versioned and source-attributed | Spec for an LLM model or its parameters |
| Classified as domain_kc or meta_kc | Short definition entry (3 lines max) |
| Injected into prompts via retrieval index | External URL pointer without distilled content |
| Max 5KB body (high signal-to-noise) | Input/output demonstration pair |
| Expirable when facts can become stale | Agent identity or behavioral definition |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | title, card_type, version | Name, classify, and version the fact |
| Content | body, confidence_score, expiry_hint | Carry the distilled fact with reliability signal |
| Discoverability | domain_tags, linked_artifacts | Enable retrieval routing and cross-referencing |
| Provenance | sources | Trace the fact back to its origin |
| Consumption | brain_index, system_prompt | Retrieve and inject facts into agent context at runtime |

### bld_collaboration_knowledge_card.md
---
kind: collaboration
id: bld_collaboration_knowledge_card
pillar: P12
llm_function: COLLABORATE
purpose: How knowledge-card-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: knowledge-card-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the essential, searchable fact about this topic?"
I do not define agent personas. I do not configure boot parameters.
I distill knowledge into atomic facts so agents and builders have factual context for decisions.
## Crew Compositions
### Crew: "Content Foundation"
```
  1. context-doc-builder -> "domain scope and background"
  2. knowledge-card-builder -> "atomic searchable facts (density > 0.8)"
  3. glossary-entry-builder -> "term definitions"
  4. few-shot-example-builder -> "format examples grounded in knowledge"
```
### Crew: "New Agent End-to-End"
```
  1. knowledge-card-builder -> "domain knowledge for agent expertise"
  2. agent-builder -> "agent definition shaped by knowledge"
  3. instruction-builder -> "execution steps grounded in facts"
  4. boot-config-builder -> "provider configuration"
  5. iso-package-builder -> "deployable package"
```
### Crew: "RAG Pipeline Setup"
```
  1. knowledge-card-builder -> "content to embed and index"
  2. embedding-config-builder -> "embedding model parameters"
  3. brain-index-builder -> "search index configuration"
```
## Handoff Protocol
### I Receive
- seeds: topic name, domain, source material or research brief
- optional: density target, classification (domain_kc or meta_kc), related cards
### I Produce
- knowledge_card artifact (.md + .yaml frontmatter, max 5KB, density > 0.8)
- committed to: `cex/P01/examples/p01_kc_{topic}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Knowledge cards are distilled from source material.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agent expertise is grounded in knowledge cards |
| axiom-builder | Axioms are formalized from distilled facts |
| context-doc-builder | Domain docs reference knowledge card facts |
| brain-index-builder | Knowledge cards are primary content for indexing |
| instruction-builder | Recipes reference factual knowledge for accuracy |

### bld_config_knowledge_card.md
---
kind: config
id: bld_config_knowledge_card
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: knowledge_card Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p01_kc_{topic_slug}.md` | `p01_kc_prompt_caching.md` |
| Builder directory | kebab-case | `knowledge-card-builder/` |
| Frontmatter fields | snake_case | `density_score`, `when_to_use` |
| Topic slug | lowercase, underscores | `rag_fundamentals`, `prompt_caching` |
Rule: id MUST equal filename stem (validator H02 checks this).
## File Paths
- Output: `cex/P01_knowledge/examples/p01_kc_{topic}.md`
- Compiled: `cex/P01_knowledge/compiled/p01_kc_{topic}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: 200-5120 bytes (validator H08)
- Total (frontmatter + body): max ~6500 bytes
- Density: >= 0.80
- Bullet max: 80 chars (validator S10)
- Title: 5-100 chars (validator S03)
- tldr: <= 160 chars, no self-references (S01, S02)
## Body Requirements
- >= 4 sections (validator S06)
- Each section >= 3 non-empty lines (validator S08)
- Largest section >= 30% of body (validator S07)
- >= 1 table (S11), >= 1 code block (S12), >= 1 URL (S13)
## KC Type Selection
| Content | Type | Body Structure |
|---------|------|---------------|
| External tech (APIs, patterns) | domain_kc | Quick Ref + Concepts + Phases + Rules + Flow + Compare + Refs |
| CEX-internal (architecture) | meta_kc | Summary + Spec + Patterns + Anti + Application + Refs |
Default: domain_kc. Use meta_kc only for CEX system documentation.
## Freshness
- updated field should reflect last meaningful edit
- Knowledge degrades slower than model_cards (no 90-day hard gate)
- Stale KCs identified by brain_query freshness ranking

### bld_examples_knowledge_card.md
---
kind: examples
id: bld_examples_knowledge_card
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_card artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: knowledge-card-builder
## Golden Example
INPUT: "Destila conhecimento sobre prompt caching para otimizar custos LLM"
OUTPUT:
```yaml
id: p01_kc_prompt_caching
kind: knowledge_card
pillar: P01
title: "Prompt Caching Patterns for LLM Cost Optimization"
version: "1.0.0"
created: "2026-03-24"
updated: "2026-03-24"
author: "builder"
domain: llm_engineering
quality: null
tags: [prompt-caching, cost-optimization, latency, anthropic, openai, knowledge]
tldr: "Prompt caching reutiliza prefixos pre-processados entre chamadas LLM, reduzindo custo em ate 90% e latencia em 85%"
when_to_use: "Quando sistema LLM repete contexto longo entre chamadas"
keywords: [prompt-caching, cache-control, context-reuse]
long_tails:
  - Como configurar prompt caching na API da Anthropic
  - Tamanho minimo de prefixo para ativar cache em LLMs
axioms:
  - SEMPRE coloque conteudo estatico ANTES do dinamico
  - NUNCA cache contexto que muda a cada request
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 0.91
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
# Prompt Caching Patterns for LLM Cost Optimization
## Quick Reference
```yaml
topic: prompt_caching
scope: LLM API optimization (Anthropic, OpenAI, Google)
owner: builder
criticality: high
```
## Key Concepts
- **Cache-Control**: Anthropic `cache_control: {kind: "ephemeral"}`; TTL 5 min
- **Prefix Matching**: cache hit when prefix identical byte-a-byte
- **Minimum Tokens**: Anthropic >= 1024; OpenAI >= 1024 (auto)
- **Pricing Split**: write 1.25x base, read 0.1x (90% savings on hit)
## Strategy Phases
1. **Audit**: identify prompts with >50% static content
2. **Reorder**: static first (system > few-shot > RAG), dynamic last
3. **Annotate**: add cache breakpoints on last static block
4. **Monitor**: measure hit rate via response headers
5. **Tune**: target >= 80% hit rate, adjust granularity
## Golden Rules
- ORDENE: static first, dynamic last (always)
- AGRUPE: few large cacheable blocks > many small ones
- METRIZE: hit_rate = read / (read + creation + uncached)
- INVALIDE com cuidado: 1 byte diff = full cache miss
## Flow
```text
[Request] -> [Hash Prefix] -> [Cache Lookup]
                                   |
                         HIT: 0.1x cost, 85% faster
                         MISS: 1.25x cost, normal speed
                                   |
                             [Generate] -> [Response]
```
## Comparativo
| Provider | Min Tokens | Config | Write | Read | TTL |
|----------|-----------|--------|-------|------|-----|
| Anthropic | 1024 | Explicit | 1.25x | 0.1x | 5 min |
| OpenAI | 1024 | Automatic | 1.0x | 0.5x | 5-60 min |
| Google | 32768 | Explicit | 1.0x | 0.25x | config |
## References
- Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Related: p01_kc_rag_fundamentals (context reuse patterns)
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_kc_ pattern (H03 pass)
- kind: knowledge_card (H04 pass)
- 13 required fields present (H06 pass)
- tags: list >= 3 (H07 pass)
- body 200-5120 bytes (H08 pass)
- No internal paths (H09 pass)
- author not orchestrator (H10 pass)
- 7 sections >= 3 lines (S06, S08 pass)
- Bullets <= 80 chars (S10 pass)
- Tables + code blocks + external URL (S11-S13 pass)
- linked_artifacts with primary+related (S20 pass)
## Anti-Example
INPUT: "Documenta prompt caching"
BAD OUTPUT:
```yaml
id: prompt_caching_knowledge
kind: knowledge_card
title: Prompt Caching
author: orchestrator
quality: 9.0
tags: "caching, llm"
This document describes how prompt caching works.
In summary, it saves money. As mentioned before, caching is good.
See records/core/docs/caching.md for details.
```
FAILURES:
1. id: no `p01_kc_` prefix -> H03 FAIL
2. lp: missing -> H06 FAIL
3. author: orchestrator -> H10 FAIL

### bld_knowledge_card_knowledge_card.md
---
kind: knowledge_card
id: bld_knowledge_card_knowledge_card
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for knowledge_card production — atomic searchable facts
sources: validate_kc.py v2.0, _schema.yaml v4.0, 721 real knowledge cards
---

# Domain Knowledge: knowledge_card
## Executive Summary
Knowledge cards are atomic searchable facts — the smallest retrieval unit in a knowledge system. Each card answers ONE question about ONE topic with density >= 0.80 (>80% concrete data, no filler). Cards are retrieved via hybrid search (BM25 + vector) using frontmatter fields. They differ from model cards (LLM specs), learning records (internal experience), and context docs (domain background).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Frontmatter fields | 14 required + 5 extended |
| Quality gates | 10 HARD + 20 SOFT |
| Max body | 5120 bytes |
| Min body | 200 bytes |
| Density minimum | >= 0.80 |
| Size sweet spot | 50-80 lines (single concept), 80-120 (multi-pattern) |
| Scoring dimensions | D1 Frontmatter, D2 Density, D3 Axioms, D4 Structure, D5 Format |
## Patterns
- **Retrieval surface**: frontmatter fields drive search discovery
| Field | Retrieval role | Pattern |
|-------|---------------|---------|
| tldr | Primary match (BM25 + embedding) | Specific: "Execute CLI via subprocess, retry 3x" |
| tags | Faceted filtering, clustering | 3-7 tags, mix domain + technique |
| keywords | BM25 exact match boost | 2-5 terms user would literally type |
| long_tails | Semantic/vector search | Full phrases: "how to handle concurrent token refresh" |
| when_to_use | Agent activation trigger | Specific context, not "when needed" |
- **Density hierarchy** (most to least info/token): tables > code blocks > bullets > ASCII diagrams > paragraphs
- **Two body structures**: domain_kc (external knowledge: Quick Ref, Key Concepts, Strategy, Golden Rules, Flow, References) and meta_kc (system-internal: Exec Summary, Spec Table, Patterns, Anti-Patterns, Application, References)
- **Density gate**: density = data_lines / total_non_empty_lines; < 0.80 = card fails regardless of other quality
- **Axiom form**: ALWAYS/NEVER/IF-THEN with condition + action + consequence
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague tldr ("How to use CLI") | No search signal; returns wrong in BM25 |
| Prose body | Low density; convert to tables, bullets, code |
| Template residue ({{placeholder}}) | Unfilled fields; looks incomplete |
| Frontmatter echo in body | Body repeats title/tldr; adds zero depth |
| Giant monolith (300+ lines) | Split into 2+ focused atomic cards |
| density < 0.80 | Card fails regardless of other quality scores |
## Application
1. Define ONE topic: what single question does this card answer?
2. Write frontmatter: all 14 required fields with specific, search-optimized values
3. Select body structure: domain_kc (external) or meta_kc (internal)
4. Write dense body: tables first, bullets second, paragraphs only when necessary
5. Check density: data_lines / total >= 0.80
6. Validate: <= 5120 bytes, >= 200 bytes, axioms in ALWAYS/NEVER/IF-THEN form
## References
- validate_kc.py v2.0: 10 HARD + 20 SOFT gate validator
- _schema.yaml v4.0: canonical field definitions for knowledge_card
- 721 real knowledge cards: empirical patterns (p95 body = 4274 bytes)
- Information retrieval: BM25 + vector hybrid search for dense retrieval

### bld_memory_knowledge_card.md
---
id: p10_lr_knowledge_card_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Knowledge cards with body density below 0.80 (ratio of informative content to total words) fail the density gate and require rewrite. Bullets over 80 characters are caught by validator and force reformatting. Filler phrases ('this document describes', 'it is worth noting') consume tokens without adding information and are the primary cause of low density scores. Axioms written as observations ('caching improves performance') instead of rules ('ALWAYS declare cache TTL, NEVER cache without expiry') are rejected by S18. Cards referencing internal system paths fail H09."
pattern: "Achieve density >= 0.80 by: replacing prose paragraphs with bullet lists, replacing descriptions with comparison tables, removing all transition sentences, ensuring each bullet contains exactly one fact. Axioms must be ALWAYS/NEVER imperatives, not observations. Quality field must be null — scoring is external. Body size 200 bytes minimum, 5KB maximum. No internal paths in any field."
evidence: "11 knowledge card productions: 6 failed first density check (avg density 0.64). After applying bullet+table conversion, avg density reached 0.83. Axiom format errors in 4 of 11 (observation format instead of ALWAYS/NEVER). H09 path violations in 2 early productions. Quality set to a number in 3 early productions (validator rejections)."
confidence: 0.75
outcome: SUCCESS
domain: knowledge_card
tags: [knowledge-card, density, axioms, frontmatter, atomic-facts, classification]
tldr: "Density >= 0.80 requires bullets over prose and tables over descriptions. Axioms are ALWAYS/NEVER rules, not observations. quality:null always."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [knowledge_card, density, axiom, frontmatter, bullet, table, tldr, domain, meta, quality_null]
---

## Summary
Knowledge cards distill domain knowledge into high-density atomic facts. The primary quality gate is density >= 0.80 — the ratio of informative content to total words. The most reliable path to high density is structural: replace prose with bullets, replace descriptions with tables, and eliminate all filler language.
## Pattern
Density boosting techniques (apply in order):
1. **Prose -> bullets** - Convert every paragraph into a bullet list. Each bullet = one fact. If a bullet needs a sub-fact, use a nested bullet, not a compound sentence.
2. **Descriptions -> tables** - Convert any comparison, enumeration, or mapping into a markdown table. Tables carry ~3x the information per line compared to prose.
3. **Remove transitions** - Delete: "as we can see", "it is worth noting", "in summary", "this document", "the following". These add zero information.
4. **Bullet length** - Each bullet under 80 characters. If over, split into two bullets or use a table.
5. **Axiom format** - Every axiom must be an imperative starting with ALWAYS or NEVER. Not "caching is important" but "ALWAYS declare TTL when caching, NEVER cache without expiry".
Frontmatter rules:
- `quality: null` always — scoring is external, never self-assigned
- `id` slug uses underscores: `p01_kc_topic_name`
- `tags` as YAML list, not comma-separated string
- No paths containing `records/`, `.claude/`, `/home/`, `C:\` anywhere in the card
Body size constraints: minimum 200 bytes (4+ sections with 3+ lines each), maximum 5KB.
## Anti-Pattern
- Prose paragraphs — density drops below 0.70 immediately.
- Bullets over 80 chars — validator S10 catches, forces reformatting.
- Axiom as observation: "Caching improves performance" — must be "ALWAYS declare cache TTL".
- `quality: 8.5` — validator H05 rejects any non-null value.
- `tags: "ai, ml, cache"` as string — validator H07 rejects, must be YAML list.
- Internal paths in any field — validator H09 rejects, breaks portability.
- Self-referencing tldr: "This card describes caching" — tldr must be the direct fact, not a description of the card.
## Context

### bld_output_template_knowledge_card.md
---
kind: output_template
id: bld_output_template_knowledge_card
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for knowledge_card production
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: knowledge_card (domain_kc)
```yaml
id: p01_kc_{{topic_slug}}
kind: knowledge_card
pillar: P01
title: "{{Title 5-100 chars}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{satellite_name}}"
domain: {{domain_name}}
quality: null
tags: [{{tag1}}, {{tag2}}, {{tag3}}, knowledge]
tldr: "{{Dense <=160ch, no self-refs}}"
when_to_use: "{{Retrieval condition}}"
keywords: [{{kw1}}, {{kw2}}, {{kw3}}]
long_tails:
  - {{long tail query 1}}
  - {{long tail query 2}}
axioms:
  - {{ALWAYS/NEVER actionable rule}}
linked_artifacts:
  primary: {{artifact_id_or_null}}
  related: [{{related_id_or_empty}}]
density_score: {{0.80_to_1.00}}
data_source: "{{source_url_or_artifact_ref}}"
# {{Title}}
## Quick Reference
` ``yaml
topic: {{topic_name}}
scope: {{scope_description}}
owner: {{owner_satellite}}
criticality: {{low|medium|high}}
` ``
## Key Concepts
- **{{Concept 1}}**: {{concrete detail with example}}
- **{{Concept 2}}**: {{concrete detail with example}}
- **{{Concept 3}}**: {{concrete detail with example}}
## Strategy Phases
1. **{{Phase 1}}**: {{action with measurable outcome}}
2. **{{Phase 2}}**: {{action with measurable outcome}}
3. **{{Phase 3}}**: {{action with measurable outcome}}
## Golden Rules
- {{RULE 1 — actionable, concrete}}
- {{RULE 2 — actionable, concrete}}
- {{RULE 3 — actionable, concrete}}
## Flow
` ``text
[{{Input}}] -> [{{Process}}] -> [{{Decide}}] -> [{{Output}}]
` ``
## Comparativo
| {{Dimension}} | {{Option A}} | {{Option B}} |
|---------------|-------------|-------------|
| {{Row 1}} | {{val}} | {{val}} |
| {{Row 2}} | {{val}} | {{val}} |
## References
- Related artifact: {{artifact_ref}}
- Source: {{external_url}}
```
NOTE: For meta_kc, replace body with:
Executive Summary, Spec Table, Patterns, Anti-Patterns, Application, References.

### bld_quality_gate_knowledge_card.md
---
id: p11_qg_knowledge_card
kind: quality_gate
pillar: P11
title: "Gate: Knowledge Card"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: "edison"
domain: "knowledge_card — atomic searchable facts with high information density"
quality: null
tags: [quality-gate, knowledge-card, density, fact, distillation, searchability]
tldr: "Gates ensuring knowledge_card artifacts contain concrete atomic facts with density >= 0.8, semantic frontmatter, and file size <= 5KB."
density_score: 0.94
---

# Gate: Knowledge Card
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: knowledge_card` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^KC_[A-Z0-9_]+$` | Lowercase, missing KC_ prefix, or non-alphanumeric chars |
| H03 | ID equals filename stem | `id: KC_REDIS_TTL` in file `KC_CACHE_TTL.md` |
| H04 | Kind equals literal `knowledge_card` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All 19 required fields present | Missing: domain, tldr, density_score, sources, or card_type |
| H07 | `density_score` is a float in range [0.0, 1.0] | Outside range or non-numeric value |
| H08 | `density_score` >= 0.8 | Score below threshold — card too sparse to be useful |
| H09 | Total file size <= 5120 bytes | Exceeds 5KB limit |
| H10 | `tldr` is <= 160 characters | tldr exceeds character limit |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Factual concreteness | 1.0 | Card contains specific values, numbers, or verifiable facts | Mix of facts and vague statements | Entirely vague or conceptual |
| S02 | Atomicity | 1.0 | Card covers exactly one concept with no scope creep | Mostly one concept; minor tangents | Multiple unrelated concepts |
| S03 | Searchability — tags | 1.0 | Tags cover domain, subtopic, and use-case angles (>= 4 distinct tags) | 3 tags | Fewer than 3 tags |
| S04 | Source attribution | 1.0 | At least one specific source (URL, paper, spec version, date) | Source mentioned but not specific | No sources |
| S05 | Card type classification | 0.5 | `card_type` is `domain_kc` or `meta_kc` with correct body structure for that type | Type present but body structure mismatches | Type absent |
| S06 | Density discipline | 1.0 | No padding, no restatements, no filler sentences in body | Minor padding present | More than 20% filler content |
| S07 | tldr precision | 1.0 | tldr is a standalone searchable sentence capturing the key fact | tldr too vague to retrieve the card | tldr absent or over 160 characters |
| S08 | Currency | 0.5 | `created` date present; `updated` reflects last substantive revision | Created date only, no updated | No dates |
| S09 | Cross-references | 0.5 | Related cards or concepts linked in body | Related concepts mentioned but not linked | No cross-references |
| S10 | Practical applicability | 1.0 | Body answers "when would I use this?" with a concrete scenario | Implicitly applicable but not stated | Pure theory with no application context |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to knowledge pool as authoritative reference card |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Rapidly evolving topic where sources are not yet stabilized (e.g., new library release, breaking API change) |
| Approver | Domain expert reviewer |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `knowledge-card-builder` for pipeline function `INJECT`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
