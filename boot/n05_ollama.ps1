# CEX N05 Ollama -- CEX-N05-OPERATIONS (Aider + Ollama)
# Mirrors boot/n05.ps1 but uses direct Ollama API via _tools/ollama_nucleus.py
# CLI: python | Model: qwen3:8b (default) -- aider replaced 2026-04-13
# Sin: Gating Wrath (Gating Wrath)

# --- UX: Window title with mission + sin + status ---
. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI (claude/gemini/codex/ollama)
. $PSScriptRoot/_shared/emit_exit_signal.ps1
. $PSScriptRoot/_shared/run_with_timeout.ps1
$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "n05"
. $PSScriptRoot/_shared/theme.ps1  # Per-nucleus theme (bg color, scrollback)
$sinName = "Gating Wrath"

# Detect model (env override or default)
$ollamaModel = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { "qwen3:8b" }
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
    Clear-Host
} catch {}

# Build title: N0X Sin | repo@branch [mission] -- STATUS
function Set-CexTitle($status) {
    $t = "N05 $sinName [OLLAMA]"
    if ($gitRepo) { $t += " | $gitRepo" }
    if ($gitBranch) { $t += "@$gitBranch" }
    if ($mission) { $t += " [$mission]" }
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}

Set-CexTitle "BOOTING"

# --- Environment ---
$env:CEX_NUCLEUS = "N05"
$env:CEX_ROOT = $cexRoot
Set-Location $env:CEX_ROOT

# Load .env (secrets for MCP servers, LLM providers). System env wins.
. "$PSScriptRoot\_shared\load_dotenv.ps1"

# --- Build task file for aider --message-file ---
$sysPrompt = @'
You are N05 Operations Nucleus of CEX, driven by Gating Wrath.
CI gates are absolute. Tests must pass. Deploys are gated.
No mercy for broken builds or skipped validations.
Domain: code review, testing, CI/CD, deploy, infrastructure.

IMPORTANT RULES:
1. Read .cex/runtime/handoffs/n05_task.md for your task
2. Execute the task fully and autonomously
3. All artifacts need YAML frontmatter with quality: null
4. After saving files, run: python _tools/cex_compile.py <path>
5. Commit with: git add <files> && git commit -m "[N05] <description>"
6. Signal complete: python -c "from _tools.signal_writer import write_signal; write_signal('n05', 'complete', 9.0)"
'@

$taskContent = ""
if (Test-Path $handoff) {
    $taskContent = Get-Content $handoff -Raw -EA SilentlyContinue
}

# Write combined prompt to temp file
$tempDir = "$cexRoot\.cex\runtime\tmp"
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
$taskFile = "$tempDir\n05_ollama_task.md"

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

# --- Launch direct API wrapper (ollama_nucleus.py) ---
# aider replaced 2026-04-13: aider cannot parse full-file LLM output (expects SEARCH/REPLACE)
$env:CEX_TASK_FILE = $handoff

Write-Host "  [>>] Launching ollama_nucleus.py with $ollamaModel" -ForegroundColor Red
Write-Host ""

Set-CexTitle "RUNNING"
$cex_start_time = Get-Date
$watchdog = Start-CexWatchdog
& python "$cexRoot\_tools\ollama_nucleus.py" --nucleus N05 --model $ollamaModel --task-file $handoff
$exitStatus = Stop-CexWatchdog $watchdog
Set-CexTitle "DONE"
Emit-ExitSignal -StartTime $cex_start_time -Status $exitStatus
