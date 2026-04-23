@echo off
:: CEX-LAB -- experiments, benchmarks, breaking changes (private repo: cex-lab)
:: Usage: cex-lab [subcommand]

set CEX_ROOT=%~dp0
set CEX_TIER=lab
set CEX_REMOTE=lab
cd /d "%CEX_ROOT%"

if "%~1"=="" (
    powershell -NoProfile -NoExit -ExecutionPolicy Bypass -File boot\cex.ps1
) else if "%~1"=="status" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_monitor.ps1
) else if "%~1"=="stop" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_stop.ps1
) else if "%~1"=="grid" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_grid.ps1 -mission %2 -interactive
) else if "%~1"=="solo" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_solo.ps1 -nucleus %2 -task "%~3" -interactive
) else if "%~1"=="doctor" (
    python _tools\cex_doctor.py
) else if "%~1"=="promote" (
    echo Promoting lab to dev...
    git push origin main
) else (
    powershell -NoProfile -NoExit -ExecutionPolicy Bypass -File boot\cex.ps1 %*
)
