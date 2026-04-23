param(
    [Parameter(Mandatory=$true)][string]$Nucleus,
    [Parameter(Mandatory=$true)][string]$Handoff,
    [Parameter(Mandatory=$true)][string]$Output,
    [string]$Mission = "TASK",
    [string]$Model = "llama3.1:8b",
    [int]$MaxIters = 15,
    [int]$RequireReads = 2
)
. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI (claude/gemini/codex/ollama)

# Set repo root
$RepoRoot = Resolve-Path "$PSScriptRoot\.."
Set-Location $RepoRoot

# Window title per nucleus
$host.UI.RawUI.WindowTitle = "CEX $($Nucleus.ToUpper()) - $Mission - Ollama/$Model"

# Color per nucleus for visual distinction
$colors = @{
    "n01" = "Cyan"
    "n02" = "Magenta"
    "n03" = "Yellow"
    "n04" = "Green"
    "n05" = "Red"
    "n06" = "Blue"
}
$color = $colors[$Nucleus.ToLower()]
if ($color) { $host.UI.RawUI.ForegroundColor = $color }

Write-Host "============================================================"
Write-Host "  CEX $($Nucleus.ToUpper()) - Ollama Agentic Boot"
Write-Host "  Model:   $Model"
Write-Host "  Mission: $Mission"
Write-Host "  Handoff: $Handoff"
Write-Host "  Output:  $Output"
Write-Host "============================================================"
Write-Host ""

# Run the agentic runner with interactive + auto-commit
python _tools/cex_agentic_nucleus.py `
    --nucleus $Nucleus `
    --handoff $Handoff `
    --output $Output `
    --model $Model `
    --mission $Mission `
    --max-iters $MaxIters `
    --require-reads $RequireReads `
    --auto-commit `
    --interactive

# On exit, log completion
Write-Host ""
Write-Host "=== Nucleus $($Nucleus.ToUpper()) completed. ==="
