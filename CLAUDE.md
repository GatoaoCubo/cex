# CEX — Typed Knowledge System for LLM Agents

> 257 kinds · 260 builders · 3381 ISOs · 12 pillars · 8 nuclei (N00-N07) · 8F pipeline · cex_sdk runtime · 82 tools

## Brand Identity

> **Not yet bootstrapped.** Type `/init` or the user just needs to answer a few questions.

The X in CEX is a variable. Once bootstrapped, this section shows WHO this brain belongs to.
Every nucleus reads `.cex/brand/brand_config.yaml` and auto-injects brand context into prompts.

**If this section says "Not yet bootstrapped" — ASK THE USER before doing anything else.**
See `.claude/rules/brand-bootstrap.md` for the auto-detection protocol.

| How | For whom |
|-----|----------|
| `/init` | User types this in chat — LLM asks ~6 questions conversationally |
| `gato3` / `cex-main` | PATH shortcuts — boot N07 on the right worktree from any PS |
| `boot/cex.ps1` | Direct boot — sin-aware UX, worktree-agnostic |
| `boot/n06.ps1` | Full 15-question Brand Discovery + 32-block Brand Book |

## Who Am I?

Check `CEX_NUCLEUS`. N07 = Orchestrator. N03 = Builder. Not set = read and decide.

**Nucleus self-load (mandatory at boot):** if `CEX_NUCLEUS` is `n01..n06`, your first action is to read `N{0X}_*/rules/n{0X}-*.md` (your identity + 8F rules + routing). N07 reads `.claude/rules/n07-*.md` only — it never pre-loads other nuclei's rules to keep the orchestrator boot lean. **Intent transmutation:** for any user input, resolve to `{kind, pillar, nucleus, verb}` via `P03_prompt/layers/p03_pc_cex_universal.md` (the `prompt_compiler` artifact) BEFORE acting. This is F1 CONSTRAIN, mandatory in every 8F run.

## Pointers

| What | Where |
|------|-------|
| **8F pipeline** | `.claude/rules/8f-reasoning.md` |
| **Orchestrator rules** | `.claude/rules/n07-orchestrator.md` |
| **Nucleus rules** | `N0{1-6}_*/rules/n0{1-6}-*.md` (1 per nucleus, lazy-loaded by the nucleus on boot — N07 does not pre-load these) |
| **Commands** | `.claude/commands/` → /build, /validate, /dispatch, /status, /doctor, /mission |
| **Builders (source of truth)** | `archetypes/builders/{kind}-builder/` (13 ISOs each) |
| **Sub-agents** | `.claude/agents/{kind}-builder.md` (125 files) |
| **N00 Genesis (archetype)** | `N00_genesis/` + `P{01-12}_*/` + `archetypes/` |
| **Pillar schemas** | `P{01-12}_*/_schema.yaml` (all descriptions in EN) |
| **Kind KCs** | `P01_knowledge/library/kind/kc_{kind}.md` (131 files) |
| **Kind registry** | `.cex/kinds_meta.json` (257 kinds) |
| **Composable-crew rule** | `.claude/rules/composable-crew.md` (5 WAVE8 primitives + grid-of-crews) |
| **Lazy skills (auto-fire)** | `.claude/skills/{cross_wave_cleanup,shared_file_proposal,new_nucleus_bootstrap,auto_accept_handoff}.md` -- mirrored to `.cex/skills/` for codex/gemini/ollama |
| **Crew CLI** | `_tools/cex_crew.py` (list/show/run) |
| **Example crew** | `N02_marketing/crews/p12_ct_product_launch.md` (4-role sequential) |
| **Nucleus defs** | `N0[0-7]_*/architecture/nucleus_def_n0[0-7].md` (8 machine-readable identities) |
| **Terminology** | `_docs/specs/spec_metaphor_dictionary.md` + Rosetta Stone KC |
| **N07 tech authority** | `.claude/rules/n07-technical-authority.md` |
| **Infinite loop spec** | `_docs/specs/spec_infinite_bootstrap_loop.md` |
| **Subagent definitions** | `.claude/agents/` (259 builder sub-agents) |
| **Nucleus fractals** | `N{01-07}_*/` (13 subdirs each, mirrors N00's 12 pillars) |
| **SDK runtime** | `cex_sdk/` (78 .py, 4504 lines) |
| **Boot scripts** | `boot/cex.ps1` (N07) · `boot/n0{1-6}.ps1` (PowerShell-only) |
| **Decision manifest** | `.cex/runtime/decisions/decision_manifest.yaml` |
| **GDP skill** | `archetypes/builders/_shared/skill_guided_decisions.md` |
| **Prompt Compiler** (intent transmutation source-of-truth, 257 kinds, PT+EN) | `P03_prompt/layers/p03_pc_cex_universal.md` -- referenced by `n07-input-transmutation.md` |
| **Intent Resolver** | `_tools/cex_intent_resolver.py` (Python-first, 0 tokens) |
| **Setup Validator** | `_tools/cex_setup_validator.py` (new PC readiness check) |
| **Hygiene Tool** | `_tools/cex_hygiene.py` (artifact CRUD, 8 rules) |
| **Prompt Cache** | `_tools/cex_prompt_cache.py` + `.cex/cache/` (260 builders pre-compiled) |
| **Preflight** | `_tools/cex_preflight.py` — hybrid local/cloud context pre-compiler (Ollama + Haiku) |
| **Token Efficiency Map** | `N01_intelligence/reports/token_efficiency_gap_map.md` |
| **Taxonomy Audit** | `N01_intelligence/reports/taxonomy_completeness_audit.md` |
| **Port Plan (external repos)** | `_docs/specs/port_plan_external_repos.md` |
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
| `/crew list\|show\|run <name>` | **Composable crew (WAVE8)**: list/inspect/run multi-role teams (sequential\|hierarchical\|consensus) |

### Composable Crews (WAVE8)

Crews = 1 coherent package from N roles with handoffs. Use when solo-builder is too shallow and grid is too parallel.

```bash
python _tools/cex_crew.py list                      # discover registered crews
python _tools/cex_crew.py show product_launch       # inspect resolved plan
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md
python _tools/cex_crew.py run product_launch \
    --charter ... --execute                         # real LLM calls
```

**5 WAVE8 primitives**: `crew_template` (P12) · `role_assignment` (P02) · `capability_registry` (P08) · `nucleus_def` (P02) · `team_charter` (P12). See `.claude/rules/composable-crew.md` for authoring + **grid-of-crews** composition.

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

> Budget-optimized: 2 Opus + 5 Sonnet + preflight (2026-04-13). Config: `.cex/config/nucleus_models.yaml`

| Domain | Nucleus | CLI | Model | Context | Tier |
|--------|---------|-----|-------|---------| -----|
| Research/analysis | N01 | claude | sonnet-4-6 | 200K | Sonnet |
| Marketing/copy | N02 | claude | sonnet-4-6 | 200K | Sonnet |
| Build/create | N03 | claude | opus-4-6 | 1M | **Opus** |
| Knowledge/docs | N04 | claude | sonnet-4-6 | 200K | Sonnet |
| Code/test/deploy | N05 | claude | sonnet-4-6 | 200K | Sonnet |
| Brand/monetization | N06 | claude | sonnet-4-6 | 200K | Sonnet |
| Orchestration | N07 | claude | opus-4-6 | 1M | **Opus** |

> **Preflight**: `cex_preflight.py` pre-compiles context via local Ollama (qwen3:14b) or Haiku before nucleus boot. Reduces token burn ~70%.

## Boris-isms adopted (BORIS_MERGE, 2026-04-15)

21 items from Boris Cherny's Claude Code workflow, assimilated and multi-runtime-capable.
Each item was mapped to the existing CEX architecture; the ones that did not map
cleanly were dropped (see "Out of scope" in `plan_boris_merge.md`).

| # | Item | Where it landed | Multi-runtime? |
|---|------|-----------------|----------------|
| 1 | Native skills | `.claude/skills/{commit,simplify,btw,verify,dream}.md` + mirror `.cex/skills/` | yes (mirror) |
| 2 | Slash commands | `.claude/commands/{simplify,loop,schedule,batch,...}.md` | yes (wraps skill) |
| 3 | `isolation: worktree` | frontmatter on heavy builders (agent, workflow, system_prompt, landing_page, crew_template) | yes (dispatch `-w`) |
| 4 | `settings.json` hooks | `.claude/settings.json` + `_tools/cex_hooks_native.py` | yes (single entrypoint) |
| 5 | PostToolUse compile | `cex_hooks_native.py post-tool-use` | yes |
| 6 | PostCompact memory decay | `cex_hooks_native.py post-compact` | yes |
| 7 | SessionStart preflight | `cex_hooks_native.py session-start` | yes |
| 8 | Stop auto-signal | `cex_hooks_native.py stop` | yes |
| 9 | `.mcp.json` root | consolidated root + per-nucleus overlays still win | partial (no MCP on ollama) |
| 10 | Permissions pattern (template) | `.claude/nucleus-settings/_template.json` (new nuclei only) | n/a |
| 11 | `--bare` startup | `cex_run.py --bare` skips KC index + memory load | yes |
| 12 | `/simplify` | skill + command both | yes |
| 13 | `/loop` dynamic | ScheduleWakeup native; cron fallback for others | yes |
| 14 | `/schedule` | CronCreate native; host cron fallback | yes |
| 15 | `/batch` worktree | `dispatch.sh --tmux` + `-w` flag | yes |
| 16 | `/btw` | existing, documented | claude-only (intentional) |
| 17 | `/voice` | **out of scope** (client-side feature, not server-side) | n/a |
| 18 | `--auto-accept` handoff | `CEX_AUTO_ACCEPT` env; all 4 boot wrappers honor | yes |
| 19 | `swarm N kind` | `dispatch.sh swarm <kind> <N>` | yes |
| 20 | `-w` dispatch flag | `dispatch.sh -w [id]` + worktree auto-create | yes |
| 21 | `--add-dir` | **out of scope** (not a CEX painpoint) | n/a |

Support artifacts:
- `.claude/rules/new-nucleus-bootstrap.md` -- 9-file checklist for N08+ nuclei
- `.claude/rules/composable-crew.md` -- updated with swarm reference
- `_docs/specs/spec_multi_runtime_features.md` -- 4-runtime compatibility matrix
- `.github/workflows/claude_learn.yml` + `_tools/cex_claude_learn.py` -- `@.claude learn` PR-comment learning loop

## Constraints

**NEVER**: skip frontmatter · publish below 8.0 · pass task as CLI arg · overwrite without git
**ALWAYS**: load builder ISOs first · compile after save · signal on complete · boot interactive
