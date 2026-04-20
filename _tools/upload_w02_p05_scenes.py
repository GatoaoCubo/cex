"""
Upload w02_p05 scene PNGs to Supabase Storage and wire into missing rows.

4 scenes available in .cex/cache/w10_scenes_w02_p05/:
  01_janela_hero.png, 02_observacao.png, 03_cama_suspensa.png, 04_ambiente.png

Target rows (w02_p05 with NULL storage_url):
  - threads (1:1 image)    -> 01_janela_hero.png
  - pinterest (2:3 image)  -> 02_observacao.png
Remaining NULL rows (fb 4:5 video, linkedin 1:1 video) are video-type, skipped.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PROJECT = "fuuguegkqnpzrrhwymgw"
REST = f"https://{PROJECT}.supabase.co/rest/v1"
STORAGE = f"https://{PROJECT}.supabase.co/storage/v1"
BUCKET = "content_library"
KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
if not KEY:
    sys.exit("SUPABASE_SERVICE_ROLE_KEY not set")

REST_HDR = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
STOR_HDR_BIN = {"apikey": KEY, "Authorization": f"Bearer {KEY}", "Content-Type": "image/png",
                "x-upsert": "true", "Cache-Control": "3600"}


SCENES_DIR = Path("C:/Users/PC/Documents/GitHub/cex/.cex/cache/w10_scenes_w02_p05")

# channel -> (scene filename, storage path suffix)
MAPPING = {
    "threads":   ("01_janela_hero.png",  "w02_p05/1x1/threads.png"),
    "pinterest": ("02_observacao.png",   "w02_p05/2x3/pinterest.png"),
}


def upload_file(local_path: Path, storage_path: str) -> str:
    """Upload file to Storage, return public URL."""
    body = local_path.read_bytes()
    url = f"{STORAGE}/object/{BUCKET}/{storage_path}"
    req = urllib.request.Request(url, data=body, headers=STOR_HDR_BIN, method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            r.read()
    except urllib.error.HTTPError as e:
        if e.code == 409:
            # Already exists, upsert via PUT
            req2 = urllib.request.Request(url, data=body, headers=STOR_HDR_BIN, method="PUT")
            with urllib.request.urlopen(req2) as r:
                r.read()
        else:
            raise
    return f"{STORAGE}/object/public/{BUCKET}/{storage_path}"


def patch_row(row_id: str, url: str) -> None:
    patch_url = f"{REST}/content_library?id=eq.{row_id}"
    body = json.dumps({"storage_url": url, "publish_status": "pending", "ayshare_job_id": None}).encode("utf-8")
    hdr = dict(REST_HDR, **{"Prefer": "return=minimal"})
    req = urllib.request.Request(patch_url, data=body, headers=hdr, method="PATCH")
    with urllib.request.urlopen(req) as r:
        r.read()


def find_rows() -> list[dict]:
    channels = ",".join(MAPPING.keys())
    url = f"{REST}/content_library?post_id=eq.w02_p05&channel=in.({channels})&storage_url=is.null&select=id,channel"
    req = urllib.request.Request(url, headers=REST_HDR)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def main() -> None:
    if not SCENES_DIR.exists():
        sys.exit(f"Scenes dir not found: {SCENES_DIR}")

    rows = find_rows()
    print(f"[i] found {len(rows)} w02_p05 rows needing media")

    for row in rows:
        ch = row["channel"]
        if ch not in MAPPING:
            continue
        fname, sp = MAPPING[ch]
        local = SCENES_DIR / fname
        if not local.exists():
            print(f"  [!!] missing local: {local}")
            continue
        print(f"  uploading {ch} <- {fname}")
        public_url = upload_file(local, sp)
        patch_row(row["id"], public_url)
        print(f"  [OK] {ch}: {public_url}")

    print("[done]")


if __name__ == "__main__":
    main()
