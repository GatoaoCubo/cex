# CEX Spawn Monitor v1.0
$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\temp\spawn_pids.txt"
$signalDir = "$root\.cex_signals"

if (-not (Test-Path $pidFile)) { Write-Output "No active spawns."; exit 0 }

$lines = Get-Content $pidFile
$spawnTime = (Get-Item $pidFile).LastWriteTime

Write-Output ""
Write-Output "  NUCLEUS   STATUS     QUALITY  TIME"
Write-Output "  --------- ---------- -------  ----"

foreach ($line in $lines) {
    $parts = $line.Trim().Split(' ')
    if ($parts.Count -lt 2) { continue }
    $procId = [int]$parts[0]
    $nucleus = $parts[1]
    $upper = $nucleus.ToUpper()

    $hasSignal = $false; $quality = '  -'; $status = 'RUNNING'

    $sigs = Get-ChildItem "$signalDir\signal_${nucleus}_*.json" -EA SilentlyContinue |
        Where-Object { $_.LastWriteTime -gt $spawnTime }
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

    $age = [math]::Round(((Get-Date) - $spawnTime).TotalMinutes)
    Write-Output "  $($upper.PadRight(9)) $($status.PadRight(10)) $($quality.ToString().PadRight(7))  ${age}min"
}
