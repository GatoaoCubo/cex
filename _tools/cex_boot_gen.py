#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Boot Generator -- reads nucleus_models.yaml -> generates boot/*.ps1

Usage:
  python _tools/cex_boot_gen.py              # generate all boot scripts
  python _tools/cex_boot_gen.py --dry-run    # show what would be generated
  python _tools/cex_boot_gen.py --nucleus n03  # generate one
  python _tools/cex_boot_gen.py --show       # show current config table

Reads:  .cex/P09_config/nucleus_models.yaml
Writes: boot/n0{1-6}.ps1 + boot/cex.ps1 (PowerShell-only stack)
"""
import argparse
import sys
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".cex" / "config" / "nucleus_models.yaml"
SINS_CONFIG = ROOT / ".cex" / "config" / "nucleus_sins.yaml"
TEMPLATE = ROOT / ".cex" / "config" / "nucleus_models.template.yaml"
BOOT_DIR = ROOT / "boot"


def _load_sins() -> dict:
    """Load nucleus_sins.yaml for sin-aware UX."""
    if SINS_CONFIG.exists():
        try:
            with open(SINS_CONFIG, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        except Exception:
            pass
    return {}


# Nucleus metadata (domain prompts + agent cards + initial messages)
NUCLEUS_META = {
    "n07": {
        "title": "CEX-N07-ORCHESTRATOR",
        "var": "CEX_NUCLEUS=N07",
        "agent_card": "N07_admin/agent_card_n07.md",
        "prompt": "You are N07 Orchestrator of CEX. Dispatch nuclei, never build. Read CLAUDE.md e .claude/rules/n07-orchestrator.md.",
        "initial": "Ready. What do you need?",
    },
    "n01": {
        "title": "CEX-N01-RESEARCH",
        "var": "CEX_NUCLEUS=N01",
        "agent_card": "N01_intelligence/agent_card_n01.md",
        "prompt": "You are N01 Research Nucleus of CEX. Domain: research, analysis, papers, competitors. IF .cex/runtime/handoffs/n01_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n01_task.md and execute. If no handoff, report ready.",
    },
    "n02": {
        "title": "CEX-N02-MARKETING",
        "var": "CEX_NUCLEUS=N02",
        "agent_card": "N02_marketing/agent_card_n02.md",
        "prompt": "You are N02 Marketing Nucleus of CEX. Domain: copy, ads, campaigns, brand voice. IF .cex/runtime/handoffs/n02_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n02_task.md and execute. If no handoff, report ready.",
    },
    "n03": {
        "title": "CEX-N03-BUILDER",
        "var": "CEX_NUCLEUS=N03",
        "agent_card": "N03_engineering/agent_card_n03.md",
        "prompt": "You are N03 Builder Nucleus of CEX. 8F pipeline mandatory. Read .claude/rules/n03-8f-enforcement.md and N03_engineering/P02_model/agent_engineering.md. IF .cex/runtime/handoffs/n03_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n03_task.md and execute. If no handoff, report ready.",
    },
    "n04": {
        "title": "CEX-N04-KNOWLEDGE",
        "var": "CEX_NUCLEUS=N04",
        "agent_card": "N04_knowledge/agent_card_n04.md",
        "prompt": "You are N04 Knowledge Nucleus of CEX. Domain: RAG, indexing, knowledge cards, taxonomy. IF .cex/runtime/handoffs/n04_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n04_task.md and execute. If no handoff, report ready.",
    },
    "n05": {
        "title": "CEX-N05-OPERATIONS",
        "var": "CEX_NUCLEUS=N05",
        "agent_card": "N05_operations/agent_card_n05.md",
        "prompt": "You are N05 Operations Nucleus of CEX. Domain: code review, testing, CI/CD, deploy. IF .cex/runtime/handoffs/n05_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n05_task.md and execute. If no handoff, report ready.",
    },
    "n06": {
        "title": "CEX-N06-COMMERCIAL",
        "var": "CEX_NUCLEUS=N06",
        "agent_card": "N06_commercial/agent_card_n06.md",
        "prompt": "You are N06 Commercial Nucleus of CEX. Domain: pricing, funnels, monetization, brand. IF .cex/runtime/handoffs/n06_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
        "initial": "Read .cex/runtime/handoffs/n06_task.md and execute. If no handoff, report ready.",
    },
}

# Nucleus color scheme (visually distinct per nucleus)
NUCLEUS_COLORS = {
    "n01": {"bg": "DarkBlue",    "fg": "White",  "accent": "Cyan",    "label": "RESEARCH"},
    "n02": {"bg": "DarkMagenta", "fg": "White",  "accent": "Magenta", "label": "MARKETING"},
    "n03": {"bg": "DarkGreen",   "fg": "White",  "accent": "Green",   "label": "BUILDER"},
    "n04": {"bg": "DarkCyan",    "fg": "White",  "accent": "Yellow",  "label": "KNOWLEDGE"},
    "n05": {"bg": "DarkGray",    "fg": "White",  "accent": "Gray",    "label": "OPERATIONS"},
    "n06": {"bg": "DarkRed",     "fg": "White",  "accent": "Red",     "label": "COMMERCIAL"},
    "n07": {"bg": "Black",       "fg": "White",  "accent": "White",   "label": "ORCHESTRATOR"},
}


# CLI-specific boot templates -- PowerShell format (rich UX: colors, sizing, Unicode)
def build_claude_ps1(nucleus: str, cfg: dict, meta: dict) -> str:
    try:
        from cex_model_resolver import resolve_model
        _default_model = resolve_model(nucleus)["model"]
    except Exception:
        _default_model = "claude-sonnet-4-6"
    model = cfg.get("model", _default_model)
    flags = cfg.get("flags", "--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome")
    mcps = cfg.get("mcps", "")
    settings = cfg.get("settings", "")
    ctx = cfg.get("context", 200000)

    # Sin-aware colors (from nucleus_sins.yaml, fallback to legacy NUCLEUS_COLORS)
    sins = _load_sins()
    sin_data = sins.get(nucleus, {})
    sin_color = sin_data.get("color", {})
    legacy_colors = NUCLEUS_COLORS.get(nucleus, NUCLEUS_COLORS["n03"])

    bg = sin_color.get("ps_bg", legacy_colors["bg"])
    fg = sin_color.get("ps_fg", legacy_colors["fg"])
    accent = sin_color.get("ps_accent", legacy_colors["accent"])
    label = legacy_colors["label"]

    # Sin identity
    icon_raw = sin_data.get("icon", "")
    virtue = sin_data.get("virtue", "")
    virtue_en = sin_data.get("virtue_en", "")
    tagline = sin_data.get("tagline", "")
    sin_injection = sin_data.get("prompt_injection", "").strip()

    # ASCII-safe icon (PS1 must be ASCII-only per ascii-code-rule.md)
    icon = icon_raw if icon_raw.isascii() else "[*]"
    # ASCII-safe tagline and virtue
    def _ascii_safe(s):
        return s.encode('ascii', 'replace').decode('ascii').replace('?', '-') if s else ""
    tagline = _ascii_safe(tagline)
    virtue_display = _ascii_safe(virtue)
    virtue_en_display = _ascii_safe(virtue_en)

    # Build the sin-injected prompt (sin lens BEFORE the domain prompt)
    full_prompt = meta["prompt"]
    if sin_injection:
        # Clean for PS here-string (no special escaping needed inside @'...'@)
        safe_injection = sin_injection.replace('\n', ' ').strip()
        full_prompt = f"{safe_injection} --- {full_prompt}"
    # Replace any non-ASCII in prompt (em-dashes, accents, etc.)
    full_prompt = full_prompt.replace('\u2014', '--').replace('\u2013', '-')
    full_prompt = full_prompt.encode('ascii', 'replace').decode('ascii').replace('?', '-')

    # Build PS argument array items (each flag as separate quoted string)
    flag_parts = flags.split() if flags else []
    flags_array = ", ".join(f'"{f}"' for f in flag_parts)

    # MCP and settings as conditional argument additions
    mcp_line = f'$args += "--mcp-config", "{ROOT}\\{mcps}"' if mcps else "# no MCP config"
    # Settings precedence: explicit cfg.settings -> per-nucleus allowlist stub -> none
    # The allowlist stub (.claude/nucleus-settings/{nucleus}.json) exists for N01-N07
    # as a scoped permission reference; existing nuclei still bypass via global
    # settings.json, but the --settings flag ensures the stub is loaded when present.
    if settings:
        settings_line = f'$args += "--settings", "{ROOT}\\{settings}"'
    else:
        settings_line = (
            f'$stubPath = Join-Path $cexRoot ".claude/nucleus-settings/{nucleus}.json"\n'
            f'if (Test-Path $stubPath) {{ $cliArgs += "--settings", $stubPath }}'
        )

    nuc_upper = nucleus.upper()
    ctx_k = ctx // 1000
    var_name = meta["var"].split("=")[0]
    var_val = meta["var"].split("=")[1]
    agent_card = meta.get("agent_card", "")
    initial = meta.get("initial", "Ready.")

    return '''# CEX {nuc_upper} -- {meta["title"]}
# Generated by cex_boot_gen.py from .cex/P09_config/nucleus_models.yaml + nucleus_sins.yaml
# CLI: claude | Model: {model} | Context: {ctx}
# Sin: {virtue_display} ({virtue_en_display})
# isolation: worktree
# permissions: .claude/nucleus-settings/{nucleus}.json (auto-loaded if present)
# flags: {flags}

# --- UX: Window title with mission + sin + status ---
# Auto-detect root from script location (worktree-agnostic)
. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI (claude/gemini/codex/ollama)
$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "{nucleus}"
. $PSScriptRoot/_shared/theme.ps1  # Per-nucleus theme (bg color, scrollback)
$sinName = "{virtue_en_display}"
$modelShort = "{model}" -replace "claude-", ""

# Detect mission from handoff file
$mission = ""
$handoff = "$cexRoot\\.cex\\runtime\\handoffs\\${{nucleus}}_task.md"
if (Test-Path $handoff) {{
    $content = Get-Content $handoff -Head 10 -EA SilentlyContinue
    foreach ($line in $content) {{
        if ($line -match "^mission:\\s*(.+)$") {{
            $mission = $Matches[1].Trim()
            break
        }}
    }}
}}

# Detect git repo name + branch
$gitBranch = ""
$gitRepo = ""
try {{
    $gitBranch = (git rev-parse --abbrev-ref HEAD 2>$null)
    $gitRemote = (git remote get-url origin 2>$null)
    if ($gitRemote -match "[/:]([^/]+?)(?:\\.git)?$") {{ $gitRepo = $Matches[1] }}
}} catch {{}}

# Build title: N0X Sin | repo@branch [mission] -- STATUS
function Set-CexTitle($status) {{
    $t = "{nuc_upper} $sinName"
    if ($gitRepo) {{ $t += " | $gitRepo" }}
    if ($gitBranch) {{ $t += "@$gitBranch" }}
    if ($mission) {{ $t += " [$mission]" }}
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}}

Set-CexTitle "BOOTING"

try {{
    $Host.UI.RawUI.BackgroundColor = "{bg}"
    $Host.UI.RawUI.ForegroundColor = "{fg}"
    if (-not $env:CEX_GRID) {{
        # Solo mode: set buffer + window size. Grid mode: spawn_grid controls sizing.
        $bufSize = $Host.UI.RawUI.BufferSize
        $bufSize.Width = 160; $bufSize.Height = 9999
        $Host.UI.RawUI.BufferSize = $bufSize
        $winSize = $Host.UI.RawUI.WindowSize
        $winSize.Width = [Math]::Min(160, $Host.UI.RawUI.MaxWindowSize.Width)
        $winSize.Height = [Math]::Min(40, $Host.UI.RawUI.MaxWindowSize.Height)
        $Host.UI.RawUI.WindowSize = $winSize
    }}
    Clear-Host
}} catch {{}}

Write-Host ""
Write-Host "  {icon} {nuc_upper} {virtue_display} - {virtue_en_display}" -ForegroundColor {accent}
Write-Host "  {'=' * 50}" -ForegroundColor DarkGray
Write-Host "  {tagline}" -ForegroundColor DarkGray
Write-Host "  {model}  |  {ctx_k}K context  |  8F pipeline" -ForegroundColor DarkGray
if ($mission) {{ Write-Host "  Mission: $mission" -ForegroundColor {accent} }}
Write-Host ""

# --- Environment ---
$env:CLAUDECODE = ""
$env:{var_name} = "{var_val}"
$env:CEX_ROOT = $cexRoot
$env:CLAUDE_CODE_USE_POWERSHELL_TOOL = "1"
Set-Location $env:CEX_ROOT

# Load .env (secrets for MCP servers, LLM providers). System env wins.
. "$PSScriptRoot\\_shared\\load_dotenv.ps1"

# --- Launch CLI ---
# System prompt (sin identity + domain role) injected via --append-system-prompt
$sysPrompt = @'
{full_prompt}
'@

# Initial message (what the nucleus does on startup)
$initialMsg = @'
{initial}
'@

# Build argument list (avoids PowerShell parsing -- flags as operators)
$cliArgs = @({(flags_array + ', ' if flags_array else '')}"--effort", "max", "--model", "{model}", "--name", "CEX-{nuc_upper}")
$cliArgs += "--append-system-prompt", "{agent_card}"
$cliArgs += "--append-system-prompt", ".cex/P09_config/context_self_select.md"
$cliArgs += "--append-system-prompt", $sysPrompt
{mcp_line}
{settings_line}
$cliArgs += $initialMsg

Set-CexTitle "RUNNING"
& claude @cliArgs
Set-CexTitle "DONE"
'''


def _ascii_clean(s: str) -> str:
    """ASCII-only sanitizer for prompt strings baked into PS1 here-strings."""
    if not s:
        return ""
    s = s.replace('\u2014', '--').replace('\u2013', '-')
    return s.encode('ascii', 'replace').decode('ascii').replace('?', '-')


def _simple_ps1(nucleus: str, cfg: dict, meta: dict, cli: str,
                default_model: str, default_flags: str, launch_cmd: str,
                task_suffix: str) -> str:
    """
    Generic simplified PS1 builder for non-claude CLIs (gemini/codex).
    No sin-aware UX, no --append-system-prompt (CLIs do not support it).
    System context is injected into the initial prompt as a here-string.
    """
    model = cfg.get("model", default_model)
    flags = cfg.get("flags", default_flags)
    legacy_colors = NUCLEUS_COLORS.get(nucleus, NUCLEUS_COLORS["n03"])
    bg = legacy_colors["bg"]
    fg = legacy_colors["fg"]
    accent = legacy_colors["accent"]
    label = legacy_colors["label"]

    nuc_upper = nucleus.upper()
    var_name = meta["var"].split("=")[0]
    var_val = meta["var"].split("=")[1]
    agent_card = meta.get("agent_card", "")
    domain_prompt = _ascii_clean(meta["prompt"])

    flag_parts = flags.split() if flags else []
    flags_array = ", ".join(f'"{f}"' for f in flag_parts)
    flags_prefix = (flags_array + ", ") if flags_array else ""

    handoff_name = f"${{nucleus}}_task{task_suffix}.md"

    return '''# CEX {nuc_upper} -- {meta["title"]} ({cli.upper()})
# Generated by cex_boot_gen.py -- CLI override: {cli}
# Model: {model} | Handoff suffix: {task_suffix or "(default)"}

. $PSScriptRoot/_shared/vt_enable.ps1  # Enable ANSI/VT for TUI
$cexRoot = Split-Path -Parent $PSScriptRoot
$nucleus = "{nucleus}"
. $PSScriptRoot/_shared/theme.ps1  # Per-nucleus theme

# Detect mission from handoff file
$mission = ""
$handoff = "$cexRoot\\.cex\\runtime\\handoffs\\{handoff_name}"
if (Test-Path $handoff) {{
    $content = Get-Content $handoff -Head 10 -EA SilentlyContinue
    foreach ($line in $content) {{
        if ($line -match "^mission:\\s*(.+)$") {{
            $mission = $Matches[1].Trim()
            break
        }}
    }}
}}

function Set-CexTitle($status) {{
    $t = "{nuc_upper} {label} [{cli}]"
    if ($mission) {{ $t += " [$mission]" }}
    $t += " -- $status"
    $Host.UI.RawUI.WindowTitle = $t
}}

Set-CexTitle "BOOTING"

try {{
    $Host.UI.RawUI.BackgroundColor = "{bg}"
    $Host.UI.RawUI.ForegroundColor = "{fg}"
    if (-not $env:CEX_GRID) {{
        $bufSize = $Host.UI.RawUI.BufferSize
        $bufSize.Width = 160; $bufSize.Height = 9999
        $Host.UI.RawUI.BufferSize = $bufSize
        $winSize = $Host.UI.RawUI.WindowSize
        $winSize.Width = [Math]::Min(160, $Host.UI.RawUI.MaxWindowSize.Width)
        $winSize.Height = [Math]::Min(40, $Host.UI.RawUI.MaxWindowSize.Height)
        $Host.UI.RawUI.WindowSize = $winSize
    }}
    Clear-Host
}} catch {{}}

Write-Host ""
Write-Host "  [*] {nuc_upper} {label} via {cli.upper()}" -ForegroundColor {accent}
Write-Host "  ==================================================" -ForegroundColor DarkGray
Write-Host "  {model}  |  8F pipeline  |  handoff: {handoff_name}" -ForegroundColor DarkGray
if ($mission) {{ Write-Host "  Mission: $mission" -ForegroundColor {accent} }}
Write-Host ""

$env:{var_name} = "{var_val}"
$env:CEX_ROOT = $cexRoot
$env:CEX_CLI = "{cli}"
Set-Location $env:CEX_ROOT

# Load .env (secrets for MCP servers, LLM providers). System env wins.
. "$PSScriptRoot\\_shared\\load_dotenv.ps1"

# System context baked into prompt (no --append-system-prompt on {cli})
$sysPrompt = @'
{domain_prompt}

You are running via {cli.upper()} CLI in CEX multi-CLI test mode.
Read the handoff at .cex/runtime/handoffs/{handoff_name.replace("${nucleus}", nucleus)} and execute.
Rules loaded from:
  - .claude/rules/n07-orchestrator.md
  - .claude/rules/{nucleus}-*.md
  - .claude/rules/8f-reasoning.md
  - .claude/rules/ascii-code-rule.md
Your agent card: {agent_card}
Follow 8F pipeline F1->F8. Save output, compile, commit, signal on complete.
'@

# Read handoff inline (bypasses CLI gitignore policy -- gemini respects .gitignore,
# codex does not; this path works for both).
$handoffPath = Join-Path $cexRoot ".cex/runtime/handoffs/{handoff_name.replace("${nucleus}", nucleus)}"
if (Test-Path $handoffPath) {{
    $handoffBody = Get-Content -Raw -LiteralPath $handoffPath
}} else {{
    $handoffBody = "(no handoff at $handoffPath -- report ready and exit)"
}}

$initialMsg = @"
Execute the task described in the handoff BELOW (embedded verbatim -- do NOT try to re-read the path).
Follow its frontmatter (mission, kind, output path) exactly.
Follow the 8F pipeline. Signal on complete.

=== HANDOFF BEGIN ===
$handoffBody
=== HANDOFF END ===

SYSTEM CONTEXT:
$sysPrompt
"@

$cliArgs = @({flags_prefix}"--model", "{model}")
{{extra_args}}

Set-CexTitle "RUNNING"
& {launch_cmd} @cliArgs $initialMsg
Set-CexTitle "DONE"
'''


def build_gemini_ps1(nucleus: str, cfg: dict, meta: dict) -> str:
    try:
        from cex_model_resolver import resolve_model
        _gemini_default = resolve_model(nucleus).get("model", "gemini-2.5-flash-lite")
        # If the resolved model is not a gemini model, use fallback
        if not _gemini_default.startswith("gemini"):
            _gemini_default = "gemini-2.5-flash-lite"
    except Exception:
        _gemini_default = "gemini-2.5-flash-lite"
    tpl = _simple_ps1(
        nucleus, cfg, meta,
        cli="gemini",
        default_model=_gemini_default,
        default_flags="--yolo",
        launch_cmd="gemini",
        task_suffix="_gemini",
    )
    return tpl.replace("{extra_args}", '$cliArgs += "--include-directories", $cexRoot')


def build_codex_ps1(nucleus: str, cfg: dict, meta: dict) -> str:
    tpl = _simple_ps1(
        nucleus, cfg, meta,
        cli="codex",
        default_model="default",
        default_flags="--dangerously-bypass-approvals-and-sandbox -c model_reasoning_effort=high",
        launch_cmd="codex exec",
        task_suffix="_codex",
    )
    # Codex CLI on ChatGPT-plus auth rejects explicit --model
    tpl = tpl.replace(', "--model", "default"', '')
    # Pipe prompt via stdin to avoid Windows cmd-line length limits on long handoffs
    tpl = tpl.replace(
        '& codex exec @cliArgs $initialMsg',
        '$initialMsg | & codex exec @cliArgs -'
    )
    return tpl.replace("{extra_args}", '$cliArgs += "-C", $cexRoot')


# Builders registry -- multi-CLI stack
BUILDERS = {
    "claude": build_claude_ps1,
    "gemini": build_gemini_ps1,
    "codex":  build_codex_ps1,
}


def load_config() -> dict:
    if CONFIG.exists():
        with open(CONFIG, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    elif TEMPLATE.exists():
        print(f"[WARN] No {CONFIG.name} found. Using template.")
        with open(TEMPLATE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    else:
        print("[ERROR] No nucleus_models.yaml or template found.")
        sys.exit(1)


def generate(config: dict, only: str = None, dry_run: bool = False, cli_override: str = None):
    BOOT_DIR.mkdir(exist_ok=True)
    generated = []

    for nucleus, cfg in config.items():
        if only and nucleus != only:
            continue
        if nucleus not in NUCLEUS_META:
            print(f"[SKIP] Unknown nucleus: {nucleus}")
            continue

        meta = NUCLEUS_META[nucleus]
        cli = cli_override if cli_override else cfg.get("cli", "claude")
        builder = BUILDERS.get(cli)

        if not builder:
            print(f"[ERROR] Unknown CLI '{cli}' for {nucleus} -- supported: {list(BUILDERS.keys())}")
            continue

        # When --cli override is set, ignore cfg model/flags (they are claude-specific)
        # and let the builder fall back to its defaults.
        if cli_override:
            cfg_effective = {k: v for k, v in cfg.items() if k not in ("model", "flags")}
        else:
            cfg_effective = cfg
        content = builder(nucleus, cfg_effective, meta)
        # Filename: claude keeps legacy names (n0X.ps1 / cex.ps1), others suffix with _cli
        if cli == "claude":
            if nucleus == "n07":
                path = BOOT_DIR / "cex.ps1"
            else:
                path = BOOT_DIR / f"{nucleus}.ps1"
        else:
            if nucleus == "n07":
                path = BOOT_DIR / f"cex_{cli}.ps1"
            else:
                path = BOOT_DIR / f"{nucleus}_{cli}.ps1"

        if dry_run:
            print(f"\n{'='*60}")
            print(f"  Would write: {path}")
            print(f"  CLI: {cli} | Model: {cfg.get('model','?')}")
            print(f"{'='*60}")
            print(content)
        else:
            path.write_text(content, encoding="utf-8")
            generated.append((path.name, cli, cfg.get('model','?')))

    if not dry_run and generated:
        print(f"[BOOT-GEN] Generated {len(generated)} scripts:")
        for name, cli, model in generated:
            print(f"  OK boot/{name} ({cli} {model})")


def show_table(config: dict):
    print(f"\n{'Nucleus':<10} {'CLI':<10} {'Model':<35} {'Fallback':<20}")
    print("-" * 80)
    for nucleus in ["n07", "n01", "n02", "n03", "n04", "n05", "n06"]:
        cfg = config.get(nucleus, {})
        cli = cfg.get("cli", "?")
        model = cfg.get("model", "?")
        fb = cfg.get("fallback", {})
        fb_str = f"{fb.get('cli','')}/{fb.get('model','')}" if fb else "-"
        print(f"{nucleus.upper():<10} {cli:<10} {model:<35} {fb_str:<20}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true", help="Show generated scripts without writing them.")
    parser.add_argument("--nucleus", help="Generate only the specified nucleus.")
    parser.add_argument("--show", action="store_true", help="Show the current config table.")
    parser.add_argument("--cli", help="Override the configured CLI for generation.")
    args, _ = parser.parse_known_args()
    config = load_config()

    cli_override = args.cli

    if args.show:
        show_table(config)
    elif args.dry_run:
        generate(config, only=args.nucleus, dry_run=True, cli_override=cli_override)
    else:
        generate(config, only=args.nucleus, cli_override=cli_override)
