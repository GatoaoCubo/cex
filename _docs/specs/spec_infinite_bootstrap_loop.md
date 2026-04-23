---
id: spec_infinite_bootstrap_loop
kind: context_doc
title: "CEX Peak Architecture: Infinite Bootstrap Loop"
version: 2.0.0
quality: 9.0
created: 2026-04-07
updated: 2026-04-08
purpose: Full spec for autonomous infinite self-building loop with max throughput (Claude Code native)
density_score: null
---

# CEX Peak Architecture: Infinite Bootstrap Loop

## Vision

CEX builds itself from zero. N07 orchestrates continuously, 6 nuclei work
in parallel (each with sub-agents via Claude Code Agent tool), artifacts
flow through 8F, quality gates filter, and the flywheel never stops.
N07 never idles.

## Bill of Materials (from zero)

| Component | Files | Tokens est. |
|-----------|-------|------------|
| Builder ISOs (13 per kind) | 1,630 | 24.5M |
| Kind KCs | 123 | 1.8M |
| Domain KCs | 88 | 1.3M |
| Templates + examples | 377 | 5.7M |
| Pillar schemas | 12 | 0.2M |
| Tools (.py) | 59 | 0.9M |
| Rules + configs | 16 | 0.2M |
| Nucleus artifacts | 313 | 4.7M |
| Sub-agents | 125 | 1.9M |
| **TOTAL** | **2,742** | **41.1M** |

## Throughput Estimates

| Configuration | Artifacts/hour | Time to build all |
|--------------|---------------|-------------------|
| 6 nuclei solo | 180 | 15.2h |
| 6 nuclei x4 sub-agents | 720 | 3.8h |
| + continuous batching | 864 | 3.2h |

## Architecture

```
overnight_infinite.cmd (loop forever)
  |
  +-- N07 (claude --continue, resumes session state)
  |     |
  |     +-- WORK + DISPATCH (non-blocking interleaved)
  |     |     |
  |     |     +-- N01 + Agent tool sub-agents (research)
  |     |     +-- N02 + Agent tool sub-agents (marketing)
  |     |     +-- N03 + Agent tool sub-agents (build)
  |     |     +-- N04 + Agent tool sub-agents (knowledge)
  |     |     +-- N05 + Agent tool sub-agents (code)
  |     |     +-- N06 + Agent tool sub-agents (commercial)
  |     |     |
  |     |     +-- = 6 nuclei x (1 + 4 sub-agents) = 30 LLM streams
  |     |
  |     +-- When context approaching limit:
  |           write state to disk, exit cleanly
  |
  +-- SLEEP 10s
  +-- RESTART N07 (claude --continue, fresh context via auto-compaction)
```

## 5 Blockers and Solutions

### Blocker 1: N07 Context Exhaustion (dies at 1M tokens)

**Problem**: N07 fills its 1M context and can't continue orchestrating.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **claude --continue** | Claude Code natively supports `--continue` flag to resume previous session | Native in Claude Code |
| **claude --fork-session** | Creates a new session forked from previous state (prevents corruption) | Native in Claude Code |
| **Auto-compaction** | Claude Code automatically compresses conversation when approaching context limit | Native in Claude Code |
| **mission_state.yaml** | CEX-specific checkpoint file on disk with task queue + progress | NEEDS BUILD |

**Recommended approach**: Combine `mission_state.yaml` (CEX state) with Claude Code's `--continue` or `--fork-session` (context transfer).

```yaml
# .cex/runtime/mission_state.yaml
mission: full_bootstrap
started: 2026-04-07T20:00:00
wave: 3
tasks_total: 2742
tasks_completed: 847
tasks_in_progress:
  n01: {task: "research_kc_batch_12", started: "2026-04-07T22:14:00"}
  n03: {task: "build_isos_wave3", started: "2026-04-07T22:14:30"}
next_tasks:
  - {nucleus: n03, kind: prompt_template, count: 9}
  - {nucleus: n04, kind: knowledge_card, count: 15}
quality_gate:
  passed: 830
  failed: 17
  retried: 12
tokens_used: 12400000
```

**Implementation**: N05 builds `cex_mission_state.py` (read/write/update checkpoint).
N07 reads on boot, writes before context exhaustion.

**Comparison: Claude Code vs alternatives for session continuity**:

| Feature | Claude Code | Gemini CLI | Codex CLI |
|---------|------------|------------|-----------|
| Session resume | `--continue` | Not supported | Not supported |
| Safe fork | `--fork-session` | N/A | N/A |
| Auto-compaction | Built-in | N/A | N/A |
| Context window | 1M tokens | 1M tokens | 192K tokens |

### Blocker 2: Sub-agents Inside Each Nucleus (6x -> 30x)

**Problem**: Each nucleus runs 1 LLM instance. Could run 1 + 4 sub-agents.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **Claude Code Agent tool** | Native sub-agent spawning built into Claude Code. Supports parallel execution, typed agent specialization, automatic context isolation | Native in Claude Code |
| **Agent .md files** | YAML frontmatter defines agent: name, tools, model. Auto-discovered from `.claude/agents/` | Native convention |
| **--agents JSON** | Inline agent definitions via CLI flag for runtime agent creation | Native in Claude Code |
| **subagent_type parameter** | Agent tool accepts `subagent_type` to route to specialized agent definitions | Native in Claude Code |

**Recommended approach**: Use Claude Code Agent tool directly -- no extensions needed.

```
.claude/agents/                      # Project-level agents for CEX
  knowledge-card-builder.md          # Sub-agent: builds 1 KC
  agent-builder.md                   # Sub-agent: builds 1 agent artifact
  prompt-template-builder.md         # Sub-agent: builds 1 prompt template
  ...                                # 125 builder sub-agents total
```

Each nucleus uses the Agent tool natively. When N03 gets "build 12 ISOs for citation-builder", it spawns:
- 4+ parallel sub-agents via Agent tool, each building a subset
- Total time: fraction of solo execution

**Constraint**: Agent tool supports concurrent parallel sub-agents.
With 6 nuclei x 4+ concurrent = 24+ parallel LLM streams.

**Comparison: Sub-agent approaches**:

| Approach | Isolation | Setup | Concurrency | Status |
|----------|-----------|-------|-------------|--------|
| Claude Code Agent tool | Full (separate context) | Zero config | Unlimited parallel calls | Native |
| LangGraph sub-graphs | Shared process | Python setup | Async coroutines | External lib |
| CrewAI agents | Shared process | YAML config | Thread pool | External lib |

### Blocker 3: Git Conflicts (6 nuclei writing same repo)

**Problem**: Multiple nuclei committing simultaneously causes merge conflicts
on shared files (kinds_meta.json, _schema.yaml).

**Solutions found**:

| Solution | How | Pros | Cons |
|----------|-----|------|------|
| **Branch-per-nucleus** | Each nucleus works in `n0X/task` branch, N07 merges | Clean isolation | Merge overhead, N07 must resolve |
| **Lock files** | `.cex/runtime/locks/{file}.lock` with PID | Simple | Deadlocks if nucleus crashes |
| **Append-only directories** | Each nucleus writes only to its own `N0X_*/` dir | Zero conflicts | Shared files (kinds_meta) still conflict |
| **N07 consolidation queue** | Nuclei write to staging dir, N07 applies to main | Zero conflicts | Delay between produce and commit |
| **Proposal pattern** | Nuclei write `.proposal.md` files, N07 merges post-wave | Zero conflicts | Deferred application |

**Recommended approach**: Hybrid -- append-only for artifacts + proposal pattern for shared resources.

Current reality: nuclei ALREADY mostly write to their own directories.
The only shared files that conflict:
- `.cex/kinds_meta.json` -- N07 should be sole writer (nuclei propose, N07 applies)
- `P{xx}/_schema.yaml` -- same, N07 applies
- `archetypes/builders/` -- conflict-free if each nucleus builds different kinds

**Implementation**:
1. `_tools/cex_lock.py` -- atomic file locking (PID-based, auto-expire 5min) -- EXISTS
2. Rule: nuclei NEVER edit kinds_meta.json or _schema.yaml directly
3. Rule: nuclei write proposals to `.cex/runtime/proposals/{nucleus}_{file}.yaml`
4. N07 reads proposals, applies to shared files, commits
5. See `.claude/rules/shared-file-proposal.md` for full protocol

### Blocker 4: Continuous Batching (no wave gaps)

**Problem**: Current model is wave-based -- dispatch all, wait all, consolidate, next wave.
Idle time between waves wastes throughput.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **Event-driven dispatcher** | N07 checks git log every ~30s, dispatches next task immediately when a nucleus finishes | PATTERN EXISTS (non-blocking lifecycle rule) |
| **Task queue file** | `.cex/runtime/task_queue.yaml` with prioritized tasks, N07 pops and dispatches | NEEDS BUILD |
| **cex_mission_runner.py** | Already supports multi-wave with signal polling | EXISTS but wave-based |

**Recommended approach**: Enhance `cex_mission_runner.py` with continuous mode.

```python
# Current (wave-based):
dispatch_wave(nuclei) -> wait_all() -> consolidate() -> next_wave()

# Target (continuous):
while tasks_remain():
    for nucleus in idle_nuclei():
        task = pop_next_task(nucleus.domain)
        dispatch(nucleus, task)
    sleep(30)
    check_completions()  # git log + signals
    consolidate_completed()
```

**Implementation**: N05 adds `--continuous` flag to `cex_mission_runner.py`.

### Blocker 5: Infinite Runtime (overnight_infinite.cmd)

**Problem**: N07 eventually exhausts context or crashes. Need auto-restart.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **CMD loop** | `@echo off` + `:loop` + `goto loop` with claude inside | PATTERN EXISTS (overnight_h1.cmd) |
| **claude --continue** | Resume previous session with context | Native in Claude Code |
| **claude --fork-session** | Fork session to prevent state corruption on resume | Native in Claude Code |
| **Auto-compaction** | Claude Code compresses conversation automatically | Native in Claude Code |
| **mission_state.yaml** | State file survives restart | NEEDS BUILD |

**Recommended approach**: CMD loop + mission_state.yaml + claude --continue.

```cmd
@echo off
title CEX INFINITE BOOTSTRAP
:loop
echo [%time%] Starting N07 session...

claude --model opus-4-6 ^
   --append-system-prompt "N07_admin/agent_card_n07.md" ^
   --append-system-prompt ".cex/config/context_self_select.md" ^
   -p "Read .cex/runtime/mission_state.yaml. Continue the mission from where it left off. When context is 80%%%% full, write state and exit with message EXIT_CHECKPOINT."

echo [%time%] N07 exited. Restarting in 10s...
timeout /t 10 /nobreak
goto loop
```

**Key**: N07 must write `mission_state.yaml` BEFORE exiting. The next instance reads it and continues seamlessly.

**Comparison: Restart strategies**:

| Strategy | Context preserved | State preserved | Risk |
|----------|------------------|-----------------|------|
| `--continue` (same session) | Yes (compacted) | Yes | Compaction loss |
| `--fork-session` (new from old) | Partial (forked) | Yes (if state file written) | Fork divergence |
| Fresh start + state file | No | Yes (from disk) | Cold start overhead |
| **Recommended: state file + --continue** | **Yes** | **Yes** | **Minimal** |

## Implementation Roadmap

| Step | What | Nucleus | Depends on | Effort |
|------|------|---------|-----------|--------|
| 1 | `cex_mission_state.py` (checkpoint R/W) | N05 | -- | 1 dispatch |
| 2 | `overnight_infinite.cmd` (auto-restart loop) | N05 | Step 1 | 1 dispatch |
| 3 | `cex_lock.py` (shared file locking) | N05 | -- | EXISTS |
| 4 | Proposal pattern for shared files | N07 (rule) | Step 3 | EXISTS |
| 5 | Agent tool sub-agent definitions | -- | -- | EXISTS (125 in .claude/P02_model/) |
| 6 | Boot scripts with Claude Code CLI | N05 | -- | EXISTS (boot/n0X.cmd) |
| 7 | `--continuous` mode in mission_runner | N05 | Steps 1,3 | 1 dispatch |
| 8 | Task queue file + auto-prioritization | N05 | Step 7 | 1 dispatch |
| 9 | Full integration test (mini bootstrap) | N07 | Steps 1-8 | 1 mission |

**Estimated total**: 4 dispatches + 1 integration test (Steps 3-6 already exist).
With continuous batching: ~1 hour to build remaining infrastructure.
Then the infrastructure builds CEX: ~3-4 hours for full from-zero bootstrap.

## Multi-Provider Model Strategy

### The Insight: Not Every Task Needs Opus

Opus 4.6 (1M context, $15/M tokens) is overkill for mechanical tasks.
A 3-tier model strategy cuts cost 70%+ without quality loss:

| Tier | Model | Context | Cost/M | Use for |
|------|-------|---------|--------|---------|
| **T1 Reasoning** | claude-opus-4-6 | 1M | $15 | Complex builds, architecture, research |
| **T2 Execution** | claude-sonnet-4-6, gemini-2.5-pro | 200K-1M | $3-5 | Standard ISOs, KCs, templates |
| **T3 Mechanical** | claude-haiku-4-5, gemini-flash, ollama/qwen3 | 128K-200K | $0-0.25 | Renames, format fixes, compilation |

### How Claude Code Supports Multi-Model

Claude Code supports model selection per process via `--model` flag:

```bash
# Nucleus main process: Opus (complex orchestration)
claude --model opus-4-6

# Sub-agent via Agent tool: Haiku (fast recon, read-only)
# Defined in .claude/agents/scout.md with model frontmatter
# Or specified inline: Agent({ model: "haiku", ... })

# Sub-agent via Agent tool: Sonnet (standard artifact generation)
# Defined in .claude/agents/builder-iso.md with model frontmatter

# Per-dispatch model override:
# Agent({ model: "sonnet", subagent_type: "knowledge-card-builder", ... })
```

**Comparison: Multi-model support across CLIs**:

| CLI | Model selection | Sub-agent model override | Provider switching |
|-----|----------------|--------------------------|-------------------|
| Claude Code | `--model` flag + Agent tool `model` param | Yes (per sub-agent) | Anthropic only (native) |
| Gemini CLI | `--model` flag | No sub-agent system | Google only |
| Codex CLI | `--model` flag | No sub-agent system | OpenAI only |

### The 3-Tier Architecture Applied to CEX

```
N07 (Opus -- needs deepest reasoning for orchestration)
  |
  +-- N03 Engineering (Opus -- complex 8F pipeline, 12 ISOs)
  |     +-- Agent(model:"sonnet"): builder-iso (standard ISO generation)
  |     +-- Agent(model:"sonnet"): builder-iso
  |     +-- Agent(model:"haiku"): formatter (frontmatter fixes)
  |     +-- Agent(model:"haiku"): compiler (cex_compile.py runner)
  |
  +-- N01 Research (Opus -- deep analysis, 1M context for papers)
  |     +-- Agent(model:"haiku"): scout (fast web search recon)
  |     +-- Agent(model:"haiku"): scout
  |     +-- Agent(model:"sonnet"): kc-writer (structured KC from research)
  |     +-- Agent(model:"sonnet"): kc-writer
  |
  +-- N04 Knowledge (Sonnet -- standard indexing, no deep reasoning)
  |     +-- Agent(model:"haiku"): kc-writer (batch KC generation)
  |     +-- Agent(model:"haiku"): kc-writer
  |     +-- Agent(model:"haiku"): formatter (compile + validate)
  |     +-- Agent(model:"haiku"): indexer (cex_index.py runner)
  |
  +-- N05 Operations (Opus -- code requires precision)
  |     +-- Agent(model:"haiku"): test-runner (run tests, report results)
  |     +-- Agent(model:"haiku"): linter (mechanical checks)
  |
  +-- N02 Marketing (Sonnet -- creative but structured)
  |     +-- Agent(model:"sonnet"): copy-writer (ad variants)
  |     +-- Agent(model:"haiku"): formatter
  |
  +-- N06 Commercial (Sonnet -- pricing models, structured)
        +-- Agent(model:"haiku"): analyst (data gathering)
        +-- Agent(model:"haiku"): formatter
```

### Cost Model at Peak Throughput

| Component | Instances | Model | Tokens/hr | Cost/hr |
|-----------|-----------|-------|-----------|---------|
| N07 orchestrator | 1 | Opus | 500K | $7.50 |
| Nucleus main (x6) | 6 | Opus (2) + Sonnet (4) | 6M | $30-60 |
| Sub-agents T2 (x12) | 12 | Sonnet | 12M | $36-60 |
| Sub-agents T3 (x12) | 12 | Haiku | 12M | $0-3 |
| **TOTAL** | **31** | **mixed** | **~30M** | **$73-130/hr** |

### Free Tier Strategy (zero cost)

For users on Anthropic Max subscription (unlimited Claude Code usage):

| Component | How | Limitation |
|-----------|-----|-----------|
| N07 orchestrator | Claude Code (Max) | Unlimited |
| N01-N06 nuclei | Claude Code (Max) | Unlimited |
| Sub-agents | Agent tool (included) | Unlimited |

**Throughput on Max**: Full speed, zero marginal cost.
**Full CEX from zero on Max**: ~3-4 hours.

For users without Max (API billing):

| Nucleus | Model | Cost/hr est. |
|---------|-------|-------------|
| N07 | Opus | $7.50 |
| N01-N06 | Mixed Opus/Sonnet | $30-60 |
| Sub-agents | Haiku/Sonnet | $3-36 |
| **Total** | -- | **$40-100/hr** |

### Fine-Tuned Models

A CEX-specific fine-tuned model would be the endgame:

| What to fine-tune on | Output | Use for |
|---------------------|--------|---------|
| 1,630 builder ISOs | FT that generates ISOs from kind name | T3 sub-agent for batch ISO generation |
| 123 kind KCs | FT that generates KCs from kind schema | T3 sub-agent for batch KC generation |
| 377 templates + examples | FT that fills templates from intent | T3 sub-agent for template filling |

**How**: Export training pairs (input=kind+schema, output=artifact) -> fine-tune on OpenAI or Hugging Face -> use via API endpoint.

Then reference in Agent tool:
```markdown
Agent({
  model: "haiku",  // or custom endpoint if supported
  subagent_type: "knowledge-card-builder",
  prompt: "Build KC for {kind} using template..."
})
```

### Model Selection in nucleus_models.yaml

The existing config supports per-nucleus model routing:

```yaml
n03:
  cli: claude
  model: opus-4-6          # Main process: T1
  context: 1000000
  sub_agents:               # Per-nucleus sub-agent config
    builder_iso:
      model: sonnet         # T2: standard generation via Agent tool
    formatter:
      model: haiku          # T3: mechanical
    compiler:
      model: haiku          # T3: validation
  fallback:
    cli: claude
    model: sonnet-4-6
```

### Router Decision Matrix

`cex_router.py` exists with health checks + fallback chains.
Extend it with task-complexity routing:

| Task complexity | Signal | Route to |
|----------------|--------|----------|
| **Complex** (new kind, architecture, research) | unknown kind, no template match, >3 sections | T1 Opus |
| **Standard** (ISO from template, KC from schema) | template match >60%, known kind | T2 Sonnet |
| **Mechanical** (rename, format, compile, validate) | no generation needed, find-replace | T3 Haiku |

```python
# In cex_router.py
def route_task(self, task: dict) -> str:
    if task.get("template_match", 0) < 0.6:
        return "T1"  # needs reasoning
    if task.get("is_mechanical", False):
        return "T3"  # cheap model
    return "T2"  # standard execution
```

## Throughput at Peak

| Config | Streams | Tokens/hr | Artifacts/hr | Cost/hr | Time full build |
|--------|---------|-----------|-------------|---------|----------------|
| 6 nuclei solo (all Opus) | 6 | 6M | 180 | $90 | 15h |
| 6 nuclei x4 sub (all Opus) | 24 | 24M | 720 | $360 | 3.8h |
| 6 nuclei x4 sub (mixed tiers) | 24 | 24M | 720 | $73-130 | 3.8h |
| + continuous batching (mixed) | 24 | 30M | 864 | $90-150 | 3.2h |
| Max subscription (unlimited) | 24 | 30M | 864 | $0 marginal | 3.2h |
| With CEX fine-tuned model | 24 | 30M | 1000+ | $30-50 | 2.5h |

## Human intervention required

Zero (after `/mission start`).
