# CEX Spawn Stop v2.0 — Multi-CLI: claude + codex + gemini
$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"
$stopped = 0

# Step 1: Kill CMDs by PID
if (Test-Path $pidFile) {
    $lines = Get-Content $pidFile
    foreach ($line in $lines) {
        $parts = $line.Trim().Split(' ')
        if ($parts.Count -ge 2) {
            $procId = [int]$parts[0]
            $nucleus = $parts[1].ToUpper()
            $cli = if ($parts.Count -ge 3) { $parts[2] } else { 'claude' }
            Stop-Process -Id $procId -Force -EA SilentlyContinue
            Write-Output "[$nucleus] CMD PID:$procId ($cli) stopped"
            $stopped++
        }
    }
    Remove-Item $pidFile -Force -EA SilentlyContinue
} else {
    Write-Output "[INFO] No spawn_pids.txt found"
}

# Step 2: Kill orphan processes (all 3 CLIs)
foreach ($procName in @('claude','codex','gemini')) {
    $procs = Get-Process $procName -EA SilentlyContinue
    foreach ($p in $procs) {
        Stop-Process -Id $p.Id -Force -EA SilentlyContinue
        Write-Output "[ORPHAN] $procName.exe PID:$($p.Id) killed"
        $stopped++
    }
}

Write-Output "[STOP] $stopped processes terminated."
