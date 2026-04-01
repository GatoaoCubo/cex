You are N07, the orchestrator. The user wants to autonomously improve artifacts.

## Two Modes

### Mode 1: TRUE AutoResearch (agent mode)
Karpathy pattern — an LLM agent reads `program.md`, modifies the target artifact,
and runs experiments autonomously. The agent generates creative hypotheses.
The metric (`cex_score.py`) is immutable. Keep/discard via git.

```bash
# Spawn an LLM agent to evolve one artifact (runs until interrupted)
python _tools/cex_evolve.py agent <file>
python _tools/cex_evolve.py agent <file> --provider codex
python _tools/cex_evolve.py agent <file> --provider gemini
```

The agent reads `program.md` in the repo root. That file contains:
- The experiment loop protocol
- What the agent can/cannot modify
- Quality dimensions and strategy tips
- The "NEVER STOP" instruction

**This is the real AutoResearch.** The LLM is the researcher.

### Mode 2: Heuristic Fallback (no LLM, fast batch)
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
| Improve one important artifact deeply | `agent` | LLM generates real hypotheses |
| Score 300 builder specs | `sweep` | No LLM needed for batch scoring |
| Post-mission cleanup | `sweep` | Fast, mechanical |
| User says "make this better" | `agent` | Creative improvement needs LLM |
| User is AFK for hours | `agent` | Runs indefinitely |

## The 3-File Architecture (Karpathy)

| File | Role | Who writes | Who modifies |
|------|------|-----------|-------------|
| `program.md` | Experiment loop instructions | Human | Nobody (read-only) |
| Target artifact | The file being improved | Agent | Agent only |
| `cex_score.py` | The metric | Human | Nobody (immutable) |
