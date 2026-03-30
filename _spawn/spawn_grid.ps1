# CEX Spawn Grid v1.0 — Launch multiple nucleus builders
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
    [int]$maxSlots = 6
)

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Grid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

$root = Split-Path $PSScriptRoot -Parent
$handoffDir = "$root\.cexuntime\handoffs"
$signalDir = "$root\.cexuntime\signals"
$pidFile = "$root\.cex\temp\spawn_pids.txt"

New-Item -ItemType Directory -Force -Path $handoffDir,$signalDir,"$root\.cex\temp" | Out-Null

$gridPos = @{
    n01 = @{x=0;    y=0};    n02 = @{x=640;  y=0}
    n03 = @{x=1280; y=0};    n04 = @{x=0;    y=520}
    n05 = @{x=640;  y=520};  n06 = @{x=1280; y=520}
}

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
Write-Output "[GRID] Mission: $mission | Mode: $mode | Handoffs: $($handoffs.Count)"

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

    $bootScript = "$root\boot\$nucleus.cmd"
    if (-not (Test-Path $bootScript)) {
        Write-Output "[$upper] SKIP: no boot script"
        return $null
    }

    $identity = "Voce e $upper Builder. Leia .cex/runtime/handoffs/$($handoff.Name). Execute todas as tarefas. Commit e signal ao terminar."

    $proc = Start-Process cmd -ArgumentList "/k `"$bootScript`" `"$identity`"" -WorkingDirectory $root -PassThru
    Start-Sleep -Seconds 3

    if ($proc) {
        [Win32Grid]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, 640, 520, $true) | Out-Null
        "$($proc.Id) $nucleus" | Add-Content $pidFile
        Write-Output "[$upper] Spawned PID:$($proc.Id) handoff:$($handoff.Name)"
    }
    return $proc
}

# Static mode: launch all at once
if ($mode -eq "static") {
    $launched = 0
    foreach ($h in $handoffs) {
        if ($launched -ge $maxSlots) { break }
        Launch-Nucleus $h | Out-Null
        $launched++
        Start-Sleep -Seconds 4
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
        if ($age -gt 900) {
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
