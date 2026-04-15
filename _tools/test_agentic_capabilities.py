#!/usr/bin/env python3
"""test_agentic_capabilities.py: Measure leverage capabilities of free models.

Tests the 6 capabilities that determine if we can build an agentic nucleus
runner on top of free local models. Results dictate whether we use native
tool-calling (Plan A), ReAct text parsing (Plan B), or swap base model (Plan C).

Experiments:
  E1  native tool calling    (Ollama tools: param)
  E2  ReAct text parsing     (Action: tool(args) format)
  E3  JSON mode fidelity     (strict JSON output)
  E4  multi-turn coherence   (3-turn conversation recall)
  E5  few-shot delta         (0-shot vs 2-shot adherence)
  E6  self-critique loop     (generate -> critique -> improve)

Usage:
    python _tools/test_agentic_capabilities.py --models "gemma2:9b,qwen3:14b,llama3.1:8b"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib import request

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / ".cex" / "runtime" / "benchmarks" / "agentic"
OUT.mkdir(parents=True, exist_ok=True)


def call_ollama(model: str, messages: list, tools: list = None,
                fmt: str = None, timeout: int = 120) -> dict:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"num_predict": 600, "temperature": 0.2},
    }
    if tools:
        payload["tools"] = tools
    if fmt:
        payload["format"] = fmt
    data = json.dumps(payload).encode()
    req = request.Request(
        "http://localhost:11434/api/chat",
        data=data, headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode())
        wall = time.time() - t0
        msg = body.get("message", {})
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls", [])
        content_clean = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        return {
            "ok": True, "wall": round(wall, 1),
            "content": content_clean, "tool_calls": tool_calls,
            "bytes": len(content_clean),
        }
    except Exception as e:
        return {"ok": False, "wall": round(time.time() - t0, 1), "error": str(e)}


# E1: Native tool calling
READ_FILE_TOOL = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Read contents of a file at the given path",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
}

def e1_native_tools(model: str) -> dict:
    """Does model emit tool_calls when given tools param?"""
    r = call_ollama(model, [
        {"role": "user", "content": "Read the file at /etc/hostname and tell me its contents. Use the read_file tool."}
    ], tools=[READ_FILE_TOOL])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL", "detail": r.get("error")}
    tcs = r.get("tool_calls", [])
    if tcs:
        call = tcs[0].get("function", {})
        name = call.get("name")
        args = call.get("arguments", {})
        ok = name == "read_file" and isinstance(args, dict) and "path" in args
        return {
            "score": 1.0 if ok else 0.5,
            "verdict": "OK" if ok else "PARTIAL",
            "tool_calls": len(tcs), "correct_shape": ok,
            "wall": r["wall"],
        }
    return {"score": 0, "verdict": "NO_TOOL_CALL",
            "content_preview": r["content"][:200], "wall": r["wall"]}


# E2: ReAct text parsing
REACT_SYSTEM = """You are an agent with one tool:
  read_file(path: str) -> str

Respond in this EXACT format:
Thought: <your reasoning>
Action: read_file("<path>")

Do NOT add explanation after the Action line. Stop after Action."""

REACT_PATTERN = re.compile(r'Action:\s*read_file\s*\(\s*["\']([^"\']+)["\']\s*\)', re.IGNORECASE)

def e2_react_text(model: str) -> dict:
    r = call_ollama(model, [
        {"role": "system", "content": REACT_SYSTEM},
        {"role": "user", "content": "I need the contents of /etc/hostname"}
    ])
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    m = REACT_PATTERN.search(r["content"])
    if m:
        path = m.group(1)
        ok = "hostname" in path
        return {"score": 1.0 if ok else 0.7, "verdict": "OK" if ok else "PARSED_WRONG_PATH",
                "parsed_path": path, "wall": r["wall"]}
    has_thought = "Thought:" in r["content"] or "thought:" in r["content"].lower()
    return {"score": 0.3 if has_thought else 0,
            "verdict": "UNPARSEABLE" if has_thought else "NO_FORMAT",
            "preview": r["content"][:200], "wall": r["wall"]}


# E3: JSON mode
def e3_json_mode(model: str) -> dict:
    r = call_ollama(model, [
        {"role": "user", "content": 'Return ONLY JSON with fields name (string), year (int), tags (list of 3 strings) about TF-IDF. No prose.'}
    ], fmt="json")
    if not r.get("ok"):
        return {"score": 0, "verdict": "FAIL_CALL"}
    try:
        obj = json.loads(r["content"])
        has_keys = all(k in obj for k in ["name", "year", "tags"])
        tags_ok = isinstance(obj.get("tags"), list) and len(obj["tags"]) == 3
        year_ok = isinstance(obj.get("year"), int)
        score = sum([has_keys, tags_ok, year_ok]) / 3
        return {"score": round(score, 2),
                "verdict": "OK" if score == 1.0 else "PARTIAL",
                "parsed": True, "has_keys": has_keys,
                "tags_ok": tags_ok, "year_ok": year_ok, "wall": r["wall"]}
    except json.JSONDecodeError as e:
        return {"score": 0, "verdict": "INVALID_JSON",
                "error": str(e)[:100], "preview": r["content"][:200], "wall": r["wall"]}


# E4: Multi-turn coherence
def e4_multiturn(model: str) -> dict:
    msgs = [{"role": "user", "content": "My favorite color is teal. My birthday is July 14th. Remember these."}]
    r1 = call_ollama(model, msgs)
    if not r1.get("ok"):
        return {"score": 0, "verdict": "FAIL_T1"}
    msgs.append({"role": "assistant", "content": r1["content"]})
    msgs.append({"role": "user", "content": "What's an interesting historical event from my birthday?"})
    r2 = call_ollama(model, msgs)
    if not r2.get("ok"):
        return {"score": 0, "verdict": "FAIL_T2"}
    msgs.append({"role": "assistant", "content": r2["content"]})
    msgs.append({"role": "user", "content": "In 2 words, what did I say my favorite color was?"})
    r3 = call_ollama(model, msgs)
    if not r3.get("ok"):
        return {"score": 0, "verdict": "FAIL_T3"}
    recalled_color = "teal" in r3["content"].lower()
    t2_has_bastille = "bastille" in r2["content"].lower() or "july 14" in r2["content"].lower() or "1789" in r2["content"]
    score = (1.0 if recalled_color else 0) * 0.7 + (1.0 if t2_has_bastille else 0) * 0.3
    return {"score": round(score, 2),
            "verdict": "OK" if recalled_color and t2_has_bastille else "PARTIAL" if recalled_color or t2_has_bastille else "FAIL",
            "recalled_color": recalled_color, "knew_date_context": t2_has_bastille,
            "wall_total": r1["wall"] + r2["wall"] + r3["wall"]}


# E5: Few-shot delta
E5_TASK = "Extract the city from: 'The conference will be held in Lisbon on March 5th.' Output ONLY the city name, nothing else."

def e5_fewshot(model: str) -> dict:
    # Zero-shot
    r0 = call_ollama(model, [{"role": "user", "content": E5_TASK}])
    # Few-shot
    fewshot = [
        {"role": "user", "content": "Extract the city from: 'Meeting in Paris on Friday.' Output ONLY the city name."},
        {"role": "assistant", "content": "Paris"},
        {"role": "user", "content": "Extract the city from: 'I was in Tokyo last summer.' Output ONLY the city name."},
        {"role": "assistant", "content": "Tokyo"},
        {"role": "user", "content": E5_TASK},
    ]
    r2 = call_ollama(model, fewshot)
    if not (r0.get("ok") and r2.get("ok")):
        return {"score": 0, "verdict": "FAIL_CALL"}
    # Strict: output must be exactly "Lisbon" (+/- whitespace/punct)
    def strict_ok(s): return s.strip().rstrip(".").lower() == "lisbon"
    zero_ok = strict_ok(r0["content"])
    few_ok = strict_ok(r2["content"])
    # Soft: contains Lisbon
    zero_soft = "lisbon" in r0["content"].lower()
    few_soft = "lisbon" in r2["content"].lower()
    delta = (1.0 if few_ok else 0) - (1.0 if zero_ok else 0)
    return {"zero_strict": zero_ok, "few_strict": few_ok,
            "zero_soft": zero_soft, "few_soft": few_soft,
            "zero_bytes": len(r0["content"]), "few_bytes": len(r2["content"]),
            "delta_strict": delta,
            "score": 1.0 if few_ok else 0.5 if few_soft else 0,
            "verdict": "STRICT_OK" if few_ok else "SOFT_OK" if few_soft else "FAIL"}


# E6: Self-critique
def e6_selfcritique(model: str) -> dict:
    task = "Write a 2-sentence description of TF-IDF."
    r1 = call_ollama(model, [{"role": "user", "content": task}])
    if not r1.get("ok"):
        return {"score": 0, "verdict": "FAIL_T1"}
    r2 = call_ollama(model, [
        {"role": "user", "content": task},
        {"role": "assistant", "content": r1["content"]},
        {"role": "user", "content": "Critique this in 1 sentence: what's missing or imprecise? Then rewrite it better (2 sentences)."},
    ])
    if not r2.get("ok"):
        return {"score": 0, "verdict": "FAIL_T2"}
    c1, c2 = r1["content"], r2["content"]
    has_critique = any(w in c2.lower() for w in ["missing", "imprecise", "could", "should", "lacks", "vague", "fails"])
    longer = len(c2) > len(c1)
    has_formula = "idf" in c2.lower() and ("log" in c2.lower() or "/" in c2 or "inverse" in c2.lower())
    score = sum([has_critique, longer, has_formula]) / 3
    return {"score": round(score, 2),
            "verdict": "OK" if score >= 0.67 else "PARTIAL" if score > 0 else "FAIL",
            "has_critique_language": has_critique, "longer_output": longer,
            "has_formula_detail": has_formula,
            "v1_bytes": len(c1), "v2_bytes": len(c2)}


EXPERIMENTS = [
    ("E1_native_tools", e1_native_tools),
    ("E2_react_text", e2_react_text),
    ("E3_json_mode", e3_json_mode),
    ("E4_multiturn", e4_multiturn),
    ("E5_fewshot", e5_fewshot),
    ("E6_selfcritique", e6_selfcritique),
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

    # Summary matrix
    print("\n" + "="*60)
    print("  SUMMARY (score per experiment, per model)")
    print("="*60)
    header = f"{'Exp':<20}" + "".join(f"{m:<15}" for m in models)
    print(header)
    print("-" * len(header))
    for name, _ in EXPERIMENTS:
        row = f"{name:<20}"
        for m in models:
            s = results[m][name].get("score", "?")
            v = results[m][name].get("verdict", "?")
            cell = f"{s}|{v[:10]}"
            row += f"{cell:<15}"
        print(row)

    # Aggregate score
    print("-" * len(header))
    row = f"{'AGGREGATE':<20}"
    for m in models:
        total = sum(results[m][n].get("score", 0) or 0 for n, _ in EXPERIMENTS)
        row += f"{total:.2f}/{len(EXPERIMENTS):.1f}".ljust(15)
    print(row)

    out_file = OUT / f"agentic_capabilities_{int(time.time())}.json"
    out_file.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"\nDetailed results: {out_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
