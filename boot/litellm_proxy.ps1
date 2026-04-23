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
$configPath = "$cexRoot\.cex\P09_config\litellm_config.yaml"
$venvPython = "$cexRoot\.venv_litellm\Scripts\python.exe"

if (-not (Test-Path $configPath)) {
    Write-Host "[FAIL] LiteLLM config not found: $configPath" -ForegroundColor Red
    exit 1
}

# Prefer dedicated 3.12 venv (orjson has no 3.14 wheel)
# Invoke python -m (avoids Windows App Control blocking unsigned .exe shims)
if (Test-Path $venvPython) {
    $pythonExe = $venvPython
} else {
    $pythonExe = "python"
    try {
        & $pythonExe -c "import litellm.proxy" 2>$null
        if ($LASTEXITCODE -ne 0) { throw "missing" }
    } catch {
        Write-Host "[FAIL] litellm[proxy] not installed. Create venv:" -ForegroundColor Red
        Write-Host "  py -3.12 -m venv .venv_litellm" -ForegroundColor Yellow
        Write-Host "  .venv_litellm\Scripts\python.exe -m pip install 'litellm[proxy]' pyyaml" -ForegroundColor Yellow
        exit 1
    }
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

# Force UTF-8 (LiteLLM banner has Unicode; Windows cp1252 default crashes)
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"

# Clear DATABASE_URL so prisma migrate is skipped (we run keyless / no DB).
# .env may carry a stale Railway URL -- override here.
$env:DATABASE_URL = ""
$env:LITELLM_DB_URL = ""

# Start LiteLLM proxy via python -m (avoids signed-EXE policy)
& $pythonExe -m litellm.proxy.proxy_cli --config $configPath --port 4000 --detailed_debug
