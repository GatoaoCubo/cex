---
quality: 8.2
quality: 7.6
id: skill_catalog_cex
kind: knowledge_card
pillar: P01
title: "CEX Skill & Command Catalog"
version: 1.0.0
tags: [skills, commands, catalog, reference, open-source]
skill_count: 10
command_count: 20
related:
  - spec_n07_operational_intelligence
  - auto-accept-handoff
  - p01_kc_orchestration_best_practices
  - p08_ac_orchestrator
  - p03_sp_orchestration_nucleus
  - p01_kc_cex_orchestration_architecture
  - bld_examples_skill
  - p12_wf_admin_orchestration
  - n07_output_orchestration_audit
  - p12_wf_orchestration_pipeline
density_score: 0.99
updated: "2026-04-22"
---

# CEX Skill & Command Catalog

Complete reference for all skills (auto-fire and user-invoked) and slash commands.
For each: trigger, what it does, when to use, prerequisites, and recommendations.

---

## Skills

Skills are behaviors the system knows how to execute. Some fire automatically
(auto-fire) in response to events. Others are triggered by the user with a slash command.

### How Skills Differ from Commands

| | Skills | Commands |
|---|--------|----------|
| Where defined | `.claude/skills/*.md` | `.claude/commands/*.md` |
| Multi-runtime | Yes (mirrored to `.cex/skills/`) | Claude-only |
| Fire mode | Auto-fire (event) or user-invoked | User-invoked only |
| Scope | Behavioral primitives | Orchestration flows |

---

### Skill Table

| Skill | Type | Trigger | What it does | When to use | Prerequisites |
|-------|------|---------|-------------|-------------|---------------|
| `auto-accept-handoff` | auto-fire | Grid/overnight dispatch | Sets `auto_accept: true` on handoffs so nuclei use recommended defaults instead of blocking on uncovered GDP gaps | When dispatching autonomous missions where user will not be present | Decision manifest locked via GDP |
| `btw` | user-invoked | `/btw` or "btw..." in message | Captures an ad-hoc observation the user drops mid-work into the right memory type (user, feedback, project, reference) without breaking flow | When user drops context mid-session that should survive across conversations | None |
| `commit` | user-invoked | `/commit` or "commit" | Stages changes, writes conventional commit grouped by nucleus, runs pre-commit hooks | When ready to save changes to git | Changes exist in working tree |
| `cross-wave-cleanup` | auto-fire | Between waves of /mission, /grid, /showoff, /batch | Kills wrapper PID trees and orphan processes between dispatch waves so the next wave starts clean | After any multi-spawn wave completes and before the next wave starts | Active PID tracking in `.cex/runtime/pids/` |
| `dream` | user-invoked | `/dream` or "brainstorm" | Generates 3-5 divergent approaches to a problem before committing to one | When the problem is ill-specified or has multiple valid architectures; when picking wrong = multi-day rework | None |
| `new-nucleus-bootstrap` | auto-fire | Creating N08+ | Scaffolds rule, agent card, prompt, 4 boot scripts, and scoped permissions for a new nucleus | When extending CEX beyond the current 7 nuclei | N07 orchestrator session |
| `shared-file-proposal` | auto-fire | Concurrent nuclei active | Uses a `.proposal` file instead of direct edits when concurrent nuclei need to change `CLAUDE.md`, `kinds_meta.json`, shared tools, or rules | During grid or concurrent dispatch when more than one nucleus is active | Grid or multi-nucleus dispatch active |
| `simplify` | user-invoked | `/simplify [path]` | Reviews changed code for reuse, quality, and efficiency across three lenses; fixes issues found | After implementing a feature, before committing; when code feels over-engineered | Changes exist (defaults to `git diff HEAD`) |
| `verify` | user-invoked | `/verify` | Validates artifacts against quality gates and schema; reports score and gate pass/fail | After building or modifying artifacts; before signaling N07 that work is done | Artifact exists |
| `mentor` | user-invoked | `/mentor [topic]` | Teaches CEX concepts through 4 lenses (storytelling, analogy, quiz, media) with Socratic dialogue | When learning CEX methodology; when producing educational content for external use | None |

---

### Skill Details

#### `auto-accept-handoff`
When N07 writes handoff files for a grid dispatch (especially for overnight or unattended runs), this skill adds `auto_accept: true` to the frontmatter. Nuclei reading this field know to use the recommended default for any decision gap not covered by the GDP manifest -- they do not pause and ask the user.

**Why**: Prevents a dispatched nucleus from blocking indefinitely on a subjective choice when no one is watching.

**Related**: Decision manifest at `.cex/runtime/decisions/decision_manifest.yaml`

---

#### `btw`
Decision tree for classifying what the user just said:
1. **User fact / preference / correction** -> `~/.claude/projects/.../memory/` as `feedback_*.md` or `user_*.md`
2. **Project state / decision / deadline** -> `.cex/runtime/` or `N0x/memory/` as `project_*.md`
3. **External pointer** (Linear, Slack, Grafana URL) -> `reference_*.md`

Saves immediately. Does not interrupt the current flow.

---

#### `cross-wave-cleanup`
After any wave completes, this skill:
1. Reads `.cex/runtime/pids/spawn_pids.txt` for wrapper + worker PIDs from that wave
2. Identifies completed workers (signaled or process exited)
3. Issues `taskkill /F /PID <pid> /T` (tree-kill: kills parent + all children including claude.exe, node.exe, uvx)
4. Cleans up PID file entries for the dead processes
5. Reports a clean-state confirmation to N07

**Warning**: Never use `Stop-Process` -- it orphans grandchildren. Tree-kill is mandatory.

---

#### `shared-file-proposal`
When a nucleus running in a grid needs to edit a protected shared file (CLAUDE.md, kinds_meta.json, a shared tool), instead of writing directly it:
1. Creates a `.proposal` file alongside the target: `CLAUDE.md.proposal_n03`
2. Describes the change in structured format (line range, old content, new content)
3. Signals N07 that a proposal is pending
4. N07 or the user applies proposals after the wave completes

**Why**: Prevents git merge conflicts when 3+ nuclei try to edit the same file in the same wave.

---

## Commands

Slash commands are the primary user interface for CEX. Every command is backed by a skill or a set of instructions that the active nucleus (usually N07) executes.

---

### Command Table

| Command | Usage | What it does | When to use | Nucleus | Est. Time |
|---------|-------|-------------|-------------|---------|-----------|
| `/init` | `/init [folder_path]` | First-time brand setup -- ~6 questions, generates `brand_config.yaml` | First time using CEX (skip if dev/test repo) | N07 | 2 min |
| `/plan <goal>` | `/plan build CRM` | Decomposes goal into tasks, identifies nuclei, maps wave dependencies | Starting a new project or feature | N07 | 2-5 min |
| `/guide [topic]` | `/guide pricing` | Co-pilot mode: asks GDP decision points before building | When subjective choices matter (tone, audience, style) | N07 | 3-10 min |
| `/spec [plan]` | `/spec plan_crm` | Creates detailed spec from plan + decisions (artifact list, wave structure) | After `/plan` + `/guide` | N07 | 3-5 min |
| `/grid [spec]` | `/grid BRAND_LAUNCH` | Dispatches nuclei autonomously from spec | After spec is ready and decisions are locked | N07 | 30-60 min |
| `/build <intent>` | `/build agent for sales` | Builds single artifact via 8F pipeline | When you need exactly 1 artifact | N03 (routed) | 2-5 min |
| `/validate [file\|all]` | `/validate all` | Checks artifact quality against quality gates; reports scores | After building, before publishing | N05 | 1-3 min |
| `/dispatch <nuc> <task>` | `/dispatch n03 fix tests` | Sends task to specific nucleus (bypasses intent resolution) | When you know exactly which nucleus to use | target | 1-2 min setup |
| `/mission <goal>` | `/mission launch product` | Full lifecycle shortcut: plan + guide + spec + grid + consolidate | Ambitious multi-artifact goals; the "do everything" path | N07 | 30-90 min |
| `/status` | `/status` | System health dashboard: processes, signals, quality metrics, PID states | Anytime; especially after dispatch | N07 | instant |
| `/cex-doctor` | `/cex-doctor` or `/cex-doctor --full` | Full diagnostics: builder health (302 builders), ISOs, schema wiring | When something seems broken; before a release gate | N07 | 1-3 min |
| `/consolidate` | `/consolidate` | Post-dispatch: verify deliverables, stop processes, commit results, archive signals | After nuclei complete a wave | N07 | 2-5 min |
| `/evolve [file\|all]` | `/evolve all` | Autonomous artifact improvement loop (heuristic then agent mode) | When quality < 9.0 across artifacts; post-session cleanup | N07 | 10-60 min |
| `/mentor [topic]` | `/mentor 8F` | Teach CEX via 4 lenses: storytelling, analogy, quiz, media production | Learning CEX methodology; producing educational content | N04 | 5-20 min |
| `/batch <file>` | `/batch intents.txt` | Run many tasks in parallel worktrees (one intent per line) | Bulk artifact production; swarm mode | N07 | varies |
| `/simplify [path]` | `/simplify _tools/` | Review and fix code quality across 3 lenses | Code cleanup before release; after refactor | N05 | 2-10 min |
| `/loop [interval] <cmd>` | `/loop 5m /status` | Run a command on a recurring interval (self-paced if no interval given) | Monitoring a long-running grid; polling for state | N07 | ongoing |
| `/schedule <cron> <cmd>` | `/schedule "0 */6 * * *" /evolve` | Create a scheduled remote agent (cron-based) | Recurring automated tasks; nightly quality runs | N07 | setup only |
| `/showoff` | `/showoff [--skip gemini]` | 4-runtime grid validation: Claude + Codex + Gemini + Ollama in 5 waves | Proving multi-runtime works; smoke-testing after config changes | N07 | 15-30 min |
| `/grid-test` | `/grid-test` | Multi-runtime wave orchestration for cross-runtime validation | Before major deployments; verifying runtime parity | N07 | 20-40 min |

---

### Command Details

#### `/init`
Runs the brand bootstrap protocol. Asks 6 questions conversationally:
1. Company/brand name
2. What you do in one sentence
3. 3 core values
4. Brand personality (formal/casual, technical/friendly)
5. Ideal customer description
6. Revenue model (subscription, one-time, courses, etc.)

Produces `.cex/brand/brand_config.yaml`. Skip on dev/test repos where brand context is not needed.

---

#### `/build <intent>`
The fastest path to one artifact. Intent is transmuted via `cex_intent_resolver.py` to `{kind, pillar, nucleus}`, then the appropriate builder is loaded and 8F runs.

Examples:
- `/build knowledge card about React hooks` -> kind=knowledge_card, N04
- `/build landing page for SaaS product` -> kind=landing_page, N02
- `/build agent for customer support` -> kind=agent, N03

---

#### `/guide`
Triggers the Guided Decision Protocol (GDP). N07 identifies all subjective decisions the upcoming task requires and presents them as Decision Points (DP1, DP2, ...). User answers are written to `.cex/runtime/decisions/decision_manifest.yaml`. This manifest travels with every handoff so nuclei know the decisions without re-asking.

Use `/guide` before any `/grid` or `/mission` that has subjective choices (tone, audience, visual style, pricing model).

---

#### `/evolve [target]`

Three evolution modes:
- **Heuristic** (free): string substitution, structure fixes, density improvements
- **Agent** (token cost): LLM rewrites artifact using loaded builder ISOs
- **Sweep** (`--all`): runs across all artifacts below quality threshold

Default threshold: quality < 9.0. Tool: `cex_evolve.py`.

---

#### `/cex-doctor`

Two tiers:
- **fast** (default): checks ISOs, sub-agents, schema wiring for all 302 builders
- **full**: adds flywheel audit (109 checks across 7 layers), ASCII compliance scan, brand ref scan
- **audit <name>**: focuses on one builder or nucleus

Target: 0 FAIL before any public release.

---

#### `/consolidate`

N07 consolidation loop (in order):
1. DETECT: poll `git log --since` + `.cex/runtime/signals/` for completion
2. VERIFY: `python _tools/cex_doctor.py` (quick health check)
3. STOP: `bash _spawn/dispatch.sh stop` (session-aware kill-tree)
4. COMMIT: stage nucleus outputs + write commit (Gemini nuclei need manual commit)
5. REPORT: output consolidation summary with quality scores and next steps

Also unloads Ollama models (`ollama unload`) to free VRAM between waves.

---

## Workflow Recommendations

| Goal | Recommended Flow | Approx. Time |
|------|-----------------|--------------|
| Build 1 artifact | `/build <intent>` | 2-5 min |
| Build with guidance | `/guide` then `/build` | 5-10 min |
| Multi-artifact project | `/plan` -> `/guide` -> `/spec` -> `/grid` -> `/consolidate` | 30-60 min |
| Full autopilot | `/mission <goal>` | 30-90 min |
| Improve existing | `/evolve [target]` | 10-60 min |
| Learn CEX | `/mentor [topic]` | 5-20 min |
| Diagnose issues | `/cex-doctor` then `/status` | 2-5 min |
| Multi-runtime validation | `/showoff` or `/grid-test` | 15-40 min |
| Bulk production | `/batch <intents.txt>` | varies |

---

## Decision: Skill vs Command vs Tool

| If you want to... | Use |
|-------------------|-----|
| Capture context mid-flow | Skill: `btw` |
| Commit changes correctly | Skill: `commit` |
| Clean code quality | Skill or Command: `simplify` |
| Validate artifacts | Skill: `verify` |
| Build one artifact | Command: `/build` |
| Run full project lifecycle | Command: `/mission` |
| Execute a Python pipeline | Tool: `_tools/cex_*.py` |
| Dispatch autonomously | Command: `/grid` + `dispatch.sh` |

---

## Related Files

| File | Purpose |
|------|---------|
| `.claude/skills/*.md` | Skill definitions (source of truth) |
| `.claude/commands/*.md` | Command implementations |
| `.cex/skills/*.md` | Multi-runtime mirrors (Codex, Gemini, Ollama) |
| `_spawn/dispatch.sh` | Grid/solo dispatch script |
| `.cex/runtime/decisions/decision_manifest.yaml` | GDP decision record |
| `.cex/runtime/handoffs/` | Active task handoffs |
| `.cex/runtime/signals/` | Nucleus completion signals |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_n07_operational_intelligence]] | downstream | 0.36 |
| [[auto-accept-handoff]] | downstream | 0.34 |
| [[p01_kc_orchestration_best_practices]] | sibling | 0.32 |
| [[p08_ac_orchestrator]] | downstream | 0.30 |
| [[p03_sp_orchestration_nucleus]] | downstream | 0.29 |
| [[p01_kc_cex_orchestration_architecture]] | sibling | 0.28 |
| [[bld_examples_skill]] | downstream | 0.26 |
| [[p12_wf_admin_orchestration]] | downstream | 0.26 |
| [[n07_output_orchestration_audit]] | downstream | 0.25 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.25 |
