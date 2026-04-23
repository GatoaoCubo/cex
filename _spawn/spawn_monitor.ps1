# CEX Spawn Monitor v1.1 -- auto-prunes dead PIDs older than 30min
$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"
$signalDir = "$root\.cex\runtime\signals"

if (-not (Test-Path $pidFile)) { Write-Output "No active spawns."; exit 0 }

$lines = Get-Content $pidFile
$fileMTime = (Get-Item $pidFile).LastWriteTime

Write-Output ""
Write-Output "  NUCLEUS   STATUS     QUALITY  TIME"
Write-Output "  --------- ---------- -------  ----"

$survivors = @()  # lines to keep (alive OR recent)
$pruned = 0

foreach ($line in $lines) {
    $parts = $line.Trim().Split(' ')
    if ($parts.Count -lt 2) { continue }
    $procId = [int]$parts[0]
    $nucleus = $parts[1]
    $upper = $nucleus.ToUpper()

    # Per-process spawn time from PID entry (parts[4]), fall back to file mtime
    $procSpawn = $fileMTime
    if ($parts.Count -ge 5) {
        try { $procSpawn = [datetime]::Parse($parts[4] -replace '_', ' ') } catch { }
    }

    $quality = '  -'; $status = 'RUNNING'

    $sigs = Get-ChildItem "$signalDir\signal_${nucleus}_*.json" -EA SilentlyContinue |
        Where-Object { $_.LastWriteTime -gt $procSpawn }
    if ($sigs) {
        $latest = $sigs | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        try {
            $data = Get-Content $latest.FullName -Raw | ConvertFrom-Json
            $status = $data.status.ToUpper()
            $quality = $data.quality_score
        } catch { $status = 'SIGNAL_ERR' }
    }

    $alive = Get-Process -Id $procId -EA SilentlyContinue
    if (-not $alive -and $status -eq 'RUNNING') { $status = 'CRASHED' }

    $age = [math]::Round(((Get-Date) - $procSpawn).TotalMinutes)

    # Prune: dead PID AND age > 30min = drop from file (stale cruft)
    if (-not $alive -and $age -gt 30) {
        $pruned += 1
        continue  # don't print, don't keep
    }

    Write-Output "  $($upper.PadRight(9)) $($status.PadRight(10)) $($quality.ToString().PadRight(7))  ${age}min"
    $survivors += $line
}

# Rewrite pid file if we pruned anything
if ($pruned -gt 0) {
    if ($survivors.Count -gt 0) {
        $survivors | Set-Content $pidFile -Encoding UTF8
    } else {
        Remove-Item $pidFile -Force
    }
    Write-Output ""
    Write-Output "  [PRUNED $pruned stale entries (dead PID, age > 30min)]"
}
