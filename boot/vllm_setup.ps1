# CEX vLLM Setup -- ONE-TIME WSL2 + CUDA + vLLM installation
#
# Usage: Run as Administrator
#   powershell -ExecutionPolicy Bypass -File boot/vllm_setup.ps1
#
# What this does:
#   1. Installs WSL2 with Ubuntu 24.04
#   2. Inside WSL: installs CUDA toolkit, Python 3.12, vLLM
#   3. Tests CUDA passthrough (nvidia-smi)
#   4. Tests vLLM with a basic completion
#
# Prerequisites:
#   - Windows 11 Pro with virtualization enabled (BIOS)
#   - NVIDIA GPU driver 560+ installed on Windows (NOT inside WSL)
#   - Internet connection
#   - Admin privileges
#
# Hardware target: RTX 5070 Ti (16GB VRAM, Blackwell SM_120)

$ErrorActionPreference = "Stop"
$cexRoot = Split-Path -Parent $PSScriptRoot

# --- Banner ---
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  CEX vLLM Setup (WSL2 + CUDA)" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Target: RTX 5070 Ti (16GB VRAM)" -ForegroundColor DarkGray
Write-Host "  Stack:  WSL2 -> Ubuntu 24.04 -> CUDA -> vLLM" -ForegroundColor DarkGray
Write-Host ""

# --- Check admin ---
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)
if (-not $isAdmin) {
    Write-Host "[FAIL] This script must run as Administrator." -ForegroundColor Red
    Write-Host "       Right-click PowerShell -> Run as Administrator" -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Running as Administrator" -ForegroundColor Green

# --- Check Windows version ---
$osVersion = [System.Environment]::OSVersion.Version
if ($osVersion.Build -lt 19041) {
    Write-Host "[FAIL] Windows build $($osVersion.Build) too old. Need 19041+ for WSL2." -ForegroundColor Red
    exit 1
}
Write-Host "[OK] Windows build $($osVersion.Build) supports WSL2" -ForegroundColor Green

# --- Check NVIDIA driver on Windows ---
$nvidiaSmi = Get-Command "nvidia-smi" -ErrorAction SilentlyContinue
if (-not $nvidiaSmi) {
    # Try default path
    $defaultPath = "C:\Windows\System32\nvidia-smi.exe"
    if (Test-Path $defaultPath) {
        $nvidiaSmi = $defaultPath
    } else {
        Write-Host "[FAIL] nvidia-smi not found. Install NVIDIA driver 560+ from nvidia.com" -ForegroundColor Red
        exit 1
    }
}
$driverInfo = & nvidia-smi --query-gpu=driver_version,name,memory.total --format=csv,noheader 2>&1
Write-Host "[OK] NVIDIA driver found: $driverInfo" -ForegroundColor Green

# ============================================================
# PHASE 1: Install WSL2
# ============================================================
Write-Host ""
Write-Host "--- Phase 1: WSL2 Installation ---" -ForegroundColor Yellow

$wslInstalled = $false
try {
    $wslStatus = wsl --status 2>&1
    if ($LASTEXITCODE -eq 0) {
        $wslInstalled = $true
    }
} catch {
    $wslInstalled = $false
}

if ($wslInstalled) {
    Write-Host "[OK] WSL2 already installed" -ForegroundColor Green
} else {
    Write-Host "[>>] Installing WSL2 (this may take a few minutes)..." -ForegroundColor Cyan
    wsl --install --no-distribution
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[FAIL] WSL2 installation failed. Reboot and retry." -ForegroundColor Red
        Write-Host "       If virtualization is disabled, enable it in BIOS." -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] WSL2 installed. A reboot MAY be required." -ForegroundColor Green
    Write-Host "[WARN] If this is the first WSL install, reboot now and re-run this script." -ForegroundColor Yellow
}

# --- Check if Ubuntu 24.04 is installed ---
$distros = wsl --list --quiet 2>&1
$hasUbuntu = $false
if ($distros) {
    foreach ($d in $distros) {
        $clean = $d -replace "`0", ""  # Remove null chars from wsl output
        if ($clean -match "Ubuntu-24.04") {
            $hasUbuntu = $true
            break
        }
    }
}

if ($hasUbuntu) {
    Write-Host "[OK] Ubuntu-24.04 already installed" -ForegroundColor Green
} else {
    Write-Host "[>>] Installing Ubuntu 24.04 (downloads ~600MB)..." -ForegroundColor Cyan
    wsl --install -d Ubuntu-24.04
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[FAIL] Ubuntu 24.04 installation failed." -ForegroundColor Red
        Write-Host "       Try manually: wsl --install -d Ubuntu-24.04" -ForegroundColor Red
        exit 1
    }
    Write-Host "[OK] Ubuntu 24.04 installed" -ForegroundColor Green
    Write-Host ""
    Write-Host "[WARN] Ubuntu will open a terminal to create your user account." -ForegroundColor Yellow
    Write-Host "       Create a username and password, then close that terminal." -ForegroundColor Yellow
    Write-Host "       Then re-run this script to continue setup." -ForegroundColor Yellow
    Write-Host ""
    exit 0
}

# --- Set Ubuntu 24.04 as default ---
wsl --set-default Ubuntu-24.04 2>$null

# ============================================================
# PHASE 2: CUDA + Python + vLLM inside WSL
# ============================================================
Write-Host ""
Write-Host "--- Phase 2: CUDA + Python + vLLM (inside WSL) ---" -ForegroundColor Yellow

# Test CUDA passthrough first
Write-Host "[>>] Testing CUDA passthrough..." -ForegroundColor Cyan
$cudaTest = wsl -d Ubuntu-24.04 -- nvidia-smi 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[FAIL] nvidia-smi failed inside WSL. CUDA passthrough not working." -ForegroundColor Red
    Write-Host "       Ensure you have NVIDIA driver 560+ on Windows (NOT inside WSL)." -ForegroundColor Red
    Write-Host "       Do NOT install nvidia-driver inside WSL -- passthrough handles it." -ForegroundColor Red
    Write-Host "       Output: $cudaTest" -ForegroundColor DarkGray
    exit 1
}
Write-Host "[OK] CUDA passthrough working" -ForegroundColor Green

# Build the setup script to run inside WSL
$wslSetupScript = @'
#!/bin/bash
set -e

echo "[>>] Updating apt packages..."
sudo apt-get update -qq
sudo apt-get install -y -qq software-properties-common curl wget git

# --- Python 3.12 ---
echo "[>>] Installing Python 3.12..."
if command -v python3.12 &>/dev/null; then
    echo "[OK] Python 3.12 already installed"
else
    sudo add-apt-repository -y ppa:deadsnakes/ppa
    sudo apt-get update -qq
    sudo apt-get install -y -qq python3.12 python3.12-venv python3.12-dev
fi

# --- CUDA toolkit (runtime only -- driver comes from Windows) ---
echo "[>>] Installing CUDA toolkit 12.8..."
if dpkg -l | grep -q cuda-toolkit-12-8; then
    echo "[OK] CUDA toolkit 12.8 already installed"
else
    # Add NVIDIA CUDA repo for Ubuntu 24.04
    wget -q https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb -O /tmp/cuda-keyring.deb
    sudo dpkg -i /tmp/cuda-keyring.deb
    sudo apt-get update -qq
    sudo apt-get install -y -qq cuda-toolkit-12-8
    rm -f /tmp/cuda-keyring.deb
fi

# --- vLLM virtual environment ---
echo "[>>] Setting up vLLM virtual environment..."
VENV_DIR="$HOME/.venvs/vllm"
if [ -d "$VENV_DIR" ]; then
    echo "[OK] vLLM venv exists at $VENV_DIR"
else
    python3.12 -m venv "$VENV_DIR"
    echo "[OK] Created venv at $VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

echo "[>>] Installing/upgrading pip..."
pip install --upgrade pip -q

echo "[>>] Installing vLLM (this may take 5-10 minutes)..."
pip install vllm -q

echo "[>>] Installing HuggingFace hub (for model downloads)..."
pip install huggingface-hub -q

# --- Verify installations ---
echo ""
echo "=== Verification ==="

echo -n "Python: "
python3 --version

echo -n "CUDA toolkit: "
if command -v nvcc &>/dev/null; then
    nvcc --version | grep "release" | head -1
else
    echo "[WARN] nvcc not in PATH (runtime-only install is fine for vLLM)"
fi

echo -n "nvidia-smi: "
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader

echo -n "vLLM: "
python3 -c "import vllm; print(vllm.__version__)"

echo -n "PyTorch CUDA: "
python3 -c "import torch; print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, device={torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"

echo ""
echo "[OK] All components installed successfully"
echo ""
echo "To start vLLM server, run from Windows PowerShell:"
echo "  powershell -File boot/vllm_server.ps1"
'@

# Write the setup script to a temp file accessible from WSL
$wslTmpDir = "$env:TEMP\cex_vllm_setup"
if (-not (Test-Path $wslTmpDir)) {
    New-Item -ItemType Directory -Path $wslTmpDir -Force | Out-Null
}
$wslSetupPath = "$wslTmpDir\setup_vllm.sh"
$wslSetupScript | Out-File -FilePath $wslSetupPath -Encoding ascii -NoNewline

# Convert Windows path to WSL path
$wslMountPath = $wslSetupPath -replace "\\", "/" -replace "^([A-Z]):", '/mnt/$1'
$wslMountPath = $wslMountPath.Substring(0,5).ToLower() + $wslMountPath.Substring(5)

Write-Host "[>>] Running setup inside WSL (this takes 5-15 minutes)..." -ForegroundColor Cyan
Write-Host "     Log: watch the output below" -ForegroundColor DarkGray
Write-Host ""

wsl -d Ubuntu-24.04 -- bash "$wslMountPath"
$setupExitCode = $LASTEXITCODE

# Clean up
Remove-Item $wslTmpDir -Recurse -Force -ErrorAction SilentlyContinue

if ($setupExitCode -ne 0) {
    Write-Host ""
    Write-Host "[FAIL] WSL setup script failed (exit code: $setupExitCode)" -ForegroundColor Red
    Write-Host "       Check the output above for errors." -ForegroundColor Red
    exit 1
}

# ============================================================
# PHASE 3: Final Report
# ============================================================
Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  CEX vLLM Setup Complete" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Stack installed:" -ForegroundColor White
Write-Host "    WSL2 ......... Ubuntu 24.04" -ForegroundColor White
Write-Host "    CUDA ......... 12.8 (passthrough from Windows driver)" -ForegroundColor White
Write-Host "    Python ....... 3.12" -ForegroundColor White
Write-Host "    vLLM ......... latest (in ~/.venvs/vllm)" -ForegroundColor White
Write-Host ""
Write-Host "  Next steps:" -ForegroundColor Yellow
Write-Host "    1. Download a base model (first server start does this)" -ForegroundColor White
Write-Host "    2. Start the server:" -ForegroundColor White
Write-Host "       powershell -File boot/vllm_server.ps1" -ForegroundColor Cyan
Write-Host "    3. Test the API:" -ForegroundColor White
Write-Host "       curl http://localhost:8000/v1/models" -ForegroundColor Cyan
Write-Host ""
Write-Host "  LoRA adapters expected at:" -ForegroundColor Yellow
Write-Host "    _data/ft/adapters/cex-n0X-qlora/" -ForegroundColor White
Write-Host "    (train with Unsloth or PEFT, then place here)" -ForegroundColor DarkGray
Write-Host ""
