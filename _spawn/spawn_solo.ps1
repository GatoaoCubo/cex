# CEX Spawn Solo v1.0 — Launch single nucleus builder
param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('n03','n01','n02','n04','n05','n06')]
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

$root = Split-Path $PSScriptRoot -Parent
$pos = $grid[$nucleus]
$upper = $nucleus.ToUpper()
$handoffDir = "$root\.cex\handoffs"
$signalDir = "$root\.cex_signals"
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

# Build boot command
$bootScript = "$root\boot\$nucleus.cmd"
if (-not (Test-Path $bootScript)) {
    Write-Output "[$upper] ERROR: $bootScript not found"
    exit 1
}

$identity = "Voce e $upper Builder. Leia CLAUDE.md. Execute tarefas de .cex/handoffs/. Commit e signal ao terminar."
if ($task) {
    $identity = "$identity TAREFA: $task"
}

$proc = Start-Process cmd -ArgumentList "/k `"$bootScript`" `"$identity`"" -WorkingDirectory $root -PassThru
Start-Sleep -Seconds 3

# Position window
if ($proc -and $pos) {
    [Win32]::MoveWindow($proc.MainWindowHandle, $pos.x, $pos.y, 640, 520, $true) | Out-Null
}

# Record PID
"$($proc.Id) $nucleus" | Add-Content $pidFile
Write-Output "[$upper] Spawned PID:$($proc.Id) at ($($pos.x),$($pos.y))"
