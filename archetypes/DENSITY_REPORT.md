# Density Report — CEX Examples
## Wave 5 | 2026-03-22 | 18 examples analisados

---

## Definicao de Tiers

| Tier | Score | Criterio |
|------|-------|----------|
| Elite | 0.90-1.00 | Tabelas dominantes, YAML I/O, ASCII diagrams, zero prosa |
| High | 0.80-0.89 | Estrutura solida, bullets majoritarios, prosa minima |
| Standard | 0.70-0.78 | Mix prosa/estrutura, revisao recomendada |
| Low | <0.65 | Prosa dominante — rejeitar ou refazer |

---

## Analise por Arquivo

| File | Tokens(est) | Density | Tier | Notes |
|------|-------------|---------|------|-------|
| p03_pt_action_prompt | ~320 | 0.95 | Elite | Acao-por-bullet, formato ultra-denso |
| p01_kc_catalogo_proprio_mercado_livre | ~361 | 0.92 | Elite | Taxonomy tables, compacto, domain mastery |
| p03_pt_satellite_orchestrator | ~718 | 0.91 | Elite | Routing tables + dispatch protocol |
| p04_skill_ml_ads | ~770 | 0.91 | Elite | Funnel table + YAML I/O + metrics gates |
| p01_kc_agent_orchestration_quickstart | ~762 | 0.90 | Elite | Multi-agent mapping + ASCII flow |
| p03_pt_catalogo_ml_strategy | ~875 | 0.90 | Elite | Modulos ricos, maior example do repo |
| p01_kc_zero_touch_execution | ~729 | 0.89 | High | Borderline Elite — execution patterns |
| p03_pt_sdk_agent_builder | ~746 | 0.89 | High | Borderline Elite — SDK build patterns |
| p01_kc_quality_gate_implementation | ~824 | 0.88 | High | Gate tables detalhadas (Draft/Pool/Golden) |
| p01_kc_test_chain_validation | ~447 | 0.88 | High | Compacto e bem estruturado |
| p02_agent_catalogo_ml_strategy | ~790 | 0.88 | High | 5 modulos, rich tables |
| p02_agent_pesquisa | ~286 | 0.88 | High | Menor agent, alta densidade relativa |
| p01_kc_cicd_pipeline_architecture | ~795 | 0.87 | High | Pipeline tables, alguma prosa no summary |
| p02_agent_gateway | ~805 | 0.87 | High | ASCII arch diagram + intent routing table |
| p02_agent_amazon_ads | ~806 | 0.86 | High | Capabilities table, full agent spec |
| p04_skill_design_extractor | ~690 | 0.86 | High | Workflow phases, structured output |
| p01_kc_claude_coding_skills | ~758 | 0.85 | High | Bullets forte, alguma prosa em Application |
| p04_skill_voice_pipeline | ~716 | 0.85 | High | Fases claras, YAML I/O presente |

---

## Resumo

| Tier | Count | % do Total |
|------|-------|------------|
| Elite (>=0.90) | 6 | 33% |
| High (0.80-0.89) | 12 | 67% |
| Standard (0.70-0.78) | 0 | 0% |
| Low (<0.65) | 0 | 0% |
| **Total** | **18** | **100%** |

**Density media**: 0.886 (88.6%)
**Menor**: 0.85 (p01_kc_claude_coding_skills, p04_skill_voice_pipeline)
**Maior**: 0.95 (p03_pt_action_prompt)

---

## Padroes Identificados

### O que eleva para Elite
- Tabelas com 3+ colunas dominando a estrutura
- YAML I/O block explicito (input/output schema)
- ASCII art diagram (arquitetura visual)
- Formato acao-por-bullet (verbo:objeto pattern)
- Multiplas spec tables (cada secao tem tabela propria)

### O que mantém em High (0.85-0.89)
- Boa estrutura, mas Executive Summary com 3-4 linhas de prosa
- Secao Application/Purpose com paragrafos ao invez de bullets
- Referencias textuais ao invez de tabela de cross-references

### Acoes de Upgrade (High → Elite)
1. Converter Executive Summary em bullets (1 linha cada)
2. Trocar paragrafos de Application por tabela "Quando usar / O que fazer"
3. Adicionar YAML I/O explicito (mesmo que sumario)
4. Adicionar density_score realista no frontmatter

---

## Top 3 Golden Candidates (por density + quality)

| Rank | File | Score | Density | Razao |
|------|------|-------|---------|-------|
| 1 | p03_pt_action_prompt | 9.0 | 0.95 | Formato perfeito, acao-por-bullet |
| 2 | p04_skill_ml_ads | 9.5 | 0.91 | YAML I/O + funnel table + quality gates |
| 3 | p01_kc_catalogo_proprio_mercado_livre | 9.5 | 0.92 | Domain mastery, taxonomy compacta |

---
*Metodo: word_count x 1.3 = token estimate | density_score do YAML frontmatter | 18/18 examples analisados*
