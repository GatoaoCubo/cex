# Mission: MONETIZE_CEX — N04 Knowledge Perspective
**Nucleus**: N04 Knowledge | **Model**: gemini/2.5-pro | **Priority**: HIGH
**Output**: `N04_knowledge/output/output_monetization_curriculum.md`
**Signal on complete**: `python _tools/signal_writer.py n04 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto (10-15min) + texto detalhado + exercícios práticos no CEX |
| Currículo | 3 tracks: Foundations (free, M01-M03) → Builder (pago, M04-M10) → Master (premium, M11-M14) |
| Pricing | Explorer R$0 / Builder R$497 / Master R$997 |

## O CEX em números (pra dimensionar o conteúdo)

- 114 kinds, 107 builders, 12 pillars, 8 nuclei (N00-N07)
- Pipeline 8F (F1-Intake → F8-Publish)
- GDP (Guided Decision Protocol) — user decide WHAT, LLM decide HOW
- Tools: cex_run.py, cex_evolve.py, cex_8f_motor.py, cex_crew_runner.py, etc.
- Overnight flywheel (overnight.ps1) — bootstrap → evolve → cycle → farm
- spawn_grid.ps1 — 6 nuclei simultâneos em grid de janelas
- nucleus_models.yaml — config de modelos por núcleo (Claude/Gemini/Codex/Ollama)

## SUA MISSÃO (N04 — Knowledge)

Produza um **design instrucional detalhado** do currículo cobrindo:

### 1. Análise de pré-requisitos
- O que o aluno precisa saber ANTES (Python? Git? CLI? LLM basics?)
- Persona primária: quem é o aluno ideal? (dev jr? sr? AI engineer? creator?)
- Persona secundária: quem poderia comprar mas precisa de mais suporte?

### 2. Learning objectives por módulo
Para cada um dos 14 módulos, defina:
- **Objetivo**: o que o aluno será capaz de fazer ao final
- **Conceitos-chave**: 3-5 conceitos que o módulo ensina
- **Output prático**: o artefato que o aluno produz (checkpoint)
- **Duração estimada**: minutos de vídeo + tempo de exercício
- **Dependências**: quais módulos são pré-requisito

### Track 1: Foundations (free)
| M01 | O que é CEX — filosofia typed knowledge |
| M02 | Instalação + `/init` (bootstrap brand) |
| M03 | Primeiro artefato: `/build` |

### Track 2: Builder (pago R$497)
| M04 | 8F Pipeline deep-dive |
| M05 | Nuclei: o que cada um faz |
| M06 | Configurando modelos (nucleus_models.yaml) |
| M07 | `/guide` + GDP — co-pilot decisions |
| M08 | `/grid` — spawn multi-nucleus |
| M09 | AutoResearch + overnight flywheel |
| M10 | Criando builders custom |

### Track 3: Master (premium R$997)
| M11 | Fine-tuning cex-brain (QLoRA + Ollama) |
| M12 | Deploy: Supabase + RAG + API |
| M13 | Criando kinds novos |
| M14 | CEX pra equipes / agências |

### 3. Estrutura didática de cada módulo
- Template padrão (intro → conceito → demo → exercício → checkpoint)
- Como cada módulo conecta com o anterior (narrative arc)
- Quais módulos podem ser feitos fora de ordem

### 4. Assessment strategy
- Como verificar que o aluno aprendeu? (quiz? output do CEX? peer review?)
- Gamificação: badges, progress bar, "Builder Certified"?
- Community checkpoints: alunos compartilham outputs no Discord?

### 5. Mapa de conteúdo → artefatos CEX existentes
- Quais artefatos do repo já servem como material de referência?
- O que precisa ser CRIADO especificamente pro curso? (novos KCs, examples, tutorials?)
- Gap analysis: conteúdo que falta no repo pra o curso funcionar

### 6. Escalabilidade do currículo
- Como adicionar módulos futuros sem quebrar a estrutura?
- Módulos bônus possíveis (MCP integration, Supabase advanced, etc.)

## Formato do output

```yaml
---
id: n04_output_monetization_curriculum
kind: output_template
pillar: P05
domain: knowledge
quality: null
tags: [monetization, curriculum, learning-design, modules, assessment]
---
```

Use tabelas pra o mapa de módulos. Texto conciso. Markdown estruturado.

## Ao finalizar

1. Salve em `N04_knowledge/output/output_monetization_curriculum.md`
2. `git add N04_knowledge/ && git commit -m "[N04] Monetization curriculum design"`
3. `python _tools/signal_writer.py n04 MONETIZE_CEX_COMPLETE 9.0`
