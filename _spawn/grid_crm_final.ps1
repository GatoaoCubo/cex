param()

$root = Split-Path $PSScriptRoot -Parent
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Grid {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

# --- Kill previous spawns ---
if (Test-Path $pidFile) {
    Get-Content $pidFile | ForEach-Object {
        $spawnPid = ($_ -split ' ')[0]
        if ($spawnPid -match '^\d+$') {
            try { Stop-Process -Id $spawnPid -Force -ErrorAction SilentlyContinue } catch {}
        }
    }
    Write-Host "[CLEANUP] Previous spawns killed" -ForegroundColor DarkGray
}

$positions = @(
    @{x=0;    y=0;    w=640; h=1040},
    @{x=640;  y=0;    w=640; h=1040},
    @{x=1280; y=0;    w=640; h=1040}
)

$bootFiles = @(
    "n01_batch_a.cmd",
    "n01_batch_b.cmd",
    "n01_batch_f.cmd"
)

$labels = @(
    "BATCH_A Diretorios Pet",
    "BATCH_B Google Maps",
    "BATCH_F CNAE Deep"
)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CRM_FULL_HARVEST - WAVE FINAL GRID   " -ForegroundColor Cyan
Write-Host "  3x N01 paralelos - Base: 244 contatos" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

New-Item -ItemType Directory -Force -Path "$root\.cex\runtime\pids" | Out-Null
"" | Out-File -FilePath $pidFile -Encoding utf8

for ($i = 0; $i -lt $bootFiles.Count; $i++) {
    $bootName = $bootFiles[$i]
    $label = $labels[$i]
    $pos = $positions[$i]
    $bootPath = "$root\boot\$bootName"

    if (-not (Test-Path $bootPath)) {
        Write-Host "  [SLOT $i] SKIP - $bootPath not found" -ForegroundColor Red
        continue
    }

    Write-Host "  [SLOT $i] $label" -ForegroundColor Green

    $proc = Start-Process cmd -ArgumentList "/k `"$bootPath`"" -WorkingDirectory $root -PassThru
    Start-Sleep -Seconds 4

    if ($proc -and $proc.MainWindowHandle) {
        [Win32Grid]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, $pos.w, $pos.h, $true) | Out-Null
        Write-Host "           Window positioned OK" -ForegroundColor DarkGreen
    }

    "$($proc.Id) n01 claude $bootName" | Add-Content $pidFile
    Write-Host "           PID:$($proc.Id) at ($($pos.x),$($pos.y))" -ForegroundColor DarkGray
    Write-Host ""

    Start-Sleep -Seconds 2
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  3/3 SLOTS DISPATCHED                  " -ForegroundColor Cyan
Write-Host "  Monitor: dir .cex\runtime\signals\    " -ForegroundColor Cyan
Write-Host "  Merge:   python N01_research\output\data\merge_batches.py --all" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
