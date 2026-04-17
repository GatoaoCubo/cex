# CEX Aider Grid -- PowerShell Visual Mode (3x2 layout)
# Opens 1 window per nucleus with aider + ollama, tiled 3 columns x 2 rows
#
# Usage: powershell -File _spawn\spawn_grid_aider.ps1 -mission MISSION
#        (or via: bash _spawn/dispatch.sh grid-aider MISSION)

param(
    [string]$mission = "GRID",
    [string]$model = "ollama_chat/qwen3:8b",
    [string[]]$nuclei = @("n01","n02","n03","n04","n05","n06")
)

$CEX_ROOT = Split-Path -Parent $PSScriptRoot
$pidFile = Join-Path $CEX_ROOT ".cex\runtime\pids\spawn_pids_aider.txt"
$tmpDir = Join-Path $env:TEMP "cex_aider"
New-Item -ItemType Directory -Path $tmpDir -Force | Out-Null

# --- Window positioning (3 columns x 2 rows) ---
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool repaint);
    [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
}
"@

# Screen dimensions
Add-Type -AssemblyName System.Windows.Forms
$screenW = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea.Width
$screenH = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea.Height
$cols = 3
$rows = 2
$cellW = [int]($screenW / $cols)
$cellH = [int]($screenH / $rows)

# Grid positions: [col, row] for each nucleus slot
$positions = @(
    @(0, 0), # N01: top-left
    @(1, 0), # N02: top-center
    @(2, 0), # N03: top-right
    @(0, 1), # N04: bottom-left
    @(1, 1), # N05: bottom-center
    @(2, 1)  # N06: bottom-right
)

# Nucleus display colors (foreground only, no background fill)
$nucColors = @{
    "n01" = "Green"
    "n02" = "Magenta"
    "n03" = "Cyan"
    "n04" = "Yellow"
    "n05" = "Red"
    "n06" = "White"
}

Write-Host ""
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host "  CEX Aider Grid: $mission" -ForegroundColor Cyan
Write-Host "  Layout: 3x2 | Model: $model | Cost: `$0" -ForegroundColor Green
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host ""

# Clear pid file
"" | Out-File $pidFile -Encoding utf8

$slot = 0
$launched = @()

foreach ($nuc in $nuclei) {
    $taskFile = Join-Path $CEX_ROOT "${nuc}_task.md"

    if (-not (Test-Path $taskFile)) {
        Write-Host "  [$($nuc.ToUpper())] SKIP" -ForegroundColor DarkGray
        $slot++
        continue
    }

    $color = $nucColors[$nuc]
    if (-not $color) { $color = "White" }
    $title = "$($nuc.ToUpper()) [AIDER] $mission"

    # Write temp launcher
    $launcher = Join-Path $tmpDir "launch_${nuc}.ps1"
    @"
`$env:OLLAMA_API_BASE = 'http://localhost:11434'
Set-Location '$CEX_ROOT'
`$Host.UI.RawUI.WindowTitle = '$title'
`$Host.UI.RawUI.ForegroundColor = '$color'
Write-Host ''
Write-Host '  $($nuc.ToUpper()) -- Aider + Ollama' -ForegroundColor $color
Write-Host '  Task: ${nuc}_task.md' -ForegroundColor Gray
Write-Host ''
aider --model $model --subtree-only --yes-always --auto-commits --no-show-model-warnings --no-suggest-shell-commands --commit-language english --file ${nuc}_task.md --read CLAUDE.md --message 'Read the task file and execute every task described. Create all requested files. Always write in English.'
Write-Host ''
Write-Host '  [DONE] $($nuc.ToUpper()) finished.' -ForegroundColor Green
Write-Host '  Press any key to close...' -ForegroundColor DarkGray
`$null = `$Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
"@ | Out-File $launcher -Encoding utf8

    $proc = Start-Process powershell -ArgumentList "-ExecutionPolicy","Bypass","-File",$launcher -PassThru
    "$($proc.Id) $nuc aider s_aider $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')" | Add-Content $pidFile -Encoding utf8

    # Position the window in 3x2 grid (retry until handle available)
    $pos = $positions[$slot]
    $x = $pos[0] * $cellW
    $y = $pos[1] * $cellH
    for ($retry = 0; $retry -lt 10; $retry++) {
        Start-Sleep -Milliseconds 300
        $proc.Refresh()
        $hwnd = $proc.MainWindowHandle
        if ($hwnd -ne [IntPtr]::Zero) {
            [Win32]::MoveWindow($hwnd, $x, $y, $cellW, $cellH, $true) | Out-Null
            break
        }
    }

    $launched += $nuc
    Write-Host "  [$($nuc.ToUpper())] PID:$($proc.Id) @ col=$($pos[0]) row=$($pos[1])" -ForegroundColor $color
    $slot++
}

Write-Host ""
Write-Host "  Grid: $($launched.Count)/6 nuclei launched in 3x2 layout" -ForegroundColor Cyan
Write-Host "  Kill: Get-Process powershell | Where { `$_.MainWindowTitle -match 'AIDER' } | Stop-Process -Force" -ForegroundColor DarkGray
Write-Host ""
