---
id: spec_preflight_boot_integration
kind: decision_record
title: Preflight Boot Integration Spec
version: 1.0.0
quality: 9.0
tags: [preflight, boot, optimization, token-budget]
created: 2026-04-13
density_score: 1.0
---

# Preflight Boot Integration

## Decision

Integrate `cex_preflight.py` into the nucleus boot pipeline so that every dispatch automatically pre-compiles context before the main model starts.

## Current Boot Flow

```
spawn_grid.ps1 / dispatch.sh
  -> boot/n0X.ps1
     -> set env vars
     -> & claude --model X --append-system-prompt agent_card.md ...
```

## New Boot Flow (with preflight)

```
spawn_grid.ps1 / dispatch.sh
  -> boot/n0X.ps1
     -> set env vars
     -> python _tools/cex_preflight.py --handoff {handoff_path} --output {cache_file}
        (runs on Ollama/Haiku, ~5-10 seconds, $0 or negligible cost)
     -> & claude --model X --append-system-prompt agent_card.md
                           --append-system-prompt {cache_file}
```

## Changes Required

### 1. boot/n0X.ps1 (all 6 nucleus boot scripts)

Add before `& claude @cliArgs`:

```powershell
# --- Preflight: pre-compile context (local/cheap model) ---
$preflightCache = "$cexRoot\.cex\cache\preflight\${nucleus}_latest.md"
$handoffPath = "$cexRoot\.cex\runtime\handoffs\${nucleus}_task.md"
if (Test-Path $handoffPath) {
    Set-CexTitle "PREFLIGHT"
    $preflightResult = & python "$cexRoot\_tools\cex_preflight.py" --handoff $handoffPath --output $preflightCache 2>&1
    if ($LASTEXITCODE -eq 0 -and (Test-Path $preflightCache)) {
        $cliArgs += "--append-system-prompt", $preflightCache
        Write-Host "  [OK] Preflight: context pre-compiled" -ForegroundColor Green
    } else {
        Write-Host "  [WARN] Preflight skipped (fallback: full context)" -ForegroundColor Yellow
    }
}
```

### 2. boot_gen.py (regenerate boot scripts)

Update `_tools/cex_boot_gen.py` template to include the preflight block.
This ensures new nuclei or regenerated boots always have preflight.

### 3. cex_preflight.py --output flag

The `--output` flag writes a markdown file (not JSON) suitable for direct injection
via `--append-system-prompt`. Format:

```markdown
# Preflight Context for {nucleus} — {kind}

## Selected ISOs (top {N} of 13)
{iso_content}

## Selected Knowledge Cards (top {N})
{kc_content}

## Task Context
{compressed_handoff}
```

### 4. spawn_grid.ps1

No changes needed — grid dispatches via boot scripts, which now include preflight.

## Graceful Degradation

| Scenario | Behavior |
|----------|----------|
| Ollama offline + Haiku offline | Skip preflight, boot with full context (current behavior) |
| Ollama slow (>30s) | Timeout, skip preflight |
| Preflight cache exists and fresh | Use cache, skip recomputation |
| No handoff file | Skip preflight (nucleus boots interactive) |

## Metrics

Track in `.cex/cache/preflight/stats.json`:
- `total_preflights`: count
- `avg_reduction_pct`: rolling average
- `cache_hits`: count (reused existing cache)
- `local_calls`: Ollama usage count
- `cloud_calls`: Haiku usage count
- `tokens_saved_total`: cumulative

## Timeline

1. N05 delivers `cex_preflight.py` (current dispatch)
2. N07 integrates into boot scripts (next task)
3. Regenerate boot scripts via `cex_boot_gen.py`
4. Test: dispatch N03 with preflight, verify token reduction
