# CEX Spawn Solo v2.0 — Multi-CLI: claude + codex + gemini
# Each nucleus uses the BEST CLI for its domain:
#   N03 Builder    → claude opus  (complex construction)
#   N05 Operations → codex        (code review, testing)
#   N04 Knowledge  → gemini       (1M context, RAG)
#   N01 Research   → gemini       (1M context, papers)
#   N02 Marketing  → claude sonnet (creative writing)
#   N06 Commercial → claude sonnet (persuasive copy)

param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('n01','n02','n03','n04','n05','n06')]
    [string]$nucleus,
    [string]$task = "",
    [switch]$interactive
)

Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32 {
    [DllImport("user32.dll")]
    public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int W, int H, bool r);
}
"@

$grid = @{
    n01 = @{x=0;    y=0};    n02 = @{x=640;  y=0}
    n03 = @{x=1280; y=0};    n04 = @{x=0;    y=520}
    n05 = @{x=640;  y=520};  n06 = @{x=1280; y=520}
}

# CLI per nucleus (best tool for the job)
$cliMap = @{
    n01 = 'gemini';   n02 = 'claude'
    n03 = 'claude';   n04 = 'gemini'
    n05 = 'codex';    n06 = 'claude'
}

$root = Split-Path $PSScriptRoot -Parent
$pos = $grid[$nucleus]
$cli = $cliMap[$nucleus]
$upper = $nucleus.ToUpper()
$handoffDir = "$root\.cex\runtime\handoffs"
$signalDir = "$root\.cex/runtime/signals"
$pidFile = "$root\.cex\temp\spawn_pids.txt"

New-Item -ItemType Directory -Force -Path $handoffDir,$signalDir,"$root\.cex\temp" | Out-Null

# Write handoff if task provided
if ($task) {
    $handoffPath = "$handoffDir\${nucleus}_task.md"
    @"
# $upper Builder Task
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFA
$task

## COMMIT
git add -A
git commit -m "[$upper] task complete"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('$nucleus', 'complete', 9.0)"
"@ | Set-Content -Path $handoffPath -Encoding UTF8
    Write-Output "[$upper] Handoff: $handoffPath"
}

# Boot script
$bootScript = "$root\boot\$nucleus.cmd"
if (-not (Test-Path $bootScript)) {
    Write-Output "[$upper] ERROR: $bootScript not found"
    exit 1
}

# Build launch args per CLI type
$shellFlag = if ($interactive) { "/k" } else { "/c" }

if ($task) {
    switch ($cli) {
        'claude' {
            if ($interactive) {
                $bootArgs = "$shellFlag `"$bootScript`" `"$task`""
            } else {
                $bootArgs = "$shellFlag `"$bootScript`" -p `"$task`""
            }
        }
        'codex' {
            $bootArgs = "$shellFlag `"$bootScript`" `"$task`""
        }
        'gemini' {
            if ($interactive) {
                $bootArgs = "$shellFlag `"$bootScript`" `"$task`""
            } else {
                $bootArgs = "$shellFlag `"$bootScript`" -p `"$task`""
            }
        }
    }
} else {
    $bootArgs = "/k `"$bootScript`""
}

# Spawn
$proc = Start-Process cmd -ArgumentList $bootArgs -WorkingDirectory $root -PassThru
Start-Sleep -Seconds 3

# Position window
if ($proc -and $pos) {
    [Win32]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, 640, 520, $true) | Out-Null
}

# Record PID + CLI type
"$($proc.Id) $nucleus $cli" | Add-Content $pidFile
Write-Output "[$upper] Spawned PID:$($proc.Id) CLI:$cli at ($($pos.x),$($pos.y))"
