# CEX Aider Grid -- PowerShell Visual Mode
# Opens 1 window per nucleus with aider + ollama, visible and interactive
#
# Usage: powershell -File _spawn\spawn_grid_aider.ps1 -mission MISSION
#        (or via: bash _spawn/dispatch.sh grid-aider MISSION)

param(
    [string]$mission = "GRID",
    [string]$model = "ollama_chat/qwen3:8b",
    [string[]]$nuclei = @("n01","n02","n03","n04","n05","n06")
)

$CEX_ROOT = Split-Path -Parent $PSScriptRoot
$pidFile = Join-Path $CEX_ROOT ".cex\runtime\pids\spawn_pids_aider.txt"
$tmpDir = Join-Path $env:TEMP "cex_aider"
New-Item -ItemType Directory -Path $tmpDir -Force | Out-Null

Write-Host "=== CEX Aider Grid: $mission ===" -ForegroundColor Cyan
Write-Host "  Model: $model (FREE, local)" -ForegroundColor Green

# Clear pid file
"" | Out-File $pidFile -Encoding utf8

foreach ($nuc in $nuclei) {
    $taskFile = Join-Path $CEX_ROOT "${nuc}_task.md"

    if (-not (Test-Path $taskFile)) {
        Write-Host "  [$($nuc.ToUpper())] SKIP -- no ${nuc}_task.md" -ForegroundColor DarkGray
        continue
    }

    # Write a temp launcher script per nucleus (avoids all quoting issues)
    $launcher = Join-Path $tmpDir "launch_${nuc}.ps1"
    $title = "$($nuc.ToUpper()) [AIDER+OLLAMA] - $mission"

    @"
`$env:OLLAMA_API_BASE = 'http://localhost:11434'
Set-Location '$CEX_ROOT'
`$Host.UI.RawUI.WindowTitle = '$title'
`$Host.UI.RawUI.ForegroundColor = 'White'
Write-Host ''
Write-Host '  ============================================' -ForegroundColor Cyan
Write-Host '  $($nuc.ToUpper()) -- Aider + Ollama' -ForegroundColor Cyan
Write-Host '  Model: $model | Cost: `$0' -ForegroundColor Green
Write-Host '  Task: ${nuc}_task.md' -ForegroundColor Gray
Write-Host '  ============================================' -ForegroundColor Cyan
Write-Host ''
aider --model $model --subtree-only --yes-always --auto-commits --no-show-model-warnings --no-suggest-shell-commands --commit-language english --file ${nuc}_task.md --read CLAUDE.md --message 'Read the task file and execute every task described. Create all requested files. Always write in English.'
Write-Host ''
Write-Host '  [DONE] $($nuc.ToUpper()) finished.' -ForegroundColor Green
Write-Host '  Press any key to close...' -ForegroundColor DarkGray
`$null = `$Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
"@ | Out-File $launcher -Encoding utf8

    $proc = Start-Process powershell -ArgumentList "-ExecutionPolicy","Bypass","-File",$launcher -PassThru
    "$($proc.Id) $nuc aider s_aider $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')" | Add-Content $pidFile -Encoding utf8

    Write-Host "  [$($nuc.ToUpper())] PID:$($proc.Id) -- window opened" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Grid: windows opened. Watch them work! ===" -ForegroundColor Cyan
Write-Host "  Kill all: Get-Process powershell | Where { `$_.MainWindowTitle -match 'AIDER' } | Stop-Process" -ForegroundColor DarkGray
