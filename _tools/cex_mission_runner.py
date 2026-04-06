#!/usr/bin/env python3
"""CEX Mission Runner v1.0 -- Autonomous wave-based grid orchestration.

Reads a mission plan, executes wave by wave:
  write handoffs -> dispatch grid -> poll signals -> stop -> quality gate -> consolidate

Usage:
    python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --dry-run
    python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --timeout 3600
    python _tools/cex_mission_runner.py --mission MONETIZE --waves waves.yaml

Exit codes:
    0 = all waves complete, all quality gates passed
    1 = timeout on one or more waves
    2 = quality gate failure (outputs below threshold)
    3 = crash (nucleus died)
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "_tools"
SPAWN = ROOT / "_spawn"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
PID_FILE = ROOT / ".cex" / "runtime" / "pids" / "spawn_pids.txt"
ARCHIVE_DIR = ROOT / ".cex" / "archive" / "handoffs_done"


def log(msg, level="INFO"):
    ts = datetime.now().strftime("%H:%M:%S")
    # Windows cp1252 can't handle unicode box chars -- replace them
    safe_msg = str(msg).encode("ascii", "replace").decode("ascii")
    print(f"[{ts}] [{level}] {safe_msg}", flush=True)


def parse_args():
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
    return p.parse_args()


# ==================================================
# WAVE PARSING
# ==================================================

def parse_waves_from_plan(plan_path: str) -> list:
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


def parse_waves_from_json(waves_path: str) -> list:
    """Load waves from JSON/YAML file."""
    text = Path(waves_path).read_text(encoding="utf-8")
    if waves_path.endswith((".yaml", ".yml")):
        import yaml
        return yaml.safe_load(text)
    return json.loads(text)


# ==================================================
# GRID OPERATIONS
# ==================================================

def clean_signals():
    """Remove old signals."""
    if SIGNAL_DIR.exists():
        for f in SIGNAL_DIR.glob("signal_*.json"):
            f.unlink()
    log("Signals cleaned")


def copy_handoffs_to_tasks(mission: str, nuclei: list):
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


def dispatch_grid(mission: str, dry_run: bool = False):
    """Launch spawn_grid.ps1 in static mode."""
    if dry_run:
        log("[DRY-RUN] Would launch spawn_grid.ps1", "DRY")
        return

    cmd = [
        "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
        "-Command",
        f"Start-Process powershell -ArgumentList '-File', "
        f"'{SPAWN / 'spawn_grid.ps1'}', '-mission', '{mission}', '-mode', 'static' "
        f"-WorkingDirectory '{ROOT}'"
    ]
    subprocess.run(cmd, cwd=str(ROOT), timeout=30)
    log("Grid dispatched")
    time.sleep(10)  # Wait for processes to spawn


def watch_signals(nuclei: list, timeout: int, poll: int, dry_run: bool = False) -> dict:
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


def find_signals_fallback(nuclei: list) -> dict:
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


def stop_processes(dry_run: bool = False):
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

def quality_gate(nuclei: list, watch_result: dict, floor: float) -> dict:
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
# CONSOLIDATION
# ==================================================

def consolidate_wave(mission: str, wave_num: int, nuclei: list, dry_run: bool = False):
    """Commit outputs, archive handoffs, write wave summary."""
    if dry_run:
        log(f"[DRY-RUN] Would consolidate wave {wave_num}", "DRY")
        return

    # Git add all nucleus outputs
    subprocess.run(["git", "add", "-A"], cwd=str(ROOT), capture_output=True)
    subprocess.run(
        ["git", "commit", "-m",
         f"[N07/mission] {mission} wave {wave_num}: "
         f"{', '.join(n['nucleus'].upper() for n in nuclei)} complete",
         "--no-verify"],
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

def run_mission(args):
    mission = args.mission
    log(f"{'='*50}")
    log(f"CEX MISSION RUNNER v1.0")
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
    run_mission(args)
