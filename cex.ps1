# CEX shortcut -- PowerShell-native (no cmd subshell)
# Opens N07 Orchestrator on the cex (gato-ao-cubo) worktree
# Usage: cex [subcommand] [args...]

$CexRoot = $PSScriptRoot
Set-Location $CexRoot

if ($args.Count -eq 0) {
    & "$CexRoot\boot\cex.ps1"
    return
}

$sub  = $args[0]
$rest = if ($args.Count -gt 1) { $args[1..($args.Count - 1)] } else { @() }

switch ($sub) {
    'status' { & "$CexRoot\_spawn\spawn_monitor.ps1" }
    'stop'   { & "$CexRoot\_spawn\spawn_stop.ps1" @rest }
    'grid'   { & "$CexRoot\_spawn\spawn_grid.ps1" -mission $rest[0] -interactive }
    'solo'   {
        $task = if ($rest.Count -gt 1) { $rest[1] } else { '' }
        & "$CexRoot\_spawn\spawn_solo.ps1" -nucleus $rest[0] -task $task -interactive
    }
    'doctor' { python "$CexRoot\_tools\cex_doctor.py" }
    default  { & "$CexRoot\boot\cex.ps1" @args }
}
