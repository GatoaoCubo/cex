# CEX — Typed Knowledge System for LLM Agents

> 123 kinds · 125 builders · 12 pillars · 8 nuclei (N00-N07) · 8F pipeline · cex_sdk runtime · 59 tools

## Brand Identity

> **✅ Bootstrapped: GATO³** — Curadoria de bem-estar felino + casa harmonizada

| Field | Value |
|-------|-------|
| **Brand** | GATO³ (Gato ao Cubo) |
| **Tagline** | Educação que acalma, soluções que funcionam, casa que continua elegante. |
| **Archetype** | Caregiver (Cuidadora + Sábia + Criadora) |
| **Voice** | Sofisticado-acolhedor, informativo, minimalista |
| **Visual** | PB minimalista (Allrounder + Kenao) |
| **ICP** | Tutores de gatos 25-45, urbanos, classe B-C+ |
| **Model** | Hybrid (B2C direto + B2B revenda + marketplaces) |
| **Persona** | Ro — guia acolhedora com protocolos práticos |
| **Site** | gato3.com.br |

Every nucleus reads `.cex/brand/brand_config.yaml` and auto-injects brand context into prompts.

| How | For whom |
|-----|----------|
| `/init` | User types this in chat — LLM asks ~6 questions conversationally |
| `init.cmd` | User double-clicks file in root — interactive CLI |
| `boot/cex.cmd` | Auto-detects on first run, offers 3 choices |
| `boot/n06.cmd` | Full 15-question Brand Discovery + 32-block Brand Book |

## Who Am I?

Check `CEX_NUCLEUS`. N07 = Orchestrator. N03 = Builder. Not set = read and decide.

## Pointers

| What | Where |
|------|-------|
| **8F pipeline** | `.claude/rules/8f-reasoning.md` |
| **Orchestrator rules** | `.claude/rules/n07-orchestrator.md` |
| **Nucleus rules** | `.claude/rules/n{01-06}-*.md` (1 per nucleus) |
| **Commands** | `.claude/commands/` → /build, /validate, /dispatch, /status, /doctor, /mission |
| **Builders (source of truth)** | `archetypes/builders/{kind}-builder/` (13 ISOs each) |
| **Sub-agents** | `.claude/agents/{kind}-builder.md` (125 files) |
| **N00 Genesis (archetype)** | `N00_genesis/` + `P{01-12}_*/` + `archetypes/` |
| **Pillar schemas** | `P{01-12}_*/_schema.yaml` (all descriptions in EN) |
| **Kind KCs** | `P01_knowledge/library/kind/kc_{kind}.md` (123 files) |
| **Kind registry** | `.cex/kinds_meta.json` (123 kinds) |
| **Terminology** | `_docs/specs/spec_metaphor_dictionary.md` + Rosetta Stone KC |
| **N07 tech authority** | `.claude/rules/n07-technical-authority.md` |
| **Infinite loop spec** | `_docs/specs/spec_infinite_bootstrap_loop.md` |
| **Subagent definitions** | `.claude/agents/` (125 builder sub-agents) |
| **Nucleus fractals** | `N{01-07}_*/` (13 subdirs each, mirrors N00's 12 pillars) |
| **SDK runtime** | `cex_sdk/` (78 .py, 4504 lines) |
| **Boot scripts** | `boot/cex.cmd` (N07) · `boot/n0{1-6}.cmd` |
| **Decision manifest** | `.cex/runtime/decisions/decision_manifest.yaml` |
| **GDP skill** | `archetypes/builders/_shared/skill_guided_decisions.md` |
| **Runtime** | `.cex/runtime/{handoffs,signals,pids,decisions}/` |
| **Experiment history** | `.cex/experiments/results.tsv` |
| **Learning records** | `.cex/learning_records/` |
| **Session state** | `.cex/runtime/` (handoffs, signals, archive) |

## 4 Rules

1. **8F is mandatory.** Every artifact passes F1→F8. No exceptions.
2. **GDP before dispatch.** Subjective decisions → ask user first → write manifest → THEN execute autonomously.
3. **N07 never builds.** Dispatch via `bash _spawn/dispatch.sh`. Always.
4. **quality: null.** Never self-score. Peer-review assigns quality.

> **GDP (Guided Decision Protocol)**: User decides WHAT (tone, audience, style). LLM decides HOW (files, pipeline, structure).
> See `.claude/rules/guided-decisions.md` and `archetypes/builders/_shared/skill_guided_decisions.md`.

## The Workflow

```
/plan → /guide → /spec → /grid → /consolidate
  │        │        │       │         │
  │        │        │       │         └→ verify + score + clean
  │        │        │       └→ dispatch nuclei (autonomous)
  │        │        └→ spec blueprint (exact artifacts)
  │        └→ decisions with user (co-pilot)
  └→ decompose goal into tasks
```

User decides WHAT → LLM builds HOW → verify together.

## Commands

| Command | Purpose |
|---------|---------|
| `/init` | **First run**: configure CEX for your brand (~2 min) |
| `/plan <goal>` | Decompose goal → tasks, nuclei, dependencies |
| `/guide [goal]` | **Co-pilot**: ask me before building — guided decisions |
| `/spec [plan]` | Create spec blueprint from plan + decisions |
| `/grid [spec]` | Execute spec — autonomous dispatch to nuclei |
| `/build <intent>` | Build single artifact via 8F pipeline |
| `/validate [file\|all]` | Check artifact quality |
| `/dispatch <nucleus> <task>` | Send task to single nucleus |
| `/mission <goal>` | **Shortcut**: plan+guide+spec+grid+consolidate in one |
| `/status` | System health dashboard |
| `/doctor` | Full diagnostics |
| `/consolidate` | Post-dispatch: verify + score + clean |
| `/evolve [file\|all]` | **AutoResearch**: autonomous artifact improvement loop |

## Tools (run with `--help`)

| Tool | Purpose |
|------|---------|
| `cex_run.py` | **Unified entry**: intent → discover → plan → compose prompt |
| `cex_8f_motor.py` | Intent parser + classifier + fan-out + plan (1385L) |
| `cex_8f_runner.py` | Full 8F pipeline (--execute, --nucleus, --kind) |
| `cex_crew_runner.py` | Prompt composer: ISOs + memory + context → LLM prompt (839L) |
| `cex_query.py` | TF-IDF builder discovery (361L) |
| `cex_auto.py` | Self-healing flywheel (scan, plan, cycle) |
| `cex_mission.py` | Goal → decomposed artifacts |
| `cex_mission_runner.py` | **Autonomous orchestration**: waves → grid → poll → stop → gate → consolidate |
| `cex_signal_watch.py` | **Blocking signal poll**: waits for nuclei completion, detects crashes |
| `cex_batch.py` | Multi-intent processing from file |
| `cex_compile.py` | .md → .yaml compilation (--all) |
| `cex_doctor.py` | Builder health check (118 PASS) |
| `cex_hooks.py` | Pre/post validation + git hook |
| `cex_score.py` | Peer review scoring (--apply) |
| `cex_feedback.py` | Quality tracking + archive + metrics |
| `cex_quality_monitor.py` | Quality snapshots + regression detection |
| `cex_prompt_optimizer.py` | Builder ISO analysis + improvement suggestions |
| `cex_retriever.py` | TF-IDF artifact similarity (2184 docs, 12K vocab) |
| `cex_token_budget.py` | Token counting + budget allocation |
| `cex_memory_select.py` | Relevant memory injection (keyword + LLM) |
| `cex_memory_update.py` | Memory decay + append + prune |
| `cex_schema_hydrate.py` | Hydrate ISOs with universal patterns |
| `cex_materialize.py` | Builder ISOs → sub-agents |
| `cex_system_test.py` | Full system validation (54 tests) |
| `signal_writer.py` | Inter-nucleus signals |
| `cex_bootstrap.py` | **First-run**: brand setup → propagate → audit |
| `brand_inject.py` | Replace `{{BRAND_*}}` in templates |
| `brand_validate.py` | Validate brand_config.yaml (13 req fields) |
| `brand_propagate.py` | Push brand context to all nuclei |
| `brand_audit.py` | Score brand consistency (6 dimensions) |
| `brand_ingest.py` | Scan user's messy folder → extract brand signals |
| `cex_evolve.py` | **AutoResearch loop**: evolve artifacts autonomously (keep/discard) |
| `cex_model_updater.py` | **Self-heal**: discover/check/apply/propagate model version updates |
| `cex_release_check.py` | **Release gate**: validates README, deps, CI, versions for public release |
| `cex_prompt_layers.py` | Compiled artifact scanner: loads 15+ pillar artifacts into prompts |
| `cex_skill_loader.py` | Builder ISO loader: 13 ISOs per kind, shared skills, conditionals |
| `cex_router.py` | Multi-provider routing: 4 providers x 7 nuclei + fallback chains |
| `cex_gdp.py` | GDP enforcement: manifest I/O, NeedsUserDecision gate at F4 |
| `cex_memory_types.py` | 4-type memory taxonomy: correction/preference/convention/context |
| `cex_memory_age.py` | Freshness caveats, age labels, linear decay over 365d |
| `cex_agent_spawn.py` | Agent config validation + spawn pre-flight checks |
| `cex_coordinator.py` | Synthesis gates between mission waves + workflow orchestration |
| `cex_compile.py --target` | **Reverse compiler**: CEX artifacts -> claude-md, cursorrules, customgpt |
| `cex_flywheel_audit.py` | **Doc vs Practice**: 109 checks across 7 layers + 7 wires + 7 cascades |

## Quick Dispatch

```bash
bash _spawn/dispatch.sh solo n03 "task"   # 1 builder
bash _spawn/dispatch.sh grid MISSION      # up to 6 parallel
bash _spawn/dispatch.sh status            # monitor
bash _spawn/dispatch.sh stop              # stop MY session's nuclei only
bash _spawn/dispatch.sh stop n03          # stop only N03 (surgical)
bash _spawn/dispatch.sh stop --all        # stop ALL nuclei (DANGEROUS)
bash _spawn/dispatch.sh stop --dry-run    # preview what would die
```

> **Session-aware (v4.0)**: Multiple N07 orchestrators can run simultaneously.
> `stop` only kills YOUR nuclei. Use `--all` explicitly to kill everything.

## Nucleus Routing

> All nuclei upgraded to Opus 1M context (2026-04-06). Config: `.cex/config/nucleus_models.yaml`

| Domain | Nucleus | CLI | Model | Context |
|--------|---------|-----|-------|---------|
| Research/analysis | N01 | claude | opus-4-6 | 1M |
| Marketing/copy | N02 | claude | opus-4-6 | 1M |
| Build/create | N03 | claude | opus-4-6 | 1M |
| Knowledge/docs | N04 | claude | opus-4-6 | 1M |
| Code/test/deploy | N05 | claude | opus-4-6 | 1M |
| Brand/monetization | N06 | claude | opus-4-6 | 1M |
| Orchestration | N07 | claude | opus-4-6 | 1M |

## Constraints

**NEVER**: skip frontmatter · publish below 8.0 · pass task as CLI arg · overwrite without git
**ALWAYS**: load builder ISOs first · compile after save · signal on complete · boot interactive
