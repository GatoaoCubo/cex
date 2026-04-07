@echo off
:: CEX Overnight H1 -- Hardening + Evolve
:: Double-click to run. Check .cex\overnight\ in the morning.
:: Safe to run unattended: crash recovery, budget cap, auto-commit.

title CEX OVERNIGHT H1 [%date% %time%]
color 0E
mode con: cols=160 lines=50

echo.
echo   ============================================================
echo   CEX OVERNIGHT H1 -- Floor Before Ceiling
echo   ============================================================
echo   Phase 1: H1 Gaps (process lifecycle, naming, rules)
echo   Phase 2: Evolve all artifacts below 9.0
echo   Phase 3: Doctor + Flywheel audit
echo   ============================================================
echo   Started: %date% %time%
echo   Log: .cex\overnight\h1_%date:~-4%%date:~3,2%%date:~0,2%.log
echo   Kill: close this window (or Ctrl+C)
echo   ============================================================
echo.

set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"

set LOG=.cex\overnight\h1_%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%.log
if not exist .cex\overnight mkdir .cex\overnight

:: ============================================================
:: PHASE 1: H1 GAPS (sequential -p mode dispatches)
:: ============================================================
echo [%time%] PHASE 1: H1 GAPS >> %LOG%

echo [%time%] [1/6] G1.1 Creating n03-builder.md rule...
echo [%time%] G1.1 n03 rule >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G1.1"  "Read .cex/config/nucleus_sins.yaml for N03 (Soberba Inventiva). Create .claude/rules/n03-builder.md with: N03 identity, 8F enforcement, quality floor 9.0, never skip frontmatter. Follow the same format as .claude/rules/n05-operations.md. Then git add and commit with message '[N03] rule: n03-builder.md -- Soberba Inventiva identity + 8F enforcement'." >> %LOG% 2>&1
echo [%time%] G1.1 done (exit: %errorlevel%) >> %LOG%

echo [%time%] [2/6] G2.1 Kill-before-spawn in spawn_solo...
echo [%time%] G2.1 kill-before-spawn >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G2.1"  "Edit _spawn/spawn_solo.ps1. BEFORE the 'Start-Process cmd' line, add logic to: 1) Check if a process for this nucleus already exists in spawn_pids.txt. 2) If yes, kill it with 'taskkill /F /PID <pid> /T'. 3) Remove the old entry from spawn_pids.txt. This prevents duplicate nuclei. Add a comment '# Kill-before-spawn (roadmap principle 6)'. Then git add and commit with '[N07] fix: kill-before-spawn in spawn_solo (roadmap principle 6)'." >> %LOG% 2>&1
echo [%time%] G2.1 done (exit: %errorlevel%) >> %LOG%

echo [%time%] [3/6] G2.4 Convert boots to -p mode...
echo [%time%] G2.4 boots -p mode >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G2.4"  "Read all 6 boot files: boot/n01.cmd through boot/n06.cmd. For EACH one, change the claude launch line from interactive to -p mode. The pattern: change 'claude %%FLAGS%% %%MODEL%% ...' to 'claude -p %%FLAGS%% %%MODEL%% ...'. Keep all other flags (--dangerously-skip-permissions, --permission-mode, --no-chrome, --model, --mcp-config, --settings). Add '--name N0X-<Domain>' flag. After the claude line, add 'echo.' and 'echo [N0X COMPLETE]' and 'echo Press any key to close...' and 'pause >nul'. Then git add all 6 and commit with '[N07] feat: all boots -p mode -- auto-exit, zero idle (roadmap principle 3)'." >> %LOG% 2>&1
echo [%time%] G2.4 done (exit: %errorlevel%) >> %LOG%

echo [%time%] [4/6] G1.2+G1.3 Fix naming convention in kinds_meta...
echo [%time%] G1.2+G1.3 naming >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G1.3"  "Read .cex/kinds_meta.json. The naming patterns are WRONG for most kinds. Reality: KCs use 'kc_{{topic}}.md', templates use 'tpl_{{kind}}.md', builders use 'bld_{{role}}_{{kind}}.md'. Update the 12 kinds that have 'NONE' as naming to have a real pattern based on their pillar prefix. Also fix the 2 pillar mismatches: axiom should be P02 or naming should match P02, and naming_rule should be P08 or naming should match P08. Then git add and commit with '[N04] fix: kinds_meta naming patterns match reality (roadmap principle 2)'." >> %LOG% 2>&1
echo [%time%] G1.3 done (exit: %errorlevel%) >> %LOG%

echo [%time%] [5/6] G2.2+G2.3+G2.5 Fix spawn scripts...
echo [%time%] G2.2+G2.3+G2.5 spawn fixes >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G2.X"  "Fix 3 spawn scripts: 1) _spawn/spawn_stop.ps1: find any remaining 'Stop-Process' calls and replace with 'taskkill /F /PID <pid> /T' (some were already fixed, check orphan scan section). 2) _spawn/spawn_monitor.ps1: the monitor shows RUNNING for processes that already signaled complete. Fix: check if signal exists AND is newer than spawn time before showing status. 3) _spawn/flywheel_monitor.ps1: has a parse error with an invalid variable reference using colon. Find and fix it. All files must be ASCII-only. Then git add all 3 and commit with '[N05] fix: spawn_stop taskkill, monitor stale PIDs, flywheel parse (roadmap principle 1+6)'." >> %LOG% 2>&1
echo [%time%] G2.X done (exit: %errorlevel%) >> %LOG%

echo [%time%] [6/6] G4.4 Wire sanitize into pre-commit...
echo [%time%] G4.4 sanitize hook >> %LOG%
pi -p --model anthropic/claude-opus-4-6 --name "OVERNIGHT-G4.4"  "Read _tools/cex_hooks.py. Check if cex_sanitize.py is already wired into the pre-commit hook. If not, add a new check that runs 'python _tools/cex_sanitize.py --check --scope _tools/' on staged .py files. The check should FAIL the commit if any non-ASCII is found in executable code. Then git add and commit with '[N05] feat: cex_sanitize wired into pre-commit hook (roadmap principle 5)'." >> %LOG% 2>&1
echo [%time%] G4.4 done (exit: %errorlevel%) >> %LOG%

echo.
echo   [PHASE 1 COMPLETE] Check log for details.
echo.

:: ============================================================
:: H1 GATE CHECK
:: ============================================================
echo [%time%] H1 GATE CHECK >> %LOG%
python _tools/cex_doctor.py >> %LOG% 2>&1
python _tools/cex_flywheel_audit.py >> %LOG% 2>&1
python _tools/cex_sanitize.py --check --scope _tools/ >> %LOG% 2>&1
echo [%time%] H1 gate logged >> %LOG%

:: ============================================================
:: PHASE 2: OVERNIGHT EVOLVE (uses existing overnight.ps1)
:: ============================================================
echo.
echo   [PHASE 2] Starting overnight evolve (target: 9.0)...
echo [%time%] PHASE 2: EVOLVE >> %LOG%

:: Run evolve phase only (skip bootstrap -- already done April 2)
powershell -NoProfile -ExecutionPolicy Bypass -File boot\overnight.ps1 -Phase evolve -MaxTokens 200000 -TargetScore 9.0 >> %LOG% 2>&1

echo [%time%] PHASE 2 COMPLETE >> %LOG%

:: ============================================================
:: PHASE 3: FINAL AUDIT
:: ============================================================
echo.
echo   [PHASE 3] Final audit...
echo [%time%] PHASE 3: FINAL AUDIT >> %LOG%

python _tools/cex_doctor.py >> %LOG% 2>&1
python _tools/cex_flywheel_audit.py >> %LOG% 2>&1
python _tools/cex_release_check.py >> %LOG% 2>&1

:: Final commit
git add -A >> %LOG% 2>&1
git commit -m "[OVERNIGHT-H1] %date% -- gaps + evolve + audit" >> %LOG% 2>&1

echo [%time%] OVERNIGHT COMPLETE >> %LOG%

:: ============================================================
:: SUMMARY
:: ============================================================
echo.
echo   ============================================================
echo   OVERNIGHT COMPLETE
echo   ============================================================
echo   Log: %LOG%
echo   Review: type %LOG% ^| more
echo   Git:    git log --oneline -20
echo   Doctor: python _tools/cex_doctor.py
echo   ============================================================
echo.
pause
