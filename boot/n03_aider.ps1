# CEX Nucleus N03 (Engineering) -- Aider + Ollama Free Mode
# Spawns aider with qwen3:14b for artifact building at $0 cost
# Usage: boot\n03_aider.ps1  (reads n03_task.md for instructions)

. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI (claude/gemini/codex/ollama)
. $PSScriptRoot/_shared/fix_pathext.ps1  # Guard: .PS1 before .CMD breaks npx-based MCP servers
$ErrorActionPreference = "SilentlyContinue"
$CEX_ROOT = Split-Path -Parent $PSScriptRoot
Set-Location $CEX_ROOT

# --- Window identity ---
$Host.UI.RawUI.WindowTitle = "N03 Engineering [AIDER+OLLAMA] - CEX"
$Host.UI.RawUI.ForegroundColor = "Cyan"

# --- Read task file ---
$taskFile = Join-Path $CEX_ROOT "n03_task.md"
$handoffDir = Join-Path $CEX_ROOT ".cex\runtime\handoffs"

if (Test-Path $taskFile) {
    $task = Get-Content $taskFile -Raw -Encoding UTF8
    Write-Host "[N03-AIDER] Task loaded from n03_task.md" -ForegroundColor Green
} elseif (Test-Path "$handoffDir\*n03*") {
    $latest = Get-ChildItem "$handoffDir\*n03*" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    $task = Get-Content $latest.FullName -Raw -Encoding UTF8
    Write-Host "[N03-AIDER] Task loaded from $($latest.Name)" -ForegroundColor Green
} else {
    $task = "You are N03 Engineering nucleus of CEX. Read CLAUDE.md for context. Ask the user what to build."
    Write-Host "[N03-AIDER] No task file found. Interactive mode." -ForegroundColor Yellow
}

# --- Collect relevant files for aider context ---
$contextFiles = @(
    "CLAUDE.md"
    ".claude/rules/n03-builder.md"
    ".claude/rules/8f-reasoning.md"
    ".cex/kinds_meta.json"
)

# Add task file if exists
if (Test-Path $taskFile) {
    $contextFiles += "n03_task.md"
}

# Filter to existing files
$existingFiles = $contextFiles | Where-Object { Test-Path (Join-Path $CEX_ROOT $_) }
$fileArgs = ($existingFiles | ForEach-Object { "--file `"$_`"" }) -join " "

# --- Launch aider ---
# Set Ollama API base
$env:OLLAMA_API_BASE = "http://localhost:11434"

# Run aider (interactive with task context)
aider --model ollama_chat/qwen3:14b --auto-commits --yes --subtree-only --no-show-model-warnings @existingFiles
