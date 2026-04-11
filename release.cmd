@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul 2>&1
title CEX Release Builder

echo.
echo  ========================================
echo   CEX Release Builder
echo  ========================================
echo.

:: ============================================================
:: CONFIG
:: ============================================================

:: Read version from CLAUDE.md or default
set "VERSION=1.0.0"
for /f "tokens=2 delims=:" %%a in ('findstr /i "version:" CLAUDE.md 2^>nul') do (
    set "VERSION=%%a"
    set "VERSION=!VERSION: =!"
)

set "RELEASE_DIR=_releases"
set "ZIP_NAME=cex-v%VERSION%"
set "ZIP_PATH=%RELEASE_DIR%\%ZIP_NAME%.zip"

echo  Version:  %VERSION%
echo  Output:   %ZIP_PATH%
echo.

:: ============================================================
:: PRE-FLIGHT CHECKS
:: ============================================================

echo  [1/6] Pre-flight checks...

:: Doctor
python _tools/cex_doctor.py 2>nul | findstr /c:"0 FAIL" >nul
if errorlevel 1 (
    echo  [FAIL] cex_doctor.py has failures. Fix before release.
    python _tools/cex_doctor.py 2>nul | findstr /c:"FAIL"
    pause
    exit /b 1
)
echo    [OK] Doctor: 0 FAIL

:: Compile
python _tools/cex_compile.py --all 2>nul | findstr /c:"compiled successfully" >nul
if errorlevel 1 (
    echo  [FAIL] Compilation errors. Fix before release.
    pause
    exit /b 1
)
echo    [OK] Compile: all OK

:: Sanitizer
python _tools/cex_sanitize.py --check --scope _tools/ 2>nul | findstr /c:"Dirty:   0" >nul
if errorlevel 1 (
    echo  [FAIL] Non-ASCII in code files. Run: python _tools/cex_sanitize.py --fix --scope _tools/
    pause
    exit /b 1
)
echo    [OK] Sanitizer: ASCII clean

:: Git clean
for /f %%i in ('git status --porcelain 2^>nul ^| find /c /v ""') do set DIRTY=%%i
if %DIRTY% GTR 0 (
    echo    [WARN] %DIRTY% uncommitted files -- they WILL be included in ZIP
)

echo.

:: ============================================================
:: BUILD INDEX (fresh TF-IDF for distribution)
:: ============================================================

echo  [2/6] Rebuilding search index...
python _tools/cex_retriever.py --build >nul 2>&1
echo    [OK] TF-IDF index rebuilt

echo.

:: ============================================================
:: CREATE RELEASE DIR
:: ============================================================

echo  [3/6] Preparing release directory...
if not exist "%RELEASE_DIR%" mkdir "%RELEASE_DIR%"

:: Clean previous build of same version
if exist "%ZIP_PATH%" del "%ZIP_PATH%"

echo    [OK] Release dir ready

echo.

:: ============================================================
:: PACKAGE ZIP (exclude secrets, runtime, dev-only files)
:: ============================================================

echo  [4/6] Packaging ZIP...

:: Use git archive for clean export (respects .gitignore automatically)
git archive --format=zip --prefix=%ZIP_NAME%/ HEAD -o "%ZIP_PATH%" 2>nul

if errorlevel 1 (
    echo  [FAIL] git archive failed
    pause
    exit /b 1
)

:: Add the freshly built index (not in git)
:: Use PowerShell to append to ZIP since CMD has no native zip support
powershell -Command "
    $indexFile = '.cex\retriever_index.json'
    if (Test-Path $indexFile) {
        $zip = [System.IO.Compression.ZipFile]::Open('%ZIP_PATH%', 'Update')
        $entry = $zip.CreateEntry('%ZIP_NAME%/.cex/retriever_index.json')
        $stream = $entry.Open()
        $bytes = [System.IO.File]::ReadAllBytes($indexFile)
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Close()
        $zip.Dispose()
        Write-Host '    [OK] TF-IDF index added to ZIP'
    }
" 2>nul

:: Get ZIP size
for %%f in ("%ZIP_PATH%") do set "ZIP_SIZE=%%~zf"
set /a ZIP_MB=%ZIP_SIZE% / 1048576

echo    [OK] ZIP created: %ZIP_MB% MB

echo.

:: ============================================================
:: VERIFY ZIP CONTENTS
:: ============================================================

echo  [5/6] Verifying ZIP contents...

:: Count files in ZIP
for /f %%i in ('powershell -Command "(Get-Archive '%ZIP_PATH%' -EA SilentlyContinue).Entries.Count" 2^>nul') do set ZIP_COUNT=%%i
if not defined ZIP_COUNT (
    :: Fallback: use tar to list
    for /f %%i in ('tar -tf "%ZIP_PATH%" 2^>nul ^| find /c /v ""') do set ZIP_COUNT=%%i
)

echo    Files in ZIP: %ZIP_COUNT%

:: Verify critical files exist in ZIP
set "MISSING=0"
for %%f in (CLAUDE.md install.cmd requirements.txt boot/cex.ps1) do (
    tar -tf "%ZIP_PATH%" 2>nul | findstr /c:"%%f" >nul 2>nul
    if errorlevel 1 (
        echo    [MISS] %%f
        set /a MISSING+=1
    )
)

:: Verify secrets are NOT in ZIP
set "LEAKED=0"
for %%f in (.env _config/client_secret.json _config/token.json) do (
    tar -tf "%ZIP_PATH%" 2>nul | findstr /c:"%%f" >nul 2>nul
    if not errorlevel 1 (
        echo    [LEAK] %%f found in ZIP -- DANGER
        set /a LEAKED+=1
    )
)

if %LEAKED% GTR 0 (
    echo  [FAIL] Secrets found in ZIP! Do NOT distribute.
    del "%ZIP_PATH%"
    pause
    exit /b 1
)

if %MISSING% EQU 0 (
    echo    [OK] All critical files present
) else (
    echo    [WARN] %MISSING% critical file(s) missing
)
echo    [OK] No secrets leaked

echo.

:: ============================================================
:: GENERATE CHECKSUMS
:: ============================================================

echo  [6/6] Generating checksums...

:: SHA256
powershell -Command "(Get-FileHash '%ZIP_PATH%' -Algorithm SHA256).Hash" > "%RELEASE_DIR%\%ZIP_NAME%.sha256" 2>nul
for /f %%h in (%RELEASE_DIR%\%ZIP_NAME%.sha256) do set "SHA256=%%h"
echo    SHA256: %SHA256%

:: Write release notes
(
    echo CEX Release v%VERSION%
    echo ========================
    echo.
    echo Date: %DATE%
    echo SHA256: %SHA256%
    echo.
    echo Installation:
    echo   1. Extract ZIP
    echo   2. Double-click install.cmd
    echo   3. Follow prompts
    echo.
    echo Requirements:
    echo   - Windows 10/11
    echo   - Internet connection ^(first run only^)
    echo   - Anthropic Max subscription ^(for Claude Opus^)
    echo     OR Ollama installed locally ^(free, reduced quality^)
) > "%RELEASE_DIR%\%ZIP_NAME%-RELEASE-NOTES.txt"

echo    [OK] Checksums and release notes saved

:: ============================================================
:: SUMMARY
:: ============================================================

echo.
echo  ========================================
echo   RELEASE COMPLETE
echo  ========================================
echo.
echo   File:     %ZIP_PATH%
echo   Size:     %ZIP_MB% MB
echo   SHA256:   %SHA256:~0,16%...
echo.
echo   Upload to:
echo     Hotmart:  https://app.hotmart.com/products
echo     Gumroad:  https://app.gumroad.com/products
echo     GitHub:   gh release create v%VERSION% %ZIP_PATH%
echo.
echo  ========================================
echo.
pause
