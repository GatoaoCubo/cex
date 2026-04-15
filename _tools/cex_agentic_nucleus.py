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


def agentic_loop(model: str, system: str, task: str, max_iters: int = 15,
                 verbose: bool = True, min_iters: int = 4,
                 history: list | None = None,
                 require_reads_before_done: int = 2) -> dict:
    """Run ReAct loop. If history is passed, append to it (REPL continuation).

    Anti-fabrication: done() is rejected if fewer than
    `require_reads_before_done` read_file/grep calls happened first.
    """
    if history is None:
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": task},
        ]
    else:
        messages = history
        messages.append({"role": "user", "content": task})
    trace = []
    t0 = time.time()
    nudges_used = 0
    MAX_NUDGES = 2
    reads_performed = 0
    fabrication_rejections = 0
    MAX_FABRICATION_REJECTIONS = 2
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
            # Stop guard: nudge up to MAX_NUDGES times if shallow (iters too low OR content thin)
            shallow = (i + 1) < min_iters or len(content) < 1500
            if nudges_used < MAX_NUDGES and shallow:
                nudges_used += 1
                if verbose:
                    print(f"  [GUARD {nudges_used}/{MAX_NUDGES}] iters={i+1} content={len(content)}B. Nudging.", flush=True)
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content":
                    f"You stopped after {i+1} tool uses with only {len(content)} bytes of output. "
                    "That is not enough. The handoff requires a complete report with ALL required "
                    "sections (Verification, New Wired Tools, Still Missing, Next Iteration). "
                    "Use list_dir/read_file/grep to gather more evidence. When ready, call "
                    "done(report=<full markdown>) to submit."})
                continue
            trace.append({"iter": i + 1, "type": "text_only", "content": content[:300]})
            if verbose:
                print(f"  -> no tool_calls, stopping. Final: {content[:200]}", flush=True)
            return {"ok": True, "final": content, "iters": i + 1,
                    "wall": round(time.time() - t0, 1), "trace": trace,
                    "reason": "no_tool_call", "history": messages}

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
                # Anti-fabrication guard: require evidence-gathering first
                if reads_performed < require_reads_before_done and \
                   fabrication_rejections < MAX_FABRICATION_REJECTIONS:
                    fabrication_rejections += 1
                    if verbose:
                        print(f"  [ANTI-FAB {fabrication_rejections}/{MAX_FABRICATION_REJECTIONS}] "
                              f"done() with only {reads_performed} reads < {require_reads_before_done}. "
                              "Rejecting.", flush=True)
                    trace.append({"iter": i + 1, "type": "done_rejected",
                                  "reads": reads_performed, "bytes": len(report)})
                    messages.append({"role": "tool", "content":
                        f"REJECTED: done() called with only {reads_performed} read_file/grep "
                        f"call(s). You must gather evidence by reading at least "
                        f"{require_reads_before_done} files/grep results before submitting. "
                        "Do NOT fabricate numbers or claims. Call list_dir, read_file, or grep "
                        "to gather real evidence from the repo, THEN call done()."})
                    continue
                trace.append({"iter": i + 1, "type": "done", "bytes": len(report),
                              "reads": reads_performed})
                return {"ok": True, "final": report, "iters": i + 1,
                        "wall": round(time.time() - t0, 1), "trace": trace,
                        "reason": "done_called", "history": messages}

            result = execute_tool(name, args)
            if name in ("read_file", "grep"):
                reads_performed += 1
            trace.append({"iter": i + 1, "tool": name, "args": args,
                          "result_bytes": len(result), "reads_so_far": reads_performed})
            if verbose:
                print(f"    -> {len(result)} bytes (reads={reads_performed})", flush=True)
            messages.append({"role": "tool", "content": result[:4000]})

    return {"ok": False, "final": "MAX_ITERS", "iters": max_iters,
            "wall": round(time.time() - t0, 1), "trace": trace,
            "reason": "max_iters", "history": messages}


SYSTEM_PROMPT = f"""You are a CEX nucleus agent running inside the CEX repository on Windows.

REPO ROOT: {ROOT}
OS: Windows (paths use forward slashes, relative to repo root).
ALL PATHS MUST BE RELATIVE. Examples: "_tools", "N01_intelligence", "archetypes/builders".
FORBIDDEN: "/home/user/...", "/tmp/...", "C:\\\\Users\\\\..." -- those do not exist here.
FORBIDDEN: glob patterns in paths ("N06_*", "_tools/*.py") -- use exact paths or use grep instead.

Available tools (invoke via tool_calls, NOT JSON in content):
- list_dir(path)      -- list entries under a relative path
- read_file(path)     -- read a file (UTF-8, capped at 8KB)
- grep(pattern, path) -- regex search under a dir or file
- done(report)        -- submit final markdown report (ends the loop)

========================================
MANDATORY: 8F PIPELINE (every task, every time)
========================================
You do NOT just call tools and write a report. You execute the 8F reasoning pipeline:

F1 CONSTRAIN: Read .cex/kinds_meta.json (grep for the kind you care about).
              Identify pillar, naming rule, max_bytes.
F2 BECOME:    Read archetypes/builders/{{kind}}-builder/bld_manifest_{{kind}}.md
              and bld_instruction_{{kind}}.md. Load your identity.
F3 INJECT:    Read P01_knowledge/library/kind/kc_{{kind}}.md for the knowledge card.
              grep for similar artifacts (e.g., compiled/, N0x/). Collect 2-3 examples.
F4 REASON:    Plan your report: which sections, what claims, what evidence for each.
F5 CALL:      Any remaining tool calls needed to fill evidence gaps.
F6 PRODUCE:   Draft the report with ALL required sections from the handoff.
F7 GOVERN:    Self-check: does every claim cite a file you read? are all required
              sections present? are any numbers fabricated?
F8 COLLABORATE: Call done(report=<full markdown>).

ANTI-FABRICATION RULES:
1. Every numeric claim ("N builders", "X files") MUST come from a tool result.
   If you did not read/grep for it, DO NOT state it.
2. Every file path you reference MUST exist (you saw it via list_dir or read_file).
3. If the handoff lists required sections, include them ALL -- even if empty ("None observed").
4. Do NOT drift: stay on the tool/artifact the handoff asks about. Do not pivot to
   "comprehensive vocabulary atlas" or other tangents.

DISCIPLINE:
- Minimum 4-6 tool calls BEFORE done(). The runner will reject premature done() calls.
- Target >= 1500 bytes in your final report. Thin reports get nudged.
- If a required section has no evidence yet, go gather it -- do not guess.

If the user asks a conversational question (no file to read), answer briefly
without inventing paths."""


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


def auto_commit(nucleus: str, output_path: Path, mission: str) -> None:
    """Stage output + commit with nucleus attribution."""
    import subprocess
    try:
        rel = output_path.relative_to(ROOT).as_posix()
        subprocess.run(["git", "add", rel], cwd=ROOT, check=False, capture_output=True)
        msg = f"[{nucleus.upper()}] {mission}: agentic report via llama3.1:8b"
        subprocess.run(["git", "commit", "-m", msg, "--no-verify"],
                       cwd=ROOT, check=False, capture_output=True)
        print(f"[{nucleus}] committed {rel}", flush=True)
    except Exception as e:
        print(f"[{nucleus}] commit skipped: {e}", flush=True)


def interactive_repl(nucleus: str, model: str, last_result: dict, output_path: Path) -> None:
    """Drop into REPL so user can ask follow-ups or approve commit."""
    print("\n" + "=" * 60, flush=True)
    print(f"  {nucleus.upper()} READY - interactive mode", flush=True)
    print("  Commands:", flush=True)
    print("    <type a task>  -> run another agentic loop", flush=True)
    print("    :show          -> show last output", flush=True)
    print("    :commit        -> git commit the output", flush=True)
    print("    :quit          -> exit window", flush=True)
    print("=" * 60, flush=True)

    system = SYSTEM_PROMPT + f"\n\nYou are nucleus {nucleus.upper()}."
    # Carry history from the initial loop so REPL keeps mission context
    history = last_result.get("history")
    if history is None:
        history = [{"role": "system", "content": system}]
    repl_turn = 0

    while True:
        try:
            user_input = input(f"\n[{nucleus}]> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nbye")
            break

        if not user_input:
            continue
        if user_input == ":quit":
            break
        if user_input == ":show":
            print(last_result.get("final", ""))
            continue
        if user_input == ":commit":
            auto_commit(nucleus, output_path, "INTERACTIVE")
            continue
        if user_input == ":reset":
            history = [{"role": "system", "content": system}]
            print(f"[{nucleus}] history reset", flush=True)
            continue

        # run new agentic task, preserve history, write to separate file
        repl_turn += 1
        result = agentic_loop(model, system, user_input, max_iters=10,
                              verbose=True, history=history)
        history = result.get("history", history)
        repl_out = output_path.with_name(f"{output_path.stem}.repl{repl_turn}.md")
        repl_out.write_text(result["final"], encoding="utf-8")
        last_result = result
        print(f"\n[{nucleus}] done: {result['reason']}, {result['iters']} iters, "
              f"{result['wall']}s, saved {repl_out.name}")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--nucleus", required=True, help="nucleus id (n01..n06)")
    p.add_argument("--handoff", required=True, help="path to handoff .md file")
    p.add_argument("--output", required=True, help="where to write the final report")
    p.add_argument("--model", default="llama3.1:8b")
    p.add_argument("--max-iters", type=int, default=15)
    p.add_argument("--require-reads", type=int, default=2,
                   help="Minimum read_file/grep calls before done() accepted (anti-fabrication)")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--interactive", action="store_true", help="drop into REPL after loop")
    p.add_argument("--auto-commit", action="store_true", help="git commit output after loop")
    p.add_argument("--mission", default="TASK", help="mission tag for commit messages")
    args = p.parse_args()

    handoff_path = Path(args.handoff)
    if not handoff_path.exists():
        print(f"ERROR: handoff not found: {args.handoff}", file=sys.stderr)
        return 1
    task = handoff_path.read_text(encoding="utf-8")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    system = SYSTEM_PROMPT + f"\n\nYou are nucleus {args.nucleus.upper()}. Your directory is N0{args.nucleus[-1]}_*/"

    print("=" * 60, flush=True)
    print(f"  {args.nucleus.upper()} - {args.mission} - {args.model}", flush=True)
    print("=" * 60, flush=True)
    print(f"Handoff: {args.handoff}", flush=True)
    print(f"Output:  {args.output}", flush=True)
    print("", flush=True)

    result = agentic_loop(args.model, system, task,
                          max_iters=args.max_iters, verbose=not args.quiet,
                          require_reads_before_done=args.require_reads)

    output_path.write_text(result["final"], encoding="utf-8")
    trace_path = output_path.with_suffix(".trace.json")
    trace_path.write_text(json.dumps(result, indent=2, default=str), encoding="utf-8")

    print("\n" + "=" * 60, flush=True)
    print(f"[{args.nucleus}] COMPLETE: {result['reason']}, {result['iters']} iters, "
          f"{result['wall']}s, {len(result['final'])} bytes", flush=True)
    print(f"[{args.nucleus}] Output: {output_path}", flush=True)
    print("=" * 60, flush=True)

    if args.auto_commit:
        auto_commit(args.nucleus, output_path, args.mission)

    if args.interactive:
        interactive_repl(args.nucleus, args.model, result, output_path)

    return 0 if result["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
