param(
  [int]$HardCapHours = 10,
  [int]$WaveTimeoutSec = 1500,
  [int]$FlywheelSleepSec = 180
)

# Overnight orchestrator -- runs TYPE_HINT_RETROFIT W3..W7 then falls back to
# cex vs cex self-improvement (cex_auto + cex_evolve). Designed to run in an
# isolated PowerShell window; survives N07 session exit. All errors logged,
# no user prompts, no interactive blocks.

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$stamp = Get-Date -Format "yyyyMMdd_HHmm"
$stateDir = "$root\_reports\overnight"
if (-not (Test-Path $stateDir)) { New-Item -ItemType Directory -Path $stateDir | Out-Null }
$state = "$stateDir\state_$stamp.md"
$log   = "$stateDir\log_$stamp.txt"

$start = Get-Date
$deadline = $start.AddHours($HardCapHours)

function Log($msg) {
  $line = "[$((Get-Date).ToString('HH:mm:ss'))] $msg"
  Add-Content -Path $log -Value $line -Encoding UTF8
  Write-Host $line
}

function State($section, $body) {
  Add-Content -Path $state -Value "## $section" -Encoding UTF8
  Add-Content -Path $state -Value $body -Encoding UTF8
  Add-Content -Path $state -Value "" -Encoding UTF8
}

# Header
Set-Content -Path $state -Value "# Overnight codex orchestrator -- $stamp" -Encoding UTF8
Add-Content -Path $state -Value "" -Encoding UTF8
Add-Content -Path $state -Value "Start: $start" -Encoding UTF8
Add-Content -Path $state -Value "Hard cap: $HardCapHours hours (deadline $deadline)" -Encoding UTF8
Add-Content -Path $state -Value "Wave timeout: $WaveTimeoutSec s" -Encoding UTF8
Add-Content -Path $state -Value "" -Encoding UTF8

Log "Overnight orchestrator started. Deadline=$deadline"

# -----------------------------------------------------------------------
# PHASE A -- TYPE_HINT_RETROFIT queue (W3..W7)
# -----------------------------------------------------------------------

$waves = @(
  @{ name="W3"; targets=@("cex_sanitize.py","cex_showoff.py","cex_vector_store.py","test_agentic_capabilities_v2.py","test_wave1_builder_gen_v2.py","cex_finetune_export.py") },
  @{ name="W4"; targets=@("cex_discovery.py","cex_ft_train.py","cex_memo.py","wave_pipeline.py","cex_intent_resolver.py","cex_litellm_test.py") },
  @{ name="W5"; targets=@("cex_score_python.py","cex_evolve_below9.py","cex_flywheel_worker.py","notebooklm_create.py","translate_isos.py","cex_release_check.py") },
  @{ name="W6"; targets=@("cex_system_test.py","wave1_builder_gen_v2.py","test_cex_wave_validator.py") },
  @{ name="W7"; targets=@("cex_overnight.py","brand_validate.py","cex_continuous.py","cex_mission_state.py","cex_mission_runner.py","cex_index.py","cex_notebooklm.py") }
)

function Write-TypeHintHandoff($waveName, $targets) {
  $reportPath = "_reports/ops/type_hint_retrofit_$($waveName.ToLower())_$stamp.md"
  $targetsYaml = ($targets | ForEach-Object { "  - _tools/$_" }) -join "`n"
  $handoff = @"
---
mission: TYPE_HINT_RETROFIT
wave: $waveName
nucleus: n05
role: mechanical_refactor
runtime: codex
auto_accept: true
deliverable_report: $reportPath
report_priority: 1
targets:
$targetsYaml
timeout_s: $WaveTimeoutSec
---

# N05 TYPE_HINT_RETROFIT $waveName

## Context

Overnight wave $waveName. Add type hints to every public function
(non-underscore-prefixed) in every target file.

## Deliverable

Per file:
1. Parameter types on all args except self/cls.
2. Return types on all functions (None if no return).
3. Use typing stdlib; prefer builtin generics if file is py3.10+.
4. Any is acceptable when genuinely ambiguous.
5. One commit per file: ``refactor(<tool>): add type hints to public functions``.
6. No body/logic/name/decorator changes. Annotations only.
7. ASCII-only per .claude/rules/ascii-code-rule.md.

## Verification per file

``python -c "import ast; t=ast.parse(open('_tools/<f>.py').read()); fns=[n for n in ast.walk(t) if isinstance(n,ast.FunctionDef) and not n.name.startswith('_')]; ty=[n for n in fns if n.returns and all(a.annotation for a in n.args.args if a.arg not in ('self','cls'))]; print(len(ty),'/',len(fns))"``

Target 100% or Any. ``python _tools/<f>.py --help`` must still exit 0 for CLI tools; ``python -c "import _tools.<f>"`` must import cleanly for libs.

## Report (PRIORITY 1)

Write $reportPath with coverage delta table, commit list, sanity checks, and trailing ``## TYPE_HINT_RETROFIT_${waveName}_PASS`` sentinel. Write it BEFORE the last commit if budget is tight.

## Boundaries

Only touch the files listed. No other edits. No renames. No ``# type: ignore``.

## Budget

$WaveTimeoutSec s. Waves W1/W2 proved this shape at 60 fns in 181 s and 81 fns in 271 s. Adjust `Any` fallback aggressively if approaching deadline.
"@
  Set-Content -Path ".cex\runtime\handoffs\n05_task_codex.md" -Value $handoff -Encoding UTF8
}

function Wait-Wave($maxSec, $reportPath) {
  $t0 = Get-Date
  while ($true) {
    $elapsed = ((Get-Date) - $t0).TotalSeconds
    if (Test-Path $reportPath) { return "COMPLETE" }
    if ($elapsed -ge $maxSec) { return "TIMEOUT" }
    Start-Sleep -Seconds 30
  }
}

function Push-IfClean {
  git add -A 2>&1 | Out-Null
  $pending = git status --porcelain 2>&1
  if ($pending) {
    git commit -m "chore(overnight): auto-commit stray artifacts [$stamp]" 2>&1 | Out-Null
  }
  git push origin main 2>&1 | Out-Null
}

$waveIdx = 0
foreach ($wave in $waves) {
  if ((Get-Date) -ge $deadline) { Log "Deadline hit before wave $($wave.name); skipping rest of Phase A"; break }
  $waveIdx++
  $reportPath = "_reports/ops/type_hint_retrofit_$($wave.name.ToLower())_$stamp.md"
  Log "Phase A wave $($wave.name) -- $($wave.targets.Count) files -- report=$reportPath"
  Write-TypeHintHandoff $wave.name $wave.targets

  # Kill any lingering n05 before dispatching
  bash _spawn/dispatch.sh stop n05 2>&1 | Out-Null
  Start-Sleep -Seconds 2

  $dispatchOut = bash _spawn/dispatch.sh solo-codex n05 2>&1
  Log "Dispatched wave $($wave.name): $($dispatchOut | Select-Object -Last 1)"

  $result = Wait-Wave $WaveTimeoutSec $reportPath
  Log "Wave $($wave.name) result=$result"

  # Kill codex regardless (done or timed out)
  bash _spawn/dispatch.sh stop n05 2>&1 | Out-Null
  Start-Sleep -Seconds 5

  Push-IfClean
  $commits = git log --oneline -20 | Select-String "$($wave.targets[0].Replace('.py',''))|wave|$($wave.name)" | Select-Object -First 10
  State "Phase A -- Wave $($wave.name)" @"
Result: $result
Report: $reportPath
Last commits:
$($commits -join "`n")
"@
}

Log "Phase A complete. Moving to Phase B (flywheel)."

# -----------------------------------------------------------------------
# PHASE B -- CEX vs CEX self-improvement (cex_auto + cex_evolve)
# -----------------------------------------------------------------------

$cycle = 0
while ((Get-Date) -lt $deadline) {
  $cycle++
  $mode = if ($cycle % 2 -eq 1) { "auto" } else { "evolve" }
  Log "Phase B cycle $cycle mode=$mode"

  $cycleReport = "$stateDir\phase_b_cycle${cycle}_$stamp.log"
  try {
    if ($mode -eq "auto") {
      # Self-healing flywheel: scan + plan + execute one cycle
      python _tools/cex_auto.py cycle --max 10 *>&1 | Tee-Object -FilePath $cycleReport | Out-Null
    } else {
      # Heuristic batch over quality:null files (free, no LLM)
      python _tools/cex_evolve.py sweep --target 8.5 --max-rounds 2 *>&1 | Tee-Object -FilePath $cycleReport | Out-Null
    }
  } catch {
    Log "Phase B cycle $cycle ERROR: $_"
  }

  Push-IfClean
  $tail = Get-Content $cycleReport -Tail 10 -ErrorAction SilentlyContinue
  State "Phase B -- cycle $cycle ($mode)" @"
Log: $cycleReport
Tail:
$($tail -join "`n")
"@

  Log "Phase B cycle $cycle done. Sleeping $FlywheelSleepSec s."
  Start-Sleep -Seconds $FlywheelSleepSec
}

# -----------------------------------------------------------------------
# SHUTDOWN
# -----------------------------------------------------------------------

$end = Get-Date
$durMin = [math]::Round(($end - $start).TotalMinutes, 1)
Log "Overnight orchestrator finished. Duration=${durMin} min"

State "Summary" @"
Start: $start
End:   $end
Duration: $durMin min
Phase A waves attempted: $waveIdx / $($waves.Count)
Phase B cycles: $cycle
Log file: $log
"@

Push-IfClean
