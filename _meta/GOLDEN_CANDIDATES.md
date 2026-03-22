# Golden Candidates — CEX Migration List
# Generated: 2026-03-22 | Source: codexa-core (9916 MD files)
# Criteria: quality >= 9.0, size 1KB-8KB, structured content
# Format: path | tipo CEX | estimated quality | razao

## P01 Knowledge Cards

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/pool/knowledge/KC_ATLAS_005_ZERO_TOUCH_EXECUTION_PATTERNS.md | P01 meta_kc | 9.0 | quality_score=9.0, TAC-8 architecture, retry patterns, real YAML configs |
| records/pool/knowledge/KC_ATLAS_006_PRE_DEPLOY_VALIDATION_CHECKLIST.md | P01 meta_kc | 8.5 | checklist estruturado, pre-deploy patterns, ATLAS domain |
| records/pool/knowledge/KC_ATLAS_007_CI_CD_PIPELINE_ARCHITECTURE.md | P01 meta_kc | 8.5 | pipeline architecture, CI/CD patterns, densidade estimada alta |
| records/pool/knowledge/KC_ATLAS_009_TEST_AUTOMATION_STRATEGY.md | P01 meta_kc | 8.5 | test strategy patterns, automation gates |
| records/pool/knowledge/KC_ATLAS_010_QUALITY_GATE_IMPLEMENTATION.md | P01 meta_kc | 9.0 | quality gate patterns, 5D framework, mensuravel |
| records/pool/knowledge/KC_ATLAS_012_CLAUDE_OBSERVABILITY_EVALUATION.md | P01 meta_kc | 8.5 | LLM observability, evaluation patterns |
| records/pool/knowledge/KC_ATLAS_013_CLAUDE_COMPUTER_USE_ARCHITECTURE.md | P01 meta_kc | 8.5 | computer use arch, tool use patterns |
| records/pool/knowledge/KC_EDISON_025_CLAUDE_CODING_SKILLS_PATTERNS.md | P01 meta_kc | 9.0 | coding patterns golden, EDISON distill source |
| records/pool/knowledge/KC_EDISON_029_CLAUDE_AGENT_ORCHESTRATION_QUICKSTART.md | P01 meta_kc | 9.0 | orchestration quickstart, agent patterns |
| records/pool/knowledge/KC_PYTHA_069_CAT_LOGO_PR_PRIO_MERCADO_LIVRE.md | P01 domain_kc | 10.0 | MIGRADO: p01_kc_catalogo_proprio_mercado_livre.md |

## P02 Agents

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/agents/catalogo_ml_strategy/README.md | P02 agent | 9.0 | 5 modulos, ASCII arch, inputs/outputs YAML, metricas de sucesso, regras de ouro |
| records/agents/amazon-ads-agent/README.md | P02 agent | 8.5 | YORK satellite, ML Ads, structured when_to_use, integration map |
| records/agents/amazon-analytics-agent/README.md | P02 agent | 8.5 | analytics domain, YORK, capabilities bem definidas |
| records/agents/amazon-listing-agent/README.md | P02 agent | 8.5 | listing creation, YORK, full workflow |
| records/agents/amazon-strategy-agent/README.md | P02 agent | 8.5 | strategy domain, market analysis |
| records/agents/gateway/README.md | P02 agent | 9.0 | API gateway pattern, routing, auth |

## P04 Skills

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/skills/ml-ads/SKILL.md | P04 skill | 9.5 | MIGRADO: p04_skill_ml_ads.md — modulos, YAML I/O, funnel table, quality gates reais |
| records/skills/amazon-ads-agent/SKILL.md | P04 skill | 8.5 | ML Ads YORK, estrutura completa |
| records/skills/amazon-listing-agent/SKILL.md | P04 skill | 8.5 | listing creation workflow |
| records/skills/amazon-analytics-agent/SKILL.md | P04 skill | 8.5 | analytics patterns |
| records/skills/design-extractor/SKILL.md | P04 skill | 8.0 | design extraction, structured |
| records/skills/voice_pipeline/SKILL.md | P04 skill | 8.5 | voice pipeline patterns |

## P08 Architecture

| Path | Tipo CEX | Est. Quality | Razao |
|------|----------|-------------|-------|
| records/pool/audits/2026-02-28-meta-evolution/LLM_ARCHITECTURE_REVIEW.md | P08 architecture | 9.0 | arquitetura LLM completa, tech decisions documentadas |

## Priority Migration Queue

1. KC_ATLAS_010 (quality gates — universal pattern)
2. KC_EDISON_029 (agent orchestration — core CODEXA pattern)
3. catalogo_ml_strategy/README.md (domain agent — P02 example)
4. amazon-ads-agent/SKILL.md (YORK domain skill)
5. KC_ATLAS_007 (CI/CD patterns — deploy domain)

---
*Search method: find size +1k -5k (KCs), find size +2k -8k (agents/skills), grep quality 9.x*
*Total candidates: 22 | Migrated: 2 (ml-ads skill, zero-touch KC)*
*Next: run /evolve to auto-migrate top 5*
