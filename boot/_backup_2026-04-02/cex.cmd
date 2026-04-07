@echo off
:: CEX Boot - N07 Orchestrator
:: Runtime: pi (subscription/OAuth) | Model: claude-opus-4-6 | Thinking: xhigh
:: The orchestrator. NEVER builds. Dispatches to N01-N06.
:: FIRST RUN: detects missing brand_config.yaml and triggers bootstrap.

set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
set CEX_NUCLEUS=N07
set CLAUDECODE=
cd /d "%CEX_ROOT%"

:: -- Bootstrap Check --
if not exist "%CEX_ROOT%\.cex\brand\.bootstrapped" (
    echo.
    echo  ============================================================
    echo   CEX FIRST RUN DETECTED
    echo  ============================================================
    echo.
    echo   The X in CEX is YOUR brand. Let's fill it.
    echo   This will configure the entire system for your company.
    echo.
    echo   Option 1: Quick bootstrap ^(13 questions, ~5 min^)
    echo     python _tools/cex_bootstrap.py
    echo.
    echo   Option 2: Full Brand Discovery ^(15 questions + brand book^)
    echo     boot\n06.cmd
    echo.
    echo   Option 3: Import existing brand config
    echo     python _tools/cex_bootstrap.py --from-file your_brand.yaml
    echo.
    echo  ============================================================
    echo.
    choice /C QFI /M "  [Q]uick bootstrap, [F]ull discovery (N06), or [I]gnore for now?"
    if errorlevel 3 goto :start_orchestrator
    if errorlevel 2 goto :full_discovery
    if errorlevel 1 goto :quick_bootstrap
)
goto :start_orchestrator

:quick_bootstrap
python _tools/cex_bootstrap.py
goto :start_orchestrator

:full_discovery
call boot\n06.cmd
goto :eof

:start_orchestrator
:: -- Load Brand Name for Title --
for /f "tokens=2 delims=: " %%a in ('findstr /C:"BRAND_NAME" "%CEX_ROOT%\.cex\brand\brand_config.yaml" 2^>nul') do (
    set BRAND_NAME=%%a
)
if defined BRAND_NAME (
    title %BRAND_NAME%-CEX-N07-ORCHESTRATOR
) else (
    title CEX-N07-ORCHESTRATOR
)

:: ALWAYS interactive -- N07 orchestrates, never receives task args
pi --model anthropic/claude-opus-4-6 --thinking xhigh
