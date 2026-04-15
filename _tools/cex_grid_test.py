#!/usr/bin/env python3
"""cex_grid_test.py: multi-runtime wave orchestrator.

Runs the SAME mission across N runtimes sequentially (one wave per runtime):
  wave_k = dispatch mission to runtime_k --> poll --> close --> archive
  between waves: active sleep (30s) + status line

For each wave, produces _reports/gridtest_{mission}/{runtime}/ with:
  - LEVERAGE_MAP_V2_n0X.md (nucleus output)
  - LEVERAGE_MAP_V2_n0X.trace.json (ReAct trace)
  - wave_report.json (files, bytes, iters, reads, completed_count)
Final: _reports/gridtest_{mission}/matrix.md comparing all runtimes.

Usage:
  python _tools/cex_grid_test.py --mission leverage_map \
      --runtimes ollama-llama,ollama-qwen-coder,claude \
      --wave-timeout 900 --poll-interval 30
  python _tools/cex_grid_test.py --mission leverage_map --dry-run
  python _tools/cex_grid_test.py --resume _reports/gridtest_leverage_map/state.json

Does NOT call ScheduleWakeup. All sleeps are in-process (time.sleep) so the
caller can run this with run_in_background and poll the log file.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MISSIONS_DIR = ROOT / ".cex" / "config" / "missions"
RUNTIMES_DIR = ROOT / ".cex" / "config" / "runtimes"
PID_DIR = ROOT / ".cex" / "runtime" / "pids"

DEFAULT_RUNTIMES = [
    "claude",
    "gemini",
    "codex",
    "ollama-llama",
    "ollama-qwen-coder",
]

INTER_WAVE_SLEEP = 15  # seconds between wave teardown and next dispatch


def ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def log(msg: str, state_log: Path | None = None) -> None:
    line = f"[{ts()}] {msg}"
    print(line, flush=True)
    if state_log:
        with state_log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")


def resolve_output_dir(mission: str, runtime: str) -> Path:
    """Where the ollama spawn writes. Claude/gemini/codex write elsewhere."""
    if runtime.startswith("ollama-"):
        tag = runtime.replace("ollama-", "")
        return ROOT / "_reports" / f"{mission.lower()}_{tag}"
    # claude/gemini/codex: nuclei commit into N0x_*/ directories (not a unified dir)
    # So we check git log for commits instead of file landing.
    return ROOT / "_reports" / f"{mission.lower()}_{runtime}"


def list_output_files(output_dir: Path, mission_upper: str) -> list[Path]:
    if not output_dir.exists():
        return []
    return sorted(output_dir.glob(f"{mission_upper}_n0*.md"))


def get_grid_pid_file(mission: str, runtime: str) -> Path:
    if runtime.startswith("ollama-"):
        return PID_DIR / f"grid_ollama_{mission}.txt"
    return PID_DIR / "spawn_pids.txt"


def parse_pid_file(pid_file: Path) -> list[int]:
    if not pid_file.exists():
        return []
    pids = []
    for line in pid_file.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            pids.append(int(line.split()[0]))
        except (ValueError, IndexError):
            continue
    return pids


def pid_alive(pid: int) -> bool:
    if os.name == "nt":
        r = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command",
             f"if (Get-Process -Id {pid} -EA SilentlyContinue) {{ 'yes' }} else {{ 'no' }}"],
            capture_output=True, text=True, timeout=10,
        )
        return "yes" in r.stdout
    try:
        os.kill(pid, 0)
        return True
    except (ProcessLookupError, PermissionError):
        return False


def kill_pid_tree(pid: int) -> None:
    if os.name == "nt":
        subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", f"taskkill /F /PID {pid} /T"],
            capture_output=True, timeout=10,
        )
    else:
        try:
            os.kill(pid, 9)
        except ProcessLookupError:
            pass


def dispatch_wave(mission: str, runtime: str, output_tag: str, state_log: Path) -> int:
    cmd = [
        sys.executable, str(ROOT / "_tools" / "cex_mission_dispatch.py"),
        "--mission", mission,
        "--runtime", runtime,
        "--output-tag", output_tag,
    ]
    log(f"DISPATCH wave: {' '.join(cmd)}", state_log)
    return subprocess.call(cmd, cwd=ROOT)


def poll_wave(
    mission_cfg: dict,
    runtime: str,
    output_dir: Path,
    pid_file: Path,
    timeout_s: int,
    poll_interval: int,
    state_log: Path,
) -> dict:
    """Block until all nuclei committed or timeout. Return summary dict."""
    mission_upper = mission_cfg["mission"]
    nuclei = mission_cfg["nuclei"]
    min_bytes = mission_cfg.get("min_bytes", 800)
    expected = len(nuclei)

    start = time.time()
    last_report = 0.0
    result = {
        "runtime": runtime,
        "mission": mission_upper,
        "expected": expected,
        "landed": 0,
        "usable": 0,
        "files": {},
        "timed_out": False,
        "elapsed_s": 0,
    }

    while True:
        elapsed = time.time() - start
        files = list_output_files(output_dir, mission_upper)
        landed = len(files)
        usable = sum(1 for f in files if f.stat().st_size >= min_bytes)

        pids = parse_pid_file(pid_file)
        alive = [p for p in pids if pid_alive(p)]

        if time.time() - last_report >= poll_interval or landed == expected:
            log(
                f"  poll [{runtime}] elapsed={int(elapsed)}s "
                f"landed={landed}/{expected} usable={usable} "
                f"pids_alive={len(alive)}/{len(pids)}",
                state_log,
            )
            last_report = time.time()

        if landed >= expected:
            break
        if elapsed >= timeout_s:
            result["timed_out"] = True
            log(f"  TIMEOUT after {int(elapsed)}s", state_log)
            break
        time.sleep(min(poll_interval, max(5, poll_interval // 3)))

    result["landed"] = landed
    result["usable"] = usable
    result["elapsed_s"] = int(time.time() - start)
    for f in list_output_files(output_dir, mission_upper):
        nuc = f.stem.rsplit("_", 1)[-1]
        trace = f.with_suffix(".trace.json")
        file_info = {
            "bytes": f.stat().st_size,
            "usable": f.stat().st_size >= min_bytes,
        }
        if trace.exists():
            try:
                t = json.loads(trace.read_text(encoding="utf-8", errors="replace"))
                iters = t.get("iters") or t.get("iterations")
                if iters is None and isinstance(t, list):
                    iters = len(t)
                file_info["iters"] = iters
                if isinstance(t, dict):
                    file_info["reads"] = t.get("reads_performed")
                    file_info["done_called"] = t.get("done_called")
            except (json.JSONDecodeError, OSError):
                pass
        result["files"][nuc] = file_info
    return result


def close_wave(mission: str, runtime: str, pid_file: Path, state_log: Path) -> int:
    """Kill all windows from this wave."""
    pids = parse_pid_file(pid_file)
    killed = 0
    for pid in pids:
        if pid_alive(pid):
            kill_pid_tree(pid)
            killed += 1
    log(f"  close [{runtime}] killed {killed}/{len(pids)} PIDs", state_log)
    return killed


def archive_wave(
    mission: str,
    runtime: str,
    output_dir: Path,
    archive_root: Path,
    wave_result: dict,
    state_log: Path,
) -> Path:
    dest = archive_root / runtime
    dest.mkdir(parents=True, exist_ok=True)
    copied = 0
    mission_upper = mission.upper() if mission.isupper() else wave_result["mission"]
    if output_dir.exists():
        for f in output_dir.glob(f"{mission_upper}_n0*.*"):
            shutil.copy2(f, dest / f.name)
            copied += 1
    (dest / "wave_report.json").write_text(
        json.dumps(wave_result, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    log(f"  archive [{runtime}] -> {dest} ({copied} files)", state_log)
    return dest


def write_matrix(archive_root: Path, waves: list[dict]) -> Path:
    matrix = archive_root / "matrix.md"
    lines = [
        f"# Grid-Test Matrix",
        f"",
        f"Generated: {ts()}",
        f"",
        f"| Runtime | Landed | Usable | Timeout | Elapsed(s) |",
        f"|---|---|---|---|---|",
    ]
    for w in waves:
        lines.append(
            f"| {w['runtime']} | {w['landed']}/{w['expected']} "
            f"| {w['usable']}/{w['expected']} "
            f"| {'yes' if w['timed_out'] else 'no'} "
            f"| {w['elapsed_s']} |"
        )
    lines += ["", "## Per-nucleus bytes", "", "| Runtime | n01 | n02 | n03 | n04 | n05 | n06 |", "|---|---|---|---|---|---|---|"]
    for w in waves:
        row = [w["runtime"]]
        for nuc in ("n01", "n02", "n03", "n04", "n05", "n06"):
            info = w["files"].get(nuc, {})
            b = info.get("bytes")
            row.append(str(b) if b is not None else "-")
        lines.append("| " + " | ".join(row) + " |")
    matrix.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return matrix


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mission", required=True, help="mission dir name under .cex/config/missions/")
    p.add_argument("--runtimes", default=",".join(DEFAULT_RUNTIMES),
                   help="comma-separated runtime names (in order)")
    p.add_argument("--wave-timeout", type=int, default=900,
                   help="max seconds per wave (default 900)")
    p.add_argument("--poll-interval", type=int, default=30,
                   help="status poll interval in seconds (default 30)")
    p.add_argument("--inter-wave-sleep", type=int, default=INTER_WAVE_SLEEP,
                   help=f"sleep between waves in seconds (default {INTER_WAVE_SLEEP})")
    p.add_argument("--output-tag-suffix", default="gridtest",
                   help="suffix appended to per-runtime tags (default 'gridtest')")
    p.add_argument("--dry-run", action="store_true",
                   help="resolve + print plan, do not dispatch")
    p.add_argument("--skip-claude-family", action="store_true",
                   help="skip claude/gemini/codex (output-dir detection not wired)")
    args = p.parse_args()

    mission_yaml = MISSIONS_DIR / args.mission / "mission.yaml"
    if not mission_yaml.exists():
        print(f"ERROR: mission not found: {mission_yaml}", file=sys.stderr)
        return 1
    mission_cfg = load_yaml(mission_yaml)
    mission_upper = mission_cfg["mission"]

    requested = [r.strip() for r in args.runtimes.split(",") if r.strip()]
    runtimes = []
    for r in requested:
        if not (RUNTIMES_DIR / f"{r}.yaml").exists():
            print(f"WARN: runtime yaml missing, skipping: {r}")
            continue
        if args.skip_claude_family and r in ("claude", "gemini", "codex"):
            print(f"SKIP (flag): {r}")
            continue
        runtimes.append(r)

    if not runtimes:
        print("ERROR: no valid runtimes", file=sys.stderr)
        return 1

    archive_root = ROOT / "_reports" / f"gridtest_{args.mission.lower()}"
    archive_root.mkdir(parents=True, exist_ok=True)
    state_log = archive_root / "state.log"
    state_log.write_text(f"# grid-test {mission_upper} started {ts()}\n", encoding="utf-8")

    log(f"=== GRID TEST: {mission_upper} ===", state_log)
    log(f"runtimes: {runtimes}", state_log)
    log(f"archive: {archive_root}", state_log)
    log(f"wave_timeout={args.wave_timeout}s poll={args.poll_interval}s inter_wave={args.inter_wave_sleep}s", state_log)

    if args.dry_run:
        log("DRY-RUN: exiting without dispatch", state_log)
        return 0

    waves: list[dict] = []
    for i, runtime in enumerate(runtimes, 1):
        log(f"", state_log)
        log(f"=== WAVE {i}/{len(runtimes)}: {runtime} ===", state_log)

        tag = runtime.replace("ollama-", "") if runtime.startswith("ollama-") else runtime
        output_dir = resolve_output_dir(mission_upper.lower(), runtime)
        pid_file = get_grid_pid_file(mission_upper, runtime)

        rc = dispatch_wave(args.mission, runtime, tag, state_log)
        if rc != 0:
            log(f"  dispatch FAILED rc={rc}", state_log)
            waves.append({
                "runtime": runtime, "mission": mission_upper,
                "expected": len(mission_cfg["nuclei"]), "landed": 0, "usable": 0,
                "files": {}, "timed_out": False, "elapsed_s": 0, "dispatch_rc": rc,
            })
            continue

        time.sleep(5)  # let windows spawn + first iteration kick off

        result = poll_wave(
            mission_cfg, runtime, output_dir, pid_file,
            args.wave_timeout, args.poll_interval, state_log,
        )
        close_wave(mission_upper, runtime, pid_file, state_log)
        archive_wave(mission_upper, runtime, output_dir, archive_root, result, state_log)
        waves.append(result)

        if i < len(runtimes):
            log(f"  inter-wave sleep {args.inter_wave_sleep}s before next runtime", state_log)
            time.sleep(args.inter_wave_sleep)

    matrix = write_matrix(archive_root, waves)
    log(f"", state_log)
    log(f"=== COMPLETE ===", state_log)
    log(f"matrix: {matrix}", state_log)
    log(f"state_log: {state_log}", state_log)
    return 0


if __name__ == "__main__":
    sys.exit(main())
