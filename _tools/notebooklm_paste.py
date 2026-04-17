#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Paste content into an existing NotebookLM notebook.
Targeted fix: uses force click to bypass Material overlay.
"""

import json
import time
from pathlib import Path

CONTENT_FILE = Path(__file__).parent.parent / "N00_genesis" / "P01_knowledge" / "library" / "domain" / "meta" / "kc_8f_pipeline.md"
STATE_FILE = Path(r"C:\Users\PC\AppData\Local\notebooklm-mcp\Data\browser_state\state.json")
SS_DIR = Path(__file__).parent

NOTEBOOK_URL = "https://notebooklm.google.com/notebook/940fd258-847f-47c1-b7e6-caca7b730681"


def load_cookies():
    data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    cookies = []
    for c in data.get("cookies", []):
        cookie = {"name": c["name"], "value": c["value"], "domain": c["domain"], "path": c.get("path", "/")}
        if c.get("expires", -1) > 0: cookie["expires"] = c["expires"]
        if c.get("httpOnly"): cookie["httpOnly"] = True
        if c.get("secure"): cookie["secure"] = True
        if c.get("sameSite"):
            ss = c["sameSite"].capitalize()
            if ss in ("Strict", "Lax", "None"): cookie["sameSite"] = ss
        cookies.append(cookie)
    return cookies


def main():
    from playwright.sync_api import sync_playwright

    content = CONTENT_FILE.read_text(encoding="utf-8")
    cookies = load_cookies()
    print(f"[OK] Content: {len(content)} chars | Cookies: {len(cookies)}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox"],
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        )
        context.add_cookies(cookies)
        page = context.new_page()

        # 1. Go to homepage first (cookies need homepage to stick), then notebook
        print("\n[STEP 1] Opening NotebookLM homepage first...")
        page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded", timeout=45000)
        time.sleep(5)
        print(f"  Homepage: {page.title()} | URL: {page.url}")

        if "accounts.google" in page.url:
            print("[FAIL] Cookies expired -- need to re-auth via NotebookLM MCP setup_auth")
            browser.close()
            return

        print("  [OK] Logged in! Navigating to notebook...")
        page.goto(NOTEBOOK_URL, wait_until="domcontentloaded", timeout=45000)
        time.sleep(5)
        page.screenshot(path=str(SS_DIR / "nlm_paste_01.png"))
        print(f"  Title: {page.title()} | URL: {page.url}")

        # 2. Click "Adicionar fontes" (Add sources) button
        print("\n[STEP 2] Clicking 'Adicionar fontes'...")
        time.sleep(2)
        added = False
        for sel in [
            'button:has-text("Adicionar fontes")',
            'button:has-text("Add source")',
            'button:has-text("Adicionar")',
            ':text("Adicionar fontes")',
            '[aria-label*="Adicionar"]',
            '[aria-label*="Add source"]',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=3000):
                    loc.click()
                    added = True
                    print(f"  [OK] Clicked: {sel}")
                    break
            except Exception:
                continue

        if not added:
            # Try the + icon
            print("  [INFO] Trying + icon...")
            try:
                loc = page.locator("button").filter(has_text="add").first
                if loc.is_visible(timeout=2000):
                    loc.click()
                    added = True
                    print("  [OK] Clicked + icon")
            except Exception:
                pass

        if not added:
            print("  [WARN] Dumping buttons:")
            for el in page.locator("button").all()[:20]:
                try:
                    txt = el.inner_text(timeout=500).strip().replace("\n"," ")[:60]
                    if txt: print(f"    '{txt}'")
                except: pass

        time.sleep(3)
        page.screenshot(path=str(SS_DIR / "nlm_paste_02.png"))

        # 3. Click "Texto copiado" in the source picker
        print("\n[STEP 3] Clicking 'Texto copiado'...")
        time.sleep(2)
        for sel in [
            ':text("Texto copiado")',
            'button:has-text("Texto copiado")',
            ':text("Copied text")',
            ':text("Colar")',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=3000):
                    loc.click()
                    print(f"  [OK] Clicked: {sel}")
                    break
            except Exception:
                continue

        time.sleep(3)
        page.screenshot(path=str(SS_DIR / "nlm_paste_03.png"))

        # 4. Fill the title input (inside dialog)
        print("\n[STEP 4] Setting title...")
        for sel in [
            'input[formcontrolname="title"]',
            'input[aria-label*="t\u00edtulo"]',
            'input[aria-label*="title"]',
            'input[placeholder*="t\u00edtulo"]',
            'input[placeholder*="title"]',
            'input[placeholder*="Cole o t\u00edtulo"]',
            # Inside dialog: try mat-dialog inputs
            'mat-dialog-container input',
            '.cdk-overlay-pane input',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=2000):
                    loc.click(force=True)
                    loc.fill("8F Pipeline - Anatomia Completa CEX")
                    print(f"  [OK] Title set via: {sel}")
                    break
            except Exception:
                continue

        # 5. Fill the textarea (THE KEY STEP -- use force click to bypass overlay)
        print("\n[STEP 5] Pasting content into textarea...")
        pasted = False

        # Target the textarea by aria-label 'Texto colado' (found in dump)
        for sel in [
            'textarea[aria-label="Texto colado"]',
            'textarea[placeholder*="Cole o texto"]',
            'textarea[formcontrolname="pastedText"]',
            # Inside dialog overlay
            '.cdk-overlay-pane textarea',
            'mat-dialog-container textarea',
            # Generic fallback within the dialog
            '[role="dialog"] textarea',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=2000):
                    # Force click bypasses the overlay interception
                    loc.click(force=True)
                    time.sleep(0.5)
                    loc.fill(content[:200000])
                    pasted = True
                    print(f"  [OK] Pasted {len(content)} chars via: {sel}")
                    break
            except Exception as e:
                print(f"  {sel}: {e}")
                continue

        if not pasted:
            # Nuclear option: use JavaScript to find and fill
            print("  [INFO] Trying JavaScript injection...")
            try:
                result = page.evaluate("""
                    () => {
                        const textareas = document.querySelectorAll('textarea');
                        const info = [];
                        for (const ta of textareas) {
                            info.push({
                                ariaLabel: ta.getAttribute('aria-label'),
                                placeholder: ta.getAttribute('placeholder'),
                                name: ta.getAttribute('name'),
                                formcontrol: ta.getAttribute('formcontrolname'),
                                visible: ta.offsetParent !== null,
                                id: ta.id,
                            });
                        }
                        return info;
                    }
                """)
                print(f"  Found {len(result)} textareas:")
                for i, ta in enumerate(result):
                    print(f"    [{i}]: aria='{ta.get('ariaLabel')}' placeholder='{ta.get('placeholder')}' visible={ta.get('visible')} fc='{ta.get('formcontrol')}'")

                # Try to fill via JS
                js_result = page.evaluate("""
                    (content) => {
                        const textareas = document.querySelectorAll('textarea');
                        for (const ta of textareas) {
                            const label = ta.getAttribute('aria-label') || '';
                            if (label.includes('colado') || label.includes('Texto colado')) {
                                // Trigger Angular's change detection
                                const nativeInputValueSetter = Object.getOwnPropertyDescriptor(
                                    window.HTMLTextAreaElement.prototype, 'value'
                                ).set;
                                nativeInputValueSetter.call(ta, content);
                                ta.dispatchEvent(new Event('input', { bubbles: true }));
                                ta.dispatchEvent(new Event('change', { bubbles: true }));
                                return 'FILLED: ' + label;
                            }
                        }
                        return 'NOT_FOUND';
                    }
                """, content[:200000])
                print(f"  JS result: {js_result}")
                if "FILLED" in str(js_result):
                    pasted = True
            except Exception as e:
                print(f"  JS error: {e}")

        time.sleep(2)
        page.screenshot(path=str(SS_DIR / "nlm_paste_04.png"))

        # 6. Click "Inserir" button
        print("\n[STEP 6] Clicking 'Inserir'...")
        time.sleep(1)
        for sel in [
            '.cdk-overlay-pane button:has-text("Inserir")',
            '[role="dialog"] button:has-text("Inserir")',
            'button:has-text("Inserir")',
            'button:has-text("Insert")',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=3000):
                    loc.click(force=True)
                    print(f"  [OK] Clicked: {sel}")
                    break
            except Exception:
                continue

        # Wait for processing
        print("  [INFO] Waiting for source to be processed...")
        time.sleep(15)
        page.screenshot(path=str(SS_DIR / "nlm_paste_05.png"))
        print(f"  URL: {page.url}")

        # 7. Share notebook
        print("\n[STEP 7] Sharing notebook...")
        time.sleep(2)
        for sel in [
            'button:has-text("Compartilhar")',
            '[aria-label*="Compartilhar"]',
            'button:has-text("Share")',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=3000):
                    loc.click()
                    print(f"  [OK] Clicked share: {sel}")
                    time.sleep(3)
                    page.screenshot(path=str(SS_DIR / "nlm_paste_06.png"))

                    # Change access to "Anyone with link"
                    for access_sel in [
                        ':text("Restrito")',
                        ':text("Restricted")',
                        'button:has-text("Restrito")',
                        '[aria-label*="acesso"]',
                    ]:
                        try:
                            loc2 = page.locator(access_sel).first
                            if loc2.is_visible(timeout=2000):
                                loc2.click()
                                time.sleep(2)
                                # Select "Anyone with link"
                                for opt in [':text("Qualquer pessoa")', ':text("Anyone")', ':text("Leitores")']:
                                    try:
                                        loc3 = page.locator(opt).first
                                        if loc3.is_visible(timeout=2000):
                                            loc3.click()
                                            time.sleep(2)
                                            break
                                    except: pass
                                break
                        except: pass

                    # Copy link
                    for copy_sel in [
                        'button:has-text("Copiar link")',
                        'button:has-text("Copy link")',
                    ]:
                        try:
                            loc4 = page.locator(copy_sel).first
                            if loc4.is_visible(timeout=2000):
                                loc4.click()
                                print(f"  [OK] Copied link")
                                time.sleep(2)
                                break
                        except: pass

                    page.screenshot(path=str(SS_DIR / "nlm_paste_07.png"))
                    break
            except Exception:
                continue

        # Final
        final_url = page.url
        print(f"\n{'='*60}")
        print(f"[RESULT] Notebook URL: {NOTEBOOK_URL}")
        print(f"[RESULT] Current URL: {final_url}")
        print(f"{'='*60}")

        print("\n[...] Keeping browser open 15s...")
        time.sleep(15)
        browser.close()
        print("[DONE]")


if __name__ == "__main__":
    main()
