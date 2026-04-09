#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Boot Generator -- reads nucleus_models.yaml -> generates boot/*.cmd

Usage:
  python _tools/cex_boot_gen.py              # generate all boot scripts
  python _tools/cex_boot_gen.py --dry-run    # show what would be generated
  python _tools/cex_boot_gen.py --nucleus n03  # generate one
  python _tools/cex_boot_gen.py --show       # show current config table

Reads:  .cex/config/nucleus_models.yaml
Writes: boot/n0{1-6}.cmd + boot/cex.cmd + fallback scripts
"""
import yaml, sys, os
from pathlib import Path

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
        "prompt": "You are N03 Builder Nucleus of CEX. 8F pipeline mandatory. Read .claude/rules/n03-8f-enforcement.md and N03_engineering/agents/agent_engineering.md. IF .cex/runtime/handoffs/n03_task.md EXISTS, READ AND EXECUTE IMMEDIATELY.",
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
    model = cfg.get("model", "claude-sonnet-4-6")
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
    settings_line = f'$args += "--settings", "{ROOT}\\{settings}"' if settings else "# no settings"

    nuc_upper = nucleus.upper()
    ctx_k = ctx // 1000
    var_name = meta["var"].split("=")[0]
    var_val = meta["var"].split("=")[1]
    agent_card = meta.get("agent_card", "")
    initial = meta.get("initial", "Ready.")

    return f'''# CEX {nuc_upper} -- {meta["title"]}
# Generated by cex_boot_gen.py from .cex/config/nucleus_models.yaml + nucleus_sins.yaml
# CLI: claude | Model: {model} | Context: {ctx}
# Sin: {virtue_display} ({virtue_en_display})

# --- UX: Window title with mission + sin + status ---
$cexRoot = "{ROOT}"
$nucleus = "{nucleus}"
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
    if ($gitRemote -match "[/:]([^/]+?)(?:\.git)?$") {{ $gitRepo = $Matches[1] }}
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
$cliArgs = @({(flags_array + ', ' if flags_array else '')}"--model", "{model}", "--name", "CEX-{nuc_upper}")
$cliArgs += "--append-system-prompt", "{agent_card}"
$cliArgs += "--append-system-prompt", ".cex/config/context_self_select.md"
$cliArgs += "--append-system-prompt", $sysPrompt
{mcp_line}
{settings_line}
$cliArgs += $initialMsg

Set-CexTitle "RUNNING"
& claude @cliArgs
Set-CexTitle "DONE"
'''


# Legacy CMD format (kept for fallback/compatibility)
def build_claude_cmd(nucleus: str, cfg: dict, meta: dict) -> str:
    model = cfg.get("model", "claude-sonnet-4-6")
    flags = cfg.get("flags", "--dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome")
    mcps = cfg.get("mcps", "")
    settings = cfg.get("settings", "")

    lines = [
        "@echo off",
        f":: CEX {nucleus.upper()} -- {meta['title']}",
        f":: Generated by cex_boot_gen.py from .cex/config/nucleus_models.yaml",
        f":: CLI: claude | Model: {model}",
        "",
        f"title {meta['title']}",
        "set CLAUDECODE=",
        f"set {meta['var']}",
        f"set CEX_ROOT={ROOT}",
        'cd /d "%CEX_ROOT%"',
        "",
        f"set MODEL=--model {model}",
        f"set NAME=--name CEX-{nucleus.upper()}",
        f"set FLAGS={flags}",
    ]
    if mcps:
        lines.append(f'set MCP=--mcp-config %CEX_ROOT%\\{mcps.replace("/", chr(92))}')
    else:
        lines.append("set MCP=")
    if settings:
        lines.append(f'set SETTINGS=--settings %CEX_ROOT%\\{settings.replace("/", chr(92))}')
    else:
        lines.append("set SETTINGS=")

    lines += [
        "",
        ":: ALWAYS interactive -- task comes from handoff file, never CLI args",
        f'claude %FLAGS% %NAME% %MODEL% %MCP% %SETTINGS% "{meta["prompt"]}"',
    ]
    return "\n".join(lines) + "\n"


def build_gemini_cmd(nucleus: str, cfg: dict, meta: dict) -> str:
    model = cfg.get("model", "gemini-2.5-pro")
    flags = cfg.get("flags", "--yolo")

    return "\n".join([
        "@echo off",
        f":: CEX {nucleus.upper()} -- {meta['title']}",
        f":: Generated by cex_boot_gen.py from .cex/config/nucleus_models.yaml",
        f":: CLI: gemini | Model: {model}",
        "",
        f"title {meta['title']}",
        f"set {meta['var']}",
        f"set CEX_ROOT={ROOT}",
        'cd /d "%CEX_ROOT%"',
        "",
        ":: Force subscription OAuth (clear API keys)",
        "set GOOGLE_API_KEY=",
        "set GEMINI_API_KEY=",
        "set GOOGLE_AI_API_KEY=",
        "",
        ":: ALWAYS interactive -- task comes from handoff file, never CLI args",
        f'gemini -m {model} {flags} "{meta["prompt"]}"',
    ]) + "\n"


def build_codex_cmd(nucleus: str, cfg: dict, meta: dict) -> str:
    model = cfg.get("model", "o3")
    flags = cfg.get("flags", "--full-auto")

    return "\n".join([
        "@echo off",
        f":: CEX {nucleus.upper()} -- {meta['title']}",
        f":: Generated by cex_boot_gen.py from .cex/config/nucleus_models.yaml",
        f":: CLI: codex | Model: {model}",
        "",
        f"title {meta['title']}",
        f"set {meta['var']}",
        f"set CEX_ROOT={ROOT}",
        'cd /d "%CEX_ROOT%"',
        "",
        ":: ALWAYS interactive -- task comes from handoff file, never CLI args",
        f'codex -m {model} {flags} "{meta["prompt"]}"',
    ]) + "\n"


def build_pi_cmd(nucleus: str, cfg: dict, meta: dict) -> str:
    """DEPRECATED: pi CLI is no longer supported. Use claude CLI instead."""
    # Redirect to claude CMD builder as fallback
    return build_claude_cmd(nucleus, cfg, meta)


def build_ollama_cmd(nucleus: str, cfg: dict, meta: dict) -> str:
    model = cfg.get("model", "qwen3:32b")
    flags = cfg.get("flags", "")

    return "\n".join([
        "@echo off",
        f":: CEX {nucleus.upper()} -- {meta['title']}",
        f":: Generated by cex_boot_gen.py from .cex/config/nucleus_models.yaml",
        f":: CLI: ollama | Model: {model}",
        "",
        f"title {meta['title']}",
        f"set {meta['var']}",
        f"set CEX_ROOT={ROOT}",
        'cd /d "%CEX_ROOT%"',
        "",
        ":: Local model -- no API keys needed",
        f'ollama run {model}',
    ]) + "\n"


# Primary builders (PowerShell -- rich UX)
BUILDERS_PS1 = {
    "claude": build_claude_ps1,
}

# Legacy builders (CMD -- fallback for non-PS environments)
BUILDERS_CMD = {
    "claude": build_claude_cmd,
    "gemini": build_gemini_cmd,
    "codex": build_codex_cmd,
    "pi": build_pi_cmd,
    "ollama": build_ollama_cmd,
}

# Default: PS1 if available, else CMD
BUILDERS = {**BUILDERS_CMD}  # base
BUILDERS.update(BUILDERS_PS1)  # override with PS1 where available


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


def generate(config: dict, only: str = None, dry_run: bool = False):
    BOOT_DIR.mkdir(exist_ok=True)
    generated = []

    for nucleus, cfg in config.items():
        if only and nucleus != only:
            continue
        if nucleus not in NUCLEUS_META:
            print(f"[SKIP] Unknown nucleus: {nucleus}")
            continue

        meta = NUCLEUS_META[nucleus]
        cli = cfg.get("cli", "claude")
        builder = BUILDERS.get(cli)

        if not builder:
            print(f"[ERROR] Unknown CLI '{cli}' for {nucleus}")
            continue

        # Main boot script -- PS1 for PowerShell builders, CMD for legacy
        content = builder(nucleus, cfg, meta)
        is_ps1 = cli in BUILDERS_PS1
        ext = ".ps1" if is_ps1 else ".cmd"
        if nucleus == "n07":
            path = BOOT_DIR / f"cex{ext}"
        else:
            path = BOOT_DIR / f"{nucleus}{ext}"

        if dry_run:
            print(f"\n{'='*60}")
            print(f"  Would write: {path}")
            print(f"  CLI: {cli} | Model: {cfg.get('model','?')}")
            print(f"{'='*60}")
            print(content)
        else:
            path.write_text(content, encoding="utf-8")
            generated.append((path.name, cli, cfg.get('model','?')))

        # Fallback script (if defined)
        fb = cfg.get("fallback")
        if fb:
            fb_cli = fb.get("cli", "claude")
            fb_builder = BUILDERS.get(fb_cli)
            if fb_builder:
                fb_content = fb_builder(nucleus, fb, meta)
                fb_path = BOOT_DIR / f"{nucleus}-{fb_cli}.cmd"
                if dry_run:
                    print(f"\n  [FALLBACK] Would write: {fb_path}")
                    print(f"  CLI: {fb_cli} | Model: {fb.get('model','?')}")
                else:
                    fb_path.write_text(fb_content, encoding="utf-8")
                    generated.append((fb_path.name, f"fallback:{fb_cli}", fb.get('model','?')))

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
    args = sys.argv[1:]
    config = load_config()

    if "--help" in args:
        print(__doc__)
    elif "--show" in args:
        show_table(config)
    elif "--dry-run" in args:
        nucleus = args[args.index("--nucleus") + 1] if "--nucleus" in args else None
        generate(config, only=nucleus, dry_run=True)
    else:
        nucleus = args[args.index("--nucleus") + 1] if "--nucleus" in args else None
        generate(config, only=nucleus)
