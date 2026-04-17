# boot/_shared/worktree_helpers.ps1
# BORIS_MERGE D2 -- shared helpers for --worktree across 4 runtimes (claude/codex/gemini/ollama)
# Sourced by boot/n0X*.ps1 wrappers.

function Resolve-CexWorktreeDir {
    param(
        [string]$WorktreeId,
        [string]$RepoRoot
    )
    if (-not $WorktreeId) { return $RepoRoot }

    $dir = Join-Path $RepoRoot ".cex/worktrees/$WorktreeId"

    if (-not (Test-Path $dir)) {
        Write-Host "[BOOT] creating worktree: $dir"
        $branch = "worktree/$WorktreeId"
        Push-Location $RepoRoot
        try {
            git worktree add -b $branch $dir HEAD 2>&1 | Out-Null
        } finally {
            Pop-Location
        }
    }

    return $dir
}

function Enter-CexWorktree {
    param(
        [string]$WorktreeDir
    )
    if (-not $WorktreeDir) { return }
    if (-not (Test-Path $WorktreeDir)) {
        Write-Warning "[BOOT] worktree missing: $WorktreeDir -- falling back to repo root"
        return
    }
    Set-Location $WorktreeDir
    $env:CEX_WORKTREE_DIR = $WorktreeDir
    Write-Host "[BOOT] entered worktree: $WorktreeDir"
}

function Initialize-CexAutoAccept {
    param(
        [int]$AutoAccept = 0
    )
    if ($AutoAccept -eq 1) {
        $env:CEX_AUTO_ACCEPT = "1"
        Write-Host "[BOOT] auto-accept ENABLED -- handoff manifest is authoritative"
    } else {
        Remove-Item Env:\CEX_AUTO_ACCEPT -ErrorAction SilentlyContinue
    }
}
