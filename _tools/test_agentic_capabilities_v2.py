#!/usr/bin/env python3
"""test_agentic_capabilities_v2.py: Round 2 experiments.

E7  long context needle    (retrieve fact buried in 3K text)
E8  code correctness       (generate + self-verify python)
E9  error recovery         (adapt when tool returns error)
E10 planning decomposition (break task into numbered steps)
E11 tool loop simulation   (multi-step ReAct: list -> read -> answer)
E12 strict format delta    (markdown sections in exact order)

Usage:
    python _tools/test_agentic_capabilities_v2.py --models "gemma2:9b,qwen3:14b,llama3.1:8b"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib import request

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".cex" / "runtime" / "benchmarks" / "agentic"
OUT.mkdir(parents=True, exist_ok=True)


def call_ollama(
    model: str,
    messages: list[dict[str, str]],
    fmt: str | None = None,
    timeout: int = 180,
    num_predict: int = 800,
) -> dict[str, Any]:
    payload = {
        "model": model, "messages": messages, "stream": False,
        "options": {"num_predict": num_predict, "temperature": 0.2},
    }
    if fmt:
        payload["format"] = fmt
    data = json.dumps(payload).encode()
    req = request.Request("http://localhost:11434/api/chat", data=data,
                          headers={"Content-Type": "application/json"})
    t0 = time.time()
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode())
        content = body.get("message", {}).get("content", "")
        content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        return {"ok": True, "wall": round(time.time() - t0, 1), "content": content}
    except Exception as e:
        return {"ok": False, "wall": round(time.time() - t0, 1), "error": str(e)}


# E7: Long context needle
def e7_long_context(model: str) -> dict[str, Any]:
    filler = "The benchmark system tracks model performance over time. " * 60  # ~3K chars
    needle = "SECRET_CODE_ALPHA_47Q is the activation key."
    haystack = filler[:1500] + " " + needle + " " + filler[:1500]
    r = call_ollama(model, [
        {"role": "user", "content": f"Read this text carefully:\n\n{haystack}\n\nWhat is the activation key? Output ONLY the key value (format ALPHA_XXX)."}
    ])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    found = "ALPHA_47Q" in r["content"].upper()
    return {"score": 1.0 if found else 0,
            "verdict": "OK" if found else "FAIL",
            "wall": r["wall"], "preview": r["content"][:150]}


# E8: Code correctness (generate fibonacci + we verify)
def e8_code_correctness(model: str) -> dict[str, Any]:
    r = call_ollama(model, [
        {"role": "user", "content": "Write a Python function `fib(n)` that returns the nth Fibonacci number (0-indexed, fib(0)=0, fib(1)=1, fib(7)=13). Output ONLY the code, no explanation, no markdown fences."}
    ])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    code = r["content"].strip()
    # Strip markdown fences if present
    code = re.sub(r"^```\w*\n?", "", code)
    code = re.sub(r"\n?```$", "", code)
    try:
        ns = {}
        exec(code, ns)
        fib = ns.get("fib")
        if not callable(fib):
            return {"score": 0, "verdict": "NO_FUNC", "preview": code[:200]}
        tests = [(0, 0), (1, 1), (7, 13), (10, 55)]
        passed = sum(1 for n, exp in tests if fib(n) == exp)
        return {"score": round(passed / 4, 2),
                "verdict": f"{passed}/4_PASS",
                "wall": r["wall"]}
    except Exception as e:
        return {"score": 0, "verdict": "EXEC_ERR",
                "error": str(e)[:100], "preview": code[:200]}


# E9: Error recovery
def e9_error_recovery(model: str) -> dict[str, Any]:
    msgs = [
        {"role": "system", "content": "You are an agent. Use read_file(path) tool. Respond with Action: read_file(\"<path>\")"},
        {"role": "user", "content": "Get the contents of the config file at ./config.yaml"},
        {"role": "assistant", "content": 'Action: read_file("./config.yaml")'},
        {"role": "user", "content": "ERROR: File not found at ./config.yaml. It may be at a different path. Try again."},
    ]
    r = call_ollama(model, msgs)
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    content = r["content"].lower()
    # Good recovery: tries different path (e.g. /etc, /P09_config/, src/)
    adapted = bool(re.search(r'read_file\(["\'][^"\']+\.ya?ml["\']\)', r["content"], re.IGNORECASE))
    tried_different_path = adapted and "./config.yaml" not in r["content"]
    return {"score": 1.0 if tried_different_path else 0.5 if adapted else 0,
            "verdict": "ADAPTED" if tried_different_path else "REPEATED" if adapted else "FAIL",
            "preview": r["content"][:200], "wall": r["wall"]}


# E10: Planning decomposition
def e10_planning(model: str) -> dict[str, Any]:
    r = call_ollama(model, [
        {"role": "user", "content": "I need to build a web scraper that extracts product prices from a shopping site and saves to CSV. Break this into exactly 5 numbered steps (1-5). Format: '1. <step>'. Output ONLY the numbered list, no preamble."}
    ])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    content = r["content"].strip()
    steps = re.findall(r'^\s*(\d+)\.\s+(.+?)$', content, re.MULTILINE)
    correct_count = len(steps) == 5
    sequential = all(int(n) == i+1 for i, (n, _) in enumerate(steps))
    has_scraping = any("scrap" in s[1].lower() or "fetch" in s[1].lower() or "request" in s[1].lower() for s in steps)
    has_csv = any("csv" in s[1].lower() or "save" in s[1].lower() or "write" in s[1].lower() for s in steps)
    score = sum([correct_count, sequential, has_scraping, has_csv]) / 4
    return {"score": round(score, 2),
            "verdict": "OK" if score == 1 else "PARTIAL" if score > 0.5 else "FAIL",
            "step_count": len(steps), "sequential": sequential,
            "wall": r["wall"]}


# E11: Tool loop simulation (3-step ReAct)
def e11_tool_loop(model: str) -> dict[str, Any]:
    sys_prompt = """You are an agent. Available tools:
  list_dir(path) -> list of filenames
  read_file(path) -> file contents
  done(answer) -> final answer

Respond ONE action at a time in this EXACT format:
Action: <tool>("<arg>")

Do not add explanations after the Action. Wait for the observation before the next action."""

    # Turn 1: list
    msgs = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": "Find the port number in the project's config files."},
    ]
    r1 = call_ollama(model, msgs, num_predict=100)
    if not r1.get("ok"):
        return {"score": 0, "verdict": "FAIL_T1"}

    t1_ok = bool(re.search(r'list_dir\(', r1["content"]))
    msgs.append({"role": "assistant", "content": r1["content"]})

    # Turn 2: provide fake observation
    msgs.append({"role": "user", "content": 'Observation: ["settings.yaml", "readme.md", "main.py"]'})
    r2 = call_ollama(model, msgs, num_predict=100)
    if not r2.get("ok"):
        return {"score": 0.33 if t1_ok else 0, "verdict": "FAIL_T2"}

    t2_ok = bool(re.search(r'read_file\(["\'].*settings\.ya?ml["\']\)', r2["content"], re.IGNORECASE))
    msgs.append({"role": "assistant", "content": r2["content"]})

    # Turn 3: provide file contents
    msgs.append({"role": "user", "content": 'Observation: "server:\\n  host: localhost\\n  port: 8080\\n"'})
    r3 = call_ollama(model, msgs, num_predict=100)
    if not r3.get("ok"):
        return {"score": 0.66 if (t1_ok and t2_ok) else 0, "verdict": "FAIL_T3"}

    t3_ok = "8080" in r3["content"] and ("done(" in r3["content"].lower() or "Action: done" in r3["content"])
    score = sum([t1_ok, t2_ok, t3_ok]) / 3
    return {"score": round(score, 2),
            "verdict": "FULL_LOOP" if score == 1 else "PARTIAL" if score > 0.33 else "FAIL",
            "t1_listed": t1_ok, "t2_read_right_file": t2_ok, "t3_done_with_answer": t3_ok,
            "wall_total": r1["wall"] + r2["wall"] + r3["wall"]}


# E12: Strict format adherence
def e12_strict_format(model: str) -> dict[str, Any]:
    r = call_ollama(model, [
        {"role": "user", "content": """Output EXACTLY this structure (markdown with these 4 sections in this order, nothing more):

## Problem
<1 sentence>

## Approach
<1 sentence>

## Trade-offs
<1 sentence>

## Conclusion
<1 sentence>

Topic: choosing between SQL and NoSQL for a social media app."""}
    ])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    content = r["content"]
    expected = ["## Problem", "## Approach", "## Trade-offs", "## Conclusion"]
    found_order = [s for s in expected if s in content]
    in_order = found_order == expected
    no_extras = len(re.findall(r'^##\s', content, re.MULTILINE)) == 4
    no_preamble = content.strip().startswith("## Problem")
    score = sum([in_order, no_extras, no_preamble]) / 3
    return {"score": round(score, 2),
            "verdict": "STRICT" if score == 1 else "PARTIAL" if score > 0.5 else "FAIL",
            "in_order": in_order, "no_extras": no_extras, "no_preamble": no_preamble,
            "wall": r["wall"]}


EXPERIMENTS = [
    ("E7_long_context", e7_long_context),
    ("E8_code_correct", e8_code_correctness),
    ("E9_error_recovery", e9_error_recovery),
    ("E10_planning", e10_planning),
    ("E11_tool_loop", e11_tool_loop),
    ("E12_strict_format", e12_strict_format),
]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--models", default="gemma2:9b,qwen3:14b,llama3.1:8b")
    args = p.parse_args()
    models = [m.strip() for m in args.models.split(",") if m.strip()]

    results = {}
    for model in models:
        print(f"\n{'='*60}\n  Model: {model}\n{'='*60}")
        results[model] = {}
        for name, fn in EXPERIMENTS:
            print(f"  [{name}]", end=" ", flush=True)
            t0 = time.time()
            try:
                r = fn(model)
            except Exception as e:
                r = {"score": 0, "verdict": "EXCEPTION", "error": str(e)}
            r["elapsed"] = round(time.time() - t0, 1)
            results[model][name] = r
            print(f"-> {r.get('verdict','?')} score={r.get('score','?')} ({r['elapsed']}s)")

    print("\n" + "="*60)
    print("  SUMMARY (round 2)")
    print("="*60)
    header = f"{'Exp':<22}" + "".join(f"{m:<15}" for m in models)
    print(header); print("-" * len(header))
    for name, _ in EXPERIMENTS:
        row = f"{name:<22}"
        for m in models:
            s = results[m][name].get("score", "?")
            v = results[m][name].get("verdict", "?")[:10]
            row += f"{str(s)+'|'+v:<15}"
        print(row)
    print("-" * len(header))
    row = f"{'AGGREGATE':<22}"
    for m in models:
        total = sum(results[m][n].get("score", 0) or 0 for n, _ in EXPERIMENTS)
        row += f"{total:.2f}/{len(EXPERIMENTS):.1f}".ljust(15)
    print(row)

    out_file = OUT / f"agentic_capabilities_v2_{int(time.time())}.json"
    out_file.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"\nDetailed results: {out_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
