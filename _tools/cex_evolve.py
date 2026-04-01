#!/usr/bin/env python3
"""
cex_evolve.py — Autonomous Experiment Loop (AutoResearch pattern)

Inspired by Karpathy's AutoResearch: give the system one artifact, one metric,
and let it run experiments autonomously. Keep what improves, discard what doesn't.

3-file architecture (mapped to CEX):
  program.md  → CLAUDE.md + builder specs + quality gates (human goals)
  train.py    → The target artifact being evolved (agent modifies)
  prepare.py  → cex_score.py + cex_compile.py + cex_doctor.py (immutable metric)

Modes:
  single <file>          — Evolve one artifact until quality >= threshold
  sweep                  — Evolve all quality:null artifacts
  prompt <file>          — Evolve a system prompt by measuring output quality
  report                 — Show experiment history

Usage:
  python _tools/cex_evolve.py single N01_intelligence/agents/agent_intelligence.md
  python _tools/cex_evolve.py single N01_intelligence/agents/agent_intelligence.md --target 9.0 --max-rounds 10
  python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 3
  python _tools/cex_evolve.py report
  python _tools/cex_evolve.py prompt N01_intelligence/prompts/system_prompt_intelligence.md
"""

import sys
import os
import re
import json
import subprocess
import time
import datetime
import shutil
import hashlib
from pathlib import Path
from typing import Optional

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

RESULTS_DIR = CEX_ROOT / ".cex" / "experiments"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_FILE = RESULTS_DIR / "results.tsv"

# ============================================================
# METRIC: The immutable evaluation (prepare.py equivalent)
# ============================================================

def read_frontmatter(filepath: Path) -> dict:
    """Extract YAML frontmatter from a .md file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def get_current_quality(filepath: Path) -> Optional[float]:
    """Read current quality score from frontmatter."""
    fm = read_frontmatter(filepath)
    q = fm.get("quality", "null")
    if q == "null" or not q:
        return None
    try:
        return float(q)
    except ValueError:
        return None


def score_artifact(filepath: Path) -> Optional[float]:
    """Run cex_score.py and return the score."""
    result = subprocess.run(
        [sys.executable, "_tools/cex_score.py", "--apply", str(filepath)],
        capture_output=True, text=True, timeout=60
    )
    # Parse score from output
    for line in result.stdout.split("\n"):
        if "score:" in line.lower() or "→" in line:
            match = re.search(r"(\d+\.\d+)", line)
            if match:
                return float(match.group(1))
    # Fallback: re-read from file
    return get_current_quality(filepath)


def validate_artifact(filepath: Path) -> bool:
    """Run compile check on artifact."""
    result = subprocess.run(
        [sys.executable, "_tools/cex_compile.py", str(filepath)],
        capture_output=True, text=True, timeout=30
    )
    return result.returncode == 0


def compute_density(filepath: Path) -> float:
    """Compute information density (signal per token)."""
    text = filepath.read_text(encoding="utf-8")
    # Strip frontmatter
    body = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
    words = body.split()
    if not words:
        return 0.0

    # Density heuristics
    total = len(words)
    filler_words = {"the", "a", "an", "is", "are", "was", "were", "be", "been",
                    "being", "have", "has", "had", "do", "does", "did", "will",
                    "would", "could", "should", "may", "might", "shall", "can",
                    "this", "that", "these", "those", "it", "its", "of", "in",
                    "to", "for", "with", "on", "at", "by", "from", "as", "into",
                    "through", "during", "before", "after", "and", "but", "or",
                    "nor", "not", "no", "so", "yet", "both", "either", "neither",
                    "each", "every", "all", "any", "some", "such", "than", "too",
                    "very", "just", "also"}
    filler_count = sum(1 for w in words if w.lower().strip(".,;:!?") in filler_words)
    content_ratio = 1 - (filler_count / total) if total > 0 else 0

    # Structural density: tables, lists, code blocks add density
    table_lines = len(re.findall(r"^\|.*\|$", body, re.MULTILINE))
    list_lines = len(re.findall(r"^[-*]\s", body, re.MULTILINE))
    code_blocks = len(re.findall(r"```", body))
    structure_bonus = min(0.15, (table_lines + list_lines + code_blocks) / max(1, total) * 5)

    density = min(1.0, content_ratio * 0.85 + structure_bonus + 0.10)
    return round(density, 2)


# ============================================================
# EXPERIMENT LEDGER (results.tsv equivalent)
# ============================================================

def init_results():
    """Create results.tsv if it doesn't exist."""
    if not RESULTS_FILE.exists():
        RESULTS_FILE.write_text(
            "timestamp\tfile\tround\tquality\tdensity\tstatus\tdescription\n",
            encoding="utf-8"
        )


def log_result(filepath: str, round_num: int, quality: float,
               density: float, status: str, description: str):
    """Append one experiment result."""
    init_results()
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    q = f"{quality:.1f}" if quality else "0.0"
    d = f"{density:.2f}" if density else "0.00"
    line = f"{ts}\t{filepath}\t{round_num}\t{q}\t{d}\t{status}\t{description}\n"
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(line)


# ============================================================
# GIT OPS (keep/discard via git)
# ============================================================

def git_snapshot(filepath: Path) -> str:
    """Save current state, return content hash."""
    content = filepath.read_text(encoding="utf-8")
    return hashlib.md5(content.encode()).hexdigest()


def git_commit_keep(filepath: Path, msg: str):
    """Commit an improvement."""
    subprocess.run(["git", "add", str(filepath)], capture_output=True)
    subprocess.run(["git", "commit", "-m", msg], capture_output=True)


def git_restore(filepath: Path):
    """Discard changes (git checkout)."""
    subprocess.run(["git", "checkout", "--", str(filepath)], capture_output=True)


# ============================================================
# EVOLUTION ENGINE
# ============================================================

def analyze_weaknesses(filepath: Path) -> list[str]:
    """Analyze an artifact and return improvement suggestions."""
    fm = read_frontmatter(filepath)
    text = filepath.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n?", "", text, flags=re.DOTALL)
    suggestions = []

    # Check density
    density = compute_density(filepath)
    if density < 0.90:
        suggestions.append("increase_density: remove filler words, compress prose into tables")

    # Check frontmatter completeness
    required = {"id", "kind", "title", "version", "created", "author", "quality", "tags", "tldr"}
    missing = required - set(fm.keys())
    if missing:
        suggestions.append(f"fix_frontmatter: missing {', '.join(missing)}")

    # Check density_score field
    if "density_score" not in fm:
        suggestions.append("add_density_score: add density_score field to frontmatter")

    # Check for prose-heavy sections (>5 consecutive non-structured lines)
    lines = body.split("\n")
    prose_run = 0
    for line in lines:
        if line.strip() and not line.startswith("#") and not line.startswith("|") and not line.startswith("-") and not line.startswith("```"):
            prose_run += 1
            if prose_run > 5:
                suggestions.append("reduce_prose: convert long prose sections into tables or bullet lists")
                break
        else:
            prose_run = 0

    # Check for missing sections based on kind
    kind = fm.get("kind", "")
    if kind == "schema" and "Required" not in body and "Field" not in body:
        suggestions.append("add_field_table: schemas need a field/type/description table")
    if kind == "output" and "Template" not in body:
        suggestions.append("add_template: output templates need a ## Template section")
    if kind == "quality_gate" and "Hard Gate" not in body and "H01" not in body:
        suggestions.append("add_hard_gates: quality gates need hard pass/fail checks")

    # Check tags count
    tags_str = fm.get("tags", "[]")
    tag_count = tags_str.count(",") + 1 if tags_str != "[]" else 0
    if tag_count < 3:
        suggestions.append("add_tags: minimum 3 tags required")

    # Check tldr length
    tldr = fm.get("tldr", "").strip('"\'')
    if len(tldr) < 20:
        suggestions.append("improve_tldr: tldr should be 20-200 chars")
    elif len(tldr) > 200:
        suggestions.append("shorten_tldr: tldr exceeds 200 chars")

    if not suggestions:
        suggestions.append("polish: minor wording and structure improvements")

    return suggestions


def apply_improvement(filepath: Path, suggestion: str) -> str:
    """Apply a specific improvement to an artifact. Returns description."""
    text = filepath.read_text(encoding="utf-8")

    if "fix_frontmatter" in suggestion:
        # Add missing frontmatter fields
        field = suggestion.split("missing ")[-1].split(",")[0].strip()
        if field == "density_score" or "add_density_score" in suggestion:
            density = compute_density(filepath)
            if "density_score" not in text:
                text = text.replace("\n---", f"\ndensity_score: {density}\n---", 1)
                filepath.write_text(text, encoding="utf-8")
                return f"added density_score: {density}"

    if "add_density_score" in suggestion:
        density = compute_density(filepath)
        if "density_score" not in text:
            text = text.replace("\n---", f"\ndensity_score: {density}\n---", 1)
            filepath.write_text(text, encoding="utf-8")
            return f"added density_score: {density}"

    if "increase_density" in suggestion:
        # Remove common filler phrases
        replacements = [
            ("In this section, we will discuss ", ""),
            ("It is important to note that ", ""),
            ("As mentioned earlier, ", ""),
            ("Please note that ", ""),
            ("It should be noted that ", ""),
            ("In order to ", "To "),
            ("Due to the fact that ", "Because "),
            ("At this point in time ", "Now "),
            ("In the event that ", "If "),
            ("For the purpose of ", "For "),
            ("With regard to ", "Regarding "),
            ("In terms of ", "In "),
            ("A large number of ", "Many "),
            ("The majority of ", "Most "),
            ("In the near future ", "Soon "),
        ]
        changes = 0
        for old, new in replacements:
            if old in text:
                text = text.replace(old, new)
                changes += 1
        if changes > 0:
            filepath.write_text(text, encoding="utf-8")
            return f"removed {changes} filler phrases"

    if "improve_tldr" in suggestion or "shorten_tldr" in suggestion:
        # Just flag it — needs LLM for good tldr rewrite
        return "tldr flagged for manual review"

    if "polish" in suggestion:
        # Ensure consistent formatting
        text = re.sub(r"\n{3,}", "\n\n", text)  # Remove triple+ newlines
        text = re.sub(r" +\n", "\n", text)  # Remove trailing spaces
        filepath.write_text(text, encoding="utf-8")
        return "polished formatting (whitespace cleanup)"

    return f"analyzed: {suggestion}"


def evolve_single(filepath: Path, target: float = 9.0, max_rounds: int = 5,
                  verbose: bool = True) -> dict:
    """
    Evolve a single artifact through the experiment loop.
    Returns dict with final quality, rounds run, status.
    """
    fp = Path(filepath)
    if not fp.exists():
        print(f"[ERROR] File not found: {fp}")
        return {"status": "error", "quality": 0, "rounds": 0}

    if verbose:
        print(f"\n{'='*60}")
        print(f"[EVOLVE] {fp}")
        print(f"  Target: {target} | Max rounds: {max_rounds}")
        print(f"{'='*60}")

    # Baseline measurement
    baseline_hash = git_snapshot(fp)
    baseline_quality = get_current_quality(fp)
    baseline_density = compute_density(fp)

    if baseline_quality and baseline_quality >= target:
        if verbose:
            print(f"  ✅ Already at {baseline_quality} (>= {target}). Skipping.")
        log_result(str(fp), 0, baseline_quality, baseline_density, "skip", "already at target")
        return {"status": "skip", "quality": baseline_quality, "rounds": 0}

    if verbose:
        print(f"  Baseline: quality={baseline_quality or 'null'}, density={baseline_density}")

    best_quality = baseline_quality or 0.0
    rounds_run = 0

    for round_num in range(1, max_rounds + 1):
        rounds_run = round_num
        if verbose:
            print(f"\n  --- Round {round_num}/{max_rounds} ---")

        # Analyze weaknesses
        suggestions = analyze_weaknesses(fp)
        if verbose:
            print(f"  Suggestions: {', '.join(s.split(':')[0] for s in suggestions)}")

        # Apply first actionable improvement
        description = "no change"
        for suggestion in suggestions:
            description = apply_improvement(fp, suggestion)
            if description != f"analyzed: {suggestion}":
                break

        if verbose:
            print(f"  Applied: {description}")

        # Validate
        if not validate_artifact(fp):
            if verbose:
                print(f"  ❌ Compile failed. Reverting.")
            git_restore(fp)
            log_result(str(fp), round_num, 0, 0, "crash", f"compile fail after: {description}")
            continue

        # Measure
        new_density = compute_density(fp)
        new_quality = score_artifact(fp)
        if new_quality is None:
            new_quality = best_quality  # Score didn't change

        if verbose:
            print(f"  Result: quality={new_quality}, density={new_density}")

        # Keep or discard (the AutoResearch pattern)
        if new_quality > best_quality:
            # KEEP
            best_quality = new_quality
            git_commit_keep(fp, f"[evolve] {fp.name}: {description} (q={new_quality})")
            log_result(str(fp), round_num, new_quality, new_density, "keep", description)
            if verbose:
                print(f"  ✅ KEEP (improved to {new_quality})")

            if new_quality >= target:
                if verbose:
                    print(f"  🎯 Target {target} reached!")
                break
        else:
            # DISCARD
            git_restore(fp)
            log_result(str(fp), round_num, new_quality, new_density, "discard", description)
            if verbose:
                print(f"  ↩️  DISCARD (no improvement: {new_quality} <= {best_quality})")

    return {"status": "complete", "quality": best_quality, "rounds": rounds_run}


def evolve_sweep(target: float = 8.5, max_rounds: int = 3, verbose: bool = True):
    """Evolve all quality:null artifacts."""
    # Find all quality:null files
    null_files = []
    for root, _, files in os.walk(CEX_ROOT):
        if ".git" in root or "_archive" in root or "node_modules" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                fp = Path(root) / f
                q = get_current_quality(fp)
                if q is None:
                    fm = read_frontmatter(fp)
                    if fm.get("quality") == "null":
                        null_files.append(fp)

    print(f"\n[SWEEP] Found {len(null_files)} artifacts with quality:null")
    print(f"  Target: {target} | Max rounds per artifact: {max_rounds}")

    results = []
    for i, fp in enumerate(null_files):
        print(f"\n[{i+1}/{len(null_files)}] {fp.relative_to(CEX_ROOT)}")
        result = evolve_single(fp, target=target, max_rounds=max_rounds, verbose=verbose)
        results.append({"file": str(fp.relative_to(CEX_ROOT)), **result})

    # Summary
    kept = sum(1 for r in results if r["status"] == "complete" and r["quality"] >= target)
    skipped = sum(1 for r in results if r["status"] == "skip")
    print(f"\n{'='*60}")
    print(f"[SWEEP COMPLETE]")
    print(f"  Total: {len(results)} | Reached target: {kept} | Already ok: {skipped}")
    print(f"{'='*60}")


def show_report():
    """Display experiment history."""
    if not RESULTS_FILE.exists():
        print("[REPORT] No experiments recorded yet.")
        return

    lines = RESULTS_FILE.read_text(encoding="utf-8").strip().split("\n")
    print(f"\n{'='*80}")
    print(f"EXPERIMENT HISTORY ({len(lines)-1} experiments)")
    print(f"{'='*80}")

    # Parse and summarize
    keeps = 0
    discards = 0
    crashes = 0
    skips = 0
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) >= 6:
            status = parts[5]
            if status == "keep":
                keeps += 1
            elif status == "discard":
                discards += 1
            elif status == "crash":
                crashes += 1
            elif status == "skip":
                skips += 1

    print(f"  Keep: {keeps} | Discard: {discards} | Crash: {crashes} | Skip: {skips}")
    print(f"\nLast 20 experiments:")
    for line in lines[-20:]:
        print(f"  {line}")


# ============================================================
# CLI
# ============================================================

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return

    mode = sys.argv[1]

    if mode == "single":
        if len(sys.argv) < 3:
            print("Usage: cex_evolve.py single <file> [--target N] [--max-rounds N]")
            return
        filepath = Path(sys.argv[2])
        target = 9.0
        max_rounds = 5
        for i, arg in enumerate(sys.argv[3:], 3):
            if arg == "--target" and i + 1 < len(sys.argv):
                target = float(sys.argv[i + 1])
            if arg == "--max-rounds" and i + 1 < len(sys.argv):
                max_rounds = int(sys.argv[i + 1])
        evolve_single(filepath, target=target, max_rounds=max_rounds)

    elif mode == "sweep":
        target = 8.5
        max_rounds = 3
        for i, arg in enumerate(sys.argv[2:], 2):
            if arg == "--target" and i + 1 < len(sys.argv):
                target = float(sys.argv[i + 1])
            if arg == "--max-rounds" and i + 1 < len(sys.argv):
                max_rounds = int(sys.argv[i + 1])
        evolve_sweep(target=target, max_rounds=max_rounds)

    elif mode == "report":
        show_report()

    elif mode == "prompt":
        if len(sys.argv) < 3:
            print("Usage: cex_evolve.py prompt <system_prompt.md>")
            return
        print("[TODO] Prompt evolution requires LLM integration. Use /evolve command for now.")

    else:
        print(f"Unknown mode: {mode}. Use: single, sweep, prompt, report")


if __name__ == "__main__":
    main()
