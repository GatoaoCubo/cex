---
kind: tools
id: bld_tools_safety_policy
pillar: P04
llm_function: CALL
purpose: Tools available for safety_policy production
quality: 9.1
title: "Tools Safety Policy"
version: "1.1.0"
author: n06_hybrid_review
tags: [safety_policy, builder, tools, perspective_api, openai_moderation, aws_comprehend, nist_ai_rmf]
tldr: "Real tools for safety_policy production: Perspective API, OpenAI Moderation API, AWS Comprehend, Azure Content Moderator, PhotoDNA (CSAM), IBM OpenPages."
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.92
---

## CEX Internal Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compiles safety_policy .md to .yaml; validates frontmatter | After every edit |
| cex_score.py --apply | Scores policy against 5D rubric (quality gate) | Before commit |
| cex_retriever.py | Finds related safety policies and guardrail artifacts | During composition |
| cex_doctor.py | Detects conflicts between overlapping safety policies | Policy updates |
| cex_hooks.py pre-commit | Validates ASCII-only, schema compliance before git commit | Automated |

## External Classification APIs (real, production-grade)
| Tool | Provider | Endpoint | Categories | Cost |
|------|----------|----------|------------|------|
| Perspective API | Google/Jigsaw | commentanalyzer.googleapis.com | TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT, SEXUALLY_EXPLICIT | Free (quota) |
| OpenAI Moderation API | OpenAI | api.openai.com/v1/moderations | hate, harassment, self-harm, sexual, sexual/minors, violence | Free with API key |
| Azure Content Moderator | Microsoft | api.cognitive.microsoft.com | Image, text, PII detection | $1/1K calls |
| AWS Comprehend | AWS | comprehend.amazonaws.com | HATE_SPEECH, HARASSMENT, SEXUAL, VIOLENCE | $0.0001/unit |
| AWS Rekognition | AWS | rekognition.amazonaws.com | Image/video content moderation (NSFW, violence, alcohol) | $0.001/image |

## CSAM Detection (mandatory for any image/video platform)
| Tool | Provider | Method | Reporting |
|------|----------|--------|-----------|
| PhotoDNA | Microsoft | Hash matching vs NCMEC database | Automated NCMEC CyberTipline report |
| Google CSAI Match | Google | Hash matching vs IWF/NCMEC | Automated report |
| NCMEC CyberTipline API | NCMEC | Mandatory report filing | 18 U.S.C. 2258A compliance |

## Compliance Documentation Tools
| Tool | Purpose | Framework |
|------|---------|-----------|
| IBM OpenPages | GRC (Governance, Risk, Compliance) policy management | EU AI Act, ISO 27001 |
| OneTrust AI Governance | AI policy lifecycle: draft -> review -> approve -> monitor | NIST AI RMF, EU AI Act |
| NIST AI RMF Playbook | Policy structure template for GOVERN function | NIST AI RMF (2023) |
| EU AI Act Compliance Checker | Automated check of AI system against high-risk criteria | EU AI Act |

## Red-Teaming Tools (policy validation)
| Tool | Purpose | Source |
|------|---------|--------|
| Garak | LLM vulnerability scanner: probes for safety policy gaps | NVIDIA Research, garak.ai |
| PyRIT | Python Risk Identification Toolkit for generative AI | Microsoft, github.com/azure/pyrit |
| PromptBench | Adversarial prompt robustness evaluation | ACL 2024 |

## Retired / Do Not Use
| Tool | Why removed |
|------|-------------|
| SafetyChain | Does not exist (fictional) |
| PolicyForge | Does not exist (fictional) |
| RiskAssess | Does not exist (fictional) |
