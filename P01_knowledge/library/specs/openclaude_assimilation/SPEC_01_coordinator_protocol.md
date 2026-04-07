---
kind: spec
pillar: P01
title: "SPEC_01: Coordinator Protocol → N07 Orchestrator"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
depends_on: [SPEC_02, SPEC_05, SPEC_06]
target_files:
  - _tools/cex_mission_runner.py
  - _tools/cex_coordinator.py (NEW)
  - .claude/rules/n07-orchestrator.md
---

# SPEC_01: Coordinator Protocol → N07 Orchestrator

## Pattern Harvested

OpenClaude's Coordinator Mode is a **role-switching protocol** where the main agent
becomes a pure delegator that NEVER executes tools directly — only spawns workers,
sends messages, and synthesizes results.

### Key Architectural Decisions (from coordinatorMode.ts)

```pseudocode
# 1. Role separation: coordinator vs worker
if COORDINATOR_MODE:
    tools = [Agent, SendMessage, TaskStop]  # NO Bash, Read, Write, Edit
    prompt = COORDINATOR_SYSTEM_PROMPT       # 6-section protocol
else:
    tools = ALL_TOOLS
    prompt = DEFAULT_PROMPT

# 2. Session mode matching (resume preserves mode)
function matchSessionMode(stored_mode):
    if current != stored → flip env var
    return warning_if_switched

# 3. Worker context injection
function getCoordinatorUserContext(mcp_clients, scratchpad):
    return { workerToolsContext: "Workers have: Bash, Read, Edit, ..." }
```

### The 6-Section Coordinator Protocol

1. **Your Role** — Coordinate, don't execute. Synthesize, don't delegate understanding.
2. **Your Tools** — Agent (spawn), SendMessage (continue), TaskStop (cancel)
3. **Workers** — Autonomous executors with full tool access
4. **Task Workflow** — Research → Synthesis → Implementation → Verification
5. **Writing Worker Prompts** — Self-contained specs, never "based on your findings"
6. **Example Session** — Concrete parallel-research → synthesize → implement flow

### Critical Anti-Pattern: "Never Delegate Understanding"

```
# BAD — lazy delegation
dispatch(worker, "Based on research findings, fix the bug")

# GOOD — synthesized spec
dispatch(worker, "Fix null pointer at src/auth/validate.ts:42. 
  Session.user is undefined when expired. Add null check before user.id.
  Return 401 'Session expired'.")
```

## CEX Adaptation

### What Changes

| Component | Current | After |
|-----------|---------|-------|
| N07 role | Rules-only (.md) | Rules + runtime coordinator class |
| Mission runner | Linear wave execution | Coordinator protocol with synthesis gates |
| Worker dispatch | Fire-and-forget | Spawn + monitor + continue/stop |
| Signal system | Complete/error only | + progress + synthesis-ready |

### New: `_tools/cex_coordinator.py`

```python
class CexCoordinator:
    """N07 Coordinator Protocol — never builds, only orchestrates."""
    
    COORDINATOR_TOOLS = ['dispatch', 'send_message', 'stop_task', 'status']
    
    def __init__(self, mission_id: str):
        self.mission_id = mission_id
        self.active_workers: dict[str, WorkerState] = {}
        self.synthesis_queue: list[WorkerResult] = []
    
    def spawn_worker(self, nucleus: str, task_spec: str, 
                     run_in_background: bool = True) -> str:
        """Dispatch to nucleus with self-contained spec."""
        worker_id = f"{nucleus}_{uuid4().hex[:8]}"
        # Write handoff file
        write_handoff(worker_id, nucleus, task_spec)
        # Launch via dispatch
        dispatch(nucleus, task_spec, worker_id)
        self.active_workers[worker_id] = WorkerState(
            nucleus=nucleus, status='running', started=now()
        )
        return worker_id
    
    def send_message(self, worker_id: str, message: str):
        """Continue existing worker with follow-up instruction."""
        append_to_handoff(worker_id, message)
        signal_worker(worker_id, 'continue')
    
    def stop_worker(self, worker_id: str):
        """Stop a misdirected worker."""
        signal_worker(worker_id, 'stop')
        self.active_workers[worker_id].status = 'stopped'
    
    def synthesize(self, worker_results: list[WorkerResult]) -> str:
        """N07's MOST IMPORTANT JOB: understand before dispatching next."""
        # Coordinator reads results, extracts:
        # - File paths mentioned
        # - Decisions made
        # - Gaps found
        # Then writes a synthesis that proves understanding
        return build_synthesis_spec(worker_results)
    
    def run_phase(self, phase: str, tasks: list[Task]):
        """Execute a workflow phase (research/implement/verify)."""
        if phase == 'research':
            # Parallel spawn — fan out
            for task in tasks:
                self.spawn_worker(task.nucleus, task.spec)
        elif phase == 'implement':
            # Sequential — one writer per file set
            for task in tasks:
                self.spawn_worker(task.nucleus, task.spec)
                self.wait_for(task.worker_id)
        elif phase == 'verify':
            # Fresh workers — no implementation bias
            for task in tasks:
                self.spawn_worker(task.nucleus, task.spec)
```

### Modified: `cex_mission_runner.py`

Add synthesis gate between waves:

```python
# Current: wave1 → wave2 → wave3 (linear)
# New: wave1(research) → SYNTHESIS_GATE → wave2(implement) → VERIFY_GATE → wave3(verify)

def run_mission_with_coordinator(mission):
    coord = CexCoordinator(mission.id)
    
    # Phase 1: Research (parallel)
    research_ids = []
    for task in mission.research_tasks:
        wid = coord.spawn_worker(task.nucleus, task.spec)
        research_ids.append(wid)
    
    # Wait + collect
    results = coord.wait_all(research_ids)
    
    # SYNTHESIS GATE — coordinator must prove understanding
    synthesis = coord.synthesize(results)
    if not synthesis.has_specific_file_paths():
        raise SynthesisError("Coordinator must cite specific files/lines")
    
    # Phase 2: Implement (from synthesis)
    for impl_spec in synthesis.implementation_specs:
        wid = coord.spawn_worker(impl_spec.nucleus, impl_spec.spec)
        result = coord.wait_for(wid)
        if result.failed:
            coord.send_message(wid, f"Fix: {result.error}")
    
    # Phase 3: Verify (fresh workers)
    for verify_task in synthesis.verification_tasks:
        coord.spawn_worker(verify_task.nucleus, verify_task.spec)
```

### Modified: `.claude/rules/n07-orchestrator.md`

Add coordinator protocol section referencing the 6-section pattern.

## Acceptance Criteria

1. ✅ `CexCoordinator` class exists with spawn/send/stop/synthesize
2. ✅ Mission runner uses synthesis gates between phases
3. ✅ N07 NEVER calls build tools directly (only dispatch)
4. ✅ Worker results arrive as structured notifications
5. ✅ Anti-pattern detection: rejects "based on findings" style delegation
6. ✅ Backward compatible: existing `dispatch.sh` still works
7. ✅ All existing tests pass (`cex_system_test.py`)

## 8F Impact

- **F4 REASON**: Coordinator adds a synthesis step before F6 — improves plan quality
- **F7 GOVERN**: New gate: "does spec cite specific paths?" 
- **F8 COLLABORATE**: Signals now include progress, not just complete/error
