# CEX Spawn Stop v1.0
$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\temp\spawn_pids.txt"

if (Test-Path $pidFile) {
    $lines = Get-Content $pidFile
    foreach ($line in $lines) {
        $parts = $line.Trim().Split(' ')
        if ($parts.Count -ge 2) {
            Stop-Process -Id ([int]$parts[0]) -Force -EA SilentlyContinue
            Write-Output "[$($parts[1].ToUpper())] Stopped PID:$($parts[0])"
        }
    }
    Remove-Item $pidFile -Force
}

# Kill orphan claude.exe
$claudes = Get-Process claude -EA SilentlyContinue
foreach ($c in $claudes) {
    Stop-Process -Id $c.Id -Force -EA SilentlyContinue
    Write-Output "[ORPHAN] claude.exe PID:$($c.Id) killed"
}

Write-Output "[STOP] All spawns terminated."
