param()

$root = Split-Path $PSScriptRoot -Parent
$handoffDir = "$root\.cex\runtime\handoffs"
$missionDir = "$handoffDir\crm_mission"
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Grid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

$positions = @(
    @{x=0;    y=0;    w=640; h=520},
    @{x=640;  y=0;    w=640; h=520},
    @{x=1280; y=0;    w=640; h=520},
    @{x=0;    y=520;  w=640; h=520},
    @{x=640;  y=520;  w=640; h=520},
    @{x=1280; y=520;  w=640; h=520}
)

$batchFiles = @(
    "batch_a_diretorios_pet",
    "batch_b_google_maps",
    "batch_c_social_discovery",
    "batch_d_marketplaces",
    "batch_e_reputation",
    "batch_f_cnae_deep"
)

$batchLabels = @(
    "BATCH_A Diretorios Pet",
    "BATCH_B Google Maps",
    "BATCH_C Social IG/FB",
    "BATCH_D Marketplaces",
    "BATCH_E Reputacao",
    "BATCH_F CNAE Deep"
)

$bootScript = "$root\boot\n01.cmd"

Write-Host ""
Write-Host "  CEX GRID - CRM_FULL_HARVEST - 6 SLOTS" -ForegroundColor Cyan
Write-Host "  Model: Claude Opus 4 x 6 parallel" -ForegroundColor Cyan
Write-Host ""

New-Item -ItemType Directory -Force -Path "$root\.cex\runtime\pids" | Out-Null

for ($i = 0; $i -lt $batchFiles.Count; $i++) {
    $batchName = $batchFiles[$i]
    $label = $batchLabels[$i]
    $pos = $positions[$i]
    $slotLetter = [char]([int][char]'A' + $i)

    $batchPath = "$missionDir\$batchName.md"
    if (-not (Test-Path $batchPath)) {
        Write-Host "  [SLOT $slotLetter] SKIP - $batchPath not found" -ForegroundColor Red
        continue
    }

    $content = Get-Content $batchPath -Raw
    Set-Content -Path "$handoffDir\n01_task.md" -Value $content -Encoding UTF8

    Write-Host "  [SLOT $slotLetter] $label" -ForegroundColor Green

    $proc = Start-Process cmd -ArgumentList "/k `"$bootScript`"" -WorkingDirectory $root -PassThru
    Start-Sleep -Seconds 3

    if ($proc -and $proc.MainWindowHandle) {
        [Win32Grid]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, $pos.w, $pos.h, $true) | Out-Null
    }

    "$($proc.Id) n01 claude slot_$slotLetter $batchName" | Add-Content $pidFile
    Write-Host "           PID:$($proc.Id) at ($($pos.x),$($pos.y))" -ForegroundColor DarkGray

    if ($i -lt ($batchFiles.Count - 1)) {
        Write-Host "           Waiting 18s for handoff read..." -ForegroundColor DarkGray
        Start-Sleep -Seconds 18
    }
}

Write-Host ""
Write-Host "  6/6 SLOTS DISPATCHED" -ForegroundColor Green
Write-Host "  Monitor: bash _spawn/dispatch.sh status" -ForegroundColor Green
Write-Host "  Stop:    bash _spawn/dispatch.sh stop" -ForegroundColor Green
Write-Host ""
