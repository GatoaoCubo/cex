You are N07, the orchestrator. The user wants to autonomously improve artifacts.

## Three Modes

### Mode 1: TRUE AutoResearch via SDK (agent mode)
Karpathy pattern — Python controls the loop, LLM generates hypotheses via `execute_prompt()`.
Budget-tracked, provider-agnostic, no subprocess spawning.
All LLM calls go through the SDK cascade (Anthropic → OpenAI → Ollama → CLI fallback).

```bash
# Evolve one artifact (budget-tracked, stops at target or budget)
python _tools/cex_evolve.py agent <file>
python _tools/cex_evolve.py agent <file> --budget 50000 --target 9.0 --max-rounds 10
```

The loop:
1. Python reads artifact, sends to LLM: "suggest ONE improvement"
2. LLM returns hypothesis + modified content
3. Python applies change, runs cex_score.py (immutable metric)
4. Keep (git commit) or discard (git restore)
5. Check budget → continue or stop

**This is the real AutoResearch.** Budget-enforced, tracked, autonomous.

### Mode 2: Hybrid Auto-Hook (auto mode)
Designed to run automatically after every artifact creation.
Heuristic pass (free, 0 tokens) → score → agent only if score < threshold.

```bash
python _tools/cex_evolve.py auto <file>
python _tools/cex_evolve.py auto <file> --threshold 8.5 --budget 30000
```

**This is wired into `cex_run.py` as the post-build hook.** Every artifact created
via the pipeline gets auto-evolved: heuristic for free, agent only when needed.

### Mode 3: Heuristic Fallback (no LLM, fast batch)
Python-only mechanical fixes. Useful when LLM budget is limited.
Does NOT generate creative improvements — only frontmatter, whitespace, filler removal.

```bash
python _tools/cex_evolve.py single <file> --target 9.0
python _tools/cex_evolve.py sweep --target 8.5
python _tools/cex_evolve.py report
```

## When to Use Which

| Situation | Mode | Why |
|-----------|------|-----|
| Improve one important artifact deeply | `agent` | LLM generates real hypotheses, budget-tracked |
| After building any artifact (automatic) | `auto` | Wired into pipeline, smart budget |
| Score 300 builder specs | `sweep` | No LLM needed for batch scoring |
| Post-mission cleanup | `sweep` | Fast, mechanical |
| User says "make this better" | `agent` | Creative improvement needs LLM |
| User is AFK for hours | `agent --budget 200000` | Runs until budget exhausted |

## Architecture (SDK Integration)

```
cex_evolve.py (Python controls the loop)
    │
    └── execute_prompt()          ← cex_intent.py (single SDK gateway)
         │
         ├── SDK Anthropic        ← ANTHROPIC_API_KEY
         ├── SDK OpenAI           ← OPENAI_API_KEY
         ├── SDK Ollama           ← local
         ├── CLI claude           ← fallback
         └── HTTP Ollama          ← last resort
```

All token tracking, provider routing, and budget enforcement happen automatically.

## The 3-File Architecture (Karpathy)

| File | Role | Who controls |
|------|------|-------------|
| `program.md` | Strategy hints (optional) | Human (read-only) |
| Target artifact | The file being improved | Python loop + LLM suggestions |
| `cex_score.py` | The immutable metric | Nobody (read-only) |
