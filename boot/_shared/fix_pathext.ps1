# Normalize PATHEXT for the current shell BEFORE spawning claude/codex/gemini.
#
# Bug this guards against (Windows-only):
#   If the user's PATHEXT has .PS1 before .CMD (some installers prepend it,
#   notably some Node/PowerShell setups), then npm/npx package binary lookup
#   resolves to the .ps1 shim before the .cmd shim. Spawning a .ps1 via
#   ShellExecute opens it in Notepad by default (Microsoft's anti-malware
#   default for double-click). Result: every npx-based MCP server opens a
#   Notepad window instead of starting.
#
# Fix: in this shell only (does NOT touch the user's persistent env), force
# PATHEXT to the Windows default order (CMD before PS1). The boot script
# inherits this when it spawns claude.exe, so all child MCP spawns use the
# corrected order.
#
# To make it permanent for the user (recommended once detected):
#   [Environment]::SetEnvironmentVariable("PATHEXT",
#     ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC", "User")

$default = ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
$current = $env:PATHEXT
if (-not $current) {
    $env:PATHEXT = $default
    return
}

# Detect the bug: .PS1 listed before .CMD (case-insensitive)
$exts = $current.ToUpper().Split(';') | Where-Object { $_ }
$psIdx = [array]::IndexOf($exts, ".PS1")
$cmdIdx = [array]::IndexOf($exts, ".CMD")
if ($psIdx -ge 0 -and $cmdIdx -ge 0 -and $psIdx -lt $cmdIdx) {
    Write-Host "[boot] PATHEXT has .PS1 before .CMD -- npm/npx shims would open in Notepad." -ForegroundColor Yellow
    Write-Host "[boot] Normalizing PATHEXT for this shell. To fix permanently, run:" -ForegroundColor Yellow
    Write-Host "       [Environment]::SetEnvironmentVariable('PATHEXT','$default','User')" -ForegroundColor DarkYellow
    $env:PATHEXT = $default
}
