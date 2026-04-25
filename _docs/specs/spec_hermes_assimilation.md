---
quality: 8.3
quality: 7.9
id: spec_hermes_assimilation
kind: spec
pillar: P08
nucleus: N07
domain: assimilation
type: executable_spec
version: 1.0.0
status: awaiting_gdp
tags: [hermes, assimilation, autonomous_skills, fractal_mirror, n00_source_of_truth]
upstream: N01_intelligence/P01_knowledge/kc_hermes_agent_assimilation.md
updated: 2026-04-18
density_score: 1.0
---

## TL;DR

Executable spec to assimilate HERMES (NousResearch) into CEX. Two pillars:
1. **Autonomous skill creation** — port the closed learning loop (5-tool-call
   threshold -> skill markdown -> self-improvement on reuse + nudge cycle +
   Honcho dialectic user model + FTS5 session search).
2. **Fractal mirror architecture** — N00_genesis holds the **archetype** of
   every new kind (source of truth); N01-N07 each hold a **custom mirror**
   specialized for their sin/domain. Cross-nucleus promotion rule: best
   mirror wins and back-ports to N00.

Output: 9 new kinds + 6 enriched kinds + 1 learning-loop runtime + 7 nucleus mirrors.

## Part 1 -- HERMES Autonomous Skill Creation Mechanism (verbatim)

Decoded from NousResearch README + docs + community writeups + Honcho source.

### 1.1 Trigger

> "After complex tasks (5+ tool calls), the agent creates reusable skill documents."

Complexity threshold = **>= 5 tool calls in a single task**. Below this, the
interaction is ephemeral (chat); at/above, the agent writes a persistent skill.

### 1.2 Skill Document Format

- Portable markdown following the [agentskills.io](https://agentskills.io) open standard
- Stored under `~/.hermes/skills/`
- Browsable via `/skills` or `/<skill-name>`
- Treated as **procedural memory** -- re-injected into context on similar future tasks

### 1.3 Self-Improvement On Reuse

> "Skills self-improve during use."

Mechanism: when a stored skill is loaded for a new task and the execution
diverges (new tool call order, new edge case, new parameter), the agent
**patches the skill in place** -- not a fresh copy. Skills thus grow denser
over time, not more numerous.

### 1.4 Agent-Curated Memory + Nudge Cycle

> "Agent-curated facts written to `MEMORY.md` with periodic nudges to persist durable knowledge."

- **MEMORY.md** = top-level persistent file (same pattern CEX already uses via auto-memory)
- **Nudge** = periodic in-context prompt ("do you want to persist this?") during long sessions
- Agent writes with its own discretion, subject to the nudge cadence

### 1.5 Honcho Dialectic User Model (cross-session)

From plastic-labs/honcho:

| Entity | Role |
|--------|------|
| Workspace | Top-level tenant isolation |
| Peer | Unified user/agent representation |
| Session | Interaction between peers (many-to-many with Peer) |
| Message | Atomic utterance per session |
| Collection | Named group of documents |
| Document | Vector-embedded fact per peer |

API surface:
- `peer.chat(query)` -- natural-language query against the user model
- `session.context(limits)` -- token-bounded context retrieval
- `session.add_messages()` -- ingest turn
- `alice.search()` -- hybrid search (FTS + vector) across messages
- `session.representation()` -- static peer insight for context injection

Storage: PostgreSQL + pgvector (fallback Turbopuffer / LanceDB).

Per-turn cycle (inferred from Dialectic API = `/peers/{peer_id}/chat`):
1. Turn arrives -> `session.add_messages([user_msg])`
2. Pre-response: `peer.chat("what does this user want given <msg>?")` -> static insight
3. Insight injected into generation context
4. Post-response: derived conclusions written back to peer's Collection
5. Periodic compaction: Collections summarized into durable facts

### 1.6 FTS5 Session Search

- SQLite FTS5 index over every past session message
- On context pressure, LLM summarizes hits into a few paragraphs -> injected instead of raw history
- Gives cross-session recall without blowing the context window

### 1.7 Research-Grade Outputs (byproduct)

> "Batch trajectory generation · native Atropos RL · ShareGPT export."

Every session is also a training signal. Skills + trajectories feed the
RL training loop (tinker-atropos). This is the flywheel: use -> skill ->
improvement -> RL signal -> model-level gains.

## Part 2 -- Mapping HERMES Loop -> CEX Artifacts

| HERMES component | CEX artifact (target) | Pillar | Nucleus |
|------------------|----------------------|--------|---------|
| Skill document | `skill` (enrich: auto_generated, self_improves, agentskills_compat) | P01 | N04 |
| Skill creation trigger (5 tool calls) | `self_improvement_loop` (exists, add hermes_mode) | P11 | N05 |
| MEMORY.md nudge | `curation_nudge` (NEW) | P11 | N04 |
| Honcho Peer/Session | `user_model` (NEW) | P10 | N04 |
| Honcho Dialectic loop | `memory_architecture` (exists, add dialectic_mode) | P10 | N04 |
| FTS5 + LLM summarization | `session_state` (enrich: search_backend, summarizer_model) | P10 | N04 |
| Persistent `MEMORY.md` | `knowledge_card` (pattern already in CEX auto-memory) | P01 | N04 |
| Trajectory export (ShareGPT) | `reasoning_trace` (exists, add sharegpt_export) | P11 | N05 |
| Atropos RL hook | `rl_algorithm` (exists, add trajectory_source) | P11 | N05 |

## Part 3 -- Fractal Mirror Architecture

### 3.1 The Pattern (recap for assimilated kinds)

```
N00_genesis/                           <- SOURCE OF TRUTH (archetype)
  P{XX}_{domain}/
    tpl_{kind}.md                      <- canonical template (zero-bias default)
    _schema.yaml entry                 <- authoritative schema
  P01_knowledge/library/kind/
    kc_{kind}.md                       <- canonical knowledge card

N01_intelligence/                      <- Analytical Envy mirror
  P{XX}_{domain}/
    {kind}_n01.md                      <- customized for research/intel
      overrides: tone, required_fields, analysis_depth
  P01_knowledge/
    kc_{kind}_n01_overlay.md           <- domain-specific overlay

N02_marketing/                         <- LUXURIA CRIATIVA mirror
  P{XX}_{domain}/
    {kind}_n02.md                      <- customized for copy/brand
      overrides: voice_registry, emotional_tone

N03_engineering/  <- SOBERBA INVENTIVA mirror (code/arch flavor)
N04_knowledge/    <- GULA DO CONHECIMENTO mirror (density/citation flavor)
N05_operations/   <- IRA mirror (gating/retry/strict flavor)
N06_commercial/   <- AVAREZA ESTRATEGICA mirror (pricing/conversion flavor)
N07_admin/        <- PREGUICA ORQUESTRADORA mirror (dispatch/handoff flavor)
```

### 3.2 Mirror Rules (enforced by `cex_mirror_audit.py`, NEW tool)

| Rule | Enforcement |
|------|-------------|
| R1 | Every new kind MUST land in N00 first (archetype) |
| R2 | Each N0X mirror is **optional** -- a nucleus only mirrors kinds it actually uses |
| R3 | A mirror overrides AT MOST: tone, voice, required_fields, quality_threshold, density_target, sin_lens, example_corpus |
| R4 | A mirror MAY NOT override: kind name, pillar, frontmatter schema, 8F pipeline hooks (those live in N00) |
| R5 | Periodic **best-mirror promotion**: `cex_mirror_audit.py --promote` picks the highest-quality mirror and back-ports delta into N00 tpl (with `promoted_from: N0X` provenance) |
| R6 | Cross-nucleus **inheritance**: a mirror MAY import another nucleus's mirror as fallback (e.g. N06's tagline mirror imports N02's) |

### 3.3 Promotion Ladder (best-mirror-wins)

```
quality(N00 tpl) < quality(N0X mirror) for N >= 2 nuclei consecutive
    -> cex_mirror_audit.py --promote
    -> back-port delta to N00 tpl_{kind}.md
    -> bump version (patch)
    -> other mirrors re-diff against new N00 (may retire overrides that became default)
```

This makes N00 compounding: good ideas born in a specific nucleus become
universal defaults automatically.

### 3.4 Fractal Cost Model

Assuming 9 new P1 kinds + 6 enriched kinds = 15 kind-operations:
- N00 archetype per kind: 1 tpl + 1 KC + schema entry = 3 files
- Maximum mirrors per kind: 7 (N01-N07) but realistic mean ~3 (nuclei that actually use it)
- Expected files: 15 x (3 archetype + 3 avg mirrors x 1 file) = 15 x 6 = **90 files**

## Part 4 -- Per-Kind Mirror Assignment

| # | Kind | N00 | N01 | N02 | N03 | N04 | N05 | N06 | N07 |
|---|------|-----|-----|-----|-----|-----|-----|-----|-----|
| 1 | user_model (NEW) | Y | Y (research subject) | Y (buyer persona) | - | Y (owner) | - | Y (ICP) | Y (orchestrator insight) |
| 2 | messaging_gateway (NEW) | Y | - | Y (DMs, campaigns) | - | - | Y (owner, runtime) | - | - |
| 3 | personality (NEW) | Y | - | Y (brand voice) | Y (coding style) | - | - | Y (sales persona) | Y (orchestrator persona) |
| 4 | context_file (NEW) | Y | - | - | Y (owner, codebase) | - | Y (runtime) | - | Y (CLAUDE.md variant) |
| 5 | pipeline_template (NEW) | Y | - | - | Y (dev pipelines) | - | Y (CI/CD) | - | Y (owner, dispatch) |
| 6 | revision_loop_policy (NEW) | Y | - | - | Y | Y (fact-check loop) | Y (owner) | - | Y |
| 7 | terminal_backend (NEW) | Y | - | - | Y | - | Y (owner) | - | - |
| 8 | curation_nudge (NEW) | Y | Y (intel nudge) | - | - | Y (owner, memory) | - | - | Y (mission nudge) |
| 9 | hibernation_policy (NEW) | Y | - | - | - | - | Y (owner) | - | - |
| 10 | skill (ENRICH) | Y | Y | Y | Y | Y (owner) | Y | Y | Y |
| 11 | session_state (ENRICH) | Y | - | - | Y | Y (owner) | Y | - | Y |
| 12 | sandbox_config (ENRICH) | Y | - | - | Y | - | Y (owner) | - | - |
| 13 | schedule (ENRICH) | Y | Y | Y | - | - | Y | Y | Y (owner) |
| 14 | agent (ENRICH) | Y | Y | Y | Y (owner) | Y | Y | Y | Y |
| 15 | handoff (ENRICH) | Y | Y | Y | Y | Y | Y | Y | Y (owner) |

Total ops: N00=15 + mirrors=70 = **85 artifact operations** (aligns with ~90 estimate).

## Part 5 -- Dispatch Plan (Waves)

### Wave 1 -- N00 archetypes (source of truth)

Dispatch N03 sequentially (solo, no grid -- avoids nested quote hell):

For each of 9 P1 kinds:
1. Generate N00 tpl_{kind}.md (canonical template)
2. Generate kc_{kind}.md in N00_genesis/P01_knowledge/library/kind/
3. Generate builder ISO bundle (12 ISOs) in archetypes/builders/{kind}-builder/
4. Register in .cex/kinds_meta.json
5. Add row to p03_pc_cex_universal.md (prompt_compiler) -- PT+EN pattern
6. Sub-agent in .claude/agents/{kind}-builder.md
7. Compile + doctor + commit

Estimate: 9 kinds x ~25min N03-Opus = ~4h. Token budget: ~500k.

### Wave 2 -- N00 enrichments (6 existing kinds)

For each of 6 kinds (skill, session_state, sandbox_config, schedule, agent, handoff):
1. Edit builder ISOs (add new frontmatter fields)
2. Update tpl
3. Bump schema version
4. Compile

Dispatch N03 sequentially. Estimate: 6 x ~10min = ~1h. Budget: ~150k.

### Wave 3 -- Fractal mirrors (per nucleus, per kind)

Matrix from Part 4: 70 mirror ops across N01-N07.

Parallelization rule: one nucleus per wave slot, that nucleus writes ALL its
mirrors in one dispatch (avoids boot overhead per file).

- N01 dispatch: 5 mirrors (user_model, curation_nudge, skill, schedule, agent, handoff) -> 6 files
- N02 dispatch: 7 mirrors
- N03 dispatch: 9 mirrors
- N04 dispatch: 8 mirrors
- N05 dispatch: 10 mirrors
- N06 dispatch: 5 mirrors
- N07 dispatch: 10 mirrors

Total: 55 mirror files (some kinds that table says "-" won't write).

Dispatch mode: **grid of 6** (N01-N06 parallel) + **solo N07** after grid
completes (N07 must read N01-N06 outputs to write orchestrator mirrors).

Estimate: ~30min parallel (grid) + ~20min N07. Budget: ~800k.

### Wave 4 -- Learning-loop runtime

New Python tools:

| Tool | Purpose |
|------|---------|
| `_tools/cex_skill_autocreate.py` | Watch session trace; when >=5 tool calls succeed, generate skill_{hash}.md |
| `_tools/cex_skill_improve.py` | On skill re-load, diff new trace vs stored skill, patch in place |
| `_tools/cex_user_model.py` | Honcho-pattern Peer/Session/Message store (SQLite + optional pgvector) |
| `_tools/cex_fts5_search.py` | SQLite FTS5 over all session transcripts + LLM-summarize hits |
| `_tools/cex_nudge.py` | Hook at F8 COLLABORATE: if knowledge_density>threshold, emit "persist?" prompt |
| `_tools/cex_mirror_audit.py` | Audit mirror coverage, score mirrors vs N00, promote best-mirror delta |

Estimate: 6 tools x ~30min N03-Opus = ~3h. Budget: ~400k.

### Wave 5 -- Integration (N07)

1. Wire tools into `.claude/settings.json` hooks (PostToolUse emits skill trigger)
2. Update CLAUDE.md (284 -> 300 kinds, reference learning-loop tools)
3. Update `.claude/rules/ubiquitous-language.md` (add Honcho/Hermes terms)
4. Run `cex_doctor.py` + `cex_mirror_audit.py --check`
5. Commit consolidation

Estimate: ~45min solo N07. Budget: ~80k.

**Total session budget: ~1.9M tokens, ~9h wall-clock (mostly parallel W3).**

## Part 6 -- Decision Points (GDP gate before Wave 1)

| DP | Question | Recommended default (if auto) |
|----|----------|-------------------------------|
| DP1 | All 9 P1 kinds or cherry-pick? | **All 9** |
| DP2 | Include Wave 2 (6 enrichments)? | **Yes** (same builders touched) |
| DP3 | Wave 3 mirror matrix as proposed, or leaner (e.g. N00 only)? | **As proposed** (fractal is the whole point) |
| DP4 | Wave 4 learning-loop runtime now or defer? | **Now** (kinds without the runtime are dead weight) |
| DP5 | `messaging_gateway`: stub only or port Telegram pilot? | **Stub only** (pilot ports are separate missions) |
| DP6 | `user_model` storage: SQLite only or Postgres+pgvector? | **SQLite default, pgvector optional** (matches HERMES fallback story) |
| DP7 | Skill auto-create threshold: 5 tool calls (HERMES default) or custom? | **5 tool calls** (proven) |
| DP8 | Mirror promotion cadence: manual `--promote` or auto-nightly? | **Manual for now** (observe before automating) |
| DP9 | Opus N03 vs Sonnet N03 for builder authoring? | **Opus** (reasoning-heavy) |
| DP10 | Run under current main branch or feature branch? | **Feature branch `feat/hermes-assimilation`** |

## Part 7 -- Acceptance Criteria

Gate passes when:
- [ ] 9 N00 archetypes exist + pass `cex_doctor.py`
- [ ] 6 enrichments reflected in schema versions bumped
- [ ] >= 55 mirrors written (matrix from Part 4)
- [ ] 6 runtime tools written + covered by unit tests
- [ ] `cex_skill_autocreate.py` successfully generates >= 1 skill from a live session with 5+ tool calls
- [ ] `cex_mirror_audit.py --check` reports 0 orphan mirrors
- [ ] `prompt_compiler` has 9 new rows (PT+EN)
- [ ] `.cex/kinds_meta.json` at 300 kinds
- [ ] CLAUDE.md header updated
- [ ] All commits pass pre-commit hooks
- [ ] Average artifact quality >= 9.0

## Part 8 -- Rollback Plan

If Wave 3 or 4 goes sideways:
1. `git revert` the consolidation commit (reverts whole wave atomically)
2. Mirror audit tool can detect partial state and list orphans
3. Kinds registered in step 4 but with incomplete mirrors: mark `status: draft` in kinds_meta.json
4. Feature branch isolates blast radius -- main stays clean

## Part 9 -- Post-Mission Follow-ups (out of scope, logged for later)

- Port Telegram gateway as pilot (D5 deferred)
- Atropos RL training loop wiring
- ShareGPT export utility
- agentskills.io interop (import public skills as CEX skill mirrors)
- `cex_honcho_bridge.py` -- optional real Honcho server integration (only if SQLite proves insufficient)
- Test multi-N07 sessions with mirror promotion (parallel nuclei racing to promote same kind)

## Properties

| Property | Value |
|----------|-------|
| Kind | spec |
| Pillar | P08 |
| Nucleus | N07 |
| Domain | assimilation |
| Status | awaiting_gdp |
| Upstream KC | kc_hermes_agent_assimilation.md |
| Total files planned | ~140 (archetypes 30 + enrichments ~20 + mirrors 55 + tools 6 + docs 4 + tests ~25) |
| Wall-clock estimate | ~9h |
| Token budget | ~1.9M |
| Rollback | feature branch + atomic consolidation revert |
