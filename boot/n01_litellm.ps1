# CEX N01 LiteLLM -- routes via proxy on :4000
# Mirrors boot/n01_ollama.ps1 but talks to the LiteLLM proxy instead of
# Ollama directly. Model alias: cex-n01 -- proxy decides backend (Anthropic
# -> Gemini -> Ollama gemma4:26b -> qwen3) per .cex/config/litellm_config.yaml.

$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "n01"
$sinName = "Analytical Envy"

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
} catch {}

function Set-CexTitle($status) {
    $t = "N01 $sinName [LITELLM]"
    if ($gitRepo)   { $t += " | $gitRepo" }
    if ($gitBranch) { $t += "@$gitBranch" }
    if ($mission)   { $t += " [$mission]" }
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}

Set-CexTitle "BOOTING"

$env:CEX_NUCLEUS = "N01"
$env:CEX_ROOT    = $cexRoot
Set-Location $env:CEX_ROOT

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

Write-Host "  [>>] Launching litellm_nucleus.py with model alias cex-n01" -ForegroundColor Green
Write-Host ""

Set-CexTitle "RUNNING"
& python "$cexRoot\_tools\litellm_nucleus.py" --nucleus N01 --base-url $proxyUrl
Set-CexTitle "DONE"
