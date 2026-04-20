"""
Fix UTF-8 double-encoding in content_library rows.

Cause: PowerShell REST POST sent UTF-8 bytes interpreted as Latin-1.
Fix:   text.encode('latin-1').decode('utf-8') reverses the damage.
Safe:  only touches rows whose text actually contains mojibake signatures.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request

PROJECT = "fuuguegkqnpzrrhwymgw"
BASE = f"https://{PROJECT}.supabase.co/rest/v1"
KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
if not KEY:
    sys.exit("SUPABASE_SERVICE_ROLE_KEY not set")

HDR = {
    "apikey": KEY,
    "Authorization": f"Bearer {KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
}


MOJIBAKE_MARKERS = ("\u00c3", "\u00e2\u20ac")  # U+00C3 (capital A tilde) + em-dash prefix


def is_mojibake(text: str | None) -> bool:
    if not text:
        return False
    return any(m in text for m in MOJIBAKE_MARKERS)


def fix(text: str | None) -> str | None:
    if text is None:
        return None
    if not is_mojibake(text):
        return text
    # cp1252 (Windows-1252) is latin-1 + Euro, smart quotes, em-dash slots.
    # The original PowerShell REST path encoded UTF-8 bytes as cp1252.
    for enc in ("cp1252", "latin-1"):
        try:
            return text.encode(enc, errors="strict").decode("utf-8", errors="strict")
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
    return text


def fetch_all() -> list[dict]:
    url = f"{BASE}/content_library?select=id,caption_text,alt_text,metadata&limit=500"
    req = urllib.request.Request(url, headers=HDR)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def patch(row_id: str, payload: dict) -> None:
    url = f"{BASE}/content_library?id=eq.{row_id}"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=HDR, method="PATCH")
    with urllib.request.urlopen(req) as r:
        r.read()


def main() -> None:
    rows = fetch_all()
    print(f"[i] fetched {len(rows)} rows")
    fixed = 0
    for row in rows:
        patch_body: dict = {}

        new_caption = fix(row.get("caption_text"))
        if new_caption != row.get("caption_text"):
            patch_body["caption_text"] = new_caption

        new_alt = fix(row.get("alt_text"))
        if new_alt != row.get("alt_text"):
            patch_body["alt_text"] = new_alt

        meta = row.get("metadata") or {}
        if isinstance(meta, dict):
            new_meta = {}
            meta_changed = False
            for k, v in meta.items():
                if isinstance(v, str):
                    nv = fix(v)
                    new_meta[k] = nv
                    if nv != v:
                        meta_changed = True
                else:
                    new_meta[k] = v
            if meta_changed:
                patch_body["metadata"] = new_meta

        if patch_body:
            patch(row["id"], patch_body)
            fixed += 1
            print(f"  [OK] {row['id']}: keys={list(patch_body.keys())}")

    print(f"[done] fixed {fixed}/{len(rows)} rows")


if __name__ == "__main__":
    main()
