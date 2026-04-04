# CRM_FULL_HARVEST — Wave Final Grid (Batches A + B + F)
# Usage: powershell -ExecutionPolicy Bypass -File _spawn/grid_crm_final.ps1
param()

$root = Split-Path $PSScriptRoot -Parent
$handoffDir = "$root\.cex\runtime\handoffs\crm_mission"
$runtimeDir = "$root\.cex\runtime"
$pidFile = "$runtimeDir\pids\spawn_pids.txt"

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Grid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

# 3 slots — side by side
$positions = @(
    @{x=0;    y=0;    w=640; h=1040},   # Batch A (left)
    @{x=640;  y=0;    w=640; h=1040},   # Batch B (center)
    @{x=1280; y=0;    w=640; h=1040}    # Batch F (right)
)

$batches = @(
    @{
        id    = "batch_a"
        label = "BATCH_A Diretorios Pet"
        file  = "batch_a_diretorios_pet.md"
        env   = "CEX_NUCLEUS=n01"
    },
    @{
        id    = "batch_b"
        label = "BATCH_B Google Maps"
        file  = "batch_b_google_maps.md"
        env   = "CEX_NUCLEUS=n01"
    },
    @{
        id    = "batch_f"
        label = "BATCH_F CNAE Deep"
        file  = "batch_f_cnae_deep.md"
        env   = "CEX_NUCLEUS=n01"
    }
)

New-Item -ItemType Directory -Force -Path "$runtimeDir\pids" | Out-Null
"" | Out-File -FilePath $pidFile -Encoding utf8

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CRM_FULL_HARVEST — Wave Final Grid   " -ForegroundColor Cyan
Write-Host "  3 batches N01 paralelos               " -ForegroundColor Cyan
Write-Host "  Base: 244 contatos | Meta: 500+       " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$pids = @()

for ($i = 0; $i -lt $batches.Count; $i++) {
    $batch = $batches[$i]
    $pos = $positions[$i]
    $handoffPath = "$handoffDir\$($batch.file)"

    if (-not (Test-Path $handoffPath)) {
        Write-Host "[SKIP] $($batch.label) — handoff not found: $($batch.file)" -ForegroundColor Red
        continue
    }

    # Build the prompt — read handoff content
    $handoffContent = Get-Content -Path $handoffPath -Raw -Encoding utf8
    $prompt = @"
You are N01 Research Analyst for GATO3. Your mission: $($batch.label).

READ THIS HANDOFF CAREFULLY — it contains exact URLs, methods, and output format:
File: .cex/runtime/handoffs/crm_mission/$($batch.file)

CRITICAL RULES:
1. NUNCA inventar dados — campo vazio se nao encontrou
2. FONTE OBRIGATORIA em cada registro (fonte_descoberta)
3. Output: JSON direto em N01_research/output/data/
4. DEDUP contra crm_pet_abc.json (244 contatos existentes)
5. Commit ao final + signal

Start by reading the handoff file, then execute systematically.
"@

    Write-Host "[LAUNCH] $($batch.label)" -ForegroundColor Green
    Write-Host "  Handoff: $handoffPath"
    Write-Host "  Position: $($pos.x),$($pos.y)"

    $proc = Start-Process -FilePath "claude" -ArgumentList "--print", "--dangerously-skip-permissions" -WorkingDirectory $root -PassThru -WindowStyle Normal
    
    if ($proc) {
        $pids += $proc.Id
        "$($proc.Id) $($batch.label)" | Out-File -FilePath $pidFile -Append -Encoding utf8
        Start-Sleep -Milliseconds 500

        # Position window
        try {
            [Win32Grid]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, $pos.w, $pos.h, $true) | Out-Null
        } catch {}

        Write-Host "  PID: $($proc.Id)" -ForegroundColor Yellow
    }

    Start-Sleep -Seconds 2
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  $($pids.Count) batches launched" -ForegroundColor Cyan
Write-Host "  PIDs: $($pids -join ', ')" -ForegroundColor Cyan
Write-Host "  Monitor: bash _spawn/dispatch.sh status" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "When all complete, run:" -ForegroundColor Yellow
Write-Host "  python N01_research/output/data/merge_batches.py --all" -ForegroundColor White
