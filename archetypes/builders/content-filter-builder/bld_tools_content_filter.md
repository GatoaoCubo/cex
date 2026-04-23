---
kind: tools
id: bld_tools_content_filter
pillar: P04
llm_function: CALL
purpose: Tools available for content_filter production
quality: 9.0
title: "Tools Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, tools]
tldr: "Tools available for content_filter production"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_tools_safety_policy
  - bld_knowledge_card_content_filter
  - content-filter-builder
  - n06_audit_content_filter_builder
  - kc_guardrail
  - bld_instruction_content_filter
  - bld_output_template_content_filter
  - bld_collaboration_content_filter
  - kc_content_filter
  - p03_sp_content_filter_builder
---

## Production Tools

This ISO defines a content filter -- the moderation rules that gate output or input.
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles content into standardized format | Pre-processing |
| cex_score.py | Assigns risk scores based on policy rules | Filtering |
| cex_retriever.py | Fetches external data for context checks | Validation |
| cex_doctor.py | Diagnoses content for harmful patterns | Post-processing |
| cex_analyzer.py | Parses metadata and language features | Initial screening |
| cex_optimizer.py | Refines filters for accuracy and efficiency | Deployment |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| val_check.py | Verifies filter compliance with policies | Testing |
| val_compare.py | Cross-checks outputs against golden standards | QA |
| val_audit.py | Logs and reviews filter decisions | Auditing |

## External Classification APIs (real, production-grade)
| Tool | Provider | Use Case | Cost |
|------|----------|----------|------|
| Perspective API | Google/Jigsaw | Text toxicity scoring (8 attributes) | Free (quota) |
| OpenAI Moderation API | OpenAI | LLM input/output harm classification (11 categories) | Free with API key |
| AWS Comprehend Detect Toxic Content | AWS | Batch text toxicity detection | $0.0001/unit |
| AWS Rekognition Content Moderation | AWS | Image/video NSFW, violence, suggestive content | $0.001/image |
| Azure Content Moderator | Microsoft | Text + image moderation, PII detection | $1/1K calls |
| Google Vision SafeSearch | Google | Image: adult, spoof, medical, violence, racy | $1.50/1K images |
| PhotoDNA | Microsoft | CSAM hash matching (mandatory for image platforms) | Enterprise license |
| NCMEC CyberTipline | NCMEC | CSAM mandatory reporting API | Free (mandatory) |

## NLP Processing Libraries (real, open-source)
| Library | Purpose | When |
|---------|---------|------|
| spaCy | Tokenization, NER, linguistic features | Pre-processing stage |
| Hugging Face Transformers | Load fine-tuned toxicity classifiers (ToxicBert, HateBERT) | ML classify stage |
| Detoxify | BERT-based multilingual toxicity classifier | Text toxicity scan |
| langdetect / langid | Language detection for multilingual routing | Pre-processing |

## Retired / Do Not Use
| Tool | Why removed |
|------|-------------|
| "Content Policy Library (open-source guidelines)" | Does not exist (fictional) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_safety_policy]] | sibling | 0.44 |
| [[bld_knowledge_card_content_filter]] | upstream | 0.38 |
| [[content-filter-builder]] | downstream | 0.32 |
| [[n06_audit_content_filter_builder]] | downstream | 0.31 |
| [[kc_guardrail]] | upstream | 0.28 |
| [[bld_instruction_content_filter]] | upstream | 0.27 |
| [[bld_output_template_content_filter]] | downstream | 0.26 |
| [[bld_collaboration_content_filter]] | downstream | 0.26 |
| [[kc_content_filter]] | upstream | 0.24 |
| [[p03_sp_content_filter_builder]] | upstream | 0.23 |
