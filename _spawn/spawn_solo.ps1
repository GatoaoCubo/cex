# CEX Spawn Solo v4.0 -- reads nucleus_models.yaml (single source of truth)
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('n01','n02','n03','n04','n05','n06','n07')]
    [string]$nucleus,
    [string]$task = "",
    [switch]$interactive,
    [ValidateSet('claude','gemini','codex','ollama','litellm','auto')]
    [string]$cli = ""   # if empty, read from nucleus_models.yaml
)

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

# Dynamic grid: detect screen size, calculate 3x2 layout
# Works on any monitor. Taskbar-aware via WorkingArea.
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$cols = 3; $rows = 2
$cellW = [math]::Floor($screen.Width / $cols)
$cellH = [math]::Floor($screen.Height / $rows)
$ox = $screen.X; $oy = $screen.Y

# Fixed cell map -- same layout as spawn_grid.ps1
# +--------+--------+--------+
# |  N01   |  N02   |  N03   |
# +--------+--------+--------+
# |  N04   |  N05   |  N06   |
# +--------+--------+--------+
$grid = @{
    n01 = @{x=$ox;             y=$oy}
    n02 = @{x=$ox+$cellW;      y=$oy}
    n03 = @{x=$ox+2*$cellW;    y=$oy}
    n04 = @{x=$ox;             y=$oy+$cellH}
    n05 = @{x=$ox+$cellW;      y=$oy+$cellH}
    n06 = @{x=$ox+2*$cellW;    y=$oy+$cellH}
}

$root = Split-Path $PSScriptRoot -Parent
$pos = $grid[$nucleus]
$upper = $nucleus.ToUpper()
$runtimeDir = "$root\.cex\runtime"

New-Item -ItemType Directory -Force -Path "$runtimeDir\handoffs","$runtimeDir\signals","$runtimeDir\pids" | Out-Null

# -- CLI selection --
# If -cli was passed explicitly, honor it (enables `dispatch.sh solo-ollama n04`).
# Otherwise read from nucleus_models.yaml (single source of truth).
if (-not $cli) {
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
} else {
    Write-Output "[$upper] CLI from -cli arg: $cli"
}

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

# Kill-before-spawn (roadmap principle 6)
$pidFile = "$runtimeDir\pids\spawn_pids.txt"
if (Test-Path $pidFile) {
    $surviving = @()
    foreach ($line in Get-Content $pidFile) {
        if ($line -match "^\s*(\d+)\s+$nucleus\s") {
            $oldPid = [int]$matches[1]
            Write-Output "[$upper] Killing existing PID:$oldPid before respawn"
            & taskkill /F /PID $oldPid /T 2>$null
        } else {
            $surviving += $line
        }
    }
    if ($surviving.Count -gt 0) {
        $surviving | Set-Content $pidFile -Encoding UTF8
    } else {
        Remove-Item $pidFile -Force
    }
}

# Boot script -- PowerShell-only stack (sin-aware UX: colors, sizing, banner)
# Per-CLI suffix: claude -> n0X.ps1 | gemini -> n0X_gemini.ps1 | ollama -> n0X_ollama.ps1
$cliSuffix = if ($cli -eq "claude") { "" } else { "_$cli" }
$bootPs1 = "$root\boot\${nucleus}${cliSuffix}.ps1"

if (Test-Path $bootPs1) {
    Write-Output "[$upper] Boot: PowerShell (sin-aware UX)"
    $proc = Start-Process powershell -ArgumentList @(
        "-NoProfile", "-NoExit", "-ExecutionPolicy", "Bypass",
        "-File", $bootPs1
    ) -WorkingDirectory $root -PassThru
} else {
    Write-Output "[$upper] ERROR: no boot script at $bootPs1"; exit 1
}

# Position window in fixed grid cell (retry loop for window handle)
if ($proc -and $pos) {
    $hwnd = [IntPtr]::Zero
    for ($i = 0; $i -lt 10; $i++) {
        Start-Sleep -Milliseconds 500
        try { $proc.Refresh() } catch {}
        $hwnd = $proc.MainWindowHandle
        if ($hwnd -ne [IntPtr]::Zero) { break }
    }
    if ($hwnd -ne [IntPtr]::Zero) {
        [Win32]::MoveWindow($hwnd, $pos.x, $pos.y, $cellW, $cellH, $true) | Out-Null
    } else {
        Write-Output "[$upper] WARN: no window handle after 5s -- window not positioned"
    }
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
"$($proc.Id) $nucleus $cli $sessionId $timestamp" | Add-Content $pidFile
Write-Output "[$upper] Spawned PID:$($proc.Id) CLI:$cli Session:$sessionId at ($($pos.x),$($pos.y))"
