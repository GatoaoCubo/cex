# CEX N05 LiteLLM -- routes via proxy on :4000
# Mirrors boot/n05_ollama.ps1 but talks to the LiteLLM proxy instead of
# Ollama directly. Model alias: cex-n05 -- proxy decides backend (Anthropic
# -> Gemini -> Ollama gemma4:26b -> qwen3) per .cex/P09_config/litellm_config.yaml.

. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI (claude/gemini/codex/ollama)
. $PSScriptRoot/_shared/emit_exit_signal.ps1
$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "n05"
. $PSScriptRoot/_shared/theme.ps1  # Per-nucleus theme (bg color, scrollback)
$sinName = "Gating Wrath"

$proxyUrl = if ($env:LITELLM_BASE_URL) { $env:LITELLM_BASE_URL } else { "http://localhost:4000" }

$mission = ""
$handoff = "$cexRoot\.cex\runtime\handoffs\${nucleus}_task.md"
if (Test-Path $handoff) {
    $content = Get-Content $handoff -Head 10 -EA SilentlyContinue
    foreach ($line in $content) {
        if ($line -match "^mission:\s*(.+)$") { $mission = $Matches[1].Trim(); break }
    }
}

$gitBranch = ""; $gitRepo = ""
try {
    $gitBranch = (git rev-parse --abbrev-ref HEAD 2>$null)
    $gitRemote = (git remote get-url origin 2>$null)
    if ($gitRemote -match "[/:]([^/]+?)(?:\.git)?$") { $gitRepo = $Matches[1] }
    Clear-Host
} catch {}

function Set-CexTitle($status) {
    $t = "N05 $sinName [LITELLM]"
    if ($gitRepo)   { $t += " | $gitRepo" }
    if ($gitBranch) { $t += "@$gitBranch" }
    if ($mission)   { $t += " [$mission]" }
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}

Set-CexTitle "BOOTING"

$env:CEX_NUCLEUS = "N05"
$env:CEX_ROOT    = $cexRoot
Set-Location $env:CEX_ROOT

# Load .env (secrets for MCP servers, LLM providers). System env wins.
. "$PSScriptRoot\_shared\load_dotenv.ps1"

Write-Host "  [>>] Probing LiteLLM proxy at $proxyUrl ..." -ForegroundColor DarkGray
try {
    $h = Invoke-RestMethod -Uri "$proxyUrl/health/liveliness" -TimeoutSec 5 -EA Stop
    Write-Host "  [OK] proxy: $h" -ForegroundColor Green
} catch {
    Write-Host "  [FAIL] LiteLLM proxy not responding at $proxyUrl" -ForegroundColor Red
    Write-Host "  Start it: powershell -File boot/litellm_proxy.ps1" -ForegroundColor Yellow
    Set-CexTitle "FAIL - NO PROXY"
    return
}

if (-not (Test-Path $handoff)) {
    Write-Host "  [WARN] No handoff at $handoff" -ForegroundColor Yellow
    Write-Host "  Drop a task there or the runner will exit." -ForegroundColor Yellow
}

$env:CEX_TASK_FILE = $handoff

Write-Host "  [>>] Launching litellm_nucleus.py with model alias cex-n05" -ForegroundColor Green
Write-Host ""

Set-CexTitle "RUNNING"
$cex_start_time = Get-Date
& python "$cexRoot\_tools\litellm_nucleus.py" --nucleus N05 --base-url $proxyUrl
Set-CexTitle "DONE"
Emit-ExitSignal -StartTime $cex_start_time
