# Exit-signal safety net for non-claude runtimes (gemini, codex, ollama).
# Emits a signal AFTER the CLI exits IF the LLM inside didn't already signal.
# This prevents the "nucleus ran, produced artifact, but no signal" failure mode
# that breaks grid polling (showoff wave 5, etc.).
#
# Contract:
#   - Caller sets $env:CEX_NUCLEUS (n01..n06) and optionally $env:CEX_MISSION.
#   - Call Emit-ExitSignal at the END of the wrapper, after the CLI returns.
#   - If a signal for this nucleus exists dated >= script-start-time, no-op.
#   - Otherwise writes status='exited' signal so the orchestrator unblocks.

function Emit-ExitSignal {
    param(
        [string]$Nucleus = $env:CEX_NUCLEUS,
        [string]$Mission = $env:CEX_MISSION,
        [datetime]$StartTime = (Get-Date).AddHours(-1),
        [string]$Status = "exited",
        [double]$Quality = 0.0
    )
    if (-not $Nucleus) { return }
    $Nucleus = $Nucleus.ToLower()
    $root = if ($env:CEX_ROOT) { $env:CEX_ROOT } else { Split-Path -Parent $PSScriptRoot | Split-Path -Parent }
    $signalDir = Join-Path $root ".cex\runtime\signals"
    if (-not (Test-Path $signalDir)) { New-Item -ItemType Directory -Force -Path $signalDir | Out-Null }

    # Check if a signal for this nucleus was written since StartTime
    $existing = Get-ChildItem $signalDir -Filter "signal_${Nucleus}_*.json" -EA SilentlyContinue |
                Where-Object { $_.LastWriteTime -ge $StartTime }
    if ($existing) {
        Write-Host "[EXIT_SIGNAL] $Nucleus already signalled ($($existing.Count) signals since start)" -ForegroundColor DarkGray
        return
    }

    # No signal -- emit a best-effort exited signal
    try {
        $py = "python"
        $cmd = "import sys; sys.path.insert(0, '_tools'); from signal_writer import write_signal; write_signal('$Nucleus', '$Status', $Quality, mission='$Mission')"
        & $py -c $cmd 2>&1 | Out-Host
        Write-Host "[EXIT_SIGNAL] $Nucleus emitted safety-net signal (status=$Status mission=$Mission)" -ForegroundColor Yellow
    } catch {
        Write-Host "[EXIT_SIGNAL] failed to emit for ${Nucleus}: $_" -ForegroundColor Red
    }
}
