# CEX Flywheel Monitor v1.0
# Lightweight status checker -- run in separate terminal
#
# Usage:
#   powershell -File _tools/cex_flywheel_monitor.ps1
#   powershell -File _tools/cex_flywheel_monitor.ps1 -watch -interval 60

param(
    [switch]$watch,
    [int]$interval = 30
)

$root = $PSScriptRoot | Split-Path -Parent
$signalDir = "$root\.cex_signals"

function Show-Status {
    Clear-Host
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host "  CEX FLYWHEEL MONITOR -- $ts" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""

    # Read all signals
    $signals = Get-ChildItem "$signalDir\N*_cycle*_*.json" -EA SilentlyContinue | Sort-Object Name

    if (-not $signals) {
        Write-Host "  No signals found. Flywheel not running?" -ForegroundColor Yellow
        return
    }

    # Group by cycle
    $byCycle = @{}
    foreach ($sig in $signals) {
        $content = Get-Content $sig.FullName -Raw -EA SilentlyContinue | ConvertFrom-Json
        if ($content) {
            $cycle = $content.cycle
            if (-not $byCycle.ContainsKey($cycle)) { $byCycle[$cycle] = @() }
            $byCycle[$cycle] += $content
        }
    }

    # Display
    $NUCLEI = @("N01", "N02", "N03", "N04", "N05", "N06", "N07")
    $DOMAINS = @{
        N01="Research"; N02="Marketing"; N03="Engineering"; N04="Knowledge";
        N05="Operations"; N06="Commercial"; N07="Admin"
    }

    foreach ($cycle in ($byCycle.Keys | Sort-Object)) {
        $entries = $byCycle[$cycle]
        $completes = ($entries | Where-Object { $_.status -eq "complete" }).Count
        Write-Host "  CYCLE $cycle  [$completes/$($NUCLEI.Count) complete]" -ForegroundColor White
        Write-Host ""

        foreach ($nuc in $NUCLEI) {
            $entry = $entries | Where-Object { $_.nucleus -eq $nuc } | Select-Object -First 1
            if ($entry) {
                $icon = if ($entry.status -eq "complete") { "[OK]" } else { "[!!]" }
                $color = if ($entry.status -eq "complete") { "Green" } else { "Yellow" }
                $passes = if ($entry.details.passes) { "P:$($entry.details.passes)" } else { "" }
                $fails = if ($entry.details.fails) { "F:$($entry.details.fails)" } else { "" }
                Write-Host "    $icon $nuc $($DOMAINS[$nuc].PadRight(15)) $($entry.status.PadRight(10)) $passes $fails" -ForegroundColor $color
            } else {
                Write-Host "    [..] $nuc $($DOMAINS[$nuc].PadRight(15)) pending" -ForegroundColor DarkGray
            }
        }
        Write-Host ""
    }

    # Check for active processes
    $workers = Get-Process python* -EA SilentlyContinue | Where-Object {
        $_.MainWindowTitle -match "flywheel" -or $_.CommandLine -match "flywheel"
    }
    if ($workers) {
        Write-Host "  ACTIVE: $($workers.Count) worker processes" -ForegroundColor Green
    }

    # Check log
    $logFile = "$signalDir\flywheel.log"
    if (Test-Path $logFile) {
        Write-Host "  LOG (last 5 lines):" -ForegroundColor DarkGray
        Get-Content $logFile -Tail 5 | ForEach-Object {
            Write-Host "    $_" -ForegroundColor DarkGray
        }
    }
}

# Run
Show-Status

if ($watch) {
    Write-Host ""
    Write-Host "  Watching every ${interval}s... (Ctrl+C to stop)" -ForegroundColor Cyan
    while ($true) {
        Start-Sleep -Seconds $interval
        Show-Status
    }
}
