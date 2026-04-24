# Commands

CEXAI provides slash commands for every phase of the workflow. Commands are defined in `.claude/commands/` and work across runtimes.

## Lifecycle Commands

These commands follow the standard workflow sequence:

```
/plan  -->  /guide  -->  /spec  -->  /grid  -->  /consolidate
```

### /init

**First-time brand configuration.** Takes about 2 minutes.

```
/init
```

Asks 6 questions about your brand (name, mission, values, personality, audience, revenue model) and writes `.cex/brand/brand_config.yaml`. All subsequent artifacts auto-inject your brand context. See [[Getting Started]] for details.

### /plan

**Decompose a goal into tasks.** Identifies which nuclei handle each task and maps dependencies.

```
/plan build a content marketing system
```

Output: task list with nucleus assignments, dependency graph, and wave structure.

### /guide

**Co-pilot mode.** Triggers the Guided Decision Protocol (GDP) -- CEXAI asks you subjective questions before building.

```
/guide create a brand launch kit
```

GDP presents Decision Points for tone, audience, style, and other subjective choices. Answers are recorded in `.cex/runtime/decisions/decision_manifest.yaml` and carried to all dispatched nuclei.

Natural language triggers that also activate GDP: "guide me", "ask me first", "let's decide together", "walk me through", "help me choose".

### /spec

**Create a spec blueprint** from a plan and decisions.

```
/spec plan_content_marketing
```

Output: exact list of artifacts to produce, with kinds, pillars, and target paths.

### /grid

**Execute a spec by dispatching nuclei autonomously.**

```
/grid spec_content_marketing
```

Dispatches up to 6 nuclei in parallel. Each nucleus reads its handoff, loads the decision manifest, and executes the [[8F Pipeline]] autonomously.

### /consolidate

**Post-dispatch cleanup.** Verifies deliverables, scores quality, stops processes, and archives signals.

```
/consolidate
```

### /mission

**Full lifecycle shortcut.** Combines `/plan` + `/guide` + `/spec` + `/grid` + `/consolidate` in one command.

```
/mission build a SaaS onboarding system
```

This is the most common entry point for complex goals. CEXAI decomposes the goal, asks you decisions, creates a spec, dispatches nuclei, monitors progress, and consolidates results.

## Build Commands

### /build

**Build a single artifact** via the [[8F Pipeline]].

```
/build knowledge_card about prompt engineering
/build landing_page for developer tools product
/build agent for customer support automation
```

The intent is resolved to a [[Kinds|kind]], the builder is loaded, and the full F1-F8 pipeline executes.

### /dispatch

**Send a task to a specific nucleus.**

```
/dispatch n03 "build the agent card for N05"
/dispatch n01 "research competitor pricing in EdTech"
```

Lower-level than `/build` -- you choose the nucleus explicitly.

### /validate

**Check artifact quality** against gates and scoring rubrics.

```
/validate path/to/artifact.md
/validate all
```

Runs F7 GOVERN checks: 7 hard gates, 12-point checklist, 5-dimension scoring.

## Monitoring Commands

### /status

**System health dashboard.** Shows running processes, signal state, artifact counts, and quality distribution.

```
/status
```

### /cex-doctor

**Full diagnostics.** Separate from Claude Code's native `/doctor`.

```
/cex-doctor
/cex-doctor fast
/cex-doctor full
/cex-doctor audit n03
```

Tiered execution: `fast` for quick checks, `full` for comprehensive validation, `audit <name>` for nucleus-specific inspection.

## Improvement Commands

### /evolve

**Autonomous artifact improvement loop.** Scans artifacts below quality threshold and improves them iteratively.

```
/evolve path/to/artifact.md
/evolve all
```

Uses heuristic pass first (free, no LLM calls), then agent mode for stubborn artifacts.

### /mentor

**Vocabulary and taxonomy navigator.** Teaches the CEXAI methodology through storytelling, analogies, and quizzes.

```
/mentor what is a kind?
/mentor explain 8F pipeline
/mentor quiz me on pillars
```

Covers the 8F pipeline, 12 pillars, and 300-kind taxonomy. Available in multiple didactic modes.

## Crew Commands

### /crew

**Manage composable multi-role teams.** See [[Architecture]] for crew concepts.

```
/crew list                    # List registered crews
/crew show product_launch     # Inspect a crew's resolved plan
/crew run product_launch      # Execute a crew (dry run)
```

Crews combine multiple roles into coherent packages with handoffs, using one of three topologies: sequential, hierarchical, or consensus.

## Dispatch Infrastructure

These are the underlying shell commands that `/dispatch` and `/grid` use:

```bash
# Solo -- 1 builder in a new window
bash _spawn/dispatch.sh solo n03 "task description"

# Grid -- up to 6 parallel builders
bash _spawn/dispatch.sh grid MISSION_NAME

# Monitor running dispatches
bash _spawn/dispatch.sh status

# Stop my session's nuclei only (safe)
bash _spawn/dispatch.sh stop

# Stop a specific nucleus (surgical)
bash _spawn/dispatch.sh stop n03

# Stop all nuclei across all sessions (dangerous)
bash _spawn/dispatch.sh stop --all

# Preview what would be killed
bash _spawn/dispatch.sh stop --dry-run

# Swarm -- N parallel builders of the same kind
bash _spawn/dispatch.sh swarm agent 5 "scaffold 5 niche sales agents"
```

Session-aware: multiple N07 orchestrators can run simultaneously. `stop` only kills your own session's nuclei by default.

## Quick Reference

| Command | Purpose | GDP? |
|---------|---------|------|
| `/init` | Configure brand | Yes |
| `/plan <goal>` | Decompose goal into tasks | No |
| `/guide [goal]` | Co-pilot decisions | Yes |
| `/spec [plan]` | Create spec blueprint | No |
| `/grid [spec]` | Dispatch nuclei | No (reads manifest) |
| `/build <intent>` | Build single artifact | No (factual) |
| `/validate [target]` | Check quality | No |
| `/dispatch <nuc> <task>` | Send task to nucleus | No |
| `/mission <goal>` | Full lifecycle | Yes (at /guide phase) |
| `/status` | Health dashboard | No |
| `/cex-doctor` | Full diagnostics | No |
| `/consolidate` | Post-dispatch cleanup | No |
| `/evolve [target]` | Improve artifacts | No |
| `/mentor [question]` | Teach methodology | No |
| `/crew <action>` | Manage crews | No |

## Related Pages

- [[Getting Started]] -- First `/build` and `/mission` walkthrough
- [[8F Pipeline]] -- The reasoning protocol behind `/build`
- [[Architecture]] -- Nuclei, dispatch modes, and crews
- [[Kinds]] -- What `/build` produces
