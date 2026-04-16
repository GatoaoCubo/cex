# PowerShell-native launcher for the current worktree.
# Usage: repo-launch [subcommand] [args...]

$RepoRoot = $PSScriptRoot
Set-Location $RepoRoot

if ($args.Count -eq 0) {
    & "$RepoRoot\boot\cex.ps1"
    return
}

$sub  = $args[0]
$rest = if ($args.Count -gt 1) { $args[1..($args.Count - 1)] } else { @() }

switch ($sub) {
    'status' { & "$RepoRoot\_spawn\spawn_monitor.ps1" }
    'stop'   { & "$RepoRoot\_spawn\spawn_stop.ps1" @rest }
    'grid'   { & "$RepoRoot\_spawn\spawn_grid.ps1" -mission $rest[0] -interactive }
    'solo'   {
        $task = if ($rest.Count -gt 1) { $rest[1] } else { '' }
        & "$RepoRoot\_spawn\spawn_solo.ps1" -nucleus $rest[0] -task $task -interactive
    }
    'doctor' { python "$RepoRoot\_tools\cex_doctor.py" }
    default  { & "$RepoRoot\boot\cex.ps1" @args }
}
