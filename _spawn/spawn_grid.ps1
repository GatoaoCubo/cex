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
    [ValidateSet('claude','gemini','codex','ollama','litellm','auto')]
    [string]$cli = "claude",
    [string]$Model = ""
)

# -Model overrides hardcoded model in boot/n0X.ps1 via CEX_CLAUDE_MODEL env.
# Used by grid-haiku to run Haiku instead of default Sonnet/Opus mix.
if ($Model) {
    $env:CEX_CLAUDE_MODEL = $Model
    Write-Output "[GRID] Model override active: CEX_CLAUDE_MODEL=$Model"
}

# Multi-CLI config (3 routing levels):
#   L1 explicit: -cli claude|gemini|codex -- operator override, global for this grid
#   L2 auto:     -cli auto -- resolver picks per-nucleus from nucleus_models.yaml
#                              (primary + fallback_chain, binary pre-check)
#   L3 router:   cex_router.py (not used here; used by cex_mission_runner.py)
#
# Per-CLI boot + handoff suffix mapping:
#   claude -> boot/n0X.ps1        + handoff copy .cex/runtime/handoffs/n0X_task.md
#   gemini -> boot/n0X_gemini.ps1 + handoff copy .cex/runtime/handoffs/n0X_task_gemini.md
#   codex  -> boot/n0X_codex.ps1  + handoff copy .cex/runtime/handoffs/n0X_task_codex.md
$globalCli = $cli
$cliSuffix = if ($cli -eq "claude") { "" }
             elseif ($cli -eq "auto") { "" }  # placeholder; real suffix resolved per-nucleus
             else { "_$cli" }

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

# Walk process tree recursively from a parent PID, return all descendant PIDs
# Fix for "wrapper PID pitfall" -- Start-Process -PassThru returns the wrapper
# powershell.exe PID, NOT the actual worker (claude.exe/codex.exe/node.exe).
# We need the grandchildren/great-grandchildren to track real liveness.
function Get-DescendantPids($parentId) {
    $allProcs = Get-CimInstance Win32_Process -EA SilentlyContinue
    $result = @()
    $queue = [System.Collections.Queue]::new()
    $queue.Enqueue($parentId)
    while ($queue.Count -gt 0) {
        $current = $queue.Dequeue()
        $kids = $allProcs | Where-Object { $_.ParentProcessId -eq $current }
        foreach ($k in $kids) {
            $result += [PSCustomObject]@{
                Id = [int]$k.ProcessId
                Name = ($k.Name -replace '\.exe$','').ToLower()
                Parent = [int]$current
            }
            $queue.Enqueue([int]$k.ProcessId)
        }
    }
    return $result
}

# Resolve CLI for a nucleus via YAML fallback chain + binary pre-check.
# Called when $globalCli -eq "auto". Returns hashtable @{cli=..; model=..; flags=..; chain_step=..}
# or $null if no working CLI in the chain.
function Resolve-NucleusCli($nucleus) {
    $resolverScript = "$root\_tools\cex_cli_resolver.py"
    if (-not (Test-Path $resolverScript)) {
        Write-Output "  [WARN] resolver missing, falling back to claude: $resolverScript"
        return @{cli="claude"; chain_step="default"}
    }
    try {
        $raw = & python $resolverScript --nucleus $nucleus --pre-check --json 2>&1
        $json = $raw -join "`n" | ConvertFrom-Json
        if ($json.error) {
            Write-Output "  [WARN] resolver error for ${nucleus}: $($json.error)"
            return $null
        }
        return @{
            cli = $json.cli
            model = $json.model
            flags = $json.flags
            chain_step = $json.chain_step
        }
    } catch {
        Write-Output "  [WARN] resolver failed for ${nucleus}: $_"
        return @{cli="claude"; chain_step="default"}
    }
}

# Find worker PIDs (claude/codex/gemini/node) that are descendants of a wrapper.
# Returns comma-separated PID list, "-" if none found.
function Find-WorkerPids($wrapperPid, $cli) {
    $targetNames = switch ($cli) {
        "claude"  { @("claude","node") }
        "gemini"  { @("gemini","node") }
        "codex"   { @("codex") }
        "ollama"  { @("python") }
        "litellm" { @("python") }
        default   { @("claude","codex","gemini","node","python") }
    }
    $descendants = Get-DescendantPids $wrapperPid
    $workers = $descendants | Where-Object { $targetNames -contains $_.Name }
    if ($workers.Count -eq 0) { return "-" }
    return ($workers | ForEach-Object { $_.Id }) -join ","
}

# Launch a single nucleus with handoff
function Launch-Nucleus($handoff) {
    $nucleus = Get-NucleusFromHandoff $handoff.Name
    $upper = $nucleus.ToUpper()
    $pos = $gridPos[$nucleus]
    if (-not $pos) { $pos = @{x=0; y=0} }

    # Resolve CLI: explicit (L1) or auto from YAML fallback_chain (L2)
    $effectiveCli = $globalCli
    $chainStep = "explicit"
    if ($globalCli -eq "auto") {
        $resolved = Resolve-NucleusCli $nucleus
        if (-not $resolved) {
            Write-Output "[$upper] SKIP: no working CLI in fallback chain"
            return $null
        }
        $effectiveCli = $resolved.cli
        $chainStep = $resolved.chain_step
    }
    $effectiveSuffix = if ($effectiveCli -eq "claude") { "" } else { "_$effectiveCli" }

    # Per-CLI boot script: claude -> n0X.ps1, gemini -> n0X_gemini.ps1, codex -> n0X_codex.ps1
    $bootPs1 = "$root\boot\${nucleus}${effectiveSuffix}.ps1"
    if (-not (Test-Path $bootPs1)) {
        # Auto fallback: if resolved CLI lacks a boot script, try claude
        if ($globalCli -eq "auto" -and $effectiveCli -ne "claude") {
            Write-Output "[$upper] WARN: no boot script for $effectiveCli ($bootPs1), falling back to claude"
            $effectiveCli = "claude"
            $effectiveSuffix = ""
            $chainStep = "boot_fallback"
            $bootPs1 = "$root\boot\${nucleus}.ps1"
        }
        if (-not (Test-Path $bootPs1)) {
            Write-Output "[$upper] SKIP: no boot script ($bootPs1)"
            return $null
        }
    }
    $bootScript = $bootPs1
    $bootType = "ps1"

    Write-Output "[$upper] Boot via $effectiveCli ($chainStep)"

    # Write per-nucleus + per-CLI handoff pointer so boot script picks it up
    $nucleusHandoff = "$handoffDir\${nucleus}_task${effectiveSuffix}.md"
    Copy-Item $handoff.FullName -Destination $nucleusHandoff -Force

    # Set env var so boot scripts skip their own WindowSize override
    $env:CEX_GRID = "1"
    $env:CEX_GRID_W = "$gW"
    $env:CEX_GRID_H = "$gH"

    # ALWAYS boot interactive -- task comes from handoff, never CLI args (avoids nested-quote hell)
    # Capture wrapper stdout+stderr to log file for post-mortem diagnostics (race conditions, crashes)
    $logDir = "$root\.cex\runtime\logs\spawn"
    if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir -Force | Out-Null }
    $logFile = "$logDir\${nucleus}_$(Get-Date -Format 'yyyyMMdd_HHmmss').log"
    # Interactive mode => visible window (NO stdout redirect, Windows hides window when redirecting).
    # Non-interactive (headless) => capture stdout/stderr for post-mortem; window hidden.
    if ($interactive) {
        $proc = Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -NoExit -File `"$bootScript`"" -WorkingDirectory $root -PassThru -WindowStyle Normal
    } else {
        $proc = Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -NoExit -File `"$bootScript`"" -WorkingDirectory $root -PassThru -RedirectStandardOutput $logFile -RedirectStandardError "${logFile}.err"
    }
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
            # bRepaint=$true: TUI needs WM_SIZE to adapt alt-screen-buffer to
            # final window dimensions. Without repaint, Claude renders at
            # initial (smaller) window size and leaves bottom/side dead zones.
            # Previous "overlap" was caused by banner+DarkBlue bg in boot scripts
            # (fixed by cex_fix_boot_banner.py), not by forced repaint itself.
            [Win32Grid]::MoveWindow($hwnd, $pos.x, $pos.y, $gW, $gH, $true) | Out-Null
        } else {
            Write-Output "[$upper] WARN: no window handle after 5s -- window not positioned"
        }
        # PID format: {wrapper_pid} {nucleus} {cli} {session_id} {timestamp} {worker_pids}
        # worker_pids is filled by Enrich-PidFile after all launches (empty = "-" here)
        # cli = effectiveCli (per-nucleus resolved, not the global -cli flag)
        $sessId = if ($env:CEX_SESSION_ID) { $env:CEX_SESSION_ID } else { "s$PID" }
        $ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
        "$($proc.Id) $nucleus $effectiveCli $sessId $ts -" | Add-Content $pidFile
        Write-Output "[$upper] Spawned wrapper PID:$($proc.Id) handoff:$($handoff.Name)"
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
    # NOTE: Re-enforce reposition removed (2026-04-14). Previously this ran 6s
    # after launch, yanking windows mid-TUI-render. Claude TUI boots in 2-3s and
    # the WM_SIZE event from MoveWindow triggered full repaint glitches (alt
    # screen buffer desync). First MoveWindow (at launch time) is final.
    # Enrich PID file: walk descendants to capture real worker PIDs
    # (Start-Process -PassThru returned the wrapper, not the worker.)
    Write-Output "[GRID] Enriching PID file with worker PIDs..."
    Start-Sleep -Seconds 4  # let CLI workers actually start
    if (Test-Path $pidFile) {
        $lines = Get-Content $pidFile
        $newLines = @()
        foreach ($line in $lines) {
            $parts = $line.Trim() -split '\s+'
            if ($parts.Count -lt 5) { $newLines += $line; continue }
            $wPid = [int]$parts[0]; $nuc = $parts[1]; $c = $parts[2]
            $sess = $parts[3]; $t = $parts[4]
            $workerList = Find-WorkerPids $wPid $c
            $newLines += "$wPid $nuc $c $sess $t $workerList"
            Write-Output "  [$($nuc.ToUpper())] wrapper:$wPid workers:$workerList"
        }
        Set-Content $pidFile $newLines -Encoding UTF8
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
