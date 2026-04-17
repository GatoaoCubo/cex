# Spawn ONE nucleus in its fixed 3x2 cell, regardless of other running grids.
# Used by cex_showoff.py (Wave 5 mixed) and any future solo-with-layout dispatch.
#
# Usage:
#   powershell -File _spawn/spawn_one_positioned.ps1 -Nucleus n01 -BootScript boot/n01_ollama.ps1
#
# Emits: PID of wrapper powershell on success, blank on failure.

param(
    [Parameter(Mandatory=$true)][string]$Nucleus,
    [Parameter(Mandatory=$true)][string]$BootScript
)

$ErrorActionPreference = "Stop"

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32One {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

Add-Type -AssemblyName System.Windows.Forms
$scr = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$gW = [math]::Floor($scr.Width / 3)
$gH = [math]::Floor($scr.Height / 2)
$gOx = $scr.X; $gOy = $scr.Y

# Fixed 3x2 cell map (same as spawn_grid.ps1 -- DO NOT DIVERGE)
$fixedCells = @{
    "n01" = @{col=0; row=0}
    "n02" = @{col=1; row=0}
    "n03" = @{col=2; row=0}
    "n04" = @{col=0; row=1}
    "n05" = @{col=1; row=1}
    "n06" = @{col=2; row=1}
}

$cell = $fixedCells[$Nucleus.ToLower()]
if (-not $cell) {
    Write-Error "[POS] Unknown nucleus: $Nucleus (expected n01..n06)"
    exit 1
}

$posX = $gOx + $cell.col * $gW
$posY = $gOy + $cell.row * $gH

$root = Split-Path $PSScriptRoot -Parent
$bootPath = if ([System.IO.Path]::IsPathRooted($BootScript)) { $BootScript } else { Join-Path $root $BootScript }

if (-not (Test-Path $bootPath)) {
    Write-Error "[POS] Boot script missing: $bootPath"
    exit 2
}

# Signal boot wrapper to skip self-sizing
$env:CEX_GRID = "1"
$env:CEX_GRID_W = "$gW"
$env:CEX_GRID_H = "$gH"

$proc = Start-Process powershell `
    -ArgumentList "-ExecutionPolicy Bypass -NoExit -File `"$bootPath`"" `
    -WorkingDirectory $root -PassThru -WindowStyle Normal

if (-not $proc) {
    Write-Error "[POS] Start-Process returned null"
    exit 3
}

# Poll for window handle (up to 5s)
$hwnd = [IntPtr]::Zero
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Milliseconds 500
    try { $proc.Refresh() } catch {}
    $hwnd = $proc.MainWindowHandle
    if ($hwnd -ne [IntPtr]::Zero) { break }
}

if ($hwnd -ne [IntPtr]::Zero) {
    [Win32One]::MoveWindow($hwnd, $posX, $posY, $gW, $gH, $true) | Out-Null
    Write-Output "[POS] $Nucleus -> cell ($($cell.col),$($cell.row)) at ${posX}x${posY} ${gW}x${gH} PID:$($proc.Id)"
} else {
    Write-Output "[POS] $Nucleus PID:$($proc.Id) WARN: no hwnd after 5s (not positioned)"
}

# Append to PID file for stop/status tracking
$pidFile = "$root\.cex\runtime\pids\spawn_pids.txt"
$pidDir = Split-Path $pidFile -Parent
if (-not (Test-Path $pidDir)) { New-Item -ItemType Directory -Path $pidDir -Force | Out-Null }
$sessId = if ($env:CEX_SESSION_ID) { $env:CEX_SESSION_ID } else { "s$PID" }
$ts = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
# cli inferred from boot script name (n0X.ps1 -> claude; n0X_gemini.ps1 -> gemini; etc.)
$bootName = [System.IO.Path]::GetFileNameWithoutExtension($bootPath)
$cli = if ($bootName -match "_([a-z]+)$") { $matches[1] } else { "claude" }
"$($proc.Id) $Nucleus $cli $sessId $ts -" | Add-Content $pidFile

exit 0
