---
id: p12_wf_notebooklm_pipeline
kind: workflow
pillar: P12
title: "NotebookLM Pipeline -- KC to Human Content via Browser Automation"
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: N01_intelligence
domain: notebooklm-pipeline
step_count: 6
execution: sequential
agent_groups: [n01_intelligence, n04_knowledge]
timeout: 900
retry_policy: per_step
depends_on: [spec_notebooklm_pipeline]
signals: [complete, error, auth_expired]
spawn_configs: []
quality: 9.0
tags: [workflow, notebooklm, pipeline, browser-automation, content-factory, kc]
tldr: "6-step pipeline: select KCs -> format -> auth check -> upload via Playwright -> activate Estudio -> collect outputs. Zero API -- all browser-based."
density_score: null
---

# NotebookLM Pipeline -- KC to Human Content

## Purpose

Transforms CEX knowledge cards into human-consumable content (podcasts, flashcards, quizzes)
via Google NotebookLM. Since NotebookLM has no public API, all write operations use
Playwright browser automation against the NotebookLM UI.

Compared to alternatives:
- **vs ElevenLabs TTS**: NotebookLM produces 2-host conversational podcasts (not monotone narration)
- **vs manual flashcards**: NotebookLM auto-generates 20-75 cards from source content
- **vs custom quiz builders**: NotebookLM understands context and generates relevant assessments

## Steps

### Step 1: Select KCs [n01_intelligence]
- **Agent**: n01_intelligence
- **Action**: Query KC library by domain, filter by quality >= 8.0, sort by relevance
- **Input**: domain name OR explicit KC paths + target notebook domain
- **Output**: ordered list of KC paths with metadata (title, domain, byte size, quality)
- **Tool**: `cex_retriever.py` (TF-IDF similarity) + `cex_doctor.py` (quality filter)
- **Signal**: kc_selection_complete
- **Timeout**: 60s
- **Constraint**: max 50 KCs per notebook (NotebookLM limit), max 500K words per source

### Step 2: Format KCs [n04_knowledge]
- **Agent**: n04_knowledge
- **Action**: Convert KC markdown to NotebookLM-optimized plain text
- **Input**: KC paths from Step 1
- **Output**: formatted text files (title + clean content, no YAML frontmatter)
- **Transform**:
  - Strip YAML frontmatter (NotebookLM doesn't parse it)
  - Preserve markdown headers (NotebookLM uses them for structure)
  - Expand tables to prose (NotebookLM processes prose better than tables)
  - Prepend title as H1 for source identification
  - Truncate to 200K chars if oversized
- **Signal**: format_complete
- **Timeout**: 120s

### Step 3: Auth Check [n04_knowledge]
- **Agent**: n04_knowledge
- **Action**: Validate Google session cookies are fresh
- **Input**: cookie state file path (`%LOCALAPPDATA%\notebooklm-mcp\Data\browser_state\state.json`)
- **Output**: `{auth_valid: bool, expires_in_days: int, account: str}`
- **Check**: SID, HSID, SSID, APISID, SAPISID cookies present and not expired
- **On failure**: emit `auth_expired` signal, halt pipeline, print re-auth instructions
- **Tool**: `cex_notebooklm.py --reauth` (if interactive session available)
- **Timeout**: 15s

### Step 4: Upload Sources [n04_knowledge]
- **Agent**: n04_knowledge
- **Action**: Paste each formatted KC into target NotebookLM notebook via Playwright
- **Input**: formatted texts from Step 2 + notebook_id from config + cookies from Step 3
- **Output**: `{notebook_id, sources_uploaded: int, indexing_status: str}`
- **Tool**: `cex_notebooklm.py --upload <kc_path> --domain <domain>`
- **Playwright sequence**:
  1. Navigate to notebook URL
  2. Click "Adicionar fontes" (PT-BR)
  3. Click "Texto copiado"
  4. Fill title + paste content
  5. Click "Inserir"
  6. Wait for indexing confirmation (poll 30s, timeout 5min per source)
- **Rate limit**: 1 source per 30 seconds (avoid Google rate limiting)
- **On failure**: screenshot + retry once, then skip source and continue
- **Signal**: upload_complete
- **Timeout**: 300s (scales with source count)

### Step 5: Activate Estudio [n04_knowledge]
- **Agent**: n04_knowledge
- **Action**: Generate outputs via NotebookLM Estudio panel
- **Input**: notebook_id + output types (default: flashcards, audio_summary, quiz)
- **Output**: `{outputs: [{type, status, count_or_duration}]}`
- **Tool**: `cex_notebooklm.py --studio <notebook_id> --outputs flashcards,audio_summary,quiz`
- **Playwright sequence**:
  1. Navigate to notebook
  2. Open Estudio panel (right sidebar)
  3. Click each output button (PT-BR labels)
  4. Poll for completion (flashcards ~30s, audio ~5min, quiz ~30s)
- **On failure**: retry once per output type, report partial success
- **Signal**: studio_complete
- **Timeout**: 600s (audio generation can take 2-10 minutes)

### Step 6: Collect and Report [n01_intelligence]
- **Agent**: n01_intelligence
- **Action**: Update config, compile status report, signal completion
- **Input**: upload results from Step 4 + studio results from Step 5
- **Output**: pipeline execution report
- **Actions**:
  1. Update `notebooklm_notebooks.yaml` with new sources + outputs
  2. Write execution report to `N01_intelligence/output/`
  3. Signal N07 with completion status + quality metrics
- **Tool**: `cex_notebooklm.py --status <notebook_id>`
- **Signal**: complete (with notebook_id + output manifest)
- **Timeout**: 30s

## Data Flow

```
[KC Library]
     |
     v
Step 1: SELECT (cex_retriever + quality filter)
     |  {kc_paths[], domain, quality_scores}
     v
Step 2: FORMAT (strip frontmatter, expand tables, truncate)
     |  {formatted_texts[], titles[]}
     v
Step 3: AUTH CHECK (cookie validation)
     |  {auth_valid, account}
     |
     | [HALT if auth_expired]
     v
Step 4: UPLOAD (Playwright -> NotebookLM UI)
     |  {notebook_id, sources_uploaded, indexing_ok}
     v
Step 5: STUDIO (Playwright -> Estudio panel)
     |  {flashcards: N, audio: Xmin, quiz: N}
     v
Step 6: COLLECT (update config, report, signal)
     |  {execution_report, signal: complete}
     v
[NotebookLM Outputs Ready]
```

## Error Handling

| Step | Error | Action |
|------|-------|--------|
| 1 | No KCs match domain | Return empty list, warn, suggest broader domain |
| 3 | Auth expired | Emit `auth_expired` signal, halt, print `cex_notebooklm.py --reauth` |
| 4 | Playwright timeout | Screenshot + retry once with fresh page |
| 4 | Source limit (50) reached | Warn at 45, halt upload at 50, suggest new notebook |
| 5 | Audio generation timeout (>15min) | Report partial, continue with other outputs |
| Any | Google UI changed (selector miss) | Screenshot for debug, try fallback selectors, fail gracefully |

## Integration Points

| Trigger | From | Action |
|---------|------|--------|
| KC committed in F8 | Any nucleus | Auto-upload if `publish_mode: auto` in config |
| Content Factory Wave 3 | N07 mission | Parallel with N03 tool-based production |
| Manual invocation | User CLI | `python _tools/cex_notebooklm.py --upload <path>` |

## Config Reference

- Pipeline config: `.cex/config/notebooklm_notebooks.yaml`
- Auth state: `%LOCALAPPDATA%\notebooklm-mcp\Data\browser_state\state.json`
- Spec: `_docs/specs/spec_notebooklm_pipeline.md`

## Metrics

| Metric | Target |
|--------|--------|
| KC upload rate | 1 source / 30 seconds |
| Total pipeline time (10 KCs) | < 15 minutes |
| Flashcard generation | 20-75 cards per KC |
| Audio generation | 5-30 min podcast per notebook |
| Success rate (per source) | > 95% |
