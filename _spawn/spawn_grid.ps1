# CEX Spawn Grid v1.0 -- Launch multiple nucleus builders
# Usage:
#   powershell -File _spawn/spawn_grid.ps1 -mission NAME -interactive
#   powershell -File _spawn/spawn_grid.ps1 -mission NAME -mode continuous

param(
    [string]$mission = "",
    [ValidateSet('auto','static','continuous')]
    [string]$mode = "auto",
    [switch]$interactive,
    [int]$pollSeconds = 30,
    [int]$maxMinutes = 45,
    [int]$maxSlots = 6,
    [ValidateSet('claude','gemini','codex')]
    [string]$cli = "claude"
)

# Multi-CLI config:
#   claude -> boot/n0X.ps1       + handoff copy .cex/runtime/handoffs/n0X_task.md
#   gemini -> boot/n0X_gemini.ps1 + handoff copy .cex/runtime/handoffs/n0X_task_gemini.md
#   codex  -> boot/n0X_codex.ps1  + handoff copy .cex/runtime/handoffs/n0X_task_codex.md
$cliSuffix = if ($cli -eq "claude") { "" } else { "_$cli" }

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Grid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

$root = Split-Path $PSScriptRoot -Parent
$handoffDir = "$root\.cex/runtime/handoffs"
$signalDir = "$root\.cex/runtime/signals"
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"

New-Item -ItemType Directory -Force -Path $handoffDir,$signalDir,"$root\.cex\runtime\pids" | Out-Null

# Dynamic grid: detect screen size, adapt layout to nucleus count
Add-Type -AssemblyName System.Windows.Forms
$scr = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$gOx = $scr.X; $gOy = $scr.Y

# gridPos is computed AFTER handoff discovery (see below)
$gridPos = @{}

# Discover handoffs for mission
$handoffs = @()
if ($mission) {
    $handoffs = Get-ChildItem "$handoffDir\${mission}_*.md" -EA SilentlyContinue | Sort-Object Name
}
if (-not $handoffs -or $handoffs.Count -eq 0) {
    $handoffs = Get-ChildItem "$handoffDir\*.md" -EA SilentlyContinue | Sort-Object Name
}

if ($handoffs.Count -eq 0) {
    Write-Output "[GRID] No handoffs found in $handoffDir"
    exit 1
}

# Auto-detect mode
if ($mode -eq "auto") {
    $mode = if ($handoffs.Count -gt $maxSlots) { "continuous" } else { "static" }
}
# Fixed 3x2 grid layout (3 cols, 2 rows) -- each nucleus has a PERMANENT cell
# Just by looking at screen position you know which nucleus it is:
#
#   +--------+--------+--------+
#   |  N01   |  N02   |  N03   |
#   +--------+--------+--------+
#   |  N04   |  N05   |  N06   |
#   +--------+--------+--------+
#
$n = $handoffs.Count
$gCols = 3; $gRows = 2
$gW = [math]::Floor($scr.Width / $gCols)
$gH = [math]::Floor($scr.Height / $gRows)

# Fixed cell map: nucleus -> (col, row) -- NEVER changes regardless of dispatch order
$fixedCells = @{
    "n01" = @{col=0; row=0}  # top-left
    "n02" = @{col=1; row=0}  # top-center
    "n03" = @{col=2; row=0}  # top-right
    "n04" = @{col=0; row=1}  # bottom-left
    "n05" = @{col=1; row=1}  # bottom-center
    "n06" = @{col=2; row=1}  # bottom-right
}

# Build position map from fixed cells
foreach ($h in $handoffs) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($h.Name)
    $parts = $base -split '_'
    $nuc = $parts[-1]
    $cell = $fixedCells[$nuc]
    if ($cell) {
        $gridPos[$nuc] = @{x=$gOx + $cell.col * $gW; y=$gOy + $cell.row * $gH}
    } else {
        # Unknown nucleus -- fallback to first empty cell
        $gridPos[$nuc] = @{x=$gOx; y=$gOy}
    }
}

Write-Output "[GRID] Mission: $mission | Mode: $mode | Handoffs: $n | Layout: ${gCols}x${gRows}"

# Extract nucleus from handoff filename (pattern: {mission}_{nucleus}.md or {mission}_batch_{N}_{nucleus}.md)
function Get-NucleusFromHandoff($filename) {
    $base = [System.IO.Path]::GetFileNameWithoutExtension($filename)
    $parts = $base -split '_'
    return $parts[-1]  # last segment is nucleus name
}

# Launch a single nucleus with handoff
function Launch-Nucleus($handoff) {
    $nucleus = Get-NucleusFromHandoff $handoff.Name
    $upper = $nucleus.ToUpper()
    $pos = $gridPos[$nucleus]
    if (-not $pos) { $pos = @{x=0; y=0} }

    # Per-CLI boot script: claude -> n0X.ps1, gemini -> n0X_gemini.ps1, codex -> n0X_codex.ps1
    $bootPs1 = "$root\boot\${nucleus}${cliSuffix}.ps1"
    if (Test-Path $bootPs1) {
        $bootScript = $bootPs1
        $bootType = "ps1"
    } else {
        Write-Output "[$upper] SKIP: no boot script ($bootPs1)"
        return $null
    }

    Write-Output "[$upper] Boot via $cli ($bootType)"

    # Write per-nucleus + per-CLI handoff pointer so boot script picks it up
    $nucleusHandoff = "$handoffDir\${nucleus}_task${cliSuffix}.md"
    Copy-Item $handoff.FullName -Destination $nucleusHandoff -Force

    # Set env var so boot scripts skip their own WindowSize override
    $env:CEX_GRID = "1"
    $env:CEX_GRID_W = "$gW"
    $env:CEX_GRID_H = "$gH"

    # ALWAYS boot interactive -- task comes from handoff, never CLI args (avoids nested-quote hell)
    $proc = Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -File `"$bootScript`"" -WorkingDirectory $root -PassThru
    # Retry loop: poll for window handle (up to 5s, 500ms intervals)
    if ($proc) {
        $hwnd = [IntPtr]::Zero
        for ($i = 0; $i -lt 10; $i++) {
            Start-Sleep -Milliseconds 500
            try { $proc.Refresh() } catch {}
            $hwnd = $proc.MainWindowHandle
            if ($hwnd -ne [IntPtr]::Zero) { break }
        }
        if ($hwnd -ne [IntPtr]::Zero) {
            [Win32Grid]::MoveWindow($hwnd, $pos.x, $pos.y, $gW, $gH, $true) | Out-Null
        } else {
            Write-Output "[$upper] WARN: no window handle after 5s -- window not positioned"
        }
        # PID format: {pid} {nucleus} {cli} {session_id} {timestamp}
        $sessId = if ($env:CEX_SESSION_ID) { $env:CEX_SESSION_ID } else { "s$PID" }
        $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
        "$($proc.Id) $nucleus $cli $sessId $ts" | Add-Content $pidFile
        Write-Output "[$upper] Spawned PID:$($proc.Id) handoff:$($handoff.Name)"
    }
    return $proc
}

# Static mode: launch all at once
if ($mode -eq "static") {
    $launched = 0
    $launchedProcs = @{}
    foreach ($h in $handoffs) {
        if ($launched -ge $maxSlots) { break }
        $nucleus = Get-NucleusFromHandoff $h.Name
        $proc = Launch-Nucleus $h
        if ($proc) { $launchedProcs[$nucleus] = $proc }
        $launched++
        Start-Sleep -Seconds 4
    }
    # Re-enforce grid positions after all windows have settled
    # Boot scripts may resize windows; this second pass corrects them
    Write-Output "[GRID] Re-enforcing window positions..."
    Start-Sleep -Seconds 6
    foreach ($kv in $launchedProcs.GetEnumerator()) {
        $nucleus = $kv.Key
        $proc = $kv.Value
        $pos = $gridPos[$nucleus]
        if (-not $pos) { continue }
        try {
            $proc.Refresh()
            $hwnd = $proc.MainWindowHandle
            if ($hwnd -ne [IntPtr]::Zero) {
                [Win32Grid]::MoveWindow($hwnd, $pos.x, $pos.y, $gW, $gH, $true) | Out-Null
                Write-Output "  [$($nucleus.ToUpper())] repositioned"
            }
        } catch {}
    }
    Write-Output "[GRID] Static: $launched/$($handoffs.Count) launched"
    exit 0
}

# Continuous mode: launch slots, monitor, re-dispatch
$queue = [System.Collections.Queue]::new()
foreach ($h in $handoffs) { $queue.Enqueue($h) }

$active = @{}
$completed = 0
$startTime = Get-Date

# Initial fill
while ($active.Count -lt $maxSlots -and $queue.Count -gt 0) {
    $h = $queue.Dequeue()
    $nucleus = Get-NucleusFromHandoff $h.Name
    $proc = Launch-Nucleus $h
    if ($proc) { $active[$nucleus] = @{proc=$proc; handoff=$h; start=Get-Date} }
    Start-Sleep -Seconds 4
}

Write-Output "[GRID] Continuous: $($active.Count) active, $($queue.Count) queued"

# Monitor loop
while ($active.Count -gt 0 -or $queue.Count -gt 0) {
    $elapsed = ((Get-Date) - $startTime).TotalMinutes
    if ($elapsed -gt $maxMinutes) {
        Write-Output "[GRID] TIMEOUT: ${maxMinutes}min exceeded"
        break
    }

    Start-Sleep -Seconds $pollSeconds

    # Check for completed signals
    $toRemove = @()
    foreach ($kv in $active.GetEnumerator()) {
        $nucleus = $kv.Key
        $info = $kv.Value
        $spawnTime = $info.start

        $sigs = Get-ChildItem "$signalDir\signal_${nucleus}_*.json" -EA SilentlyContinue |
            Where-Object { $_.LastWriteTime -gt $spawnTime }

        if ($sigs) {
            $completed++
            Write-Output "[$($nucleus.ToUpper())] COMPLETE ($completed total)"
            $toRemove += $nucleus
        }

        # Stuck detection
        $age = ((Get-Date) - $spawnTime).TotalSeconds
        if ($age -gt 5400) {  # 90min stuck threshold (was 900s=15min)
            Write-Output "[$($nucleus.ToUpper())] STUCK (${age}s)"
            $toRemove += $nucleus
        }
    }

    foreach ($n in $toRemove) {
        $active.Remove($n)
        # Re-dispatch from queue
        if ($queue.Count -gt 0) {
            $h = $queue.Dequeue()
            $nucleus = Get-NucleusFromHandoff $h.Name
            $proc = Launch-Nucleus $h
            if ($proc) { $active[$nucleus] = @{proc=$proc; handoff=$h; start=Get-Date} }
            Start-Sleep -Seconds 4
        }
    }

    Write-Output "[GRID] Active:$($active.Count) Queue:$($queue.Count) Done:$completed Elapsed:$([math]::Round($elapsed))min"
}

Write-Output "[GRID] FINISHED: $completed completed, $($queue.Count) remaining"
