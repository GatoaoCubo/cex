@echo off
:: Repo launcher -- opens N07 on the current worktree
:: Usage: repo-launch [subcommand]

set CEX_ROOT=%~dp0
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
) else (
    powershell -NoProfile -NoExit -ExecutionPolicy Bypass -File boot\cex.ps1 %*
)
