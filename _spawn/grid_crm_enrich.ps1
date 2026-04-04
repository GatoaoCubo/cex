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
    "n01_enrich_1.cmd",
    "n01_enrich_2.cmd",
    "n01_enrich_3.cmd"
)

$labels = @(
    "ENRICH_1 SCS+Diadema (130)",
    "ENRICH_2 SBC+RibPires (117)",
    "ENRICH_3 SA+Maua+RGS (129)"
)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CRM ENRICHMENT GRID - 376 contatos   " -ForegroundColor Cyan
Write-Host "  3x N01 paralelos - tel/wpp/ig/web     " -ForegroundColor Cyan
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
Write-Host "  3/3 ENRICHMENT SLOTS DISPATCHED       " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
