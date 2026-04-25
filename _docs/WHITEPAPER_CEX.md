# CEX: A Relational Model for AI Knowledge

**Technical Whitepaper v3.0** | March 2026

*For developers, data architects, and AI engineers who understand
why databases needed SQL -- and why AI codebases need the same revolution.*

---

## Abstract

Every AI framework solves execution: how to run chains, orchestrate agents,
call tools. None solves organization: how to structure, discover, validate,
and govern the knowledge that feeds those systems.

CEX proposes a relational model for AI knowledge -- a typed, indexed, governed
taxonomy that does for LLM artifacts what SQL did for data in 1970.

**Central thesis**: The industry treats AI knowledge as STRING.
CEX treats it as TYPED TABLE. Same revolution, different decade.

---

## 1. The Problem: Humans Are the Bottleneck

A human says: *"I want an ultra prompt to sell my course."*

That is 9 tokens. The LLM needs 8 dimensions filled to produce quality output:

| # | Dimension | What LLM needs | What human gave |
|---|-----------|-----------------|-----------------|
| 1 | BECOME | Who am I? (identity) | -- (0%) |
| 2 | INJECT | What do I know? (knowledge) | "my course" (20%) |
| 3 | REASON | How do I think? (method) | -- (0%) |
| 4 | CALL | What tools do I have? | -- (0%) |
| 5 | PRODUCE | What output format? | "prompt" (30%) |
| 6 | CONSTRAIN | What are the rules? | -- (0%) |
| 7 | GOVERN | What quality bar? | "ultra" (10%) |
| 8 | COLLABORATE | Who receives this? | -- (0%) |

**Coverage: 7.5%.** The human provided 0.6 of 8.0 dimensions.
The remaining 92.5% is MISSING. This is not an edge case -- it is
the normal state of every human-to-LLM interaction, every day.

The human is the bottleneck. Not because they are incapable,
but because they are human. **CEX closes this gap automatically.**

---

## 2. The 8 Functions: An Empirical Discovery

### 2.1 Origin: 337 Artifacts, 12 Frameworks

| Framework | Artifacts | Mapped to 8F | Orphans |
|-----------|-----------|--------------|---------|
| LangChain | 47 | 44 (93%) | 3 |
| CrewAI | 31 | 29 (93%) | 2 |
| DSPy | 28 | 27 (96%) | 1 |
| AutoGen | 34 | 31 (91%) | 3 |
| Haystack | 39 | 37 (94%) | 2 |
| LlamaIndex | 42 | 40 (95%) | 2 |
| Guidance | 18 | 17 (94%) | 1 |
| Instructor | 15 | 15 (100%) | 0 |
| Outlines | 12 | 12 (100%) | 0 |
| LMQL | 16 | 15 (93%) | 1 |
| LangGraph | 22 | 21 (95%) | 1 |
| Semantic Kernel | 33 | 31 (93%) | 2 |
| **TOTAL** | **337** | **319 (94.7%)** | **18** |

The 18 orphans: config (5), README (4), test fixtures (3), CI/CD (4), license (2). Infrastructure -- not AI functions.

**94.7% of AI artifacts across 12 frameworks map to 8 functions. 0% orphans are unmapped AI functions.**

### 2.2 The 8 Functions

| # | Function | Question | SQL Equivalent |
|---|----------|----------|----------------|
| 1 | BECOME | Who am I? | CREATE TABLE |
| 2 | INJECT | What do I know? | INSERT |
| 3 | REASON | How do I think? | WHERE clause |
| 4 | CALL | What tools? | Stored procedure |
| 5 | PRODUCE | What output? | SELECT result |
| 6 | CONSTRAIN | What rules? | CHECK + FK |
| 7 | GOVERN | Good enough? | EXPLAIN + AUDIT |
| 8 | COLLABORATE | Who next? | JOIN + FEDERATE |

### 2.3 Proof That 8 Is Exact (Not 7, Not 9)

**Proof 1 -- Philosophical (removal test):**

| Remove | Result |
|--------|--------|
| BECOME | Schizophrenic AI (who am I?) |
| INJECT | Ignorant AI (what do I know?) |
| REASON | Impulsive AI (how to think?) |
| CALL | Impotent AI (what can I do?) |
| PRODUCE | Mute AI (what do I output?) |
| CONSTRAIN | Lawless AI (what limits?) |
| GOVERN | Standardless AI (good enough?) |
| COLLABORATE | Isolated AI (who is next?) |

Add a 9th -- it reduces to an existing function:

| Candidate | Reduces to |
|-----------|------------|
| LEARN | GOVERN (feedback loop) |
| REMEMBER | INJECT (memory = input) |
| EXPLAIN | PRODUCE (explanation = output) |
| PLAN | REASON (planning = reasoning) |
| ADAPT | REASON (adaptation = re-reasoning) |
| PERSIST | PRODUCE + COLLABORATE |

Every 9th is a subset. None of the 8 is subset of another. **8 orthogonal. Minimum necessary, maximum sufficient.**

**Proof 2 -- Structural (isomorphism across 4 independent domains):**

| CEX | Shannon 1948 | OODA Loop | Compiler | Neuroscience |
|-----|-------------|-----------|----------|--------------|
| BECOME | Source identity | -- | #include | Self-model |
| INJECT | Encoding | Observe | #define | Declarative memory |
| REASON | Channel select | Orient | Parsing+AST | Prefrontal cortex |
| CALL | Transmission | Decide | Library call | Motor system |
| PRODUCE | Decoding | Act | Codegen | Output cortex |
| CONSTRAIN | Noise filter | -- | Type check | Inhibitory system |
| GOVERN | Feedback | -- | Test/debug | Metacognition |
| COLLABORATE | Destination | Loop | Linking (ld) | Social cognition |

4 independent models, same 8 blocks. Not coincidence -- structure.

**Proof 3 -- Empirical:** 94.7% coverage across 337 artifacts (see 2.1).

---

## 3. The SQL Analogy: Deep Mapping

### 3.1 Concept-by-Concept

| SQL Concept | CEX Equivalent | What it does |
|-------------|----------------|--------------|
| DATABASE | Repository | Container for everything |
| SCHEMA | Pillar (P01-P12) | Organizational namespace |
| TABLE | Kind (300 kinds) | Shape/format of data |
| COLUMN | Frontmatter field | Required attributes |
| ROW | Instance (.md file) | One real artifact |
| PRIMARY KEY | id (== filename stem) | Unique identifier |
| FOREIGN KEY | references[] | Synapses between files |
| INDEX | Naming convention | How to FIND fast |
| VIEW | compiled/ (.yaml) | Same data, different form |
| MATERIALIZED VIEW | Auto-compiled on commit | Always fresh |
| CHECK | max_bytes, density | Value validation |
| NOT NULL | required: true | Mandatory fields |
| UNIQUE | id == stem | No duplicates |
| TRIGGER | Pre-commit hook | Automatic on event |
| STORED PROCEDURE | Builder (13 files) | Factory for data |
| NORMALIZATION | density >= 0.80 | Zero derivable redundancy |
| TRANSACTION | Atomic commit | All or nothing |
| EXPLAIN PLAN | cex doctor --explain | Diagnose query cost |
| INFO_SCHEMA | _schema.yaml | Metadata of metadata |
| INSERT | cex forge | Create new artifact |
| SELECT | find -name | Discovery/search |
| DELETE CASCADE | cex doctor --cascade | Show deletion impact |
| JOIN | Synapse graph | Connect artifacts |
| FEDERATED DB | Distributed registry | Share across repos |

### 3.2 INDEX = Naming Convention (The Key Insight)

In SQL without INDEX:

    SELECT * FROM users WHERE email = x -- FULL TABLE SCAN. O(n). Slow.

In SQL with INDEX on email:

    SELECT * FROM users WHERE email = x -- INDEX LOOKUP. O(log n). Fast.

In CEX without naming convention:

    "Find the knowledge card for the agent builder"
    FULL REPO SCAN. Open ALL .md. O(n). 930 files x 10 tokens = 9,300 wasted.

In CEX with naming v2.0:

    find -name "bld_knowledge_card_agent*"
    INDEX LOOKUP. O(1). 0 tokens wasted. 1 exact result. 23x fewer reads.

**The naming convention IS the index.** A DBA never creates a table without an index. A CEX repo should never have files without semantic naming.

### 3.3 Normal Forms

| Form | SQL | CEX |
|------|-----|-----|
| 1NF | Each cell = 1 atomic value | Each file = 1 purpose (13 per builder) |
| 2NF | Column depends on full key | Frontmatter depends on complete id |
| 3NF | No column depends on non-key | density >= 0.80 = zero redundancy |

### 3.4 Advanced SQL Concepts

**Foreign Keys:** Pre-commit validates references[] point to existing IDs.  shows deletion impact.

**Materialized Views:** Post-commit auto-compiles .md to .yaml. INDEX.md recalculated. Never stale.

**EXPLAIN PLAN:**  shows LLM navigation cost. With naming v2.0: 3 reads, 5KB. Without: 70 reads, 140KB. **23x gain.**

**INFORMATION_SCHEMA:** _schema.yaml per pillar = self-describing metadata.  shows schema, instance count, fill rate, avg quality.

---

## 4. The Taxonomy: 123 Kinds in 12 Pillars

| Group | Pillars | Functions |
|-------|---------|-----------|
| CORE | P01 Knowledge, P02 Model, P03 Prompt, P04 Tools | BECOME, INJECT, REASON, CALL |
| QUALITY | P05 Output, P06 Schema, P07 Evals, P08 Architecture | PRODUCE, CONSTRAIN, GOVERN |
| SCALE | P09 Config, P10 Memory, P11 Feedback, P12 Orchestration | GOVERN, COLLABORATE |

### Naming Grammar (Fractal)

    {layer}_{kind}_{topic}.{ext}

| Layer | Prefix | Example |
|-------|--------|---------|
| Builder (L0) | bld_ | bld_system_prompt_agent.md |
| Template (L1) | tpl_ | tpl_knowledge_card.md |
| Example (L1) | ex_ | ex_knowledge_card_rag.md |
| Instance (L2) | -- | knowledge_card_rag.yaml |

Rules: Max 50 chars. snake_case. ASCII only. id == stem. Same grammar at every layer.

---

## 5. The Compilation Pipeline

### 5.1 The Core Concept

    Compiler C:   .c    -> preprocess -> parse -> optimize -> codegen -> .exe
    Compiler CEX: intent -> capture -> decompose -> hydrate -> compile -> envelope -> prompt

The user NEVER writes the final prompt. The user gives INTENT. CEX COMPILES it. Like writing .c, never assembly.

### 5.2 Technical Keywords

| Concept | Term | Analogy |
|---------|------|---------|
| Raw user desire | INTENT | Unprocessed. 5-20 tokens |
| Break into 8 dims | DECOMPOSITION | Package into 8 orthogonal dimensions |
| Fill missing dims | HYDRATION | React: dry HTML + state = living app |
| Assemble layers | COMPILATION | 50 .c files -> 1 binary |
| Wrap in protocol | ENVELOPE | HTTP request: headers + body |
| Verify 8/8 filled | COMPLETENESS AUDIT | Code coverage for prompts |
| Test each function | FUNCTION COVERAGE TEST | Unit test each dimension |

### 5.3 Hybrid Engine (90% Cost Reduction)

| Phase | Engine | Cost | Deterministic |
|-------|--------|------|---------------|
| CAPTURE | Python | /usr/bin/bash | Yes |
| DECOMPOSE | LLM micro (haiku) | ~/usr/bin/bash.001 | No |
| HYDRATE | Python + SQLite | /usr/bin/bash | Yes |
| COMPILE | Python + Jinja2 | /usr/bin/bash | Yes |
| ENVELOPE | Python | /usr/bin/bash | Yes |

80% deterministic. 90% cheaper than full-LLM approach.

### 5.4 Full Walkthrough

**INPUT**: "I want an ad for my Python course" (8 tokens)

**PHASE 1 -- CAPTURE:** raw_intent captured. 8 tokens.

**PHASE 2 -- DECOMPOSE:**

| Function | Filled | Extracted |
|----------|--------|-----------|
| BECOME | 0% | (who should AI be? not said) |
| INJECT | 20% | "my Python course" (vague) |
| REASON | 0% | (how to reason? not said) |
| CALL | 0% | (tools? not said) |
| PRODUCE | 25% | "ad" (type but no format) |
| CONSTRAIN | 0% | (rules? not said) |
| GOVERN | 0% | (quality bar? not said) |
| COLLABORATE | 0% | (who receives? not said) |
| **COVERAGE** | **5.6%** | **0.45 of 8.0 dimensions** |

**PHASE 3 -- HYDRATE (fill from repo):**

| Function | Source | Hydrated with |
|----------|-------|---------------|
| BECOME | bld_system_prompt_copywriter.md | Identity: copywriter, persuasive |
| INJECT | ex_knowledge_card_python_course.md | Title, price, benefits, objections |
| INJECT+ | ex_few_shot_ad_course.md (x3) | 3 real examples (2 wins, 1 failure) |
| REASON | bld_instruction_copywriter.md | AIDA: Attention-Interest-Desire-Action |
| CALL | (none needed) | tools=[] (explicitly empty) |
| PRODUCE | tpl_response_format_ad.md | headline + body + CTA + hashtags |
| CONSTRAIN | bld_quality_gate_copywriter.md | Max 2200 chars, casual, emoji max 3 |
| GOVERN | quality gate rubric | clarity>=8, persuasion>=9, CTA>=9 |
| COLLABORATE | (inferred) | next=null (terminal) |
| **COVERAGE** | **100%** | **8.0 of 8.0 dimensions** |

From 5.6% to 100%. **CEX filled the 94.4% the human did not provide.**

**PHASE 4 -- COMPILE:** 8 layers assembled in correct order. BECOME before INJECT. INJECT before REASON. Not arbitrary.

**PHASE 5 -- ENVELOPE:**

    +--------------------------------------------------+
    | SYSTEM PROMPT (outer -- user never sees)          |
    |  BECOME: copywriter, persuasive, no jargon       |
    |  CONSTRAIN: max 2200, casual, emoji max 3        |
    |  GOVERN: self-evaluate clarity>=8, CTA>=9        |
    +--------------------------------------------------+
    | CONTEXT (knowledge -- before user prompt)         |
    |  INJECT: course details, price, proof, audience   |
    |  REASON: AIDA framework, 3 options, pick best    |
    |  FEW-SHOT: 3 real ad examples                    |
    +--------------------------------------------------+
    | USER PROMPT (original intent INSIDE envelope)    |
    |  "I want an ad for my Python course"             |
    +--------------------------------------------------+
    | ROUTING (metadata -- invisible to LLM)           |
    |  next:null | coverage:8/8 | sources:7            |
    |  quality_target:9.0 | compile_time:0.3s          |
    +--------------------------------------------------+

**Result:** 8 tokens in -> ~1,200 tokens compiled. **Amplification: 150:1.** Coverage: 100%.

### 5.5 The Brain Learns (Feedback Loop)

User: "Loved the ad -- sold 42 courses in 3 days"
-> CEX saves as few_shot: ex_few_shot_ad_python_42sales.md
-> Updates quality: score = 9.2 (real, not estimated)
-> Next compilation injects THIS as example. Brain got smarter.

User: "Too formal, didnt like it"
-> Updates knowledge_card_tone: "more colloquial"
-> Updates constraint: "avoid words: acquire, verify"
-> Next compilation uses corrected version. Brain learned from criticism.

---

## 6. Stress Test: Governance x 8 Functions

| Function | Governance | Gap |
|----------|-----------|-----|
| BECOME | OK | Naming v2.0 resolves discovery |
| INJECT | Partial | FK between KC and agent not enforced |
| REASON | Critical | Zero validation of chain quality |
| CALL | Partial | Skills without dependency check |
| PRODUCE | OK | Output template + schema cover it |
| CONSTRAIN | OK | Pre-commit + doctor cover it |
| GOVERN | Critical | Quality gates do not auto-execute |
| COLLABORATE | Critical | Zero synapse graph |

**3 OK, 2 partial, 3 critical.** Each critical gap = missing SQL concept:
- REASON -> needs per-kind STORED PROCEDURES
- GOVERN -> needs CHECK + TRIGGER automation
- COLLABORATE -> needs FK graph (ERD)

---

## 7. 8 Untapped Benefits

| # | Benefit | Industry does | Nobody does (CEX opportunity) | SQL analog |
|---|---------|--------------|-------------------------------|------------|
| B1 | Typed Injection | RAG injects blob | LLM knows WHAT it injects | TYPED COLUMNS |
| B2 | Identity Composition | 1 monolithic prompt | Compose identity from parts | JOIN |
| B3 | Reasoning Recipes | Generic CoT for all | Per-kind optimal strategy | STORED PROC/TABLE |
| B4 | Tool Auto-Discovery | Hardcoded tool list | find -name bld_skill_* | INDEX |
| B5 | Contract Validation | Test at runtime | Test chain at design-time | CHECK CONSTRAINT |
| B6 | Self-Evaluating | Eval separate from artifact | Artifact judges itself | CHECK + TRIGGER |
| B7 | Collaboration Graph | Hardcoded routing | Emergent dependency graph | FK + ERD |
| B8 | Distributed Registry | Each company = silo | npm install for knowledge | FEDERATED DB |

---

## 8. Builders: Stored Procedures (Self-Referential)

301 builders x 13 ISOs = 1,612+ stored procedures (1,630 total with shared ISOs).

Each builder = factory for one kind of artifact. system-prompt-builder produces identity files. instruction-builder produces method files. quality-gate-builder produces validation files.

**Self-referential loop:** system-prompt-builder follows schemas from validation-schema-builder, built by instruction-builder, whose quality is checked by quality-gate-builder, whose identity comes from system-prompt-builder. Loop closes. CEX eats its own dog food.

---

## 9. Governance Without Runtime

| Layer | Mechanism | Scope |
|-------|-----------|-------|
| LAW | CODEX.md + _schema.yaml | Read-dependent (any LLM) |
| GATE | Pre-commit hook (7 checks) | Universal (blocks all violators) |
| GUARD | cex doctor | On-demand diagnostics |

Checks: naming pattern, frontmatter fields, max_bytes, orphan detection, empty file, density, duplicate ID. FK integrity at commit. Cascade analysis before deletion.

---

## 10. Market Gap: Nobody Does This

| Category | Examples | What they bootstrap | What they DO NOT |
|----------|---------|--------------------|--------------------|
| AI Brain Builders | CustomGPTs, Claude Projects, Notion AI | Single prompt + flat files | Taxonomy, kinds, governance, composition |
| Agent Frameworks | LangChain, CrewAI, AutoGen, DSPy | Runtime execution | Knowledge organization, discovery, validation |
| Knowledge Mgmt | Obsidian, Roam, Mem.ai | Human thinking | LLM-operable structure, typed artifacts |
| Scaffolding | create-react-app, Vite, Cookiecutter | Code project structure | AI knowledge, builders, quality gates |

The gap:

    EXISTS:     "Bootstrap a WEBSITE"      (Lovable, Bolt, v0)
    EXISTS:     "Bootstrap an API"         (FastAPI template, Rails new)
    EXISTS:     "Bootstrap AGENTS"         (CrewAI, LangChain templates)
    NOT EXISTS: "Bootstrap an AI BRAIN"    <-- CEX fills this gap

Lovable bootstraps the FACE of your company. CEX bootstraps the BRAIN.

---

## 11. Bootstrap Behavior: The Product

### Day 1: cex init (human does once, 30 seconds)

    $ cex init
    Company name?  > MyBusiness
    Domain?        > [e-commerce / SaaS / education / services]
    Product(s)?    > "online Python course"
    Audience?      > "junior devs seeking first job"
    Tone of voice? > [formal / casual / technical / fun]

5 questions. 30 seconds. CEX generates a complete, operable repo: 301 builders ready, 123 kind knowledge cards, 125 sub-agent definitions, full governance (pre-commit, doctor, schemas), multi-LLM entry points (CLAUDE.md, .cursorrules, GPT system prompt).

### Day 2+: Human asks things, CEX compiles

    Human: "make an ad for my course"
    CEX:   CAPTURE(8 tok) -> DECOMPOSE(5.6%) -> HYDRATE(100%)
           -> COMPILE(8 layers) -> ENVELOPE(1200 tok)
    LLM:   executes with 100% context -> governed output, quality >= 9.0

The human does NOT need to know BECOME, INJECT, REASON...
The human does NOT need to know frontmatter, kind, pillar...
The human ONLY needs to know:
- "make an ad" -> ad appears, formatted, governed
- "didnt like it" -> next one is better (constraints updated)
- "sold 42 courses" -> brain gets smarter (few_shot saved)

### The Brain Grows

Every interaction enriches the repo:
- Successful outputs become few_shot examples (evidence-based)
- Feedback updates knowledge cards and constraints (self-correcting)
- Quality scores accumulate, improving routing (self-optimizing)
- The more you use it, the better it gets
- Day 1: functional. Day 30: expert. Day 365: irreplaceable.

---

## 12. The Pitch

**For a SQL audience:**
"SQL organized data. CEX organizes intelligence."

**For a startup audience:**
"The create-react-app for artificial intelligence."

**For a business audience:**
"1 command. Your company has proprietary AI. No code. No team. No 6 months."

**For a technical audience:**
"A prompt compilation pipeline that closes the 92.5% gap between human intent and what LLMs actually need. 8 typed dimensions. 150:1 amplification. Governed by design."

---

## References

1. Codd, E.F. (1970). A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*.
2. Shannon, C.E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*.
3. Boyd, J. (1996). The Essence of Winning and Losing (OODA Loop).
4. Wei et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS*.
5. Yao et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*.
6. Khattab et al. (2023). DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines. *arXiv*.
7. SQLite Consortium. The Most Widely Deployed Database Engine in the World.
8. Anthropic (2024-2026). Claude System Prompt Best Practices.

---

*CEX v3.0 -- "SQL organized data. CEX organizes intelligence."*
