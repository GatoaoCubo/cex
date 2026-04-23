#!/usr/bin/env python3
"""Batch upload audio_source.md files to NotebookLM via Chrome CDP."""

import json
import sys
import time
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = CEX_ROOT / "_output" / "mentor"

CONCEPTS = [
    "nuclei", "kinds",
    "gdp", "builder", "dispatch",
    "crews", "signals", "memory", "sin_lens",
]

RESULTS_FILE = CEX_ROOT / ".cex" / "config" / "notebooklm_mentor_notebooks.yaml"


def upload_concept(page, concept, content):
    """Create notebook, paste content, rename. Returns notebook_id."""
    # Go to homepage
    page.goto("https://notebooklm.google.com/", wait_until="networkidle", timeout=30000)
    time.sleep(5)

    # Debug: save screenshot
    ss_path = CEX_ROOT / "_tools" / "screenshots" / f"nlm_debug_{concept}.png"
    ss_path.parent.mkdir(parents=True, exist_ok=True)
    page.screenshot(path=str(ss_path))
    print(f"  [DBG] Screenshot: {ss_path}")
    print(f"  [DBG] URL: {page.url}")
    print(f"  [DBG] Title: {page.title()}")

    # Wait for and click "Criar novo notebook"
    try:
        create_btn = page.get_by_role("button", name="Criar novo notebook")
        create_btn.wait_for(state="visible", timeout=15000)
        create_btn.click()
    except Exception:
        # Fallback: click via JS
        page.evaluate("""
        () => {
            const btns = [...document.querySelectorAll('button, [role="button"]')];
            const btn = btns.find(b => b.textContent.includes('Criar novo'));
            if (btn) { btn.click(); return 'clicked'; }
            return 'not_found: ' + btns.map(b => b.textContent.trim().substring(0,30)).join(' | ');
        }
        """)
    time.sleep(5)

    # Extract notebook ID from URL
    url = page.url
    notebook_id = url.split("/notebook/")[1].split("?")[0] if "/notebook/" in url else "unknown"
    print(f"  [OK] Notebook created: {notebook_id}")

    # Click "Texto copiado" in dialog
    try:
        texto_btn = page.get_by_role("button", name="Texto copiado")
        texto_btn.wait_for(state="visible", timeout=10000)
        texto_btn.click()
        time.sleep(2)
    except Exception as e:
        print(f"  [WARN] Dialog not found, trying add source: {e}")
        page.get_by_role("button", name="Adicionar fontes").click()
        time.sleep(2)
        page.get_by_role("button", name="Texto copiado").click()
        time.sleep(2)

    # Inject content via JS (fast, bypasses char-by-char typing)
    escaped = json.dumps(content)
    inject_js = """
    () => {{
        const ta = document.querySelector('textarea[placeholder*="Cole"]');
        if (!ta) return 'NO_TEXTAREA';
        ta.focus();
        ta.value = {escaped};
        ta.dispatchEvent(new Event('input', {{bubbles: true}}));
        ta.dispatchEvent(new Event('change', {{bubbles: true}}));
        return ta.value.length;
    }}
    """
    result = page.evaluate(inject_js)
    print(f"  [OK] Content injected: {result} chars")

    # Click "Inserir"
    time.sleep(1)
    inserir_btn = page.get_by_role("button", name="Inserir")
    inserir_btn.wait_for(state="visible", timeout=5000)
    inserir_btn.click()
    time.sleep(5)
    print("  [OK] Source inserted")

    # Rename notebook
    title = f"CEX Mentor: {concept.replace('_', ' ').title()} (EN)"
    rename_js = """
    () => {{
        const input = document.querySelector('editable-project-title input, editable-project-title textarea');
        if (!input) return 'NO_INPUT';
        input.focus();
        input.select();
        input.value = {json.dumps(title)};
        input.dispatchEvent(new Event('input', {{bubbles: true}}));
        input.dispatchEvent(new Event('change', {{bubbles: true}}));
        input.blur();
        return input.value;
    }}
    """
    renamed = page.evaluate(rename_js)
    print(f"  [OK] Renamed to: {renamed}")
    time.sleep(2)

    return notebook_id


def main():
    from playwright.sync_api import sync_playwright

    results = {}
    errors = []

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = context.new_page()

        for concept in CONCEPTS:
            src = OUTPUT_DIR / concept / "en" / "audio_source.md"
            if not src.exists():
                print(f"[SKIP] {concept}: no audio_source.md")
                errors.append(concept)
                continue

            content = src.read_text(encoding="utf-8")
            print(f"\n[{CONCEPTS.index(concept)+2}/10] Uploading: {concept} ({len(content)} chars)")

            try:
                nb_id = upload_concept(page, concept, content)
                results[concept] = {
                    "notebook_id": nb_id,
                    "url": f"https://notebooklm.google.com/notebook/{nb_id}",
                    "source": str(src.relative_to(CEX_ROOT)),
                    "chars": len(content),
                }
            except Exception as e:
                print(f"  [FAIL] {concept}: {e}")
                errors.append(concept)

        page.close()

    # Add pillars (already uploaded manually)
    results["pillars"] = {
        "notebook_id": "c505dc47-3bd1-4204-80f8-9a05b0e94766",
        "url": "https://notebooklm.google.com/notebook/c505dc47-3bd1-4204-80f8-9a05b0e94766",
        "source": "_output/mentor/pillars/en/audio_source.md",
        "chars": 11411,
    }

    # Write results
    lines = [
        "# NotebookLM Mentor Notebooks (auto-generated)",
        f"# Generated: {time.strftime('%Y-%m-%d %H:%M')}",
        "# 10 concepts x EN audio_source uploaded",
        "",
        "version: 1",
        "mission: INFOPRODUCT_MEDIA_SCALE",
        "language: en",
        "",
        "notebooks:",
    ]
    for concept in ["pillars", "nuclei", "kinds", "gdp", "builder", "dispatch", "crews", "signals", "memory", "sin_lens"]:
        if concept in results:
            r = results[concept]
            lines.append(f"  {concept}:")
            lines.append(f'    notebook_id: "{r["notebook_id"]}"')
            lines.append(f'    url: "{r["url"]}"')
            lines.append(f'    source: "{r["source"]}"')
            lines.append(f"    chars: {r['chars']}")
            lines.append("    status: uploaded")
        else:
            lines.append(f"  {concept}:")
            lines.append("    status: failed")

    RESULTS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n[OK] Results saved to {RESULTS_FILE}")

    if errors:
        print(f"[WARN] Failed: {errors}")
        return 1
    print(f"[OK] All {len(results)} notebooks created successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
