# CEX vLLM Server -- Launches vLLM inside WSL2 with LoRA hot-swap
#
# Usage: powershell -File boot/vllm_server.ps1 [-Model gemma4:27b] [-Port 8000]
# Test:  curl http://localhost:8000/v1/models
# Docs:  http://localhost:8000/docs (Swagger UI)
#
# Architecture:
#   Windows (LiteLLM:4000) -> WSL2 (vLLM:8000) -> GPU (base model + LoRA)
#   One base model loaded once. LoRA adapters swapped per-request via model name.
#
# Request example (with LoRA):
#   curl http://localhost:8000/v1/chat/completions \
#     -d '{"model":"cex-n03","messages":[{"role":"user","content":"hello"}]}'
#
# The "model" field selects the LoRA adapter. Base model handles all.

param(
    [string]$Model = "google/gemma-3-27b-it",

    [int]$Port = 8000,

    [int]$MaxConcurrent = 6,

    [string]$FallbackModel = "Qwen/Qwen3-14B",

    [switch]$NoLoRA,

    [string]$QuantMethod = "awq",

    [int]$GpuMemoryUtilization = 90,

    [int]$MaxLoraRank = 64,

    [int]$MaxModelLen = 16384
)

$ErrorActionPreference = "Stop"
$cexRoot = Split-Path -Parent $PSScriptRoot

# --- Banner ---
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  CEX vLLM Server (WSL2 + LoRA)" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Model:  $Model" -ForegroundColor DarkGray
Write-Host "  Port:   $Port" -ForegroundColor DarkGray
Write-Host "  LoRA:   $(if ($NoLoRA) { 'disabled' } else { 'enabled' })" -ForegroundColor DarkGray
Write-Host ""

# --- Check WSL ---
try {
    $wslCheck = wsl -d Ubuntu-24.04 -- echo "ok" 2>&1
    if ($wslCheck -ne "ok") { throw "WSL not responding" }
} catch {
    Write-Host "[FAIL] Ubuntu-24.04 not available in WSL." -ForegroundColor Red
    Write-Host "       Run: powershell -File boot/vllm_setup.ps1" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] WSL2 Ubuntu-24.04 is running" -ForegroundColor Green

# --- Check vLLM installed ---
$vllmCheck = wsl -d Ubuntu-24.04 -- bash -c "source ~/.venvs/vllm/bin/activate && python3 -c 'import vllm; print(vllm.__version__)'" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[FAIL] vLLM not found in WSL." -ForegroundColor Red
    Write-Host "       Run: powershell -File boot/vllm_setup.ps1" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] vLLM $vllmCheck found" -ForegroundColor Green

# --- Check CUDA ---
$cudaCheck = wsl -d Ubuntu-24.04 -- nvidia-smi --query-gpu=memory.total --format=csv,noheader 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[FAIL] CUDA passthrough not working." -ForegroundColor Red
    exit 1
}
Write-Host "[OK] GPU available: $($cudaCheck.Trim()) VRAM" -ForegroundColor Green

# --- Build LoRA module arguments ---
$loraArgs = ""
if (-not $NoLoRA) {
    # Map Windows adapter paths to WSL mount paths
    $adapterDir = "$cexRoot\_data\ft\adapters"
    $wslAdapterBase = $adapterDir -replace "\\", "/" -replace "^([A-Z]):", '/mnt/$1'
    $wslAdapterBase = $wslAdapterBase.Substring(0,5).ToLower() + $wslAdapterBase.Substring(5)

    # Discover existing LoRA adapter directories
    $nuclei = @("n01", "n02", "n03", "n04", "n05", "n06", "n07")
    $loraModules = @()
    $foundAdapters = @()
    $missingAdapters = @()

    foreach ($nuc in $nuclei) {
        $adapterPath = "$adapterDir\cex-$nuc-qlora"
        $wslPath = "$wslAdapterBase/cex-$nuc-qlora"

        if (Test-Path $adapterPath) {
            # Verify adapter has required files (adapter_config.json or adapter_model.safetensors)
            $hasConfig = (Test-Path "$adapterPath\adapter_config.json") -or (Test-Path "$adapterPath\adapter_model.safetensors")
            if ($hasConfig) {
                $loraModules += "cex-$nuc=$wslPath"
                $foundAdapters += $nuc
            } else {
                $missingAdapters += "$nuc (dir exists but no adapter files)"
            }
        } else {
            $missingAdapters += "$nuc (no directory)"
        }
    }

    if ($loraModules.Count -gt 0) {
        $loraModuleStr = $loraModules -join " "
        $loraArgs = "--enable-lora --max-lora-rank $MaxLoraRank --lora-modules $loraModuleStr"
        Write-Host "[OK] LoRA adapters found: $($foundAdapters -join ', ')" -ForegroundColor Green
    } else {
        Write-Host "[WARN] No LoRA adapter directories found at:" -ForegroundColor Yellow
        Write-Host "       $adapterDir\cex-n0X-qlora\" -ForegroundColor Yellow
        Write-Host "       Starting without LoRA. Train adapters first." -ForegroundColor Yellow
        Write-Host "       Server will still work -- just no per-nucleus specialization." -ForegroundColor DarkGray
    }

    if ($missingAdapters.Count -gt 0) {
        Write-Host "[WARN] Missing adapters: $($missingAdapters -join ', ')" -ForegroundColor Yellow
    }
}

# --- Check if port is in use ---
$portInUse = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
if ($portInUse) {
    Write-Host "[WARN] Port $Port is already in use. Existing vLLM instance?" -ForegroundColor Yellow
    Write-Host "       Kill it first or use -Port to change." -ForegroundColor Yellow
    $response = Read-Host "Continue anyway? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        exit 0
    }
}

# --- HuggingFace token (for gated models like Gemma) ---
$hfToken = $env:HF_TOKEN
$hfArgs = ""
if ($hfToken) {
    Write-Host "[OK] HF_TOKEN found (for gated model access)" -ForegroundColor Green
    $hfArgs = "export HF_TOKEN='$hfToken' &&"
} else {
    Write-Host "[WARN] HF_TOKEN not set. Gated models (Gemma) will fail." -ForegroundColor Yellow
    Write-Host "       Set it: `$env:HF_TOKEN = 'hf_...'" -ForegroundColor Yellow
    Write-Host "       Get token at: https://huggingface.co/settings/tokens" -ForegroundColor DarkGray

    if ($Model -match "gemma") {
        Write-Host "[>>] Falling back to $FallbackModel (ungated)" -ForegroundColor Cyan
        $Model = $FallbackModel
    }
}

# --- GPU memory utilization ---
$gpuUtil = $GpuMemoryUtilization / 100.0
if ($gpuUtil -gt 0.95) { $gpuUtil = 0.95 }
if ($gpuUtil -lt 0.5) { $gpuUtil = 0.5 }

# --- Build vLLM command ---
$vllmCmd = @(
    "$hfArgs",
    "source ~/.venvs/vllm/bin/activate &&",
    "python3 -m vllm.entrypoints.openai.api_server",
    "--model $Model",
    "--host 0.0.0.0",
    "--port $Port",
    "--max-model-len $MaxModelLen",
    "--gpu-memory-utilization $gpuUtil",
    "--max-num-seqs $MaxConcurrent",
    "--dtype auto",
    "--trust-remote-code",
    "--served-model-name base"
) -join " "

# Append LoRA args if any
if ($loraArgs) {
    $vllmCmd += " $loraArgs"
}

# --- Summary ---
Write-Host ""
Write-Host "--- Server Configuration ---" -ForegroundColor Yellow
Write-Host "  Base model:     $Model" -ForegroundColor White
Write-Host "  Max seq len:    $MaxModelLen tokens" -ForegroundColor White
Write-Host "  GPU mem util:   $($GpuMemoryUtilization)%" -ForegroundColor White
Write-Host "  Max concurrent: $MaxConcurrent requests" -ForegroundColor White
Write-Host "  Port:           $Port (OpenAI-compatible)" -ForegroundColor White
Write-Host "  Endpoint:       http://localhost:$Port/v1/chat/completions" -ForegroundColor White
if ($loraArgs) {
    Write-Host "  LoRA adapters:  $($foundAdapters.Count) loaded" -ForegroundColor White
    Write-Host "  Max LoRA rank:  $MaxLoraRank" -ForegroundColor White
}
Write-Host ""
Write-Host "--- API Usage ---" -ForegroundColor Yellow
Write-Host '  # Base model (no LoRA):' -ForegroundColor DarkGray
Write-Host '  curl http://localhost:8000/v1/chat/completions \' -ForegroundColor White
Write-Host '    -H "Content-Type: application/json" \' -ForegroundColor White
Write-Host '    -d "{\"model\":\"base\",\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}]}"' -ForegroundColor White
Write-Host ""
if ($loraArgs) {
    Write-Host '  # With LoRA adapter (per-nucleus):' -ForegroundColor DarkGray
    Write-Host '  curl http://localhost:8000/v1/chat/completions \' -ForegroundColor White
    Write-Host '    -H "Content-Type: application/json" \' -ForegroundColor White
    Write-Host '    -d "{\"model\":\"cex-n03\",\"messages\":[{\"role\":\"user\",\"content\":\"hello\"}]}"' -ForegroundColor White
    Write-Host ""
}
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor DarkGray
Write-Host ""

# --- Window title ---
$Host.UI.RawUI.WindowTitle = "CEX vLLM -- $Model -- port $Port"

# --- Launch vLLM inside WSL ---
wsl -d Ubuntu-24.04 -- bash -c "$vllmCmd"

$Host.UI.RawUI.WindowTitle = "CEX vLLM -- STOPPED"
Write-Host ""
Write-Host "[OK] vLLM server stopped" -ForegroundColor Green
