# CEX Flywheel Stop v1.0
# Kills all flywheel worker processes
#
# Usage: powershell -File _tools/cex_flywheel_stop.ps1

$root = $PSScriptRoot | Split-Path -Parent
$signalDir = "$root\.cex_signals"

Write-Host "Stopping CEX Flywheel..." -ForegroundColor Yellow

# Kill python processes running flywheel_worker
$killed = 0
Get-Process python* -EA SilentlyContinue | ForEach-Object {
    try {
        $cmdline = (Get-CimInstance Win32_Process -Filter "ProcessId = $($_.Id)" -EA SilentlyContinue).CommandLine
        if ($cmdline -match "flywheel_worker") {
            $_.Kill()
            $killed++
            Write-Host "  Killed PID $($_.Id)" -ForegroundColor Red
        }
    } catch {}
}

if ($killed -eq 0) {
    Write-Host "  No active flywheel workers found" -ForegroundColor Green
} else {
    Write-Host "  Killed $killed workers" -ForegroundColor Yellow
}

# Archive signals
$archiveDir = "$signalDir\archive"
New-Item -ItemType Directory -Path $archiveDir -Force -EA SilentlyContinue | Out-Null
$moved = (Get-ChildItem "$signalDir\*.json" -EA SilentlyContinue | 
    Move-Item -Destination $archiveDir -Force -PassThru -EA SilentlyContinue).Count
Write-Host "  Archived $moved signal files" -ForegroundColor DarkGray
