#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Auto-Research Loop -- versioned self-improving artifact evolution.

Fuses 3 patterns:
  - ruflo/SAFLA: feedback loops + cross-session learning
  - aiox/improve-self: 3 execution modes (YOLO/interactive/preflight)
  - CEX/cex_evolve.py: scan-judge-build-validate cycle

6-phase cycle: SCAN -> JUDGE -> BUILD -> VALIDATE -> PERSIST -> VERSION

All phases use Python + Ollama (local, $0). No cloud API calls.

Usage:
    python _tools/cex_auto_research.py scan
    python _tools/cex_auto_research.py run --mode yolo
    python _tools/cex_auto_research.py run --mode interactive
    python _tools/cex_auto_research.py run --mode preflight
    python _tools/cex_auto_research.py status
    python _tools/cex_auto_research.py history
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))

STATE_FILE = ROOT / ".cex" / "runtime" / "auto_research_state.json"
LOG_FILE = ROOT / ".cex" / "learning_records" / "auto_research_log.jsonl"

OLLAMA_BASE = "http://localhost:11434/v1"
DEFAULT_MODEL = "qwen3:14b"
DEFAULT_TARGETS_PER_CYCLE = 5


def _validate_url(url):
    """Reject non-HTTP schemes and private/loopback IPs (SSRF guard)."""
    import socket
    import urllib.parse
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("URL scheme %r not allowed" % parsed.scheme)
    hostname = (parsed.hostname or "").lower()
    if hostname in ("localhost", "[::]", "[::1]"):
        raise ValueError("Loopback hostname %r not allowed" % hostname)
    try:
        ip = socket.gethostbyname(parsed.hostname)
        parts = ip.split(".")
        if (parts[0] in ("10", "127")
                or (parts[0] == "172" and 16 <= int(parts[1]) <= 31)
                or (parts[0] == "192" and parts[1] == "168")
                or ip.startswith("169.254")
                or ip == "0.0.0.0"
                or ip == "::1"):
            raise ValueError("Private IP %s not allowed" % ip)
    except socket.gaierror:
        pass
QUALITY_FLOOR = 8.0

sys.path.insert(0, str(ROOT / "_tools"))


# ================================================================
# State Management
# ================================================================

def load_state() -> dict[str, Any]:
    """Load auto-research state from disk."""
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {
        "cycle": 0,
        "last_run": None,
        "total_improved": 0,
        "total_rejected": 0,
        "total_scanned": 0,
        "model": DEFAULT_MODEL,
        "mode": "preflight",
        "history": [],
    }


def save_state(state: dict[str, Any]) -> None:
    """Persist auto-research state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def append_log(entry: dict[str, Any]) -> None:
    """Append a learning record to the JSONL log."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(str(LOG_FILE), "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ================================================================
# Phase 1: SCAN
# ================================================================

def phase_scan() -> list[dict[str, Any]]:
    """Scan for improvement targets across the codebase.

    Returns list of target dicts sorted by priority:
        [{type, path, reason, priority, effort}]
    """
    targets = []

    # 1a. Find quality:null artifacts (never scored)
    null_count = 0
    for ndir in sorted(ROOT.iterdir()):
        if not ndir.name.startswith("N0") or not ndir.is_dir():
            continue
        for md in ndir.rglob("*.md"):
            if any(p.startswith(".") for p in md.parts):
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not fm:
                continue
            if "quality: null" in fm.group(1) or "quality:" not in fm.group(1):
                targets.append({
                    "type": "quality_null",
                    "path": str(md.relative_to(ROOT)),
                    "reason": "Never scored (quality: null)",
                    "priority": 2,
                    "effort": "small",
                })
                null_count += 1

    # 1b. Find low-quality artifacts (scored < 8.5)
    for ndir in sorted(ROOT.iterdir()):
        if not ndir.name.startswith("N0") or not ndir.is_dir():
            continue
        for md in ndir.rglob("*.md"):
            if any(p.startswith(".") for p in md.parts):
                continue
            try:
                text = md.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not fm:
                continue
            qm = re.search(r"quality:\s*([\d.]+)", fm.group(1))
            if qm:
                score = float(qm.group(1))
                if 0 < score < 8.5:
                    targets.append({
                        "type": "low_score",
                        "path": str(md.relative_to(ROOT)),
                        "reason": "Score %.1f < 8.5" % score,
                        "priority": 3,
                        "effort": "medium",
                        "current_score": score,
                    })

    # 1c. Run hygiene scan if available
    try:
        from cex_hygiene import scan_all
        issues = scan_all()
        for issue in issues[:20]:  # cap at 20
            targets.append({
                "type": "hygiene",
                "path": issue.get("path", ""),
                "reason": issue.get("message", "hygiene issue"),
                "priority": 4,
                "effort": "small",
            })
    except (ImportError, Exception):
        pass

    # Sort by priority (lower = higher priority)
    targets.sort(key=lambda t: (t["priority"], t.get("current_score", 10)))
    return targets


# ================================================================
# Phase 2: JUDGE
# ================================================================

def phase_judge(
    targets: list[dict[str, Any]],
    max_targets: int = DEFAULT_TARGETS_PER_CYCLE,
) -> list[dict[str, Any]]:
    """Select top N targets for this cycle.

    Returns: list of selected target dicts.
    """
    # Prioritize: quality_null > low_score > hygiene
    selected = []
    seen_paths = set()

    for t in targets:
        if t["path"] in seen_paths:
            continue
        seen_paths.add(t["path"])
        selected.append(t)
        if len(selected) >= max_targets:
            break

    return selected


# ================================================================
# Phase 3: BUILD (Ollama-powered improvements)
# ================================================================

def _call_ollama(prompt, model=DEFAULT_MODEL):
    """Call Ollama via OpenAI-compatible API. Returns response text or None."""
    import urllib.error
    import urllib.request

    url = "%s/chat/completions" % OLLAMA_BASE
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 4096,
    }).encode("utf-8")

    try:
        _validate_url(url)
        req = urllib.request.Request(
            url, data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            choices = data.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "")
    except (urllib.error.URLError, OSError, json.JSONDecodeError) as e:
        print("  [WARN] Ollama call failed: %s" % str(e)[:80], file=sys.stderr)

    return None


def _score_artifact_fast(path):
    """Score artifact using Python-only L1+L2."""
    try:
        from cex_score_python import score_fast
        return score_fast(str(path))
    except ImportError:
        from cex_score import score_artifact
        score, notes = score_artifact(str(path))
        return {"score": score, "notes": [notes]}


def phase_build_one(
    target: dict[str, Any],
    model: str = DEFAULT_MODEL,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Attempt to improve a single target.

    Returns: {improved: bool, old_score, new_score, action, error}
    """
    path = ROOT / target["path"]
    if not path.exists():
        return {"improved": False, "error": "file not found"}

    result = {"improved": False, "old_score": 0, "new_score": 0,
              "action": "", "error": None}

    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        result["error"] = str(e)[:80]
        return result

    # Score before
    before = _score_artifact_fast(str(path))
    result["old_score"] = before.get("score", 0)

    ttype = target["type"]

    if ttype == "quality_null":
        # Just score it -- no content change needed
        result["action"] = "score_only"
        result["new_score"] = before.get("score", 0)
        result["improved"] = True
        if not dry_run:
            try:
                from cex_score import update_quality
                update_quality(str(path), before["score"])
            except Exception:
                pass
        return result

    elif ttype == "low_score":
        if dry_run:
            result["action"] = "would_rewrite"
            return result

        # Ask Ollama to improve the weakest areas
        notes = before.get("notes", [])
        notes_str = "; ".join(notes[:5]) if notes else "general improvement needed"

        prompt = (
            "You are a technical editor improving a knowledge artifact.\n\n"
            "## Current Artifact\n```markdown\n%s\n```\n\n"
            "## Issues\n%s\n\n"
            "## Instructions\n"
            "Rewrite the artifact to fix the issues above. Rules:\n"
            "- Keep the YAML frontmatter (---...---) intact\n"
            "- Increase content density (remove filler, add specifics)\n"
            "- Add concrete examples, numbers, or technical details\n"
            "- Keep the same structure (headings, tables)\n"
            "- Output ONLY the complete rewritten artifact, nothing else\n"
        ) % (content[:3000], notes_str)

        response = _call_ollama(prompt, model=model)
        if not response:
            result["error"] = "ollama returned empty"
            return result

        # Validate response has frontmatter
        if not response.strip().startswith("---"):
            # Try to extract markdown from code blocks
            md_match = re.search(r"```(?:markdown)?\n(---.*?)```", response, re.DOTALL)
            if md_match:
                response = md_match.group(1)
            else:
                result["error"] = "response missing frontmatter"
                return result

        result["action"] = "rewrite"
        # Write to temp, score, then decide
        temp_path = path.with_suffix(".tmp.md")
        temp_path.write_text(response, encoding="utf-8")

        after = _score_artifact_fast(str(temp_path))
        result["new_score"] = after.get("score", 0)

        if after["score"] >= QUALITY_FLOOR and after["score"] > before["score"]:
            # Accept improvement
            path.write_text(response, encoding="utf-8")
            result["improved"] = True
            try:
                from cex_score import update_quality
                update_quality(str(path), after["score"])
            except Exception:
                pass
        else:
            result["error"] = "new score %.1f not better than %.1" % (
                after["score"], before["score"])

        # Clean up temp
        if temp_path.exists():
            temp_path.unlink()

        return result

    elif ttype == "hygiene":
        result["action"] = "hygiene_fix"
        # Hygiene fixes are mechanical -- delegate to cex_hygiene
        try:
            r = subprocess.run(
                [sys.executable, str(ROOT / "_tools" / "cex_hygiene.py"),
                 "fix", target["path"]],
                capture_output=True, text=True, timeout=30
            )
            result["improved"] = r.returncode == 0
            result["new_score"] = result["old_score"]
        except Exception as e:
            result["error"] = str(e)[:80]
        return result

    return result


# ================================================================
# Phase 4: VALIDATE (handled inline in phase_build_one)
# ================================================================

# ================================================================
# Phase 5: PERSIST
# ================================================================

def phase_persist(
    cycle_num: int,
    results: list[dict[str, Any]],
    model: str,
) -> dict[str, Any]:
    """Write learning record for this cycle."""
    improved = [r for r in results if r.get("improved")]
    rejected = [r for r in results if not r.get("improved")]

    entry = {
        "cycle": cycle_num,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "model": model,
        "targets_attempted": len(results),
        "targets_improved": len(improved),
        "targets_rejected": len(rejected),
        "details": results,
    }
    append_log(entry)
    return entry


# ================================================================
# Phase 6: VERSION
# ================================================================

def phase_version(
    state: dict[str, Any],
    cycle_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Update state with cycle results."""
    improved = sum(1 for r in cycle_results if r.get("improved"))
    rejected = sum(1 for r in cycle_results if not r.get("improved"))

    state["cycle"] += 1
    state["last_run"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    state["total_improved"] += improved
    state["total_rejected"] += rejected

    # Keep last 50 history entries
    state["history"].append({
        "cycle": state["cycle"],
        "improved": improved,
        "rejected": rejected,
        "duration_s": 0,  # filled by caller
    })
    if len(state["history"]) > 50:
        state["history"] = state["history"][-50:]

    save_state(state)
    return state


# ================================================================
# Main Loop
# ================================================================

def run_cycle(
    mode: str = "preflight",
    model: str = DEFAULT_MODEL,
    max_targets: int = DEFAULT_TARGETS_PER_CYCLE,
) -> dict[str, Any]:
    """Execute one full 6-phase cycle.

    Args:
        mode: "yolo" (autonomous), "interactive" (with prompts), "preflight" (plan only)
        model: Ollama model to use
        max_targets: Max targets per cycle

    Returns:
        dict with cycle results
    """
    state = load_state()
    cycle_num = state["cycle"] + 1
    start_time = time.time()

    print("=" * 60)
    print("  CEX Auto-Research Cycle #%d  [mode=%s, model=%s]" % (
        cycle_num, mode, model))
    print("=" * 60)

    # Phase 1: SCAN
    print("\n[1/6] SCAN...")
    targets = phase_scan()
    state["total_scanned"] = len(targets)
    print("  Found %d targets" % len(targets))
    for t in targets[:10]:
        print("    [%s] %s -- %s" % (t["type"][:8], t["path"][:50], t["reason"][:40]))

    # Phase 2: JUDGE
    print("\n[2/6] JUDGE...")
    selected = phase_judge(targets, max_targets=max_targets)
    print("  Selected %d targets for this cycle" % len(selected))

    if mode == "preflight":
        print("\n[PREFLIGHT] Plan complete. Would process:")
        for i, t in enumerate(selected, 1):
            print("  %d. [%s] %s" % (i, t["type"], t["path"]))
        save_state(state)
        return {"mode": "preflight", "targets": selected, "cycle": cycle_num}

    if mode == "interactive":
        print("\nProceed with %d targets? (y/n): " % len(selected), end="")
        answer = input().strip().lower()
        if answer != "y":
            print("Aborted by user.")
            return {"mode": "interactive", "aborted": True}

    # Phase 3+4: BUILD + VALIDATE
    print("\n[3/6] BUILD + [4/6] VALIDATE...")
    results = []
    for i, target in enumerate(selected, 1):
        print("  [%d/%d] %s %s" % (i, len(selected), target["type"], target["path"][:50]))
        dry_run = (mode == "preflight")
        r = phase_build_one(target, model=model, dry_run=dry_run)
        r["target"] = target
        results.append(r)
        tag = "[OK]" if r.get("improved") else "[--]"
        print("    %s action=%s old=%.1f new=%.1f %s" % (
            tag, r.get("action", "?"),
            r.get("old_score", 0), r.get("new_score", 0),
            r.get("error", "") or ""))

    # Phase 5: PERSIST
    print("\n[5/6] PERSIST...")
    phase_persist(cycle_num, results, model)
    improved = sum(1 for r in results if r.get("improved"))
    rejected = sum(1 for r in results if not r.get("improved"))
    print("  Improved: %d  Rejected: %d" % (improved, rejected))

    # Phase 6: VERSION
    print("\n[6/6] VERSION...")
    duration = time.time() - start_time
    state["mode"] = mode
    state["model"] = model
    state = phase_version(state, results)
    state["history"][-1]["duration_s"] = int(duration)
    save_state(state)
    print("  Cycle #%d complete in %ds" % (state["cycle"], int(duration)))

    # Git commit if YOLO mode
    if mode == "yolo" and improved > 0:
        print("\n[GIT] Committing improvements...")
        try:
            subprocess.run(["git", "add", "-A"], capture_output=True, timeout=30)
            msg = "[AUTO] cycle %d: %d artifacts improved, %d rejected" % (
                state["cycle"], improved, rejected)
            subprocess.run(
                ["git", "commit", "-m", msg],
                capture_output=True, timeout=30
            )
            print("  Committed: %s" % msg)
        except Exception as e:
            print("  [WARN] git commit failed: %s" % str(e)[:80])

    return {
        "mode": mode,
        "cycle": state["cycle"],
        "improved": improved,
        "rejected": rejected,
        "duration_s": int(duration),
        "results": results,
    }


def run_continuous(
    mode: str = "yolo",
    model: str = DEFAULT_MODEL,
    max_cycles: int = 100,
    max_targets: int = DEFAULT_TARGETS_PER_CYCLE,
    pause: int = 30,
) -> None:
    """Run cycles continuously (YOLO mode)."""
    for i in range(max_cycles):
        result = run_cycle(mode=mode, model=model, max_targets=max_targets)

        if result.get("improved", 0) == 0 and result.get("rejected", 0) == 0:
            print("\n[DONE] No more targets to process. Stopping.")
            break

        if i < max_cycles - 1:
            print("\n  Pausing %ds before next cycle..." % pause)
            time.sleep(pause)


# ================================================================
# CLI
# ================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Auto-Research Loop -- versioned self-improving evolution"
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("scan", help="Find improvement targets")

    run_p = sub.add_parser("run", help="Execute improvement cycle(s)")
    run_p.add_argument("--mode", choices=["yolo", "interactive", "preflight"],
                       default="preflight", help="Execution mode")
    run_p.add_argument("--model", default=DEFAULT_MODEL,
                       help="Ollama model (default: %s)" % DEFAULT_MODEL)
    run_p.add_argument("--max-targets", type=int, default=DEFAULT_TARGETS_PER_CYCLE,
                       help="Max targets per cycle")
    run_p.add_argument("--continuous", action="store_true",
                       help="Run multiple cycles (YOLO mode)")
    run_p.add_argument("--max-cycles", type=int, default=100,
                       help="Max cycles in continuous mode")
    run_p.add_argument("--pause", type=int, default=30,
                       help="Seconds between cycles")

    sub.add_parser("status", help="Show current state")
    sub.add_parser("history", help="Show past cycles")

    args = parser.parse_args()

    if args.command == "scan":
        targets = phase_scan()
        print("CEX Auto-Research Scan Results")
        print("=" * 70)
        by_type = {}
        for t in targets:
            by_type.setdefault(t["type"], []).append(t)
        for ttype, items in sorted(by_type.items()):
            print("\n  %s (%d targets):" % (ttype, len(items)))
            for t in items[:10]:
                print("    %s -- %s" % (t["path"][:50], t["reason"][:40]))
            if len(items) > 10:
                print("    ... and %d more" % (len(items) - 10))
        print("\nTotal: %d targets" % len(targets))

    elif args.command == "run":
        if args.continuous and args.mode == "yolo":
            run_continuous(
                mode=args.mode, model=args.model,
                max_cycles=args.max_cycles,
                max_targets=args.max_targets,
                pause=args.pause,
            )
        else:
            run_cycle(
                mode=args.mode, model=args.model,
                max_targets=args.max_targets,
            )

    elif args.command == "status":
        state = load_state()
        print("CEX Auto-Research Status")
        print("  Cycle:          %d" % state["cycle"])
        print("  Last run:       %s" % (state["last_run"] or "never"))
        print("  Total improved: %d" % state["total_improved"])
        print("  Total rejected: %d" % state["total_rejected"])
        print("  Total scanned:  %d" % state["total_scanned"])
        print("  Model:          %s" % state["model"])
        print("  Mode:           %s" % state["mode"])

    elif args.command == "history":
        state = load_state()
        if not state["history"]:
            print("No history yet.")
            return
        print("%-6s | %-8s | %-8s | %-6s" % ("Cycle", "Improved", "Rejected", "Time"))
        print("-" * 40)
        for h in state["history"][-20:]:
            print("%-6d | %-8d | %-8d | %ds" % (
                h["cycle"], h["improved"], h["rejected"],
                h.get("duration_s", 0)))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
