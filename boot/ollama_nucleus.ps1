# CEX Ollama Nucleus Boot -- Lightweight local model runner
# Usage: powershell -File boot/ollama_nucleus.ps1 -Nucleus n01 [-Model qwen3:14b]
#
# Designed for overnight evolve and bulk operations where cost > quality.
# No MCP servers, no sub-agents -- just system prompt + task + ollama.
#
# The script:
#   1. Reads nucleus config from nucleus_models.yaml (fallback_local.model)
#   2. Reads the task handoff from .cex/runtime/handoffs/{nucleus}_task.md
#   3. Loads the agent card as system context
#   4. Pipes everything into `ollama run` as an interactive session

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("n01","n02","n03","n04","n05","n06")]
    [string]$Nucleus,

    [string]$Model = "",

    [switch]$NonInteractive
)

# Auto-detect root from script location (worktree-agnostic)
$cexRoot = Split-Path -Parent $PSScriptRoot
Set-Location $cexRoot

# --- Resolve model ---
if (-not $Model) {
    # Read from nucleus_models.yaml fallback_local or fallback_chain
    $yamlPath = "$cexRoot\.cex\P09_config\nucleus_models.yaml"
    if (Test-Path $yamlPath) {
        $content = Get-Content $yamlPath -Raw
        # Simple regex extraction for this nucleus's fallback_local model
        $section = $false
        foreach ($line in (Get-Content $yamlPath)) {
            if ($line -match "^${Nucleus}:") { $section = $true; continue }
            if ($section -and $line -match "^\w" -and $line -notmatch "^\s") { $section = $false }
            if ($section -and $line -match "^\s+fallback_local:") {
                $inFallback = $true
                continue
            }
            if ($section -and $inFallback -and $line -match "^\s+model:\s*(.+)$") {
                $Model = $Matches[1].Trim()
                break
            }
            if ($section -and $inFallback -and $line -match "^\s+\w+:" -and $line -notmatch "model:") {
                continue
            }
            if ($inFallback -and $line -match "^\s{2}\w") { $inFallback = $false }
        }
    }
    if (-not $Model) { $Model = "qwen3:8b" }
}

# --- Verify ollama is available ---
$ollamaPath = Get-Command ollama -EA SilentlyContinue
if (-not $ollamaPath) {
    Write-Host "[FAIL] ollama not found in PATH. Install from https://ollama.com" -ForegroundColor Red
    exit 1
}

# --- Verify model is pulled ---
$pulled = ollama list 2>&1
if ($pulled -notmatch [regex]::Escape($Model)) {
    Write-Host "[WARN] Model '$Model' not found locally. Pulling..." -ForegroundColor Yellow
    ollama pull $Model
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[FAIL] Could not pull $Model" -ForegroundColor Red
        exit 1
    }
}

# --- Read task handoff ---
$taskFile = "$cexRoot\.cex\runtime\handoffs\${Nucleus}_task.md"
$taskContent = ""
if (Test-Path $taskFile) {
    $taskContent = Get-Content $taskFile -Raw -Encoding UTF8
    Write-Host "[OK] Task loaded: $taskFile" -ForegroundColor Green
} else {
    # Also check root
    $rootTask = "$cexRoot\${Nucleus}_task.md"
    if (Test-Path $rootTask) {
        $taskContent = Get-Content $rootTask -Raw -Encoding UTF8
        Write-Host "[OK] Task loaded: $rootTask" -ForegroundColor Green
    } else {
        Write-Host "[WARN] No task handoff found for $Nucleus" -ForegroundColor Yellow
    }
}

# --- Load agent card as system context ---
$nucDirMap = @{
    "n01" = "N01_intelligence"
    "n02" = "N02_marketing"
    "n03" = "N03_engineering"
    "n04" = "N04_knowledge"
    "n05" = "N05_operations"
    "n06" = "N06_commercial"
}
$nucDir = $nucDirMap[$Nucleus]
$agentCard = "$cexRoot\$nucDir\agent_card_$Nucleus.md"
$systemContext = ""
if (Test-Path $agentCard) {
    $systemContext = Get-Content $agentCard -Raw -Encoding UTF8
}

# --- Read sin prompt injection ---
$sinPrompt = ""
$sinsFile = "$cexRoot\.cex\P09_config\nucleus_sins.yaml"
if (Test-Path $sinsFile) {
    $inNuc = $false
    $inPrompt = $false
    $lines = @()
    foreach ($line in (Get-Content $sinsFile)) {
        if ($line -match "^${Nucleus}:") { $inNuc = $true; continue }
        if ($inNuc -and $line -match "^\w" -and $line -notmatch "^\s") { $inNuc = $false }
        if ($inNuc -and $line -match "^\s+prompt_injection:\s*\|") { $inPrompt = $true; continue }
        if ($inPrompt -and $line -match "^\s{4}\S") {
            $lines += $line.TrimStart()
        }
        if ($inPrompt -and $line -match "^\s{0,2}\S" -and $lines.Count -gt 0) {
            $inPrompt = $false
        }
    }
    $sinPrompt = $lines -join "`n"
}

# --- Window title ---
$Host.UI.RawUI.WindowTitle = "$($Nucleus.ToUpper()) Ollama/$Model -- RUNNING"

# --- Banner ---
Write-Host ""
Write-Host "  [*] $($Nucleus.ToUpper()) -- Ollama/$Model (local)" -ForegroundColor Cyan
Write-Host "  ==================================================" -ForegroundColor DarkGray
Write-Host "  Lightweight mode: no MCP, no sub-agents" -ForegroundColor DarkGray
Write-Host "  For overnight evolve and bulk operations" -ForegroundColor DarkGray
Write-Host ""

# --- Build system prompt ---
$fullSystem = @"
You are CEX nucleus $($Nucleus.ToUpper()).
$sinPrompt

RULES:
- Follow the 8F pipeline for all tasks
- quality: null (never self-score)
- Save artifacts to the correct pillar directory
- Use standard YAML frontmatter on all artifacts

CONTEXT:
$systemContext

TASK:
$taskContent
"@

if ($NonInteractive -and $taskContent) {
    # Non-interactive: pipe task, get response, exit
    Write-Host "[>>] Running non-interactive..." -ForegroundColor DarkGray
    $fullSystem | ollama run $Model
    $Host.UI.RawUI.WindowTitle = "$($Nucleus.ToUpper()) Ollama/$Model -- DONE"
} else {
    # Interactive: start ollama with system prompt, user types queries
    # Write system prompt to temp file for --system flag
    $tmpSystem = [System.IO.Path]::GetTempFileName()
    $fullSystem | Out-File $tmpSystem -Encoding utf8
    Write-Host "[>>] Starting interactive session (type /bye to exit)..." -ForegroundColor DarkGray
    Write-Host ""
    ollama run $Model --system $fullSystem
    Remove-Item $tmpSystem -EA SilentlyContinue
    $Host.UI.RawUI.WindowTitle = "$($Nucleus.ToUpper()) Ollama/$Model -- DONE"
}
