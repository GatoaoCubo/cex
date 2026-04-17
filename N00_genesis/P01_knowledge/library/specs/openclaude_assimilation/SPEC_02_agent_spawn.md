---
id: spec_02_agent_spawn
kind: spec
pillar: P01
title: "SPEC_02: Agent Fork/Spawn → Dispatch System"
version: 1.0.0
status: active
created: 2026-04-05
quality: 9.0
depends_on: [SPEC_05, SPEC_06]
target_files:
  - _spawn/dispatch.sh
  - _tools/cex_agent_spawn.py (NEW)
  - _tools/cex_crew_runner.py
  - _tools/signal_writer.py
---

# SPEC_02: Agent Fork/Spawn → Dispatch System

## Pattern Harvested

OpenClaude has a **dual-mode agent system**: `spawn` (fresh context) vs `fork` (inherited context).
This maps directly to CEX's need for both "cold start" nucleus dispatch and "warm continuation".

### Key Patterns from AgentTool

```pseudocode
# 1. FORK vs SPAWN decision
if subagent_type is None:
    mode = FORK          # Inherits parent's full conversation
    tools = parent.tools # Identical tool pool (cache sharing)
    prompt = directive   # Short: "what to do" not "what's going on"
else:
    mode = SPAWN         # Fresh context, zero knowledge
    tools = resolve_agent_tools(definition)
    prompt = full_spec   # Self-contained briefing

# 2. Fork child rules (buildChildMessage)
FORK_RULES = """
1. You ARE the fork. Do NOT spawn sub-agents.
2. Do NOT converse or ask questions.
3. USE tools directly: Bash, Read, Write.
4. If modifying files, commit before reporting.
5. Stay within scope.
6. Report under 500 words.
7. Output: Scope → Result → Key files → Files changed → Issues
"""

# 3. Recursive fork guard
if is_in_fork_child(messages):
    reject("Cannot fork from inside a fork")

# 4. Worker isolation modes
isolation = "default" | "worktree" | "remote"
# worktree = git worktree (isolated copy, auto-cleanup)
# remote = separate environment (background)

# 5. Result notification format
<task-notification>
  <task-id>{id}</task-id>
  <status>completed|failed|killed</status>
  <summary>{human-readable}</summary>
  <result>{agent's final response}</result>
  <usage>
    <total_tokens>N</total_tokens>
    <tool_uses>N</tool_uses>
    <duration_ms>N</duration_ms>
  </usage>
</task-notification>
```

### Agent Lifecycle

```
spawn/fork → run(tools, prompt) → yield messages → notify parent → cleanup
                                    ↑                    │
                                    └── retry on fail ───┘
```

### Continue vs Re-spawn Decision Matrix

| Situation | Action | Why |
|-----------|--------|-----|
| Research → same-area implementation | Continue (SendMessage) | Worker has file context |
| Broad research → narrow implementation | Fresh spawn | Avoid noise |
| Correcting a failure | Continue | Worker has error context |
| Verifying another worker's code | Fresh spawn | Fresh eyes |
| Wrong approach entirely | Fresh spawn | Clean slate |

## CEX Adaptation

### What Changes

| Component | Current | After |
|-----------|---------|-------|
| dispatch.sh | PowerShell→process spawn | Python orchestrated + PS fallback |
| Worker tracking | PID files only | Structured WorkerState + notifications |
| Continuation | Not supported | SendMessage equivalent via handoffs |
| Isolation | None | Git worktree mode for parallel writes |
| Notifications | signal_writer (minimal) | Structured task-notification |

### New: `_tools/cex_agent_spawn.py`

```python
"""CEX Agent Spawn — Fork/Spawn dual-mode dispatch for nuclei."""

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
import subprocess, json, time, uuid

class SpawnMode(Enum):
    SPAWN = "spawn"   # Fresh context, full briefing needed
    FORK = "fork"     # Inherited context, directive only

class Isolation(Enum):
    DEFAULT = "default"     # Same worktree
    WORKTREE = "worktree"   # Git worktree (parallel-safe)

@dataclass
class WorkerState:
    worker_id: str
    nucleus: str
    mode: SpawnMode
    isolation: Isolation
    status: str = "pending"    # pending → running → completed|failed|stopped
    pid: int = 0
    started_at: float = 0.0
    completed_at: float = 0.0
    result_summary: str = ""
    token_usage: int = 0
    tool_uses: int = 0

@dataclass 
class TaskNotification:
    """Structured result from a completed worker."""
    task_id: str
    status: str            # completed | failed | killed
    summary: str
    result: str = ""
    total_tokens: int = 0
    tool_uses: int = 0
    duration_ms: int = 0
    
    def to_yaml(self) -> str:
        return yaml.dump(asdict(self), default_flow_style=False)

class AgentSpawner:
    """Manages worker lifecycle: spawn, fork, continue, stop."""
    
    RUNTIME_DIR = Path(".cex/runtime")
    
    def __init__(self):
        self.workers: dict[str, WorkerState] = {}
        self._load_active_workers()
    
    def spawn(self, nucleus: str, task_spec: str, 
              mode: SpawnMode = SpawnMode.SPAWN,
              isolation: Isolation = Isolation.DEFAULT) -> str:
        """Launch a new worker."""
        worker_id = f"{nucleus}_{uuid.uuid4().hex[:8]}"
        
        # Guard: no fork-from-fork
        if mode == SpawnMode.FORK and self._is_inside_fork():
            raise RuntimeError("Cannot fork from inside a fork")
        
        # Create handoff
        handoff = {
            "worker_id": worker_id,
            "nucleus": nucleus,
            "mode": mode.value,
            "task_spec": task_spec,
            "isolation": isolation.value,
            "created_at": time.time(),
        }
        handoff_path = self.RUNTIME_DIR / "handoffs" / f"{worker_id}.yaml"
        handoff_path.parent.mkdir(parents=True, exist_ok=True)
        handoff_path.write_text(yaml.dump(handoff))
        
        # Setup isolation
        worktree_path = None
        if isolation == Isolation.WORKTREE:
            worktree_path = self._create_worktree(worker_id)
        
        # Dispatch
        cwd = worktree_path or "."
        pid = self._launch_nucleus(nucleus, worker_id, task_spec, cwd)
        
        # Track
        state = WorkerState(
            worker_id=worker_id, nucleus=nucleus, mode=mode,
            isolation=isolation, status="running", pid=pid,
            started_at=time.time()
        )
        self.workers[worker_id] = state
        self._save_pid(worker_id, pid)
        
        return worker_id
    
    def send_message(self, worker_id: str, message: str):
        """Continue an existing worker (warm context)."""
        if worker_id not in self.workers:
            raise ValueError(f"Unknown worker: {worker_id}")
        
        # Append continuation to handoff
        handoff_path = self.RUNTIME_DIR / "handoffs" / f"{worker_id}.yaml"
        continuation = {
            "type": "continuation",
            "message": message,
            "sent_at": time.time(),
        }
        with open(handoff_path, "a") as f:
            f.write(f"\n---\n{yaml.dump(continuation)}")
        
        # Signal worker to read continuation
        self._signal(worker_id, "continue")
    
    def stop(self, worker_id: str):
        """Stop a misdirected worker."""
        state = self.workers.get(worker_id)
        if state and state.pid:
            self._kill_process(state.pid)
        self._signal(worker_id, "stop")
        if state:
            state.status = "stopped"
    
    def wait_for(self, worker_id: str, timeout: float = 300) -> TaskNotification:
        """Block until worker completes."""
        # Poll signal file
        signal_path = self.RUNTIME_DIR / "signals" / f"{worker_id}.yaml"
        start = time.time()
        while time.time() - start < timeout:
            if signal_path.exists():
                return self._parse_notification(signal_path)
            time.sleep(2)
        
        # Timeout
        self.stop(worker_id)
        return TaskNotification(
            task_id=worker_id, status="killed",
            summary=f"Timeout after {timeout}s"
        )
    
    def wait_all(self, worker_ids: list[str], 
                 timeout: float = 600) -> list[TaskNotification]:
        """Wait for multiple workers (parallel polling)."""
        results = {}
        start = time.time()
        pending = set(worker_ids)
        
        while pending and (time.time() - start) < timeout:
            for wid in list(pending):
                signal_path = self.RUNTIME_DIR / "signals" / f"{wid}.yaml"
                if signal_path.exists():
                    results[wid] = self._parse_notification(signal_path)
                    pending.remove(wid)
            if pending:
                time.sleep(2)
        
        # Kill remaining
        for wid in pending:
            self.stop(wid)
            results[wid] = TaskNotification(
                task_id=wid, status="killed", summary="Timeout"
            )
        
        return [results[wid] for wid in worker_ids]
    
    def _create_worktree(self, worker_id: str) -> str:
        """Create isolated git worktree for parallel-safe writes."""
        path = f".cex/worktrees/{worker_id}"
        subprocess.run(
            ["git", "worktree", "add", "--detach", path],
            check=True, capture_output=True
        )
        return path
    
    def _launch_nucleus(self, nucleus, worker_id, task_spec, cwd) -> int:
        """Launch nucleus process."""
        proc = subprocess.Popen(
            ["bash", "_spawn/dispatch.sh", "solo", nucleus, worker_id],
            cwd=cwd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return proc.pid
```

### Modified: `signal_writer.py`

Add TaskNotification format:

```python
def write_task_notification(worker_id, status, summary, result="", 
                            tokens=0, tools=0, duration_ms=0):
    """Write structured task notification (OpenClaude pattern)."""
    notification = {
        "task_id": worker_id,
        "status": status,
        "summary": summary,
        "result": result,
        "usage": {
            "total_tokens": tokens,
            "tool_uses": tools,
            "duration_ms": duration_ms,
        },
        "completed_at": time.time(),
    }
    path = SIGNAL_DIR / f"{worker_id}.yaml"
    path.write_text(yaml.dump(notification))
```

## Acceptance Criteria

1. ✅ `AgentSpawner` supports both SPAWN and FORK modes
2. ✅ `send_message` enables warm continuation of existing workers
3. ✅ `stop` kills misdirected workers gracefully
4. ✅ Fork-from-fork guard prevents recursive spawning
5. ✅ Git worktree isolation for parallel writes
6. ✅ Structured TaskNotification replaces raw signals
7. ✅ `wait_all` enables parallel research patterns
8. ✅ Existing `dispatch.sh` remains functional (backward compat)

## 8F Impact

- **F5 CALL**: Spawner becomes a first-class tool in the pipeline
- **F7 GOVERN**: Notifications include token usage for cost tracking
- **F8 COLLABORATE**: Richer signals enable coordinator synthesis
