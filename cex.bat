@echo off
REM CEX CLI - Unified Entry Point
REM Usage: cex [task] | cex status | cex stop | cex grid [mission]
REM Boot: N07 Orchestrator (pi + opus-4-6 xhigh)

set CEX_ROOT=%~dp0
cd /d "%CEX_ROOT%"

if "%~1"=="status" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_monitor.ps1
    goto :eof
)

if "%~1"=="stop" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_stop.ps1
    goto :eof
)

if "%~1"=="grid" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_grid.ps1 -mission %2 -interactive
    goto :eof
)

if "%~1"=="solo" (
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn\spawn_solo.ps1 -nucleus %2 -task %3 -interactive
    goto :eof
)

if "%~1"=="doctor" (
    python _tools\cex_doctor.py
    goto :eof
)

REM Default: boot N07 Orchestrator
call boot\cex.cmd %*
