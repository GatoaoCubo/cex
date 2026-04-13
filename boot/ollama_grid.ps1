# CEX Ollama Grid -- Launch 6 nuclei (N01-N06) using Aider + Ollama
# Zero-cost local inference grid. Requires: Ollama running, aider installed.
#
# Usage:
#   powershell -File boot/ollama_grid.ps1
#   $env:OLLAMA_MODEL = "qwen3:14b"; powershell -File boot/ollama_grid.ps1
#
# Layout: 3 columns x 2 rows (same as spawn_grid.ps1)
# PID tracking: .cex/runtime/pids/ollama_grid_pids.txt

$cexRoot = Split-Path -Parent $PSScriptRoot
Set-Location $cexRoot

# --- Config ---
$ollamaModel = if ($env:OLLAMA_MODEL) { $env:OLLAMA_MODEL } else { "gemma4:26b" }
$sessionId = "ollama-" + [System.Guid]::NewGuid().ToString().Substring(0, 8)
$runtimeDir = "$cexRoot\.cex\runtime"
$pidFile = "$runtimeDir\pids\ollama_grid_pids.txt"

# Ensure dirs exist
New-Item -ItemType Directory -Force -Path "$runtimeDir\pids" | Out-Null
New-Item -ItemType Directory -Force -Path "$runtimeDir\tmp" | Out-Null
"" | Set-Content $pidFile -Encoding utf8

# --- Pre-flight: check Ollama is running ---
Write-Host ""
Write-Host "  === CEX OLLAMA GRID ===" -ForegroundColor Cyan
Write-Host "  Model: ollama/$ollamaModel" -ForegroundColor DarkGray
Write-Host "  Session: $sessionId" -ForegroundColor DarkGray
Write-Host "  Cost: $0.00 (local inference)" -ForegroundColor Green
Write-Host ""

Write-Host "  [>>] Pre-flight: checking Ollama..." -ForegroundColor DarkGray
$ollamaOk = $false
try {
    $resp = Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 5 -EA Stop
    $ollamaOk = $true
    $available = $resp.models | ForEach-Object { $_.name }
    Write-Host "  [OK] Ollama responding. Models: $($available -join ', ')" -ForegroundColor Green

    # Check requested model
    $modelFound = ($available -contains $ollamaModel) -or ($available -contains "${ollamaModel}:latest")
    if (-not $modelFound) {
        # Try fallback
        $fallback = "qwen3:14b"
        $fallbackFound = ($available -contains $fallback) -or ($available -contains "${fallback}:latest")
        if ($fallbackFound) {
            Write-Host "  [WARN] $ollamaModel not found. Falling back to $fallback" -ForegroundColor Yellow
            $ollamaModel = $fallback
        } else {
            Write-Host "  [FAIL] Neither $ollamaModel nor $fallback found in Ollama" -ForegroundColor Red
            Write-Host "  Pull a model first: ollama pull $ollamaModel" -ForegroundColor Red
            return
        }
    } else {
        Write-Host "  [OK] $ollamaModel available" -ForegroundColor Green
    }
} catch {
    Write-Host "  [FAIL] Ollama not responding at localhost:11434" -ForegroundColor Red
    Write-Host "  Start Ollama first: ollama serve" -ForegroundColor Red
    return
}

# --- Pre-flight: check aider ---
$aiderPath = Get-Command aider -EA SilentlyContinue
if (-not $aiderPath) {
    Write-Host "  [FAIL] aider not found in PATH" -ForegroundColor Red
    Write-Host "  Install: pip install aider-chat" -ForegroundColor Red
    return
}
Write-Host "  [OK] aider found: $($aiderPath.Source)" -ForegroundColor Green

# --- Set OLLAMA_NUM_PARALLEL for concurrent inference ---
$env:OLLAMA_NUM_PARALLEL = "6"
Write-Host "  [OK] OLLAMA_NUM_PARALLEL=6 (concurrent inference enabled)" -ForegroundColor Green

# --- Propagate model to nuclei via env ---
$env:OLLAMA_MODEL = $ollamaModel

Write-Host ""

# --- Window layout: 3x2 grid ---
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32OllamaGrid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$cols = 3; $rows = 2
$cellW = [math]::Floor($screen.Width / $cols)
$cellH = [math]::Floor($screen.Height / $rows)

# --- Nucleus definitions ---
$nuclei = @(
    @{id="n01"; name="Research";    color="Green";   boot="boot\n01_ollama.ps1"}
    @{id="n02"; name="Marketing";   color="Magenta"; boot="boot\n02_ollama.ps1"}
    @{id="n03"; name="Builder";     color="Blue";    boot="boot\n03_ollama.ps1"}
    @{id="n04"; name="Knowledge";   color="Cyan";    boot="boot\n04_ollama.ps1"}
    @{id="n05"; name="Operations";  color="Red";     boot="boot\n05_ollama.ps1"}
    @{id="n06"; name="Commercial";  color="Yellow";  boot="boot\n06_ollama.ps1"}
)

# --- Check handoffs exist ---
$handoffCount = 0
foreach ($nuc in $nuclei) {
    $hf = "$cexRoot\.cex\runtime\handoffs\$($nuc.id)_task.md"
    if (Test-Path $hf) { $handoffCount++ }
}
if ($handoffCount -eq 0) {
    Write-Host "  [WARN] No handoff files found in .cex/runtime/handoffs/" -ForegroundColor Yellow
    Write-Host "  Nuclei will boot but have no tasks. Write handoffs first." -ForegroundColor Yellow
    Write-Host ""
}

# --- Launch all 6 nuclei ---
$launched = 0
foreach ($nuc in $nuclei) {
    $idx = $launched
    $bootPath = "$cexRoot\$($nuc.boot)"

    if (-not (Test-Path $bootPath)) {
        Write-Host "  [FAIL] Missing: $($nuc.boot)" -ForegroundColor Red
        continue
    }

    # Set CEX_GRID env so boot scripts skip window sizing (we control layout)
    $env:CEX_GRID = "1"

    $proc = Start-Process powershell -ArgumentList @(
        "-NoProfile", "-NoExit", "-ExecutionPolicy", "Bypass",
        "-File", $bootPath
    ) -WorkingDirectory $cexRoot -PassThru

    # Position in 3x2 grid
    $col = $idx % $cols
    $row = [math]::Floor($idx / $cols)
    $x = $screen.X + ($col * $cellW)
    $y = $screen.Y + ($row * $cellH)

    # Wait for window handle
    $hwnd = [IntPtr]::Zero
    for ($i = 0; $i -lt 10; $i++) {
        Start-Sleep -Milliseconds 200
        try { $proc.Refresh() } catch {}
        $hwnd = $proc.MainWindowHandle
        if ($hwnd -ne [IntPtr]::Zero) { break }
    }
    if ($hwnd -ne [IntPtr]::Zero) {
        [Win32OllamaGrid]::MoveWindow($hwnd, $x, $y, $cellW, $cellH, $true) | Out-Null
    }

    # Record PID
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$($proc.Id) $($nuc.id) aider $sessionId $timestamp" | Add-Content $pidFile -Encoding utf8

    $launched++
    $hfStatus = if (Test-Path "$cexRoot\.cex\runtime\handoffs\$($nuc.id)_task.md") { "task" } else { "idle" }
    Write-Host "  [$launched/6] $($nuc.id.ToUpper()) $($nuc.name) PID=$($proc.Id) grid=($col,$row) [$hfStatus]" -ForegroundColor $nuc.color
}

# Clear CEX_GRID so it does not leak to the orchestrator shell
$env:CEX_GRID = ""

Write-Host ""
Write-Host "  === ALL $launched OLLAMA NUCLEI LAUNCHED ===" -ForegroundColor Cyan
Write-Host "  Session: $sessionId" -ForegroundColor DarkGray
Write-Host "  PIDs: $pidFile" -ForegroundColor DarkGray
Write-Host "  Model: ollama/$ollamaModel" -ForegroundColor DarkGray
Write-Host "  OLLAMA_NUM_PARALLEL: 6" -ForegroundColor DarkGray
Write-Host "  Handoffs: $handoffCount/6 nuclei have tasks" -ForegroundColor DarkGray
Write-Host ""
Write-Host "  Monitor: git log --oneline --since='5 minutes ago'" -ForegroundColor DarkGray
Write-Host "  Stop all: Get-Content $pidFile | ForEach-Object { taskkill /F /PID `$(`$_ -split ' ')[0] /T }" -ForegroundColor DarkGray
Write-Host ""
