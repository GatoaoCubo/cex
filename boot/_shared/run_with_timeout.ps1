# Timeout watchdog for boot wrappers.
# Reads $env:CEX_NUCLEUS_TIMEOUT (seconds, default 300).
# Spawns a background job that tree-kills the wrapper's CHILDREN after timeout,
# leaving the wrapper alive so Emit-ExitSignal can still run.
#
# Usage in wrapper:
#   . $PSScriptRoot/_shared/run_with_timeout.ps1
#   $watchdog = Start-CexWatchdog
#   & gemini @cliArgs $initialMsg        # or claude/codex/ollama
#   $status = Stop-CexWatchdog $watchdog # returns 'timeout' or 'exited'
#   Emit-ExitSignal -StartTime $cex_start_time -Status $status

function Start-CexWatchdog {
    param(
        [int]$TimeoutSec = 0
    )
    if ($TimeoutSec -le 0) {
        if ($env:CEX_NUCLEUS_TIMEOUT) {
            $TimeoutSec = [int]$env:CEX_NUCLEUS_TIMEOUT
        } else {
            $TimeoutSec = 300
        }
    }
    $wrapperPid = $PID
    $job = Start-Job -ScriptBlock {
        param($ppid, $t)
        Start-Sleep -Seconds $t
        # Only kill CHILDREN of wrapper -- wrapper itself must survive to signal
        $kids = Get-CimInstance Win32_Process -EA SilentlyContinue |
            Where-Object { $_.ParentProcessId -eq $ppid }
        foreach ($k in $kids) {
            taskkill /F /PID $k.ProcessId /T 2>&1 | Out-Null
        }
        return "timeout_fired"
    } -ArgumentList $wrapperPid, $TimeoutSec
    Write-Host "[WATCHDOG] armed for ${TimeoutSec}s (wrapper PID:$wrapperPid)" -ForegroundColor DarkGray
    return $job
}

function Stop-CexWatchdog {
    param($Job)
    if (-not $Job) { return "exited" }
    $fired = ($Job.State -eq "Completed")
    Stop-Job $Job -EA SilentlyContinue | Out-Null
    Remove-Job $Job -Force -EA SilentlyContinue | Out-Null
    if ($fired) {
        Write-Host "[WATCHDOG] TIMEOUT -- nucleus exceeded budget, children tree-killed" -ForegroundColor Red
        return "timeout"
    }
    Write-Host "[WATCHDOG] disarmed -- nucleus finished within budget" -ForegroundColor DarkGray
    return "exited"
}
