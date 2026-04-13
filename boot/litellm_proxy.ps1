# CEX LiteLLM Proxy Boot Script
# Starts LiteLLM as unified routing proxy for all nuclei
#
# Usage: powershell -File boot/litellm_proxy.ps1
# Test:  curl http://localhost:4000/health
# Docs:  http://localhost:4000/docs (Swagger UI)
#
# Every nucleus calls: POST http://localhost:4000/v1/chat/completions
# with model: "cex-n0X" -- LiteLLM routes to correct provider.

$cexRoot = Split-Path -Parent $PSScriptRoot
$configPath = "$cexRoot\.cex\config\litellm_config.yaml"

if (-not (Test-Path $configPath)) {
    Write-Host "[FAIL] LiteLLM config not found: $configPath" -ForegroundColor Red
    exit 1
}

# Check if litellm is installed
$litellm = Get-Command litellm -ErrorAction SilentlyContinue
if (-not $litellm) {
    Write-Host "[FAIL] litellm not found. Install: pip install litellm" -ForegroundColor Red
    exit 1
}

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  CEX LiteLLM Proxy" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Config: $configPath"
Write-Host "Port:   4000"
Write-Host "Health: http://localhost:4000/health"
Write-Host "Docs:   http://localhost:4000/docs"
Write-Host ""
Write-Host "Models routed:" -ForegroundColor Yellow
Write-Host "  cex-n07 -> opus (orchestration)"
Write-Host "  cex-n03 -> opus (building)"
Write-Host "  cex-n01 -> sonnet (research)"
Write-Host "  cex-n02 -> sonnet (marketing)"
Write-Host "  cex-n04 -> sonnet (knowledge)"
Write-Host "  cex-n05 -> sonnet (operations)"
Write-Host "  cex-n06 -> sonnet (commercial)"
Write-Host ""
Write-Host "Press Ctrl+C to stop" -ForegroundColor DarkGray
Write-Host ""

# Start LiteLLM proxy
litellm --config $configPath --port 4000 --detailed_debug
