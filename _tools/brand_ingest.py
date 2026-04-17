# -*- coding: utf-8 -*-
"""brand_ingest.py -- Ingest brand signals from folder, URL, GitHub repo, or file.

Usage:
    python _tools/brand_ingest.py <folder>            # scan folder (original)
    python _tools/brand_ingest.py --url <url>         # scrape website
    python _tools/brand_ingest.py --repo <gh_url>     # read GitHub repo
    python _tools/brand_ingest.py --file <path>       # single file
    python _tools/brand_ingest.py <folder> --summary
    python _tools/brand_ingest.py --url <url> --for-llm
"""
import sys
import os
import re
import json
import urllib.request
import urllib.parse
import urllib.error
import html.parser
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
    _STOPWORDS = {
        "The", "And", "For", "This", "That", "With", "From", "Into", "Over",
        "Under", "About", "After", "Before", "Between", "Through", "During",
        "Learn", "More", "Read", "Click", "Get", "Use", "Find", "See", "View",
        "Error", "Warning", "Info", "True", "False", "None", "Null", "Ok",
        "Yes", "No", "New", "Old", "All", "Any", "Not", "Our", "Your", "Their",
        "Its", "His", "Her", "We", "You", "They", "He", "She", "It", "Who",
        "What", "When", "Where", "Why", "How", "Can", "May", "Will", "Should",
        "Must", "Have", "Has", "Had", "Was", "Were", "Been", "Being", "Are",
        "Does", "Did", "Done", "Copyright", "Privacy", "Terms", "Policy",
        "Login", "Sign", "Home", "Menu", "Blog", "Page", "Site", "Web",
        "Http", "Https", "Www", "Com", "Org", "Net", "Dns", "Ip", "Api",
    }
    caps = re.findall(r"\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2}\b", text)
    name_freq = defaultdict(int)
    for name in caps:
        if len(name) > 2 and name not in _STOPWORDS:
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


# ---------------------------------------------------------------------------
# HTML parser helper (stdlib only, no beautifulsoup dependency)
# ---------------------------------------------------------------------------

class _TextExtractor(html.parser.HTMLParser):
    """Extract visible text and meta tags from HTML."""

    SKIP_TAGS = {"script", "style", "noscript", "head", "nav", "footer", "aside"}

    def __init__(self):
        super().__init__()
        self._skip = 0
        self.text_parts = []
        self.meta = {}
        self.colors = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self._skip += 1
        attr_dict = dict(attrs)
        if tag == "meta":
            name = attr_dict.get("name", attr_dict.get("property", ""))
            content = attr_dict.get("content", "")
            if name and content:
                self.meta[name.lower()] = content
        if tag in ("link", "a") and attr_dict.get("href", "").endswith(".css"):
            pass
        if "style" in attr_dict:
            colors = COLOR_HEX.findall(attr_dict["style"])
            self.colors.extend(colors)

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS and self._skip > 0:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip == 0:
            stripped = data.strip()
            if stripped:
                self.text_parts.append(stripped)

    def get_text(self):
        return " ".join(self.text_parts)


def _fetch_url(url: str, timeout: int = 10) -> str:
    """Fetch URL content as text. Returns empty string on error."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CEX-brand-ingest/1.0)"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(500_000)
            charset = "utf-8"
            ct = resp.headers.get("Content-Type", "")
            m = re.search(r"charset=([^\s;]+)", ct)
            if m:
                charset = m.group(1).strip()
            return raw.decode(charset, errors="replace")
    except Exception as exc:
        sys.stderr.write(f"[WARN] fetch {url}: {exc}\n")
        return ""


def _ingest_via_firecrawl(url: str, signals: dict) -> dict:
    """Use Firecrawl API for richer content extraction."""
    import json as _json
    api_key = os.environ.get("FIRECRAWL_API_KEY", "")
    endpoint = "https://api.firecrawl.dev/v1/scrape"
    payload = json.dumps({
        "url": url,
        "formats": ["markdown", "extract"],
        "extract": {"prompt": "Extract brand name, tagline, colors, values, mission, target audience"}
    }).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    try:
        req = urllib.request.Request(endpoint, data=payload, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = _json.loads(resp.read().decode("utf-8", errors="replace"))
        text = data.get("data", {}).get("markdown", "")
        if not text:
            text = str(data)
        extracted = data.get("data", {}).get("extract", {}) or {}
        sig = extract_signals_from_text(text)
        if extracted.get("tagline"):
            sig["potential_tagline"] = extracted["tagline"]
        if extracted.get("colors"):
            sig["colors_hex"].extend(extracted["colors"])
        sig["source"] = url
        sig["source_text"] = text[:5000]
        signals.update(sig)
        return signals
    except Exception as exc:
        sys.stderr.write(f"[WARN] firecrawl failed ({exc}), falling back to requests\n")
        return _ingest_via_requests(url, signals)


def _ingest_via_requests(url: str, signals: dict) -> dict:
    """Plain HTTP extraction for homepage + /about + /pricing."""
    base = url.rstrip("/")
    paths = ["", "/about", "/pricing", "/sobre", "/sobre-nos"]
    combined_text = ""
    all_colors = []

    for path in paths:
        target = base + path
        html_content = _fetch_url(target)
        if not html_content:
            continue
        parser = _TextExtractor()
        try:
            parser.feed(html_content)
        except Exception:
            pass
        text = parser.get_text()
        combined_text += "\n" + text
        all_colors.extend(parser.colors)

        # Merge meta tags
        for k, v in parser.meta.items():
            if k in ("description", "og:description") and not signals.get("potential_tagline"):
                signals["potential_tagline"] = v[:200]
            if k in ("og:title", "title") and not signals.get("potential_brand_name"):
                signals["potential_brand_name"] = v

        # Extract colors from raw CSS references
        raw_colors = COLOR_HEX.findall(html_content)
        all_colors.extend(raw_colors)

    sig = extract_signals_from_text(combined_text)
    sig["colors_hex"] = list(set(sig.get("colors_hex", []) + all_colors))[:10]
    sig["source"] = url
    sig["source_text"] = combined_text[:5000]
    signals.update(sig)
    return signals


def ingest_url(url: str) -> dict:
    """Fetch brand signals from a website URL."""
    signals = {
        "colors_hex": [], "colors_rgb": [], "fonts": [],
        "urls": [], "emails": [], "social_handles": [],
        "prices_brl": [], "prices_usd": [],
        "potential_names": [], "potential_values": [],
        "likely_language": "pt-BR",
        "source_mode": "url",
        "inventory": {
            "total_files": 0, "total_size_kb": 0,
            "text_files": 0, "doc_files": 0, "image_files": 0, "web_files": 1,
            "doc_names": [], "image_names": [],
        },
    }

    # Quick connectivity check before full ingest
    probe = _fetch_url(url)
    if not probe:
        sys.stderr.write(
            "[WARN] Could not reach %s\n"
            "[HINT] The site may be:\n"
            "  a) Unreachable from this machine (DNS / firewall)\n"
            "  b) JavaScript-rendered (needs FIRECRAWL_API_KEY for full extraction)\n"
            "  c) Blocking bots -- try /init <folder> with downloaded brand files instead\n" % url
        )
        signals["source_mode"] = "url_failed"
        return signals

    if os.environ.get("FIRECRAWL_API_KEY"):
        result = _ingest_via_firecrawl(url, signals)
    else:
        result = _ingest_via_requests(url, signals)
        # Warn if very little content was extracted (likely JS-rendered)
        text = result.get("source_text", "")
        if len(text) < 200 and not result.get("potential_brand_name"):
            sys.stderr.write(
                "[WARN] Extracted very little content from %s\n"
                "[HINT] Site may use JavaScript rendering.\n"
                "  Set FIRECRAWL_API_KEY for richer extraction, or use:\n"
                "  brand_ingest.py <folder>  with downloaded brand materials\n" % url
            )

    # Build source_excerpts compat key
    src_text = result.pop("source_text", "")
    result["source_excerpts"] = [{"file": url, "content": src_text[:5000]}] if src_text else []
    return result


def ingest_repo(repo_url: str) -> dict:
    """Fetch brand signals from a GitHub repository."""
    # Parse owner/repo from URL
    m = re.search(r"github\.com/([^/]+)/([^/?\s]+)", repo_url)
    if not m:
        sys.stderr.write(f"[WARN] Cannot parse GitHub URL: {repo_url}\n")
        return {}
    owner, repo = m.group(1), m.group(2).rstrip("/")

    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/main"
    api_base = f"https://api.github.com/repos/{owner}/{repo}"

    files_to_try = [
        "README.md", "readme.md", "README.rst",
        "docs/brand.md", "docs/about.md", "CONTRIBUTING.md",
        ".github/README.md",
    ]

    combined_text = ""
    fetched_count = 0
    for fname in files_to_try:
        content = _fetch_url(f"{raw_base}/{fname}")
        if content:
            combined_text += f"\n\n### {fname}\n{content[:10000]}"
            fetched_count += 1

    # Get repo description via GitHub API
    api_data_raw = _fetch_url(api_base)
    if api_data_raw:
        try:
            api_data = json.loads(api_data_raw)
            desc = api_data.get("description", "")
            if desc:
                combined_text = f"Description: {desc}\n\n" + combined_text
        except Exception:
            pass

    if not combined_text.strip():
        sys.stderr.write(
            "[WARN] Could not read any files from %s/%s\n"
            "[HINT] If this is a private repo, set GITHUB_PAT env var:\n"
            "  export GITHUB_PAT=ghp_your_token\n"
            "  Or clone the repo locally and use: brand_ingest.py <folder>\n" % (owner, repo)
        )

    sig = extract_signals_from_text(combined_text)
    sig["source"] = repo_url
    sig["source_mode"] = "repo"
    sig["inventory"] = {
        "total_files": 1, "total_size_kb": round(len(combined_text) / 1024, 1),
        "text_files": 1, "doc_files": 0, "image_files": 0, "web_files": 0,
        "doc_names": [], "image_names": [],
    }
    sig["source_excerpts"] = [{"file": repo_url, "content": combined_text[:5000]}]
    return sig


def ingest_file(file_path: str) -> dict:
    """Ingest a single file (MD, TXT, PDF, DOCX)."""
    path = Path(file_path)
    if not path.exists():
        sys.stderr.write(f"[WARN] File not found: {file_path}\n")
        return {}

    ext = path.suffix.lower()
    text = ""

    if ext in TEXT_EXTS:
        text = read_text_file(path)
    elif ext in DOC_EXTS:
        # Try markitdown if available
        try:
            import subprocess
            result = subprocess.run(
                ["python", "-m", "markitdown", str(path)],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0 and result.stdout:
                text = result.stdout
        except Exception:
            pass
        if not text:
            text = path.read_bytes().decode("utf-8", errors="replace")[:50_000]
    else:
        text = path.read_bytes().decode("utf-8", errors="replace")[:50_000]

    sig = extract_signals_from_text(text)
    sig["source"] = str(path)
    sig["source_mode"] = "file"
    sig["inventory"] = {
        "total_files": 1, "total_size_kb": round(path.stat().st_size / 1024, 1),
        "text_files": 1 if ext in TEXT_EXTS else 0,
        "doc_files": 1 if ext in DOC_EXTS else 0,
        "image_files": 0, "web_files": 0,
        "doc_names": [path.name] if ext in DOC_EXTS else [],
        "image_names": [],
    }
    sig["source_excerpts"] = [{"file": path.name, "content": text[:5000]}]
    return sig


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Ingest brand signals from folder, URL, GitHub repo, or file"
    )
    # Folder is optional now (was positional)
    parser.add_argument("folder", nargs="?", default=None,
                        help="Path to folder with brand files (original mode)")
    parser.add_argument("--url", default=None, help="Scrape a website URL for brand signals")
    parser.add_argument("--repo", default=None, help="Read a GitHub repo for brand signals")
    parser.add_argument("--file", default=None, dest="single_file",
                        help="Ingest a single file (MD/TXT/PDF/DOCX)")
    parser.add_argument("--output", "-o", help="Save signals to JSON file")
    parser.add_argument("--summary", action="store_true", help="Print summary only")
    parser.add_argument("--for-llm", action="store_true", help="Format as LLM prompt")
    args = parser.parse_args()

    # Route to the right ingestion mode
    if args.url:
        signals = ingest_url(args.url)
    elif args.repo:
        signals = ingest_repo(args.repo)
    elif args.single_file:
        signals = ingest_file(args.single_file)
    elif args.folder:
        folder = Path(args.folder)
        if not folder.exists():
            print(f"ERROR: folder not found: {folder}")
            sys.exit(1)
        signals = ingest(folder)
    else:
        parser.print_help()
        sys.exit(1)

    if args.for_llm:
        print(format_for_llm(signals))
    elif args.summary:
        inv = signals.get("inventory", {})
        mode = signals.get("source_mode", "folder")
        print(f"Mode: {mode} | Source: {signals.get('source', args.folder or '')}")
        print(f"Scanned: {inv.get('total_files', 1)} file(s) ({inv.get('total_size_kb', 0)}KB)")
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
