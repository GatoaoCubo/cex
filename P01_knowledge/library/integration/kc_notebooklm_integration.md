---
id: p01_kc_notebooklm_integration
kind: knowledge_card
type: domain
pillar: P01
title: "NotebookLM Integration — AI-Powered Content Transformation"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: notebooklm
quality: null
tags: [notebooklm, google, audio-overview, study-guide, quiz, content-factory, integration, INJECT]
tldr: "Feed docs to NotebookLM to auto-generate Audio Overviews (podcasts), Video Overviews, Study Guides, Quizzes, FAQs, Timelines, and Flashcards"
when_to_use: "When any nucleus needs to transform existing documents into multi-format learning/engagement content"
keywords: [notebooklm, audio-overview, podcast, study-guide, quiz, flashcards, faq, timeline]
feeds_kinds: [workflow, dag, audio_tool]
linked_artifacts: [kc_elevenlabs_tts, kc_youtube_api, kc_pandoc_pipeline]
density_score: null
---

# NotebookLM Integration

## Quick Reference
```yaml
service: Google NotebookLM
url: https://notebooklm.google.com
auth: Google Account (free with Google One AI Premium for advanced features)
mcp_server: notebooklm-mcp
mcp_tools:
  - add_notebook        # Create new notebook from sources
  - select_notebook     # Switch active notebook
  - ask_question        # Query notebook content
  - get_notebook        # Get notebook details
  - list_notebooks      # List all notebooks
  - search_notebooks    # Search across notebooks
  - remove_notebook     # Delete notebook
  - list_sessions       # Active browser sessions
  - get_library_stats   # Usage statistics
max_sources_per_notebook: 50
max_source_size: 500,000 words per source (or 200MB file)
supported_inputs: [Google Docs, Google Slides, PDF, Web URL, plain text, YouTube URL, audio file]
```

## Capabilities (Content Outputs)

| Output | What It Generates | Duration/Size | Best For |
|--------|-------------------|---------------|----------|
| **Audio Overview** | 2-speaker conversational podcast discussing your docs | 5-30 min | Repurposing long content into podcast format |
| **Video Overview** | Visual companion to Audio Overview with key points | 5-30 min | YouTube/social video from existing docs |
| **Study Guide** | Structured summary with key concepts, definitions | 2-5 pages | Course companions, onboarding docs |
| **Quiz** | Multiple choice + short answer questions | 10-20 questions | Testing comprehension, course validation |
| **Flashcards** | Front/back pairs for key terms and concepts | 20-50 cards | Spaced repetition, learning aids |
| **FAQ** | Common questions + answers from source material | 10-30 Q&A pairs | Help centers, product pages |
| **Timeline** | Chronological events extracted from sources | Variable | Historical content, project histories |
| **Briefing Doc** | Executive summary of all sources | 1-3 pages | Quick decision-making briefs |
| **Table of Contents** | Structural outline of source material | 1 page | Navigation aid for large docs |

## Workflow: Feed Documents → Generate Content

### Step 1: Create Notebook with Sources

Via MCP (programmatic):
```
Tool: add_notebook
Input: {
  "name": "AI Guide for Creators",
  "sources": [
    {"type": "url", "value": "https://docs.google.com/document/d/abc123"},
    {"type": "url", "value": "https://example.com/ai-workflow-guide"},
    {"type": "text", "value": "Additional context: this is for Brazilian creators..."}
  ]
}
```

Via UI (manual):
1. Go to notebooklm.google.com → New Notebook
2. Upload: PDFs, paste URLs, or link Google Docs
3. Wait for processing (30s-5min depending on volume)

### Step 2: Generate Audio Overview

Via UI: Click "Audio Overview" → "Generate" → wait 2-5 min → download MP3

The Audio Overview creates a natural 2-speaker podcast where AI hosts discuss your documents. They explain concepts, ask each other questions, and make the content engaging.

**Customization options:**
- Focus on specific sources (select which sources to include)
- Custom instructions: "Focus on practical applications, not theory"
- Target audience: "Explain for beginners" or "Keep it technical"
- Language: auto-detects from source material (PT-BR works natively)

### Step 3: Generate Study Materials

Via UI: Notebook Guide panel → select output type → Generate

Each output can be regenerated with different focus areas. Combine multiple outputs for a complete content package.

## Content Factory Integration Pattern

```
Source Documents (ebooks, blog posts, guides)
    │
    ▼
NotebookLM Notebook
    │
    ├── Audio Overview ──→ YouTube podcast episode
    │                       (combine with Canva thumbnail)
    │
    ├── Video Overview ──→ YouTube/social video
    │
    ├── Study Guide ───→ PDF via Typst (course companion)
    │
    ├── Quiz ──────────→ Course module assessment
    │
    ├── Flashcards ────→ Anki deck / app integration
    │
    ├── FAQ ───────────→ Website help section
    │
    └── Briefing Doc ──→ Email newsletter / social carousel
```

## MCP Server Operations

```python
# Via MCP tools in Claude Code

# List all notebooks
# Tool: list_notebooks

# Search for specific content
# Tool: search_notebooks
# Input: {"query": "AI workflow automation"}

# Ask a question against loaded docs
# Tool: ask_question
# Input: {"question": "What are the top 3 tools mentioned for video creation?"}

# Get notebook stats
# Tool: get_library_stats
```

## Feeding Strategy (Maximize Quality)

| Source Type | How to Feed | Tips |
|-------------|------------|------|
| Blog posts | Web URL | Clean URLs without tracking params |
| Ebooks | PDF upload | Split 500+ page books into chapters |
| Video transcripts | Plain text paste | Clean up auto-captions first |
| Presentations | Google Slides link | Include speaker notes for context |
| Research papers | PDF upload | Works well with academic format |
| Code documentation | Plain text or URL | Add explanatory context alongside code |
| Meeting notes | Google Docs link | NotebookLM understands conversation format |

**Optimal source mix:** 5-15 sources of 1,000-50,000 words each. More focused sources = better outputs.

## Audio Overview Best Practices

- **Keep notebooks focused.** 3-10 related sources > 50 scattered sources. Focused = coherent podcast.
- **Add a text source with instructions**: "This content is for Brazilian creators aged 25-40. Keep the tone conversational and use practical examples."
- **PT-BR sources produce PT-BR audio.** Language follows the source material. Don't mix PT-BR and EN sources in one notebook.
- **Download immediately.** Audio files are generated fresh each time. There's no persistent storage — save the MP3.
- **Post-process with FFmpeg**: add intro/outro music, normalize volume, add chapter markers.

## Gotchas

- **No public API (REST) yet.** Integration is via MCP server (browser automation) or manual UI. No REST endpoints for generation.
- **Audio Overview generation takes 2-10 minutes.** Not instant. Plan for async workflow.
- **50 source limit per notebook.** For large content libraries, create thematic notebooks (not one mega-notebook).
- **Audio Overviews are non-deterministic.** Same sources can produce different podcasts on regeneration. Save good ones immediately.
- **Video Overview requires Google One AI Premium** ($20/mo). Audio Overview is available on free tier.
- **MCP session depends on browser auth.** If Google session expires, MCP tools fail. Use `re_auth` tool to refresh.
- **Source processing is not instant.** Large PDFs (100+ pages) can take 5+ minutes to index. Wait for "Ready" status before generating outputs.
- **No edit/trim capability.** You can't edit the generated audio/video. Regenerate with different instructions or post-process with FFmpeg.
- **Content accuracy**: NotebookLM can hallucinate details when sources are ambiguous. Always review generated Study Guides and Quizzes for accuracy.

## Cost

| Tier | Audio Overview | Video Overview | Other Outputs |
|------|---------------|----------------|---------------|
| Free (Google Account) | Yes (limited/day) | No | Yes |
| Google One AI Premium ($20/mo) | Unlimited | Yes | Yes |

For Content Factory: Google One AI Premium is required for Video Overviews and higher rate limits.

## Docs
- Product page: https://notebooklm.google.com
- Help center: https://support.google.com/notebooklm
- MCP server: configured in `.mcp-*.json` as `notebooklm-mcp`
