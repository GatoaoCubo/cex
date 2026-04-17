#!/usr/bin/env python3
"""CEX Evolve Ollama -- LLM-powered artifact improvement via local models.

Targets artifacts the heuristic can't push past 8.7. Uses Ollama (free,
local) to rewrite content: add tables, cross-refs, expand sections.

Architecture (Karpathy AutoResearch):
  1. Read artifact + score
  2. Send to Ollama with improvement prompt
  3. Write result, score
  4. Keep if improved, git restore if not
  5. Commit batch, repeat

Usage:
  python _tools/cex_evolve_ollama.py                    # default: below 9.0
  python _tools/cex_evolve_ollama.py --target 9.5       # push higher
  python _tools/cex_evolve_ollama.py --model qwen3:8b   # lighter model
  python _tools/cex_evolve_ollama.py --dry-run           # preview targets
  python _tools/cex_evolve_ollama.py --max-cycles 50     # limit cycles
  python _tools/cex_evolve_ollama.py --scope P01         # single pillar
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Force unbuffered output for background execution
import functools
print = functools.partial(print, flush=True)

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

OLLAMA_URL = "http://localhost:11434/api/chat"
SKIP_DIRS = {'.git', 'node_modules', '.cex/cache', 'compiled', '_external'}

# ============================================================
# SCORING (reuse from cex_evolve.py)
# ============================================================

def read_frontmatter(filepath: Path) -> dict[str, str]:
    text = filepath.read_text(encoding="utf-8", errors="ignore")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def get_quality(filepath: Path) -> float | None:
    fm = read_frontmatter(filepath)
    q = fm.get("quality", "null")
    if q == "null" or not q:
        return None
    try:
        return float(q)
    except ValueError:
        return None


def score_artifact(filepath: Path) -> float | None:
    """Run cex_score.py and return score."""
    result = subprocess.run(
        [sys.executable, "_tools/cex_score.py", "--apply", str(filepath)],
        capture_output=True, text=True, timeout=60, cwd=str(CEX_ROOT)
    )
    for line in result.stdout.split("\n"):
        if "score:" in line.lower() or "->" in line:
            m = re.search(r"(\d+\.\d+)", line)
            if m:
                return float(m.group(1))
    return get_quality(filepath)


def compile_artifact(filepath: Path) -> bool:
    result = subprocess.run(
        [sys.executable, "_tools/cex_compile.py", str(filepath)],
        capture_output=True, text=True, timeout=30, cwd=str(CEX_ROOT)
    )
    return result.returncode == 0


# ============================================================
# OLLAMA CLIENT
# ============================================================

def ollama_chat(
    model: str,
    system_msg: str,
    user_msg: str,
    max_tokens: int = 6000,
    temperature: float = 0.4,
) -> str | None:
    """Call Ollama native API. Uses /no_think to disable qwen3 reasoning."""
    # Prepend /no_think to user message to disable thinking mode
    user_msg_patched = "/no_think\n" + user_msg

    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg_patched}
        ],
        "stream": False,
        "options": {
            "num_predict": max_tokens,
            "temperature": temperature
        }
    }).encode("utf-8")

    req = Request(OLLAMA_URL, data=payload,
                  headers={"Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            msg = data.get("message", {})
            content = msg.get("content", "")
            # Fallback: qwen3 sometimes still puts output in thinking
            if not content and msg.get("thinking"):
                content = msg.get("thinking", "")
            tokens = data.get("eval_count", 0)
            duration = data.get("total_duration", 0) / 1e9
            print(f"({tokens}tok, {duration:.1f}s)", end=" ", flush=True)
            return content
    except URLError as e:
        print(f"[OLLAMA ERROR: {e}]", end=" ", flush=True)
        return None
    except Exception as e:
        print(f"[OLLAMA ERROR: {e}]", end=" ", flush=True)
        return None


def check_ollama(model: str) -> bool:
    """Verify Ollama is running and model exists."""
    try:
        req = Request("http://localhost:11434/api/tags")
        with urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            models = [m["name"] for m in data.get("models", [])]
            # Check for exact or prefix match
            for m in models:
                if m == model or m.startswith(model.split(":")[0]):
                    return True
            print(f"[ERROR] Model '{model}' not found. Available: {models}")
            return False
    except Exception as e:
        print(f"[ERROR] Ollama not reachable: {e}")
        return False


# ============================================================
# DISCOVERY
# ============================================================

def find_targets(target_score: float = 9.0, scope: str | None = None) -> list[tuple[float, float, Path]]:
    """Find artifacts below target with numeric quality."""
    results = []
    for root, dirs, files in os.walk(CEX_ROOT):
        if any(skip in root.replace("\\", "/") for skip in SKIP_DIRS):
            continue
        if scope and scope not in root:
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            path = Path(root) / f
            try:
                txt = path.read_text(encoding='utf-8', errors='ignore')
                if '---' not in txt[:10]:
                    continue
                m = re.search(r'quality:\s*([\d.]+)', txt[:500])
                if m:
                    q = float(m.group(1))
                    if 0 < q < target_score:
                        # Compute opportunity score
                        lines = len(txt.splitlines())
                        tables = txt.count('|') // 3
                        has_boundary = '## Boundary' in txt
                        has_related = '## Related' in txt or '## See Also' in txt
                        # Priority: fewer tables + no boundary = more opportunity
                        opp = 0
                        if tables == 0 and lines > 30:
                            opp += 15
                        if not has_boundary:
                            opp += 5
                        if not has_related:
                            opp += 5
                        opp += max(0, (9.0 - q) * 10)
                        results.append((opp, q, path))
            except Exception:
                pass
    results.sort(reverse=True)  # highest opportunity first
    return results


# ============================================================
# IMPROVEMENT PROMPT
# ============================================================

SYSTEM_PROMPT = """You are a CEX artifact improver. You receive a markdown artifact with YAML frontmatter and must return an IMPROVED version.

Rules:
1. Keep the YAML frontmatter block (--- to ---) intact. Only change quality if scoring changes.
2. NEVER remove existing content. Only ADD or RESTRUCTURE.
3. Add tables where prose exists. Tables > prose. Minimum 4 columns, 5 rows.
4. Add a ## Boundary section if missing: 1-2 sentences defining what this artifact IS and IS NOT.
5. Add a ## Related Kinds section if missing: list 3-5 related CEX kinds with 1-sentence relationships.
6. Expand thin sections (< 3 lines) with concrete examples, data, or comparisons.
7. All text must be English only. No emojis. No smart quotes.
8. Output ONLY the improved markdown. No explanations before or after.
9. Keep existing structure headers. Do not rename sections.
10. Target: information density >= 0.85. Every line must carry signal."""


def build_user_prompt(filepath: Path, content: str, quality: float) -> str:
    """Build the improvement prompt for a specific artifact."""
    fm = read_frontmatter(filepath)
    kind = fm.get("kind", "unknown")
    lines = len(content.splitlines())
    tables = content.count('|') // 3
    has_boundary = '## Boundary' in content
    has_related = '## Related' in content or '## See Also' in content

    needs = []
    if tables == 0 and lines > 30:
        needs.append("ADD at least one comparison/reference table (4+ cols, 5+ rows)")
    if not has_boundary:
        needs.append("ADD ## Boundary section (what this IS vs IS NOT)")
    if not has_related:
        needs.append("ADD ## Related Kinds section (3-5 related kinds with relationships)")
    if lines < 60:
        needs.append("EXPAND content to at least 80 lines with concrete data")
    if not needs:
        needs.append("DENSIFY: replace prose with structured data (tables, lists)")
        needs.append("ADD concrete examples, metrics, or comparison data")

    needs_str = "\n".join(f"- {n}" for n in needs)

    return f"""Artifact: {filepath.name}
Kind: {kind}
Current quality: {quality}
Lines: {lines} | Tables: {tables}

REQUIRED IMPROVEMENTS:
{needs_str}

CURRENT CONTENT:
{content}

Return the COMPLETE improved artifact (frontmatter + body). Nothing else."""


# ============================================================
# EVOLVE LOOP
# ============================================================

def evolve_one(filepath: Path, model: str, target: float = 9.0) -> tuple[float | None, str]:
    """Send one artifact to Ollama, apply result, score, keep/discard."""
    content = filepath.read_text(encoding="utf-8", errors="ignore")
    quality = get_quality(filepath) or 0.0

    # Build prompt
    user_prompt = build_user_prompt(filepath, content, quality)

    # Call Ollama
    result = ollama_chat(model, SYSTEM_PROMPT, user_prompt,
                         max_tokens=6000, temperature=0.4)

    if not result or len(result.strip()) < 20:
        return None, "empty response"

    # Clean: extract markdown if wrapped in code block
    if result.startswith("```"):
        result = re.sub(r"^```\w*\n", "", result)
        result = re.sub(r"\n```\s*$", "", result)

    # Validate: must have frontmatter
    if "---" not in result[:10]:
        return None, "no frontmatter in response"

    # Save original for rollback
    original = content
    original_hash = hashlib.md5(content.encode()).hexdigest()

    # Write new content
    filepath.write_text(result, encoding="utf-8")

    # Check it compiles
    if not compile_artifact(filepath):
        filepath.write_text(original, encoding="utf-8")
        return None, "compile failed"

    # Score
    new_quality = score_artifact(filepath)
    if new_quality is None:
        new_quality = get_quality(filepath) or 0.0

    # Keep or discard
    if new_quality > quality:
        # KEEP -- retry git ops in case of lock contention
        for attempt in range(3):
            r1 = subprocess.run(["git", "add", str(filepath)],
                                capture_output=True, cwd=str(CEX_ROOT))
            msg = f"[evolve-ollama] {filepath.name}: {quality:.1f} -> {new_quality:.1f}"
            r2 = subprocess.run(["git", "commit", "-m", msg],
                                capture_output=True, text=True, cwd=str(CEX_ROOT))
            if r2.returncode == 0:
                break
            time.sleep(2 + attempt * 3)  # backoff: 2s, 5s, 8s
        return new_quality, "improved"
    else:
        # DISCARD
        filepath.write_text(original, encoding="utf-8")
        return quality, f"no improvement ({new_quality:.1f} <= {quality:.1f})"


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Evolve via Ollama")
    parser.add_argument("--model", default="qwen3:14b",
                        help="Ollama model (default: qwen3:14b)")
    parser.add_argument("--target", type=float, default=9.0)
    parser.add_argument("--batch", type=int, default=6,
                        help="Artifacts per cycle")
    parser.add_argument("--max-cycles", type=int, default=200)
    parser.add_argument("--sleep", type=int, default=2,
                        help="Seconds between artifacts (GPU cooldown)")
    parser.add_argument("--scope", default=None,
                        help="Filter path (e.g. P01, N03, archetypes)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("=" * 60)
    print("CEX EVOLVE OLLAMA FLYWHEEL")
    print(f"  Model: {args.model} | Target: {args.target}")
    print(f"  Batch: {args.batch} | Max cycles: {args.max_cycles}")
    if args.scope:
        print(f"  Scope: {args.scope}")
    print("=" * 60)

    if not args.dry_run:
        if not check_ollama(args.model):
            sys.exit(1)

    for cycle in range(1, args.max_cycles + 1):
        targets = find_targets(args.target, args.scope)
        if not targets:
            print(f"\n[DONE] No artifacts below {args.target}.")
            break

        batch = targets[:args.batch]
        print(f"\n--- Cycle {cycle} | {len(targets)} targets remaining ---")

        improved = 0
        failed = 0

        for opp_score, quality, path in batch:
            rel = path.relative_to(CEX_ROOT)
            print(f"  [{quality:.1f}] {rel}", end=" ", flush=True)

            if args.dry_run:
                print(f"[DRY-RUN] opp={opp_score}")
                continue

            try:
                new_q, reason = evolve_one(path, args.model, args.target)
                if new_q and new_q > quality:
                    print(f"-> {new_q:.1f} [OK]")
                    improved += 1
                else:
                    print(f"[{reason}]")
                    failed += 1
            except Exception as e:
                print(f"[ERROR: {e}]")
                failed += 1
                # Restore just in case
                subprocess.run(["git", "checkout", "--", str(path)],
                               capture_output=True, cwd=str(CEX_ROOT))

            time.sleep(args.sleep)

        if args.dry_run:
            break

        print(f"  Cycle {cycle}: {improved} improved, {failed} unchanged")

        # Batch commit summary if any stragglers
        if improved > 0:
            subprocess.run(["git", "add", "-A"], capture_output=True,
                           cwd=str(CEX_ROOT))
            subprocess.run(
                ["git", "diff", "--cached", "--quiet"],
                capture_output=True, cwd=str(CEX_ROOT)
            )

    print("\n[FLYWHEEL] Complete.")


if __name__ == "__main__":
    main()
