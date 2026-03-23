# CEX Google Drive Setup Guide

**Version**: 1.0.0 | **Time**: ~5 minutes | **Requires**: Google account

## Why Google Drive?

Domain experts (non-devs) contribute knowledge via familiar UI.
No Git, no CLI, no markdown — just drag-and-drop files.

```
Expert drops file     →  Drive folder    →  CEX syncs     →  Pool artifact
(any format)             (by domain)        (auto-triage)    (quality-gated)
```

## Quick Setup (Any Company)

### Step 1: Google Cloud Credentials (~2 min)

```bash
# 1. Go to: https://console.cloud.google.com/apis/credentials
# 2. Create project (or use existing)
# 3. Enable "Google Drive API"
# 4. Create Credentials > OAuth Client ID > Desktop App
# 5. Download JSON
# 6. Save as: _config/client_secret.json
```

### Step 2: Create Drive Structure (~1 min)

```bash
cd your-cex-instance/
python _tools/setup_gdrive.py --setup
```

This creates in your Google Drive:

```
CODEXA Conhecimento/
  marketing/          + _processados/ + _templates/
  pesquisa/           + _processados/ + _templates/
  ecommerce/          + _processados/ + _templates/
  operacoes/          + _processados/ + _templates/
  conhecimento/       + _processados/ + _templates/
  build/              + _processados/ + _templates/
  _templates/         (shared templates)
```

First run opens browser for OAuth consent. After that, token is cached.

### Step 3: Share with Specialists

Right-click each domain folder > Share:
- Marketing team → `marketing/` (Editor)
- Research team → `pesquisa/` (Editor)
- Amazon analysts → `ecommerce/` (Editor)
- CEO → root folder (Owner)

Each specialist sees ONLY their domain folder.

### Step 4: Daily Sync

```bash
# Check what's new
python _tools/setup_gdrive.py --check

# Pull to inbox
python _tools/setup_gdrive.py --sync --inbox records/inbox/raw/

# Or via STELLA
"sincroniza drive"
"processa contribuicoes"
```

## Customizing for Your Company

### Rename Root Folder

Edit `_tools/setup_gdrive.py`, change `root_name`:
```python
STRUCTURE = {
    "root_name": "SUA EMPRESA Conhecimento",  # ← change this
    ...
}
```

### Add/Remove Domain Folders

```python
"folders": {
    "marketing":    {"satellite": "LILY",   "desc": "..."},
    "juridico":     {"satellite": "PYTHA",  "desc": "Legal docs"},  # ← add
    # "operacoes": ...,  # ← remove by commenting
}
```

### Custom Satellite Mapping

Each domain maps to a satellite for processing:
- Files in `marketing/` → LILY processes (markitdown for docs)
- Files in `pesquisa/` → SHAKA processes (firecrawl for URLs)
- Files in `ecommerce/` → YORK processes (data extraction)

Change mappings in `STRUCTURE["folders"]`.

## For Multiple Companies (SaaS)

```python
# Each company gets its own root folder + config
python _tools/setup_gdrive.py --setup --config _config/company_a.yaml
python _tools/setup_gdrive.py --setup --config _config/company_b.yaml

# Sync specific company
python _tools/setup_gdrive.py --sync --config _config/company_a.yaml --inbox records/inbox/raw/
```

## Security Notes

| Item | Rule |
|------|------|
| `client_secret.json` | NEVER commit to git (add to .gitignore) |
| `token.json` | NEVER commit (contains refresh token) |
| Drive permissions | Least privilege: editors on own folder only |
| Sync frequency | Daily or on-demand (not real-time) |
| File size limit | 100MB per file (Drive API limit for direct download) |
| Batch limit | 10 files per sync (quality control) |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "client_secret.json not found" | Download from Google Cloud Console |
| "Token expired" | Delete token.json, run again (re-auth) |
| "Quota exceeded" | Wait 24h or increase quota in Cloud Console |
| "Permission denied" | Check folder sharing settings |
| "File too large" | Split or compress before uploading |
