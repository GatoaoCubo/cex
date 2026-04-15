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
# IMPORTANT: When -Nucleus is specified, do NOT auto-scope to session.
# "-Nucleus n03" means "kill n03 everywhere" (or in -Session if given).
$targetSession = ""
if ($Session) {
    $targetSession = $Session
} elseif (-not $All -and -not $Nucleus) {
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
        # FIX(G15): -Nucleus must NOT trigger session-wide kill.
        # When -Nucleus is set, ONLY nucleus match fires.
        $shouldKill = $false
        if ($All) {
            $shouldKill = $true
        } elseif ($Nucleus -and $nuc -eq $Nucleus.ToLower()) {
            # Nucleus-specific: respect -Session if given, else kill across all sessions
            if ($targetSession) {
                $shouldKill = ($sess -eq $targetSession)
            } else {
                $shouldKill = $true
            }
        } elseif (-not $Nucleus -and $targetSession -and $sess -eq $targetSession) {
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

# --- STEP 2: CommandLine scan (MORE RELIABLE than MainWindowTitle) ---
# MainWindowTitle can be truncated or stale (prompt-theme title).
# Win32_Process.CommandLine is the immutable launch command -- source of truth.
# Runs on MY session by default, -All to scan every session.
Log ""
Log "  STEP 2: CommandLine scan (boot/n0X_*.ps1 wrappers)"
$cimAll = Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" -EA SilentlyContinue
$bootWrappers = @($cimAll | Where-Object {
    $PSItem.CommandLine -match 'boot[/\\]n0[1-7](_gemini|_codex|_ollama|_litellm)?\.ps1' -and
    $PSItem.ProcessId -notin $killedPids -and
    $PSItem.ProcessId -ne $PID
})
$wrappedBySession = @{}
if (-not $All -and $targetSession) {
    # Only kill wrappers whose pid matches our session's pid file entries
    $sessionPids = @()
    if (Test-Path $pidFile) {
        foreach ($line in (Get-Content $pidFile)) {
            $parts = $line.Trim().Split(' ')
            if ($parts.Count -ge 4 -and $parts[3] -eq $targetSession) {
                $sessionPids += [int]$parts[0]
            }
        }
    }
    # ALSO: if pid file is incomplete (showoff case), fall back to ALL boot wrappers
    # since they will have been created by the current N07 orchestration.
    # Session protection means we check if they're children of claude.exe from another session.
}
foreach ($w in $bootWrappers) {
    $match = $Matches[0]
    if ($All) {
        Log "    CMDLINE: PID:$($w.ProcessId) $match"
        Kill-Tree -TargetPid $w.ProcessId -Tag "cmdline"
    } elseif ($targetSession) {
        # Only kill if this wrapper is in MY session's pid file, OR orphan (no pid file entry)
        $inSession = $sessionPids -contains $w.ProcessId
        $tracked = $false
        if (Test-Path $pidFile) {
            foreach ($line in (Get-Content $pidFile)) {
                if (($line.Trim().Split(' '))[0] -eq "$($w.ProcessId)") { $tracked = $true; break }
            }
        }
        if ($inSession -or -not $tracked) {
            Log "    CMDLINE: PID:$($w.ProcessId) (in-session:$inSession tracked:$tracked)"
            Kill-Tree -TargetPid $w.ProcessId -Tag "cmdline-session"
        } else {
            Log "    CMDLINE: SKIP PID:$($w.ProcessId) (other session)"
        }
    }
}
if ($bootWrappers.Count -eq 0) { Log "    No boot wrappers found" }

# --- STEP 2b: Orphan node.exe cleanup (gemini children) ---
# Gemini CLI runs as node.exe -- no gemini.exe. When wrapper dies without
# tree-killing, node.exe lingers. Kill any node whose parent is dead AND
# whose CommandLine references gemini/codex npm packages.
Log ""
Log "  STEP 2b: Orphan node.exe (gemini/codex CLI workers)"
$orphanNodes = @(Get-CimInstance Win32_Process -Filter "Name='node.exe'" -EA SilentlyContinue |
    Where-Object {
        $parentAlive = Get-Process -Id $PSItem.ParentProcessId -EA SilentlyContinue
        -not $parentAlive -and
        ($PSItem.CommandLine -match 'gemini|codex|@google|@openai' -or $PSItem.CommandLine -eq $null)
    })
foreach ($n in $orphanNodes) {
    if ($n.ProcessId -notin $killedPids) {
        Log "    ORPHAN node PID:$($n.ProcessId) parent-dead"
        Kill-Tree -TargetPid $n.ProcessId -Tag "orphan-node"
    }
}
if ($orphanNodes.Count -eq 0) { Log "    No orphan node processes" }

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
            Log "    ORPHAN cli PID:$($p.Id) parent CMD:$parentPid -- killing tree"
            Kill-Tree -TargetPid $parentPid -Tag "orphan"
        } else {
            Log "    ORPHAN cli PID:$($p.Id) no parent CMD -- killing directly"
            Kill-Tree -TargetPid $p.Id -Tag "orphan-direct"
        }
        $found = $true
    }
    
    foreach ($p in @(Get-Process "codex" -EA SilentlyContinue | Where-Object { $PSItem.Id -notin $killedPids })) {
        Log "    ORPHAN codex PID:$($p.Id)"
        Kill-Tree -TargetPid $p.Id -Tag "orphan-codex"
        $found = $true
    }
    
    if (-not $found) { Log "    No orphans" }
} else {
    Log "    SKIPPED (only with -All -- DANGEROUS: kills ALL claude+pi processes)"
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
