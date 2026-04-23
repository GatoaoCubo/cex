#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a NotebookLM notebook via Playwright browser automation.
Injects Google cookies from NotebookLM MCP's saved state.
UI is in Portuguese (pt-BR).
"""

import json
import time
from pathlib import Path
from typing import Any

CONTENT_FILE = Path(__file__).parent.parent / "N00_genesis" / "P01_knowledge" / "library" / "domain" / "meta" / "kc_8f_pipeline.md"
STATE_FILE = Path(r"C:\Users\PC\AppData\Local\notebooklm-mcp\Data\browser_state\state.json")
SS_DIR = Path(__file__).parent


def load_cookies() -> list[dict[str, Any]]:
    data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
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


def click_first_visible(
    page: Any, selectors: list[str], label: str = "element", timeout: int = 3000
) -> bool:
    for sel in selectors:
        try:
            loc = page.locator(sel).first
            if loc.is_visible(timeout=timeout):
                print(f"  [OK] Found {label}: {sel}")
                loc.click()
                return True
        except Exception:
            continue
    print(f"  [WARN] {label} not found with any selector")
    return False


def dump_elements(page: Any, tag: str = "button", limit: int = 15) -> None:
    els = page.locator(tag).all()
    for i, el in enumerate(els[:limit]):
        try:
            txt = el.inner_text(timeout=500).strip().replace("\n", " ")[:80]
            aria = (el.get_attribute("aria-label") or "")[:60]
            if txt or aria:
                print(f"    {tag}[{i}]: '{txt}' aria='{aria}'")
        except Exception:
            pass


def main() -> None:
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

        # 1. Navigate to NotebookLM
        print("\n[STEP 1] Navigating to NotebookLM...")
        page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded", timeout=45000)
        time.sleep(3)
        page.screenshot(path=str(SS_DIR / "nlm_ss_01.png"))
        print(f"  Title: {page.title()} | URL: {page.url}")

        if "accounts.google" in page.url:
            print("[FAIL] Not authenticated")
            browser.close()
            return

        # 2. Click "Criar novo" button
        print("\n[STEP 2] Clicking 'Criar novo'...")
        clicked = click_first_visible(page, [
            '[aria-label="Criar novo notebook"]',
            'button:has-text("Criar novo")',
            'button:has-text("Criar")',
            'button:has-text("New")',
        ], "create button")

        if not clicked:
            dump_elements(page, "button")
            browser.close()
            return

        time.sleep(5)
        page.screenshot(path=str(SS_DIR / "nlm_ss_02.png"))
        print(f"  URL after create: {page.url}")

        # 3. Look for source upload dialog -- click "Texto copiado" / "Copied text"
        print("\n[STEP 3] Looking for 'Texto copiado' source option...")
        time.sleep(2)

        # The NotebookLM source dialog usually shows icons for: Drive, Link, Upload, Copied text, etc.
        source_clicked = click_first_visible(page, [
            ':text("Texto copiado")',
            ':text("Copied text")',
            'button:has-text("Texto copiado")',
            'button:has-text("Copied text")',
            ':text("Colar texto")',
            ':text("Paste text")',
            ':text("Texto")',
            'div:has-text("Texto copiado")',
        ], "text source option")

        if not source_clicked:
            print("  Dumping visible elements:")
            dump_elements(page, "button", 20)
            dump_elements(page, "[role='button']", 10)
            dump_elements(page, "[role='menuitem']", 10)
            dump_elements(page, "a", 10)
            dump_elements(page, "div.source-option", 10)
            # Also try clicking any element that has "text" in class
            page.screenshot(path=str(SS_DIR / "nlm_ss_03.png"))
            print("  [INFO] Keeping browser open 30s for manual inspection...")
            time.sleep(30)
            browser.close()
            return

        time.sleep(3)
        page.screenshot(path=str(SS_DIR / "nlm_ss_03.png"))

        # 4. Find title input and set notebook name
        print("\n[STEP 4] Setting source title...")
        title_set = False
        for sel in [
            'input[placeholder*="t\u00edtulo"]',
            'input[placeholder*="title"]',
            'input[placeholder*="T\u00edtulo"]',
            'input[placeholder*="Title"]',
            'input[placeholder*="nome"]',
            'input[type="text"]',
        ]:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=2000):
                    loc.fill("8F Pipeline - Anatomia Completa da Producao CEX")
                    title_set = True
                    print(f"  [OK] Title set via: {sel}")
                    break
            except Exception:
                continue

        # 5. Paste content into textarea
        print("\n[STEP 5] Pasting content...")
        pasted = False
        for sel in ["textarea", '[contenteditable="true"]', '[role="textbox"]']:
            try:
                loc = page.locator(sel).first
                if loc.is_visible(timeout=3000):
                    loc.click()
                    loc.fill(content[:200000])
                    pasted = True
                    print(f"  [OK] Pasted {len(content)} chars via: {sel}")
                    break
            except Exception as e:
                print(f"  {sel}: {e}")
                continue

        if not pasted:
            print("  [WARN] No textarea found")
            dump_elements(page, "textarea", 5)
            dump_elements(page, "[contenteditable]", 5)

        time.sleep(2)
        page.screenshot(path=str(SS_DIR / "nlm_ss_04.png"))

        # 6. Click insert/add button
        print("\n[STEP 6] Clicking insert/submit...")
        click_first_visible(page, [
            'button:has-text("Inserir")',
            'button:has-text("Insert")',
            'button:has-text("Adicionar")',
            'button:has-text("Add")',
            'button:has-text("Salvar")',
            'button:has-text("Save")',
            'button:has-text("Enviar")',
            'button:has-text("Submit")',
        ], "submit button")

        time.sleep(8)
        page.screenshot(path=str(SS_DIR / "nlm_ss_05.png"))
        print(f"  URL: {page.url}")

        # 7. Try to share the notebook
        print("\n[STEP 7] Getting share link...")
        time.sleep(3)

        shared = click_first_visible(page, [
            'button:has-text("Compartilhar")',
            'button:has-text("Share")',
            '[aria-label*="Compartilhar"]',
            '[aria-label*="Share"]',
        ], "share button")

        if shared:
            time.sleep(3)
            page.screenshot(path=str(SS_DIR / "nlm_ss_06.png"))

            # Try to click "Anyone with the link" option
            click_first_visible(page, [
                ':text("Qualquer pessoa com o link")',
                ':text("Anyone with the link")',
                ':text("Leitores")',
                ':text("Viewers")',
            ], "access option", timeout=3000)

            time.sleep(2)

            # Copy link
            click_first_visible(page, [
                'button:has-text("Copiar link")',
                'button:has-text("Copy link")',
                'button:has-text("Copiar")',
                'button:has-text("Copy")',
            ], "copy link button", timeout=3000)

            time.sleep(2)
            page.screenshot(path=str(SS_DIR / "nlm_ss_07.png"))

        # Final result
        final_url = page.url
        print(f"\n[RESULT] Final URL: {final_url}")

        # Try to extract notebook ID from URL
        if "/notebook/" in final_url:
            notebook_id = final_url.split("/notebook/")[-1].split("?")[0].split("/")[0]
            share_url = f"https://notebooklm.google.com/notebook/{notebook_id}"
            print(f"[RESULT] Share URL: {share_url}")

        print("\n[...] Keeping browser open 15s...")
        time.sleep(15)
        browser.close()
        print("[DONE]")


if __name__ == "__main__":
    main()
