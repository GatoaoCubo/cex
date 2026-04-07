# CEX Spawn Stop v4.0 -- Session-aware process termination
# 
# CRITICAL: Only kills processes from YOUR session by default.
# The other N07 sessions are NOT touched unless -All is specified.
#
# Usage:
#   powershell -File _spawn/spawn_stop.ps1                  # kill MY session nuclei
#   powershell -File _spawn/spawn_stop.ps1 -Nucleus n03     # kill only N03
#   powershell -File _spawn/spawn_stop.ps1 -All             # kill ALL CEX nuclei
#   powershell -File _spawn/spawn_stop.ps1 -DryRun          # preview without killing
#   powershell -File _spawn/spawn_stop.ps1 -Session s13020  # kill specific session

param(
    [switch]$DryRun,
    [switch]$Quiet,
    [switch]$All,
    [string]$Nucleus = "",
    [string]$Session = ""
)

$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"
$stopped = 0
$killedPids = [System.Collections.ArrayList]@()

function Log($msg) {
    if (-not $Quiet) { Write-Output $msg }
}

function Kill-Tree {
    param([int]$TargetPid, [string]$Tag)
    # Kill all children first (claude.exe, node.exe, etc), then the parent (cmd.exe)
    $kids = Get-CimInstance Win32_Process -EA SilentlyContinue |
        Where-Object { $PSItem.ParentProcessId -eq $TargetPid }
    foreach ($k in $kids) { Kill-Tree -TargetPid $k.ProcessId -Tag "$Tag>$($k.Name)" }
    $p = Get-Process -Id $TargetPid -EA SilentlyContinue
    if ($p) {
        if ($DryRun) { Log "  (DRY) Would kill PID:$TargetPid $($p.ProcessName) $Tag" }
        else {
            # taskkill /F /T = force + tree-kill (kills all child processes)
            # Stop-Process does NOT tree-kill -- orphans claude.exe + node.exe
            $tkResult = taskkill /F /PID $TargetPid /T 2>&1
            Log "  Killed PID:$TargetPid $($p.ProcessName) $Tag (tree-kill)"
        }
        $script:stopped++
        [void]$script:killedPids.Add($TargetPid)
    }
}

# Determine MY session ID (same logic as spawn_solo)
$mySession = $env:CEX_SESSION_ID
if (-not $mySession) {
    $parentPid = (Get-CimInstance Win32_Process -Filter "ProcessId=$PID" -EA SilentlyContinue).ParentProcessId
    $mySession = "s$parentPid"
}

# Determine which session to target
$targetSession = ""
if ($Session) {
    $targetSession = $Session
} elseif (-not $All) {
    $targetSession = $mySession
}

Log "=== CEX Spawn Stop v4.0 (session-aware) ==="
if ($All) {
    Log "  MODE: ALL -- killing every CEX nucleus process"
} elseif ($Nucleus) {
    Log "  MODE: Single nucleus $($Nucleus.ToUpper())"
} else {
    Log "  MODE: Session $targetSession only (use -All to kill everything)"
}
Log ""

# --- STEP 1: Kill by PID file (session-filtered) ---
Log "  STEP 1: PID file entries"
$remainingLines = @()
if (Test-Path $pidFile) {
    foreach ($line in (Get-Content $pidFile)) {
        $parts = $line.Trim().Split(' ')
        if ($parts.Count -lt 2) { continue }
        
        $cmdPid = [int]$parts[0]
        $nuc = $parts[1]
        $cli = if ($parts.Count -ge 3) { $parts[2] } else { "?" }
        $sess = if ($parts.Count -ge 4) { $parts[3] } else { "unknown" }
        $ts = if ($parts.Count -ge 5) { $parts[4] } else { "" }
        $upper = $nuc.ToUpper()
        
        # Filter: should we kill this entry?
        $shouldKill = $false
        if ($All) {
            $shouldKill = $true
        } elseif ($Nucleus -and $nuc -eq $Nucleus.ToLower()) {
            $shouldKill = $true
        } elseif ($targetSession -and $sess -eq $targetSession) {
            $shouldKill = $true
        }
        
        if ($shouldKill) {
            $alive = Get-Process -Id $cmdPid -EA SilentlyContinue
            if ($alive) {
                Log "    $upper : Kill CMD PID:$cmdPid + children (session:$sess)"
                Kill-Tree -TargetPid $cmdPid -Tag $upper
            } else {
                Log "    $upper : PID:$cmdPid already dead (session:$sess)"
            }
        } else {
            # Keep this line in the PID file (belongs to another session)
            $remainingLines += $line
            Log "    $upper : SKIP PID:$cmdPid (session:$sess != target)"
        }
    }
    
    # Rewrite PID file with only surviving entries
    if (-not $DryRun) {
        if ($remainingLines.Count -gt 0) {
            $remainingLines | Set-Content $pidFile -Encoding UTF8
        } else {
            Set-Content $pidFile "" -Encoding UTF8
        }
    }
} else {
    Log "    No PID file"
}

# --- STEP 2: Window title scan (only if -All) ---
Log ""
Log "  STEP 2: Window title scan"
if ($All) {
    # Nuclei can run in CMD (.cmd boot) or PowerShell (.ps1 boot)
    $wins = @(Get-Process cmd, powershell -EA SilentlyContinue |
        Where-Object { $PSItem.MainWindowTitle -match 'CEX-N0[1-7]|N0[1-6]\s' })
    foreach ($w in $wins) {
        if ($w.Id -notin $killedPids) {
            Log "    Found '$($w.MainWindowTitle)' PID:$($w.Id)"
            Kill-Tree -TargetPid $w.Id -Tag "title"
        }
    }
    if ($wins.Count -eq 0) { Log "    No CEX windows found" }
} else {
    Log "    SKIPPED (only with -All flag)"
}

# --- STEP 3: Orphan scan (ONLY if -All, NEVER by default) ---
Log ""
Log "  STEP 3: Orphan CLI scan"
if ($All) {
    $found = $false
    
    foreach ($p in @(Get-Process "claude" -EA SilentlyContinue | Where-Object { $PSItem.Id -notin $killedPids })) {
        $cimProc = Get-CimInstance Win32_Process -Filter "ProcessId=$($p.Id)" -EA SilentlyContinue
        $parentPid = $cimProc.ParentProcessId
        $parentAlive = Get-Process -Id $parentPid -EA SilentlyContinue
        if ($parentAlive -and $parentAlive.ProcessName -eq "cmd") {
            Log "    ORPHAN claude PID:$($p.Id) parent CMD:$parentPid -- killing tree"
            Kill-Tree -TargetPid $parentPid -Tag "orphan"
        } else {
            Log "    ORPHAN claude PID:$($p.Id) no parent CMD -- killing directly"
            if (-not $DryRun) { taskkill /F /PID $($p.Id) /T 2>&1 | Out-Null }
            $script:stopped++
        }
        $found = $true
    }
    
    foreach ($p in @(Get-Process "codex" -EA SilentlyContinue | Where-Object { $PSItem.Id -notin $killedPids })) {
        Log "    ORPHAN codex PID:$($p.Id)"
        if (-not $DryRun) { taskkill /F /PID $($p.Id) /T 2>&1 | Out-Null }
        $script:stopped++; $found = $true
    }
    
    if (-not $found) { Log "    No orphans" }
} else {
    Log "    SKIPPED (only with -All -- DANGEROUS: kills ALL claude processes)"
}

# --- SUMMARY ---
Log ""
if ($DryRun) { Log "  RESULT: DRY-RUN would have killed $stopped processes" }
else          { Log "  RESULT: $stopped processes terminated" }

$statusFile = "$root\.cex\runtime\grid_status.json"
@{
    action    = "stop"
    stopped   = $stopped
    dry_run   = $DryRun.IsPresent
    session   = if ($All) { "ALL" } else { $targetSession }
    timestamp = (Get-Date -Format o)
} | ConvertTo-Json | Set-Content $statusFile -Encoding UTF8
