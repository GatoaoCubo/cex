# CEX Session Checkpoint — 2026-03-26

**Resume from here.** Everything needed to continue Wave 1+.

---

## CURRENT STATE (commit 03041ca)

| Metric | Value |
|--------|-------|
| Total files | 1,661 |
| Builders (bld_*) | 932 (70 dirs x ~13 files) |
| Templates (tpl_*) | 85 (across 12 pillars) |
| Examples (ex_*) | 193 (all naming v2.0 compliant) |
| Legacy naming (p{NN}_*) | 0 in examples, 159 in compiled/ |
| Satellite in filenames | 0 (all renamed to director) |
| Satellite in content | ~567 files (future wave) |
| Wikilinks (graph edges) | 406 |
| Obsidian color groups | 12 (one per pillar, builders unified) |
| packages/ orphans | 157 files (real content, relocate to nuclei later) |

---

## WHAT WAS DONE (this session — 6 commits)

| # | Commit | What |
|---|--------|------|
| 1 | e40d658 | Whitepaper v3.0 -- 20KB, 12 sections, complete thesis |
| 2 | 4594dc0 | Rename 932 builders to naming v2.0 |
| 3 | 4b3bdfb | Obsidian graph colors by 8 LLM functions |
| 4 | 7b644c0 | Skeleton files: 47 new files + 278 wikilinks |
| 5 | 52106ab | 7 fractal nuclei + delete 1,890 .gitkeep + 600 scaffold |
| 6 | 03041ca | Wave 0: delete 38 CODEXA files, rename 149 examples, satellite to director |

---

## ARCHITECTURE (5 layers)

```
L4 ROOT        CLAUDE.md, README, INDEX, LLM_PIPELINE, CEX_ARCHITECTURE_MAP
L0 DNA         archetypes/builders/  (70 dirs x 13 files = 932 bld_*.md)
L1 SCHEMA      P01-P12/             (templates + examples + compiled + _schema.yaml)
L2 INSTANCES   N01-N07/             (7 nuclei x 12 subdirs = fractal departments)
L3 ENGINE      _tools/              (9 scripts -- pipeline engine NOT YET built)
```

### 12 Pillars with Builder Mapping

| Pillar | Builders |
|--------|----------|
| P01_knowledge | knowledge-card, rag-source, glossary-entry, context-doc, embedding-config |
| P02_model | agent, iso-package, lens, mental-model, model-card, router, boot-config, fallback-chain |
| P03_prompt | prompt-template, system-prompt, chain, instruction, action-prompt, few-shot-example |
| P04_tools | skill, scraper, mcp-server, plugin, hook, cli-tool, client, connector, daemon |
| P05_output | response-format, formatter, naming-rule, parser |
| P06_schema | validation-schema, input-schema, interface, type-def, validator |
| P07_evals | quality-gate, scoring-rubric, golden-test, smoke-eval, unit-eval, e2e-eval, benchmark |
| P08_architecture | component-map, diagram, law, pattern, director |
| P09_config | env-config, feature-flag, path-config, permission, runtime-rule, runtime-state, spawn-config |
| P10_memory | learning-record, session-state, axiom, brain-index |
| P11_feedback | guardrail, lifecycle-rule, optimizer, bugloop |
| P12_orchestration | dispatch-rule, handoff, signal, workflow, dag |

### 7 Nuclei (Fractal Departments)

| Nucleus | Department | Instances |
|---------|-----------|-----------|
| N01_intelligence | Intelligence/Orchestration | 5 |
| N02_marketing | Marketing/Growth | 4 |
| N03_engineering | Engineering/Build | 2 |
| N04_knowledge | Knowledge/Documentation | 1 |
| N05_operations | Operations/Deploy | 1 |
| N06_commercial | Commercial/Sales | 1 |
| N07_admin | Admin/Finance | 1 |

Each has 12 subdirs mirroring 12 pillars.

### Agent Maturity (replaces satellite concept)

| Level | CEX Term | CODEXA Equiv | Functions |
|-------|----------|-------------|-----------|
| L1 | Task Agent | simple agent | 2-3/8 |
| L2 | Domain Agent | specialized | 5-6/8 |
| L3 | Director | satellite | 8/8 + spawns |
| L4 | Orchestrator | STELLA | meta |

---

## NEXT WAVES

### Wave 1: GOVERNANCE (~1h)
- Pre-commit hook (7 checks)
- cex_doctor.py v2 (naming v2.0 + density)
- validate_builder.py (bld_* naming)
- Multi-LLM entry points (.cursorrules, copilot-instructions)
- Tag: v6.0.0-governance

### Wave 2: ENGINE (~1.5h)
- SQLite index (.cex/index.db)
- Pipeline engine (cex_pipeline.py): CAPTURE, DECOMPOSE, HYDRATE, COMPILE, ENVELOPE
- Feedback loop (cex_feedback.py)
- Tag: v7.0.0-engine

### Wave 3: PRODUCT (~2h)
- cex init CLI (5 questions, functional repo day 1)
- Multi-LLM onboarding
- Tag: v8.0.0-product

### Wave 4: LAUNCH (~2h)
- Landing page, pip install, demo
- Tag: v1.0.0-public

### Deferred
- Content universalization (~567 files: satellite in content, CODEXA names)
- Recompile 159 compiled/ yamls
- Relocate 157 packages/ files to nuclei
- C08 redo: OUTPUT_TEMPLATE.md (69/70 builders)

---

## KEY FILES TO READ ON RESUME

| File | Purpose |
|------|---------|
| _docs/WHITEPAPER_CEX.md | Complete thesis (20KB) |
| archetypes/CODEX.md | Governance rules |
| _docs/NAMING_CONVENTION.md | Naming v2.0 spec |
| _docs/ARCHITECTURE.md | Repo structure |
| CLAUDE.md | LLM entry point |
| CEX_ARCHITECTURE_MAP.md | Obsidian home |
| .obsidian/graph.json | 12 pillar colors |
| _tools/cex_doctor.py | v1 (needs v2) |
| _tools/validate_builder.py | Needs bld_* update |

---

## OBSIDIAN GRAPH (12 colors)

| Color | Hex | Pillar |
|-------|-----|--------|
| Red | #F44336 | P01_knowledge |
| Orange | #FF9800 | P02_model |
| Yellow | #FFEB3B | P03_prompt |
| Green | #4CAF50 | P04_tools |
| Teal | #009688 | P05_output |
| Light Blue | #03A9F4 | P06_schema |
| Indigo | #3F51B5 | P07_evals |
| Purple | #9C27B0 | P08_architecture |
| Brown | #795548 | P09_config |
| Pink | #E91E63 | P10_memory |
| Light Green | #8BC34A | P11_feedback |
| Blue Grey | #607D8B | P12_orchestration |

---

## NAMING GRAMMAR

```
bld_{kind}_{builder_topic}.md    L0 builders
tpl_{kind}.md                    L1 templates
ex_{kind}_{topic}.md             L1 examples
{kind}_{topic}.yaml              L1 compiled
{kind}_{topic}.md                L2 nucleus instances
```

Max 50 chars. snake_case. ASCII. id == stem.

---

## 8 LLM FUNCTIONS

| # | Function | Question | SQL |
|---|----------|----------|-----|
| 1 | BECOME | Who am I? | CREATE TABLE |
| 2 | INJECT | What do I know? | INSERT |
| 3 | REASON | How do I think? | WHERE |
| 4 | CALL | What tools? | Stored Proc |
| 5 | PRODUCE | What output? | SELECT |
| 6 | CONSTRAIN | What rules? | CHECK+FK |
| 7 | GOVERN | Good enough? | EXPLAIN |
| 8 | COLLABORATE | Who next? | JOIN+FEDERATE |

---

## SPAWN (for Edison batches from codexa-core)

```
# Solo
powershell -NoProfile -ExecutionPolicy Bypass -File records/core/powershell/spawn_solo.ps1 -sat edison -task "TASK" -interactive

# Grid
powershell -NoProfile -ExecutionPolicy Bypass -File records/core/powershell/spawn_grid.ps1 -mission NAME -interactive

# Monitor / Stop
powershell -NoProfile -ExecutionPolicy Bypass -File records/core/powershell/spawn_monitor.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File records/core/powershell/spawn_stop.ps1
```

---

*Checkpoint 2026-03-26T20:50 | Resume: read this, then Wave 1*
