# -*- coding: utf-8 -*-
"""brand_ingest.py -- Ingest messy user files into structured brand signals.

Reads a folder of mixed files (PDF, DOCX, TXT, MD, images, HTML, PPTX)
and extracts brand-relevant signals: names, colors, values, tone, audience.
Output: structured JSON that feeds brand_config_extractor or cex_bootstrap.

Uses markitdown MCP for file conversion when available, falls back to
plain text extraction.

Usage:
    python _tools/brand_ingest.py <folder_path> [--output signals.json]
    python _tools/brand_ingest.py <folder_path> --summary
    python _tools/brand_ingest.py <folder_path> --for-llm  (prompt-ready output)
"""
import sys
import os
import re
import json
from pathlib import Path
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# File types we can process
TEXT_EXTS = {".txt", ".md", ".csv", ".json", ".yaml", ".yml", ".toml", ".env"}
DOC_EXTS = {".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".rtf"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}
WEB_EXTS = {".html", ".htm", ".css"}
ALL_EXTS = TEXT_EXTS | DOC_EXTS | IMAGE_EXTS | WEB_EXTS

# Brand signal patterns
COLOR_HEX = re.compile(r"#[0-9a-fA-F]{6}\b")
COLOR_RGB = re.compile(r"rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)")
FONT_NAMES = re.compile(
    r"(?:font-family|font):\s*['\"]?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)['\"]?",
    re.IGNORECASE,
)
URL_PATTERN = re.compile(r"https?://[^\s\"'<>]+")
EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
SOCIAL_HANDLES = re.compile(r"@[\w.]{3,30}")
PRICE_BRL = re.compile(r"R\$\s*[\d.,]+")
PRICE_USD = re.compile(r"\$\s*[\d.,]+")


def scan_folder(folder: Path) -> dict:
    """Scan a folder and categorize files by type."""
    inventory = {
        "text": [], "docs": [], "images": [], "web": [],
        "unknown": [], "total_size": 0, "total_files": 0,
    }

    for f in folder.rglob("*"):
        if f.is_dir():
            continue
        if f.name.startswith("."):
            continue

        ext = f.suffix.lower()
        size = f.stat().st_size
        info = {"path": str(f), "name": f.name, "ext": ext, "size": size}
        inventory["total_size"] += size
        inventory["total_files"] += 1

        if ext in TEXT_EXTS:
            inventory["text"].append(info)
        elif ext in DOC_EXTS:
            inventory["docs"].append(info)
        elif ext in IMAGE_EXTS:
            inventory["images"].append(info)
        elif ext in WEB_EXTS:
            inventory["web"].append(info)
        else:
            inventory["unknown"].append(info)

    return inventory


def read_text_file(path: Path, max_bytes: int = 50_000) -> str:
    """Read a text file, truncating if too large."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
        if len(content) > max_bytes:
            content = content[:max_bytes] + "\n\n[... truncated ...]"
        return content
    except Exception:
        return ""


def extract_signals_from_text(text: str) -> dict:
    """Extract brand-relevant signals from text content."""
    signals = {
        "colors_hex": list(set(COLOR_HEX.findall(text))),
        "colors_rgb": list(set(COLOR_RGB.findall(text))),
        "fonts": list(set(FONT_NAMES.findall(text))),
        "urls": list(set(URL_PATTERN.findall(text)))[:20],
        "emails": list(set(EMAIL_PATTERN.findall(text)))[:5],
        "social_handles": list(set(SOCIAL_HANDLES.findall(text)))[:10],
        "prices_brl": list(set(PRICE_BRL.findall(text)))[:10],
        "prices_usd": list(set(PRICE_USD.findall(text)))[:10],
    }

    # Detect language
    pt_markers = ["empresa", "marca", "produto", "cliente", "valor", "miss\u00e3o",
                  "vis\u00e3o", "pre\u00e7o", "curso", "venda"]
    en_markers = ["company", "brand", "product", "customer", "value", "mission",
                  "vision", "price", "course", "sale"]

    text_lower = text.lower()
    pt_count = sum(1 for m in pt_markers if m in text_lower)
    en_count = sum(1 for m in en_markers if m in text_lower)
    signals["likely_language"] = "pt-BR" if pt_count > en_count else "en-US"

    # Detect potential brand names (capitalized phrases, repeated)
    caps = re.findall(r"\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2}\b", text)
    name_freq = defaultdict(int)
    for name in caps:
        if len(name) > 2 and name not in {"The", "And", "For", "This", "That", "With"}:
            name_freq[name] += 1
    signals["potential_names"] = sorted(
        name_freq.keys(), key=lambda k: name_freq[k], reverse=True
    )[:10]

    # Detect potential values/principles
    value_patterns = [
        r"(?:values?|valores?|princip[io]s?|pilares?)[\s:]+(.+?)(?:\n|$)",
        r"(?:we believe|acreditamos|nosso[s]? valor)[\s:]+(.+?)(?:\n|$)",
    ]
    values_found = []
    for pat in value_patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        values_found.extend(matches)
    signals["potential_values"] = values_found[:10]

    # Detect potential mission/vision
    mission_pats = [
        "(?:miss[a\u00e3]o|mission)[\\s:]+(.+?)(?:\\n|$)",
        "(?:vis[a\u00e3]o|vision)[\\s:]+(.+?)(?:\\n|$)",
    ]
    for pat in mission_pats:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            key = "potential_mission" if "miss" in pat else "potential_vision"
            signals[key] = matches[0].strip()[:500]

    # Detect potential taglines (short impactful phrases)
    tagline_pats = [
        r"(?:tagline|slogan|lema)[\s:]+[\"']?(.+?)[\"']?(?:\n|$)",
    ]
    for pat in tagline_pats:
        matches = re.findall(pat, text, re.IGNORECASE)
        if matches:
            signals["potential_tagline"] = matches[0].strip()[:100]

    return signals


def merge_signals(all_signals: list[dict]) -> dict:
    """Merge signals from multiple files into consolidated brand signals."""
    merged = {
        "colors_hex": [], "colors_rgb": [], "fonts": [],
        "urls": [], "emails": [], "social_handles": [],
        "prices_brl": [], "prices_usd": [],
        "potential_names": [], "potential_values": [],
        "likely_language": "pt-BR",
    }

    lang_votes = {"pt-BR": 0, "en-US": 0}

    for sig in all_signals:
        for key in ["colors_hex", "colors_rgb", "fonts", "urls", "emails",
                     "social_handles", "prices_brl", "prices_usd",
                     "potential_names", "potential_values"]:
            merged[key].extend(sig.get(key, []))

        lang = sig.get("likely_language", "pt-BR")
        lang_votes[lang] = lang_votes.get(lang, 0) + 1

        for key in ["potential_mission", "potential_vision", "potential_tagline"]:
            if key in sig and key not in merged:
                merged[key] = sig[key]

    # Deduplicate and sort by frequency
    for key in ["colors_hex", "fonts", "potential_names"]:
        freq = defaultdict(int)
        for item in merged[key]:
            freq[item] += 1
        merged[key] = sorted(freq.keys(), key=lambda k: freq[k], reverse=True)[:10]

    for key in ["colors_rgb", "urls", "emails", "social_handles",
                "prices_brl", "prices_usd", "potential_values"]:
        merged[key] = list(set(merged[key]))[:10]

    merged["likely_language"] = max(lang_votes, key=lang_votes.get)

    return merged


def ingest(folder: Path) -> dict:
    """Full ingest pipeline: scan -> read -> extract -> merge."""
    inventory = scan_folder(folder)
    all_signals = []
    source_texts = []

    # Process text files
    for info in inventory["text"]:
        path = Path(info["path"])
        text = read_text_file(path)
        if text:
            signals = extract_signals_from_text(text)
            signals["source"] = info["name"]
            all_signals.append(signals)
            source_texts.append({"file": info["name"], "content": text[:5000]})

    # Process web files (HTML/CSS)
    for info in inventory["web"]:
        path = Path(info["path"])
        text = read_text_file(path)
        if text:
            signals = extract_signals_from_text(text)
            signals["source"] = info["name"]
            all_signals.append(signals)
            source_texts.append({"file": info["name"], "content": text[:5000]})

    merged = merge_signals(all_signals)
    merged["inventory"] = {
        "total_files": inventory["total_files"],
        "total_size_kb": round(inventory["total_size"] / 1024, 1),
        "text_files": len(inventory["text"]),
        "doc_files": len(inventory["docs"]),
        "image_files": len(inventory["images"]),
        "web_files": len(inventory["web"]),
        "doc_names": [d["name"] for d in inventory["docs"]],
        "image_names": [i["name"] for i in inventory["images"]],
    }
    merged["source_excerpts"] = source_texts[:10]

    return merged


def format_for_llm(signals: dict) -> str:
    """Format extracted signals as a prompt for LLM brand synthesis."""
    parts = []
    parts.append("# Brand Signals Extracted from User Files")
    parts.append("")
    parts.append("I ingested the user's files and found these brand signals.")
    parts.append("Use them to fill brand_config.yaml. Ask the user to confirm/correct.")
    parts.append("")

    inv = signals.get("inventory", {})
    parts.append(f"## Source: {inv.get('total_files', 0)} files, {inv.get('total_size_kb', 0)}KB")
    if inv.get("doc_names"):
        parts.append(f"- Documents (need markitdown): {', '.join(inv['doc_names'])}")
    if inv.get("image_names"):
        parts.append(f"- Images (may contain logos/palette): {', '.join(inv['image_names'])}")
    parts.append("")

    # Names
    if signals.get("potential_names"):
        parts.append("## Potential Brand Names (by frequency)")
        for i, name in enumerate(signals["potential_names"][:5], 1):
            parts.append(f"  {i}. {name}")
        parts.append("")

    # Tagline/Mission/Vision
    for key, label in [("potential_tagline", "Tagline"), ("potential_mission", "Mission"),
                        ("potential_vision", "Vision")]:
        if key in signals:
            parts.append(f"## {label} (detected)")
            parts.append(f"  > {signals[key]}")
            parts.append("")

    # Values
    if signals.get("potential_values"):
        parts.append("## Values (detected)")
        for v in signals["potential_values"][:5]:
            parts.append(f"  - {v}")
        parts.append("")

    # Visual
    if signals.get("colors_hex"):
        parts.append("## Colors Found")
        for c in signals["colors_hex"][:6]:
            parts.append(f"  - {c}")
        parts.append("")

    if signals.get("fonts"):
        parts.append("## Fonts Found")
        for f in signals["fonts"][:3]:
            parts.append(f"  - {f}")
        parts.append("")

    # Market signals
    if signals.get("prices_brl") or signals.get("prices_usd"):
        parts.append("## Pricing Signals")
        for p in (signals.get("prices_brl", []) + signals.get("prices_usd", []))[:5]:
            parts.append(f"  - {p}")
        parts.append("")

    if signals.get("urls"):
        parts.append("## URLs Found")
        for u in signals["urls"][:5]:
            parts.append(f"  - {u}")
        parts.append("")

    if signals.get("social_handles"):
        parts.append("## Social Handles")
        for h in signals["social_handles"][:5]:
            parts.append(f"  - {h}")
        parts.append("")

    parts.append(f"## Language: {signals.get('likely_language', 'unknown')}")
    parts.append("")

    # Source excerpts
    if signals.get("source_excerpts"):
        parts.append("## Source Excerpts (first 5KB per file)")
        for src in signals["source_excerpts"][:5]:
            parts.append(f"### {src['file']}")
            parts.append(f"```")
            parts.append(src["content"][:2000])
            parts.append(f"```")
            parts.append("")

    parts.append("## Instructions")
    parts.append("1. Present these signals to the user for confirmation")
    parts.append("2. Ask about anything missing (especially: archetype, ICP, transformation)")
    parts.append("3. For documents (PDF/DOCX), use markitdown MCP to read them")
    parts.append("4. For images, describe what you see (logos, color schemes)")
    parts.append("5. Once confirmed, generate brand_config.yaml and run bootstrap")

    return "\n".join(parts)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Ingest messy user files into brand signals"
    )
    parser.add_argument("folder", help="Path to folder with user's brand files")
    parser.add_argument("--output", "-o", help="Save signals to JSON file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    parser.add_argument("--for-llm", action="store_true", help="Format as LLM prompt")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        print(f"ERROR: folder not found: {folder}")
        sys.exit(1)

    signals = ingest(folder)

    if args.for_llm:
        print(format_for_llm(signals))
    elif args.summary:
        inv = signals["inventory"]
        print(f"Scanned: {inv['total_files']} files ({inv['total_size_kb']}KB)")
        print(f"  Text: {inv['text_files']} | Docs: {inv['doc_files']} | Images: {inv['image_files']} | Web: {inv['web_files']}")
        if signals.get("potential_names"):
            print(f"  Names: {', '.join(signals['potential_names'][:3])}")
        if signals.get("colors_hex"):
            print(f"  Colors: {', '.join(signals['colors_hex'][:3])}")
        if signals.get("fonts"):
            print(f"  Fonts: {', '.join(signals['fonts'][:3])}")
        print(f"  Language: {signals.get('likely_language', '?')}")
    else:
        if args.output:
            out = {k: v for k, v in signals.items() if k != "source_excerpts"}
            Path(args.output).write_text(
                json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"Signals saved to {args.output}")
        else:
            print(json.dumps(signals, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
