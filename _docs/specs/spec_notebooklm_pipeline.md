---
id: spec_notebooklm_pipeline
kind: constraint_spec
pillar: P06
title: "Spec NotebookLM Pipeline — KC to Human Content via Browser Automation"
version: 1.0.0
created: 2026-04-06
author: n04_knowledge
domain: notebooklm-pipeline
quality_target: 9.0
status: READY
scope: N03_BUILD + N04_KNOWLEDGE
depends_on:
  - HANDOFF_notebooklm_pipeline (PoC validated by N04)
  - spec_content_factory_v1 (parent spec)
tags: [spec, notebooklm, pipeline, browser-automation, playwright, content-factory, flashcards, audio, quiz]
tldr: "Formal spec for Fase 1 of the NotebookLM pipeline. Tool: cex_notebooklm.py (upload/studio/status/list). Config: notebooklm_notebooks.yaml (domain→notebook mapping). Auth: Chrome profile reuse + session expiry detection. Integration: F8 hook + N04 auto-upload + N02 downstream."
density_score: null
quality: 9.2
updated: "2026-04-07"
---

# Spec NotebookLM Pipeline — KC → Human Content

## 1. ARCHITECTURE

### Data Flow

```
                         CEX SYSTEM                          │  EXTERNAL (Google)
                                                             │
  KC .md file                                                │
    │                                                        │
    ▼                                                        │
  cex_notebooklm.py --upload <kc_path>                       │
    │                                                        │
    ├─ Reads KC content from disk                            │
    ├─ Resolves domain from KC frontmatter (kind/domain)     │
    ├─ Looks up notebook_id in notebooklm_notebooks.yaml     │
    │   ├─ Found → reuse existing notebook                   │
    │   └─ Not found → create new notebook (Playwright)      │
    ├─ Loads Google cookies from MCP browser state            │
    ├─ Launches Playwright (headless=false, Chrome)           │
    │                                                        │
    ▼                                                        │
  Playwright Browser Session ──────────────────────────────► │ NotebookLM UI
    │  1. Navigate to notebook URL                           │   (notebooklm.google.com)
    │  2. Click "Adicionar fontes"                           │
    │  3. Click "Texto copiado"                              │
    │  4. Fill title + paste KC content                      │
    │  5. Click "Inserir"                                    │
    │  6. Wait for indexing (30s-5min)                       │
    │                                                        │
    ▼                                                        │
  cex_notebooklm.py --studio <notebook_id>                   │
    │                                                        │
    ├─ Option A: Playwright clicks Estúdio outputs           │
    │   └─ "Cartões didáticos", "Resumo em áudio", etc.     │
    ├─ Option B: claude --chrome spawns Chrome MCP           │
    │   └─ Uses mcp__claude-in-chrome__* (18 tools)         │
    │                                                        │
    ▼                                                        │
  NotebookLM Estúdio generates:                              │ Gemini processes
    ├─ Flashcards (20-75 cards)                              │   sources and
    ├─ Audio Summary (5-30min podcast, 2 hosts)              │   generates outputs
    └─ Quiz (10-20 questions)                                │
         │                                                   │
         ▼                                                   │
  Outputs available in NotebookLM UI                         │
    │                                                        │
    ▼                                                        │
  cex_notebooklm.py --status <notebook_id>                   │
    └─ Reports: sources indexed, outputs generated           │
```

### Component Map

| Component | Type | Path | Status |
|-----------|------|------|--------|
| `cex_notebooklm.py` | Unified CLI tool | `_tools/cex_notebooklm.py` | TO BUILD (N03) |
| `notebooklm_notebooks.yaml` | Config registry | `.cex/P09_config/notebooklm_notebooks.yaml` | TO BUILD (N04 draft) |
| `notebooklm_create.py` | Prototype (create notebook) | `_tools/notebooklm_create.py` | EXISTS (PoC) |
| `notebooklm_paste.py` | Prototype (paste into notebook) | `_tools/notebooklm_paste.py` | EXISTS (PoC) |
| NotebookLM MCP | 17 tools (query, list, search) | `.mcp-n04.json` | EXISTS (auth expires) |
| Chrome MCP | 18 tools (browser control) | via `claude --chrome` flag | EXISTS (requires spawn) |

### Key Constraint: No Public API

NotebookLM has NO REST API. All automation is browser-based:
- **Playwright** for deterministic UI automation (create, paste, click)
- **Chrome MCP** (via `claude --chrome`) for AI-driven UI navigation
- **NotebookLM MCP** for read operations (list, search, ask_question)

This means: all write operations (upload sources, activate Estúdio) require a visible browser window.

---

## 2. TOOL SPEC: `cex_notebooklm.py`

### Overview

Unified CLI that consolidates the two prototypes (`notebooklm_create.py`, `notebooklm_paste.py`) into a single tool with 4 subcommands.

### CLI Interface

```bash
# Upload a KC as source to a domain notebook
python _tools/cex_notebooklm.py --upload <kc_path> [--domain <domain>] [--notebook <id>]

# Activate Estúdio outputs for a notebook
python _tools/cex_notebooklm.py --studio <notebook_id> --outputs flashcards,audio_summary,quiz

# Check status of a notebook (sources, outputs, last sync)
python _tools/cex_notebooklm.py --status <notebook_id>

# List all tracked notebooks with domain mapping
python _tools/cex_notebooklm.py --list
```

### Subcommand: `--upload`

**Input**: Path to a KC `.md` file.
**Behavior**:

1. Read KC file, extract frontmatter (`domain`, `kind`, `title`).
2. Resolve domain:
   - If `--domain` provided → use it.
   - Else → infer from KC's `domain` field or parent directory (e.g., `library/integration/` → `integration`).
3. Look up `notebooklm_notebooks.yaml` for domain → notebook_id mapping.
   - If mapping exists and notebook is reachable → paste KC as new source.
   - If no mapping → create new notebook, save notebook_id to config.
4. Load Google cookies from MCP browser state:
   ```
   Path: %LOCALAPPDATA%\notebooklm-mcp\Data\browser_state\state.json
   ```
5. Launch Playwright (headless=false):
   - Navigate to notebook URL
   - Click "Adicionar fontes" → "Texto copiado"
   - Fill title from KC frontmatter `title`
   - Paste KC content (up to 200K chars — NotebookLM limit is 500K words per source)
   - Click "Inserir"
   - Wait for indexing confirmation (poll for "pronto" / source count change)
6. Update `notebooklm_notebooks.yaml`:
   - `last_sync` timestamp
   - Increment `source_count`
   - Add KC path to `sources` list
7. Return: `{ notebook_id, domain, source_title, status: "indexed" }`

**Error handling**:
- Auth expired → print `[AUTH_EXPIRED] Run: python _tools/cex_notebooklm.py --reauth`
- Playwright timeout → screenshot + retry once
- Source limit reached (50) → warn, suggest new notebook

### Subcommand: `--studio`

**Input**: `notebook_id` + comma-separated output list.
**Default outputs** (from GDP D2): `flashcards,audio_summary,quiz`
**Behavior**:

1. Navigate to notebook.
2. Locate "Estúdio" panel (right sidebar in NotebookLM UI).
3. For each requested output:
   - Click the output button (PT-BR labels):
     - `flashcards` → "Cartões didáticos"
     - `audio_summary` → "Resumo em áudio"
     - `quiz` → "Teste"
     - `mind_map` → "Mapa mental"
     - `briefing` → "Documento de resumo"
     - `timeline` → "Linha do tempo"
     - `faq` → "Perguntas frequentes"
   - Wait for generation (varies: flashcards ~30s, audio ~5min)
4. Publish mode (from GDP D3): auto-publish — no manual approval step.
5. Update config: `outputs_generated` list + timestamp.
6. Return: `{ notebook_id, outputs: [{type, status, count_or_duration}] }`

**Implementation note**: For audio_summary, generation can take 2-10 minutes. The tool should poll every 30s with a 15-minute timeout.

### Subcommand: `--status`

**Input**: `notebook_id`
**Behavior**:

1. Query via NotebookLM MCP: `get_notebook` → source count, name.
2. Read local config for: last_sync, sources uploaded, outputs generated.
3. Return combined status:
   ```yaml
   notebook_id: 940fd258-...
   domain: meta
   name: "CEX Meta Knowledge"
   sources: 5
   last_sync: 2026-04-06T18:00:00
   outputs:
     flashcards: generated (75 cards)
     audio_summary: generated (12min)
     quiz: pending
   ```

### Subcommand: `--list`

**Behavior**: Read `notebooklm_notebooks.yaml`, format as table.

```
DOMAIN          NOTEBOOK_ID                              SOURCES  LAST_SYNC
meta            940fd258-847f-47c1-b7e6-caca7b730681     2        2026-04-06
brand           (not created)                            0        —
integration     (not created)                            0        —
kind            (not created)                            0        —
```

### Subcommand: `--reauth`

**Behavior**: Re-authenticate Google session.

1. Launch Playwright with visible Chrome.
2. Navigate to `accounts.google.com`.
3. Wait for user to complete login (poll for cookie presence, 120s timeout).
4. Save cookies to MCP state file.
5. Alternatively: call NotebookLM MCP `setup_auth` or `re_auth` tool.

### Dependencies

```
playwright          # Browser automation (pip install playwright && playwright install chromium)
pyyaml              # Config read/write
pathlib, json       # Standard lib
```

### Code Structure (for N03)

```python
# _tools/cex_notebooklm.py

import argparse, json, time, yaml
from pathlib import Path
from datetime import datetime, timezone

CONFIG_PATH = Path(".cex/config/notebooklm_notebooks.yaml")
STATE_FILE = Path(os.environ.get("LOCALAPPDATA", "")) / "notebooklm-mcp/Data/browser_state/state.json"
NOTEBOOKLM_BASE = "https://notebooklm.google.com"

# --- Cookie Management ---
def load_cookies() -> list[dict]: ...
def check_auth(cookies: list) -> bool: ...

# --- Config Management ---
def load_config() -> dict: ...
def save_config(config: dict): ...
def resolve_domain(kc_path: Path, explicit: str | None) -> str: ...
def get_notebook_id(domain: str) -> str | None: ...

# --- Playwright Actions ---
def create_notebook(name: str, cookies: list) -> str: ...  # returns notebook_id
def paste_source(notebook_id: str, title: str, content: str, cookies: list) -> bool: ...
def activate_studio(notebook_id: str, outputs: list[str], cookies: list) -> list[dict]: ...

# --- Subcommands ---
def cmd_upload(args): ...
def cmd_studio(args): ...
def cmd_status(args): ...
def cmd_list(args): ...
def cmd_reauth(args): ...

# --- UI Selectors (PT-BR) ---
SELECTORS = {
    "add_source": ['button:has-text("Adicionar fontes")', '[aria-label*="Adicionar"]'],
    "copied_text": [':text("Texto copiado")', 'button:has-text("Texto copiado")'],
    "title_input": ['input[placeholder*="título"]', 'input[type="text"]'],
    "content_area": ['textarea[aria-label="Texto colado"]', '.cdk-overlay-pane textarea'],
    "insert_btn": ['.cdk-overlay-pane button:has-text("Inserir")', 'button:has-text("Inserir")'],
    "studio_flashcards": [':text("Cartões didáticos")'],
    "studio_audio": [':text("Resumo em áudio")'],
    "studio_quiz": [':text("Teste")'],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CEX NotebookLM Pipeline Tool")
    # ... argparse setup ...
    main()
```

### Selector Strategy

NotebookLM UI is Angular Material (PT-BR locale). Selectors must:
1. Try PT-BR labels first, EN fallback.
2. Use `force=True` on clicks to bypass Material overlay (`cdk-overlay-pane`).
3. Target `aria-label` when text selectors fail.
4. Fall back to JavaScript injection for Angular `formcontrolname` elements.

Known selectors (validated in PoC):

| Element | Primary Selector | Fallback |
|---------|-----------------|----------|
| Add sources button | `button:has-text("Adicionar fontes")` | `[aria-label*="Adicionar"]` |
| Copied text option | `:text("Texto copiado")` | `:text("Copied text")` |
| Title input | `input[placeholder*="título"]` | `mat-dialog-container input` |
| Content textarea | `textarea[aria-label="Texto colado"]` | `.cdk-overlay-pane textarea` |
| Insert button | `.cdk-overlay-pane button:has-text("Inserir")` | `button:has-text("Insert")` |
| Estúdio panel | `:text("Estúdio")` | `[aria-label*="Studio"]` |

---

## 3. CONFIG SPEC: `notebooklm_notebooks.yaml`

### Schema

```yaml
# .cex/config/notebooklm_notebooks.yaml
# Domain → NotebookLM notebook mapping
# GDP D1: 1 notebook per DOMAIN (reusable, not per-mission)

version: 1
google_account: {{BRAND_EMAIL}}   # GDP D5
publish_mode: auto                            # GDP D3
browser_engine: chrome_local                  # GDP D4
default_outputs:                              # GDP D2
  - flashcards
  - audio_summary
  - quiz

cookie_source: "%LOCALAPPDATA%\\notebooklm-mcp\\Data\\browser_state\\state.json"

domains:
  meta:
    notebook_id: "940fd258-847f-47c1-b7e6-caca7b730681"
    name: "CEX Meta Knowledge"
    description: "8F pipeline, architecture, nuclei, pillars, system design"
    sources:
      - path: "P01_knowledge/library/domain/meta/kc_8f_pipeline.md"
        uploaded: 2026-04-06
    source_count: 2
    outputs_generated:
      - type: flashcards
        count: 75
        generated: 2026-04-06
    last_sync: 2026-04-06T17:00:00-03:00
    status: active

  brand:
    notebook_id: null  # to be created on first upload
    name: "Brand Knowledge"
    description: "Brand identity, voice, visual guidelines, positioning"
    sources: []
    source_count: 0
    outputs_generated: []
    last_sync: null
    status: pending

  integration:
    notebook_id: null
    name: "Integration Knowledge"
    description: "External tool integrations: Canva, ElevenLabs, YouTube, etc."
    sources: []
    source_count: 0
    outputs_generated: []
    last_sync: null
    status: pending

  kind:
    notebook_id: null
    name: "Kind Reference"
    description: "115 kind KCs — type system, builders, schemas"
    sources: []
    source_count: 0
    outputs_generated: []
    last_sync: null
    status: pending

  operations:
    notebook_id: null
    name: "Operations Knowledge"
    description: "DevOps, CI/CD, testing, deployment patterns"
    sources: []
    source_count: 0
    outputs_generated: []
    last_sync: null
    status: pending

  commercial:
    notebook_id: null
    name: "Commercial Knowledge"
    description: "Pricing, monetization, funnels, courses"
    sources: []
    source_count: 0
    outputs_generated: []
    last_sync: null
    status: pending
```

### Validation Rules

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `version` | int | yes | Must be 1 |
| `google_account` | string | yes | Valid email |
| `publish_mode` | enum | yes | `auto` or `manual` |
| `browser_engine` | enum | yes | `chrome_local` or `firecrawl_cloud` |
| `default_outputs` | list[str] | yes | Subset of: flashcards, audio_summary, quiz, mind_map, briefing, timeline, faq, infographic, presentation, video, data_table |
| `domains.*.notebook_id` | string/null | yes | UUID or null |
| `domains.*.sources` | list | yes | Each: {path, uploaded} |
| `domains.*.source_count` | int | yes | <= 50 (NotebookLM limit) |

---

## 4. INTEGRATION POINTS

### 4.1 F8 COLLABORATE Hook

After any KC is committed in F8, optionally publish to NotebookLM:

```python
# In cex_hooks.py post_save hook (or as standalone post-commit hook)

def post_save_notebooklm(artifact_path: Path):
    """Called after F8 saves a KC. Publishes to NotebookLM if configured."""
    import yaml

    # Only trigger for knowledge_cards
    with open(artifact_path) as f:
        content = f.read()
    if "kind: knowledge_card" not in content[:500]:
        return

    # Check if auto-publish is enabled
    config = yaml.safe_load(open(".cex/config/notebooklm_notebooks.yaml"))
    if config.get("publish_mode") != "auto":
        return

    # Upload
    import subprocess
    result = subprocess.run(
        ["python", "_tools/cex_notebooklm.py", "--upload", str(artifact_path)],
        capture_output=True, text=True, timeout=120
    )
    if result.returncode == 0:
        print(f"[NotebookLM] Uploaded: {artifact_path.name}")
    else:
        print(f"[NotebookLM] Upload failed: {result.stderr[:200]}")
```

**When it fires**: Every time a KC passes F7 governance and is saved in F8.
**Guard**: Only fires if `publish_mode: auto` in config. Only for `kind: knowledge_card`.

### 4.2 N04 Workflow: KC Save → Auto-Upload

When N04 produces or updates a KC during a mission:

```
N04 builds KC via 8F
    → F8 COLLABORATE: save .md, compile .yaml, git commit
    → F8 Hook: cex_notebooklm.py --upload <path>
        → KC is pasted into domain notebook
        → Config updated with new source
    → Signal: n04 complete
```

This means every KC N04 produces is automatically available in NotebookLM within seconds of being committed.

### 4.3 N02 Downstream: Generated Content → Social Publishing

After Estúdio generates outputs:

```
N04: --studio activates flashcards + audio + quiz
    │
    ▼
N02 Marketing can consume:
    ├─ Audio Overview → edit with FFmpeg → publish as podcast (Spotify, YouTube)
    ├─ Flashcards → extract text → social carousel (Canva API)
    ├─ Quiz → embed in course module (Hotmart via N06)
    └─ Briefing Doc → email newsletter content
```

**Handoff format**: N04 signals completion with notebook_id + outputs list. N02/N06 read the config to find what was generated.

### 4.4 Mission Integration

In a Content Factory mission (`dag_cf_master`):

```
Wave 3 PRODUCE:
    N03 (parallel): Canva, Marp, Typst, ElevenLabs, FFmpeg
    N04 (parallel): NotebookLM upload + Estúdio activation
        ├─ Upload all KCs from Wave 1 research
        ├─ Activate: flashcards + audio_summary + quiz (D2 defaults)
        └─ Signal with output manifest
```

N04's NotebookLM work runs in parallel with N03's tool-based production. No dependency between them — both read from the same KC sources.

---

## 5. AUTH MANAGEMENT

### 5.1 Cookie Architecture

```
Google Account ({{BRAND_EMAIL}})
    │
    ▼
NotebookLM MCP Server (Puppeteer-based)
    │ Logs in via browser, saves cookies
    ▼
%LOCALAPPDATA%\notebooklm-mcp\Data\browser_state\state.json
    │ Contains: cookies[], localStorage, sessionStorage
    ▼
cex_notebooklm.py reads cookies from state.json
    │ Injects into Playwright browser context
    ▼
Playwright operates NotebookLM UI as authenticated user
```

### 5.2 Session Expiry Detection

Google session cookies expire after ~14 days of inactivity. Detection:

```python
def check_auth_valid(cookies: list) -> bool:
    """Check if cookies are likely still valid."""
    # 1. Check for essential cookies
    essential = {"SID", "HSID", "SSID", "APISID", "SAPISID"}
    present = {c["name"] for c in cookies}
    if not essential.issubset(present):
        return False

    # 2. Check expiry timestamps
    import time
    now = time.time()
    for c in cookies:
        if c["name"] in essential:
            if c.get("expires", 0) > 0 and c["expires"] < now:
                return False

    return True
```

### 5.3 Re-Authentication Flow

When auth expires:

```
[AUTH_EXPIRED] detected
    │
    ├─ Option 1 (preferred): NotebookLM MCP re_auth
    │   Tool: mcp__notebooklm__re_auth or mcp__notebooklm__setup_auth
    │   Spawns Puppeteer browser → user logs in → cookies saved
    │
    ├─ Option 2: Playwright re-auth
    │   python _tools/cex_notebooklm.py --reauth
    │   Launches visible Chromium → navigates to accounts.google.com
    │   Waits for user to complete login (120s timeout)
    │   Saves cookies to state.json
    │
    └─ Option 3 (fallback): Manual paste
        User manually opens NotebookLM → pastes KC content
        Only for emergency — bypasses automation entirely
```

### 5.4 Chrome Profile Isolation

**Problem**: Playwright and system Chrome cannot share the same profile simultaneously (lock file conflict).

**Solution**: Playwright uses its own Chromium instance with injected cookies (not a shared Chrome profile). Cookies are extracted from the MCP server's `state.json`, which is updated independently.

**Consequence**: If the user logs out of their system Chrome, MCP cookies may still be valid (and vice versa). The two sessions are independent.

### 5.5 Security Notes

- Cookies are stored locally in `%LOCALAPPDATA%` (user-scoped, not world-readable).
- Google account `{{BRAND_EMAIL}}` is a dedicated automation account (not personal).
- The `--dangerously-skip-permissions` flag is only needed when spawning Chrome MCP clones, not for Playwright uploads.
- No credentials are stored in the CEX repository. Cookie state is machine-local.

---

## 6. DOMAIN → NOTEBOOK MAPPING (Initial Draft)

Based on existing KC library structure (`P01_knowledge/library/`):

| Domain | Notebook Name | KC Source Directories | Est. Sources |
|--------|--------------|----------------------|-------------|
| `meta` | CEX Meta Knowledge | `library/domain/meta/` | ~10 KCs |
| `brand` | Brand Knowledge | `library/domain/brand/` | ~5 KCs |
| `integration` | Integration Knowledge | `library/integration/` | ~10 KCs (Canva, ElevenLabs, YouTube, etc.) |
| `kind` | Kind Reference | `library/kind/` | ~115 KCs (one per kind) |
| `operations` | Operations Knowledge | `library/domain/operations/` | ~5 KCs |
| `commercial` | Commercial Knowledge | `library/domain/commercial/` | ~5 KCs |

**Note on `kind` domain**: 115 KCs exceeds the 50-source limit per notebook. Strategy:
- Split into sub-notebooks: `kind-p01` (P01 kinds), `kind-p02` (P02 kinds), etc.
- Or: upload only the most-used kinds first, expand as needed.
- Decision deferred to N03 implementation — the config schema supports dynamic notebook creation.

---

## 7. RISKS AND MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|------------|
| Google changes NotebookLM UI selectors | Upload/Studio breaks | Selector strategy with multiple fallbacks + screenshot-on-failure for debug |
| Auth expires mid-mission | Pipeline halts | Pre-flight auth check in every subcommand + `--reauth` subcommand |
| Source limit (50) reached | Cannot add more KCs | Warn at 45 sources, auto-create spillover notebook |
| Estúdio generation slow (audio: 2-10 min) | Mission wave timeout | Async polling with 15-min timeout, configurable |
| Playwright not installed on target machine | Tool fails on first run | Clear error message + install instructions |
| NotebookLM launches public API | This spec becomes partially obsolete | Abstract browser actions behind interface — swap to REST when available |

---

## 8. IMPLEMENTATION PLAN (for N03, Wave 2)

### Phase 1: Core Tool (priority HIGH)

| # | Task | Complexity | Depends On |
|---|------|-----------|------------|
| 1 | Consolidate prototypes into `cex_notebooklm.py` | Medium | Prototypes exist |
| 2 | Implement `--upload` with domain resolution | Medium | Config schema |
| 3 | Implement `--studio` with default outputs | Medium | Upload working |
| 4 | Implement `--status` (MCP + local config) | Low | Config schema |
| 5 | Implement `--list` (config reader) | Low | Config schema |
| 6 | Implement `--reauth` | Low | Cookie path known |
| 7 | Create `notebooklm_notebooks.yaml` with `meta` domain populated | Low | This spec |

### Phase 2: Integration Hooks

| # | Task | Complexity |
|---|------|-----------|
| 8 | Add F8 post-save hook for auto-upload | Low |
| 9 | Add pre-flight auth check to all subcommands | Low |
| 10 | Integration test: upload KC → verify in NotebookLM MCP list | Medium |

### Phase 3: Resilience

| # | Task | Complexity |
|---|------|-----------|
| 11 | Screenshot-on-failure debugging | Low |
| 12 | Retry logic (1 retry on timeout) | Low |
| 13 | Source count guard (warn at 45, block at 50) | Low |

**Estimated N03 effort**: 8-12 tasks, all within existing kind/tool scope.

---

## DONE WHEN

- [ ] `cex_notebooklm.py` exists with 5 subcommands (upload, studio, status, list, reauth)
- [ ] `notebooklm_notebooks.yaml` exists with 6 domains mapped
- [ ] `--upload` successfully pastes a KC into `meta` notebook
- [ ] `--studio` activates flashcards + audio + quiz
- [ ] `--status` returns combined MCP + local config data
- [ ] F8 hook auto-uploads KCs when `publish_mode: auto`
- [ ] Auth expiry detected and re-auth flow works
- [ ] `python _tools/cex_doctor.py` still passes
