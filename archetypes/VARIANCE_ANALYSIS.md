# Variance Analysis: 4 Builders x 13 File Positions

> Generated: 2026-03-26 | Author: builder_agent | Quality: 9.0+
> Source: model-card-builder, knowledge-card-builder, signal-builder, quality-gate-builder

---

## T1: File-by-File Variance Matrix

### Summary Table

| # | File Position | Universal % | Type-Specific % | Key Variables | Effort to Template |
|---|---------------|-------------|-----------------|---------------|--------------------|
| 1 | MANIFEST.md | ~60% | ~40% | id, domain, llm_function, keywords, crew_role | LOW |
| 2 | SCHEMA.md | ~15% | ~85% | ALL fields, body sections, constraints, naming | HIGH |
| 3 | SYSTEM_PROMPT.md | ~35% | ~65% | domain rules (5-10), boundary statement | MEDIUM |
| 4 | INSTRUCTIONS.md | ~45% | ~55% | phase-specific steps, tool references, validation criteria | MEDIUM |
| 5 | EXAMPLES.md | ~15% | ~85% | golden artifact (full), anti-patterns (10+), gate codes | HIGH |
| 6 | TOOLS.md | ~60% | ~40% | data sources, active validators, domain APIs | LOW |
| 7 | KNOWLEDGE.md | ~35% | ~65% | foundational standard, principles, boundary comparisons | MEDIUM |
| 8 | COLLABORATION.md | ~55% | ~45% | crew compositions, handoff protocol, dependencies | LOW |
| 9 | ARCHITECTURE.md | ~40% | ~60% | boundary confusions (5+), position diagram, fractal | MEDIUM |
| 10 | CONFIG.md | ~45% | ~55% | naming pattern, file paths, size limits, domain policy | MEDIUM |
| 11 | MEMORY.md | ~45% | ~55% | common mistakes (5-10), domain-specific state | MEDIUM |
| 12 | OUTPUT_TEMPLATE.md | ~10% | ~90% | ALL frontmatter vars, ALL body section templates | HIGH |
| 13 | QUALITY_GATES.md | ~25% | ~75% | HARD gates (9-10), SOFT gates (7-20), scoring formula | HIGH |

### Effort Distribution

| Effort | Files | % of Builder | Implication |
|--------|-------|-------------|-------------|
| LOW | MANIFEST, TOOLS, COLLABORATION | 23% | Copy skeleton + fill 3-5 vars |
| MEDIUM | SYSTEM_PROMPT, INSTRUCTIONS, KNOWLEDGE, ARCHITECTURE, CONFIG, MEMORY | 46% | Adapt sections, replace domain content |
| HIGH | SCHEMA, EXAMPLES, OUTPUT_TEMPLATE, QUALITY_GATES | 31% | Rewrite per type — domain expertise required |

---

### Detailed Analysis Per File Position

#### 1. MANIFEST.md — LOW effort

**Universal skeleton (shared across all 4):**
```yaml
# Frontmatter
id: {type}-builder
kind: type_builder
pillar: {LP}
parent: {parent_chief} [PLANNED]
domain: {type}
llm_function: {BECOME|COLLABORATE|GOVERN}
version: "2.0.0"
created/updated: date
author: agent_group
tags: list

# Sections (identical structure)
## Identity — 1 paragraph
## Capabilities — 3-5 bullets
## Routing — keywords + triggers
## Crew Role — 1 sentence
```

**Type-specific (40%):** Identity description, capability bullets, keyword list, crew role sentence.

**Variables to template:**
- `{{type}}` — artifact type name
- `{{LP}}` — learning path (P01-P12)
- `{{domain}}` — domain slug
- `{{llm_function}}` — BECOME/COLLABORATE/GOVERN
- `{{identity_description}}` — 1-sentence specialist description
- `{{capabilities}}` — 3-5 bullet list
- `{{keywords}}` — 5-8 routing keywords
- `{{crew_role}}` — what question this builder answers

---

#### 2. SCHEMA.md — HIGH effort

**Universal skeleton (~15%):**
- Frontmatter metadata
- "Artifact Identity" header (LP, Type, Machine format, Naming, Max bytes)
- "Frontmatter Fields" table headers (Field, Type, Required, Default, Notes)
- "Body Structure" section header
- "Constraints" section header

**Type-specific (~85%):**
- ALL field definitions (4-26 fields per type)
- Field types, defaults, enums, nested objects
- Body section requirements (0-12 sections)
- Size/density constraints
- Naming regex pattern
- Domain-specific semantic rules

**Evidence of variance:**
| Builder | Required Fields | Optional Fields | Body Sections | Special Objects |
|---------|----------------|-----------------|---------------|-----------------|
| model_card | 26 (frontmatter) | 0 | 5 | pricing{4}, modalities{5}, features{8} |
| knowledge_card | 13 + 6 CEX | 0 | 6-12 (2 variants) | Quick Reference yaml block |
| signal | 4 | 7 | 0 (JSON payload) | status enum, progress_pct semantics |
| quality_gate | ~8 | 0 | 5 | Definition table, Scoring table, Bypass |

**Conclusion:** SCHEMA is ~85% unique per type. Template can only provide table structure + constraint section headers. The fields themselves must be authored from `_schema.yaml` per LP.

---

#### 3. SYSTEM_PROMPT.md — MEDIUM effort

**Universal skeleton (~35%):**
```markdown
# {type}-builder System Prompt

You are {type}-builder, a CEX archetype specialist.
You know EVERYTHING about {domain_expertise}.

## Rules
1. ALWAYS read SCHEMA.md first
2-N. {domain_rules}

## Boundary
I build {type} ({what}). I do NOT build: {confusion_list}.
```

**Type-specific (~65%):** Domain expertise claim, 5-10 domain rules, boundary confusion list.

**Pattern observed:** Rules follow ALWAYS/NEVER format. Each builder has 7-10 rules. ~3 are universal (read schema, quality:null, no filler). ~5-7 are domain-specific.

**Universal rules (shared by all 4):**
1. ALWAYS read SCHEMA.md first (source of truth)
2. NEVER self-assign quality score (quality: null)
3. NEVER use filler phrases

**Type-specific rules (examples):**
- model_card: cite source URL, normalize pricing, check freshness 90d
- knowledge_card: atomic facts, density >= 0.80, bullets <= 80 chars, axioms
- signal: emit JSON only, atomic events, ISO 8601 timestamps
- quality_gate: separate HARD/SOFT, concrete thresholds, bypass policy

---

#### 4. INSTRUCTIONS.md — MEDIUM effort

**Universal skeleton (~45%):**
```markdown
## Phase 1: RESEARCH
1. Identify {what_to_build}
2. Check brain_query for duplicates
3. Gather sources
4. {domain_research_steps}

## Phase 2: COMPOSE
1. Read SCHEMA.md
2. Fill frontmatter fields
3. {domain_compose_steps}

## Phase 3: VALIDATE
1. Run validator (planned/active)
2. Check HARD gates
3. Check SOFT gates
4. If score < 8.0: revise
```

**Type-specific (~55%):** Phase 1 research targets, Phase 2 compose specifics (body sections, field-filling), Phase 3 validation tool references.

**Consistent 3-phase pattern across all 4 builders.** Phase names vary slightly (RESEARCH/CLASSIFY, COMPOSE, VALIDATE) but structure is identical.

---

#### 5. EXAMPLES.md — HIGH effort

**Universal skeleton (~15%):**
```markdown
## Golden Example
INPUT: "seed description"
OUTPUT: {complete_artifact}
WHY THIS IS GOLDEN: {checklist}

## Anti-Example
OUTPUT: {broken_artifact}
FAILURES: {gate_code_list}
```

**Type-specific (~85%):** The actual artifact content (frontmatter + body) is 100% domain-specific. Anti-patterns map to type-specific gates.

**Evidence:**
| Builder | Golden Lines | Anti-Pattern Failures | Gate Codes |
|---------|-------------|----------------------|------------|
| model_card | ~80 | 10 | H02-H10, S02-S10 |
| knowledge_card | ~90 | 10 | H03-H10, S02-S18 |
| signal | ~30 (JSON) | 5 | H01-H09 |
| quality_gate | ~50 | 4 | H02-H10 |

**Conclusion:** Examples are almost entirely bespoke. Only the section structure (Golden/Anti) is reusable.

---

#### 6. TOOLS.md — LOW effort

**Universal skeleton (~60%):**
```markdown
## Production Tools
| Tool | Purpose | When | Status |
| brain_query | Search existing {type}s | Phase 1 | ACTIVE |
| validate_artifact.py | Validate artifact | Phase 3 | PLANNED |
| cex_forge.py | Generate from seeds | Phase 2 | PLANNED |

## Data Sources / Runtime Interfaces
{type_specific_sources}

## Interim Validation
{checklist}
```

**Type-specific (~40%):** Data sources (model_card: 8 provider APIs; knowledge_card: validate_kc.py + pool; signal: signal_writer.py + monitor; quality_gate: reference gates). Most builders share brain_query + validate_artifact.py.

---

#### 7. KNOWLEDGE.md — MEDIUM effort

**Universal skeleton (~35%):**
```markdown
## Foundational Standard
{industry_reference}

## Industry Implementations / Patterns
| Source | What | CEX alignment |

## Key Principles
{domain_principles}

## Boundary vs Nearby Types
| Type | What | Why not {this_type} |

## References
```

**Type-specific (~65%):** Foundational standard (Mitchell 2019 for MC, atomicity for KC, stage-gate for QG, runtime events for SIG), principles, boundary comparisons.

---

#### 8. COLLABORATION.md — LOW effort

**Universal skeleton (~55%):**
```markdown
## My Role in Crews
I am a {SPECIALIST/INFRASTRUCTURE} builder.
I answer ONE question: "{question}"

## Crew Compositions
{2-3 numbered pipelines}

## Handoff Protocol
I Receive: {inputs}
I Produce: {artifact}
I Signal: {complete/retry}

## Dependencies
Builders I Depend On: {list_or_none}
Builders That Depend On Me: {downstream_list}
```

**Type-specific (~45%):** Role question, crew pipelines, dependency graph. All 4 builders follow identical handoff protocol structure.

---

#### 9. ARCHITECTURE.md — MEDIUM effort

**Universal skeleton (~40%):**
```markdown
## Boundary
{type} EH: {definition}
{type} NAO EH:
| Confusao | Por que NAO | Type correto |

## Position in {Flow_Type}
{ASCII diagram}

## Dependency Graph
{ASCII diagram}

## Fractal Position
LP: {LP}, Function: {function}, Scale: L0
```

**Type-specific (~60%):** Boundary confusion matrix (5+ entries), flow diagram (varies: boot flow for MC, knowledge flow for KC, runtime flow for SIG, governance flow for QG), dependency relationships.

---

#### 10. CONFIG.md — MEDIUM effort

**Universal skeleton (~45%):**
```markdown
## Naming Convention
| Scope | Convention | Example |
| Artifact | {lp_prefix}_{slug}.{ext} | ... |
| Builder dir | kebab-case | ... |
| Fields | snake_case | ... |

## File Paths
Output: cex/{LP_dir}/examples/{id}.{ext}
Compiled: cex/{LP_dir}/compiled/{id}.{ext}

## Size Limits
Body max: {N} bytes
Density: >= {0.80-0.85}
```

**Type-specific (~55%):** Naming pattern (p02_mc_ vs p01_kc_ vs p12_sig_ vs p11_qg_), format (md vs json), size limits, domain-specific policies (pricing for MC, KC type selection, progress_pct for SIG, bypass for QG).

---

#### 11. MEMORY.md — MEDIUM effort

**Universal skeleton (~45%):**
```markdown
## Accumulated Patterns / Recurrent Patterns
{domain_learnings}

## Common Mistakes
1-10 {mistakes_from_production}

## State Between Sessions
This builder is STATELESS per invocation.

## Production Counter
| Metric | Value |
```

**Type-specific (~55%):** Mistakes are entirely domain-specific (MC: pricing normalization; KC: density, bullets; SIG: quality vs quality_score, YAML; QG: subjective checks, weights).

---

#### 12. OUTPUT_TEMPLATE.md — HIGH effort

**Universal skeleton (~10%):**
```markdown
# {type} Output Template

Every field here exists in SCHEMA.md — template derives, never invents.

---
{frontmatter_template}
---

{body_template}
```

**Type-specific (~90%):** ALL frontmatter variables, ALL body section templates. This is essentially a fill-in-the-blank version of the complete artifact.

**Evidence:**
| Builder | Template Vars | Body Sections | Format |
|---------|--------------|---------------|--------|
| model_card | 30+ | 5 (Boundary, Specs, Capabilities, When to Use, References) | Markdown |
| knowledge_card | 22+ | 7 (Quick Ref, Concepts, Phases, Rules, Flow, Comparativo, Refs) | Markdown |
| signal | 12 | 0 (JSON payload) | JSON |
| quality_gate | 20+ | 5 (Definition, Checklist, Scoring, Actions, Bypass) | Markdown |

**Conclusion:** OUTPUT_TEMPLATE is the most type-specific file. Must be authored from scratch per type using SCHEMA.md as source.

---

#### 13. QUALITY_GATES.md — HIGH effort

**Universal skeleton (~25%):**
```markdown
## HARD Gates (block if ANY fails)
| Gate | Check | Why |

## SOFT Gates (contribute to score)
| Gate | Check | Weight | Score if pass |

## Scoring Formula
hard_pass = all HARD pass
soft_score = weighted sum
GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0

## Automation
Primary: validate_artifact.py --type {type}
Interim: manual check against this file

## Pre-Production Checklist
```

**Type-specific (~75%):** All gate definitions. HARD gates check type-specific field requirements. SOFT gates check type-specific quality dimensions.

**Evidence:**
| Builder | HARD Gates | SOFT Gates | Total |
|---------|-----------|-----------|-------|
| model_card | 10 | 15 | 25 |
| knowledge_card | 10 | 20 | 30 |
| signal | 9 | 9 | 18 |
| quality_gate | 10 | 7 | 17 |

**Universal HARD gates (present in all 4):**
- H01: format parses (YAML/JSON)
- H0x: id matches pattern
- H0x: id == filename stem
- H0x: type == literal
- H0x: lp == literal
- H0x: quality == null

**Type-specific HARD gates:** field requirements, size limits, boundary checks.

---

## T2: Type Complexity Classification (65 Remaining Types)

### Classification Criteria

| Tier | Criteria | Model Ideal | Count |
|------|----------|-------------|-------|
| SIMPLE | <=5 required fields, <=1024 bytes preferred, JSON-only possible, no complex body | sonnet/codex/gemini | 25 |
| MEDIUM | 6-15 fields OR 2-4 body sections OR template exists, moderate domain knowledge | sonnet/codex | 27 |
| COMPLEX | >15 fields OR 5+ body sections OR needs external research/domain expertise | opus | 13 |

### SIMPLE Tier (25 types)

| # | Type | LP | Layer | Required Fields | Max Bytes | Format | Has Template | Rationale |
|---|------|----|-------|----------------|-----------|--------|--------------|-----------|
| 1 | glossary_entry | P01 | content | 4 | 512 | yaml | No | Single definition, minimal |
| 2 | embedding_config | P01 | content | 4 | 512 | yaml | No | Config object, few fields |
| 3 | few_shot_example | P01 | content | 5 | 1024 | yaml | No | Input/output pair |
| 4 | rag_source | P01 | content | 6 | 1024 | yaml | Yes | Pointer to external source |
| 5 | lens | P02 | spec | 4 | 2048 | yaml | No | Single perspective |
| 6 | router | P02 | runtime | 3 | 1024 | yaml | No | Mapping table |
| 7 | fallback_chain | P02 | runtime | 3 | 512 | yaml | No | Ordered list |
| 8 | axiom | P10 | content | 0 | 3072 | yaml | No | Single immutable rule |
| 9 | hook | P04 | runtime | 3 | 1024 | yaml | No | Event trigger |
| 10 | client | P04 | runtime | 0 | 1024 | json | No | API client config |
| 11 | cli_tool | P04 | runtime | 0 | 1024 | yaml | No | CLI wrapper |
| 12 | connector | P04 | runtime | 0 | 1024 | json | No | Service connector |
| 13 | daemon | P04 | runtime | 0 | 1024 | yaml | No | Background process |
| 14 | naming_rule | P05 | spec | 0 | 4096 | yaml | No | Convention definition |
| 15 | input_schema | P06 | spec | 0 | 3072 | json | Yes | JSON schema |
| 16 | output_schema_P06 | P06 | spec | 0 | 3072 | json | No | Validation contract |
| 17 | type_def | P06 | spec | 0 | 3072 | yaml | No | Type definition |
| 18 | feature_flag | P09 | runtime | 0 | 1536 | json | Yes | On/off toggle |
| 19 | runtime_rule | P09 | runtime | 0 | 3072 | yaml | No | Timeout/retry config |
| 20 | path_config | P09 | runtime | 0 | 3072 | yaml | No | System paths |
| 21 | permission | P09 | governance | 0 | 3072 | yaml | No | Access rule |
| 22 | session_state | P10 | runtime | 0 | 3072 | yaml | Yes | Ephemeral state |
| 23 | spawn_config | P12 | runtime | 0 | 3072 | yaml | No | Spawn parameters |
| 24 | dispatch_rule | P12 | runtime | 0 | 3072 | yaml | No | Keyword-to-agent_group map |
| 25 | learning_record | P10 | content | 0 | 3072 | yaml | Yes | Learning entry |

### MEDIUM Tier (27 types)

| # | Type | LP | Layer | Required Fields | Max Bytes | Format | Has Template | Rationale |
|---|------|----|-------|----------------|-----------|--------|--------------|-----------|
| 1 | context_doc | P01 | content | 4 | 2048 | yaml | No | Domain synthesis needed |
| 2 | boot_config | P02 | spec | 5 | 2048 | yaml | Yes | Provider initialization |
| 3 | mental_model_P02 | P02 | spec | 3 | 2048 | yaml | No | Design blueprint |
| 4 | mcp_server | P04 | runtime | 5 | 2048 | json | Yes | Tool+resource config |
| 5 | plugin | P04 | runtime | 0 | 2048 | yaml | No | Extension interface |
| 6 | scraper | P04 | runtime | 0 | 1024 | yaml | No | Data extraction pattern |
| 7 | output_schema_P05 | P05 | spec | 0 | 4096 | json | Yes | Output format |
| 8 | parser | P05 | runtime | 0 | 4096 | yaml | No | Data extractor |
| 9 | formatter | P05 | runtime | 0 | 4096 | yaml | No | Presentation formatter |
| 10 | validator | P06 | spec | 0 | 3072 | yaml | Yes | Validation rules |
| 11 | interface | P06 | spec | 0 | 3072 | json | No | Integration contract |
| 12 | unit_eval | P07 | governance | 0 | 4096 | yaml | Yes | Agent unit test |
| 13 | smoke_eval | P07 | governance | 0 | 3072 | yaml | No | Quick sanity test |
| 14 | golden_test | P07 | governance | 0 | 4096 | yaml | Yes | Reference test case |
| 15 | instruction | P03 | prompt | 0 | 3072* | yaml | Yes | Step-by-step recipe |
| 16 | pattern | P08 | spec | 0 | 4096 | yaml | Yes | Reusable pattern |
| 17 | law | P08 | spec | 0 | 3072 | yaml | No | Operational law |
| 18 | component_map | P08 | spec | 0 | 3072 | yaml | No | Component mapping |
| 19 | diagram | P08 | spec | 0 | 4096 | yaml | No | Architecture diagram |
| 20 | env_config | P09 | runtime | 0 | 4096 | yaml | Yes | Environment vars |
| 21 | knowledge_index | P10 | runtime | 0 | 3072 | yaml | No | Search index config |
| 22 | mental_model_P10 | P10 | runtime | 0 | 3072 | yaml | Yes | Runtime state model |
| 23 | bugloop | P11 | runtime | 0 | 4096 | yaml | Yes | Fix-verify cycle |
| 24 | lifecycle_rule | P11 | governance | 0 | 4096 | yaml | No | Lifecycle policy |
| 25 | guardrail | P11 | governance | 0 | 4096 | yaml | No | Safety boundary |
| 26 | optimizer | P11 | runtime | 0 | 4096 | yaml | No | Process optimizer |
| 27 | handoff | P12 | runtime | 0 | 4096 | yaml | Yes | Task handoff packet |

### COMPLEX Tier (13 types)

| # | Type | LP | Layer | Required Fields | Max Bytes | Format | Has Template | Rationale |
|---|------|----|-------|----------------|-----------|--------|--------------|-----------|
| 1 | agent | P02 | runtime | 8 | 5120 | yaml | Yes | 10 body sections, most complex type |
| 2 | agent_package | P02 | spec | 0 | 4096 | yaml | Yes | Multi-file manifest, self-contained |
| 3 | agent_card | P08 | spec | 0 | 4096 | yaml | Yes | Complete agent_group definition |
| 4 | system_prompt | P03 | prompt | 6 | 4096 | yaml | Yes | Persona engineering, 4+ body sections |
| 5 | action_prompt | P03 | prompt | 0 | 2048* | yaml | No | No template, task decomposition |
| 6 | prompt_template | P03 | prompt | 5 | 8192 | yaml | Yes | 5 body sections, largest format |
| 7 | chain | P03 | prompt | 3 | 6144 | yaml | No | Multi-step sequencing |
| 8 | skill | P04 | runtime | 8 | 5120 | yaml | Yes | 4+ body sections, tool integration |
| 9 | e2e_eval | P07 | governance | 0 | 4096 | yaml | Yes | Pipeline testing |
| 10 | benchmark | P07 | governance | 0 | 4096 | yaml | No | Performance measurement |
| 11 | scoring_rubric | P07 | governance | 0 | 5120 | yaml | No | Evaluation dimensions |
| 12 | workflow | P12 | runtime | 0 | 3072 | yaml | Yes | Step graph + dependencies |
| 13 | dag | P12 | runtime | 0 | 3072 | yaml | No | Dependency graph |

### Tier Summary

| Tier | Count | % | Has Template | No Template | Avg Max Bytes |
|------|-------|---|-------------|-------------|---------------|
| SIMPLE | 25 | 38% | 5 (20%) | 20 (80%) | 1,741 |
| MEDIUM | 27 | 42% | 13 (48%) | 14 (52%) | 3,319 |
| COMPLEX | 13 | 20% | 8 (62%) | 5 (38%) | 4,513 |
| **Total** | **65** | **100%** | **26 (40%)** | **39 (60%)** | — |

### Template Coverage Impact

| Situation | Types | Effort Reduction |
|-----------|-------|-----------------|
| Template exists + SIMPLE | 5 | ~80% (mostly fill vars) |
| Template exists + MEDIUM | 13 | ~50% (adapt sections) |
| Template exists + COMPLEX | 8 | ~30% (template is skeleton only) |
| No template (any tier) | 39 | 0% (author from _schema.yaml) |

---

## Key Findings

### 1. Universal Builder Skeleton (reusable across ALL 65 types)
The 13-file structure itself is universal. A **meta-template** can generate ~40% of each builder:
- MANIFEST.md: ~60% reusable
- TOOLS.md: ~60% reusable (brain_query + validate_artifact shared)
- COLLABORATION.md: ~55% reusable
- INSTRUCTIONS.md: ~45% reusable (3-phase pattern)

### 2. Type-Specific Core (must be authored per type)
4 files require deep domain knowledge and cannot be meaningfully templated:
- SCHEMA.md (~85% unique)
- OUTPUT_TEMPLATE.md (~90% unique)
- EXAMPLES.md (~85% unique)
- QUALITY_GATES.md (~75% unique)

### 3. Recommended Generation Strategy

| Step | What | Who | Input |
|------|------|-----|-------|
| 1 | Generate skeleton (LOW files) | codex/gemini | _schema.yaml + TAXONOMY |
| 2 | Author core (HIGH files) | opus | _schema.yaml + existing examples + domain knowledge |
| 3 | Fill middle (MEDIUM files) | sonnet/codex | Skeleton + core files + existing builders as reference |
| 4 | Validate | any | QUALITY_GATES.md self-check |

### 4. Estimated Total Effort

| Tier | Types | Time/Type | Total Hours |
|------|-------|-----------|-------------|
| SIMPLE | 25 | ~8 min | ~3.3h |
| MEDIUM | 27 | ~15 min | ~6.7h |
| COMPLEX | 13 | ~25 min | ~5.4h |
| **Total** | **65** | — | **~15.4h** |

With 3 parallel slots at ~17 min avg/wave: **~22 waves, ~6-7 hours wall time.**
