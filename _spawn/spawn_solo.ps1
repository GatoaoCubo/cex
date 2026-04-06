# CEX Spawn Solo v4.0 -- reads nucleus_models.yaml (single source of truth)
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('n01','n02','n03','n04','n05','n06','n07')]
    [string]$nucleus,
    [string]$task = "",
    [switch]$interactive
)

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

$grid = @{
    n01 = @{x=0;    y=0};    n02 = @{x=640;  y=0}
    n03 = @{x=1280; y=0};    n04 = @{x=0;    y=520}
    n05 = @{x=640;  y=520};  n06 = @{x=1280; y=520}
}

$root = Split-Path $PSScriptRoot -Parent
$pos = $grid[$nucleus]
$upper = $nucleus.ToUpper()
$runtimeDir = "$root\.cex\runtime"

New-Item -ItemType Directory -Force -Path "$runtimeDir\handoffs","$runtimeDir\signals","$runtimeDir\pids" | Out-Null

# -- Read CLI from nucleus_models.yaml (single source of truth) --
$cli = "claude"  # fallback
$modelsFile = "$root\.cex\config\nucleus_models.yaml"
if (Test-Path $modelsFile) {
    $inNucleus = $false
    foreach ($line in Get-Content $modelsFile) {
        if ($line -match "^${nucleus}:") { $inNucleus = $true; continue }
        if ($inNucleus -and $line -match "^\w" -and $line -notmatch "^\s") { break }
        if ($inNucleus -and $line -match "^\s+cli:\s*(.+)") {
            $cli = $matches[1].Trim()
            break
        }
    }
}
Write-Output "[$upper] CLI from nucleus_models: $cli"

# Write handoff if task provided
if ($task) {
    $handoffPath = "$runtimeDir\handoffs\${nucleus}_task.md"
    # Check if decision manifest exists
    $manifestPath = "$runtimeDir\decisions\decision_manifest.yaml"
    $manifestBlock = ""
    if (Test-Path $manifestPath) {
        $manifestBlock = @"

## DECISIONS (from user -- DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.
"@
    }

    @"
---
nucleus: $upper
task: dispatch
created: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
---
# Task for $upper

$task
$manifestBlock

## ON COMPLETION
1. Commit your work: git add -A && git commit -m "[$upper] <description>"
2. Signal complete:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('$nucleus', 'complete', 9.0)"
"@ | Set-Content -Path $handoffPath -Encoding UTF8
    Write-Output "[$upper] Handoff: $handoffPath"
}

# Boot script
$bootScript = "$root\boot\$nucleus.cmd"
if (-not (Test-Path $bootScript)) {
    Write-Output "[$upper] ERROR: $bootScript not found"; exit 1
}

# ALWAYS boot interactive -- task is in the handoff file, never in args
# This avoids nested-quote hell that kills CMD
$bootArgs = "/k `"$bootScript`""

# Spawn CMD window
$proc = Start-Process cmd -ArgumentList $bootArgs -WorkingDirectory $root -PassThru
Start-Sleep -Seconds 3

# Position window in grid
if ($proc -and $pos) {
    [Win32]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, 640, 520, $true) | Out-Null
}

# Record PID with session tracking
# Session ID = PID of the PowerShell/pi that called us (our parent orchestrator)
$sessionId = $env:CEX_SESSION_ID
if (-not $sessionId) {
    # Auto-detect: use parent process PID as session identifier
    $myPid = $PID
    $parentPid = (Get-CimInstance Win32_Process -Filter "ProcessId=$myPid" -EA SilentlyContinue).ParentProcessId
    $sessionId = "s$parentPid"
}
$timestamp = Get-Date -Format "yyyy-MM-dd_HH:mm:ss"
$pidFile = "$runtimeDir\pids\spawn_pids.txt"
"$($proc.Id) $nucleus $cli $sessionId $timestamp" | Add-Content $pidFile
Write-Output "[$upper] Spawned PID:$($proc.Id) CLI:$cli Session:$sessionId at ($($pos.x),$($pos.y))"
