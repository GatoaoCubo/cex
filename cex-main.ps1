# CEX-MAIN shortcut -- PowerShell-native (no cmd subshell)
# Usage: cex-main [subcommand] [args...]
#   cex-main          -- boot N07 orchestrator on cex-main worktree
#   cex-main status   -- monitor spawned nuclei
#   cex-main stop     -- stop MY session's nuclei (pass -All for everything)
#   cex-main grid M   -- launch grid mission M
#   cex-main solo N T -- launch nucleus N with task T
#   cex-main doctor   -- run cex_doctor.py

$CexRoot = 'C:\Users\PC\Documents\GitHub\cex-main'
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
