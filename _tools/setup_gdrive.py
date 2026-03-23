import sys
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")
"""
CEX Google Drive Setup - Creates contributor folder structure.
Replicable: any CEX instance runs this to bootstrap Drive integration.
"""
import os, sys, json, io, argparse
from pathlib import Path
from datetime import datetime

try:
    import yaml
except ImportError:
    yaml = None

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive"]

STRUCTURE = {
    "root_name": "CODEXA Conhecimento",
    "mode": "per_person",  # per_person or per_domain
    "folders": {
        "marketing":    {"satellite": "LILY",   "desc": "Copy, ads, branding"},
        "pesquisa":     {"satellite": "SHAKA",  "desc": "Research, competitors"},
        "ecommerce":    {"satellite": "YORK",   "desc": "Amazon, ML, pricing"},
        "operacoes":    {"satellite": "ATLAS",  "desc": "Deploy, testing"},
        "conhecimento": {"satellite": "PYTHA",  "desc": "General knowledge"},
        "build":        {"satellite": "EDISON", "desc": "Code, architecture"},
        "_templates":   {"satellite": None,      "desc": "Shared templates"},
    }
}
def get_creds(creds_dir):
    token = creds_dir / "token.json"
    secret = creds_dir / "client_secret.json"
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not secret.exists():
                print(f"[ERROR] Put client_secret.json in {creds_dir}/")
                print("Get from: https://console.cloud.google.com/apis/credentials")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(str(secret), SCOPES)
            creds = flow.run_local_server(port=0)
        token.write_text(creds.to_json())
    return creds

def find_or_create(service, name, parent_id=None):
    q = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent_id:
        q += f" and '{parent_id}' in parents"
    r = service.files().list(q=q, fields="files(id,name)").execute()
    if r.get("files"):
        print(f"  [EXISTS] {name} -> {r['files'][0]['id']}")
        return r["files"][0]["id"]
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent_id:
        meta["parents"] = [parent_id]
    f = service.files().create(body=meta, fields="id").execute()
    print(f"  [CREATED] {name} -> {f['id']}")
    return f["id"]

def create_structure(service):
    root_id = find_or_create(service, STRUCTURE["root_name"])
    ids = {"_root": root_id}
    for name in STRUCTURE["folders"]:
        fid = find_or_create(service, name, root_id)
        ids[name] = fid
        if not name.startswith("_"):
            find_or_create(service, "_processados", fid)
            find_or_create(service, "_templates", fid)
    return ids

def check_new(service, ids):
    found = []
    for domain, fid in ids.items():
        if domain.startswith("_"): continue
        q = f"'{fid}' in parents and trashed=false and mimeType!='application/vnd.google-apps.folder'"
        r = service.files().list(q=q, fields="files(id,name,mimeType,size,createdTime)").execute()
        for f in r.get("files", []):
            found.append({"domain": domain, **f})
            kb = int(f.get("size", 0)) / 1024
            print(f"  {domain}/{f['name']} ({kb:.0f}KB)")
    print(f"[FOUND] {len(found)} files")
    return found

def sync_files(service, ids, inbox):
    inbox = Path(inbox)
    inbox.mkdir(parents=True, exist_ok=True)
    files = check_new(service, ids)
    for f in files:
        local = inbox / f"gdrive_{f['domain']}_{f['name']}"
        if local.exists():
            print(f"  [SKIP] {local.name}")
            continue
        try:
            if "google-apps" in f.get("mimeType", ""):
                mime = "application/pdf"
                if "spreadsheet" in f["mimeType"]:
                    mime = "text/csv"
                    local = local.with_suffix(".csv")
                req = service.files().export_media(fileId=f["id"], mimeType=mime)
            else:
                req = service.files().get_media(fileId=f["id"])
            buf = io.BytesIO()
            dl = MediaIoBaseDownload(buf, req)
            done = False
            while not done:
                _, done = dl.next_chunk()
            local.write_bytes(buf.getvalue())
            print(f"  [SYNCED] {local.name} ({len(buf.getvalue())//1024}KB)")
        except Exception as e:
            print(f"  [ERROR] {f['name']}: {e}")

def save_config(ids, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    cfg = {"gdrive": {"root_id": ids["_root"], "folders": {k:v for k,v in ids.items() if k!="_root"}, "created": datetime.now().isoformat()}}
    if yaml:
        path.write_text(yaml.dump(cfg, default_flow_style=False))
    else:
        path.with_suffix(".json").write_text(json.dumps(cfg, indent=2))
    print(f"[OK] Config -> {path}")



def add_person(service, root_id, name):
    """Add a contributor person folder with _processados and _rejeitados."""
    person_id = find_or_create(service, name, root_id)
    find_or_create(service, "_processados", person_id)
    find_or_create(service, "_rejeitados", person_id)
    return person_id

def main():
    p = argparse.ArgumentParser(description="CEX Google Drive Setup")
    p.add_argument("--setup", action="store_true", help="OAuth + create folders")
    p.add_argument("--check", action="store_true", help="Check new files")
    p.add_argument("--add-person", type=str, help="Add contributor folder (name_role)")
    p.add_argument("--sync", action="store_true", help="Sync to inbox/raw/")
    p.add_argument("--inbox", default="records/inbox/raw")
    p.add_argument("--creds", default="_config")
    p.add_argument("--config", default="_config/gdrive.yaml")
    a = p.parse_args()
    creds = get_creds(Path(a.creds))
    if not creds:
        sys.exit(1)
    svc = build("drive", "v3", credentials=creds)
    print("[OK] Connected to Google Drive")
    if a.setup:
        ids = create_structure(svc)
        save_config(ids, a.config)
    elif a.check:
        cfg = json.loads(Path(a.config).read_text()) if a.config.endswith(".json") else __import__("yaml").safe_load(Path(a.config).read_text())
        check_new(svc, cfg["gdrive"]["folders"])
    elif a.sync:
        cfg = json.loads(Path(a.config).read_text()) if a.config.endswith(".json") else __import__("yaml").safe_load(Path(a.config).read_text())
        sync_files(svc, cfg["gdrive"]["folders"], a.inbox)
    elif a.add_person:
        if not Path(a.config).exists():
            print("[ERROR] Run --setup first")
            sys.exit(1)
        cfg = yaml.safe_load(Path(a.config).read_text()) if yaml else json.loads(Path(a.config).read_text())
        root_id = cfg["gdrive"]["root_id"]
        pid = add_person(svc, root_id, a.add_person)
        print(f"[OK] Person folder created: {a.add_person} -> {pid}")
    else:
        p.print_help()

if __name__ == "__main__":
    main()
