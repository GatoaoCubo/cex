@echo off
:: CEX Infinite Bootstrap Loop
:: N07 orchestrates, restarts on context exhaustion.
:: Kill: close this window (or Ctrl+C)

title CEX INFINITE BOOTSTRAP [%date%]
color 0E
mode con: cols=160 lines=50

set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

echo.
echo   ============================================================
echo   CEX INFINITE BOOTSTRAP LOOP
echo   ============================================================
echo   N07 orchestrates continuously. Restarts on context exhaustion.
echo   State persisted to: .cex/runtime/mission_state.yaml
echo   Kill: close this window
echo   ============================================================
echo   Started: %date% %time%
echo   ============================================================
echo.

:loop
echo [%time%] Starting N07 session...

pi --model anthropic/claude-opus-4-6 ^
   --append-system-prompt "N07_admin/agent_card_n07.md" ^
   --append-system-prompt ".cex/config/context_self_select.md" ^
   --append-system-prompt "You are N07 Orchestrating Sloth. Read .cex/runtime/mission_state.yaml. Continue the mission from last checkpoint. Dispatch nuclei, monitor via git log (non-blocking), consolidate. When your context is getting full, write mission state to disk and exit cleanly." ^
   "Read .cex/runtime/mission_state.yaml and .cex/runtime/plans/ to find active mission. Continue from where previous N07 left off. If no active mission, report ready."

echo.
echo [%time%] N07 exited (context exhaustion or mission complete).
echo [%time%] Restarting in 10s... (Ctrl+C to stop)
timeout /t 10 /nobreak >nul
goto loop
