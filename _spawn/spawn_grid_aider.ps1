# CEX Grid Dispatch -- Aider + Ollama Free Mode
# Spawns N nuclei as separate aider instances with free local models
# Usage: powershell -File _spawn\spawn_grid_aider.ps1 -mission MISSION_NAME
#
# Each nucleus gets its own PowerShell window running aider + ollama.
# Total cost: $0 (all inference on local GPU/CPU)
# Limitation: no sub-agents, no MCP, 32K context (vs Claude's 1M)
# Best for: overnight evolve, bulk operations, simple builds

param(
    [string]$mission = "GRID",
    [string]$model = "ollama_chat/qwen3:14b",
    [string[]]$nuclei = @("n01","n02","n03","n04","n05","n06")
)

$CEX_ROOT = Split-Path -Parent $PSScriptRoot
$handoffDir = Join-Path $CEX_ROOT ".cex\runtime\handoffs"
$pidFile = Join-Path $CEX_ROOT ".cex\runtime\pids\spawn_pids_aider.txt"

Write-Host "=== CEX Aider Grid: $mission ===" -ForegroundColor Cyan
Write-Host "  Model: $model (FREE, local)" -ForegroundColor Green
Write-Host "  Nuclei: $($nuclei -join ', ')" -ForegroundColor White

# Find handoffs for this mission
$handoffs = Get-ChildItem "$handoffDir\${mission}_*.md" -ErrorAction SilentlyContinue

if ($handoffs.Count -eq 0) {
    # Try per-nucleus task files
    $handoffs = $nuclei | ForEach-Object {
        $tf = Join-Path $CEX_ROOT "${_}_task.md"
        if (Test-Path $tf) { Get-Item $tf }
    }
}

Write-Host "  Handoffs found: $($handoffs.Count)" -ForegroundColor White
Write-Host ""

# Clear pid file
"" | Out-File $pidFile -Encoding utf8

foreach ($nuc in $nuclei) {
    $taskFile = Join-Path $CEX_ROOT "${nuc}_task.md"
    $handoff = $handoffs | Where-Object { $_.Name -match $nuc } | Select-Object -First 1

    if (-not $handoff -and -not (Test-Path $taskFile)) {
        Write-Host "  [$($nuc.ToUpper())] SKIP -- no handoff or task file" -ForegroundColor DarkGray
        continue
    }

    # Context files per nucleus
    $ruleFile = ".claude/rules/$nuc-*.md" | Resolve-Path -ErrorAction SilentlyContinue | Select-Object -First 1
    $contextArgs = @("CLAUDE.md")
    if ($ruleFile) { $contextArgs += $ruleFile.Path }
    if (Test-Path $taskFile) { $contextArgs += $taskFile }

    # Read task content for --message
    $taskContent = ""
    if (Test-Path $taskFile) {
        $taskContent = (Get-Content $taskFile -Raw -Encoding UTF8).Substring(0, [Math]::Min(2000, (Get-Content $taskFile -Raw).Length))
    } elseif ($handoff) {
        $taskContent = (Get-Content $handoff.FullName -Raw -Encoding UTF8).Substring(0, [Math]::Min(2000, (Get-Content $handoff.FullName -Raw).Length))
    }

    # Spawn in new window
    # IMPORTANT: Do NOT pass --message with task content inline.
    # PS nested quoting breaks on special chars. Instead, use --read to load
    # the task file and --message with a short fixed instruction.
    $title = "$($nuc.ToUpper()) [AIDER+OLLAMA] - $mission"
    # Pass task file as --file (editable+readable), context as --read
    $fileArgs = @()
    $readArgs = @()
    if (Test-Path $taskFile) { $fileArgs += $taskFile }
    foreach ($cf in $existingFiles) {
        if ($cf -ne $taskFile) { $readArgs += "--read $cf" }
    }
    $fileStr = ($fileArgs | ForEach-Object { "--file $_" }) -join " "
    $readStr = $readArgs -join " "

    $envSetup = "`$env:OLLAMA_API_BASE = 'http://localhost:11434'"
    $cmd = "$envSetup; Set-Location '$CEX_ROOT'; `$Host.UI.RawUI.WindowTitle = '$title'; aider --model $model --subtree-only --yes --auto-commits --no-show-model-warnings $fileStr $readStr --message 'Read n03_task.md carefully and execute every task in it. Create all files listed.'"

    $proc = Start-Process powershell -ArgumentList "-NoExit", "-Command", $cmd -PassThru
    "$($proc.Id) $nuc aider s_aider $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')" | Add-Content $pidFile -Encoding utf8

    Write-Host "  [$($nuc.ToUpper())] PID:$($proc.Id) -- aider + $model" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Grid launched: $($nuclei.Count) nuclei via Aider ===" -ForegroundColor Cyan
Write-Host "  Cost: `$0 (all local inference)" -ForegroundColor Green
Write-Host "  PID file: $pidFile" -ForegroundColor DarkGray
