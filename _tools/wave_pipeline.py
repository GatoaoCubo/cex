#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Wave Pipeline -- Auto-commit + chain Wave 1->2->3 + regenerate FT dataset.

Runs wave1_builder_gen.py for each wave, auto-commits results, then
regenerates the FT dataset. Designed to run unattended overnight.

Usage:
    python _tools/wave_pipeline.py                    # Resume from current state
    python _tools/wave_pipeline.py --start-wave 2     # Start from Wave 2
    python _tools/wave_pipeline.py --dry-run           # Show what would be done
    python _tools/wave_pipeline.py --commit-only       # Just commit existing work
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"

WAVE1_KINDS = [
    "threat_model", "safety_policy", "content_filter",
    "bias_audit", "compliance_framework", "incident_report",
    "reasoning_strategy", "rl_algorithm", "reward_model",
    "search_strategy", "thinking_config",
    "agent_profile", "planning_strategy", "action_paradigm",
    "collaboration_pattern", "dual_loop_architecture",
]

WAVE2_KINDS = [
    "voice_pipeline", "realtime_session", "vad_config",
    "tts_provider", "stt_provider", "prosody_config", "transport_config",
    "edit_format", "sandbox_config", "repo_map",
    "diff_strategy", "agent_computer_interface",
    "training_method", "model_architecture", "dataset_card",
    "model_registry", "experiment_tracker", "quantization_config",
]

WAVE3_KINDS = [
    "benchmark_suite", "judge_config", "eval_metric",
    "eval_framework", "trajectory_eval",
    "reranker_config", "graph_rag_config", "agentic_rag",
    "memory_architecture", "procedural_memory",
    "consolidation_policy", "memory_benchmark",
    "prompt_technique", "prompt_optimizer", "multimodal_prompt",
    "workflow_node", "visual_workflow",
    "self_improvement_loop",
]

WAVES = {"1": WAVE1_KINDS, "2": WAVE2_KINDS, "3": WAVE3_KINDS}


def count_isos(kind: str) -> int:
    """Count existing ISOs for a kind."""
    builder_dir = BUILDERS_DIR / f"{kind.replace('_', '-')}-builder"
    if not builder_dir.exists():
        return 0
    return len(list(builder_dir.glob("bld_*.md")))


def wave_status(wave_num: int) -> tuple[int, int, int, int]:
    """Check completion status of a wave."""
    kinds = WAVES[str(wave_num)]
    complete = 0
    partial = 0
    missing = 0
    for k in kinds:
        count = count_isos(k)
        if count >= 13:
            complete += 1
        elif count > 0:
            partial += 1
        else:
            missing += 1
    return complete, partial, missing, len(kinds)


def run_wave(wave_num: int, dry_run: bool = False) -> bool:
    """Run wave generator and return success."""
    comp, part, miss, total = wave_status(wave_num)
    print(f"\n[WAVE {wave_num}] Status: {comp}/{total} complete, {part} partial, {miss} missing")

    if comp == total:
        print(f"[WAVE {wave_num}] Already complete -- skipping")
        return True

    if dry_run:
        print(f"[DRY] Would run: python _tools/wave1_builder_gen.py --wave {wave_num}")
        return True

    print(f"[WAVE {wave_num}] Launching generator...")
    result = subprocess.run(
        [sys.executable, "_tools/wave1_builder_gen.py", "--wave", str(wave_num)],
        cwd=str(ROOT),
        timeout=7200,  # 2 hours max per wave
    )

    if result.returncode != 0:
        print(f"[WAVE {wave_num}] Generator exited with code {result.returncode}")
        # Check how many we got
        comp2, _, _, _ = wave_status(wave_num)
        if comp2 > comp:
            print(f"[WAVE {wave_num}] Made progress: {comp} -> {comp2} complete")
        return False

    return True


def commit_wave(wave_num: int, dry_run: bool = False) -> bool:
    """Commit all ISOs from a wave."""
    kinds = WAVES[str(wave_num)]
    files_to_add = []
    for k in kinds:
        builder_dir = BUILDERS_DIR / f"{k.replace('_', '-')}-builder"
        if builder_dir.exists():
            for f in builder_dir.glob("bld_*.md"):
                files_to_add.append(str(f.relative_to(ROOT)))

    if not files_to_add:
        print(f"[COMMIT] No files to commit for Wave {wave_num}")
        return True

    print(f"[COMMIT] {len(files_to_add)} files from Wave {wave_num}")

    if dry_run:
        print(f"[DRY] Would commit {len(files_to_add)} files")
        return True

    # Stage files in batches (avoid command line too long)
    batch_size = 50
    for i in range(0, len(files_to_add), batch_size):
        batch = files_to_add[i:i+batch_size]
        subprocess.run(["git", "add"] + batch, cwd=str(ROOT))

    # Commit
    comp, _, _, total = wave_status(wave_num)
    msg = f"[N03-ISO] Wave {wave_num}: {comp}/{total} kinds (13 ISOs each)\n\nGenerated via Ollama qwen3:14b at $0 API cost."
    result = subprocess.run(
        ["git", "commit", "-m", msg],
        cwd=str(ROOT),
        capture_output=True, text=True,
    )

    if result.returncode == 0:
        print(f"[COMMIT] Wave {wave_num} committed successfully")
        return True
    elif "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        print(f"[COMMIT] Wave {wave_num} already committed")
        return True
    else:
        print(f"[COMMIT] Failed: {result.stderr[:200]}")
        return False


def regenerate_ft_dataset(dry_run: bool = False) -> bool:
    """Regenerate FT dataset after all waves."""
    if dry_run:
        print("[DRY] Would regenerate FT dataset")
        return True

    print("\n[FT] Regenerating fine-tune dataset...")
    result = subprocess.run(
        [sys.executable, "_tools/cex_ft_dataset.py"],
        cwd=str(ROOT),
        capture_output=True, text=True,
    )

    if result.returncode == 0:
        # Show stats
        for line in result.stdout.split("\n"):
            if "Total" in line or "pairs" in line.lower():
                print(f"[FT] {line.strip()}")
        return True
    else:
        print(f"[FT] Failed: {result.stderr[:200]}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Wave Pipeline")
    parser.add_argument("--start-wave", type=int, default=1, help="Start from wave N")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--commit-only", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()

    if args.status:
        for w in [1, 2, 3]:
            comp, part, miss, total = wave_status(w)
            pct = int(comp / total * 100) if total > 0 else 0
            print(f"Wave {w}: {comp}/{total} complete ({pct}%), {part} partial, {miss} missing")
        return

    if args.commit_only:
        for w in [1, 2, 3]:
            commit_wave(w, args.dry_run)
        return

    print("=" * 60)
    print("CEX WAVE PIPELINE -- Autonomous Builder ISO Generation")
    print("=" * 60)

    for w in range(args.start_wave, 4):
        print(f"\n{'='*60}")
        print(f"WAVE {w}")
        print(f"{'='*60}")

        success = run_wave(w, args.dry_run)
        commit_wave(w, args.dry_run)

        if not success:
            print(f"\n[WARN] Wave {w} incomplete. Re-run to resume.")
            # Don't block -- continue to next wave (ISOs are skippable)

    # After all waves, regenerate FT dataset
    regenerate_ft_dataset(args.dry_run)

    print(f"\n{'='*60}")
    print("PIPELINE COMPLETE")
    for w in [1, 2, 3]:
        comp, _, _, total = wave_status(w)
        print(f"  Wave {w}: {comp}/{total} kinds")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
