#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_evolve.py -- Autonomous Experiment Loop (Karpathy AutoResearch pattern)

Three modes:
  agent   -- TRUE AutoResearch via SDK: Python controls the loop, LLM
            generates creative hypotheses via execute_prompt(). Budget-
            tracked, provider-agnostic, no subprocess spawning.
            This is the Karpathy pattern done right.

  auto    -- Hybrid post-hook: heuristic pass (free) + agent mode only
            if score < threshold. Designed to be called automatically
            after every artifact creation. Smart budget usage.

  heuristic -- Fast fallback: Python heuristics (no LLM) do mechanical
              fixes (frontmatter, whitespace, filler). Useful for batch
              scoring when LLM budget is limited.

3-file architecture (Karpathy original):
  program.md  -> strategy hints for the LLM (human-written, read-only)
  target file -> the ONE artifact the LLM improves per round
  cex_score.py + cex_compile.py -> immutable metric (never touched)

Usage:
  # True AutoResearch via SDK (budget-tracked):
  python _tools/cex_evolve.py agent <file>
  python _tools/cex_evolve.py agent <file> --budget 50000 --target 9.0

  # Hybrid auto-hook (heuristic + agent if needed):
  python _tools/cex_evolve.py auto <file>
  python _tools/cex_evolve.py auto <file> --threshold 8.5

  # Heuristic fallback (no LLM, fast batch):
  python _tools/cex_evolve.py single <file> --target 9.0
  python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 3
  python _tools/cex_evolve.py report
"""

import argparse
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
        if "score:" in line.lower() or "->" in line:
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


def heuristic_quality(filepath: Path) -> float:
    """Compute heuristic quality estimate via structural + rubric scoring (no LLM).

    Uses score_structural + score_rubric directly -- no subprocess, no LLM tokens.
    Returns average of both layers on 0-10 scale.
    """
    tools_dir = str(Path(__file__).resolve().parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    try:
        from cex_score import score_structural, score_rubric
        struct_raw, _ = score_structural(str(filepath))
        rubric_raw, _, _ = score_rubric(str(filepath))
        return round((struct_raw + rubric_raw) / 2, 1)
    except Exception:
        return 0.0


def write_heuristic_quality(filepath: Path) -> float:
    """Compute and persist heuristic quality to frontmatter. Returns the score.

    Handles both quality:null (replace) and missing quality field (insert after id:).
    """
    q = heuristic_quality(filepath)
    if q <= 0:
        return q
    tools_dir = str(Path(__file__).resolve().parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    try:
        from cex_score import update_quality
        wrote = update_quality(str(filepath), q)
        if not wrote:
            # quality field is absent -- insert after the first frontmatter field
            text = filepath.read_text(encoding="utf-8")
            fm_match = re.match(r"^(---\n)", text)
            if fm_match:
                insert_pos = fm_match.end()
                text = text[:insert_pos] + f"quality: {q}\n" + text[insert_pos:]
                filepath.write_text(text, encoding="utf-8")
    except Exception:
        pass
    return q


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

    # Check updated field
    if "updated" not in fm:
        suggestions.append("add_updated: add updated date field to frontmatter")

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
        # Just flag it -- needs LLM for good tldr rewrite
        return "tldr flagged for manual review"

    if "add_tags" in suggestion:
        # Auto-generate tags from frontmatter kind + domain + title
        fm = read_frontmatter(filepath)
        kind = fm.get("kind", "")
        domain = fm.get("domain", "")
        pillar = fm.get("pillar", "")
        auto_tags = [t for t in [kind, domain, pillar] if t]
        if auto_tags and "tags:" in text:
            old_tags = re.search(r'tags:\s*\[.*?\]', text)
            if old_tags:
                new_tag_str = f"tags: [{', '.join(auto_tags)}]"
                text = text.replace(old_tags.group(), new_tag_str)
                filepath.write_text(text, encoding="utf-8")
                return f"auto-generated {len(auto_tags)} tags from metadata"

    if "add_updated" in suggestion or ("fix_frontmatter" in suggestion and "updated" in suggestion):
        # Add updated field with today's date
        if "updated:" not in text:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            text = text.replace("\n---", f'\nupdated: "{today}"\n---', 1)
            filepath.write_text(text, encoding="utf-8")
            return f"added updated: {today}"

    if "polish" in suggestion:
        # Ensure consistent formatting
        text = re.sub(r"\n{3,}", "\n\n", text)  # Remove triple+ newlines
        text = re.sub(r" +\n", "\n", text)  # Remove trailing spaces
        text = re.sub(r"\t", "  ", text)  # Tabs to 2 spaces
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
            print(f"  [OK] Already at {baseline_quality} (>= {target}). Skipping.")
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
                print(f"  [FAIL] Compile failed. Reverting.")
            git_restore(fp)
            log_result(str(fp), round_num, 0, 0, "crash", f"compile fail after: {description}")
            continue

        # Write heuristic quality immediately after each improvement (Bug 1 fix).
        # This ensures quality:null -> quality:X.X even if score_artifact subprocess fails.
        if description not in ("no change",) and not description.startswith("analyzed:"):
            write_heuristic_quality(fp)

        # Measure
        new_density = compute_density(fp)
        new_quality = score_artifact(fp)
        if new_quality is None:
            # Fallback: heuristic quality already written above; re-read it
            new_quality = get_current_quality(fp) or best_quality

        if verbose:
            print(f"  Result: quality={new_quality}, density={new_density}")

        # Keep or discard (the AutoResearch pattern)
        if new_quality > best_quality:
            # KEEP
            best_quality = new_quality
            git_commit_keep(fp, f"[evolve] {fp.name}: {description} (q={new_quality})")
            log_result(str(fp), round_num, new_quality, new_density, "keep", description)
            if verbose:
                print(f"  [OK] KEEP (improved to {new_quality})")

            if new_quality >= target:
                if verbose:
                    print(f"  [>>] Target {target} reached!")
                break
        else:
            # DISCARD
            git_restore(fp)
            log_result(str(fp), round_num, new_quality, new_density, "discard", description)
            if verbose:
                print(f"  <-  DISCARD (no improvement: {new_quality} <= {best_quality})")

    return {"status": "complete", "quality": best_quality, "rounds": rounds_run}


def _sweep_priority(fp: Path) -> float:
    """Sort key for sweep: null=0 (highest priority), then ascending by quality."""
    q = get_current_quality(fp)
    if q is None:
        return 0.0
    return q


def evolve_sweep(target: float = 8.5, max_rounds: int = 3,
                 apply_scores: bool = False, verbose: bool = True):
    """Evolve artifacts: quality:null first (unscored), then below-target sorted ascending.

    Priority order (Bug 2 fix):
      1. quality:null files -- unscored, unknown quality, highest risk
      2. quality < target files -- known bad, sorted worst-first
      3. quality >= target -- skipped
    """
    null_files = []
    low_files = []

    for root, _, files in os.walk(CEX_ROOT):
        if ".git" in root or "_archive" in root or "node_modules" in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            fp = Path(root) / f
            fm = read_frontmatter(fp)
            if not fm.get("kind"):
                continue  # skip non-artifact markdown files
            q_raw = fm.get("quality", "")
            if q_raw == "null" or not q_raw:
                null_files.append(fp)
            else:
                try:
                    q = float(q_raw)
                    if q < target:
                        low_files.append((q, fp))
                except ValueError:
                    null_files.append(fp)

    # Sort low-quality ascending: worst quality gets fixed first
    low_files.sort(key=lambda x: x[0])
    all_files = null_files + [fp for _, fp in low_files]

    print(f"\n[SWEEP] quality:null={len(null_files)} | below-target={len(low_files)} | total={len(all_files)}")
    print(f"  Target: {target} | Max rounds per artifact: {max_rounds}")

    improved_files = []
    results = []
    for i, fp in enumerate(all_files):
        print(f"\n[{i+1}/{len(all_files)}] {fp.relative_to(CEX_ROOT)}")
        result = evolve_single(fp, target=target, max_rounds=max_rounds, verbose=verbose)
        results.append({"file": str(fp.relative_to(CEX_ROOT)), **result})
        if result.get("status") == "complete" and result.get("quality", 0) > 0:
            improved_files.append(fp)

    # --apply-scores: final pass that writes structural+rubric scores to all improved files
    if apply_scores and improved_files:
        print(f"\n[APPLY SCORES] Writing heuristic scores to {len(improved_files)} improved files...")
        tools_dir = str(Path(__file__).resolve().parent)
        if tools_dir not in sys.path:
            sys.path.insert(0, tools_dir)
        try:
            from cex_score import score_structural, score_rubric, update_quality
            for fp in improved_files:
                struct_raw, _ = score_structural(str(fp))
                rubric_raw, _, _ = score_rubric(str(fp))
                q = round((struct_raw + rubric_raw) / 2, 1)
                update_quality(str(fp), q)
                if verbose:
                    print(f"  [SCORE] {fp.name}: {q}")
        except Exception as e:
            print(f"  [WARN] apply_scores failed: {e}")

    # Summary
    kept = sum(1 for r in results if r["status"] == "complete" and r.get("quality", 0) >= target)
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
# AGENT MODE -- True AutoResearch via SDK (Python controls, LLM thinks)
# ============================================================

def _get_execute_prompt():
    """Import execute_prompt from cex_intent.py (the single SDK gateway)."""
    tools_dir = str(Path(__file__).resolve().parent)
    if tools_dir not in sys.path:
        sys.path.insert(0, tools_dir)
    from cex_intent import execute_prompt
    return execute_prompt


def _load_strategy_hints() -> str:
    """Load program.md strategy hints (optional, not required)."""
    program = CEX_ROOT / "program.md"
    if not program.exists():
        return ""
    text = program.read_text(encoding="utf-8")
    # Extract just the Strategy and Quality Dimensions sections
    lines = text.split("\n")
    relevant = []
    capture = False
    for line in lines:
        if line.startswith("## Quality Dimensions") or line.startswith("## Strategy"):
            capture = True
        elif line.startswith("## ") and capture:
            capture = False
        if capture:
            relevant.append(line)
    return "\n".join(relevant) if relevant else text[:2000]


def evolve_agent(filepath: Path, budget_tokens: int = 50000,
                 target: float = 9.0, max_rounds: int = 10,
                 verbose: bool = True) -> dict:
    """
    TRUE AutoResearch via SDK -- Python controls the loop, LLM generates hypotheses.

    Architecture:
    - Python reads the artifact, sends it to LLM via execute_prompt()
    - LLM returns ONE hypothesis + modified content (structured)
    - Python applies the change, scores it, keeps/discards via git
    - Budget tracked via cumulative token count from SDK metrics
    - Loop stops when: target reached, budget exhausted, or max_rounds hit

    Goes through execute_prompt() -> SDK cascade -> tracked, budget-aware.
    No subprocess spawning. No CLI dependency. Works with any configured provider.

    Returns dict with: status, quality, rounds, tokens_used
    """
    fp = Path(filepath)
    if not fp.exists():
        print(f"[ERROR] File not found: {fp}")
        return {"status": "error", "quality": 0, "rounds": 0, "tokens_used": 0}

    # Get the SDK gateway
    try:
        execute_prompt = _get_execute_prompt()
    except ImportError as e:
        print(f"[ERROR] Cannot import execute_prompt: {e}")
        return {"status": "error", "quality": 0, "rounds": 0, "tokens_used": 0}

    # Baseline -- use hybrid scoring for dimension breakdown
    try:
        from cex_score import score_hybrid
        hybrid_result = score_hybrid(str(fp), use_cache=False, force_semantic=True, verbose=verbose)
        baseline_quality = hybrid_result.get("score", 0.0)
        dimension_breakdown = hybrid_result.get("dimensions", {})
        weakest_dim = hybrid_result.get("weakest", "")
        dim_suggestion = hybrid_result.get("suggestion", "")
    except Exception:
        baseline_quality = score_artifact(fp) or 0.0
        dimension_breakdown = {}
        weakest_dim = ""
        dim_suggestion = ""

    baseline_density = compute_density(fp)
    strategy_hints = _load_strategy_hints()
    tokens_used = 0
    best_quality = baseline_quality

    if baseline_quality >= target:
        if verbose:
            print(f"  [OK] Already at {baseline_quality} (>= {target}). Skipping.")
        log_result(str(fp), 0, baseline_quality, baseline_density, "skip", "already at target")
        return {"status": "skip", "quality": baseline_quality, "rounds": 0, "tokens_used": 0}

    if verbose:
        print(f"\n{'='*60}")
        print(f"[AGENT MODE via SDK] AutoResearch + Hybrid Scoring")
        print(f"  Target:   {fp}")
        print(f"  Baseline: {baseline_quality}")
        print(f"  Target:   {target}")
        print(f"  Budget:   {budget_tokens:,} tokens")
        print(f"  Rounds:   max {max_rounds}")
        if weakest_dim:
            print(f"  Weakest:  {weakest_dim}")
            print(f"  Fix hint: {dim_suggestion[:80]}")
        print(f"{'='*60}")

    rounds_run = 0
    experiment_log = []  # track what worked/failed for context

    for round_num in range(1, max_rounds + 1):
        rounds_run = round_num

        # Budget check BEFORE calling LLM
        if tokens_used >= budget_tokens:
            if verbose:
                print(f"\n  [$] Budget exhausted ({tokens_used:,}/{budget_tokens:,} tokens)")
            break

        remaining_budget = budget_tokens - tokens_used
        content = fp.read_text(encoding="utf-8")
        density = compute_density(fp)

        # Build prompt -- LLM sees artifact + history + strategy
        history_summary = ""
        if experiment_log:
            recent = experiment_log[-5:]  # last 5 experiments
            history_lines = [f"  R{e['round']}: {e['status']} ({e['description']})" for e in recent]
            history_summary = f"\n\nExperiment history (don't repeat failed ideas):\n" + "\n".join(history_lines)

        # Build dimension breakdown section (GDP D04)
        dim_section = ""
        if dimension_breakdown:
            dim_lines = []
            for dim_id, dim_info in sorted(dimension_breakdown.items()):
                desc = dim_info.get("description", dim_id) if isinstance(dim_info, dict) else dim_id
                h_score = dim_info.get("heuristic", "?") if isinstance(dim_info, dict) else "?"
                s_score = dim_info.get("semantic", "?") if isinstance(dim_info, dict) else dim_info
                marker = " <- FIX THIS" if str(dim_id) == str(weakest_dim) else ""
                dim_lines.append(f"  {dim_id}: {h_score}/10 (heuristic) | {s_score}/10 (semantic) -- {desc}{marker}")
            dim_section = "\n## Dimension Scores (focus on lowest)\n" + "\n".join(dim_lines)
            if dim_suggestion:
                dim_section += f"\n\nPRIORITY FIX: {dim_suggestion}"

        prompt = f"""You are an autonomous researcher improving a markdown artifact.
Your job: suggest ONE specific improvement and return the COMPLETE modified file.

## Current artifact ({fp.name})
Score: {best_quality}/10 | Density: {density} | Target: {target}
{dim_section}

```markdown
{content}
```
{history_summary}

{f"## Strategy hints{chr(10)}{strategy_hints}" if strategy_hints else ""}

## Rules
1. Return ONLY the complete modified file content (no explanation before/after)
2. Make ONE specific change per round (not multiple)
3. Keep all YAML frontmatter fields (don't remove any)
4. The `kind:` field must NOT change
5. Stay between 800-4096 bytes for the total file
6. Focus on the WEAKEST dimension shown above. If none shown, focus on: density (tables > prose), actionability (examples, anti-patterns), insight depth (non-obvious knowledge)

## Your response format
First line: HYPOTHESIS: <one-line description of what you're changing and which dimension it targets>
Then a blank line, then the COMPLETE file content (including --- frontmatter ---).
Nothing else."""

        if verbose:
            print(f"\n  --- Round {round_num}/{max_rounds} (budget: {remaining_budget:,} remaining) ---")

        # Call LLM via SDK gateway
        try:
            response_text = execute_prompt(prompt)
        except SystemExit:
            if verbose:
                print(f"  [FAIL] No LLM provider available. Stopping.")
            break
        except Exception as e:
            if verbose:
                print(f"  [FAIL] LLM error: {e}")
            log_result(str(fp), round_num, best_quality, density, "crash", f"llm_error: {e}")
            continue

        # Track tokens (best effort -- depends on SDK metrics being printed to stderr)
        # Conservative estimate if SDK doesn't report: ~4 chars per token
        estimated_tokens = (len(prompt) + len(response_text)) // 4
        tokens_used += estimated_tokens

        # Parse response: extract hypothesis and content
        hypothesis, new_content = _parse_agent_response(response_text)

        if not new_content:
            if verbose:
                print(f"  [WARN]  Could not parse response. Skipping round.")
            log_result(str(fp), round_num, best_quality, density, "crash", "unparseable response")
            experiment_log.append({"round": round_num, "status": "crash", "description": "unparseable"})
            continue

        if verbose:
            print(f"  Hypothesis: {hypothesis}")

        # Apply change
        fp.write_text(new_content, encoding="utf-8")

        # Validate (compile check)
        if not validate_artifact(fp):
            if verbose:
                print(f"  [FAIL] Compile failed. Reverting.")
            git_restore(fp)
            log_result(str(fp), round_num, 0, 0, "crash", f"compile fail: {hypothesis}")
            experiment_log.append({"round": round_num, "status": "crash", "description": hypothesis})
            continue

        # Score (hybrid: structural + rubric + semantic)
        new_density = compute_density(fp)
        try:
            from cex_score import score_hybrid
            hr = score_hybrid(str(fp), use_cache=False, verbose=False)
            new_quality = hr.get("score", 0.0)
            # Update dimension breakdown for next round's prompt
            dimension_breakdown = hr.get("dimensions", dimension_breakdown)
            weakest_dim = hr.get("weakest", weakest_dim)
            dim_suggestion = hr.get("suggestion", dim_suggestion)
        except Exception:
            new_quality = score_artifact(fp) or best_quality

        if verbose:
            print(f"  Result: quality={new_quality}, density={new_density}")
            if weakest_dim:
                print(f"  Weakest: {weakest_dim} | {dim_suggestion[:60]}")

        # Keep or discard
        if new_quality > best_quality:
            best_quality = new_quality
            git_commit_keep(fp, f"[evolve] {fp.name}: {hypothesis} (q={new_quality})")
            log_result(str(fp), round_num, new_quality, new_density, "keep", hypothesis)
            experiment_log.append({"round": round_num, "status": "keep", "description": hypothesis})
            if verbose:
                print(f"  [OK] KEEP ({new_quality})")
            if new_quality >= target:
                if verbose:
                    print(f"  [>>] Target {target} reached!")
                break
        else:
            git_restore(fp)
            log_result(str(fp), round_num, new_quality, new_density, "discard", hypothesis)
            experiment_log.append({"round": round_num, "status": "discard", "description": hypothesis})
            if verbose:
                print(f"  <-  DISCARD ({new_quality} <= {best_quality})")

    result = {
        "status": "complete",
        "quality": best_quality,
        "rounds": rounds_run,
        "tokens_used": tokens_used,
        "improved": best_quality > baseline_quality,
        "delta": round(best_quality - baseline_quality, 1),
    }

    if verbose:
        print(f"\n{'='*60}")
        print(f"[AGENT COMPLETE]")
        print(f"  Quality: {baseline_quality} -> {best_quality} (delta{result['delta']:+.1f})")
        print(f"  Rounds:  {rounds_run}/{max_rounds}")
        print(f"  Tokens:  {tokens_used:,}/{budget_tokens:,}")
        print(f"{'='*60}")

    return result


def _parse_agent_response(response: str) -> tuple[str, str]:
    """Parse LLM response into (hypothesis, file_content).

    Expected format:
      HYPOTHESIS: <description>
      <blank line>
      <complete file content>
    """
    if not response or not response.strip():
        return "", ""

    lines = response.strip().split("\n")
    hypothesis = "unknown improvement"
    content_start = 0

    # Find HYPOTHESIS line
    for i, line in enumerate(lines):
        if line.strip().upper().startswith("HYPOTHESIS:"):
            hypothesis = line.split(":", 1)[1].strip()
            content_start = i + 1
            break

    # Skip blank lines after hypothesis
    while content_start < len(lines) and not lines[content_start].strip():
        content_start += 1

    content = "\n".join(lines[content_start:]).strip()

    # If no HYPOTHESIS found, treat entire response as content
    if content_start == 0:
        # Try to detect if response starts with frontmatter
        if response.strip().startswith("---"):
            return "direct modification", response.strip()
        # Otherwise it might be wrapped in code blocks
        if "```" in response:
            import re
            match = re.search(r"```(?:markdown)?\n(.*?)```", response, re.DOTALL)
            if match:
                return "direct modification", match.group(1).strip()

    # Strip code block wrapper if present
    if content.startswith("```") and content.endswith("```"):
        content = content.split("\n", 1)[1] if "\n" in content else content[3:]
        content = content.rsplit("```", 1)[0].strip()

    return hypothesis, content


# ============================================================
# AUTO MODE -- Hybrid post-hook (heuristic + agent if needed)
# ============================================================

def evolve_auto(filepath: Path, threshold: float = 8.5,
                agent_budget: int = 30000, agent_target: float = 9.0,
                agent_max_rounds: int = 5, verbose: bool = True) -> dict:
    """
    Hybrid AutoResearch post-hook: heuristic pass (free) + agent if needed.

    Designed to be called automatically after every artifact creation.
    Flow:
      1. Heuristic pass (Python-only, 0 tokens) -- frontmatter, whitespace, filler
      2. Score via cex_score.py
      3. If score >= threshold -> done (zero LLM cost)
      4. If score < threshold -> spawn agent mode via SDK (budget-capped)

    This is the "Hybrid F" strategy -- smart budget, automatic trigger.

    Returns dict with: status, quality, mode_used, tokens_used
    """
    fp = Path(filepath)
    if not fp.exists():
        return {"status": "error", "quality": 0, "mode_used": "none", "tokens_used": 0}

    if verbose:
        print(f"\n[AUTO] {fp.name}")

    # Step 1: Heuristic pass (free)
    heuristic_result = evolve_single(fp, target=threshold, max_rounds=3, verbose=False)
    post_heuristic_quality = heuristic_result.get("quality", 0)

    if verbose:
        print(f"  Heuristic: q={post_heuristic_quality} (status={heuristic_result['status']})")

    # Step 2: Check if good enough
    if post_heuristic_quality >= threshold:
        if verbose:
            print(f"  [OK] Above threshold ({threshold}). No LLM needed.")
        return {
            "status": "complete",
            "quality": post_heuristic_quality,
            "mode_used": "heuristic",
            "tokens_used": 0,
        }

    # Step 3: Agent mode via SDK (budget-capped)
    if verbose:
        print(f"  [!] Score {post_heuristic_quality} < {threshold}. Spawning agent mode...")

    agent_result = evolve_agent(
        fp,
        budget_tokens=agent_budget,
        target=agent_target,
        max_rounds=agent_max_rounds,
        verbose=verbose,
    )

    return {
        "status": agent_result.get("status", "error"),
        "quality": agent_result.get("quality", post_heuristic_quality),
        "mode_used": "agent" if agent_result.get("tokens_used", 0) > 0 else "heuristic",
        "tokens_used": agent_result.get("tokens_used", 0),
        "delta": agent_result.get("delta", 0),
    }


# ============================================================
# CLI
# ============================================================

def _parse_cli_args(argv: list, start: int = 3) -> dict:
    """Parse --key value pairs from argv."""
    args = {}
    i = start
    while i < len(argv):
        if argv[i].startswith("--") and i + 1 < len(argv):
            key = argv[i][2:].replace("-", "_")
            args[key] = argv[i + 1]
            i += 2
        else:
            i += 1
    return args


def main():
    known_modes = {"agent", "auto", "single", "sweep", "report"}
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-") and sys.argv[1] not in known_modes:
        mode = sys.argv[1]
        print(f"Unknown mode: {mode}. Use: agent, auto, single, sweep, report")
        print(f"\n  agent  = TRUE AutoResearch via SDK (budget-tracked)")
        print(f"  auto   = Hybrid: heuristic (free) + agent if score < threshold")
        print(f"  single = Heuristic only (Python, no LLM)")
        print(f"  sweep  = Heuristic batch (all quality:null)")
        print(f"  report = Experiment history")
        return

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="mode")

    agent_parser = subparsers.add_parser("agent", help="Run SDK-backed AutoResearch.")
    agent_parser.add_argument("file", nargs="?", help="Target file.")
    agent_parser.add_argument("rest", nargs=argparse.REMAINDER)

    auto_parser = subparsers.add_parser("auto", help="Run heuristic mode, then agent mode if needed.")
    auto_parser.add_argument("file", nargs="?", help="Target file.")
    auto_parser.add_argument("rest", nargs=argparse.REMAINDER)

    single_parser = subparsers.add_parser("single", help="Run heuristic evolution on one file.")
    single_parser.add_argument("file", nargs="?", help="Target file.")
    single_parser.add_argument("rest", nargs=argparse.REMAINDER)

    sweep_parser = subparsers.add_parser("sweep", help="Run heuristic evolution on quality:null + below-target files.")
    sweep_parser.add_argument("--apply-scores", action="store_true",
                              help="After sweep, write structural+rubric scores to all improved files.")
    sweep_parser.add_argument("rest", nargs=argparse.REMAINDER)

    subparsers.add_parser("report", help="Show experiment history.")

    parsed, _ = parser.parse_known_args()
    if not parsed.mode:
        print(__doc__)
        return

    mode = parsed.mode

    if mode == "agent":
        # TRUE AutoResearch via SDK -- Python controls, LLM thinks
        if not parsed.file:
            print("Usage: cex_evolve.py agent <file> [--budget N] [--target N] [--max-rounds N]")
            return
        filepath = Path(parsed.file)
        args = _parse_cli_args([sys.argv[0], mode, parsed.file] + parsed.rest)
        evolve_agent(
            filepath,
            budget_tokens=int(args.get("budget", 50000)),
            target=float(args.get("target", 9.0)),
            max_rounds=int(args.get("max_rounds", 10)),
        )

    elif mode == "auto":
        # Hybrid post-hook: heuristic + agent if needed
        if not parsed.file:
            print("Usage: cex_evolve.py auto <file> [--threshold N] [--budget N] [--target N]")
            return
        filepath = Path(parsed.file)
        args = _parse_cli_args([sys.argv[0], mode, parsed.file] + parsed.rest)
        result = evolve_auto(
            filepath,
            threshold=float(args.get("threshold", 8.5)),
            agent_budget=int(args.get("budget", 30000)),
            agent_target=float(args.get("target", 9.0)),
            agent_max_rounds=int(args.get("max_rounds", 5)),
        )
        print(f"\n  Result: {json.dumps(result, indent=2)}")

    elif mode == "single":
        # Heuristic fallback -- no LLM
        if not parsed.file:
            print("Usage: cex_evolve.py single <file> [--target N] [--max-rounds N]")
            return
        filepath = Path(parsed.file)
        args = _parse_cli_args([sys.argv[0], mode, parsed.file] + parsed.rest)
        evolve_single(
            filepath,
            target=float(args.get("target", 9.0)),
            max_rounds=int(args.get("max_rounds", 5)),
        )

    elif mode == "sweep":
        # Heuristic batch -- no LLM
        args = _parse_cli_args([sys.argv[0], mode] + parsed.rest, start=2)
        apply_scores = getattr(parsed, "apply_scores", False) or ("apply_scores" in args)
        evolve_sweep(
            target=float(args.get("target", 8.5)),
            max_rounds=int(args.get("max_rounds", 3)),
            apply_scores=apply_scores,
        )

    elif mode == "report":
        show_report()

    else:
        print(f"Unknown mode: {mode}. Use: agent, auto, single, sweep, report")
        print(f"\n  agent  = TRUE AutoResearch via SDK (budget-tracked)")
        print(f"  auto   = Hybrid: heuristic (free) + agent if score < threshold")
        print(f"  single = Heuristic only (Python, no LLM)")
        print(f"  sweep  = Heuristic batch (all quality:null)")
        print(f"  report = Experiment history")


if __name__ == "__main__":
    main()
