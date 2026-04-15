#!/usr/bin/env python3
"""cex_agentic_nucleus.py: Minimal ReAct loop for free agentic nuclei.

Runs a single nucleus task via llama3.1:8b with native tool calling.
Tools: list_dir, read_file, grep, done.

Usage:
    python _tools/cex_agentic_nucleus.py \\
        --nucleus n01 \\
        --handoff .cex/runtime/handoffs/LEVERAGE_MAP_n01.md \\
        --output .cex/runtime/out/leverage_map_n01.md
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
MAX_READ_BYTES = 8000
MAX_GREP_LINES = 40


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "list_dir",
            "description": "List entries in a directory (files + subdirs). Path relative to repo root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": f"Read a text file (capped at {MAX_READ_BYTES} bytes). Path relative to repo root.",
            "parameters": {
                "type": "object",
                "properties": {"path": {"type": "string"}},
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "grep",
            "description": f"Search for a pattern in files under a directory. Returns up to {MAX_GREP_LINES} matching lines.",
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string"},
                    "path": {"type": "string"},
                },
                "required": ["pattern", "path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "done",
            "description": "Submit the final markdown report. Call this ONLY when analysis is complete.",
            "parameters": {
                "type": "object",
                "properties": {"report": {"type": "string"}},
                "required": ["report"],
            },
        },
    },
]


def safe_path(p: str) -> Path:
    """Resolve path and ensure it stays inside repo root."""
    candidate = (ROOT / p).resolve() if not Path(p).is_absolute() else Path(p).resolve()
    if ROOT not in candidate.parents and candidate != ROOT:
        raise ValueError(f"path escape: {p}")
    return candidate


def tool_list_dir(path: str) -> str:
    p = safe_path(path)
    if not p.exists():
        return f"ERROR: path does not exist: {path}"
    if not p.is_dir():
        return f"ERROR: not a directory: {path}"
    entries = []
    for e in sorted(p.iterdir())[:80]:
        kind = "d" if e.is_dir() else "f"
        entries.append(f"{kind} {e.name}")
    return json.dumps(entries)


def tool_read_file(path: str) -> str:
    p = safe_path(path)
    if not p.exists():
        return f"ERROR: file does not exist: {path}"
    if p.is_dir():
        return f"ERROR: is a directory: {path}"
    try:
        data = p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"ERROR: {e}"
    if len(data) > MAX_READ_BYTES:
        data = data[:MAX_READ_BYTES] + f"\n... [truncated, total {len(data)} bytes]"
    return data


def tool_grep(pattern: str, path: str) -> str:
    p = safe_path(path)
    if not p.exists():
        return f"ERROR: path does not exist: {path}"
    try:
        regex = re.compile(pattern, re.IGNORECASE)
    except re.error as e:
        return f"ERROR: bad regex: {e}"
    matches = []
    targets = [p] if p.is_file() else list(p.rglob("*.md")) + list(p.rglob("*.py")) + list(p.rglob("*.yaml"))
    for f in targets[:200]:
        try:
            for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if regex.search(line):
                    rel = f.relative_to(ROOT).as_posix()
                    matches.append(f"{rel}:{i}: {line[:200]}")
                    if len(matches) >= MAX_GREP_LINES:
                        return "\n".join(matches) + f"\n... [capped at {MAX_GREP_LINES}]"
        except Exception:
            continue
    if not matches:
        return "NO_MATCHES"
    return "\n".join(matches)


def execute_tool(name: str, args: dict) -> str:
    try:
        if name == "list_dir":
            return tool_list_dir(args["path"])
        if name == "read_file":
            return tool_read_file(args["path"])
        if name == "grep":
            return tool_grep(args["pattern"], args["path"])
        return f"ERROR: unknown tool {name}"
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"


def call_ollama(model: str, messages: list, tools: list, timeout: int = 180) -> dict:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "tools": tools,
        "options": {"num_predict": 1500, "temperature": 0.3},
    }
    data = json.dumps(payload).encode()
    req = request.Request(
        "http://localhost:11434/api/chat",
        data=data, headers={"Content-Type": "application/json"},
    )
    with request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode())
    return body.get("message", {})


def agentic_loop(model: str, system: str, task: str, max_iters: int = 15, verbose: bool = True) -> dict:
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": task},
    ]
    trace = []
    t0 = time.time()
    for i in range(max_iters):
        if verbose:
            print(f"[iter {i+1}/{max_iters}]", flush=True)
        msg = call_ollama(model, messages, TOOLS)
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls", [])

        if not tool_calls:
            parsed = parse_text_tool_call(content)
            if parsed:
                tool_calls = parsed
                if verbose:
                    print(f"  [fallback parse] {tool_calls[0]['function']['name']}", flush=True)

        if not tool_calls:
            trace.append({"iter": i + 1, "type": "text_only", "content": content[:300]})
            if verbose:
                print(f"  -> no tool_calls, stopping. Final: {content[:200]}", flush=True)
            return {"ok": True, "final": content, "iters": i + 1,
                    "wall": round(time.time() - t0, 1), "trace": trace, "reason": "no_tool_call"}

        messages.append({"role": "assistant", "content": content, "tool_calls": tool_calls})

        for tc in tool_calls:
            name = tc.get("function", {}).get("name", "")
            args = tc.get("function", {}).get("arguments", {})
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except Exception:
                    args = {}

            if verbose:
                arg_preview = json.dumps(args)[:120]
                print(f"  tool: {name}({arg_preview})", flush=True)

            if name == "done":
                report = args.get("report", "")
                trace.append({"iter": i + 1, "type": "done", "bytes": len(report)})
                return {"ok": True, "final": report, "iters": i + 1,
                        "wall": round(time.time() - t0, 1), "trace": trace, "reason": "done_called"}

            result = execute_tool(name, args)
            trace.append({"iter": i + 1, "tool": name, "args": args, "result_bytes": len(result)})
            if verbose:
                print(f"    -> {len(result)} bytes", flush=True)
            messages.append({"role": "tool", "content": result[:4000]})

    return {"ok": False, "final": "MAX_ITERS", "iters": max_iters,
            "wall": round(time.time() - t0, 1), "trace": trace, "reason": "max_iters"}


SYSTEM_PROMPT = """You are a CEX nucleus agent. Use the provided tools to explore files and build an analysis.

Available tools: list_dir, read_file, grep, done.

Workflow:
- Call list_dir, read_file, grep to gather evidence
- When analysis is complete, call done(report=<full markdown>) to submit
- Max 15 tool calls total

IMPORTANT: invoke tools via the tool_calls mechanism. Do not write tool calls as JSON in your text response."""


JSON_CALL_RE = re.compile(r'\{\s*"name"\s*:\s*"([^"]+)"\s*,\s*"(?:parameters|arguments)"\s*:\s*(\{[^{}]*\})\s*\}', re.DOTALL)


def parse_text_tool_call(content: str):
    """Fallback: parse JSON-in-text tool calls emitted by llama3.1."""
    m = JSON_CALL_RE.search(content)
    if not m:
        return None
    name = m.group(1)
    try:
        args = json.loads(m.group(2))
    except Exception:
        return None
    return [{"function": {"name": name, "arguments": args}}]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--nucleus", required=True, help="nucleus id (n01..n06)")
    p.add_argument("--handoff", required=True, help="path to handoff .md file")
    p.add_argument("--output", required=True, help="where to write the final report")
    p.add_argument("--model", default="llama3.1:8b")
    p.add_argument("--max-iters", type=int, default=15)
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    handoff_path = Path(args.handoff)
    if not handoff_path.exists():
        print(f"ERROR: handoff not found: {args.handoff}", file=sys.stderr)
        return 1
    task = handoff_path.read_text(encoding="utf-8")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    system = SYSTEM_PROMPT + f"\n\nYou are nucleus {args.nucleus.upper()}. Your directory is N0{args.nucleus[-1]}_*/"

    print(f"[{args.nucleus}] starting agentic loop with {args.model}", flush=True)
    result = agentic_loop(args.model, system, task,
                          max_iters=args.max_iters, verbose=not args.quiet)

    output_path.write_text(result["final"], encoding="utf-8")
    trace_path = output_path.with_suffix(".trace.json")
    trace_path.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")

    print(f"[{args.nucleus}] done: reason={result['reason']}, iters={result['iters']}, "
          f"wall={result['wall']}s, bytes={len(result['final'])}", flush=True)
    print(f"[{args.nucleus}] output: {output_path}", flush=True)
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
