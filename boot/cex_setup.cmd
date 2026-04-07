@echo off
:: CEX Zero-Install Setup
:: Run on a fresh Windows PC. Checks + installs all dependencies.
:: Requires: Python 3.12+, Node.js 22+, Git (install manually first)

title CEX SETUP
color 0E
echo.
echo   ============================================================
echo   CEX SETUP -- Zero to Running
echo   ============================================================
echo.

set FAIL=0

:: -- Layer 1: Runtime Check --
echo [1/5] Checking runtimes...
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo   [X] Python 3.12+ NOT FOUND
    echo       Install: https://python.org/downloads
    echo       Or:      winget install Python.3
    set FAIL=1
) else (
    for /f "tokens=2" %%v in ('python --version 2^>^&1') do echo   [OK] Python %%v
)

node --version >nul 2>&1
if errorlevel 1 (
    echo   [X] Node.js 22+ NOT FOUND
    echo       Install: https://nodejs.org (LTS)
    echo       Or:      winget install OpenJS.NodeJS.LTS
    set FAIL=1
) else (
    for /f %%v in ('node --version 2^>^&1') do echo   [OK] Node.js %%v
)

git --version >nul 2>&1
if errorlevel 1 (
    echo   [X] Git NOT FOUND
    echo       Install: https://git-scm.com/downloads
    echo       Or:      winget install Git.Git
    set FAIL=1
) else (
    for /f "tokens=3" %%v in ('git --version 2^>^&1') do echo   [OK] Git %%v
)

echo.
if %FAIL%==1 (
    echo   Install missing runtimes first, then re-run this script.
    echo.
    pause
    exit /b 1
)

:: -- Layer 3: Core Packages --
echo [2/5] Installing Python dependencies...
pip install pyyaml tiktoken uv 2>&1 | findstr /i "Successfully already"
echo.

echo [3/5] Installing pi coding agent...
call npm list -g @mariozechner/pi-coding-agent >nul 2>&1
if errorlevel 1 (
    call npm install -g @mariozechner/pi-coding-agent
) else (
    echo   [OK] pi already installed
)
echo.

:: -- Layer 3b: CEX Package --
echo [4/5] Installing CEX package (themes + skills + extensions)...
if exist cex-pi-package\package.json (
    cd cex-pi-package
    call npm link 2>&1 | findstr /i "added up"
    cd ..
    echo   [OK] CEX package linked
) else (
    echo   [SKIP] cex-pi-package not found (optional)
)
echo.

:: -- Verification --
echo [5/5] Verifying installation...
echo.

python _tools/cex_doctor.py 2>&1 | findstr "Result:"
python _tools/cex_flywheel_audit.py 2>&1 | findstr "HEALTH"

echo.
echo   ============================================================
echo   SETUP COMPLETE
echo   ============================================================
echo.
echo   Next steps:
echo     1. Run:  pi /login        (authenticate with your LLM provider)
echo     2. Run:  boot\cex.cmd     (start N07 orchestrator)
echo     3. Or:   boot\n03.cmd     (start a single nucleus)
echo.
echo   First time? Type /init in the chat to configure your brand.
echo.
pause
