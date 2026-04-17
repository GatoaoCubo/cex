#!/usr/bin/env python3
"""bench_nucleus_models.py: Benchmark local Ollama models per CEX nucleus domain.

Sends the same domain-appropriate prompt to each model, measures wall time,
completion tokens, fabrication proxy (numeric assertions vs cited files), and
adherence (frontmatter + section count). Outputs a ranking per nucleus.

Usage:
    python _tools/bench_nucleus_models.py --models qwen3:8b,qwen3:14b,llama3.1:8b
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib import request

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".cex" / "runtime" / "benchmarks"
OUT.mkdir(parents=True, exist_ok=True)

# Domain-specific prompts per nucleus, short enough to run fast but structured
PROMPTS = {
    "n01_research": {
        "desc": "Research/intelligence: analyze a competitor claim",
        "user": (
            "You are a research analyst. In under 300 words, analyze this claim: "
            "'LiteLLM proxy adds <5ms overhead for local models'. "
            "Output markdown with sections: ## Claim, ## Evidence, ## Verdict. "
            "Only use information you can verify; flag uncertainty."
        ),
    },
    "n02_marketing": {
        "desc": "Marketing/copy: write a landing page hero",
        "user": (
            "Write a landing page hero section for 'CEX: typed knowledge system "
            "for LLM agents'. Output: 1 headline (<=10 words), 1 subheadline "
            "(<=20 words), 3 bullet benefits. No emojis. ASCII only."
        ),
    },
    "n03_build": {
        "desc": "Builder: scaffold a CEX artifact frontmatter",
        "user": (
            "Generate ONLY the YAML frontmatter for a CEX artifact of kind "
            "'decision_record', id 'dr_model_picker', tags [routing, benchmark]. "
            "Include: id, kind, pillar (P08), title, version (1.0.0), "
            "quality (null), tags. Output frontmatter only, nothing else."
        ),
    },
    "n04_knowledge": {
        "desc": "Knowledge: explain a concept with precise citations",
        "user": (
            "Explain TF-IDF in <=200 words. Output markdown with ## Definition, "
            "## Formula, ## Use case. If you cite a specific paper or author, "
            "name it accurately; otherwise say 'classical IR technique, 1970s'."
        ),
    },
    "n05_ops": {
        "desc": "Ops: write a shell one-liner with explanation",
        "user": (
            "Write a bash one-liner that finds files modified in the last 24h "
            "under /var/log, excluding .gz, and prints path + size. Then "
            "explain each flag used. Plain output, no markdown frontmatter."
        ),
    },
    "n06_commercial": {
        "desc": "Commercial: pricing tier description",
        "user": (
            "Write a 3-tier pricing table (Free/Pro/Enterprise) for a SaaS "
            "code quality tool. Each tier: name, price/month, 3 key features. "
            "Output as markdown table. Realistic US prices."
        ),
    },
    "n07_orchestrate": {
        "desc": "Orchestration: plan a 3-wave dispatch",
        "user": (
            "Plan a 3-wave mission to build a documentation site. Each wave: "
            "which nuclei (N01-N06), what artifacts produced, handoff to next "
            "wave. Output as numbered markdown list with wave 1, 2, 3."
        ),
    },
}


def call_ollama(model: str, prompt: str, timeout: int = 300) -> dict:
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"num_predict": 800, "temperature": 0.2},
    }
    data = json.dumps(payload).encode()
    req = request.Request(
        "http://localhost:11434/api/chat",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode())
        wall = time.time() - t0
        content = body.get("message", {}).get("content", "")
        # Strip <think>...</think> blocks
        content_clean = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        return {
            "ok": True,
            "wall": wall,
            "completion_tokens": body.get("eval_count", 0),
            "prompt_tokens": body.get("prompt_eval_count", 0),
            "tps": body.get("eval_count", 0) / max(wall, 0.001),
            "content_raw": content,
            "content_clean": content_clean,
            "raw_bytes": len(content),
            "clean_bytes": len(content_clean),
        }
    except Exception as e:
        return {"ok": False, "wall": time.time() - t0, "error": str(e)}


def call_claude_cli(model: str, prompt: str, timeout: int = 300) -> dict:
    """Call Claude CLI in print mode, time the subprocess."""
    t0 = time.time()
    try:
        proc = subprocess.run(
            ["claude", "--model", model, "-p", prompt],
            capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        wall = time.time() - t0
        content = (proc.stdout or "").strip()
        # Claude CLI has no thinking leak in -p mode
        return {
            "ok": proc.returncode == 0 and len(content) > 0,
            "wall": wall,
            "completion_tokens": 0,  # CLI doesn't expose
            "prompt_tokens": 0,
            "tps": 0.0,
            "content_raw": content,
            "content_clean": content,
            "raw_bytes": len(content),
            "clean_bytes": len(content),
            "error": proc.stderr[:200] if proc.returncode != 0 else None,
        }
    except Exception as e:
        return {"ok": False, "wall": time.time() - t0, "error": str(e)}


def dispatch_call(model: str, prompt: str, timeout: int = 300) -> dict:
    """Route to Ollama or Claude based on model prefix."""
    if model.startswith("claude-") or model.startswith("sonnet") or model.startswith("opus") or model.startswith("haiku"):
        return call_claude_cli(model, prompt, timeout)
    return call_ollama(model, prompt, timeout)


def score_output(nucleus: str, output: str) -> dict:
    """Heuristic scoring: section count, frontmatter presence, length, cleanness."""
    score = {
        "sections": len(re.findall(r"^##\s", output, re.MULTILINE)),
        "has_frontmatter": "---\n" in output[:20],
        "has_table": "|" in output,
        "bullets": len(re.findall(r"^[\*\-]\s", output, re.MULTILINE)),
        "bytes": len(output),
        "has_think_leak": "<think>" in output,
    }
    # Nucleus-specific heuristics
    if nucleus == "n03_build":
        score["adherence"] = score["has_frontmatter"] and "kind:" in output
    elif nucleus in ("n01_research", "n04_knowledge"):
        score["adherence"] = score["sections"] >= 2
    elif nucleus == "n06_commercial":
        score["adherence"] = score["has_table"]
    elif nucleus == "n07_orchestrate":
        score["adherence"] = bool(re.search(r"wave\s*[123]", output, re.IGNORECASE))
    else:
        score["adherence"] = score["bytes"] > 100
    return score


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--models", default="qwen3:8b,qwen3:14b")
    p.add_argument("--nuclei", default="all")
    args = p.parse_args()

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if args.nuclei == "all":
        nuclei = list(PROMPTS.keys())
    else:
        nuclei = [n.strip() for n in args.nuclei.split(",")]

    results = {}
    for nucleus in nuclei:
        if nucleus not in PROMPTS:
            print(f"[skip] unknown nucleus: {nucleus}")
            continue
        print(f"\n=== {nucleus}: {PROMPTS[nucleus]['desc']} ===")
        results[nucleus] = {}
        for model in models:
            print(f"  [{model}] calling...", flush=True)
            r = dispatch_call(model, PROMPTS[nucleus]["user"])
            if not r["ok"]:
                print(f"    FAIL: {r.get('error', '?')}")
                results[nucleus][model] = {"ok": False, "error": r.get("error")}
                continue
            s = score_output(nucleus, r["content_clean"])
            record = {
                "ok": True,
                "wall": round(r["wall"], 1),
                "tps": round(r["tps"], 1),
                "completion_tokens": r["completion_tokens"],
                "clean_bytes": r["clean_bytes"],
                **s,
            }
            results[nucleus][model] = record
            print(
                f"    wall={record['wall']}s  tps={record['tps']}  "
                f"bytes={record['clean_bytes']}  sections={record['sections']}  "
                f"adherence={record['adherence']}"
            )
            # Save content for fabrication audit later
            out_file = OUT / f"{nucleus}_{model.replace(':', '_').replace('/', '_')}.md"
            out_file.write_text(r["content_clean"], encoding="utf-8")

    summary_file = OUT / "summary.json"
    summary_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\n=== Summary written to {summary_file} ===")

    # Per-nucleus winner
    print("\n=== Winner per nucleus (by adherence AND fastest wall) ===")
    for nucleus, models_res in results.items():
        winners = [
            (m, r) for m, r in models_res.items()
            if r.get("ok") and r.get("adherence")
        ]
        if not winners:
            print(f"  {nucleus}: NONE (no adherent model)")
            continue
        winners.sort(key=lambda x: x[1]["wall"])
        best_model, best_r = winners[0]
        print(
            f"  {nucleus}: {best_model}  "
            f"(wall={best_r['wall']}s, tps={best_r['tps']}, bytes={best_r['clean_bytes']})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
