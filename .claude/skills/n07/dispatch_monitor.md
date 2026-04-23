# dispatch_monitor -- Non-Blocking Dispatch Monitor

Pattern for N07 to monitor dispatched nuclei without blocking.

## Principle

N07 must NEVER block waiting for nuclei. Instead, interleave monitoring
checks with productive work on N07's own backlog.

## Monitor Commands (non-blocking, ~2s each)

### Git Activity

```bash
git log --oneline --since="3 minutes ago"
```

Detects nucleus commits. If a nucleus committed, it is done or progressing.

### Process State

```bash
bash _spawn/dispatch.sh status
```

Shows which nuclei are alive, their PIDs, and uptime.

### GPU State

```bash
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.free --format=csv,noheader
```

High utilization = Ollama inference active. Zero utilization = idle or done.

## Timing

- Check every 60-90 seconds (not every second -- wastes tokens and context)
- Do 2-3 of N07's own tasks between checks
- If a nucleus has been silent for 15+ minutes, investigate (check PID alive)

## Anti-Patterns

- DO NOT use `python _tools/cex_signal_watch.py` -- it blocks N07 entirely
- DO NOT poll every second -- 60-90s intervals are sufficient
- DO NOT idle while waiting -- always work on N07 backlog between checks

## N07 Backlog Ideas (work on these between checks)

1. Read and verify a spec against reality
2. Audit a pillar schema for completeness
3. Write or update a memory file
4. Check artifact quality distribution
5. Plan next mission waves
6. Update terminology or metaphor dictionary
7. Investigate a new industry pattern

## Detection Heuristics

| Signal | Meaning | Action |
|--------|---------|--------|
| New commits in git log | Nucleus produced artifacts | Note progress, continue |
| All expected nuclei committed | Wave complete | Run /consolidate |
| PID gone from status | Nucleus exited | Check if it committed (success) or crashed (no output) |
| No commits for 15+ min | Possibly stuck | Check PID alive, investigate logs |
| GPU idle, nuclei still running | CPU-bound work or stalled | Normal for non-Ollama runs |
