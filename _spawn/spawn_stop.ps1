param(
    [switch]$DryRun,
    [switch]$Quiet
)

$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"
$stopped = 0
$killedPids = [System.Collections.ArrayList]@()

function Log($msg) {
    if (-not $Quiet) { Write-Output $msg }
}

function Kill-Tree([int]$TargetPid, [string]$Tag) {
    $kids = Get-CimInstance Win32_Process -EA SilentlyContinue |
        Where-Object { $PSItem.ParentProcessId -eq $TargetPid }
    foreach ($k in $kids) { Kill-Tree $k.ProcessId "$Tag>$($k.Name)" }
    $p = Get-Process -Id $TargetPid -EA SilentlyContinue
    if ($p) {
        if ($DryRun) { Log "  [DRY] Would kill PID:$TargetPid $($p.ProcessName) $Tag" }
        else         { Stop-Process -Id $TargetPid -Force -EA SilentlyContinue; Log "  Killed PID:$TargetPid $($p.ProcessName) $Tag" }
        $script:stopped++
        [void]$script:killedPids.Add($TargetPid)
    }
}

Log "=== CEX Spawn Stop v3.0 ==="
Log ""

# --- STEP 1: Kill by PID file ---
Log "[STEP 1] PID file"
if (Test-Path $pidFile) {
    foreach ($line in (Get-Content $pidFile)) {
        $parts = $line.Trim().Split(' ')
        if ($parts.Count -lt 2) { continue }
        $id = [int]$parts[0]; $nuc = $parts[1].ToUpper()
        $alive = Get-Process -Id $id -EA SilentlyContinue
        if ($alive) { Log "  [$nuc] killing CMD PID:$id + children"; Kill-Tree $id $nuc }
        else        { Log "  [$nuc] PID:$id already dead" }
    }
    if (-not $DryRun) { Set-Content $pidFile "" -Encoding UTF8 }
}
else { Log "  No PID file" }

# --- STEP 2: Kill by window title (catches relaunched / untracked) ---
Log ""
Log "[STEP 2] Window titles"
$wins = @(Get-Process cmd -EA SilentlyContinue |
    Where-Object { $PSItem.MainWindowTitle -match 'CEX-N0[1-7]' })
foreach ($w in $wins) {
    if ($w.Id -notin $killedPids) {
        Log "  Found '$($w.MainWindowTitle)' PID:$($w.Id)"; Kill-Tree $w.Id "title"
    }
}
if ($wins.Count -eq 0) { Log "  No CEX windows found" }

# --- STEP 3: Orphan CLI processes ---
Log ""
Log "[STEP 3] Orphan scan"
$found = $false

foreach ($p in @(Get-Process "claude" -EA SilentlyContinue | Where-Object { $PSItem.Id -notin $killedPids })) {
    Log "  [ORPHAN] claude.exe PID:$($p.Id)"
    if (-not $DryRun) { Stop-Process -Id $p.Id -Force -EA SilentlyContinue }
    $script:stopped++; $found = $true
}

foreach ($p in @(Get-Process "codex" -EA SilentlyContinue | Where-Object { $PSItem.Id -notin $killedPids })) {
    Log "  [ORPHAN] codex.exe PID:$($p.Id)"
    if (-not $DryRun) { Stop-Process -Id $p.Id -Force -EA SilentlyContinue }
    $script:stopped++; $found = $true
}

$geminiNodes = @(Get-CimInstance Win32_Process -EA SilentlyContinue |
    Where-Object { $PSItem.Name -eq "node.exe" -and $PSItem.CommandLine -match "gemini" -and $PSItem.ProcessId -notin $killedPids })
foreach ($p in $geminiNodes) {
    Log "  [ORPHAN] node.exe (gemini) PID:$($p.ProcessId)"
    if (-not $DryRun) { Stop-Process -Id $p.ProcessId -Force -EA SilentlyContinue }
    $script:stopped++; $found = $true
}

if (-not $found) { Log "  No orphans" }

# --- SUMMARY ---
Log ""
if ($DryRun) { Log "[STOP] DRY-RUN: would have killed $stopped processes" }
else          { Log "[STOP] $stopped processes terminated" }

$statusFile = "$root\.cex\runtime\grid_status.json"
@{ action="stop"; stopped=$stopped; dry_run=$DryRun.IsPresent; timestamp=(Get-Date -Format o) } |
    ConvertTo-Json | Set-Content $statusFile -Encoding UTF8
