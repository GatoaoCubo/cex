# spawn_grid_ollama.ps1 - Interactive 3x2 grid of Ollama-powered nuclei
#
# Spawns 6 PowerShell windows positioned 3 cols x 2 rows on primary monitor.
# Each window runs boot/n0x_ollama.ps1 with the matching handoff.
# User can observe + interact in each window in real-time.

param(
    [string]$Mission = "LEVERAGE_MAP_V2",
    [string]$Model = "llama3.1:8b",
    [string[]]$Nuclei = @("n01","n02","n03","n04","n05","n06"),
    [int]$MaxIters = 15,
    [int]$RequireReads = 2,
    [string]$OutputTag = "",
    [hashtable]$ModelMap = $null
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path "$PSScriptRoot\.."
Set-Location $RepoRoot

# Win32 API for window positioning
$signature = @'
[DllImport("user32.dll")]
public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int nWidth, int nHeight, bool bRepaint);

[DllImport("user32.dll")]
public static extern bool SetForegroundWindow(IntPtr hWnd);
'@
if (-not ("Win32.Window" -as [type])) {
    Add-Type -MemberDefinition $signature -Name Window -Namespace Win32
}

# Detect primary monitor size
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
$screenW = $screen.Width
$screenH = $screen.Height

$cols = 3
$rows = 2
$cellW = [int]($screenW / $cols)
$cellH = [int]($screenH / $rows)

Write-Host "============================================================"
Write-Host "  CEX Grid Ollama - $Mission"
Write-Host "  Monitor: ${screenW}x${screenH}  Layout: ${cols}x${rows}"
Write-Host "  Cell:    ${cellW}x${cellH}"
Write-Host "  Model:   $Model"
Write-Host "  Nuclei:  $($Nuclei -join ',')"
Write-Host "============================================================"

# Position map: 3 cols x 2 rows, top-to-bottom left-to-right
$positions = @{
    "n01" = @{ Col=0; Row=0 }
    "n02" = @{ Col=1; Row=0 }
    "n03" = @{ Col=2; Row=0 }
    "n04" = @{ Col=0; Row=1 }
    "n05" = @{ Col=1; Row=1 }
    "n06" = @{ Col=2; Row=1 }
}

$handoffDir = Join-Path $RepoRoot ".cex\runtime\handoffs"
$outputSubdir = $Mission.ToLower()
if ($OutputTag) { $outputSubdir = "$outputSubdir`_$OutputTag" }
$outputDir  = Join-Path $RepoRoot "_reports\$outputSubdir"
$pidFile    = Join-Path $RepoRoot ".cex\runtime\pids\grid_ollama_$Mission.txt"
$pidDir     = Split-Path $pidFile -Parent
if (-not (Test-Path $pidDir)) { New-Item -ItemType Directory -Path $pidDir | Out-Null }
if (-not (Test-Path $outputDir)) { New-Item -ItemType Directory -Path $outputDir | Out-Null }
"# Grid Ollama PIDs - $Mission - $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ss')" | Set-Content -Encoding ASCII $pidFile

$sessionId = [guid]::NewGuid().ToString().Substring(0,8)

foreach ($n in $Nuclei) {
    $pos = $positions[$n]
    if (-not $pos) {
        Write-Warning "No position for $n, skipping"
        continue
    }

    $handoffPath = Join-Path $handoffDir "${Mission}_${n}.md"
    $outputPath  = Join-Path $outputDir "${Mission}_${n}.md"

    if (-not (Test-Path $handoffPath)) {
        Write-Warning "Handoff missing: $handoffPath - skipping $n"
        continue
    }

    $bootScript = Join-Path $RepoRoot "boot\n0x_ollama.ps1"

    # Per-nucleus model (ModelMap overrides -Model)
    $nucModel = $Model
    if ($ModelMap -and $ModelMap.ContainsKey($n)) {
        $nucModel = $ModelMap[$n]
    }

    # Build the command for the new window
    $psArgs = "-NoExit -NoProfile -ExecutionPolicy Bypass -File `"$bootScript`" " +
              "-Nucleus $n -Handoff `"$handoffPath`" -Output `"$outputPath`" " +
              "-Mission $Mission -Model $nucModel -MaxIters $MaxIters -RequireReads $RequireReads"

    # Launch (Start-Process returns immediately)
    $proc = Start-Process -FilePath "powershell.exe" -ArgumentList $psArgs -PassThru -WindowStyle Normal

    # Wait a moment for the window handle to be ready
    Start-Sleep -Milliseconds 700

    # Position the window
    $x = $pos.Col * $cellW
    $y = $pos.Row * $cellH

    # The wrapper PID has the window; get its handle after small wait
    try {
        # Refresh process to get MainWindowHandle
        $refreshed = Get-Process -Id $proc.Id -ErrorAction SilentlyContinue
        if ($refreshed -and $refreshed.MainWindowHandle -ne 0) {
            [Win32.Window]::MoveWindow($refreshed.MainWindowHandle, $x, $y, $cellW, $cellH, $true) | Out-Null
            Write-Host "  [$n] pid=$($proc.Id) model=$nucModel pos=($x,$y) size=${cellW}x${cellH}"
        } else {
            Write-Host "  [$n] pid=$($proc.Id) model=$nucModel (window handle not ready; manual reposition may be needed)"
        }
    } catch {
        Write-Warning "  [$n] position failed: $_"
    }

    # Record PID
    "$($proc.Id) $n ollama $sessionId $(Get-Date -Format o)" | Add-Content -Encoding ASCII $pidFile
}

Write-Host ""
Write-Host "============================================================"
Write-Host "  Grid spawned. PID file: $pidFile"
Write-Host "  Each window runs agentic loop then drops to REPL."
Write-Host "  Type :quit in any window to close it."
Write-Host "  When all 6 commits land, run: /consolidate"
Write-Host "============================================================"
