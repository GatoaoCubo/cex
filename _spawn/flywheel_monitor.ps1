# CEX Flywheel Monitor -- Autonomous doc-vs-practice loop
# Runs audit every N minutes, logs results, alerts on regression.
#
# Usage:
#   powershell -ExecutionPolicy Bypass -File _spawn/flywheel_monitor.ps1
#   powershell -ExecutionPolicy Bypass -File _spawn/flywheel_monitor.ps1 -Interval 30 -MaxRounds 10
#   powershell -ExecutionPolicy Bypass -File _spawn/flywheel_monitor.ps1 -Mode heal

param(
    [int]$Interval = 30,       # minutes between rounds
    [int]$MaxRounds = 48,      # max rounds (48 * 30min = 24h)
    [string]$Mode = "audit",   # audit | heal | loop
    [switch]$Verbose
)

$CEX_ROOT = Split-Path -Parent $PSScriptRoot
Set-Location $CEX_ROOT

$LogDir = Join-Path $CEX_ROOT ".cex\quality"
if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }

$LogFile = Join-Path $LogDir "flywheel_monitor.log"
$StartTime = Get-Date

function Log($msg) {
    $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

Log "=========================================="
Log "CEX FLYWHEEL MONITOR v1.0"
Log "Mode: $Mode | Interval: ${Interval}min | MaxRounds: $MaxRounds"
Log "=========================================="

$PrevWired = 0
$PrevBroken = 0

for ($round = 1; $round -le $MaxRounds; $round++) {
    Log ""
    Log "--- Round $round / $MaxRounds ---"

    # Run audit
    $output = python _tools/cex_flywheel_audit.py $Mode 2>&1 | Out-String

    # Parse results
    $wiredMatch = [regex]::Match($output, "WIRED:\s+(\d+)")
    $brokenMatch = [regex]::Match($output, "BROKEN:\s+(\d+)")
    $phantomMatch = [regex]::Match($output, "PHANTOM:\s+(\d+)")
    $healthMatch = [regex]::Match($output, "HEALTH:\s+(\d+)%")

    $wired = if ($wiredMatch.Success) { [int]$wiredMatch.Groups[1].Value } else { 0 }
    $broken = if ($brokenMatch.Success) { [int]$brokenMatch.Groups[1].Value } else { 0 }
    $phantom = if ($phantomMatch.Success) { [int]$phantomMatch.Groups[1].Value } else { 0 }
    $health = if ($healthMatch.Success) { $healthMatch.Groups[1].Value + "%" } else { "?%" }

    Log "Health: $health | WIRED=$wired BROKEN=$broken PHANTOM=$phantom"

    # Detect regression
    if ($round -gt 1 -and $wired -lt $PrevWired) {
        Log "!!! REGRESSION DETECTED: WIRED dropped $PrevWired -> $wired !!!"
        # Write alert file
        $alertFile = Join-Path $LogDir "ALERT_regression_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
        "REGRESSION: WIRED $PrevWired -> $wired at round $round" | Out-File $alertFile
    }

    # Detect improvement
    if ($round -gt 1 -and $broken -lt $PrevBroken) {
        Log "+++ IMPROVEMENT: BROKEN reduced $PrevBroken -> $broken +++"
    }

    # Perfect health = early exit
    if ($broken -eq 0 -and $phantom -eq 0) {
        Log "*** ALL CHECKS PASSED -- system healthy ***"
    }

    # Model staleness check (every 4th round ~ every 2h)
    if ($round % 4 -eq 1) {
        Log "Checking model versions..."
        $modelOutput = python _tools/cex_model_updater.py --check --json 2>&1 | Out-String
        try {
            $modelData = $modelOutput | ConvertFrom-Json
            if ($modelData.count -gt 0) {
                Log "!!! STALE MODELS: $($modelData.count) model(s) need update. Run: python _tools/cex_model_updater.py --full"
            } else {
                Log "Models: all current"
            }
        } catch {
            Log "Model check: parse error (non-critical)"
        }
    }

    $PrevWired = $wired
    $PrevBroken = $broken

    if ($Verbose) {
        # Log full output
        $output -split "`n" | ForEach-Object { Log "  $_" }
    }

    # Git snapshot if changes detected
    $gitStatus = git status --porcelain 2>$null
    if ($gitStatus) {
        Log "Git: uncommitted changes detected, auto-snapshot..."
        git add .cex/quality/ 2>$null
        git commit -m "[flywheel] round ${round}: health=$health wired=$wired broken=$broken" 2>$null
        Log "Git: committed snapshot"
    }

    if ($round -lt $MaxRounds) {
        $sleepSec = $Interval * 60
        Log "Sleeping ${Interval}min until next round..."
        Start-Sleep -Seconds $sleepSec
    }
}

$elapsed = ((Get-Date) - $StartTime).TotalMinutes
Log ""
Log "=========================================="
Log "FLYWHEEL MONITOR COMPLETE"
Log "Rounds: $MaxRounds | Elapsed: $([math]::Round($elapsed))min"
Log "Final: WIRED=$PrevWired BROKEN=$PrevBroken"
Log "=========================================="
