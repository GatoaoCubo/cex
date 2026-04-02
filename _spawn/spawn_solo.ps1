# CEX Spawn Solo v3.0 — clean launch, no nested quotes
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

$cliMap = @{
    n01 = 'claude'; n02 = 'claude'; n03 = 'claude'
    n04 = 'claude'; n05 = 'claude'; n06 = 'claude'
}

$root = Split-Path $PSScriptRoot -Parent
$pos = $grid[$nucleus]
$cli = $cliMap[$nucleus]
$upper = $nucleus.ToUpper()
$runtimeDir = "$root\.cex\runtime"

New-Item -ItemType Directory -Force -Path "$runtimeDir\handoffs","$runtimeDir\signals","$runtimeDir\pids" | Out-Null

# Write handoff if task provided
if ($task) {
    $handoffPath = "$runtimeDir\handoffs\${nucleus}_task.md"
    # Check if decision manifest exists
    $manifestPath = "$runtimeDir\decisions\decision_manifest.yaml"
    $manifestBlock = ""
    if (Test-Path $manifestPath) {
        $manifestBlock = @"

## DECISIONS (from user — DO NOT re-ask)
Read: .cex/runtime/decisions/decision_manifest.yaml
All subjective decisions were already made with the user.
Execute using those decisions. Do NOT override them.
If a decision is missing, use recommended default and flag it.
"@
    }

    @"
# $upper Task
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
$task
$manifestBlock

## COMMIT
git add -A
git commit -m "[$upper] task complete"

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

# ALWAYS boot interactive — task is in the handoff file, never in args
# This avoids nested-quote hell that kills CMD
$bootArgs = "/k `"$bootScript`""

# Spawn CMD window
$proc = Start-Process cmd -ArgumentList $bootArgs -WorkingDirectory $root -PassThru
Start-Sleep -Seconds 3

# Position window in grid
if ($proc -and $pos) {
    [Win32]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, 640, 520, $true) | Out-Null
}

# Record PID
$pidFile = "$runtimeDir\pids\spawn_pids.txt"
"$($proc.Id) $nucleus $cli" | Add-Content $pidFile
Write-Output "[$upper] Spawned PID:$($proc.Id) CLI:$cli at ($($pos.x),$($pos.y))"
