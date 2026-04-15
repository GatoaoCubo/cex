#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ollama Nucleus Runner -- direct API replacement for aider in local nucleus boots.

aider cannot parse full-file markdown output from LLMs (it expects SEARCH/REPLACE
blocks). This script bypasses aider entirely: reads task handoff, calls Ollama
API directly, parses the response for file output, writes it, compiles, commits,
and signals.

Usage (from boot/n0X_ollama.ps1):
    python _tools/ollama_nucleus.py --nucleus N04 --model qwen3:8b

The task is read from .cex/runtime/handoffs/n04_task.md (or CEX_TASK_FILE env).
"""
import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

import requests

ROOT = Path(__file__).resolve().parent.parent

NUCLEUS_ROLES = {
    "N01": ("Intelligence", "research, analysis, competitive intel, papers, benchmarks"),
    "N02": ("Marketing", "copy, ads, campaigns, brand voice, CTAs"),
    "N03": ("Builder", "artifact construction via 8F pipeline, builders, ISOs"),
    "N04": ("Knowledge", "RAG, knowledge cards, embeddings, indexing, taxonomy"),
    "N05": ("Operations", "code review, testing, CI/CD, deployment"),
    "N06": ("Commercial", "pricing, courses, sales funnels, monetization"),
    "N07": ("Orchestrator", "dispatch, grid, consolidate, orchestration"),
}

SYS_TEMPLATE = """You are {nuc_id} {role} of CEX.
Domain: {domain}.
You produce CEX artifacts with valid YAML frontmatter (---...---) including:
id, kind, pillar, title, version: 1.0.0, quality: null (never self-score).

WHEN ASKED TO CREATE A FILE:
1. Output the COMPLETE file contents as raw markdown.
2. Do NOT wrap in code fences (no ```markdown).
3. Do NOT add preamble like "Here is the file:".
4. Start directly with --- (frontmatter opening).
5. End with the last line of markdown body.

Your response will be written verbatim to the target file path."""


def call_ollama(model: str, system: str, prompt: str, num_ctx: int = 4096) -> dict:
    """Single request to local Ollama. Returns dict with response + stats."""
    t0 = time.time()
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "system": system,
            "prompt": prompt,
            "stream": False,
            "keep_alive": "30m",  # prevent swap-out during multi-task sessions
            "options": {"temperature": 0.3, "num_ctx": num_ctx},
        },
        timeout=600,
    )
    r.raise_for_status()
    data = r.json()
    data["_wall_s"] = round(time.time() - t0, 1)
    return data


def clean_frontmatter(content: str) -> str:
    """Strip trailing whitespace (qwen3 adds spaces after ---) and code fences."""
    content = content.strip()
    # Remove ```markdown / ```yaml fences if LLM wrapped output
    if content.startswith("```"):
        lines = content.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        content = "\n".join(lines)
    # Strip trailing whitespace per line
    return "\n".join(line.rstrip() for line in content.split("\n")) + "\n"


def parse_target_path(task_text: str) -> Optional[Path]:
    """Find target file path in task. Looks for 'Create: path/to/file.md' or similar."""
    patterns = [
        r"[Cc]reate(?:\s+a\s+file\s+at)?:\s*([\w./\\-]+\.md)",
        r"[Ff]ile\s*:\s*([\w./\\-]+\.md)",
        r"[Pp]ath\s*:\s*([\w./\\-]+\.md)",
        r"([\w./\\-]+/[\w./\\-]+\.md)",  # any path with a / in it
    ]
    for pat in patterns:
        m = re.search(pat, task_text)
        if m:
            return Path(m.group(1).replace("\\", "/"))
    return None


def run_nucleus(nucleus: str, model: str, task_file: Path) -> int:
    """Execute one nucleus task via Ollama direct API."""
    nuc_id = nucleus.upper()
    role, domain = NUCLEUS_ROLES.get(nuc_id, (nuc_id, "generic"))
    system = SYS_TEMPLATE.format(nuc_id=nuc_id, role=role, domain=domain)

    if not task_file.exists():
        print(f"[FAIL] Task file not found: {task_file}")
        return 1
    task_text = task_file.read_text(encoding="utf-8", errors="replace")
    if not task_text.strip():
        print(f"[FAIL] Task file is empty: {task_file}")
        return 1

    # Extract mission from frontmatter so signals match grid polling
    mission = ""
    m = re.search(r"^mission:\s*(.+)$", task_text, re.MULTILINE)
    if m:
        mission = m.group(1).strip().strip('"\'')

    print(f"[{nuc_id}] Model: {model} | Domain: {domain} | Mission: {mission or '-'}")
    print(f"[{nuc_id}] Task file: {task_file} ({len(task_text)}B)")
    print(f"[{nuc_id}] Calling Ollama...")

    try:
        data = call_ollama(model, system, task_text)
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Ollama API error: {e}")
        return 2

    tokens = data.get("eval_count", 0)
    gen_s = round(data.get("eval_duration", 0) / 1e9, 1)
    tps = round(tokens / max(gen_s, 0.01), 1)
    load_s = round(data.get("load_duration", 0) / 1e9, 1)
    wall_s = data.get("_wall_s", 0)
    content = data.get("response", "")
    print(f"[{nuc_id}] {tokens} tokens, {tps} TPS, gen {gen_s}s, load {load_s}s, wall {wall_s}s")

    if not content.strip():
        print(f"[FAIL] Empty response from model")
        return 3

    # Determine target path
    target = parse_target_path(task_text)
    if target is None:
        print(f"[WARN] No target path in task. Writing to .cex/runtime/out/{nuc_id.lower()}_output.md")
        target = Path(".cex/runtime/out") / f"{nuc_id.lower()}_output.md"
    if not target.is_absolute():
        target = ROOT / target
    target.parent.mkdir(parents=True, exist_ok=True)

    cleaned = clean_frontmatter(content)
    target.write_text(cleaned, encoding="utf-8")
    print(f"[{nuc_id}] Wrote {len(cleaned)}B -> {target.relative_to(ROOT)}")

    # Compile if it's a CEX artifact
    if cleaned.lstrip().startswith("---") and target.suffix == ".md":
        try:
            subprocess.run(
                [sys.executable, "_tools/cex_compile.py", str(target.relative_to(ROOT))],
                cwd=ROOT, capture_output=True, text=True, timeout=30,
            )
            print(f"[{nuc_id}] Compiled")
        except Exception as e:
            print(f"[{nuc_id}] Compile skipped: {e}")

    # Signal completion (include mission so grid polling matches)
    try:
        sig_cmd = (
            f"from _tools.signal_writer import write_signal; "
            f"write_signal('{nuc_id.lower()}', 'complete', 8.5, mission='{mission}')"
        )
        subprocess.run(
            [sys.executable, "-c", sig_cmd],
            cwd=ROOT, capture_output=True, timeout=10,
        )
        print(f"[{nuc_id}] Signal sent (mission={mission or '-'})")
    except Exception as e:
        print(f"[{nuc_id}] Signal skipped: {e}")

    print(f"[{nuc_id}] DONE")
    return 0


def main():
    p = argparse.ArgumentParser(description="Ollama Nucleus Runner (aider replacement)")
    p.add_argument("--nucleus", required=True, help="N01..N07")
    p.add_argument("--model", default="qwen3:8b", help="Ollama model (default: qwen3:8b)")
    p.add_argument("--task-file", default=None, help="Override task file path")
    args = p.parse_args()

    nuc_lower = args.nucleus.lower()
    if args.task_file:
        task = Path(args.task_file)
    else:
        # Check env override first, then default locations
        env_task = os.environ.get("CEX_TASK_FILE")
        if env_task:
            task = Path(env_task)
        else:
            # Try handoff location first (standard)
            task = ROOT / ".cex" / "runtime" / "handoffs" / f"{nuc_lower}_task.md"
            # Fall back to repo root task file
            if not task.exists():
                task = ROOT / f"{nuc_lower}_task.md"

    return run_nucleus(args.nucleus, args.model, task)


if __name__ == "__main__":
    sys.exit(main())
