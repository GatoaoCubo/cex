---
quality: 8.7
id: spec_opensource_release_v2
kind: constraint_spec
pillar: P06
title: "Spec -- CEX Open-Source Release v2.0 (Final CRUD + Clean + Vocabulary + Skill Catalog)"
version: 2.0.0
created: "2026-04-20"
author: n07_orchestrator
domain: release_engineering
quality_target: 9.0
status: SPEC
scope: full_repo
supersedes: spec_opensource_release_v1
depends_on:
  - spec_iso_12p_refactor
  - spec_hermes_assimilation
  - spec_opensource_release_v1
tags: [spec, release, open-source, audit, vocabulary, skills, CRUD]
tldr: "v1 waves done; v2 = remaining CRUD (176 tracked compiled, 14 brand refs, 16 FAIL builders) + vocabulary dictionary + skill catalog + settings health"
density_score: 0.95
updated: "2026-04-22"
---

# CEX Open-Source Release v2.0 — Final CRUD + Clean + Vocabulary + Skill Catalog

## Context

v1 spec (`spec_opensource_release_v1.md`) shipped 7 waves (W1-W7) between Apr 14-19.
All major deliverables landed: audit fixes, repo hygiene, EN translation, SDK docs,
examples, CI hardening, CHANGELOG. This v2 spec covers the **remaining delta** found
during the 2026-04-20 consolidation audit, plus two new deliverables: a structured
**vocabulary dictionary** and a **skill/command catalog** for humans and LLMs.

## Current State (2026-04-20 audit)

| Metric | Value | Target |
|--------|-------|--------|
| Release gate | 25/28 PASS | 28/28 |
| Doctor | 0 PASS / 278 WARN / 16 FAIL | 0 FAIL |
| ASCII compliance | 334/334 clean | 334/334 |
| PT-BR in core code | 0 | 0 |
| Tracked secrets | 0 | 0 |
| Brand refs in tracked files | 14 files | 0 |
| Tracked compiled/generated files | ~176 | 0 |
| PT-BR in docs | 5 spec files | 0 |

---

## Part A: Remaining CRUD (from v1 delta)

### A1. Security & Brand Scrub (P0)

14 tracked files contain brand references (`gatoaocubo3`, `@gatoaocubo3`, `financeiro@`):

| File | Brand ref | Action |
|------|-----------|--------|
| `.cex/archive/examples/ex_social_publisher_pet_shop.md` | @gatoaocubo3 handle | Replace with `@your-brand` placeholder |
| `N02_marketing/P05_output/interactive_demo_cex_builder.md` | github.com/gatoaocubo3/cex | Replace with generic repo URL |
| `N02_marketing/P05_output/product_tour_cex.md` | github.com/gatoaocubo3/cex | Replace with generic repo URL |
| `N02_marketing/P05_output/webinar_script_cex_intro.md` | github.com/gatoaocubo3/cex | Replace with generic repo URL |
| `N02_marketing/compiled/*.yaml` (3 files) | compiled from above | Auto-regenerate after fixing source |
| `N00_genesis/P04_tools/kind_social_publisher/kind_manifest_n00.md` | Audit | Check if brand-specific |
| `N05_operations/P07_evals/conformity_assessment_cex_quality.md` | Audit | Check if brand-specific |
| `N05_operations/compiled/conformity_assessment_cex_quality.yaml` | compiled | Auto-regenerate |
| `_reports/compiled/SELF_AUDIT_FINAL.yaml` | meta-reference | OK (audit report mentions checking for brand leaks) |
| `_reports/compiled/SYNTHESIS.yaml` | meta-reference | OK |
| `_reports/distillation/MISSION_COMPLETE.md` | meta-reference | OK (verification table) |
| `_tools/audit_security_brand.py` | tool name | OK (this IS the brand audit tool) |

**Net action**: Fix 4 source .md files, recompile 4 yamls. 6 files are meta-OK.

### A2. Untrack Compiled/Generated Files (P1)

| Directory | Tracked files | Action |
|-----------|--------------|--------|
| `_output/` | 67 | `git rm --cached -r _output/` + .gitignore |
| `_docs/compiled/` | 44 | `git rm --cached -r _docs/compiled/` + .gitignore |
| `.claude/compiled/` | 55 | `git rm --cached -r .claude/compiled/` + .gitignore |
| `_reports/compiled/` | 10 | `git rm --cached -r _reports/compiled/` + .gitignore |
| **Total** | **176** | |

Add to `.gitignore`:
```gitignore
# Compiled/generated (regenerate with cex_compile.py)
_output/
_docs/compiled/
.claude/compiled/
_reports/compiled/
```

### A3. Fix 16 Failing Builders (P0)

All 16 have 12 ISOs each. Doctor FAIL likely means missing sub-agent or KC wiring.

```
action-paradigm, collaboration-pattern, consolidation-policy, dataset-card,
edit-format, hibernation-policy, memory-architecture, press-release,
procedural-memory, quantization-config, realtime-session, repo-map,
terminal-backend, thinking-config, transport-config, voice-pipeline
```

**Dispatch**: N03 batch — diagnose + fix all 16 in one session.

### A4. PT-BR in Docs (P1)

| File | Action |
|------|--------|
| `_docs/specs/spec_n02_visual_frontend_engineer.md` | Translate to EN |
| `_docs/specs/spec_n05_railway_superintendent.md` | Translate to EN |
| `_docs/specs/spec_n06_brand_verticalization.md` | Translate to EN |
| `_docs/specs/spec_seed_words.md` | Translate to EN |
| `_docs/archive/PLAN_N03.md` | Untrack (internal, already gitignored?) |

### A5. Stale File Cleanup (P1)

| File | Action |
|------|--------|
| `.aiderignore` | `git rm` (aider no longer used) |
| `.cex/runtime/handoffs/n07_task.md` | Already deleted in git status |
| `.claude/scheduled_tasks.lock` | Modified — verify not tracked with secrets |

---

## Part B: Settings Health Report

### B1. Global Settings (`~/.claude/settings.json`)

```yaml
status: HEALTHY
mode: bypassPermissions
auto_updates: latest
issues: none
```

### B2. Project Settings (`.claude/settings.json`)

```yaml
status: HEALTHY
hooks:
  PostToolUse: Write + Edit -> cex_hooks_native.py (compile on save)
  PostCompact: memory decay
  SessionStart: preflight
  Stop: signal emission
permissions: Bash(*), Read(*), Write(*), Edit(*), Glob(*), Grep(*), Agent(*)
issues: none
```

### B3. Local Settings (`.claude/settings.local.json`)

```yaml
status: HEALTHY
mode: bypassPermissions
extra_permissions: WebFetch, WebSearch, NotebookEdit, mcp__*
issues: none
```

### B4. MCP Config (`.mcp.json`) — FIXED

| Server | Status | Notes |
|--------|--------|-------|
| github | OK | GITHUB_TOKEN from env |
| fetch | OK | uvx mcp-server-fetch |
| firecrawl | OK | FIRECRAWL_API_KEY from env |
| markitdown | OK | npx markitdown-mcp-npx |
| ~~brave-search~~ | **REMOVED** | Missing API key, unused |
| notebooklm | OK | npx notebooklm-mcp |
| postgres | OK | npx server-postgres |
| canva | WARN | Needs CANVA_CLIENT_ID + SECRET |
| playwright | OK | Disabled by default, needs chrome_cdp.ps1 |

**Action taken**: brave-search removed from `.mcp.json`, `.mcp-n07.json`, `.mcp-n01.json`.

### B5. Per-Nucleus Settings

| Nucleus | File | Mode | MCP Overlay | Issues |
|---------|------|------|-------------|--------|
| N01 | `n01.json` | bypassPermissions | `.mcp-n01.json`: fetch, firecrawl, markitdown, notebooklm | ~~brave-search~~ REMOVED |
| N02 | `n02.json` | bypassPermissions | `.mcp-n02.json`: markitdown, puppeteer, canva | canva needs keys |
| N03 | `n03.json` | bypassPermissions | `.mcp-n03.json`: github, fetch, canva | canva needs keys |
| N04 | `n04.json` | bypassPermissions | `.mcp-n04.json`: supabase, postgres, fetch, firecrawl | supabase needs token |
| N05 | `n05.json` | bypassPermissions | `.mcp-n05.json`: postgres, github | OK |
| N06 | `n06.json` | bypassPermissions | `.mcp-n06.json`: fetch, markitdown, stripe | stripe needs key |
| N07 | `n07.json` | bypassPermissions | `.mcp-n07.json`: github, fetch, markitdown, firecrawl(disabled) | ~~brave~~ REMOVED. GitHub read-only enforced. |
| _template | `_template.json` | scoped | — | Template for N08+ (not active) |

**Recommendation for open source**: MCP servers that need API keys should be `"disabled": true` by default
with a `_setup` comment. Currently only firecrawl and playwright follow this pattern. canva, stripe,
and supabase should match.

---

## Part C: Vocabulary Dictionary (Dev vs AI/LLM)

### Purpose

Users and LLMs reading CEX need a Rosetta Stone: what does each CEX term mean in
traditional dev language, and what does it mean in AI/LLM language? This dictionary
bridges the gap so a Rails dev and a prompt engineer both understand CEX.

### Format

Structured YAML frontmatter artifact at `docs/vocabulary.md`:

```yaml
---
id: vocabulary_cex_rosetta
kind: domain_vocabulary
pillar: P01
title: "CEX Vocabulary — Dev vs AI/LLM Rosetta Stone"
version: 1.0.0
quality: 8.2
tags: [vocabulary, glossary, rosetta, open-source]
entry_count: 80+
---
```

### Dictionary Structure (per entry)

```yaml
entries:
  - term: "kind"
    cex_definition: "Atomic artifact type from the 293-kind taxonomy"
    dev_equivalent: "class / schema / resource type"
    ai_equivalent: "prompt template category / tool type"
    example: "knowledge_card, agent, workflow, landing_page"
    pillar: "cross-cutting"
    see_also: ["builder", "ISO", "pillar"]
```

### Core Vocabulary (80+ entries organized by domain)

#### Architecture Terms

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| kind | class / schema / resource type | prompt template category | Atomic artifact type (293 registered) |
| pillar | module / package / domain | capability group | One of 12 domain groupings (P01-P12) |
| nucleus | microservice / team | agent / role | Autonomous operational unit (N01-N07) |
| ISO | interface / trait / mixin | instruction layer | Builder instruction per pillar (12 per kind) |
| builder | factory / generator | prompt chain | Kind-specific production pipeline (298 registered) |
| archetype | base class / template | meta-prompt | N00 Genesis pattern that nuclei inherit |
| fractal | convention over configuration | recursive pattern | Self-similar structure across all nuclei |
| artifact | resource / entity / record | output / generation | Any file produced by 8F pipeline |

#### Pipeline Terms (8F)

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| 8F pipeline | CI/CD pipeline | prompt chain | 8-function reasoning protocol (F1-F8) |
| F1 CONSTRAIN | schema validation / type check | intent resolution | Resolve kind, pillar, schema from input |
| F2 BECOME | dependency injection / factory | persona loading | Load builder identity + 12 ISOs |
| F3 INJECT | context assembly / data fetch | RAG / context stuffing | Assemble knowledge sources into context |
| F4 REASON | algorithm design / planning | chain-of-thought | Plan approach, sections, references |
| F5 CALL | tool invocation / API call | tool use / function calling | Execute tools for enrichment |
| F6 PRODUCE | render / generate / build | inference / generation | Generate the artifact |
| F7 GOVERN | test / validate / lint | eval / judge | Quality gate with scoring rubric |
| F8 COLLABORATE | deploy / publish / push | save + signal | Save, compile, commit, signal |

#### Orchestration Terms

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| dispatch | deploy / schedule / enqueue | agent spawn | Send task to a nucleus |
| grid | parallel deployment / fan-out | multi-agent swarm | N nuclei running in parallel |
| crew | team / squad / pipeline | multi-agent workflow | N roles with handoffs producing 1 deliverable |
| handoff | message / event / payload | context transfer | Task file passed from N07 to nucleus |
| signal | webhook / event / callback | completion notification | Nucleus reports done + quality score |
| wave | deployment phase / batch | orchestration round | Group of dispatches that run together |
| consolidate | collect / aggregate / merge | result synthesis | Verify + stop + commit after wave |
| GDP | feature flag / A/B decision | human-in-the-loop | Guided Decision Protocol (user decides WHAT) |
| mission | project / epic / initiative | goal decomposition | Full lifecycle: plan + guide + spec + grid |

#### Knowledge Terms

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| KC (knowledge_card) | doc / wiki page / record | knowledge chunk | Structured knowledge unit |
| embedding_config | search index config | vector store setup | How to embed and index artifacts |
| retriever | search engine / query service | RAG retriever | Find similar artifacts by content |
| memory | cache / session store / state | context memory | Persistent state across sessions |
| entity_memory | ORM entity / record | named entity store | Remember specific entities |
| context_window | buffer / viewport | token budget | How much context fits in one call |

#### Quality Terms

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| quality gate | CI gate / test suite | eval pass/fail | Must score >= 8.0 to publish |
| scoring rubric | test criteria / acceptance | judge rubric | 5D dimensions for quality scoring |
| density | LOC / information ratio | token efficiency | Information per byte (target >= 0.85) |
| doctor | health check / diagnostics | system audit | Builder health verification tool |
| flywheel | feedback loop / CI/CD cycle | self-improvement | Automated quality improvement cycle |

#### Sin Lens Terms

| CEX Term | Sin | Dev Equivalent | AI/LLM Equivalent |
|----------|-----|---------------|-------------------|
| Analytical Envy | N01 | competitive analysis mindset | research optimization bias |
| Creative Lust | N02 | design-driven development | creative generation priority |
| Inventive Pride | N03 | engineering excellence | build quality maximization |
| Knowledge Gluttony | N04 | documentation-first culture | knowledge accumulation bias |
| Gating Wrath | N05 | strict QA / zero-tolerance | validation strictness |
| Strategic Greed | N06 | revenue optimization | monetization focus |
| Orchestrating Sloth | N07 | delegation / management | efficient dispatch (never build directly) |

#### Tool/Integration Terms

| CEX Term | Dev Equivalent | AI/LLM Equivalent | Definition |
|----------|---------------|-------------------|------------|
| MCP server | API integration / plugin | tool provider | Model Context Protocol external tool |
| preflight | pre-deployment check | context pre-fetch | Gather external context before dispatch |
| boot script | startup script / entrypoint | agent initialization | PS1 that launches a nucleus |
| compile | build / transpile | yaml serialization | .md to .yaml conversion |
| sanitize | lint / format | ASCII enforcement | Ensure code is ASCII-only |

---

## Part D: Skill & Command Catalog

### Purpose

A single reference for humans and LLMs listing every skill and command with:
when to use, what it does, prerequisites, and recommendations.

### Format

Structured artifact at `docs/skill-catalog.md`:

```yaml
---
id: skill_catalog_cex
kind: knowledge_card
pillar: P01
title: "CEX Skill & Command Catalog"
version: 1.0.0
quality: null
tags: [skills, commands, catalog, reference, open-source]
skill_count: 11
command_count: 20
---
```

### Skills (auto-fire and user-invoked)

| Skill | Type | Trigger | What it does | When to use | Prerequisites |
|-------|------|---------|-------------|-------------|---------------|
| `auto-accept-handoff` | auto-fire | Grid/overnight dispatch | Sets auto_accept on handoffs so nuclei use recommended defaults instead of re-prompting | When dispatching autonomous missions where user won't be present | Decision manifest locked via GDP |
| `btw` | user-invoked | `/btw` or "btw..." | Captures ad-hoc observation into memory/KC without breaking flow | When user drops context mid-work that should persist | None |
| `commit` | user-invoked | `/commit` or "commit" | Stages changes, writes conventional commit grouped by nucleus, runs pre-commit hooks | When ready to save changes to git | Changes exist in working tree |
| `cross-wave-cleanup` | auto-fire | Between waves | Kills wrapper PID trees and orphan processes between dispatch waves | After any multi-spawn wave completes | Active PID tracking in `.cex/runtime/pids/` |
| `dream` | user-invoked | `/dream` or "brainstorm" | Generates 3-5 divergent approaches before committing to one | When problem is ill-specified or has multiple valid architectures | None |
| `new-nucleus-bootstrap` | auto-fire | Creating N08+ | Scaffolds rule, agent card, prompt, 4 boot scripts, scoped permissions for new nucleus | When extending CEX to N08 or higher | N07 orchestrator session |
| `shared-file-proposal` | auto-fire | Concurrent nuclei | Uses .proposal file instead of direct edits for shared files during grid | When concurrent nuclei need to change CLAUDE.md, kinds_meta.json, etc. | Grid or multi-nucleus dispatch active |
| `simplify` | user-invoked | `/simplify` | Reviews changed code for reuse, quality, efficiency; fixes issues found | After implementing a feature, before commit | Changes exist |
| `verify` | user-invoked | `/verify` | Validates artifacts against quality gates and schema | After building or modifying artifacts | Artifact exists |
| `mentor` | user-invoked | `/mentor` | Teaches CEX through storytelling, analogies, quizzes, and media production | When learning CEX concepts or producing educational content | None |

### Commands (slash commands)

| Command | Usage | What it does | When to use | Nucleus | Recommendations |
|---------|-------|-------------|-------------|---------|-----------------|
| `/init` | `/init [folder_path]` | First-time brand setup (~2 min, 6 questions) | First time using CEX | N07 | Run once. Populates `.cex/brand/brand_config.yaml` |
| `/plan <goal>` | `/plan build CRM` | Decomposes goal into tasks, identifies nuclei, maps dependencies | Starting a new project or feature | N07 | Always run before `/mission`. Produces plan file |
| `/guide [topic]` | `/guide pricing` | Co-pilot mode: asks before building, guided decisions | When subjective choices matter (tone, audience, style) | N07 | Triggers GDP. Produces decision manifest |
| `/spec [plan]` | `/spec plan_crm` | Creates detailed spec from plan + decisions | After `/plan` + `/guide` | N07 | Requires plan file. Produces spec with wave assignments |
| `/grid [spec]` | `/grid BRAND_LAUNCH` | Dispatches nuclei autonomously from spec | After spec is ready | N07 | Writes handoffs, spawns processes. Monitor with `/status` |
| `/build <intent>` | `/build agent for sales` | Builds single artifact via 8F pipeline | When you need exactly 1 artifact | N03 (routed) | Intent is transmuted to {kind, pillar, nucleus} |
| `/validate [file\|all]` | `/validate all` | Checks artifact quality against gates | After building, before publishing | N05 | Reports quality score, gates pass/fail |
| `/dispatch <nuc> <task>` | `/dispatch n03 fix tests` | Sends task to specific nucleus | When you know exactly which nucleus | target | Manual routing, bypasses intent resolution |
| `/mission <goal>` | `/mission launch product` | Full lifecycle: plan+guide+spec+grid+consolidate | Ambitious multi-artifact goals | N07 | The "do everything" command. Budget: 30min+ |
| `/status` | `/status` | System health dashboard | Anytime | N07 | Shows processes, signals, quality metrics |
| `/doctor` | `/doctor` | Full diagnostics (CEX-specific, not Claude Code native) | When something seems broken | N07 | Tiered: fast \| full \| audit <name> |
| `/consolidate` | `/consolidate` | Post-dispatch: verify + stop processes + commit | After nuclei complete | N07 | Frees GPU VRAM (ollama unload), archives signals |
| `/evolve [file\|all]` | `/evolve all` | Autonomous artifact improvement loop | When quality < 9.0 across artifacts | N07 | Heuristic pass first (free), then agent mode |
| `/mentor [topic]` | `/mentor 8F` | Teach CEX via storytelling, analogies, quizzes | Learning CEX methodology | N04 | 4 lenses: storytelling, analogy, quiz, media |
| `/batch <file>` | `/batch intents.txt` | Run many tasks in parallel worktrees | Bulk artifact production | N07 | One intent per line. --workers N for parallelism |
| `/simplify [path]` | `/simplify _tools/` | Review and fix code quality | Code cleanup | N05 | Also available as skill |
| `/loop [interval] <cmd>` | `/loop 5m /status` | Recurring command execution | Monitoring, polling | N07 | Omit interval for self-paced |
| `/schedule <cron> <cmd>` | `/schedule "0 */6 * * *" /evolve` | Create scheduled remote agent | Recurring automated tasks | N07 | Requires cron expression |
| `/showoff` | `/showoff` | 4-runtime validation (Claude+Codex+Gemini+Ollama) | Proving multi-runtime works | N07 | 5 waves. Use --skip to skip runtimes |
| `/spec [plan]` | `/spec plan_name` | Create detailed spec from plan | After planning | N07 | Produces wave-by-wave artifact list |

### Workflow Recommendations

| Goal | Recommended Flow | Time |
|------|-----------------|------|
| Build 1 artifact | `/build <intent>` | 2-5 min |
| Build with guidance | `/guide` then `/build` | 5-10 min |
| Multi-artifact project | `/plan` -> `/guide` -> `/spec` -> `/grid` -> `/consolidate` | 30-60 min |
| Full autopilot | `/mission <goal>` | 30-60 min |
| Improve existing | `/evolve [target]` | 10-30 min |
| Learn CEX | `/mentor [topic]` | 5-15 min |
| Diagnose issues | `/doctor` then `/status` | 2-5 min |

---

## Part E: Execution Plan

### Wave 1 — N07 Direct: Settings + Scrub + Untrack (this session)

| # | Action | Est. |
|---|--------|------|
| 1.1 | Remove brave-search from .mcp.json, .mcp-n07.json, .mcp-n01.json | **DONE** |
| 1.2 | Scrub 4 brand-ref source files (replace gatoaocubo3 URLs with generic) | 5 min |
| 1.3 | git rm --cached: _output/, _docs/compiled/, .claude/compiled/, _reports/compiled/ (176 files) | 5 min |
| 1.4 | Update .gitignore with compiled/generated exclusions | 2 min |
| 1.5 | git rm .aiderignore | 1 min |
| 1.6 | Disable canva/stripe/supabase MCP servers by default (add disabled: true) | 5 min |

### Wave 2 — N03 Dispatch: Fix 16 FAIL Builders

Batch handoff to diagnose and fix all 16 failing builders.

### Wave 3 — N04 Dispatch: Vocabulary + Skill Catalog + PT-BR Translation

| # | Action |
|---|--------|
| 3.1 | Create `docs/vocabulary.md` — structured vocabulary dictionary (Part C above) |
| 3.2 | Create `docs/skill-catalog.md` — full skill + command catalog (Part D above) |
| 3.3 | Translate 4 remaining PT-BR spec files to EN |
| 3.4 | Recompile all translated sources |

### Wave 4 — N07 Direct: Final Validation + Fork

| # | Action |
|---|--------|
| 4.1 | Run cex_release_check.py — target 28/28 PASS |
| 4.2 | Run cex_doctor.py — target 0 FAIL |
| 4.3 | Run cex_sanitize.py --check — target 0 dirty |
| 4.4 | Verify 0 brand refs: `grep -rn "gatoaocubo" $(git ls-files)` |
| 4.5 | Create branch: release/v1.0.0-stable |
| 4.6 | Tag: v1.0.0-stable |

### Dependency Graph

```
W1 (settings + scrub + untrack) ── DONE in this session
  |
  +── W2 (fix 16 builders)      ── N03 dispatch
  |
  +── W3 (vocab + catalog + EN) ── N04 dispatch (parallel with W2)
  |
  v
W4 (final validation + fork)    ── after W2 + W3 complete
```

---

## Acceptance Criteria

- [ ] `cex_release_check.py` = 28/28 PASS
- [ ] `cex_doctor.py` = 0 FAIL
- [ ] `cex_sanitize.py --check` = 0 dirty
- [ ] `grep -rn "gatoaocubo" $(git ls-files)` = 0 in code/config files (OK in meta-audit reports)
- [ ] `git ls-files _output/ _docs/compiled/ .claude/compiled/ _reports/compiled/` = 0
- [ ] `docs/vocabulary.md` exists with 80+ structured entries
- [ ] `docs/skill-catalog.md` exists with 11 skills + 20 commands
- [ ] All MCP servers with missing API keys have `"disabled": true`
- [ ] No brave-search in any MCP config
- [ ] All user-facing docs in EN
- [ ] MIT license present
- [ ] v1.0.0-stable tag applied
