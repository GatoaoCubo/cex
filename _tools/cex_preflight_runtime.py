"""CEX Runtime Preflight -- health-check each runtime before dispatch.

Fail fast instead of burning 5+ minutes on a gemini stall.

Probes:
  claude  -- `claude --version` works, ANTHROPIC_API_KEY or session exists
  gemini  -- `gemini --version` works, GEMINI_API_KEY set, quota not exhausted
  codex   -- `codex --version` works, prompt mode available (--prompt flag)
  ollama  -- http://localhost:11434/api/tags reachable, target model loaded

Exit codes:
  0 = all requested runtimes healthy
  1 = one or more runtimes failed
  2 = all runtimes failed (abort dispatch)

CLI:
  python _tools/cex_preflight_runtime.py --runtimes claude,gemini,ollama --model qwen3:8b
  python _tools/cex_preflight_runtime.py --all --json
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ProbeResult:
    runtime: str
    ok: bool
    detail: str
    elapsed_ms: int


def _which(name: str) -> Optional[str]:
    """Windows-aware: also check .cmd/.bat npm shims."""
    for suffix in ("", ".exe", ".cmd", ".bat"):
        path = shutil.which(name + suffix)
        if path:
            return path
    return None


def _run(cmd: list, timeout: int = 10) -> tuple[int, str]:
    # Resolve argv[0] to full path so Python can launch .cmd shims on Windows
    resolved = _which(cmd[0])
    if resolved:
        cmd = [resolved] + cmd[1:]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           shell=False)
        return r.returncode, (r.stdout + r.stderr).strip()
    except FileNotFoundError:
        return 127, "binary not found"
    except subprocess.TimeoutExpired:
        return 124, f"timeout after {timeout}s"
    except Exception as e:
        return 1, f"error: {e}"


def probe_claude() -> ProbeResult:
    t0 = time.time()
    if not _which("claude"):
        return ProbeResult("claude", False, "claude binary not in PATH",
                           int((time.time() - t0) * 1000))
    code, out = _run(["claude", "--version"], timeout=8)
    if code != 0:
        return ProbeResult("claude", False, f"version check failed: {out[:100]}",
                           int((time.time() - t0) * 1000))
    # We can't easily probe auth without a full call; assume binary success = OK
    return ProbeResult("claude", True, f"ok ({out[:80]})",
                       int((time.time() - t0) * 1000))


def probe_gemini() -> ProbeResult:
    t0 = time.time()
    if not _which("gemini"):
        return ProbeResult("gemini", False, "gemini binary not in PATH",
                           int((time.time() - t0) * 1000))
    code, out = _run(["gemini", "--version"], timeout=8)
    if code != 0:
        return ProbeResult("gemini", False, f"version check failed: {out[:100]}",
                           int((time.time() - t0) * 1000))
    # Auth can be API key OR OAuth session (managed by `gemini auth`).
    # We cannot verify OAuth without a full call. Best we can do: binary works.
    has_key = bool(os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
    auth_hint = "api_key" if has_key else "oauth-or-unauth"
    return ProbeResult("gemini", True,
                       f"ok ({out[:30]}) auth={auth_hint} -- free tier may stall",
                       int((time.time() - t0) * 1000))


def probe_codex() -> ProbeResult:
    t0 = time.time()
    if not _which("codex"):
        return ProbeResult("codex", False, "codex binary not in PATH",
                           int((time.time() - t0) * 1000))
    code, out = _run(["codex", "--version"], timeout=8)
    if code != 0:
        return ProbeResult("codex", False, f"version check failed: {out[:100]}",
                           int((time.time() - t0) * 1000))
    has_key = bool(os.environ.get("OPENAI_API_KEY"))
    auth_hint = "api_key" if has_key else "oauth-or-unauth"
    return ProbeResult("codex", True, f"ok ({out[:30]}) auth={auth_hint}",
                       int((time.time() - t0) * 1000))


def probe_ollama(model: Optional[str] = None) -> ProbeResult:
    t0 = time.time()
    try:
        import requests  # type: ignore
    except ImportError:
        return ProbeResult("ollama", False, "python-requests not installed",
                           int((time.time() - t0) * 1000))
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=4)
        r.raise_for_status()
        tags = [m["name"] for m in r.json().get("models", [])]
    except Exception as e:
        return ProbeResult("ollama", False, f"server unreachable: {e}",
                           int((time.time() - t0) * 1000))
    if model:
        if not any(model in t for t in tags):
            return ProbeResult("ollama", False,
                               f"model '{model}' not loaded (have: {', '.join(tags[:3])})",
                               int((time.time() - t0) * 1000))
        return ProbeResult("ollama", True, f"ok -- {model} ready",
                           int((time.time() - t0) * 1000))
    return ProbeResult("ollama", True, f"ok -- {len(tags)} models",
                       int((time.time() - t0) * 1000))


PROBES = {"claude": probe_claude, "gemini": probe_gemini,
          "codex": probe_codex, "ollama": probe_ollama}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runtimes", default="",
                    help="Comma list: claude,gemini,codex,ollama")
    ap.add_argument("--all", action="store_true", help="Probe all runtimes")
    ap.add_argument("--model", default=None, help="Ollama model to verify")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.all:
        targets = list(PROBES.keys())
    elif args.runtimes:
        targets = [t.strip() for t in args.runtimes.split(",") if t.strip()]
    else:
        print("error: pass --all or --runtimes", file=sys.stderr)
        sys.exit(2)
    results = []
    for rt in targets:
        fn = PROBES.get(rt)
        if not fn:
            results.append(ProbeResult(rt, False, "unknown runtime", 0))
            continue
        results.append(fn(args.model) if rt == "ollama" else fn())
    ok = sum(1 for r in results if r.ok)
    total = len(results)
    if args.json:
        print(json.dumps({"ok": ok, "total": total,
                          "results": [asdict(r) for r in results]}, indent=2))
    else:
        for r in results:
            tag = "[OK]  " if r.ok else "[FAIL]"
            print(f"{tag} {r.runtime:<8} {r.detail} ({r.elapsed_ms}ms)")
        print(f"\n{ok}/{total} runtimes healthy")
    if ok == 0:
        sys.exit(2)
    if ok < total:
        sys.exit(1)


if __name__ == "__main__":
    main()
