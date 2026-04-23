# CEX Flywheel Orchestrator v1.0
# Overnight continuous batching: nuclei feed each other in cycles
#
# Flywheel order:
#   N03 Engineering -> N04 Knowledge -> N01 Research ->
#   N05 Operations -> N02 Marketing -> N06 Commercial -> N07 Admin -> loop
#
# Usage:
#   powershell -NoProfile -ExecutionPolicy Bypass -File _tools/cex_flywheel.ps1
#   powershell -File _tools/cex_flywheel.ps1 -maxCycles 5 -level 2
#   powershell -File _tools/cex_flywheel.ps1 -dryRun
#   powershell -File _tools/cex_flywheel.ps1 -slots 2 -sleepBetween 300

param(
    [int]$maxCycles     = 10,       # max flywheel rotations
    [int]$slots         = 3,        # concurrent nucleus builds
    [int]$level         = 1,        # 1=core 7 kinds, 2=expanded
    [int]$pollSeconds   = 30,       # signal check interval
    [int]$sleepBetween  = 120,      # seconds between cycles
    [int]$stuckTimeout  = 900,      # 15 min max per nucleus
    [switch]$dryRun,
    [switch]$interactive
)

$ErrorActionPreference = "Continue"
$root = $PSScriptRoot | Split-Path -Parent
$signalDir = "$root\.cex_signals"
$logFile = "$root\.cex_signals\flywheel.log"
$python = "python"

# Flywheel order: Engineering first (builds others), then knowledge infra, then output
$FLYWHEEL = @("N03", "N04", "N01", "N05", "N07", "N02", "N06")
$DOMAINS = @{
    N01="Research"; N02="Marketing"; N03="Engineering"; N04="Knowledge";
    N05="Operations"; N06="Commercial"; N07="Admin"
}

# Ensure signal dir
New-Item -ItemType Directory -Path $signalDir -Force -EA SilentlyContinue | Out-Null

function Log($msg) {
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    $line = "[$ts] $msg"
    Write-Host $line
    Add-Content -Path $logFile -Value $line -EA SilentlyContinue
}

function Get-Signal($nucleus, $cycle) {
    Get-ChildItem "$signalDir\${nucleus}_cycle${cycle}_*.json" -EA SilentlyContinue |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1
}

function Clear-OldSignals {
    $archiveDir = "$signalDir\archive"
    New-Item -ItemType Directory -Path $archiveDir -Force -EA SilentlyContinue | Out-Null
    Get-ChildItem "$signalDir\*.json" -EA SilentlyContinue |
        Move-Item -Destination $archiveDir -Force -EA SilentlyContinue
}

function Start-NucleusWorker($nucleus, $cycle) {
    $workerScript = "$root\_tools\cex_flywheel_worker.py"
    $args_list = @("$workerScript", "--nucleus", $nucleus, "--cycle", $cycle, "--level", $level)
    if ($dryRun) { $args_list += "--dry-run" }

    Log "  SPAWN: $nucleus ($($DOMAINS[$nucleus])) cycle=$cycle level=$level"

    $proc = Start-Process -FilePath $python -ArgumentList $args_list `
        -WorkingDirectory $root -PassThru -NoNewWindow `
        -RedirectStandardOutput "$signalDir\${nucleus}_cycle${cycle}_stdout.txt" `
        -RedirectStandardError "$signalDir\${nucleus}_cycle${cycle}_stderr.txt"

    return $proc
}

function Wait-ForSlot($procs, $nuclei, $cycle) {
    $elapsed = 0
    while ($true) {
        foreach ($i in 0..($procs.Count - 1)) {
            if ($procs[$i] -and $procs[$i].HasExited) {
                $nuc = $nuclei[$i]
                $sig = Get-Signal $nuc $cycle
                if ($sig) {
                    $content = Get-Content $sig.FullName -Raw | ConvertFrom-Json
                    Log "  DONE: $nuc status=$($content.status) passes=$($content.details.passes)"
                } else {
                    Log "  DONE: $nuc (no signal file)"
                }
                return $i
            }
        }

        Start-Sleep -Seconds $pollSeconds
        $elapsed += $pollSeconds

        if ($elapsed -ge $stuckTimeout) {
            # Kill stuck processes
            foreach ($i in 0..($procs.Count - 1)) {
                if ($procs[$i] -and -not $procs[$i].HasExited) {
                    Log "  STUCK: $($nuclei[$i]) -- killing after ${stuckTimeout}s"
                    $procs[$i].Kill()
                    return $i
                }
            }
        }
    }
}

# ============================================================
#  MAIN LOOP
# ============================================================

Log "============================================================"
Log "  CEX FLYWHEEL v1.0"
Log "  Cycles: $maxCycles | Slots: $slots | Level: $level"
Log "  Sleep between: ${sleepBetween}s | Stuck timeout: ${stuckTimeout}s"
Log "  Mode: $(if ($dryRun) {'DRY-RUN'} else {'EXECUTE'})"
Log "============================================================"

Clear-OldSignals

for ($cycle = 1; $cycle -le $maxCycles; $cycle++) {
    Log ""
    Log "======== CYCLE $cycle / $maxCycles ========"

    # Queue all 7 nuclei in flywheel order
    $queue = [System.Collections.ArrayList]@($FLYWHEEL)

    # Active processes and their nuclei
    $activeProcs = @()
    $activeNuclei = @()

    # Fill initial slots
    $initialSlots = [Math]::Min($slots, $queue.Count)
    for ($s = 0; $s -lt $initialSlots; $s++) {
        $nuc = $queue[0]
        $queue.RemoveAt(0)
        $proc = Start-NucleusWorker $nuc $cycle
        $activeProcs += $proc
        $activeNuclei += $nuc
    }

    # Continuous batching: when a slot frees, fill from queue
    while ($activeProcs.Count -gt 0) {
        $freeSlot = Wait-ForSlot $activeProcs $activeNuclei $cycle

        if ($queue.Count -gt 0) {
            # Refill slot
            $nextNuc = $queue[0]
            $queue.RemoveAt(0)
            $proc = Start-NucleusWorker $nextNuc $cycle
            $activeProcs[$freeSlot] = $proc
            $activeNuclei[$freeSlot] = $nextNuc
        } else {
            # Remove completed slot
            $newProcs = @()
            $newNuclei = @()
            for ($i = 0; $i -lt $activeProcs.Count; $i++) {
                if ($i -ne $freeSlot) {
                    $newProcs += $activeProcs[$i]
                    $newNuclei += $activeNuclei[$i]
                }
            }
            $activeProcs = $newProcs
            $activeNuclei = $newNuclei
        }
    }

    # Cycle summary
    $signals = Get-ChildItem "$signalDir\*_cycle${cycle}_*.json" -EA SilentlyContinue
    $completes = ($signals | ForEach-Object {
        (Get-Content $_.FullName -Raw | ConvertFrom-Json).status
    } | Where-Object { $_ -eq "complete" }).Count

    Log ""
    Log "  CYCLE $cycle SUMMARY: $completes/$($FLYWHEEL.Count) complete"

    # Sleep between cycles (unless last cycle)
    if ($cycle -lt $maxCycles) {
        Log "  SLEEP: ${sleepBetween}s until next cycle..."
        Start-Sleep -Seconds $sleepBetween
    }
}

# Final report
Log ""
Log "============================================================"
Log "  FLYWHEEL COMPLETE: $maxCycles cycles"
Log "============================================================"

# Count total signals
$allSignals = Get-ChildItem "$signalDir\*.json" -EA SilentlyContinue
$totalComplete = ($allSignals | ForEach-Object {
    (Get-Content $_.FullName -Raw -EA SilentlyContinue | ConvertFrom-Json).status
} | Where-Object { $_ -eq "complete" }).Count

Log "  Total signals: $($allSignals.Count)"
Log "  Total complete: $totalComplete"
Log "  Log: $logFile"
Log "============================================================"
