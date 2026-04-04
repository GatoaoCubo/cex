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

$positions = @(
    @{x=0;    y=0;    w=960; h=1040}
)

$bootFiles = @(
    "n01_crm_templates.cmd"
)

$labels = @(
    "N01 CRM Templates Research"
)

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  CRM TEMPLATES RESEARCH                " -ForegroundColor Cyan
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
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DISPATCHED                            " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
