@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul 2>&1
title CEX Installer
color 0A

echo.
echo  ========================================
echo   CEX -- One-Click Installer for Windows
echo  ========================================
echo.
echo  This will install everything needed to
echo  run CEX on this machine.
echo.
echo  Press any key to start (or close to cancel)...
pause >nul

:: ============================================================
:: STEP 1: Check winget (built into Windows 10/11)
:: ============================================================

echo.
echo  [1/8] Checking winget...
where winget >nul 2>&1
if errorlevel 1 (
    echo  [FAIL] winget not found. Windows 10 1709+ required.
    echo         Download from: https://aka.ms/getwinget
    pause
    exit /b 1
)
echo  [OK] winget available

:: ============================================================
:: STEP 2: Git
:: ============================================================

echo.
echo  [2/8] Checking Git...
where git >nul 2>&1
if errorlevel 1 (
    echo  [INSTALLING] Git...
    winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements
    :: Refresh PATH
    set "PATH=%PATH%;C:\Program Files\Git\cmd"
) else (
    echo  [OK] Git already installed
)

:: ============================================================
:: STEP 3: Python
:: ============================================================

echo.
echo  [3/8] Checking Python...
where python >nul 2>&1
if errorlevel 1 (
    echo  [INSTALLING] Python 3.12...
    winget install --id Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements
    set "PATH=%PATH%;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts"
) else (
    echo  [OK] Python already installed
)

:: ============================================================
:: STEP 4: Node.js
:: ============================================================

echo.
echo  [4/8] Checking Node.js...
where node >nul 2>&1
if errorlevel 1 (
    echo  [INSTALLING] Node.js...
    winget install --id OpenJS.NodeJS -e --accept-source-agreements --accept-package-agreements
    set "PATH=%PATH%;C:\Program Files\nodejs"
) else (
    echo  [OK] Node.js already installed
)

:: ============================================================
:: STEP 5: Claude Code CLI
:: ============================================================

echo.
echo  [5/8] Checking Claude Code CLI...
where claude >nul 2>&1
if errorlevel 1 (
    echo  [INSTALLING] Claude Code...
    call npm install -g @anthropic-ai/claude-code
) else (
    echo  [OK] Claude Code already installed
)

:: ============================================================
:: STEP 6: Clone or detect repo
:: ============================================================

echo.
echo  [6/8] Setting up CEX repository...

:: Detect if running from inside the repo already
if exist "%~dp0CLAUDE.md" (
    echo  [OK] Running from CEX repo: %~dp0
    set "CEX_DIR=%~dp0"
    cd /d "%CEX_DIR%"
) else (
    :: Clone to user's Documents\GitHub\cex
    set "CEX_DIR=%USERPROFILE%\Documents\GitHub\cex"
    if exist "!CEX_DIR!\CLAUDE.md" (
        echo  [OK] CEX repo found at !CEX_DIR!
        cd /d "!CEX_DIR!"
    ) else (
        echo  [CLONING] CEX repo...
        mkdir "%USERPROFILE%\Documents\GitHub" 2>nul
        git clone https://github.com/GatoaoCubo/cex.git "%USERPROFILE%\Documents\GitHub\cex"
        cd /d "%USERPROFILE%\Documents\GitHub\cex"
    )
)

:: ============================================================
:: STEP 7: Python dependencies
:: ============================================================

echo.
echo  [7/8] Installing Python dependencies...
if exist requirements.txt (
    python -m pip install --upgrade pip --quiet 2>nul
    python -m pip install -r requirements.txt --quiet
    echo  [OK] Dependencies installed (pyyaml, tiktoken)
) else (
    echo  [WARN] requirements.txt not found
)

:: ============================================================
:: STEP 8: PowerShell execution policy
:: ============================================================

echo.
echo  [8/8] Setting PowerShell execution policy...
powershell -Command "Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser -Force" 2>nul
echo  [OK] ExecutionPolicy set to Bypass

:: ============================================================
:: STATUS LINE (optional -- copy if not exists)
:: ============================================================

if not exist "%USERPROFILE%\.claude" mkdir "%USERPROFILE%\.claude" 2>nul

if not exist "%USERPROFILE%\.claude\statusline.py" (
    if exist "%USERPROFILE%\.claude\statusline.py.bak" (
        copy "%USERPROFILE%\.claude\statusline.py.bak" "%USERPROFILE%\.claude\statusline.py" >nul
    )
    echo  [i] Status line: configure later with /statusline
)

:: ============================================================
:: DONE -- Summary
:: ============================================================

echo.
echo  ========================================
echo   INSTALLATION COMPLETE
echo  ========================================
echo.
echo  What was installed/verified:
echo    [1] Git
echo    [2] Python 3.12
echo    [3] Node.js
echo    [4] Claude Code CLI
echo    [5] CEX repository
echo    [6] Python dependencies
echo    [7] PowerShell policy
echo.
echo  ----------------------------------------
echo   NEXT STEPS (one-time):
echo  ----------------------------------------
echo.
echo  1. Authenticate Claude Code:
echo     Open a terminal and run: claude
echo     (This opens your browser for Anthropic login)
echo.
echo  2. Boot CEX N07:
echo     powershell -ExecutionPolicy Bypass -File boot\cex.ps1
echo.
echo  3. Inside Claude, type:
echo     /init
echo     (Configures CEX for your brand -- 2 min)
echo.
echo  After that, run: powershell -ExecutionPolicy Bypass -File boot\cex.ps1
echo  ========================================
echo.

:: Ask if user wants to boot now
set /p BOOT="  Boot CEX now? (y/n): "
if /i "%BOOT%"=="y" (
    echo.
    echo  Launching CEX N07...
    powershell -NoProfile -NoExit -ExecutionPolicy Bypass -File boot\cex.ps1
) else (
    echo.
    echo  To boot later: powershell -ExecutionPolicy Bypass -File boot\cex.ps1
    echo.
    pause
)
