#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_notebooklm.py -- CEX NotebookLM Pipeline Tool.

Unified CLI for uploading KCs to Google NotebookLM notebooks,
activating Estudio outputs, and managing domain-notebook mappings.

Subcommands:
  --upload <kc_path>    Upload a KC as source to a domain notebook
  --studio <id>         Activate Estudio outputs (flashcards, audio, quiz)
  --status <id>         Check notebook status (sources, outputs)
  --list                List all tracked notebooks with domain mapping
  --reauth              Re-authenticate Google session

Spec: _docs/specs/spec_notebooklm_pipeline.md
Config: .cex/P09_config/notebooklm_notebooks.yaml

Usage:
  python _tools/cex_notebooklm.py --upload P01_knowledge/library/kind/kc_agent.md
  python _tools/cex_notebooklm.py --studio 940fd258-847f-47c1-b7e6-caca7b730681
  python _tools/cex_notebooklm.py --status 940fd258-847f-47c1-b7e6-caca7b730681
  python _tools/cex_notebooklm.py --list
  python _tools/cex_notebooklm.py --reauth
  python _tools/cex_notebooklm.py --auth-check
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

# --- Paths ---

CEX_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = CEX_ROOT / ".cex" / "config" / "notebooklm_notebooks.yaml"
SCREENSHOT_DIR = CEX_ROOT / "_tools" / "screenshots" / "notebooklm"
NOTEBOOKLM_BASE = "https://notebooklm.google.com"

# Cookie state from NotebookLM MCP server
_LOCAL = os.environ.get("LOCALAPPDATA", "")
STATE_FILE = Path(_LOCAL) / "notebooklm-mcp" / "Data" / "browser_state" / "state.json" if _LOCAL else None

# Source limit per notebook (NotebookLM hard limit is 50)
SOURCE_WARN_THRESHOLD = 45
SOURCE_HARD_LIMIT = 50

# Max chars per source (NotebookLM limit is 500K words ~ 2.5M chars, we use 200K safely)
MAX_SOURCE_CHARS = 200000

# --- PT-BR UI Selectors (NotebookLM Angular Material) ---
# Using unicode escapes for accented chars per ASCII-only code rule

SELECTORS = {
    "add_source": [
        'button:has-text("Adicionar fontes")',
        '[aria-label*="Adicionar"]',
        'button:has-text("Add source")',
    ],
    "copied_text": [
        ':text("Texto copiado")',
        'button:has-text("Texto copiado")',
        ':text("Copied text")',
        'button:has-text("Copied text")',
    ],
    "title_input": [
        'input[formcontrolname="title"]',
        "input[placeholder*=\"t\\u00edtulo\"]",
        'input[placeholder*="title"]',
        'mat-dialog-container input',
        '.cdk-overlay-pane input',
    ],
    "content_area": [
        'textarea[aria-label="Texto colado"]',
        'textarea[formcontrolname="pastedText"]',
        '.cdk-overlay-pane textarea',
        'mat-dialog-container textarea',
        '[role="dialog"] textarea',
    ],
    "insert_btn": [
        '.cdk-overlay-pane button:has-text("Inserir")',
        '[role="dialog"] button:has-text("Inserir")',
        'button:has-text("Inserir")',
        'button:has-text("Insert")',
    ],
    "studio_panel": [
        ':text("Est\\u00fadio")',
        '[aria-label*="Studio"]',
        '[aria-label*="Est\\u00fadio"]',
    ],
}

# Estudio output button labels (PT-BR)
STUDIO_OUTPUTS = {
    "flashcards": [
        ':text("Cart\\u00f5es did\\u00e1ticos")',
        ':text("Flashcards")',
    ],
    "audio_summary": [
        ':text("Resumo em \\u00e1udio")',
        ':text("Audio Overview")',
    ],
    "quiz": [
        ':text("Teste")',
        ':text("Quiz")',
    ],
    "mind_map": [
        ':text("Mapa mental")',
        ':text("Mind map")',
    ],
    "briefing": [
        ':text("Documento de resumo")',
        ':text("Briefing Doc")',
    ],
    "timeline": [
        ':text("Linha do tempo")',
        ':text("Timeline")',
    ],
    "faq": [
        ':text("Perguntas frequentes")',
        ':text("FAQ")',
    ],
}


# ---------------------------------------------------------------------------
# YAML helpers (lazy import to keep startup fast)
# ---------------------------------------------------------------------------

def _yaml():
    """Lazy import PyYAML."""
    try:
        import yaml
        return yaml
    except ImportError:
        print("[FAIL] PyYAML required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Cookie Management
# ---------------------------------------------------------------------------

def _resolve_state_file() -> Path:
    """Resolve cookie state file path, expanding env vars from config."""
    if STATE_FILE and STATE_FILE.exists():
        return STATE_FILE

    # Try path from config
    cfg = load_config()
    cookie_src = cfg.get("cookie_source", "")
    if cookie_src:
        expanded = os.path.expandvars(cookie_src)
        p = Path(expanded)
        if p.exists():
            return p

    return STATE_FILE or Path(".")


def load_cookies() -> list[dict[str, Any]]:
    """Load Google cookies from NotebookLM MCP browser state."""
    sf = _resolve_state_file()
    if not sf or not sf.exists():
        print(f"[FAIL] Cookie state not found: {sf}")
        print("  Run: python _tools/cex_notebooklm.py --reauth")
        return []

    data = json.loads(sf.read_text(encoding="utf-8"))
    cookies = []
    for c in data.get("cookies", []):
        cookie = {
            "name": c["name"],
            "value": c["value"],
            "domain": c["domain"],
            "path": c.get("path", "/"),
        }
        if c.get("expires", -1) > 0:
            cookie["expires"] = c["expires"]
        if c.get("httpOnly"):
            cookie["httpOnly"] = True
        if c.get("secure"):
            cookie["secure"] = True
        if c.get("sameSite"):
            ss = c["sameSite"].capitalize()
            if ss in ("Strict", "Lax", "None"):
                cookie["sameSite"] = ss
        cookies.append(cookie)
    return cookies


def check_auth_valid(cookies: list[dict[str, Any]]) -> bool:
    """Check if Google cookies are likely still valid."""
    if not cookies:
        return False

    essential = {"SID", "HSID", "SSID", "APISID", "SAPISID"}
    present = {c["name"] for c in cookies}
    if not essential.issubset(present):
        return False

    now = time.time()
    for c in cookies:
        if c["name"] in essential:
            exp = c.get("expires", 0)
            if exp > 0 and exp < now:
                return False

    return True


# ---------------------------------------------------------------------------
# Config Management
# ---------------------------------------------------------------------------

def load_config() -> dict[str, Any]:
    """Load notebooklm_notebooks.yaml config."""
    yaml = _yaml()
    if not CONFIG_PATH.exists():
        return {
            "version": 1,
            "google_account": "",
            "publish_mode": "manual",
            "browser_engine": "chrome_local",
            "default_outputs": ["flashcards", "audio_summary", "quiz"],
            "domains": {},
        }
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}


def save_config(config: dict[str, Any]) -> None:
    """Save config back to YAML."""
    yaml = _yaml()
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(
        yaml.dump(config, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def resolve_domain(kc_path: Path, explicit: str | None = None) -> str:
    """Resolve domain from explicit flag, KC frontmatter, or directory structure."""
    if explicit:
        return explicit

    # Try frontmatter
    if kc_path.exists():
        content = kc_path.read_text(encoding="utf-8")
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            yaml = _yaml()
            try:
                fm = yaml.safe_load(fm_match.group(1))
                if isinstance(fm, dict) and fm.get("domain"):
                    return str(fm["domain"])
            except Exception:
                pass

    # Infer from directory structure
    parts = kc_path.parts
    # library/domain/meta/ -> meta
    if "domain" in parts:
        idx = list(parts).index("domain")
        if idx + 1 < len(parts):
            return parts[idx + 1]
    # library/kind/ -> kind
    if "kind" in parts:
        return "kind"
    # library/integration/ -> integration
    if "integration" in parts:
        return "integration"

    return "meta"  # fallback


def get_notebook_id(config: dict[str, Any], domain: str) -> str | None:
    """Get notebook_id for a domain, or None if not created."""
    domains = config.get("domains", {})
    entry = domains.get(domain, {})
    return entry.get("notebook_id")


# ---------------------------------------------------------------------------
# Playwright Helpers
# ---------------------------------------------------------------------------

def _check_playwright():
    """Check if playwright is available."""
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        return True
    except ImportError:
        print("[FAIL] Playwright not installed.")
        print("  Install: pip install playwright && playwright install chromium")
        return False


def _launch_browser(playwright, cookies):
    """Launch Chromium with anti-detection flags and inject cookies."""
    browser = playwright.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
    )
    context = browser.new_context(
        viewport={"width": 1280, "height": 900},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
    )
    if cookies:
        context.add_cookies(cookies)
    page = context.new_page()
    return browser, context, page


def _click_first(page, selectors, label="element", timeout=3000, force=False):
    """Try selectors in order, click first visible match. Returns True on success."""
    for sel in selectors:
        try:
            loc = page.locator(sel).first
            if loc.is_visible(timeout=timeout):
                loc.click(force=force)
                return True
        except Exception:
            continue
    return False


def _screenshot(page, name):
    """Save debug screenshot."""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    path = SCREENSHOT_DIR / f"{name}.png"
    try:
        page.screenshot(path=str(path))
    except Exception:
        pass
    return path


def _navigate_to_notebook(page, notebook_id=None):
    """Navigate to NotebookLM, optionally to a specific notebook.

    Returns True if authenticated, False if redirected to login.
    """
    # Always hit homepage first (cookies need it)
    page.goto(NOTEBOOKLM_BASE + "/", wait_until="domcontentloaded", timeout=45000)
    time.sleep(3)

    if "accounts.google" in page.url:
        return False

    if notebook_id:
        url = f"{NOTEBOOKLM_BASE}/notebook/{notebook_id}"
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        time.sleep(3)

    return True


def _fill_via_js(page, content):
    """Fallback: fill textarea via JavaScript (bypasses Angular form control)."""
    result = page.evaluate("""
        (content) => {
            const textareas = document.querySelectorAll('textarea');
            for (const ta of textareas) {
                const label = ta.getAttribute('aria-label') || '';
                if (label.includes('colado') || label.includes('Texto colado')
                    || label.includes('pasted') || label.includes('Pasted')) {
                    const setter = Object.getOwnPropertyDescriptor(
                        window.HTMLTextAreaElement.prototype, 'value'
                    ).set;
                    setter.call(ta, content);
                    ta.dispatchEvent(new Event('input', { bubbles: true }));
                    ta.dispatchEvent(new Event('change', { bubbles: true }));
                    return 'FILLED';
                }
            }
            return 'NOT_FOUND';
        }
    """, content)
    return "FILLED" in str(result)


# ---------------------------------------------------------------------------
# Auth pre-flight (runs before every browser subcommand)
# ---------------------------------------------------------------------------

def _preflight_auth() -> list:
    """Pre-flight auth check. Returns cookies if valid, exits with message if not."""
    cookies = load_cookies()
    if not check_auth_valid(cookies):
        print("[AUTH_EXPIRED] Google session expired or cookies missing.")
        print("  Run: python _tools/cex_notebooklm.py --reauth")
        print("  Or use NotebookLM MCP: mcp__notebooklm__setup_auth")
        sys.exit(2)
    return cookies


# ---------------------------------------------------------------------------
# Subcommand: --upload
# ---------------------------------------------------------------------------

def cmd_upload(args: argparse.Namespace) -> None:
    """Upload a KC as source to a domain notebook."""
    kc_path = Path(args.upload)
    if not kc_path.exists():
        print(f"[FAIL] KC file not found: {kc_path}")
        sys.exit(1)

    if not _check_playwright():
        sys.exit(1)

    content = kc_path.read_text(encoding="utf-8")
    if len(content) > MAX_SOURCE_CHARS:
        print(f"[WARN] KC is {len(content)} chars, truncating to {MAX_SOURCE_CHARS}")
        content = content[:MAX_SOURCE_CHARS]

    # Extract title from frontmatter
    title = kc_path.stem
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        yaml = _yaml()
        try:
            fm = yaml.safe_load(fm_match.group(1))
            if isinstance(fm, dict) and fm.get("title"):
                title = str(fm["title"])
        except Exception:
            pass

    # Resolve domain and notebook
    config = load_config()
    domain = resolve_domain(kc_path, args.domain)
    notebook_id = args.notebook or get_notebook_id(config, domain)

    # Check source count limit
    domains = config.get("domains", {})
    domain_entry = domains.get(domain, {})
    src_count = domain_entry.get("source_count", 0)
    if src_count >= SOURCE_HARD_LIMIT:
        print(f"[FAIL] Domain '{domain}' has {src_count} sources (limit: {SOURCE_HARD_LIMIT}).")
        print("  Create a new notebook or remove old sources.")
        sys.exit(1)
    if src_count >= SOURCE_WARN_THRESHOLD:
        print(f"[WARN] Domain '{domain}' has {src_count}/{SOURCE_HARD_LIMIT} sources.")

    cookies = _preflight_auth()

    print(f"[INFO] Uploading: {kc_path.name}")
    print(f"  Domain: {domain} | Title: {title[:60]}")
    print(f"  Notebook: {notebook_id or '(will create new)'}")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser, context, page = _launch_browser(p, cookies)

        try:
            # Navigate
            if notebook_id:
                authed = _navigate_to_notebook(page, notebook_id)
            else:
                authed = _navigate_to_notebook(page)

            if not authed:
                print("[AUTH_EXPIRED] Redirected to login page.")
                print("  Run: python _tools/cex_notebooklm.py --reauth")
                browser.close()
                sys.exit(2)

            _screenshot(page, "upload_01_navigate")

            if not notebook_id:
                # Create new notebook
                print("[STEP] Creating new notebook...")
                clicked = _click_first(page, [
                    '[aria-label="Criar novo notebook"]',
                    'button:has-text("Criar novo")',
                    'button:has-text("Criar")',
                    'button:has-text("New notebook")',
                    'button:has-text("New")',
                ], "create button")
                if not clicked:
                    print("[FAIL] Could not find 'Create notebook' button.")
                    _screenshot(page, "upload_fail_create")
                    browser.close()
                    sys.exit(1)
                time.sleep(5)
                _screenshot(page, "upload_02_created")

                # Extract notebook_id from URL
                if "/notebook/" in page.url:
                    notebook_id = page.url.split("/notebook/")[-1].split("?")[0].split("/")[0]
                    print(f"  [OK] New notebook: {notebook_id}")
                else:
                    print("[WARN] Could not extract notebook_id from URL")

            # Click "Adicionar fontes" (Add sources)
            print("[STEP] Adding source...")
            time.sleep(2)
            if not _click_first(page, SELECTORS["add_source"], "add source"):
                # Try + icon fallback
                try:
                    loc = page.locator("button").filter(has_text="add").first
                    if loc.is_visible(timeout=2000):
                        loc.click()
                except Exception:
                    print("[FAIL] Could not find 'Add source' button.")
                    _screenshot(page, "upload_fail_add")
                    browser.close()
                    sys.exit(1)

            time.sleep(3)
            _screenshot(page, "upload_03_source_dialog")

            # Click "Texto copiado" (Copied text)
            if not _click_first(page, SELECTORS["copied_text"], "copied text option"):
                print("[FAIL] Could not find 'Copied text' option.")
                _screenshot(page, "upload_fail_copied_text")
                browser.close()
                sys.exit(1)

            time.sleep(3)
            _screenshot(page, "upload_04_paste_dialog")

            # Fill title
            for sel in SELECTORS["title_input"]:
                try:
                    loc = page.locator(sel).first
                    if loc.is_visible(timeout=2000):
                        loc.click(force=True)
                        loc.fill(title[:200])
                        print(f"  [OK] Title set: {title[:60]}")
                        break
                except Exception:
                    continue

            # Fill content (force click to bypass Angular Material overlay)
            pasted = False
            for sel in SELECTORS["content_area"]:
                try:
                    loc = page.locator(sel).first
                    if loc.is_visible(timeout=2000):
                        loc.click(force=True)
                        time.sleep(0.5)
                        loc.fill(content)
                        pasted = True
                        print(f"  [OK] Pasted {len(content)} chars")
                        break
                except Exception:
                    continue

            if not pasted:
                # JavaScript fallback for Angular form controls
                print("  [INFO] Trying JavaScript injection...")
                pasted = _fill_via_js(page, content)
                if pasted:
                    print("  [OK] Pasted via JS injection")
                else:
                    print("[FAIL] Could not paste content into textarea.")
                    _screenshot(page, "upload_fail_paste")
                    browser.close()
                    sys.exit(1)

            time.sleep(2)
            _screenshot(page, "upload_05_filled")

            # Click "Inserir" (Insert)
            if not _click_first(page, SELECTORS["insert_btn"], "insert button", force=True):
                print("[FAIL] Could not find 'Insert' button.")
                _screenshot(page, "upload_fail_insert")
                browser.close()
                sys.exit(1)

            # Wait for indexing
            print("  [INFO] Waiting for source indexing (up to 60s)...")
            time.sleep(15)
            _screenshot(page, "upload_06_indexing")

            # Poll for completion (source count change or "pronto" indicator)
            for attempt in range(6):
                time.sleep(10)
                _screenshot(page, f"upload_07_poll_{attempt}")
                # Check if dialog closed (means indexing done)
                try:
                    dialog = page.locator('.cdk-overlay-pane').first
                    if not dialog.is_visible(timeout=1000):
                        print("  [OK] Source indexed (dialog closed)")
                        break
                except Exception:
                    break

            # Update config
            if notebook_id:
                if domain not in domains:
                    domains[domain] = {
                        "notebook_id": notebook_id,
                        "name": f"{domain.title()} Knowledge",
                        "description": "",
                        "sources": [],
                        "source_count": 0,
                        "outputs_generated": [],
                        "last_sync": None,
                        "status": "active",
                    }

                entry = domains[domain]
                entry["notebook_id"] = notebook_id
                entry["status"] = "active"
                entry["last_sync"] = datetime.now(timezone.utc).isoformat()

                # Add source to list (avoid duplicates)
                kc_rel = str(kc_path.relative_to(CEX_ROOT)) if kc_path.is_relative_to(CEX_ROOT) else str(kc_path)
                existing_paths = [s.get("path") for s in entry.get("sources", [])]
                if kc_rel not in existing_paths:
                    entry.setdefault("sources", []).append({
                        "path": kc_rel,
                        "uploaded": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    })
                    entry["source_count"] = len(entry["sources"])

                config["domains"] = domains
                save_config(config)
                print(f"  [OK] Config updated: {domain} -> {notebook_id[:12]}...")

            print("\n[DONE] Upload complete.")
            print(f"  notebook_id: {notebook_id}")
            print(f"  domain: {domain}")
            print(f"  source_title: {title[:60]}")
            print("  status: indexed")

        except Exception as e:
            _screenshot(page, "upload_error")
            print(f"[FAIL] Upload error: {e}")
            raise
        finally:
            time.sleep(3)
            browser.close()


# ---------------------------------------------------------------------------
# Subcommand: --studio
# ---------------------------------------------------------------------------

def cmd_studio(args: argparse.Namespace) -> None:
    """Activate Estudio outputs for a notebook."""
    notebook_id = args.studio

    if not _check_playwright():
        sys.exit(1)

    config = load_config()
    outputs = args.outputs.split(",") if args.outputs else config.get("default_outputs", ["flashcards", "audio_summary", "quiz"])

    # Validate output names
    valid_outputs = set(STUDIO_OUTPUTS.keys())
    for out in outputs:
        if out not in valid_outputs:
            print(f"[FAIL] Unknown output type: '{out}'")
            print(f"  Valid: {', '.join(sorted(valid_outputs))}")
            sys.exit(1)

    cookies = _preflight_auth()

    print(f"[INFO] Activating Estudio for notebook: {notebook_id[:12]}...")
    print(f"  Outputs: {', '.join(outputs)}")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser, context, page = _launch_browser(p, cookies)

        try:
            authed = _navigate_to_notebook(page, notebook_id)
            if not authed:
                print("[AUTH_EXPIRED] Redirected to login page.")
                browser.close()
                sys.exit(2)

            _screenshot(page, "studio_01_navigate")
            time.sleep(3)

            # Click Estudio panel to expand it
            _click_first(page, SELECTORS["studio_panel"], "estudio panel", timeout=5000)
            time.sleep(2)
            _screenshot(page, "studio_02_panel")

            results = []
            for out_type in outputs:
                selectors = STUDIO_OUTPUTS.get(out_type, [])
                print(f"  [STEP] Activating: {out_type}...")

                clicked = _click_first(page, selectors, out_type, timeout=5000)
                if clicked:
                    print(f"    [OK] Clicked {out_type}")
                    results.append({"type": out_type, "status": "generating"})
                else:
                    print(f"    [WARN] Could not find button for {out_type}")
                    results.append({"type": out_type, "status": "not_found"})

                time.sleep(3)
                _screenshot(page, f"studio_03_{out_type}")

            # For audio_summary, poll longer (2-10 min generation)
            has_audio = "audio_summary" in outputs
            if has_audio:
                print("  [INFO] Audio generation may take 2-10 minutes. Polling...")
                max_polls = 30  # 30 * 30s = 15min timeout
                for i in range(max_polls):
                    time.sleep(30)
                    _screenshot(page, f"studio_04_audio_poll_{i}")
                    # Check for completion indicators
                    try:
                        # Look for play button or download link as completion signal
                        play_btn = page.locator('button[aria-label*="Play"], button[aria-label*="Reproduzir"]').first
                        if play_btn.is_visible(timeout=1000):
                            print("    [OK] Audio generation complete")
                            break
                    except Exception:
                        continue
                    if i % 4 == 0:
                        print(f"    [INFO] Still generating... ({(i+1)*30}s)")
            else:
                # Non-audio outputs are faster (~30s)
                print("  [INFO] Waiting for generation (30s)...")
                time.sleep(30)

            _screenshot(page, "studio_05_done")

            # Update config with generated outputs
            config = load_config()
            for domain_name, domain_data in config.get("domains", {}).items():
                if domain_data.get("notebook_id") == notebook_id:
                    existing = domain_data.get("outputs_generated", [])
                    existing_types = {o.get("type") for o in existing}
                    for r in results:
                        if r["type"] not in existing_types:
                            existing.append({
                                "type": r["type"],
                                "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                            })
                    domain_data["outputs_generated"] = existing
                    break
            save_config(config)

            print("\n[DONE] Estudio activation complete.")
            print(f"  notebook_id: {notebook_id}")
            for r in results:
                print(f"  {r['type']}: {r['status']}")

        except Exception as e:
            _screenshot(page, "studio_error")
            print(f"[FAIL] Estudio error: {e}")
            raise
        finally:
            time.sleep(3)
            browser.close()


# ---------------------------------------------------------------------------
# Subcommand: --status
# ---------------------------------------------------------------------------

def cmd_status(args: argparse.Namespace) -> None:
    """Check status of a notebook (local config + info)."""
    notebook_id = args.status
    config = load_config()

    # Find domain for this notebook
    found_domain = None
    found_entry = None
    for domain_name, domain_data in config.get("domains", {}).items():
        if domain_data.get("notebook_id") == notebook_id:
            found_domain = domain_name
            found_entry = domain_data
            break

    if not found_entry:
        print(f"[WARN] Notebook {notebook_id} not found in config.")
        print("  It may not be tracked yet. Use --upload to add sources.")
        sys.exit(0)

    print("--- Notebook Status ---")
    print(f"notebook_id: {notebook_id}")
    print(f"domain: {found_domain}")
    print(f"name: {found_entry.get('name', '(unnamed)')}")
    print(f"status: {found_entry.get('status', 'unknown')}")
    print(f"sources: {found_entry.get('source_count', 0)}")
    print(f"last_sync: {found_entry.get('last_sync', 'never')}")

    sources = found_entry.get("sources", [])
    if sources:
        print(f"\nSources ({len(sources)}):")
        for s in sources:
            print(f"  - {s.get('path', '?')} (uploaded: {s.get('uploaded', '?')})")

    outputs = found_entry.get("outputs_generated", [])
    if outputs:
        print(f"\nOutputs ({len(outputs)}):")
        for o in outputs:
            count_str = f" ({o['count']} items)" if o.get("count") else ""
            print(f"  - {o.get('type', '?')}{count_str} (generated: {o.get('generated', '?')})")
    else:
        print("\nOutputs: none generated yet")

    print(f"\nURL: {NOTEBOOKLM_BASE}/notebook/{notebook_id}")


# ---------------------------------------------------------------------------
# Subcommand: --list
# ---------------------------------------------------------------------------

def cmd_list(args: argparse.Namespace) -> None:
    """List all tracked notebooks with domain mapping."""
    config = load_config()
    domains = config.get("domains", {})

    if not domains:
        print("[INFO] No domains configured yet.")
        print(f"  Config: {CONFIG_PATH}")
        return

    # Header
    fmt = "{:<15} {:<40} {:>7}  {:<12}"
    print(fmt.format("DOMAIN", "NOTEBOOK_ID", "SOURCES", "LAST_SYNC"))
    print("-" * 80)

    for domain_name, data in domains.items():
        nid = data.get("notebook_id")
        nid_display = nid[:36] if nid else "(not created)"
        src_count = data.get("source_count", 0)
        last_sync = data.get("last_sync")
        if last_sync:
            # Show just the date portion
            sync_display = str(last_sync)[:10]
        else:
            sync_display = "--"

        print(fmt.format(domain_name, nid_display, src_count, sync_display))

    print(f"\nConfig: {CONFIG_PATH}")
    print(f"Account: {config.get('google_account', '(not set)')}")
    print(f"Publish mode: {config.get('publish_mode', 'manual')}")


# ---------------------------------------------------------------------------
# Subcommand: --reauth
# ---------------------------------------------------------------------------

def cmd_reauth(args: argparse.Namespace) -> None:
    """Re-authenticate Google session via browser."""
    if not _check_playwright():
        sys.exit(1)

    print("[INFO] Launching browser for Google re-authentication...")
    print("  Please log in with your Google account.")
    print("  The browser will close automatically after login is detected.")

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser, context, page = _launch_browser(p, [])

        try:
            page.goto("https://accounts.google.com/", wait_until="domcontentloaded", timeout=30000)
            print("  [INFO] Waiting for login (up to 120s)...")

            # Poll for successful login (redirect away from accounts.google.com)
            for _ in range(24):  # 24 * 5s = 120s
                time.sleep(5)
                url = page.url
                if "myaccount.google.com" in url or "notebooklm.google.com" in url:
                    print("  [OK] Login detected!")
                    break
            else:
                print("[WARN] Login timeout (120s). Saving cookies anyway...")

            # Navigate to NotebookLM to capture its cookies
            page.goto(NOTEBOOKLM_BASE + "/", wait_until="domcontentloaded", timeout=30000)
            time.sleep(5)

            # Extract cookies from browser context
            browser_cookies = context.cookies()

            # Save to state file
            sf = _resolve_state_file()
            state = {"cookies": browser_cookies}
            sf.parent.mkdir(parents=True, exist_ok=True)
            sf.write_text(json.dumps(state, indent=2), encoding="utf-8")
            print(f"  [OK] Saved {len(browser_cookies)} cookies to {sf}")

            # Verify
            if check_auth_valid(browser_cookies):
                print("[DONE] Re-authentication successful.")
            else:
                print("[WARN] Cookies saved but may not be fully valid.")
                print("  Try: python _tools/cex_notebooklm.py --auth-check")

        except Exception as e:
            print(f"[FAIL] Re-auth error: {e}")
            raise
        finally:
            browser.close()


# ---------------------------------------------------------------------------
# Subcommand: --auth-check
# ---------------------------------------------------------------------------

def cmd_auth_check(args: argparse.Namespace) -> None:
    """Check if Google auth cookies are valid."""
    cookies = load_cookies()
    if not cookies:
        print("[FAIL] No cookies found.")
        print(f"  Expected: {STATE_FILE}")
        sys.exit(2)

    print(f"[INFO] Found {len(cookies)} cookies")

    if check_auth_valid(cookies):
        print("[OK] Auth cookies appear valid.")
        # Show key cookie expiry
        essential = {"SID", "HSID", "SSID"}
        for c in cookies:
            if c["name"] in essential:
                exp = c.get("expires", 0)
                if exp > 0:
                    exp_dt = datetime.fromtimestamp(exp, tz=timezone.utc)
                    days_left = (exp_dt - datetime.now(timezone.utc)).days
                    print(f"  {c['name']}: expires in {days_left} days")
        sys.exit(0)
    else:
        print("[FAIL] Auth cookies are expired or incomplete.")
        print("  Run: python _tools/cex_notebooklm.py --reauth")
        sys.exit(2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX NotebookLM Pipeline Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  %(prog)s --upload P01_knowledge/library/kind/kc_agent.md\n"
            "  %(prog)s --studio 940fd258-... --outputs flashcards,audio_summary\n"
            "  %(prog)s --status 940fd258-...\n"
            "  %(prog)s --list\n"
            "  %(prog)s --reauth\n"
            "  %(prog)s --auth-check\n"
            "\n"
            "Config: .cex/P09_config/notebooklm_notebooks.yaml\n"
            "Spec: _docs/specs/spec_notebooklm_pipeline.md\n"
        ),
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--upload", metavar="KC_PATH",
                        help="Upload a KC as source to a domain notebook")
    group.add_argument("--studio", metavar="NOTEBOOK_ID",
                        help="Activate Estudio outputs for a notebook")
    group.add_argument("--status", metavar="NOTEBOOK_ID",
                        help="Check notebook status")
    group.add_argument("--list", action="store_true",
                        help="List all tracked notebooks")
    group.add_argument("--reauth", action="store_true",
                        help="Re-authenticate Google session")
    group.add_argument("--auth-check", action="store_true",
                        help="Check if auth cookies are valid")

    # Upload options
    parser.add_argument("--domain", metavar="DOMAIN",
                        help="Override domain for upload (default: auto-detect)")
    parser.add_argument("--notebook", metavar="ID",
                        help="Override notebook_id for upload")

    # Studio options
    parser.add_argument("--outputs", metavar="LIST",
                        help="Comma-separated output types (default: from config)")

    args = parser.parse_args()

    if args.upload:
        cmd_upload(args)
    elif args.studio:
        cmd_studio(args)
    elif args.status:
        cmd_status(args)
    elif args.list:
        cmd_list(args)
    elif args.reauth:
        cmd_reauth(args)
    elif args.auth_check:
        cmd_auth_check(args)


if __name__ == "__main__":
    main()
