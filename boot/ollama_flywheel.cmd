@echo off
title CEX OLLAMA FLYWHEEL -- qwen3:14b
cd /d "%~dp0.."

echo ============================================================
echo CEX OLLAMA FLYWHEEL -- Persistent Loop
echo ============================================================

:LOOP
echo.
echo [%date% %time%] Starting batch...
python -u _tools/cex_evolve_ollama.py --model qwen3:14b --batch 3 --max-cycles 1 --sleep 3
echo [%date% %time%] Batch done. Sleeping 5s...
timeout /t 5 /nobreak >nul
goto LOOP
