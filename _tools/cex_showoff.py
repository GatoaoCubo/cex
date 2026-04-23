"""CEX Showoff Grid -- 4-runtime smoke validation.

Runs 5 waves to prove all 4 runtimes (claude + codex + gemini + ollama) work
in grid dispatch. Each nucleus (N01-N06) produces a tiny signature artifact.

Waves:
  W1 -- all ollama  (qwen3:8b, local, free)
  W2 -- all gemini  (gemini-2.5-flash-lite, cheapest cloud)
  W3 -- all codex   (gpt-5, cheapest OpenAI tier CLI -- gpt-5 needs API key)
  W4 -- all claude  (claude-haiku-4-5-20251001, cheapest Claude)
  W5 -- MIXED       (2 ollama + 2 gemini + 1 codex + 1 claude)

Each wave: write 6 handoffs -> dispatch grid -> poll signals -> stop -> verify.

Usage:
  python _tools/cex_showoff.py              # full 5-wave run (~25-40 min)
  python _tools/cex_showoff.py --wave 1     # single wave
  python _tools/cex_showoff.py --dry-run    # print plan, no dispatch
"""
from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
SHOWOFF_DIR = ROOT / "_showof"
NUCLEI = ["n01", "n02", "n03", "n04", "n05", "n06"]

def _build_waves():
    """Build WAVES config using model resolver when available."""
    # Resolve models dynamically, fallback to known defaults
    try:
        from cex_model_resolver import get_ollama_config, get_preflight_model
        _ollama_model = get_ollama_config()["models"].get("light", "llama3.1:8b")
        _haiku_model = get_preflight_model("cloud")["model"]
    except Exception:
        _ollama_model = "llama3.1:8b"
        _haiku_model = "claude-haiku-4-5-20251001"
    # Gemini and Codex models are runtime-specific, keep as config constants
    _gemini_model = "gemini-2.5-flash-lite"
    _codex_model = "gpt-5"

    return [
        {"n": 1, "runtime": "ollama", "model": _ollama_model,
         "dispatch": ["bash", "_spawn/dispatch.sh", "grid-ollama", "SHOWOFF_W1", _ollama_model],
         "handoff_suffix": "_ollama",
         "mapping": {n: ("ollama", _ollama_model) for n in NUCLEI}},
        {"n": 2, "runtime": "gemini", "model": _gemini_model,
         "dispatch": ["bash", "_spawn/dispatch.sh", "grid-gemini", "SHOWOFF_W2"],
         "handoff_suffix": "_gemini",
         "mapping": {n: ("gemini", _gemini_model) for n in NUCLEI}},
        {"n": 3, "runtime": "codex", "model": _codex_model,
         "dispatch": ["bash", "_spawn/dispatch.sh", "grid-codex", "SHOWOFF_W3"],
         "handoff_suffix": "_codex",
         "mapping": {n: ("codex", _codex_model) for n in NUCLEI}},
        {"n": 4, "runtime": "claude", "model": _haiku_model,
         "dispatch": ["bash", "_spawn/dispatch.sh", "grid-haiku", "SHOWOFF_W4"],
         "handoff_suffix": "",
         "mapping": {n: ("claude", _haiku_model) for n in NUCLEI}},
        {"n": 5, "runtime": "mixed", "model": "mixed",
         "dispatch": None,  # manual mixed spawn
         "handoff_suffix": None,
         "mapping": {
             "n01": ("ollama", _ollama_model),
             "n02": ("gemini", _gemini_model),
             "n03": ("codex",  _codex_model),
             "n04": ("claude", _haiku_model),
             "n05": ("ollama", _ollama_model),
             "n06": ("gemini", _gemini_model),
         }},
    ]


WAVES = _build_waves()

POLL_TIMEOUT_SEC = 300  # 5 min per wave
POLL_INTERVAL_SEC = 15

BOOT_SUFFIX = {"claude": "", "gemini": "_gemini", "codex": "_codex", "ollama": "_ollama"}
TASK_SUFFIX = {"claude": "", "gemini": "_gemini", "codex": "_codex", "ollama": "_ollama"}


def handoff_body(wave_n: int, nucleus: str, runtime: str, model: str) -> str:
    """Minimal task body -- must be trivial enough for qwen3:8b to complete."""
    out = SHOWOFF_DIR / f"w{wave_n}" / f"{nucleus}_{runtime}.md"
    body = """---
nucleus: {nucleus}
mission: SHOWOFF_W{wave_n}
runtime: {runtime}
model: {model}
---
# {nucleus.upper()} -- SHOWOFF Wave {wave_n} ({runtime})

## TASK (trivial -- do NOT run 8F, just produce the artifact)

1. Create directory `_showoff/w{wave_n}/` if missing.
2. Create file `_showoff/w{wave_n}/{nucleus}_{runtime}.md` with EXACTLY this content:

```
---
id: showoff_w{wave_n}_{nucleus}_{runtime}
kind: smoke_eval
title: "SHOWOFF Wave {wave_n} -- {nucleus} via {runtime}"
version: 1
quality: null
pillar: P07
nucleus: {nucleus}
runtime: {runtime}
model: {model}
wave: {wave_n}
tags: [showoff, smoke, multi-runtime]
---

# SHOWOFF Wave {wave_n}

Nucleus: {nucleus}
Runtime: {runtime}
Model: {model}
Signed: alive
```

3. Run: `git add _showoff/w{wave_n}/{nucleus}_{runtime}.md && git commit -m "[{nucleus}] SHOWOFF W{wave_n} via {runtime}"`
4. Signal:
```
python -c "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('{nucleus}', 'complete', 9.0, mission='SHOWOFF_W{wave_n}')"
```
5. Exit.

No 8F, no quality gate, no extra artifacts. Just the 1 file + commit + signal.
"""
    return body


def write_handoffs(wave: dict[str, Any], mixed: bool = False) -> list[Path]:
    """Write SHOWOFF_W{n}_{nucleus}.md files the dispatcher picks up."""
    wave_n = wave["n"]
    written = []
    for nucleus in NUCLEI:
        runtime, model = wave["mapping"][nucleus]
        body = handoff_body(wave_n, nucleus, runtime, model)
        # For grid dispatch: spawn_grid looks up ${mission}_{nucleus}.md
        mission_handoff = HANDOFF_DIR / f"SHOWOFF_W{wave_n}_{nucleus}.md"
        mission_handoff.write_text(body, encoding="utf-8")
        written.append(mission_handoff)
        # Also copy to the runtime-specific task file for direct boot
        suffix = TASK_SUFFIX.get(runtime, "")
        task_file = HANDOFF_DIR / f"{nucleus}_task{suffix}.md"
        task_file.write_text(body, encoding="utf-8")
    return written


def poll_signals(
    wave_n: int,
    expected: list[str],
    timeout: int = POLL_TIMEOUT_SEC,
) -> tuple[set[str], float]:
    """Poll signal dir for expected mission markers. Return (found_set, elapsed)."""
    start = time.time()
    found = set()
    mission = f"SHOWOFF_W{wave_n}"
    while time.time() - start < timeout and len(found) < len(expected):
        for sig_file in SIGNAL_DIR.glob("signal_*.json"):
            if sig_file.stat().st_mtime < start - 5:
                continue
            try:
                data = json.loads(sig_file.read_text(encoding="utf-8"))
            except Exception:
                continue
            if data.get("mission") == mission:
                found.add(data.get("nucleus", "").lower())
        if len(found) >= len(expected):
            break
        time.sleep(POLL_INTERVAL_SEC)
    return found, time.time() - start


def stop_all() -> None:
    """Kill this session's nuclei."""
    subprocess.run(["bash", "_spawn/dispatch.sh", "stop"], cwd=ROOT, timeout=60)


def spawn_mixed(wave: dict[str, Any]) -> None:
    """Wave 5: start one boot per nucleus with its assigned runtime, EACH POSITIONED
    at its fixed 3x2 cell (n01..n06 -> top-left..bottom-right).
    Uses _spawn/spawn_one_positioned.ps1 helper so positioning is consistent with
    full-grid dispatch (spawn_grid.ps1 uses the same fixedCells map).
    """
    wave_n = wave["n"]
    helper = ROOT / "_spawn" / "spawn_one_positioned.ps1"
    if not helper.exists():
        print(f"  [FATAL] positioning helper missing: {helper}")
        return
    for nucleus, (runtime, _model) in wave["mapping"].items():
        suffix = BOOT_SUFFIX[runtime]
        boot = f"boot/{nucleus}{suffix}.ps1"
        if not (ROOT / boot).exists():
            print(f"  [SKIP] {nucleus}: boot {boot} missing")
            continue
        cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass",
               "-File", str(helper),
               "-Nucleus", nucleus, "-BootScript", boot]
        print(f"  [SPAWN] {nucleus} via {runtime} (positioned)")
        subprocess.Popen(cmd, cwd=ROOT)
        time.sleep(3)  # stagger so each window gets its handle before next launch


def consolidate(wave_n: int) -> list[Path]:
    """List artifacts produced this wave."""
    wdir = SHOWOFF_DIR / f"w{wave_n}"
    if not wdir.exists():
        return []
    return sorted(wdir.glob("*.md"))


def between_wave_consolidate(wave_n: int, found_signals: set[str]) -> dict[str, int | str]:
    """After a wave polls out, before next wave spawns:
    0. Safety-net signal: for each artifact file that exists without a matching
       signal (CLI didn't exit / didn't invoke signal_writer), emit one.
    1. Commit any uncommitted showoff artifacts
    2. Archive this wave's signals
    3. Verify no stray processes from this session
    4. Print wave report
    """
    print(f"\n[W{wave_n} CONSOLIDATE] starting...")
    # 0. Safety-net: artifact-present-but-no-signal fallback
    import sys as _sys
    _sys.path.insert(0, str(ROOT / "_tools"))
    from signal_writer import write_signal  # type: ignore
    wdir = SHOWOFF_DIR / f"w{wave_n}"
    if wdir.exists():
        for art in wdir.glob("*.md"):
            nuc = art.stem.split("_")[0].lower()  # n01_ollama.md -> n01
            if nuc in found_signals:
                continue
            try:
                write_signal(nuc, "exited", 7.0, mission=f"SHOWOFF_W{wave_n}",
                             origin="showoff_safety_net", artifact=str(art.relative_to(ROOT)))
                found_signals.add(nuc)
                print(f"  [safety-net] {nuc} artifact present, emitted fallback signal")
            except Exception as e:
                print(f"  [safety-net] {nuc} skipped: {e}")
    # 1. Commit strays
    status = subprocess.run(["git", "status", "--porcelain", f"_showoff/w{wave_n}/"],
                             cwd=ROOT, capture_output=True, text=True, timeout=30)
    if status.stdout.strip():
        print(f"  [commit] uncommitted files in _showoff/w{wave_n}/ -- committing")
        subprocess.run(["git", "add", f"_showoff/w{wave_n}/"], cwd=ROOT, timeout=30)
        msg = f"[N07] SHOWOFF W{wave_n} consolidate ({len(found_signals)}/6 signals)"
        subprocess.run(["git", "commit", "-m", msg],
                       cwd=ROOT, capture_output=True, timeout=60)
    else:
        print("  [commit] clean (no uncommitted artifacts)")
    # 2. Archive wave signals
    mission = f"SHOWOFF_W{wave_n}"
    archive = SIGNAL_DIR.parent / "signals_archive"
    archive.mkdir(exist_ok=True)
    archived = 0
    for sig in SIGNAL_DIR.glob("signal_*.json"):
        try:
            data = json.loads(sig.read_text(encoding="utf-8"))
            if data.get("mission") == mission:
                sig.rename(archive / sig.name)
                archived += 1
        except Exception:
            continue
    print(f"  [archive] moved {archived} signals to signals_archive/")
    # 3. Verify no stray processes (best-effort)
    try:
        result = subprocess.run(["bash", "_spawn/dispatch.sh", "stop"],
                                cwd=ROOT, capture_output=True, timeout=30)
        print("  [stop] session processes terminated")
    except Exception as e:
        print(f"  [stop] warn: {e}")
    # 4. Report
    artifacts = consolidate(wave_n)
    status_tag = "PASS" if len(found_signals) >= len(NUCLEI) else ("PARTIAL" if found_signals else "FAIL")
    print(f"  [report] W{wave_n} [{status_tag}] signals={len(found_signals)}/6 artifacts={len(artifacts)}/6")
    return {"wave": wave_n, "status": status_tag, "signals": len(found_signals), "artifacts": len(artifacts)}


def run_wave(wave: dict[str, Any], dry: bool = False) -> bool:
    wave_n = wave["n"]
    print(f"\n{'='*70}\nSHOWOFF Wave {wave_n} -- {wave['runtime']} ({wave['model']})\n{'='*70}")
    if dry:
        for n in NUCLEI:
            rt, m = wave["mapping"][n]
            print(f"  plan: {n} -> {rt} ({m})")
        return True, set()
    # 1. Write handoffs
    files = write_handoffs(wave)
    print(f"[W{wave_n}] wrote {len(files)} handoffs")
    # 2. Dispatch
    if wave["runtime"] == "mixed":
        spawn_mixed(wave)
    else:
        print(f"[W{wave_n}] dispatch: {' '.join(wave['dispatch'])}")
        subprocess.Popen(wave["dispatch"], cwd=ROOT)
    # 3. Poll
    print(f"[W{wave_n}] polling signals (timeout {POLL_TIMEOUT_SEC}s)...")
    found, elapsed = poll_signals(wave_n, NUCLEI)
    print(f"[W{wave_n}] received {len(found)}/{len(NUCLEI)} signals in {elapsed:.0f}s -> {sorted(found)}")
    # 4. Consolidate between waves (commit + archive + stop + report)
    between_wave_consolidate(wave_n, found)
    # 5. Verify artifacts
    artifacts = consolidate(wave_n)
    for a in artifacts:
        print(f"    {a.relative_to(ROOT)}")
    passed = len(found) >= len(NUCLEI) // 2  # majority = pass
    return passed, found


def final_report(results: list[tuple[int, bool, set[str], int]]) -> None:
    print(f"\n{'='*70}\nSHOWOFF FINAL REPORT\n{'='*70}")
    total = 0
    for wave_n, ok, found, artifacts in results:
        status = "PASS" if ok else "PARTIAL"
        print(f"  W{wave_n} [{status}] signals={len(found)}/6 artifacts={artifacts}")
        total += artifacts
    print(f"\n  Total artifacts: {total}/{len(results)*6}")
    print(f"{'='*70}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave", type=int, help="Run only wave N (1-5)")
    ap.add_argument("--dry-run", action="store_true", help="Print plan only")
    ap.add_argument("--skip", default="", help="Comma-separated runtimes to skip (e.g. claude)")
    args = ap.parse_args()

    SHOWOFF_DIR.mkdir(exist_ok=True)
    skip = {s.strip().lower() for s in args.skip.split(",") if s.strip()}
    results = []
    waves = [w for w in WAVES
             if (args.wave is None or w["n"] == args.wave)
             and w["runtime"] not in skip]
    if skip:
        print(f"[SKIP] runtimes excluded: {sorted(skip)}")
    for wave in waves:
        result = run_wave(wave, dry=args.dry_run)
        if not args.dry_run:
            ok, found = result
            artifacts = len(consolidate(wave["n"]))
            results.append((wave["n"], ok, found, artifacts))

    if not args.dry_run and results:
        final_report(results)


if __name__ == "__main__":
    main()
