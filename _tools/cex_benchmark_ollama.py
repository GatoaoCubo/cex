#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Ollama Benchmark -- Compare local models vs Claude Opus on CEX tasks.

Runs identical 8F tasks through multiple models and measures:
  - Frontmatter accuracy (structural correctness)
  - Content quality (cex_score.py L1+L2 heuristic)
  - Response time
  - Token count

Usage:
    python _tools/cex_benchmark_ollama.py --models qwen3:8b
    python _tools/cex_benchmark_ollama.py --models qwen3:8b,llama3.2:8b --tasks 5
    python _tools/cex_benchmark_ollama.py --report
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / ".cex" / "benchmarks"
RESULTS_FILE = RESULTS_DIR / "ollama_benchmark.json"

sys.path.insert(0, str(ROOT / "_tools"))

# -----------------------------------------------------------------------
# Benchmark Tasks (representative CEX workloads)
# -----------------------------------------------------------------------

BENCHMARK_TASKS = [
    {
        "id": "T01_kc_simple",
        "name": "Simple Knowledge Card",
        "prompt": (
            "Create a knowledge card about RAG chunking strategies.\n\n"
            "Requirements:\n"
            "- YAML frontmatter with: id, kind, pillar, title, version, quality: null, "
            "tags, tldr, domain, created, density_score\n"
            "- kind: knowledge_card\n"
            "- pillar: P01\n"
            "- Body with at least 3 sections using ## headings\n"
            "- At least one table comparing chunking methods\n"
            "- Density >= 0.85 (no filler)\n"
            "- Output ONLY the markdown artifact, nothing else."
        ),
        "expected_kind": "knowledge_card",
        "expected_pillar": "P01",
    },
    {
        "id": "T02_agent",
        "name": "Agent Definition",
        "prompt": (
            "Create an agent artifact for a sales qualification agent.\n\n"
            "Requirements:\n"
            "- YAML frontmatter with: id, kind, pillar, title, version, quality: null, "
            "tags, tldr, domain, created, density_score\n"
            "- kind: agent\n"
            "- pillar: P02\n"
            "- Body with: ## Purpose, ## Capabilities, ## Tools, ## Routing\n"
            "- Include a capabilities table\n"
            "- Density >= 0.85\n"
            "- Output ONLY the markdown artifact, nothing else."
        ),
        "expected_kind": "agent",
        "expected_pillar": "P02",
    },
    {
        "id": "T03_prompt_template",
        "name": "Prompt Template",
        "prompt": (
            "Create a prompt_template for generating product descriptions.\n\n"
            "Requirements:\n"
            "- YAML frontmatter with: id, kind, pillar, title, version, quality: null, "
            "tags, tldr, domain, created, density_score\n"
            "- kind: prompt_template\n"
            "- pillar: P03\n"
            "- Body with: ## Template (using {{VARIABLE}} placeholders), "
            "## Variables table, ## Examples, ## Usage\n"
            "- At least 3 variables\n"
            "- Output ONLY the markdown artifact, nothing else."
        ),
        "expected_kind": "prompt_template",
        "expected_pillar": "P03",
    },
    {
        "id": "T04_quality_gate",
        "name": "Quality Gate",
        "prompt": (
            "Create a quality_gate for validating knowledge cards.\n\n"
            "Requirements:\n"
            "- YAML frontmatter with: id, kind, pillar, title, version, quality: null, "
            "tags, tldr, domain, created, density_score\n"
            "- kind: quality_gate\n"
            "- pillar: P07\n"
            "- Body with: ## Hard Gates table (H01-H07, pass/fail checks), "
            "## Soft Dimensions table (S01-S05, weighted scoring)\n"
            "- Hard gates must have | ID | Check | Fail Condition | columns\n"
            "- Soft dims must have | ID | Dimension | Weight | columns\n"
            "- Output ONLY the markdown artifact, nothing else."
        ),
        "expected_kind": "quality_gate",
        "expected_pillar": "P07",
    },
    {
        "id": "T05_intent_resolution",
        "name": "Intent Resolution (complex)",
        "prompt": (
            "I will give you a natural language request. "
            "Map it to the correct CEX artifact kind, pillar, and nucleus.\n\n"
            "Request: 'I want to set up a webhook that triggers when a new customer signs up "
            "and sends their data to our CRM'\n\n"
            "Respond ONLY with valid JSON:\n"
            '{"kind": "...", "pillar": "P0X", "nucleus": "N0X", '
            '"reasoning": "one sentence why"}'
        ),
        "expected_kind": "webhook",
        "expected_pillar": "P04",
    },
    {
        "id": "T06_structured_table",
        "name": "Structured Data Extraction",
        "prompt": (
            "Create a comparison table of 5 LLM providers.\n\n"
            "Format as a markdown table with these exact columns:\n"
            "| Provider | Model | Context Window | Price/1M tokens | Strengths |\n\n"
            "Include: Anthropic, OpenAI, Google, Mistral, Meta (Llama).\n"
            "Use real data. Output ONLY the table, no prose."
        ),
        "expected_kind": None,
        "expected_pillar": None,
    },
    {
        "id": "T07_yaml_precision",
        "name": "YAML Frontmatter Precision",
        "prompt": (
            "Generate ONLY a YAML frontmatter block (between --- delimiters) "
            "for a CEX artifact with these exact values:\n\n"
            "- id: benchmark_test_artifact\n"
            "- kind: knowledge_card\n"
            "- pillar: P01\n"
            "- title: 'Benchmark Test Artifact'\n"
            "- version: 1.0.0\n"
            "- quality: null\n"
            "- tags: [benchmark, test, ollama]\n"
            "- tldr: 'Test artifact for Ollama benchmark validation'\n"
            "- domain: testing\n"
            "- created: 2026-04-08\n"
            "- density_score: 0.95\n\n"
            "Output ONLY the frontmatter block between --- markers. Nothing else."
        ),
        "expected_kind": "knowledge_card",
        "expected_pillar": "P01",
    },
    {
        "id": "T08_multilingual",
        "name": "Multilingual Understanding",
        "prompt": (
            "Translate this CEX task to structured output:\n\n"
            "Input (PT-BR): 'Cria um agente de vendas que qualifica leads "
            "usando BANT framework e integra com Hubspot'\n\n"
            "Respond with valid JSON:\n"
            '{"kind": "...", "pillar": "P0X", "nucleus": "N0X", '
            '"domain": "...", "tools_needed": ["..."], '
            '"reasoning": "one sentence"}'
        ),
        "expected_kind": "agent",
        "expected_pillar": "P02",
    },
    {
        "id": "T09_complex_artifact",
        "name": "Complex Multi-Section Artifact",
        "prompt": (
            "Create a workflow artifact for a content production pipeline.\n\n"
            "Requirements:\n"
            "- YAML frontmatter: id, kind: workflow, pillar: P12, title, version, "
            "quality: null, tags, tldr, domain, created, density_score\n"
            "- ## Stages table: | Stage | Nucleus | Input | Output | Duration |\n"
            "- At least 5 stages\n"
            "- ## Dependencies section with a dependency list\n"
            "- ## Signals section explaining completion detection\n"
            "- ## Quality Gates section\n"
            "- Density >= 0.85\n"
            "- Output ONLY the markdown artifact."
        ),
        "expected_kind": "workflow",
        "expected_pillar": "P12",
    },
    {
        "id": "T10_reasoning",
        "name": "Multi-Step Reasoning",
        "prompt": (
            "A user says: 'I want to improve all my low-quality artifacts automatically overnight'\n\n"
            "As the CEX orchestrator (N07), plan the execution:\n"
            "1. Which tool handles this?\n"
            "2. What mode should it run in?\n"
            "3. What quality threshold?\n"
            "4. How to handle failures?\n"
            "5. Estimated duration for 1000 artifacts?\n\n"
            "Respond with structured JSON:\n"
            '{"tool": "...", "mode": "...", "threshold": N.N, '
            '"failure_strategy": "...", "estimated_hours": N, '
            '"reasoning": "..."}'
        ),
        "expected_kind": None,
        "expected_pillar": None,
    },
]


# -----------------------------------------------------------------------
# Model Runner
# -----------------------------------------------------------------------


def run_ollama(model: str, prompt: str, timeout: int = 300) -> dict:
    """Run a prompt through Ollama HTTP API and measure performance.

    Uses HTTP API instead of CLI for better control:
    - Disables thinking mode for Qwen 3 (/no_think)
    - Strips <think> blocks from DeepSeek R1
    - Lower temperature for structured output
    """
    import urllib.error
    import urllib.request

    start = time.time()

    # Disable thinking mode for models that support it
    actual_prompt = prompt
    if "qwen" in model.lower():
        actual_prompt = "/no_think\n" + prompt
    if "deepseek" in model.lower():
        actual_prompt = "/no_think\n" + prompt

    payload = json.dumps({
        "model": model,
        "prompt": actual_prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 4096,
        },
    }).encode("utf-8")

    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            elapsed = time.time() - start
            result = json.loads(resp.read().decode("utf-8"))

        output = result.get("response", "").strip()

        # Strip <think>...</think> blocks (DeepSeek R1)
        output = re.sub(r"<think>.*?</think>\s*", "", output, flags=re.DOTALL)

        eval_count = result.get("eval_count", 0)
        eval_duration = result.get("eval_duration", 1)
        tok_per_sec = (eval_count / (eval_duration / 1e9)) if eval_duration > 0 else 0

        return {
            "output": output,
            "error": "",
            "elapsed_seconds": round(elapsed, 2),
            "success": len(output) > 10,
            "tokens": eval_count,
            "tok_per_sec": round(tok_per_sec, 1),
        }
    except urllib.error.URLError as e:
        return {
            "output": "",
            "error": f"Ollama offline: {e.reason}",
            "elapsed_seconds": time.time() - start,
            "success": False,
        }
    except Exception as e:
        elapsed = time.time() - start
        if elapsed >= timeout:
            return {
                "output": "",
                "error": "TIMEOUT",
                "elapsed_seconds": timeout,
                "success": False,
            }
        return {
            "output": "",
            "error": str(e),
            "elapsed_seconds": elapsed,
            "success": False,
        }


def run_claude(prompt: str, timeout: int = 180) -> dict:
    """Run a prompt through Claude CLI (gold standard)."""
    start = time.time()
    try:
        result = subprocess.run(
            ["claude", "-p", "--model", "claude-sonnet-4-6"],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
        )
        elapsed = time.time() - start
        output = result.stdout.strip() if result.returncode == 0 else ""
        return {
            "output": output,
            "error": "",
            "elapsed_seconds": round(elapsed, 2),
            "success": result.returncode == 0 and len(output) > 10,
        }
    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "elapsed_seconds": time.time() - start,
            "success": False,
        }


# -----------------------------------------------------------------------
# Scoring
# -----------------------------------------------------------------------


def score_output(output: str, task: dict) -> dict:
    """Score model output against expected criteria."""
    scores = {
        "has_frontmatter": False,
        "frontmatter_valid": False,
        "kind_correct": False,
        "pillar_correct": False,
        "has_headings": 0,
        "has_tables": 0,
        "has_lists": 0,
        "word_count": 0,
        "is_json": False,
        "json_valid": False,
        "total_score": 0.0,
    }

    if not output:
        return scores

    scores["word_count"] = len(output.split())

    # Frontmatter check
    fm_match = re.match(r"^---\n(.*?)\n---", output, re.DOTALL)
    if fm_match:
        scores["has_frontmatter"] = True
        fm = fm_match.group(1)

        # Check required fields
        required = ["id:", "kind:", "title:", "version:"]
        present = sum(1 for f in required if f in fm)
        scores["frontmatter_valid"] = present >= 3

        # Check kind
        if task.get("expected_kind"):
            kind_m = re.search(r"kind:\s*(\S+)", fm)
            if kind_m:
                scores["kind_correct"] = kind_m.group(1).strip().strip("'\"") == task["expected_kind"]

        # Check pillar
        if task.get("expected_pillar"):
            pillar_m = re.search(r"pillar:\s*(\S+)", fm)
            if pillar_m:
                scores["pillar_correct"] = pillar_m.group(1).strip().strip("'\"") == task["expected_pillar"]

    # Structure checks
    scores["has_headings"] = len(re.findall(r"^#{1,3} ", output, re.MULTILINE))
    scores["has_tables"] = len(re.findall(r"^\|.*\|", output, re.MULTILINE))
    scores["has_lists"] = len(re.findall(r"^[-*] ", output, re.MULTILINE))

    # JSON check (for intent resolution tasks)
    json_match = re.search(r"\{[\s\S]*\}", output)
    if json_match:
        scores["is_json"] = True
        try:
            data = json.loads(json_match.group())
            scores["json_valid"] = True
            # Check kind in JSON
            if task.get("expected_kind") and data.get("kind"):
                scores["kind_correct"] = data["kind"] == task["expected_kind"]
        except json.JSONDecodeError:
            pass

    # Composite score (0-10)
    points = 0.0
    if scores["has_frontmatter"]:
        points += 2.0
    if scores["frontmatter_valid"]:
        points += 1.5
    if scores["kind_correct"]:
        points += 1.5
    if scores["pillar_correct"]:
        points += 1.0
    if scores["has_headings"] >= 3:
        points += 1.0
    elif scores["has_headings"] >= 1:
        points += 0.5
    if scores["has_tables"] >= 1:
        points += 1.0
    if scores["word_count"] >= 100:
        points += 1.0
    elif scores["word_count"] >= 50:
        points += 0.5
    if scores["json_valid"]:
        points += 1.0
    elif scores["is_json"]:
        points += 0.5

    scores["total_score"] = round(min(points, 10.0), 1)
    return scores


# -----------------------------------------------------------------------
# Benchmark Runner
# -----------------------------------------------------------------------


def run_benchmark(models: list[str], num_tasks: int = 10,
                  include_claude: bool = True) -> dict:
    """Run full benchmark across models and tasks."""
    tasks = BENCHMARK_TASKS[:num_tasks]
    results = {
        "timestamp": datetime.now().isoformat(),
        "tasks": num_tasks,
        "models": {},
    }

    all_models = models.copy()
    if include_claude:
        all_models.append("claude-sonnet")

    for model in all_models:
        print(f"\n{'='*60}")
        print(f"  MODEL: {model}")
        print(f"{'='*60}")

        model_results = {
            "task_results": [],
            "avg_score": 0.0,
            "avg_time": 0.0,
            "success_rate": 0.0,
        }

        total_score = 0.0
        total_time = 0.0
        successes = 0

        for i, task in enumerate(tasks):
            print(f"\n  [{i+1}/{len(tasks)}] {task['name']}...", end=" ", flush=True)

            if model == "claude-sonnet":
                run_result = run_claude(task["prompt"])
            else:
                run_result = run_ollama(model, task["prompt"])

            if run_result["success"]:
                score = score_output(run_result["output"], task)
                successes += 1
                print(f"OK ({run_result['elapsed_seconds']}s, score={score['total_score']})")
            else:
                score = score_output("", task)
                err = run_result["error"][:50] if run_result["error"] else "empty output"
                print(f"FAIL ({err})")

            total_score += score["total_score"]
            total_time += run_result["elapsed_seconds"]

            model_results["task_results"].append({
                "task_id": task["id"],
                "task_name": task["name"],
                "success": run_result["success"],
                "elapsed": run_result["elapsed_seconds"],
                "score": score["total_score"],
                "details": score,
                "output_length": len(run_result["output"]),
                "error": run_result.get("error", ""),
            })

        model_results["avg_score"] = round(total_score / max(len(tasks), 1), 1)
        model_results["avg_time"] = round(total_time / max(len(tasks), 1), 1)
        model_results["success_rate"] = round(successes / max(len(tasks), 1) * 100, 0)

        results["models"][model] = model_results

        print(f"\n  --- {model} SUMMARY ---")
        print(f"  Avg Score:    {model_results['avg_score']}/10")
        print(f"  Avg Time:     {model_results['avg_time']}s")
        print(f"  Success Rate: {model_results['success_rate']}%")

    # Save results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_FILE.write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\n  Results saved to {RESULTS_FILE}")

    return results


def print_report():
    """Print comparison report from saved results."""
    if not RESULTS_FILE.exists():
        print("[ERROR] No benchmark results found. Run benchmark first.")
        return

    results = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
    print(f"\n{'='*70}")
    print("  CEX OLLAMA BENCHMARK REPORT")
    print(f"  Date: {results['timestamp']}")
    print(f"  Tasks: {results['tasks']}")
    print(f"{'='*70}\n")

    # Summary table
    print(f"  {'Model':<20} {'Score':>7} {'Time':>8} {'Success':>9}")
    print(f"  {'-'*20} {'-'*7} {'-'*8} {'-'*9}")

    for model, data in sorted(
        results["models"].items(),
        key=lambda x: -x[1]["avg_score"],
    ):
        print(
            f"  {model:<20} {data['avg_score']:>6.1f} "
            f"{data['avg_time']:>7.1f}s {data['success_rate']:>8.0f}%"
        )

    # Per-task breakdown
    print(f"\n  {'Task':<30}", end="")
    for model in results["models"]:
        short = model[:12]
        print(f" {short:>12}", end="")
    print()
    print(f"  {'-'*30}", end="")
    for _ in results["models"]:
        print(f" {'-'*12}", end="")
    print()

    task_ids = [
        t["task_id"]
        for t in results["models"][list(results["models"].keys())[0]]["task_results"]
    ]
    task_names = [
        t["task_name"]
        for t in results["models"][list(results["models"].keys())[0]]["task_results"]
    ]

    for tid, tname in zip(task_ids, task_names):
        short_name = tname[:28]
        print(f"  {short_name:<30}", end="")
        for model, data in results["models"].items():
            task_r = next((t for t in data["task_results"] if t["task_id"] == tid), None)
            if task_r:
                s = task_r["score"]
                mark = "[OK]" if task_r["success"] else "[--]"
                print(f" {s:>5.1f} {mark}", end="")
            else:
                print(f" {'N/A':>9}", end="")
        print()

    # Recommendation
    print(f"\n{'='*70}")
    best = max(results["models"].items(), key=lambda x: x[1]["avg_score"])
    print(f"  BEST MODEL: {best[0]} (score: {best[1]['avg_score']}/10)")
    print(f"{'='*70}")


# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CEX Ollama Benchmark")
    parser.add_argument("--models", default="qwen3:8b",
                        help="Comma-separated model list (default: qwen3:8b)")
    parser.add_argument("--tasks", type=int, default=10,
                        help="Number of tasks to run (default: 10, max: 10)")
    parser.add_argument("--no-claude", action="store_true",
                        help="Skip Claude comparison (saves API tokens)")
    parser.add_argument("--report", action="store_true",
                        help="Print report from saved results")
    parser.add_argument("--timeout", type=int, default=300,
                        help="Timeout per task in seconds (default: 300)")

    args = parser.parse_args()

    if args.report:
        print_report()
    else:
        models = [m.strip() for m in args.models.split(",")]
        run_benchmark(
            models=models,
            num_tasks=min(args.tasks, len(BENCHMARK_TASKS)),
            include_claude=not args.no_claude,
        )
        print_report()
