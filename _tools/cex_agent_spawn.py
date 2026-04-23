#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Agent Spawn -- Fork/Spawn dual-mode dispatch for nuclei.

Pattern: OpenClaude AgentTool (forkSubagent.ts, runAgent.ts)
Adapted for CEX nucleus dispatch with structured lifecycle management.

Modes:
  SPAWN  -- Fresh context. Worker starts cold, needs full briefing.
  FORK   -- Inherited context. Worker continues from parent's state (directive only).

Lifecycle:
  spawn/fork -> running -> completed | failed | stopped
                  |
                  +-> continue (send_message) -> running -> ...

Usage:
    from cex_agent_spawn import get_spawner, SpawnMode

    spawner = get_spawner()
    wid = spawner.spawn("n03", "Build homepage hero section", mode=SpawnMode.SPAWN)
    result = spawner.wait_for(wid, timeout=300)
    print(result.summary)

CLI:
    python cex_agent_spawn.py --spawn n03 "task description"
    python cex_agent_spawn.py --status
    python cex_agent_spawn.py --stop <worker_id>
    python cex_agent_spawn.py --send <worker_id> "follow-up message"
"""

import argparse
import json
import os
import subprocess
import sys
import time
import uuid
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

import yaml

ROOT = Path(__file__).resolve().parent.parent
RUNTIME_DIR = ROOT / ".cex" / "runtime"
HANDOFF_DIR = RUNTIME_DIR / "handoffs"
SIGNAL_DIR = RUNTIME_DIR / "signals"
PID_DIR = RUNTIME_DIR / "pids"
WORKTREE_DIR = ROOT / ".cex" / "worktrees"
SPAWN_DIR = ROOT / "_spawn"

VALID_NUCLEI = {"n01", "n02", "n03", "n04", "n05", "n06", "n07"}


class SpawnMode(str, Enum):
    SPAWN = "spawn"   # Fresh context, full briefing needed
    FORK = "fork"     # Inherited context, directive only


class Isolation(str, Enum):
    DEFAULT = "default"       # Same worktree
    WORKTREE = "worktree"     # Git worktree (parallel-safe writes)


class WorkerStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    STOPPED = "stopped"


@dataclass
class WorkerState:
    """Tracked state of a dispatched worker."""
    worker_id: str
    nucleus: str
    mode: str                    # spawn | fork
    isolation: str = "default"
    status: str = "pending"
    pid: int = 0
    started_at: float = 0.0
    completed_at: float = 0.0
    task_summary: str = ""
    continuations: int = 0       # Number of send_message calls

    @property
    def elapsed_ms(self) -> int:
        end = self.completed_at or time.time()
        return int((end - self.started_at) * 1000)

    @property
    def is_alive(self) -> bool:
        return self.status in ("pending", "running")


@dataclass
class TaskNotification:
    """Structured result from a completed worker.

    Pattern: OpenClaude <task-notification> XML format.
    """
    task_id: str
    status: str                  # completed | failed | killed
    summary: str
    result: str = ""
    nucleus: str = ""
    quality_score: float = 0.0
    total_tokens: int = 0
    tool_uses: int = 0
    duration_ms: int = 0
    continuations: int = 0

    def to_dict(self) -> dict:
        return asdict(self)

    def to_yaml(self) -> str:
        return yaml.dump(self.to_dict(), default_flow_style=False)


# ---------------------------------------------------------------------------
# Fork Child Protocol (from OpenClaude buildChildMessage)
# ---------------------------------------------------------------------------

FORK_CHILD_RULES = """[FORK-CHILD] You are a forked worker process. NOT the main agent.

RULES:
1. You ARE the fork. Do NOT spawn sub-agents. Execute directly.
2. Do NOT converse, ask questions, or suggest next steps.
3. USE tools directly: read, write, compile, validate.
4. If modifying files, commit changes before reporting. Include the commit hash.
5. Do NOT emit text between tool calls. Use tools, then report once at the end.
6. Stay strictly within your directive's scope.
7. Keep your report under 500 words unless told otherwise.
8. Your response MUST begin with "Scope:". No preamble.

Output format:
  Scope: <echo your scope in one sentence>
  Result: <key findings or changes>
  Key files: <relevant file paths>
  Files changed: <list with commit hash, if any>
  Issues: <only if there are issues to flag>
"""


class AgentSpawner:
    """Manages worker lifecycle: spawn, fork, continue, stop, wait."""

    def __init__(self):
        self.workers: Dict[str, WorkerState] = {}
        self._ensure_dirs()
        self._load_active_workers()

    def _ensure_dirs(self):
        for d in (HANDOFF_DIR, SIGNAL_DIR, PID_DIR):
            d.mkdir(parents=True, exist_ok=True)

    def _load_active_workers(self):
        """Recover active workers from handoff files."""
        for hf in HANDOFF_DIR.glob("worker_*.yaml"):
            try:
                data = yaml.safe_load(hf.read_text(encoding="utf-8"))
                if data and isinstance(data, dict):
                    wid = data.get("worker_id", hf.stem)
                    if wid not in self.workers:
                        self.workers[wid] = WorkerState(
                            worker_id=wid,
                            nucleus=data.get("nucleus", ""),
                            mode=data.get("mode", "spawn"),
                            status=data.get("status", "running"),
                            started_at=data.get("created_at", 0),
                        )
            except Exception:
                pass

    # ------------------------------------------------------------------
    # SPAWN
    # ------------------------------------------------------------------

    def spawn(
        self,
        nucleus: str,
        task_spec: str,
        mode: SpawnMode = SpawnMode.SPAWN,
        isolation: Isolation = Isolation.DEFAULT,
        mission: str = "",
    ) -> str:
        """Launch a new worker.

        SPAWN mode: Worker starts fresh. task_spec must be a self-contained briefing.
        FORK mode: Worker inherits context. task_spec is a short directive.

        Returns worker_id.
        """
        nucleus = nucleus.lower()
        if nucleus not in VALID_NUCLEI:
            raise ValueError(f"Invalid nucleus '{nucleus}'. Must be one of: {sorted(VALID_NUCLEI)}")

        # Guard: no fork-from-fork
        if mode == SpawnMode.FORK and self._is_inside_fork():
            raise RuntimeError("Cannot fork from inside a fork. Execute directly instead.")

        worker_id = f"worker_{nucleus}_{uuid.uuid4().hex[:8]}"

        # Build task content
        if mode == SpawnMode.FORK:
            full_spec = f"{FORK_CHILD_RULES}\n\nDIRECTIVE: {task_spec}"
        else:
            full_spec = task_spec

        # Write handoff file
        handoff = {
            "worker_id": worker_id,
            "nucleus": nucleus,
            "mode": mode.value,
            "isolation": isolation.value,
            "mission": mission,
            "task_spec": full_spec,
            "created_at": time.time(),
            "status": "pending",
        }
        handoff_path = HANDOFF_DIR / f"{worker_id}.yaml"
        handoff_path.write_text(
            yaml.dump(handoff, default_flow_style=False, allow_unicode=True),
            encoding="utf-8",
        )

        # Also write as n0X_task.md for dispatch.sh compatibility
        task_path = HANDOFF_DIR / f"{nucleus}_task.md"
        task_md = """---
worker_id: {worker_id}
nucleus: {nucleus}
mode: {mode.value}
mission: {mission}
created_at: {time.strftime('%Y-%m-%dT%H:%M:%S')}
---

# Task for {nucleus.upper()}

{full_spec}
"""
        task_path.write_text(task_md, encoding="utf-8")

        # Setup isolation
        worktree_path = None
        if isolation == Isolation.WORKTREE:
            worktree_path = self._create_worktree(worker_id)

        # Dispatch
        cwd = worktree_path or str(ROOT)
        pid = self._launch_nucleus(nucleus, worker_id, cwd)

        # Track
        state = WorkerState(
            worker_id=worker_id,
            nucleus=nucleus,
            mode=mode.value,
            isolation=isolation.value,
            status="running",
            pid=pid,
            started_at=time.time(),
            task_summary=task_spec[:100],
        )
        self.workers[worker_id] = state
        self._save_pid(worker_id, pid)

        return worker_id

    # ------------------------------------------------------------------
    # SEND MESSAGE (continue existing worker)
    # ------------------------------------------------------------------

    def send_message(self, worker_id: str, message: str):
        """Continue an existing worker with follow-up instruction.

        Pattern: OpenClaude SendMessage -- worker resumes with full context preserved.
        Use this when the worker's context overlaps with the next task.
        """
        state = self.workers.get(worker_id)
        if not state:
            raise ValueError(f"Unknown worker: {worker_id}")
        if not state.is_alive:
            raise ValueError(f"Worker {worker_id} is {state.status}, cannot send message")

        # Append continuation to handoff
        handoff_path = HANDOFF_DIR / f"{worker_id}.yaml"
        continuation = {
            "type": "continuation",
            "message": message,
            "sent_at": time.time(),
            "continuation_number": state.continuations + 1,
        }

        with open(handoff_path, "a", encoding="utf-8") as f:
            f.write(f"\n---\n{yaml.dump(continuation, default_flow_style=False)}")

        # Also update n0X_task.md
        task_path = HANDOFF_DIR / f"{state.nucleus}_task.md"
        if task_path.exists():
            with open(task_path, "a", encoding="utf-8") as f:
                f.write(f"\n\n---\n## Continuation #{state.continuations + 1}\n\n{message}\n")

        state.continuations += 1

        # Signal worker to read continuation
        self._write_control_signal(worker_id, "continue")

    # ------------------------------------------------------------------
    # STOP
    # ------------------------------------------------------------------

    def stop(self, worker_id: str):
        """Stop a misdirected worker."""
        state = self.workers.get(worker_id)
        if state and state.pid:
            self._kill_process(state.pid)

        self._write_control_signal(worker_id, "stop")

        if state:
            state.status = "stopped"
            state.completed_at = time.time()

    def stop_all(self):
        """Stop all active workers."""
        for wid, state in self.workers.items():
            if state.is_alive:
                self.stop(wid)

    # ------------------------------------------------------------------
    # WAIT
    # ------------------------------------------------------------------

    def wait_for(self, worker_id: str, timeout: float = 300) -> TaskNotification:
        """Block until a single worker completes.

        Polls signal directory for completion.
        Returns TaskNotification with result.
        """
        state = self.workers.get(worker_id)
        if not state:
            return TaskNotification(task_id=worker_id, status="failed", summary="Unknown worker")

        start = time.time()
        while time.time() - start < timeout:
            notif = self._check_signal(state)
            if notif:
                state.status = notif.status
                state.completed_at = time.time()
                return notif

            # Check if process died
            if state.pid and not self._is_pid_alive(state.pid):
                state.status = "failed"
                state.completed_at = time.time()
                return TaskNotification(
                    task_id=worker_id,
                    status="failed",
                    summary=f"Process {state.pid} died without signaling",
                    nucleus=state.nucleus,
                    duration_ms=state.elapsed_ms,
                )

            time.sleep(5)

        # Timeout
        self.stop(worker_id)
        return TaskNotification(
            task_id=worker_id,
            status="killed",
            summary=f"Timeout after {timeout:.0f}s",
            nucleus=state.nucleus,
            duration_ms=state.elapsed_ms,
        )

    def wait_all(
        self,
        worker_ids: List[str],
        timeout: float = 600,
    ) -> List[TaskNotification]:
        """Wait for multiple workers (parallel polling).

        Returns results in same order as worker_ids.
        """
        results: Dict[str, TaskNotification] = {}
        pending = set(worker_ids)
        start = time.time()

        while pending and (time.time() - start) < timeout:
            for wid in list(pending):
                state = self.workers.get(wid)
                if not state:
                    results[wid] = TaskNotification(task_id=wid, status="failed", summary="Unknown")
                    pending.remove(wid)
                    continue

                notif = self._check_signal(state)
                if notif:
                    results[wid] = notif
                    state.status = notif.status
                    state.completed_at = time.time()
                    pending.remove(wid)
                elif state.pid and not self._is_pid_alive(state.pid):
                    results[wid] = TaskNotification(
                        task_id=wid, status="failed",
                        summary="Process died", nucleus=state.nucleus,
                    )
                    state.status = "failed"
                    state.completed_at = time.time()
                    pending.remove(wid)

            if pending:
                time.sleep(5)

        # Kill remaining
        for wid in pending:
            self.stop(wid)
            results[wid] = TaskNotification(
                task_id=wid, status="killed",
                summary=f"Timeout after {timeout:.0f}s",
                nucleus=self.workers[wid].nucleus if wid in self.workers else "",
            )

        return [results.get(wid, TaskNotification(task_id=wid, status="failed", summary="Missing"))
                for wid in worker_ids]

    # ------------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------------

    def status(self) -> List[dict]:
        """Status of all tracked workers."""
        rows = []
        for wid, state in self.workers.items():
            rows.append({
                "worker_id": wid,
                "nucleus": state.nucleus,
                "mode": state.mode,
                "status": state.status,
                "elapsed_s": state.elapsed_ms // 1000,
                "continuations": state.continuations,
                "pid": state.pid,
            })
        return rows

    # ------------------------------------------------------------------
    # INTERNALS
    # ------------------------------------------------------------------

    def _launch_nucleus(self, nucleus: str, worker_id: str, cwd: str) -> int:
        """Launch nucleus via dispatch.sh."""
        dispatch_script = SPAWN_DIR / "dispatch.sh"
        if not dispatch_script.exists():
            raise FileNotFoundError(f"dispatch.sh not found at {dispatch_script}")

        try:
            proc = subprocess.Popen(
                ["bash", str(dispatch_script), "solo", nucleus, worker_id],
                cwd=cwd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0),
            )
            return proc.pid
        except Exception as e:
            # Fallback: record the error
            return 0

    def _create_worktree(self, worker_id: str) -> Optional[str]:
        """Create isolated git worktree for parallel-safe writes."""
        WORKTREE_DIR.mkdir(parents=True, exist_ok=True)
        wt_path = str(WORKTREE_DIR / worker_id)
        try:
            subprocess.run(
                ["git", "worktree", "add", "--detach", wt_path],
                cwd=str(ROOT),
                check=True,
                capture_output=True,
            )
            return wt_path
        except subprocess.CalledProcessError:
            return None

    def _save_pid(self, worker_id: str, pid: int):
        """Append worker PID to tracking file (atomic write, no lock file race)."""
        pid_file = PID_DIR / "spawn_pids.txt"
        pid_line = f"{pid} {worker_id}\n"
        PID_DIR.mkdir(parents=True, exist_ok=True)
        # Atomic read-append-replace: avoids stale .lock race on crash
        import tempfile
        for _attempt in range(5):
            try:
                existing = ""
                if pid_file.exists():
                    existing = pid_file.read_text(encoding="utf-8")
                updated = existing + pid_line
                fd, tmp_path = tempfile.mkstemp(
                    dir=str(PID_DIR), prefix=".pid_tmp_", suffix=".txt"
                )
                try:
                    os.write(fd, updated.encode("utf-8"))
                    os.close(fd)
                    os.replace(tmp_path, str(pid_file))
                except BaseException:
                    try:
                        os.close(fd)
                    except OSError:
                        pass
                    try:
                        os.unlink(tmp_path)
                    except OSError:
                        pass
                    raise
                break
            except OSError:
                import time as _time
                _time.sleep(0.05)
        else:
            # Last resort: direct append to avoid data loss
            with open(pid_file, "a", encoding="utf-8") as f:
                f.write(pid_line)
                f.flush()

    def _check_signal(self, state: WorkerState) -> Optional[TaskNotification]:
        """Check if a signal file exists for this worker's nucleus."""
        # Check for worker-specific signal first
        worker_signal = SIGNAL_DIR / f"{state.worker_id}.yaml"
        if worker_signal.exists():
            return self._parse_signal_yaml(worker_signal, state)

        worker_signal_json = SIGNAL_DIR / f"{state.worker_id}.json"
        if worker_signal_json.exists():
            return self._parse_signal_json(worker_signal_json, state)

        # Check for nucleus signal (newer than worker start)
        for sig in sorted(SIGNAL_DIR.glob(f"signal_{state.nucleus}_*.json"),
                          key=lambda f: f.stat().st_mtime, reverse=True):
            if sig.stat().st_mtime >= state.started_at:
                return self._parse_signal_json(sig, state)

        return None

    def _parse_signal_json(self, path: Path, state: WorkerState) -> TaskNotification:
        """Parse a JSON signal file."""
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return TaskNotification(
                task_id=state.worker_id,
                status=data.get("status", "complete"),
                summary=f"Nucleus {state.nucleus} signaled {data.get('status', 'complete')}",
                nucleus=state.nucleus,
                quality_score=data.get("quality_score", 0),
                duration_ms=state.elapsed_ms,
                continuations=state.continuations,
            )
        except Exception:
            return TaskNotification(
                task_id=state.worker_id, status="completed",
                summary="Signal found but parse failed", nucleus=state.nucleus,
            )

    def _parse_signal_yaml(self, path: Path, state: WorkerState) -> TaskNotification:
        """Parse a YAML signal/notification file."""
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            return TaskNotification(
                task_id=data.get("task_id", state.worker_id),
                status=data.get("status", "completed"),
                summary=data.get("summary", ""),
                result=data.get("result", ""),
                nucleus=state.nucleus,
                quality_score=data.get("quality_score", 0),
                total_tokens=data.get("usage", {}).get("total_tokens", 0),
                tool_uses=data.get("usage", {}).get("tool_uses", 0),
                duration_ms=data.get("usage", {}).get("duration_ms", state.elapsed_ms),
                continuations=state.continuations,
            )
        except Exception:
            return TaskNotification(
                task_id=state.worker_id, status="completed",
                summary="YAML signal found but parse failed", nucleus=state.nucleus,
            )

    def _write_control_signal(self, worker_id: str, action: str):
        """Write a control signal for a worker."""
        path = SIGNAL_DIR / f"ctrl_{worker_id}.json"
        path.write_text(
            json.dumps({"worker_id": worker_id, "action": action, "at": time.time()}),
            encoding="utf-8",
        )

    def _is_inside_fork(self) -> bool:
        """Guard against recursive forking."""
        return os.getenv("CEX_FORK_CHILD") == "1"

    def _kill_process(self, pid: int):
        """Kill a process by PID (cross-platform)."""
        if not pid:
            return
        try:
            if sys.platform == "win32":
                subprocess.run(
                    ["taskkill", "/F", "/PID", str(pid)],
                    capture_output=True, timeout=10,
                )
            else:
                os.kill(pid, 9)
        except Exception:
            pass

    def _is_pid_alive(self, pid: int) -> bool:
        """Check if process is still running."""
        if not pid:
            return False
        try:
            if sys.platform == "win32":
                result = subprocess.run(
                    ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                    capture_output=True, text=True, timeout=5,
                )
                return str(pid) in result.stdout
            else:
                os.kill(pid, 0)
                return True
        except Exception:
            return False


# ---------------------------------------------------------------------------
# Extended signal_writer integration
# ---------------------------------------------------------------------------

def write_task_notification(
    worker_id: str,
    status: str,
    summary: str,
    result: str = "",
    nucleus: str = "",
    quality_score: float = 0.0,
    tokens: int = 0,
    tools: int = 0,
    duration_ms: int = 0,
):
    """Write a structured TaskNotification to signal dir.

    Use this at the end of a worker's execution to notify the coordinator.
    """
    SIGNAL_DIR.mkdir(parents=True, exist_ok=True)

    notification = {
        "task_id": worker_id,
        "status": status,
        "summary": summary,
        "result": result,
        "nucleus": nucleus,
        "quality_score": quality_score,
        "usage": {
            "total_tokens": tokens,
            "tool_uses": tools,
            "duration_ms": duration_ms,
        },
        "completed_at": time.time(),
    }

    path = SIGNAL_DIR / f"{worker_id}.yaml"
    path.write_text(
        yaml.dump(notification, default_flow_style=False, allow_unicode=True),
        encoding="utf-8",
    )
    return str(path)


# ---------------------------------------------------------------------------
# Singleton
# ---------------------------------------------------------------------------

_spawner: Optional[AgentSpawner] = None


def validate_agent_config(nucleus: str, task_spec: str) -> bool:
    """Validate that a nucleus + task_spec pair is valid for spawning."""
    nucleus = nucleus.lower()
    if nucleus not in VALID_NUCLEI:
        raise ValueError(f"Invalid nucleus '{nucleus}'. Must be one of: {sorted(VALID_NUCLEI)}")
    if not task_spec or not task_spec.strip():
        raise ValueError("task_spec cannot be empty")
    return True


def get_spawner() -> AgentSpawner:
    """Get the singleton spawner."""
    global _spawner
    if _spawner is None:
        _spawner = AgentSpawner()
    return _spawner


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="CEX Agent Spawn")
    parser.add_argument("--spawn", nargs=2, metavar=("NUCLEUS", "TASK"), help="Spawn a worker")
    parser.add_argument("--fork", nargs=2, metavar=("NUCLEUS", "DIRECTIVE"), help="Fork a worker")
    parser.add_argument("--send", nargs=2, metavar=("WORKER_ID", "MESSAGE"), help="Continue a worker")
    parser.add_argument("--stop", metavar="WORKER_ID", help="Stop a worker")
    parser.add_argument("--stop-all", action="store_true", help="Stop all workers")
    parser.add_argument("--status", action="store_true", help="Show worker status")
    parser.add_argument("--worktree", action="store_true", help="Use git worktree isolation")
    args = parser.parse_args()

    spawner = get_spawner()

    if args.spawn:
        nucleus, task = args.spawn
        iso = Isolation.WORKTREE if args.worktree else Isolation.DEFAULT
        wid = spawner.spawn(nucleus, task, mode=SpawnMode.SPAWN, isolation=iso)
        print(f"Spawned: {wid}")

    elif args.fork:
        nucleus, directive = args.fork
        wid = spawner.spawn(nucleus, directive, mode=SpawnMode.FORK)
        print(f"Forked: {wid}")

    elif args.send:
        worker_id, message = args.send
        spawner.send_message(worker_id, message)
        print(f"Message sent to {worker_id}")

    elif args.stop:
        spawner.stop(args.stop)
        print(f"Stopped: {args.stop}")

    elif args.stop_all:
        spawner.stop_all()
        print("All workers stopped")

    elif args.status:
        rows = spawner.status()
        if not rows:
            print("No active workers")
        else:
            print(f"\n{'Worker ID':35s} {'Nuc':4s} {'Mode':6s} {'Status':10s} {'Time':>7s} {'Cont':>4s}")
            print("-" * 72)
            for r in rows:
                print(
                    f"{r['worker_id']:35s} {r['nucleus']:4s} {r['mode']:6s} "
                    f"{r['status']:10s} {r['elapsed_s']:>6d}s {r['continuations']:>4d}"
                )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
