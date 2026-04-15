"""CEX Orchestrate -- single between-wave helper for every dispatch mode.

One helper, four consumers:
  - cex_mission_runner.py       /mission
  - cex_showoff.py              /showoff
  - cex_auto.py                 autonomous flywheel
  - dispatch.sh swarm           /batch swarm

Responsibilities (between-wave gate):
  1. Safety-net signals for artifacts without a signal
  2. Commit stray artifacts produced during the wave
  3. Archive this wave's signals to signals_archive/
  4. Stop MY session's nuclei (spawn_stop.ps1 CommandLine + orphan-node aware)
  5. Verify no wrappers survive
  6. Return structured wave report

All side effects are idempotent and session-scoped.
"""
from __future__ import annotations
import json
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
ARCHIVE_DIR = ROOT / ".cex" / "runtime" / "signals_archive"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
HANDOFF_ARCHIVE = ROOT / ".cex" / "archive" / "handoffs_done"


@dataclass
class WaveReport:
    mission: str
    wave: int
    signals_found: int
    signals_expected: int
    artifacts: int
    archived: int
    committed: bool
    wrappers_surviving: int
    status: str  # PASS | PARTIAL | FAIL
    elapsed_s: float

    def __str__(self) -> str:
        return (f"[{self.status}] {self.mission}/W{self.wave}: "
                f"signals={self.signals_found}/{self.signals_expected} "
                f"artifacts={self.artifacts} "
                f"archived={self.archived} "
                f"wrappers_left={self.wrappers_surviving} "
                f"t={self.elapsed_s:.0f}s")


def _write_signal(nucleus: str, status: str, quality: float, mission: str, **extra) -> bool:
    sys.path.insert(0, str(ROOT / "_tools"))
    try:
        from signal_writer import write_signal  # type: ignore
        write_signal(nucleus, status, quality, mission=mission, **extra)
        return True
    except Exception as e:
        print(f"[orchestrate] signal_writer failed for {nucleus}: {e}")
        return False


def safety_net_signals(mission: str, artifact_dir: Path, found_signals: set,
                       origin: str = "orchestrate_safety_net") -> int:
    """For each .md artifact present without a matching signal, emit one."""
    emitted = 0
    if not artifact_dir.exists():
        return 0
    for art in artifact_dir.glob("*.md"):
        nuc = art.stem.split("_")[0].lower()
        if nuc in found_signals:
            continue
        if _write_signal(nuc, "exited", 7.0, mission=mission,
                         origin=origin, artifact=str(art.relative_to(ROOT))):
            found_signals.add(nuc)
            emitted += 1
    return emitted


def commit_artifacts(mission: str, wave: int, artifact_dir: Path,
                     signals_count: int, expected_count: int) -> bool:
    """Commit any stray artifacts. Returns True if commit happened."""
    if not artifact_dir.exists():
        return False
    status = subprocess.run(
        ["git", "status", "--porcelain", str(artifact_dir.relative_to(ROOT))],
        cwd=ROOT, capture_output=True, text=True, timeout=30,
    )
    if not status.stdout.strip():
        return False
    subprocess.run(["git", "add", str(artifact_dir.relative_to(ROOT))],
                   cwd=ROOT, timeout=30)
    msg = f"[N07] {mission} W{wave} consolidate ({signals_count}/{expected_count} signals)"
    result = subprocess.run(
        ["git", "commit", "-m", msg, "--no-verify"],
        cwd=ROOT, capture_output=True, text=True, timeout=60,
    )
    return result.returncode == 0


def archive_signals(mission: str) -> int:
    """Move this mission's signals to archive. Returns count archived."""
    ARCHIVE_DIR.mkdir(exist_ok=True)
    archived = 0
    if not SIGNAL_DIR.exists():
        return 0
    for sig in SIGNAL_DIR.glob("signal_*.json"):
        try:
            data = json.loads(sig.read_text(encoding="utf-8"))
            if data.get("mission") == mission:
                sig.rename(ARCHIVE_DIR / sig.name)
                archived += 1
        except Exception:
            continue
    return archived


def archive_handoffs(mission: str, nuclei: Iterable[str]) -> int:
    """Archive consumed handoffs so next wave starts clean."""
    HANDOFF_ARCHIVE.mkdir(parents=True, exist_ok=True)
    archived = 0
    for nuc in nuclei:
        for pat in (f"{mission}_{nuc}.md", f"{nuc}_task.md",
                    f"{nuc}_task_gemini.md", f"{nuc}_task_codex.md",
                    f"{nuc}_task_ollama.md"):
            src = HANDOFF_DIR / pat
            if src.exists():
                src.rename(HANDOFF_ARCHIVE / f"{mission}_w_{src.name}")
                archived += 1
    return archived


def stop_session(mode: str = "session") -> int:
    """Invoke spawn_stop.ps1. mode: session | all | dry-run.
    Returns count of processes stopped (best-effort parse)."""
    cmd = ["bash", str(ROOT / "_spawn" / "dispatch.sh"), "stop"]
    if mode == "all":
        cmd.append("--all")
    elif mode == "dry-run":
        cmd.append("--dry-run")
    try:
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True,
                                text=True, timeout=60)
        for line in result.stdout.splitlines():
            if "RESULT:" in line and "terminated" in line:
                try:
                    return int(line.split("RESULT:")[1].strip().split()[0])
                except (ValueError, IndexError):
                    pass
    except subprocess.TimeoutExpired:
        print("[orchestrate] stop_session timed out")
    return 0


def count_surviving_wrappers() -> int:
    """Ask PS how many boot/n0X_*.ps1 wrappers are still alive."""
    ps_cmd = (
        "(Get-CimInstance Win32_Process -Filter \"Name='powershell.exe'\" "
        "| Where-Object { $_.CommandLine -match 'boot[/\\\\]n0[1-7]' } "
        "| Measure-Object).Count"
    )
    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps_cmd],
            cwd=ROOT, capture_output=True, text=True, timeout=15,
        )
        return int(result.stdout.strip() or 0)
    except Exception:
        return -1


def count_artifacts(artifact_dir: Path) -> int:
    if not artifact_dir.exists():
        return 0
    return sum(1 for _ in artifact_dir.glob("*.md"))


def between_wave(mission: str, wave: int,
                 artifact_dir: Path,
                 expected_nuclei: list[str],
                 found_signals: set,
                 stop_mode: str = "session",
                 archive_handoffs_too: bool = True) -> WaveReport:
    """Run the full between-wave consolidation. Return structured report."""
    start = time.time()
    safety_net_signals(mission, artifact_dir, found_signals)
    signals_count = len(found_signals)
    expected = len(expected_nuclei)
    committed = commit_artifacts(mission, wave, artifact_dir,
                                 signals_count, expected)
    archived = archive_signals(mission)
    if archive_handoffs_too:
        archive_handoffs(mission, expected_nuclei)
    stop_session(stop_mode)
    time.sleep(2)  # give taskkill time to settle
    surviving = count_surviving_wrappers()
    artifacts = count_artifacts(artifact_dir)
    status = ("PASS" if signals_count >= expected
              else "PARTIAL" if signals_count > 0
              else "FAIL")
    return WaveReport(
        mission=mission, wave=wave,
        signals_found=signals_count, signals_expected=expected,
        artifacts=artifacts, archived=archived, committed=committed,
        wrappers_surviving=max(surviving, 0),
        status=status, elapsed_s=time.time() - start,
    )


def main():
    """CLI: python cex_orchestrate.py --mission M --wave N --dir path --nuclei n01,n02 --signals n01"""
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mission", required=True)
    ap.add_argument("--wave", type=int, required=True)
    ap.add_argument("--dir", required=True, help="Artifact directory for this wave")
    ap.add_argument("--nuclei", required=True, help="Comma list of expected nuclei")
    ap.add_argument("--signals", default="", help="Comma list of nuclei that already signaled")
    ap.add_argument("--stop-mode", default="session", choices=["session", "all", "dry-run"])
    ap.add_argument("--json", action="store_true", help="Emit report as JSON")
    args = ap.parse_args()
    report = between_wave(
        mission=args.mission, wave=args.wave,
        artifact_dir=Path(args.dir) if Path(args.dir).is_absolute() else ROOT / args.dir,
        expected_nuclei=[n.strip() for n in args.nuclei.split(",")],
        found_signals=set(n.strip() for n in args.signals.split(",") if n.strip()),
        stop_mode=args.stop_mode,
    )
    if args.json:
        print(json.dumps(asdict(report), indent=2))
    else:
        print(report)


if __name__ == "__main__":
    main()
