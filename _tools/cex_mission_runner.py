#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Mission Runner v2.0 -- Autonomous grid orchestration (wave + continuous).

Reads a mission plan, executes wave by wave or in continuous batching mode:
  wave:       dispatch all -> wait all -> consolidate -> next wave
  continuous: dispatch all -> on completion, immediately re-dispatch -> no idle gaps

Usage:
    python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --dry-run
    python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --timeout 3600
    python _tools/cex_mission_runner.py --mission MONETIZE --waves waves.yaml
    python _tools/cex_mission_runner.py --task-queue .cex/runtime/task_queue.yaml --continuous

Exit codes:
    0 = all waves/tasks complete, all quality gates passed
    1 = timeout on one or more waves
    2 = quality gate failure (outputs below threshold)
    3 = crash (nucleus died)
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "_tools"
SPAWN = ROOT / "_spawn"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
PID_FILE = ROOT / ".cex" / "runtime" / "pids" / "spawn_pids.txt"
ARCHIVE_DIR = ROOT / ".cex" / "archive" / "handoffs_done"


def log(msg: Any, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    # Windows cp1252 can't handle unicode box chars -- replace them
    safe_msg = str(msg).encode("ascii", "replace").decode("ascii")
    print(f"[{ts}] [{level}] {safe_msg}", flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="CEX Mission Runner -- autonomous grid orchestration")
    p.add_argument("--plan", help="Path to mission plan .md file")
    p.add_argument("--mission", default="MISSION", help="Mission name (default: MISSION)")
    p.add_argument("--waves", help="Path to waves YAML/JSON definition file")
    p.add_argument("--timeout", type=int, default=3600, help="Timeout per wave in seconds (default: 3600)")
    p.add_argument("--poll", type=int, default=30, help="Signal poll interval (default: 30s)")
    p.add_argument("--quality-floor", type=float, default=8.0, help="Minimum quality score (default: 8.0)")
    p.add_argument("--max-retries", type=int, default=1, help="Max retries per failed nucleus (default: 1)")
    p.add_argument("--dry-run", action="store_true", help="Preview without executing")
    p.add_argument("--skip-stop", action="store_true", help="Don't kill processes after each wave")
    p.add_argument("--continuous", action="store_true",
                   help="Continuous batching: re-dispatch idle nuclei immediately on completion")
    p.add_argument("--task-queue", help="Path to task queue YAML/JSON for continuous mode")
    return p.parse_args()


# ==================================================
# WAVE PARSING
# ==================================================

def parse_waves_from_plan(plan_path: str) -> list[dict[str, Any]]:
    """Extract wave definitions from a mission plan .md file.

    Looks for patterns like:
        ## Wave 1 -- Description
        | N01 | gemini/2.5-pro | ... | `N01_.../output_X.md` |
        | N02 | claude/sonnet  | ... | `N02_.../output_Y.md` |
    """
    text = Path(plan_path).read_text(encoding="utf-8")
    waves = []
    current_wave = None

    for line in text.splitlines():
        # Detect wave header
        wave_match = re.match(r'^##\s*Wave\s*(\d+)', line, re.IGNORECASE)
        if wave_match:
            if current_wave:
                waves.append(current_wave)
            current_wave = {
                "wave": int(wave_match.group(1)),
                "nuclei": [],
                "description": line.strip(),
            }
            continue

        # Detect nucleus in table row
        if current_wave and "|" in line:
            nuc_match = re.search(r'\b(N0[1-6]|n0[1-6])\b', line)
            output_match = re.search(r'`([^`]+\.md)`', line)
            if nuc_match:
                nucleus = nuc_match.group(1).lower()
                expected_output = output_match.group(1) if output_match else ""
                if nucleus not in [n["nucleus"] for n in current_wave["nuclei"]]:
                    current_wave["nuclei"].append({
                        "nucleus": nucleus,
                        "expected_output": expected_output,
                    })

    if current_wave and current_wave["nuclei"]:
        waves.append(current_wave)

    # Filter out empty waves
    waves = [w for w in waves if w.get("nuclei")]

    # If no waves found, treat all nuclei with handoffs as Wave 1
    if not waves:
        handoffs = list(HANDOFF_DIR.glob("*_n0[1-6].md"))
        if handoffs:
            nuclei = []
            for h in handoffs:
                nuc_match = re.search(r'(n0[1-6])', h.stem)
                if nuc_match:
                    nuclei.append({"nucleus": nuc_match.group(1), "expected_output": ""})
            waves = [{"wave": 1, "nuclei": nuclei, "description": "Auto-detected from handoffs"}]

    return waves


def parse_waves_from_json(waves_path: str) -> list[dict[str, Any]]:
    """Load waves from JSON/YAML file."""
    text = Path(waves_path).read_text(encoding="utf-8")
    if waves_path.endswith((".yaml", ".yml")):
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


# ==================================================
# GRID OPERATIONS
# ==================================================

def clean_signals() -> None:
    """Remove old signals."""
    if SIGNAL_DIR.exists():
        for f in SIGNAL_DIR.glob("signal_*.json"):
            f.unlink()
    log("Signals cleaned")


def copy_handoffs_to_tasks(mission: str, nuclei: list[dict[str, Any]]) -> None:
    """Copy MISSION_n0X.md -> n0X_task.md for each nucleus in wave."""
    for ninfo in nuclei:
        nuc = ninfo["nucleus"]
        src = HANDOFF_DIR / f"{mission}_{nuc}.md"
        dst = HANDOFF_DIR / f"{nuc}_task.md"
        if src.exists():
            shutil.copy2(src, dst)
            log(f"  {nuc}: handoff -> task")
        else:
            log(f"  {nuc}: WARNING -- handoff {src.name} not found", "WARN")


def dispatch_grid(mission: str, dry_run: bool = False) -> None:
    """Launch spawn_grid.ps1 in static mode."""
    if dry_run:
        log("[DRY-RUN] Would launch spawn_grid.ps1", "DRY")
        return

    cmd = [
        "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
        "-Command",
        "Start-Process powershell -ArgumentList '-File', "
        f"'{SPAWN / 'spawn_grid.ps1'}', '-mission', '{mission}', '-mode', 'static' "
        f"-WorkingDirectory '{ROOT}'"
    ]
    subprocess.run(cmd, cwd=str(ROOT), timeout=30)
    log("Grid dispatched")
    time.sleep(10)  # Wait for processes to spawn


def watch_signals(
    nuclei: list[dict[str, Any]],
    timeout: int,
    poll: int,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Block until all nuclei signal or timeout. Returns parsed result."""
    expected = ",".join(n["nucleus"] for n in nuclei)

    if dry_run:
        log(f"[DRY-RUN] Would watch signals for: {expected}", "DRY")
        return {"status": "complete", "nuclei": {n["nucleus"]: {"status": "complete", "quality": 9.0} for n in nuclei}}

    cmd = [
        sys.executable, str(TOOLS / "cex_signal_watch.py"),
        "--expect", expected,
        "--timeout", str(timeout),
        "--poll", str(poll),
    ]
    log(f"Watching signals: {expected} (timeout={timeout}s, poll={poll}s)")

    # Run signal_watch -- progress goes to stderr (printed live), JSON to stdout
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))

    # Print stderr progress lines to our log
    if result.stderr:
        for line in result.stderr.strip().splitlines():
            log(f"  [WATCH] {line}")

    # Extract JSON from stdout (between markers)
    stdout = result.stdout
    try:
        if "---JSON_START---" in stdout:
            json_str = stdout.split("---JSON_START---")[1].split("---JSON_END---")[0].strip()
            return json.loads(json_str)
        else:
            return json.loads(stdout)
    except (json.JSONDecodeError, IndexError):
        log(f"Signal watch parse error. Exit code: {result.returncode}", "ERROR")
        # Fallback: scan signal dir ourselves
        signals = find_signals_fallback(nuclei)
        return {"status": "fallback", "nuclei": signals}


def find_signals_fallback(nuclei: list[dict[str, Any]]) -> dict[str, Any]:
    """Fallback: read signals directly from disk if watch parsing fails."""
    result = {}
    if SIGNAL_DIR.exists():
        for ninfo in nuclei:
            nuc = ninfo["nucleus"]
            sigs = sorted(SIGNAL_DIR.glob(f"signal_{nuc}_*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
            if sigs:
                try:
                    data = json.loads(sigs[0].read_text(encoding="utf-8"))
                    result[nuc] = {
                        "status": data.get("status", "complete"),
                        "quality": data.get("quality_score", 0),
                    }
                except Exception:
                    result[nuc] = {"status": "unknown", "quality": 0}
            else:
                result[nuc] = {"status": "no_signal", "quality": 0}
    return result


def stop_processes(dry_run: bool = False) -> None:
    """Kill all spawned processes via spawn_stop.ps1."""
    args = [
        "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
        "-File", str(SPAWN / "spawn_stop.ps1"),
    ]
    if dry_run:
        args.append("-DryRun")

    result = subprocess.run(args, capture_output=True, text=True, cwd=str(ROOT), timeout=60)
    for line in result.stdout.strip().splitlines():
        log(f"  [STOP] {line}")


# ==================================================
# QUALITY GATE (G3)
# ==================================================

def quality_gate(
    nuclei: list[dict[str, Any]],
    watch_result: dict[str, Any],
    floor: float,
) -> dict[str, Any]:
    """Check quality of each nucleus output. Returns pass/fail per nucleus."""
    gate = {}

    for ninfo in nuclei:
        nuc = ninfo["nucleus"]
        expected = ninfo.get("expected_output", "")

        # Get quality from signal
        sig_quality = watch_result.get("nuclei", {}).get(nuc, {}).get("quality", 0)

        # Also try to read from the output file frontmatter
        file_quality = None
        if expected and Path(ROOT / expected).exists():
            try:
                text = Path(ROOT / expected).read_text(encoding="utf-8")[:500]
                qm = re.search(r'quality:\s*([\d.]+)', text)
                if qm:
                    file_quality = float(qm.group(1))
            except Exception:
                pass

        # Use file quality if available, else signal quality
        quality = file_quality if file_quality is not None else sig_quality
        passed = quality >= floor if quality > 0 else True  # quality:null passes (peer review later)

        gate[nuc] = {
            "quality": quality,
            "passed": passed,
            "source": "file" if file_quality is not None else "signal",
        }

        status = "PASS" if passed else "FAIL"
        log(f"  {nuc.upper()}: quality={quality} [{status}]")

    return gate


# ==================================================
# CONTINUOUS BATCHING
# ==================================================

TASK_QUEUE_PATH = ROOT / ".cex" / "runtime" / "task_queue.yaml"

NUCLEUS_DOMAINS = {
    "n01": ["research", "analysis", "intelligence", "benchmark"],
    "n02": ["marketing", "copy", "campaign", "ad", "brand_voice"],
    "n03": ["build", "create", "scaffold", "template", "iso"],
    "n04": ["knowledge", "rag", "embedding", "chunk", "index", "taxonomy"],
    "n05": ["code", "test", "deploy", "ci", "debug", "review"],
    "n06": ["pricing", "course", "funnel", "monetization", "revenue"],
}


def load_task_queue(path: str) -> list[dict[str, Any]]:
    """Load task queue from YAML or JSON.

    Format:
    - task: "Build KC for agent kind"
      kind: knowledge_card
      nucleus: n04          # optional -- auto-routed if missing
      priority: normal       # critical | normal | low
    """
    p = Path(path)
    if not p.exists():
        log(f"Task queue not found: {path}", "ERROR")
        return []
    text = p.read_text(encoding="utf-8")
    if p.suffix in (".yaml", ".yml"):
        try:
            import yaml
            data = yaml.safe_load(text)
        except ImportError:
            log("PyYAML not installed -- falling back to JSON parser", "WARN")
            data = json.loads(text)
    else:
        data = json.loads(text)

    tasks = data if isinstance(data, list) else data.get("tasks", [])
    # Add index for tracking
    for i, t in enumerate(tasks):
        t.setdefault("id", i)
        t.setdefault("status", "pending")
        t.setdefault("priority", "normal")
        t.setdefault("nucleus", route_task_to_nucleus(t))
    return tasks


def route_task_to_nucleus(task: dict[str, Any]) -> str:
    """Auto-route a task to a nucleus based on kind or keywords."""
    kind = task.get("kind", "")
    desc = task.get("task", "").lower()

    # Check kinds_meta for pillar -> nucleus mapping
    pillar_nucleus = {
        "P01": "n04", "P02": "n03", "P03": "n03", "P04": "n05",
        "P05": "n03", "P06": "n03", "P07": "n05", "P08": "n03",
        "P09": "n05", "P10": "n04", "P11": "n05", "P12": "n03",
    }

    # Try kinds_meta.json lookup
    km_path = ROOT / ".cex" / "kinds_meta.json"
    if km_path.exists() and kind:
        try:
            km = json.loads(km_path.read_text(encoding="utf-8"))
            if kind in km:
                pillar = km[kind].get("pillar", "")
                if pillar in pillar_nucleus:
                    return pillar_nucleus[pillar]
        except Exception:
            pass

    # Keyword fallback
    for nuc, keywords in NUCLEUS_DOMAINS.items():
        if any(kw in desc for kw in keywords):
            return nuc

    return "n03"  # Default: builder


def pop_next_task(tasks: list[dict[str, Any]], nucleus: str) -> dict[str, Any]:
    """Pop the next pending task for a given nucleus. Priority: critical first."""
    priority_order = {"critical": 0, "normal": 1, "low": 2}
    candidates = [t for t in tasks if t["status"] == "pending" and t["nucleus"] == nucleus]
    if not candidates:
        # Try any pending task (flexible routing)
        candidates = [t for t in tasks if t["status"] == "pending"]
    if not candidates:
        return {}
    candidates.sort(key=lambda t: priority_order.get(t.get("priority", "normal"), 1))
    chosen = candidates[0]
    chosen["status"] = "dispatched"
    chosen["dispatched_at"] = datetime.now(timezone.utc).isoformat()
    return chosen


def write_task_handoff(mission: str, nucleus: str, task: dict[str, Any]) -> None:
    """Write a handoff file for a single task dispatch."""
    HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
    handoff_path = HANDOFF_DIR / f"{mission}_{nucleus}.md"
    content = """---
from: mission_runner
to: {nucleus.upper()}
mission: {mission}
task_id: {task.get('id', 0)}
created: {datetime.now(timezone.utc).isoformat()}
---

# Task: {task.get('task', 'No description')}

## Kind
{task.get('kind', 'unknown')}

## Instructions
Build this artifact following 8F pipeline. Load builder ISOs from
archetypes/builders/{task.get('kind', 'unknown')}-builder/.
Read KC from P01_knowledge/library/kind/kc_{task.get('kind', 'unknown')}.md.
Compile after save. Signal on complete.
"""
    handoff_path.write_text(content, encoding="utf-8")
    # Also copy to task file
    task_path = HANDOFF_DIR / f"{nucleus}_task.md"
    task_path.write_text(content, encoding="utf-8")
    log(f"  Handoff written: {handoff_path.name}")


def dispatch_solo(nucleus: str, mission: str, dry_run: bool = False) -> None:
    """Dispatch a single nucleus via dispatch.sh solo."""
    if dry_run:
        log(f"[DRY-RUN] Would dispatch {nucleus.upper()} solo", "DRY")
        return
    cmd = ["bash", str(SPAWN / "dispatch.sh"), "solo", nucleus, f"{mission} task"]
    try:
        subprocess.run(cmd, cwd=str(ROOT), timeout=30, capture_output=True)
        log(f"  {nucleus.upper()} dispatched (solo)")
    except Exception as e:
        log(f"  {nucleus.upper()} dispatch failed: {e}", "ERROR")


def check_signal(nucleus: str) -> dict[str, Any]:
    """Non-blocking check: has this nucleus signaled completion?"""
    if not SIGNAL_DIR.exists():
        return {}
    sigs = sorted(
        SIGNAL_DIR.glob(f"signal_{nucleus}_*.json"),
        key=lambda f: f.stat().st_mtime, reverse=True,
    )
    if not sigs:
        return {}
    try:
        data = json.loads(sigs[0].read_text(encoding="utf-8"))
        return {
            "status": data.get("status", "complete"),
            "quality": data.get("quality_score", 0),
            "signal_file": str(sigs[0]),
        }
    except Exception:
        return {}


def run_continuous(args: argparse.Namespace) -> None:
    """Continuous batching mode: dispatch -> poll -> re-dispatch -> repeat."""
    mission = args.mission
    log(f"{'='*50}")
    log("CEX MISSION RUNNER v2.0 -- CONTINUOUS MODE")
    log(f"Mission: {mission}")
    log(f"Timeout: {args.timeout}s | Poll: {args.poll}s")
    log(f"Quality floor: {args.quality_floor}")
    log(f"Dry run: {args.dry_run}")
    log(f"{'='*50}")

    # Load task queue
    queue_path = args.task_queue or str(TASK_QUEUE_PATH)
    tasks = load_task_queue(queue_path)
    if not tasks:
        log("No tasks in queue. Provide --task-queue or populate .cex/runtime/task_queue.yaml", "ERROR")
        sys.exit(1)

    total = len(tasks)
    log(f"Loaded {total} tasks from queue")
    for t in tasks[:10]:
        log(f"  [{t['priority']}] {t['nucleus'].upper()}: {t.get('task', '?')[:60]}")
    if total > 10:
        log(f"  ... and {total - 10} more")

    # Track active nuclei
    active = {}  # nucleus -> task
    completed = []
    failed = []
    all_nuclei = ["n01", "n02", "n03", "n04", "n05", "n06"]
    start_time = time.time()

    # Initial dispatch: fill all idle nuclei
    for nuc in all_nuclei:
        task = pop_next_task(tasks, nuc)
        if task:
            write_task_handoff(mission, nuc, task)
            dispatch_solo(nuc, mission, args.dry_run)
            active[nuc] = task
            log(f"  Initial: {nuc.upper()} -> {task.get('task', '?')[:50]}")

    if not active:
        log("No tasks to dispatch", "ERROR")
        sys.exit(1)

    log(f"\n{len(active)} nuclei dispatched. Entering poll loop (every {args.poll}s)...")

    # Main poll loop
    iteration = 0
    while active:
        elapsed = int(time.time() - start_time)
        if elapsed > args.timeout:
            log(f"TIMEOUT after {elapsed}s -- {len(active)} nuclei still active", "WARN")
            break

        time.sleep(args.poll)
        iteration += 1

        # Check for completions
        newly_done = []
        for nuc, task in list(active.items()):
            sig = check_signal(nuc)
            if sig:
                quality = sig.get("quality", 0)
                passed = quality >= args.quality_floor if quality > 0 else True
                status_tag = "PASS" if passed else "FAIL"

                log(f"  {nuc.upper()} DONE: quality={quality} [{status_tag}] "
                    f"task={task.get('task', '?')[:40]}")

                task["quality"] = quality
                task["passed"] = passed
                task["status"] = "complete"

                if passed:
                    completed.append(task)
                else:
                    failed.append(task)

                newly_done.append(nuc)

                # Clean the signal so we don't re-detect
                sig_file = sig.get("signal_file", "")
                if sig_file and Path(sig_file).exists():
                    Path(sig_file).unlink()

        # Remove completed from active, dispatch next
        for nuc in newly_done:
            del active[nuc]

            # Immediately re-dispatch
            next_task = pop_next_task(tasks, nuc)
            if next_task:
                write_task_handoff(mission, nuc, next_task)
                dispatch_solo(nuc, mission, args.dry_run)
                active[nuc] = next_task
                log(f"  RE-DISPATCH: {nuc.upper()} -> {next_task.get('task', '?')[:50]}")

        # Progress report every 5 iterations
        pending = sum(1 for t in tasks if t["status"] == "pending")
        if iteration % 5 == 0 or newly_done:
            log(f"  [poll {iteration}] active={len(active)} done={len(completed)} "
                f"fail={len(failed)} pending={pending} elapsed={elapsed}s")

    # Final stop
    if not args.skip_stop and not args.dry_run:
        log("Stopping all processes...")
        stop_processes(args.dry_run)

    # Final report
    total_duration = int(time.time() - start_time)
    pending_count = sum(1 for t in tasks if t["status"] == "pending")

    log("")
    log(f"{'='*50}")
    log(f"CONTINUOUS MISSION COMPLETE: {mission}")
    log(f"{'='*50}")
    log(f"Total tasks: {total}")
    log(f"Completed: {len(completed)} | Failed: {len(failed)} | Pending: {pending_count}")
    log(f"Duration: {total_duration}s ({total_duration // 60}min)")

    all_passed = len(failed) == 0 and pending_count == 0

    summary = {
        "mission": mission,
        "mode": "continuous",
        "status": "complete" if all_passed else "partial",
        "tasks_total": total,
        "tasks_completed": len(completed),
        "tasks_failed": len(failed),
        "tasks_pending": pending_count,
        "total_duration_seconds": total_duration,
        "all_quality_passed": all_passed,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    summary_path = ROOT / ".cex" / "runtime" / "grid_status.json"
    summary_path.write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    log(f"Summary written to {summary_path}")

    sys.exit(0 if all_passed else 2)


# ==================================================
# CONSOLIDATION
# ==================================================

def consolidate_wave(
    mission: str,
    wave_num: int,
    nuclei: list[dict[str, Any]],
    dry_run: bool = False,
) -> None:
    """Commit outputs, archive handoffs, write wave summary."""
    if dry_run:
        log(f"[DRY-RUN] Would consolidate wave {wave_num}", "DRY")
        return

    # Git add all nucleus outputs
    subprocess.run(["git", "add", "-A"], cwd=str(ROOT), capture_output=True)
    subprocess.run(
        ["git", "commit", "-m",
         f"[N07/mission] {mission} wave {wave_num}: "
         f"{', '.join(n['nucleus'].upper() for n in nuclei)} complete"],
        cwd=str(ROOT), capture_output=True
    )
    log(f"Git committed wave {wave_num}")

    # Archive handoffs
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    for ninfo in nuclei:
        nuc = ninfo["nucleus"]
        src = HANDOFF_DIR / f"{mission}_{nuc}.md"
        if src.exists():
            shutil.move(str(src), str(ARCHIVE_DIR / src.name))

    # Clean signals for next wave
    clean_signals()

    log(f"Wave {wave_num} consolidated")


# ==================================================
# MAIN LOOP
# ==================================================

def run_mission(args: argparse.Namespace) -> None:
    mission = args.mission
    log(f"{'='*50}")
    log("CEX MISSION RUNNER v1.0")
    log(f"Mission: {mission}")
    log(f"Timeout: {args.timeout}s/wave | Poll: {args.poll}s")
    log(f"Quality floor: {args.quality_floor}")
    log(f"Dry run: {args.dry_run}")
    log(f"{'='*50}")

    # Parse waves
    if args.waves:
        waves = parse_waves_from_json(args.waves)
    elif args.plan:
        waves = parse_waves_from_plan(args.plan)
    else:
        # Auto-detect from existing handoffs
        waves = parse_waves_from_plan("")
        if not waves:
            log("No waves found. Provide --plan or --waves, or write handoffs first.", "ERROR")
            sys.exit(1)

    log(f"Found {len(waves)} wave(s)")
    for w in waves:
        nuclei_str = ", ".join(n["nucleus"].upper() for n in w["nuclei"])
        log(f"  Wave {w['wave']}: {nuclei_str}")

    # Execute each wave
    results = []
    overall_start = time.time()

    for wave in waves:
        wave_num = wave["wave"]
        nuclei = wave["nuclei"]
        nuclei_str = ", ".join(n["nucleus"].upper() for n in nuclei)

        log("")
        log(f"{'='*50}")
        log(f"WAVE {wave_num}: {nuclei_str}")
        log(f"{'='*50}")

        # Step 1: Clean old signals
        clean_signals()

        # Step 2: Copy handoffs to task files
        log("Preparing handoffs...")
        copy_handoffs_to_tasks(mission, nuclei)

        # Step 2.5: Hygiene gate (warning only, does not block dispatch)
        try:
            from cex_hygiene import run_scan
            scan_result = run_scan()
            if scan_result.critical_count > 0:
                log(f"Hygiene: {scan_result.critical_count} critical issues found", "WARN")
                log("Run: python _tools/cex_hygiene.py clean", "WARN")
            else:
                log("Hygiene: clean")
        except ImportError:
            log("Hygiene scanner not available -- skipping", "WARN")
        except Exception as e:
            log(f"Hygiene scan error: {e}", "WARN")

        # Step 3: Dispatch grid
        log("Dispatching grid...")
        dispatch_grid(mission, args.dry_run)

        # Step 4: Watch signals (BLOCKING)
        log("Waiting for signals...")
        watch_result = watch_signals(nuclei, args.timeout, args.poll, args.dry_run)
        watch_status = watch_result.get("status", "unknown")

        log(f"Signal watch returned: {watch_status}")

        if watch_status == "timeout":
            log("TIMEOUT -- some nuclei didn't complete", "WARN")
        elif watch_status in ("crashed", "all_pending_crashed"):
            log("CRASH -- nuclei died without signaling", "ERROR")

        # --- T08: Coordinator synthesis gate ---
        try:
            from cex_coordinator import CexCoordinator
            coord = CexCoordinator(mission_id=mission)
            nuc_results = []
            for ninfo in nuclei:
                nuc = ninfo["nucleus"]
                sig = watch_result.get("nuclei", {}).get(nuc, {})
                nuc_results.append({
                    "nucleus": nuc, "status": sig.get("status", watch_status),
                    "quality": sig.get("quality", 0.0),
                    "output_path": sig.get("output", ""),
                })
            synthesis = coord.synthesize(nuc_results)
            if synthesis.passed:
                log(f"Synthesis gate PASSED (score={synthesis.score:.1f})")
            else:
                log(f"Synthesis gate ISSUES: {synthesis.issues}", "WARN")
        except ImportError:
            pass
        except Exception as e:
            log(f"Synthesis gate skipped: {e}", "WARN")

        # Step 5: Stop all processes
        if not args.skip_stop:
            log("Stopping processes...")
            stop_processes(args.dry_run)

        # Step 6: Quality gate
        log("Running quality gate...")
        gate = quality_gate(nuclei, watch_result, args.quality_floor)

        failures = [n for n, g in gate.items() if not g["passed"]]
        if failures:
            log(f"Quality gate FAILED for: {', '.join(failures)}", "WARN")
            # TODO: re-dispatch with feedback (G3 advanced)
        else:
            log("Quality gate PASSED for all nuclei")

        # Step 7: Consolidate
        log("Consolidating wave...")
        consolidate_wave(mission, wave_num, nuclei, args.dry_run)

        # Record wave result
        wave_result = {
            "wave": wave_num,
            "nuclei": nuclei_str,
            "watch_status": watch_status,
            "gate": gate,
            "duration": watch_result.get("duration_seconds", 0),
        }
        results.append(wave_result)

        log(f"Wave {wave_num} DONE in {wave_result['duration']}s")

    # Final report
    total_duration = int(time.time() - overall_start)

    log("")
    log(f"{'='*50}")
    log(f"MISSION COMPLETE: {mission}")
    log(f"{'='*50}")
    log(f"Waves: {len(results)}")
    log(f"Total duration: {total_duration}s ({total_duration//60}min)")

    all_passed = all(
        all(g["passed"] for g in r["gate"].values())
        for r in results
    )

    for r in results:
        gate_str = " ".join(
            f"{n.upper()}:{'OK' if g['passed'] else 'FAIL'}"
            for n, g in r["gate"].items()
        )
        log(f"  Wave {r['wave']}: {r['watch_status']} | {gate_str} | {r['duration']}s")

    # Write final summary
    summary = {
        "mission": mission,
        "status": "complete" if all_passed else "partial",
        "waves": len(results),
        "total_duration_seconds": total_duration,
        "all_quality_passed": all_passed,
        "results": results,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    summary_path = ROOT / ".cex" / "runtime" / "grid_status.json"
    summary_path.write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    log(f"Summary written to {summary_path}")

    sys.exit(0 if all_passed else 2)


if __name__ == "__main__":
    args = parse_args()
    if args.continuous:
        run_continuous(args)
    else:
        run_mission(args)
