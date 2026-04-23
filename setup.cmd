@echo off
setlocal enabledelayedexpansion
:: ============================================================
:: CEX SETUP -- Fresh PC to Running in 5 Minutes
:: ============================================================
::
:: Prerequisites (install manually):
::   - Python 3.12+  : python.org/downloads  OR  winget install Python.3
::   - Node.js 18+   : nodejs.org (LTS)      OR  winget install OpenJS.NodeJS.LTS
::   - Git 2.40+     : git-scm.com/downloads OR  winget install Git.Git
::
:: After those 3 runtimes, this script installs everything else.
:: Claude Code can install anything additional once it boots.
::
:: Usage:
::   setup.cmd
::   setup.cmd https://github.com/user/cex.git
:: ============================================================

title CEX SETUP
color 0E

echo.
echo   ============================================================
echo   CEX SETUP -- Fresh PC to Running
echo   ============================================================
echo.

set FAIL=0
set WARN=0
set REPO_URL=%~1

:: ============================================================
:: STEP 1: Validate Runtimes
:: ============================================================
echo   [1/6] Checking runtimes...
echo.

:: -- Python --
set PY_OK=0
for /f "tokens=2" %%v in ('python --version 2^>^&1') do (
    echo     [OK] Python %%v
    set PY_OK=1
)
if !PY_OK!==0 (
    echo     [FAIL] Python NOT FOUND
    echo            Install: python.org/downloads
    echo            Or:      winget install Python.3
    echo            IMPORTANT: Check "Add to PATH" during install
    set FAIL=1
)

:: -- Node.js --
set NODE_OK=0
for /f %%v in ('node --version 2^>^&1') do (
    echo     [OK] Node.js %%v
    set NODE_OK=1
)
if !NODE_OK!==0 (
    echo     [FAIL] Node.js NOT FOUND
    echo            Install: nodejs.org -- LTS version
    echo            Or:      winget install OpenJS.NodeJS.LTS
    set FAIL=1
)

:: -- Git --
set GIT_OK=0
for /f "tokens=3" %%v in ('git --version 2^>^&1') do (
    echo     [OK] Git %%v
    set GIT_OK=1
)
if !GIT_OK!==0 (
    echo     [FAIL] Git NOT FOUND
    echo            Install: git-scm.com/downloads
    echo            Or:      winget install Git.Git
    set FAIL=1
)

echo.

if !FAIL!==1 (
    echo   [XX] Install the missing runtimes above, then re-run this script.
    echo.
    pause
    exit /b 1
)

echo     All 3 runtimes found.
echo.

:: ============================================================
:: STEP 2: Install Claude Code
:: ============================================================
echo   [2/6] Claude Code CLI...
echo.

set CC_OK=0
for /f %%v in ('claude --version 2^>^&1') do (
    echo     [OK] Claude Code %%v
    set CC_OK=1
)
if !CC_OK!==0 (
    echo     Installing @anthropic-ai/claude-code ...
    call npm install -g @anthropic-ai/claude-code
    if errorlevel 1 (
        echo     [FAIL] npm install failed. Check Node.js installation.
        set FAIL=1
    ) else (
        echo     [OK] Claude Code installed
    )
)

echo.

if !FAIL!==1 (
    echo   [XX] Claude Code install failed. Fix npm issues and re-run.
    pause
    exit /b 1
)

:: ============================================================
:: STEP 3: Install Python Dependencies
:: ============================================================
echo   [3/6] Python dependencies...
echo.

python -m pip install --quiet pyyaml tiktoken 2>nul
if errorlevel 1 (
    echo     [WARN] pip install had issues -- CEX tools may not work
    set WARN=1
) else (
    echo     [OK] pyyaml + tiktoken
)

python -m pip install --quiet uv 2>nul
if errorlevel 1 (
    echo     [WARN] uv install failed -- some MCP servers wont auto-install
    set WARN=1
) else (
    echo     [OK] uv -- for uvx MCP server auto-install
)

echo.

:: ============================================================
:: STEP 4: Ensure CEX Repo
:: ============================================================
echo   [4/6] CEX repository...
echo.

if exist ".cex\kinds_meta.json" (
    echo     [OK] Already inside CEX repo
    goto :step5
)

if exist "cex\.cex\kinds_meta.json" (
    echo     [OK] CEX repo found in .\cex\
    cd cex
    goto :step5
)

if "!REPO_URL!"=="" (
    echo     CEX repo not found in current directory.
    echo.
    echo     Options:
    echo       a^) Run this script FROM inside the CEX repo
    echo       b^) Run: setup.cmd https://github.com/YOUR-USER/cex.git
    echo.
    set /p REPO_URL="    Repo URL (Enter to skip): "
)

if "!REPO_URL!"=="" (
    echo     [WARN] No repo -- cd into CEX directory and re-run
    set WARN=1
    goto :step5
)

echo     Cloning !REPO_URL! ...
git clone "!REPO_URL!" cex
if errorlevel 1 (
    echo     [FAIL] Clone failed. Check URL and network.
    pause
    exit /b 1
)
cd cex
echo     [OK] Cloned to .\cex\

:step5
echo.

:: ============================================================
:: STEP 5: Verify Installation
:: ============================================================
echo   [5/6] Verifying CEX health...
echo.

if exist "_tools\cex_doctor.py" (
    for /f "delims=" %%L in ('python _tools/cex_doctor.py 2^>^&1 ^| findstr "Result:"') do (
        echo     %%L
    )
) else (
    echo     [WARN] Not in CEX repo -- skipping health check
    set WARN=1
)

echo.

:: ============================================================
:: STEP 6: Summary
:: ============================================================
echo   [6/6] Authentication...
echo.
echo     Claude Code uses your Anthropic account directly.
echo     First run opens browser for OAuth login.
echo     Supported: Max -- unlimited Opus / Pro / API key
echo.
echo   ============================================================
if !WARN!==1 (
    echo   SETUP COMPLETE (with warnings^)
) else (
    echo   SETUP COMPLETE
)
echo   ============================================================
echo.
echo   Next steps:
echo     1. powershell boot\cex.ps1    Start N07 orchestrator
echo     2. powershell boot\n03.ps1    Start builder nucleus
echo     3. Type /init in chat         Configure your brand
echo.
echo   3 runtimes + Claude Code + clone = CEX runs.
echo.
pause
endlocal
