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
    @{x=0;    y=0;    w=960; h=1040},
    @{x=960;  y=0;    w=960; h=1040}
)

$bootFiles = @(
    "n05_crm_schema.cmd",
    "n03_crm_frontend.cmd"
)

$labels = @(
    "N05 Schema + Seed (Supabase)",
    "N03 Frontend (Tabs+Table+Map)"
)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CRM ADMIN GRID - 2 nucleos            " -ForegroundColor Cyan
Write-Host "  N05: schema+seed | N03: frontend+mapa " -ForegroundColor Cyan
Write-Host "  Repo: gato-cubo-commerce               " -ForegroundColor Cyan
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

    "$($proc.Id) $bootName" | Add-Content $pidFile
    Write-Host "           PID:$($proc.Id) at ($($pos.x),$($pos.y))" -ForegroundColor DarkGray
    Write-Host ""

    Start-Sleep -Seconds 2
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  2/2 SLOTS DISPATCHED                  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
