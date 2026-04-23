# /consolidate -- Full Resource Manager

Post-dispatch lifecycle: processes + GPU + signals + verify.

## Steps

### 1. Stop Processes

```bash
bash _spawn/dispatch.sh stop
```

Kill all nuclei spawned by this session. Uses session-aware PID tracking
so other N07 orchestrators are not affected.

### 2. Free GPU VRAM

```bash
nvidia-smi --query-gpu=memory.used,memory.free --format=csv,noheader
```

If Ollama models are loaded, unload them:

```bash
ollama stop
```

Report VRAM before and after. If nvidia-smi is not available (no GPU),
skip this step and note "No GPU detected".

### 3. Archive Signals

```bash
mkdir -p .cex/runtime/signals_archive/
mv .cex/runtime/signals/signal_*.json .cex/runtime/signals_archive/ 2>/dev/null
```

Report count of signals moved. If none exist, report "0 signals to archive".

### 4. Verify Deliverables

For each nucleus that signaled completion:
- Check that artifact files exist at the paths declared in the handoff
- Run quick doctor check:

```bash
python _tools/cex_doctor.py --quick
```

Report pass/fail per nucleus.

### 5. Git State

```bash
git status
```

- If uncommitted changes exist from Gemini nuclei: `git add` + `git commit` their work
- Show recent history:

```bash
git log --oneline -5
```

### 6. Report

Print consolidated summary:

```
--- Consolidation Report ---
Processes: N killed
GPU: X MB freed (before -> after)
Signals: N archived
Artifacts: N/M verified
Quality: avg score from doctor
Git: clean | N uncommitted files
---
```
