<#
.SYNOPSIS
    Launch Chrome with CDP remote debugging for Playwright MCP.
.DESCRIPTION
    Detects Chrome install path, gracefully closes running instance,
    relaunches with --remote-debugging-port for Claude Code browser control.
    Uses YOUR Chrome profile (cookies, sessions, extensions intact).

    IMPORTANT: Log into your accounts AFTER Chrome opens, then enable
    the playwright MCP server in .mcp.json (set disabled: false).
.USAGE
    .\boot\chrome_cdp.ps1                    # default port 9222
    .\boot\chrome_cdp.ps1 -Port 9333         # custom port
    .\boot\chrome_cdp.ps1 -GracefulOnly      # never force-kill
#>
param(
    [int]$Port = 9222,
    [switch]$GracefulOnly
)

# --- Detect Chrome path (no hardcoded paths) ---
$chromePath = $null
$candidates = @(
    (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" -EA SilentlyContinue).'(Default)',
    "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
    "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)
foreach ($c in $candidates) {
    if ($c -and (Test-Path $c)) { $chromePath = $c; break }
}
if (-not $chromePath) {
    Write-Host "[FAIL] Chrome not found. Install Chrome or set path manually." -ForegroundColor Red
    exit 1
}

# --- Detect user data dir ---
$userDataDir = "$env:LOCALAPPDATA\Google\Chrome\User Data"
if (-not (Test-Path $userDataDir)) {
    Write-Host "[FAIL] Chrome user data not found at $userDataDir" -ForegroundColor Red
    exit 1
}

# --- Handle running Chrome ---
$existing = Get-Process chrome -EA SilentlyContinue
if ($existing) {
    Write-Host "[WARN] Chrome is running ($($existing.Count) processes)." -ForegroundColor Yellow
    Write-Host "  CDP requires Chrome to start with the debug flag." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "  Option A: Close Chrome yourself (preserves session cookies)" -ForegroundColor Cyan
    Write-Host "  Option B: I close it gracefully (CloseMainWindow)" -ForegroundColor Cyan
    if (-not $GracefulOnly) {
        Write-Host "  Option C: Force kill (WARNING: may lose session cookies)" -ForegroundColor Red
    }
    Write-Host ""
    $confirm = Read-Host "Choose (a=wait for you / b=graceful / c=force / q=quit)"
    switch ($confirm.ToLower()) {
        'a' {
            Write-Host "Close Chrome, then press Enter..." -ForegroundColor Yellow
            Read-Host | Out-Null
        }
        'b' {
            $windows = Get-Process chrome -EA SilentlyContinue | Where-Object { $_.MainWindowHandle -ne 0 }
            foreach ($w in $windows) { $w.CloseMainWindow() | Out-Null }
            Write-Host "Graceful close sent. Waiting..." -ForegroundColor Yellow
            Start-Sleep -Seconds 5
            $remaining = Get-Process chrome -EA SilentlyContinue
            if ($remaining) {
                Write-Host "[WARN] $($remaining.Count) processes remain. May need force kill." -ForegroundColor Yellow
                if (-not $GracefulOnly) {
                    Stop-Process -Name chrome -Force -EA SilentlyContinue
                    Start-Sleep -Seconds 2
                }
            }
            Write-Host "[OK] Chrome closed." -ForegroundColor Green
        }
        'c' {
            if ($GracefulOnly) { Write-Host "Force kill disabled. Use -GracefulOnly:$false" -ForegroundColor Red; exit 1 }
            Stop-Process -Name chrome -Force -EA SilentlyContinue
            Start-Sleep -Seconds 3
            Write-Host "[OK] Chrome force-killed. Session cookies may be lost." -ForegroundColor Yellow
        }
        default { Write-Host "Aborted."; exit 0 }
    }
}

# --- Launch Chrome with CDP ---
$launchArgs = @(
    "--remote-debugging-port=$Port"
    "--remote-allow-origins=*"
    "--user-data-dir=$userDataDir"
    "--restore-last-session"
)

Write-Host ""
Write-Host "=== Chrome CDP Launch ===" -ForegroundColor Cyan
Write-Host "  Chrome:    $chromePath"
Write-Host "  Port:      $Port"
Write-Host "  Profile:   $userDataDir"
Write-Host "  Endpoint:  http://localhost:$Port"
Write-Host ""

Start-Process -FilePath $chromePath -ArgumentList $launchArgs
Start-Sleep -Seconds 5

# --- Verify CDP ---
try {
    $response = Invoke-WebRequest -Uri "http://localhost:$Port/json/version" -UseBasicParsing -TimeoutSec 10
    $info = $response.Content | ConvertFrom-Json
    Write-Host "[OK] Chrome CDP ready!" -ForegroundColor Green
    Write-Host "  Browser:   $($info.Browser)"
    Write-Host "  WebSocket: $($info.'webSocketDebuggerUrl')"
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "  1. Log into your accounts in Chrome (if not already)"
    Write-Host "  2. In .mcp.json: set playwright.disabled to false"
    Write-Host "  3. Restart Claude Code (or /mcp reload)"
    Write-Host "  4. Claude can now control your browser"
} catch {
    Write-Host "[FAIL] CDP not responding on port $Port" -ForegroundColor Red
    Write-Host "  Possible causes:" -ForegroundColor Yellow
    Write-Host "  - Another Chrome was already running (steals the profile lock)"
    Write-Host "  - Firewall blocking localhost:$Port"
    Write-Host "  - Chrome crashed on launch"
    Write-Host ""
    Write-Host "  Debug: curl http://localhost:$Port/json/version" -ForegroundColor Yellow
}
