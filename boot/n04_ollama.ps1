# CEX N04 Ollama -- CEX-N04-KNOWLEDGE (Aider + Ollama)
# Mirrors boot/n04.ps1 but uses aider CLI with local Ollama model
# CLI: aider | Model: ollama/gemma4:26b (fallback: ollama/qwen3:14b)
# Sin: Knowledge Gluttony (Knowledge Gluttony)

# --- UX: Window title with mission + sin + status ---
$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "n04"
$sinName = "Knowledge Gluttony"

# Detect model (env override or default)
$ollamaModel = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { "gemma4:26b" }
$modelShort = "ollama/$ollamaModel"

# Detect mission from handoff file
$mission = ""
$handoff = "$cexRoot\.cex\runtime\handoffs\${nucleus}_task.md"
if (Test-Path $handoff) {
    $content = Get-Content $handoff -Head 10 -EA SilentlyContinue
    foreach ($line in $content) {
        if ($line -match "^mission:\s*(.+)$") {
            $mission = $Matches[1].Trim()
            break
        }
    }
}

# Detect git repo name + branch
$gitBranch = ""
$gitRepo = ""
try {
    $gitBranch = (git rev-parse --abbrev-ref HEAD 2>$null)
    $gitRemote = (git remote get-url origin 2>$null)
    if ($gitRemote -match "[/:]([^/]+?)(?:\.git)?$") { $gitRepo = $Matches[1] }
} catch {}

# Build title: N0X Sin | repo@branch [mission] -- STATUS
function Set-CexTitle($status) {
    $t = "N04 $sinName [OLLAMA]"
    if ($gitRepo) { $t += " | $gitRepo" }
    if ($gitBranch) { $t += "@$gitBranch" }
    if ($mission) { $t += " [$mission]" }
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}

Set-CexTitle "BOOTING"

try {
    $Host.UI.RawUI.BackgroundColor = "DarkCyan"
    $Host.UI.RawUI.ForegroundColor = "White"
    if (-not $env:CEX_GRID) {
        $bufSize = $Host.UI.RawUI.BufferSize
        $bufSize.Width = 160; $bufSize.Height = 9999
        $Host.UI.RawUI.BufferSize = $bufSize
        $winSize = $Host.UI.RawUI.WindowSize
        $winSize.Width = [Math]::Min(160, $Host.UI.RawUI.MaxWindowSize.Width)
        $winSize.Height = [Math]::Min(40, $Host.UI.RawUI.MaxWindowSize.Height)
        $Host.UI.RawUI.WindowSize = $winSize
    }
    Clear-Host
} catch {}

Write-Host ""
Write-Host "  [*] N04 Knowledge Gluttony - OLLAMA MODE" -ForegroundColor Cyan
Write-Host "  ==================================================" -ForegroundColor DarkGray
Write-Host "  Got MORE data to ingest-" -ForegroundColor DarkGray
Write-Host "  $modelShort  |  aider CLI  |  LOCAL inference" -ForegroundColor DarkGray
if ($mission) { Write-Host "  Mission: $mission" -ForegroundColor Cyan }
Write-Host ""

# --- Environment ---
$env:CEX_NUCLEUS = "N04"
$env:CEX_ROOT = $cexRoot
Set-Location $env:CEX_ROOT

# --- Build task file for aider --message-file ---
$sysPrompt = @'
You are N04 Knowledge Nucleus of CEX, driven by Knowledge Gluttony.
Ingest every source available. Index, catalog, relate.
Your hunger for data is insatiable -- always seek one more source.
Domain: RAG, indexing, knowledge cards, taxonomy, documentation.

IMPORTANT RULES:
1. Read .cex/runtime/handoffs/n04_task.md for your task
2. Execute the task fully and autonomously
3. All artifacts need YAML frontmatter with quality: null
4. After saving files, run: python _tools/cex_compile.py <path>
5. Commit with: git add <files> && git commit -m "[N04] <description>"
6. Signal complete: python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"
'@

$taskContent = ""
if (Test-Path $handoff) {
    $taskContent = Get-Content $handoff -Raw -EA SilentlyContinue
}

# Write combined prompt to temp file
$tempDir = "$cexRoot\.cex\runtime\tmp"
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
$taskFile = "$tempDir\n04_ollama_task.md"

$combined = @"
$sysPrompt

---

## TASK (from handoff)

$taskContent

---

Read the task above and execute it now. If no task content, report ready.
"@
$combined | Set-Content $taskFile -Encoding utf8

# --- Probe model availability ---
$modelToUse = "ollama/$ollamaModel"
Write-Host "  [>>] Probing Ollama for $ollamaModel..." -ForegroundColor DarkGray
$ollamaUp = $false
try {
    $resp = Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 5 -EA Stop
    $ollamaUp = $true
    $available = $resp.models | ForEach-Object { $_.name }
    if ($available -notcontains $ollamaModel -and $available -notcontains "${ollamaModel}:latest") {
        Write-Host "  [WARN] $ollamaModel not found, falling back to qwen3:14b" -ForegroundColor Yellow
        $modelToUse = "ollama/qwen3:14b"
    } else {
        Write-Host "  [OK] $ollamaModel available" -ForegroundColor Green
    }
} catch {
    Write-Host "  [FAIL] Ollama not responding at localhost:11434" -ForegroundColor Red
    Write-Host "  Start Ollama first: ollama serve" -ForegroundColor Red
    Set-CexTitle "FAIL - NO OLLAMA"
    return
}

# --- Launch aider ---
$aiderArgs = @(
    "--model", $modelToUse,
    "--no-git",
    "--yes-always",
    "--no-suggest-shell-commands",
    "--message-file", $taskFile
)

Write-Host "  [>>] Launching aider with $modelToUse" -ForegroundColor Cyan
Write-Host ""

Set-CexTitle "RUNNING"
& aider @aiderArgs
Set-CexTitle "DONE"
