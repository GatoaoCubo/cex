"""Patch non-claude boot wrappers to wrap the CLI call with a timeout watchdog.

Idempotent: detects if `run_with_timeout.ps1` is already sourced and skips.

Pattern inserted:
  . $PSScriptRoot/_shared/run_with_timeout.ps1
  ...
  $watchdog = Start-CexWatchdog
  & <cli> @cliArgs $initialMsg
  $exitStatus = Stop-CexWatchdog $watchdog
  Emit-ExitSignal -StartTime $cex_start_time -Status $exitStatus
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOT = ROOT / "boot"
RUNTIMES = ("gemini", "codex", "ollama")
SOURCE_LINE = ". $PSScriptRoot/_shared/run_with_timeout.ps1"


def patch_wrapper(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "run_with_timeout.ps1" in text:
        return "skip (already patched)"

    # 1. Add source line after emit_exit_signal source
    emit_src = ". $PSScriptRoot/_shared/emit_exit_signal.ps1"
    if emit_src not in text:
        return "fail (emit_exit_signal not sourced)"
    text = text.replace(
        emit_src,
        emit_src + "\n" + SOURCE_LINE,
        1,
    )

    # 2. Find the CLI call line: "& <cli> @cliArgs $initialMsg" or variants.
    # Wrap with watchdog start/stop and pass status to Emit-ExitSignal.
    cli_pattern = re.compile(
        r"^(?P<indent>\s*)(?P<call>& (?:gemini|codex|ollama|node|npx|python) [^\n]+)$",
        re.MULTILINE,
    )
    m = cli_pattern.search(text)
    if not m:
        cli_pattern2 = re.compile(
            r"^(?P<indent>\s*)(?P<call>& [\$\w\"][^\n]+)$",
            re.MULTILINE,
        )
        # Scan all and pick the last one that comes before Emit-ExitSignal or Set-CexTitle "DONE"
        matches = list(cli_pattern2.finditer(text))
        # Filter: must be AFTER "RUNNING" title and BEFORE "DONE" title / Emit-ExitSignal
        for cand in reversed(matches):
            tail = text[cand.end():]
            if "Emit-ExitSignal" in tail or 'Set-CexTitle "DONE"' in tail:
                m = cand
                break
    if not m:
        return "fail (CLI call line not found)"

    call_line = m.group("call")
    indent = m.group("indent")
    replacement = (
        f"{indent}$watchdog = Start-CexWatchdog\n"
        f"{indent}{call_line}\n"
        f"{indent}$exitStatus = Stop-CexWatchdog $watchdog"
    )
    text = text[: m.start()] + replacement + text[m.end():]

    # 3. Update Emit-ExitSignal call to pass -Status $exitStatus
    emit_call_pattern = re.compile(
        r"Emit-ExitSignal(?: -StartTime \$cex_start_time)?(?! -Status)",
    )
    if emit_call_pattern.search(text):
        text = emit_call_pattern.sub(
            "Emit-ExitSignal -StartTime $cex_start_time -Status $exitStatus",
            text,
            count=1,
        )
    else:
        return "fail (Emit-ExitSignal call not found)"

    path.write_text(text, encoding="utf-8")
    return "ok"


def main():
    results = []
    for f in sorted(BOOT.glob("n0[1-7]_*.ps1")):
        if not any(f.name.endswith(f"_{rt}.ps1") for rt in RUNTIMES):
            continue
        status = patch_wrapper(f)
        results.append((f.name, status))
    ok = sum(1 for _, s in results if s == "ok")
    print(f"Patched {ok}/{len(results)} wrappers")
    for name, status in results:
        tag = "[OK]  " if status == "ok" else "[--]  " if status.startswith("skip") else "[FAIL]"
        print(f"  {tag} {name}: {status}")
    sys.exit(0 if ok == len(results) or all(s.startswith("skip") or s == "ok" for _, s in results) else 1)


if __name__ == "__main__":
    main()
