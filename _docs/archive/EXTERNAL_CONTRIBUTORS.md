# CEX External Contributors Pipeline

**Version**: 1.0.0 | **Pillar**: P01 (Knowledge) + P04 (Tools) + P09 (Config)

## Problem

Domain experts (non-devs) need to contribute specialized knowledge to CEX instances.
They don't have Git access, CLI skills, or markdown formatting knowledge.
They DO have: Google Drive, domain expertise, files in common formats.

## Architecture

```
EXTERNAL (Google Drive)          INTERNAL (CEX Instance)
────────────────────            ─────────────────────────

📁 organization Conhecimento/         records/inbox/
  📁 marketing/                   raw/       ← synced from Drive
    frameworks.docx                queue/     ← triaged by knowledge_agent
    exemplos_copy.pdf              processed/ ← audit log
    screenshot_campanha.png
  📁 pesquisa/                  records/pool/
    artigo_concorrente.pdf        knowledge/  ← KC_ artifacts
    links_importantes.txt         research/   ← RESEARCH_ artifacts
  📁 ecommerce/                   data/       ← DATA_ artifacts
    planilha_vendas.xlsx          marketing/  ← visual benchmarks
    relatorio_ACOS.pdf
  📁 geral/
    notas_reuniao.txt

        ↓ MCP sync                 ↓ Pipeline
    Drive API pull              knowledge_agent triage → Agent_group distill → Pool
```

## Google Drive Structure

```
organization Conhecimento/           ← Root shared folder
  marketing/                   ← marketing_agent domain
    _processados/              ← System moves originals here after processing
  pesquisa/                    ← research_agent domain
    _processados/
  ecommerce/                   ← commercial_agent domain
    _processados/
  operacoes/                   ← operations_agent domain
    _processados/
  conhecimento/                ← knowledge_agent domain (general knowledge)
    _processados/
  _templates/                  ← Optional: formatted templates for experts
    template_framework.docx
    template_caso_de_uso.docx
    template_analise.xlsx
```

## Contributor Permissions

| Role | Folders | Can Do | Cannot Do |
|------|---------|--------|-----------|
| Marketing specialist | marketing/ | Upload, read _processados | See other domains |
| Amazon analyst | ecommerce/ | Upload, read _processados | See marketing |
| Researcher | pesquisa/ | Upload, read _processados | See ecommerce |
| CEO (orchestrator) | ALL | Upload, read, manage | - |

## Processing Pipeline

### Step 1: Sync (MCP or Manual)

```yaml
# .mcp-ingestion.json
mcpServers:
  google-drive:
    command: npx
    args: [-y, mcp-google-drive]
    env:
      GOOGLE_CREDENTIALS_PATH: "${GOOGLE_CREDENTIALS}"
      DRIVE_FOLDER_ID: "${organization_DRIVE_FOLDER_ID}"
```

Or manual: `rclone sync gdrive:organization_Conhecimento/ records/inbox/raw/`

### Step 2: Triage (knowledge_agent)

knowledge_agent reads each file and classifies:

```yaml
triage:
  file: "frameworks_copy.docx"
  detected_domain: marketing
  detected_type: knowledge_card
  target_lp: P01
  target_agent_group: marketing_agent
  target_pool: pool/knowledge/
  suggested_id: "KC_marketing_agent_COPY_FRAMEWORKS"
  confidence: 0.85
  processing_tool: markitdown  # DOCX → MD conversion
```

### Step 3: Convert (marketing_agent markitdown for docs, research_agent firecrawl for URLs)

```
.docx/.pptx/.pdf → markitdown → clean markdown
.xlsx/.csv → pandas → structured YAML
.png/.jpg → vision model → description + metadata
.mp3/.mp4 → whisper transcript → markdown
.txt/.md → direct (minimal processing)
URLs in .txt → firecrawl → scraped + distilled
```

### Step 4: Distill (Domain Agent_group)

Agent_group applies CEX template + quality standards:
- Adds frontmatter (id, type, lp, version, quality, source)
- Structures content per CEX schema
- Validates density >= 0.8
- Scores quality >= 7.0

### Step 5: Route to Pool

```
pool/knowledge/KC_marketing_agent_COPY_FRAMEWORKS.md     ← quality 8.5 ✅
pool/data/DATA_commercial_agent_ACOS_Q1.yaml              ← quality 7.2 ✅
pool/research/RESEARCH_research_agent_COMPETITOR.md     ← quality 9.0 ✅ Golden
```

### Step 6: Feedback to Contributor

Move original to `_processados/` in Drive with status:
```
frameworks_copy.docx → _processados/frameworks_copy__PROCESSED_8.5.docx
planilha.xlsx → _processados/planilha__PROCESSED_7.2.xlsx
notas.txt → _processados/notas__REJECTED_5.1.txt  ← feedback file created
```

## Templates for Non-Dev Contributors

Optional `.docx` templates in Drive `_templates/` folder:

| Template | Purpose | Helps With |
|----------|---------|------------|
| Framework Template | Document a method/process | KC_ knowledge cards |
| Case Study Template | Document a success story | RESEARCH_ artifacts |
| Analysis Spreadsheet | Structured data input | DATA_ artifacts |
| Competitor Brief | Quick competitor snapshot | RESEARCH_ artifacts |
| Meeting Notes | Structured meeting capture | KC_ knowledge cards |

Templates have colored sections: GREEN = fill this, GRAY = system fills, RED = don't touch.

## Anti-Patterns

- **NEVER** give specialists direct repo access (Git conflicts, format issues)
- **NEVER** process without triage (wrong domain = wrong agent_group)
- **NEVER** skip quality gate (low quality artifacts poison the pool)
- **NEVER** lose originals (always move to _processados, never delete)
- **NEVER** process more than 10 files per batch (quality drops with volume)

## Metrics

Track per contributor:
- Files submitted / month
- Acceptance rate (>= 7.0 / total)
- Average quality score
- Domain coverage gaps filled
