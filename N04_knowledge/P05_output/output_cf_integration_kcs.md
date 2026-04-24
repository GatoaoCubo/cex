---
id: n04_output_cf_integration_kcs
kind: output
8f: F6_produce
pillar: P01
nucleus: N04
mission: MISSION_content_factory_wave2
task: build_integration_knowledge_cards
created: 2026-04-06
author: n04_knowledge
quality: 9.0
density_score: 1.0
related:
  - p12_dr_content_factory
  - spec_content_factory_v1
  - wf_kc_to_content
  - p12_wf_cf_publish_youtube
  - output_content_factory_internal_audit
  - output_content_factory_landscape
  - p01_kc_notebooklm_integration
  - p05_fmt_content_adapter
  - p03_sp_social_publisher_builder
  - p05_out_cf_actions_and_distribution
---

# N04 Output: Content Factory Integration Knowledge Cards

## Summary

Built **10 integration Knowledge Cards** in `P01_knowledge/library/integration/` covering all tools required by the Content Factory pipeline.

## Artifacts Created

| # | File | Domain | Bytes | Sections | Key Content |
|---|------|--------|-------|----------|-------------|
| 1 | `kc_canva_connect_api.md` | Canva API | ~4.8K | 8 | OAuth PKCE flow, autofill, export formats, rate limits |
| 2 | `kc_elevenlabs_tts.md` | ElevenLabs | ~4.9K | 9 | multilingual_v2, PT-BR voices, cloning, streaming, pricing/char |
| 3 | `kc_runway_api.md` | Runway Gen-4 | ~4.5K | 7 | image-to-video, text-to-video, async polling, prompt tips |
| 4 | `kc_ffmpeg_patterns.md` | FFmpeg | ~5.1K | 10 | 8 recipes: concat, audio mix, subtitles, thumbnail, convert, trim, overlay, speed |
| 5 | `kc_marp_cli.md` | Marp | ~4.7K | 8 | Slide syntax, directives, images, themes, batch export |
| 6 | `kc_typst_patterns.md` | Typst | ~5.0K | 9 | Document structure, functions, data loading, templates, tables |
| 7 | `kc_pandoc_pipeline.md` | Pandoc | ~4.8K | 8 | Multi-format pipeline (PDF/EPUB/DOCX/HTML), cross-refs, Lua filters |
| 8 | `kc_youtube_api.md` | YouTube Data API | ~5.0K | 8 | OAuth, resumable upload, metadata, thumbnails, playlists, quota |
| 9 | `kc_ayrshare_api.md` | Ayrshare | ~4.9K | 8 | Multi-platform posting, scheduling, platform-specific content, analytics |
| 10 | `kc_notebooklm_integration.md` | NotebookLM | ~4.8K | 8 | Audio/Video Overview, Study Guide, Quiz, MCP tools, feeding strategy |

## Coverage Matrix

```
Content Factory Pipeline Stage → KC Coverage

DESIGN:     Canva Connect API ✅
NARRATION:  ElevenLabs TTS ✅
VIDEO GEN:  Runway Gen-4 API ✅
PROCESSING: FFmpeg Patterns ✅
SLIDES:     Marp CLI ✅
EBOOKS:     Typst Patterns ✅ + Pandoc Pipeline ✅
PUBLISH:    YouTube Data API ✅ + Ayrshare Social API ✅
TRANSFORM:  NotebookLM Integration ✅
```

## Cross-References Between KCs

All KCs reference each other where relevant:
- **Runway → FFmpeg → ElevenLabs**: silent video + narration + mixing
- **Canva → Ayrshare/YouTube**: design → publish
- **Pandoc ↔ Typst ↔ Marp**: document format alternatives
- **NotebookLM → ElevenLabs/YouTube/Pandoc**: content transformation pipeline

## Quality Notes

- Each KC follows standard frontmatter (id, kind, type, pillar, tags, tldr, when_to_use, keywords, feeds_kinds, linked_artifacts)
- All include Quick Reference YAML block with auth, endpoints, rate limits
- All include real, functional code examples (Python httpx or CLI commands)
- All include Gotchas section with real-world pitfalls
- All include cost estimates where applicable
- All include links to official documentation
- `quality: null` — peer review assigns score (rule 4)

## What's NOT Covered (out of scope)

- Stripe/payment processing (N06 domain)
- Email marketing (Mailchimp/ConvertKit) — not in handoff
- Analytics dashboards (Grafana/Metabase) — N05 domain
- Storage backends (S3/R2/Supabase) — infrastructure, not content

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_content_factory]] | downstream | 0.29 |
| [[spec_content_factory_v1]] | downstream | 0.28 |
| [[wf_kc_to_content]] | downstream | 0.27 |
| [[p12_wf_cf_publish_youtube]] | downstream | 0.26 |
| [[output_content_factory_internal_audit]] | related | 0.25 |
| [[output_content_factory_landscape]] | related | 0.23 |
| [[p01_kc_notebooklm_integration]] | related | 0.22 |
| [[p05_fmt_content_adapter]] | downstream | 0.22 |
| [[p03_sp_social_publisher_builder]] | downstream | 0.22 |
| [[p05_out_cf_actions_and_distribution]] | downstream | 0.21 |
