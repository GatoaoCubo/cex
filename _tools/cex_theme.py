#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX Theme System -- reads nucleus_sins.yaml, outputs color schemes

Usage:
  python _tools/cex_theme.py --show                    # table of all nuclei + colors
  python _tools/cex_theme.py --nucleus n03             # show N03's sin + colors
  python _tools/cex_theme.py --format ps1              # PowerShell color commands
  python _tools/cex_theme.py --format ansi             # ANSI escape codes
  python _tools/cex_theme.py --format css              # CSS classes
  python _tools/cex_theme.py --format html             # HTML color cards
  python _tools/cex_theme.py --banner n03              # print sin banner for N03
  python _tools/cex_theme.py --all-banners             # print all 7 banners

Reads: .cex/P09_config/nucleus_sins.yaml
"""
import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SINS_PATH = ROOT / ".cex" / "config" / "nucleus_sins.yaml"

_cache = None

NUCLEUS_ORDER = ["n01", "n02", "n03", "n04", "n05", "n06", "n07"]
NUCLEUS_LABELS = {
    "n01": "RESEARCH",
    "n02": "MARKETING",
    "n03": "BUILDER",
    "n04": "KNOWLEDGE",
    "n05": "OPERATIONS",
    "n06": "COMMERCIAL",
    "n07": "ORCHESTRATOR",
}


def _load_sins(path: Path = SINS_PATH) -> dict:
    """Load and cache nucleus_sins.yaml."""
    global _cache
    if _cache is not None:
        return _cache
    if not path.exists():
        raise FileNotFoundError(f"nucleus_sins.yaml not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        _cache = yaml.safe_load(f) or {}
    return _cache


def get_sin(nucleus: str) -> dict:
    """Get full sin dict for a nucleus (n01-n07)."""
    sins = _load_sins()
    key = nucleus.lower()[:3]
    if key not in sins:
        raise KeyError(f"Unknown nucleus: {nucleus}. Valid: {list(sins.keys())}")
    return sins[key]


def get_color(nucleus: str, fmt: str = "hex") -> str:
    """Get color in requested format.

    fmt: 'hex', 'css', 'ps_bg', 'ps_fg', 'ps_accent', 'ansi_bg', 'ansi_fg', 'name'
    """
    sin = get_sin(nucleus)
    color = sin.get("color", {})
    return color.get(fmt, color.get("hex", "#ffffff"))


def get_prompt_injection(nucleus: str) -> str:
    """Get the prompt injection text for a nucleus."""
    sin = get_sin(nucleus)
    return sin.get("prompt_injection", "").strip()


def get_lens(nucleus: str) -> str:
    """Get the operational lens text for a nucleus."""
    sin = get_sin(nucleus)
    return sin.get("lens", "").strip()


def render_banner(nucleus: str, use_ansi: bool = True) -> str:
    """Render a colored banner for a nucleus sin.

    Returns ANSI-colored string if use_ansi=True, plain text otherwise.
    """
    sin = get_sin(nucleus)
    nuc = nucleus.lower()[:3]
    label = NUCLEUS_LABELS.get(nuc, nuc.upper())
    icon = sin.get("icon", "?")
    virtue = sin.get("virtue", "?")
    virtue_en = sin.get("virtue_en", "?")
    tagline = sin.get("tagline", "")
    color = sin.get("color", {})

    model_line = "opus-4-6 | 1M context | 8F pipeline"
    bar = "=" * 50

    if use_ansi:
        bg = color.get("ansi_bg", "")
        fg = color.get("ansi_fg", "")
        reset = "\033[0m"
        dim = "\033[2m"

        lines = [
            f"  {bg}{fg} {icon} {nuc.upper()} {virtue} {reset} -- {virtue_en}",
            f"  {dim}{bar}{reset}",
            f"  {fg}{tagline}{reset}" if tagline else "",
            f"  {dim}{model_line}{reset}",
        ]
    else:
        lines = [
            f"  {icon} {nuc.upper()} {virtue} -- {virtue_en}",
            f"  {bar}",
            f"  {tagline}" if tagline else "",
            f"  {model_line}",
        ]

    return "\n".join(line for line in lines if line)


def render_all_banners(use_ansi: bool = True) -> str:
    """Render banners for all 7 nuclei."""
    parts = []
    for nuc in NUCLEUS_ORDER:
        try:
            parts.append(render_banner(nuc, use_ansi=use_ansi))
            parts.append("")
        except (KeyError, FileNotFoundError):
            parts.append(f"  [?] {nuc.upper()} -- sin not configured")
            parts.append("")
    return "\n".join(parts)


def format_ps1(nucleus: str) -> str:
    """Generate PowerShell color commands for a nucleus."""
    sin = get_sin(nucleus)
    color = sin.get("color", {})
    nuc = nucleus.lower()[:3]
    lines = [
        f'# {nuc.upper()} -- {sin.get("virtue", "?")}',
        f'$Host.UI.RawUI.BackgroundColor = "{color.get("ps_bg", "Black")}"',
        f'$Host.UI.RawUI.ForegroundColor = "{color.get("ps_fg", "White")}"',
        f'# Accent: {color.get("ps_accent", "White")}',
    ]
    return "\n".join(lines)


def format_ansi(nucleus: str) -> str:
    """Generate ANSI escape codes for a nucleus."""
    sin = get_sin(nucleus)
    color = sin.get("color", {})
    nuc = nucleus.lower()[:3]
    lines = [
        f'# {nuc.upper()} -- {sin.get("virtue", "?")}',
        f'BG="{color.get("ansi_bg", "")}"',
        f'FG="{color.get("ansi_fg", "")}"',
        f'RESET="\\033[0m"',
    ]
    return "\n".join(lines)


def format_css(nucleus: str) -> str:
    """Generate CSS classes for a nucleus."""
    sin = get_sin(nucleus)
    color = sin.get("color", {})
    nuc = nucleus.lower()[:3]
    hex_color = color.get("hex", "#000")
    return f""".cex-{nuc} {{
  --sin-color: {hex_color};
  --sin-name: "{sin.get('sin', '?')}";
  background-color: {hex_color};
  color: white;
}}"""


def format_html(nucleus: str) -> str:
    """Generate HTML color card for a nucleus."""
    sin = get_sin(nucleus)
    color = sin.get("color", {})
    nuc = nucleus.lower()[:3]
    hex_color = color.get("hex", "#000")
    icon = sin.get("icon", "?")
    virtue = sin.get("virtue", "?")
    tagline = sin.get("tagline", "")
    label = NUCLEUS_LABELS.get(nuc, nuc.upper())
    return f"""<div class="sin-card" style="background:{hex_color};color:white;padding:16px;border-radius:8px;margin:8px">
  <h3>{icon} {nuc.upper()} {label}</h3>
  <p><strong>{virtue}</strong></p>
  <p><em>{tagline}</em></p>
</div>"""


def show_table():
    """Print a table of all nuclei with sins and colors."""
    sins = _load_sins()
    print(f"\n  {'Nuc':<5} {'Icon':<4} {'Sin':<10} {'Virtue':<25} {'Color':<10} {'Hex':<10}")
    print(f"  {'-'*70}")
    for nuc in NUCLEUS_ORDER:
        s = sins.get(nuc, {})
        c = s.get("color", {})
        icon = s.get("icon", "?")
        sin_name = s.get("sin", "?")
        virtue = s.get("virtue", "?")
        color_name = c.get("name", "?")
        hex_val = c.get("hex", "?")
        label = NUCLEUS_LABELS.get(nuc, "")
        print(f"  {nuc.upper():<5} {icon:<4} {sin_name:<10} {virtue:<25} {color_name:<10} {hex_val:<10}  {label}")
    print()


def main():
    parser = argparse.ArgumentParser(description="CEX Theme System")
    parser.add_argument("--show", action="store_true", help="Show all nuclei + colors table")
    parser.add_argument("--nucleus", metavar="N0X", help="Show sin details for one nucleus")
    parser.add_argument("--format", choices=["ps1", "ansi", "css", "html"], help="Export color format")
    parser.add_argument("--banner", metavar="N0X", help="Print sin banner for one nucleus")
    parser.add_argument("--all-banners", action="store_true", help="Print all 7 banners")
    parser.add_argument("--no-ansi", action="store_true", help="Disable ANSI colors")
    args = parser.parse_args()

    if args.show:
        show_table()
        return

    if args.all_banners:
        print(render_all_banners(use_ansi=not args.no_ansi))
        return

    if args.banner:
        print(render_banner(args.banner, use_ansi=not args.no_ansi))
        return

    if args.format:
        formatters = {"ps1": format_ps1, "ansi": format_ansi, "css": format_css, "html": format_html}
        fmt_fn = formatters[args.format]
        if args.nucleus:
            print(fmt_fn(args.nucleus))
        else:
            for nuc in NUCLEUS_ORDER:
                print(fmt_fn(nuc))
                print()
        return

    if args.nucleus:
        sin = get_sin(args.nucleus)
        nuc = args.nucleus.lower()[:3]
        label = NUCLEUS_LABELS.get(nuc, nuc.upper())
        print(f"\n  {nuc.upper()} {label}")
        print(f"  Sin:     {sin.get('sin', '?')} ({sin.get('sin_en', '?')})")
        print(f"  Virtue:  {sin.get('virtue', '?')} ({sin.get('virtue_en', '?')})")
        print(f"  Icon:    {sin.get('icon', '?')}")
        print(f"  Tagline: {sin.get('tagline', '?')}")
        print(f"  Color:   {sin.get('color', {}).get('hex', '?')} ({sin.get('color', {}).get('name', '?')})")
        print(f"\n  Lens:\n    {sin.get('lens', '').strip()}")
        print(f"\n  Prompt Injection:\n    {sin.get('prompt_injection', '').strip()}")
        print()
        return

    parser.print_help()


if __name__ == "__main__":
    main()
