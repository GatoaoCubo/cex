#!/usr/bin/env python3
"""cex_mission_dispatch.py: unified /mission entry. Runtime-agnostic dispatcher.

Reads:
  .cex/P09_config/missions/{mission}/mission.yaml  (what to do)
  .cex/P09_config/runtimes/{runtime}.yaml          (who does it)

Dispatches the right grid/solo spawn per runtime, same handoffs across all.

Usage:
    python _tools/cex_mission_dispatch.py --mission LEVERAGE_MAP_V2 --runtime ollama-qwen-coder
    python _tools/cex_mission_dispatch.py --mission LEVERAGE_MAP_V2 --runtime claude
    python _tools/cex_mission_dispatch.py --list-runtimes
    python _tools/cex_mission_dispatch.py --list-missions
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MISSIONS_DIR = ROOT / ".cex" / "config" / "missions"
RUNTIMES_DIR = ROOT / ".cex" / "config" / "runtimes"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def list_runtimes() -> list[str]:
    return sorted(p.stem for p in RUNTIMES_DIR.glob("*.yaml"))


def list_missions() -> list[str]:
    return sorted(p.name for p in MISSIONS_DIR.iterdir() if p.is_dir())


def dispatch_ollama(mission_cfg: dict, runtime_cfg: dict, output_tag: str) -> int:
    mission = mission_cfg["mission"]
    spawn_script = runtime_cfg["spawn_script"]
    models = runtime_cfg["models"]
    default_model = models.get("default", "llama3.1:8b")
    profile = runtime_cfg.get("agentic_profile", {})
    max_iters = profile.get("max_iters", 15)
    require_reads = profile.get("require_reads_before_done", 2)

    # Per-nucleus routing as PowerShell hashtable literal
    per_nucleus_models = {k: v for k, v in models.items() if k.startswith("n")}
    unique = set(per_nucleus_models.values())
    model_map_arg = None
    if len(unique) > 1:
        # Build @{n01='llama3.1:8b'; n03='qwen2.5-coder:7b'; ...}
        pairs = "; ".join(f"{k}='{v}'" for k, v in per_nucleus_models.items())
        model_map_arg = "@{" + pairs + "}"
        print(f"[route] per-nucleus: {per_nucleus_models}")

    if model_map_arg:
        # PowerShell can't bind @{...} literal from argv strings -- wrap via -Command
        # so PS parses the hashtable itself.
        ps_expr = (
            f"& '{spawn_script}' "
            f"-Mission '{mission}' -Model '{default_model}' "
            f"-MaxIters {max_iters} -RequireReads {require_reads} "
            f"-OutputTag '{output_tag}' -ModelMap {model_map_arg}"
        )
        cmd = [
            "powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass",
            "-Command", ps_expr,
        ]
    else:
        cmd = [
            "powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass",
            "-File", spawn_script,
            "-Mission", mission,
            "-Model", default_model,
            "-MaxIters", str(max_iters),
            "-RequireReads", str(require_reads),
            "-OutputTag", output_tag,
        ]
    print(f"[dispatch] {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=ROOT)


def _dispatch_via_bash(mode: str, mission: str, runtime_label: str) -> int:
    """Call bash _spawn/dispatch.sh {mode} {mission}. Returns exit code."""
    cmd = ["bash", "_spawn/dispatch.sh", mode, mission]
    print(f"[dispatch] {runtime_label}: {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=ROOT)


def dispatch_claude(mission_cfg: dict, runtime_cfg: dict, output_tag: str) -> int:
    # spawn_grid.ps1 -cli claude reads handoffs from .cex/runtime/handoffs/
    return _dispatch_via_bash("grid", mission_cfg["mission"], "claude")


def dispatch_claude_haiku(mission_cfg: dict, runtime_cfg: dict, output_tag: str) -> int:
    # Same claude path but forces Haiku model via spawn_grid -Model flag.
    model = (runtime_cfg.get("models") or {}).get("n01") or "claude-haiku-4-5-20251001"
    cmd = ["bash", "_spawn/dispatch.sh", "grid-haiku", mission_cfg["mission"], model]
    print(f"[dispatch] claude-haiku: {' '.join(cmd)}")
    return subprocess.call(cmd, cwd=ROOT)


def dispatch_gemini(mission_cfg: dict, runtime_cfg: dict, output_tag: str) -> int:
    return _dispatch_via_bash("grid-gemini", mission_cfg["mission"], "gemini")


def dispatch_codex(mission_cfg: dict, runtime_cfg: dict, output_tag: str) -> int:
    return _dispatch_via_bash("grid-codex", mission_cfg["mission"], "codex")


DISPATCHERS = {
    "ollama-llama": dispatch_ollama,
    "ollama-qwen-coder": dispatch_ollama,
    "ollama-hybrid": dispatch_ollama,
    "claude": dispatch_claude,
    "claude-haiku": dispatch_claude_haiku,
    "gemini": dispatch_gemini,
    "codex": dispatch_codex,
}


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mission", help="mission name (dir under .cex/P09_config/missions/)")
    p.add_argument("--runtime", help="runtime name (yaml stem under .cex/P09_config/runtimes/)")
    p.add_argument("--output-tag", default="",
                   help="suffix for _reports/{mission}_{tag}/ (default: runtime name)")
    p.add_argument("--list-runtimes", action="store_true")
    p.add_argument("--list-missions", action="store_true")
    p.add_argument("--show", action="store_true",
                   help="show resolved mission + runtime config without dispatching")
    args = p.parse_args()

    if args.list_runtimes:
        for r in list_runtimes():
            print(f"  {r}")
        return 0
    if args.list_missions:
        for m in list_missions():
            print(f"  {m}")
        return 0

    if not args.mission or not args.runtime:
        print("ERROR: --mission and --runtime are required", file=sys.stderr)
        print("  Runtimes:", ", ".join(list_runtimes()))
        print("  Missions:", ", ".join(list_missions()))
        return 1

    mission_yaml = MISSIONS_DIR / args.mission / "mission.yaml"
    runtime_yaml = RUNTIMES_DIR / f"{args.runtime}.yaml"

    if not mission_yaml.exists():
        print(f"ERROR: mission not found: {mission_yaml}", file=sys.stderr)
        return 1
    if not runtime_yaml.exists():
        print(f"ERROR: runtime not found: {runtime_yaml}", file=sys.stderr)
        return 1

    mission_cfg = load_yaml(mission_yaml)
    runtime_cfg = load_yaml(runtime_yaml)

    if args.runtime not in mission_cfg.get("runtime_selection", {}).get("supported", []):
        print(f"WARN: runtime {args.runtime} not in mission's supported list: "
              f"{mission_cfg.get('runtime_selection', {}).get('supported', [])}")

    output_tag = args.output_tag or args.runtime.replace("ollama-", "")

    print(f"=== MISSION DISPATCH ===")
    print(f"  mission: {mission_cfg['mission']} v{mission_cfg.get('version', 1)}")
    print(f"  runtime: {runtime_cfg['runtime']} (tier={runtime_cfg.get('tier', '?')})")
    print(f"  nuclei:  {mission_cfg.get('nuclei', [])}")
    print(f"  output:  _reports/{args.mission}_{output_tag}/")
    print(f"  quality_floor: {mission_cfg.get('quality_floor', 8.0)}")
    print(f"========================")

    if args.show:
        return 0

    dispatcher = DISPATCHERS.get(args.runtime)
    if not dispatcher:
        print(f"ERROR: no dispatcher for runtime {args.runtime}", file=sys.stderr)
        return 1

    return dispatcher(mission_cfg, runtime_cfg, output_tag)


if __name__ == "__main__":
    sys.exit(main())
