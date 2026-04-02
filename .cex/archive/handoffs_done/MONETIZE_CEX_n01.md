# Mission: MONETIZE_CEX — N01 Research Perspective
**Nucleus**: N01 Intelligence | **Model**: gemini/2.5-pro | **Priority**: HIGH
**Output**: `N01_intelligence/output/output_monetization_research.md`
**Signal on complete**: `python _tools/signal_writer.py n01 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto (10-15min) + texto detalhado + exercícios práticos no CEX |
| Currículo | 3 tracks: Foundations (free, M01-M03) → Builder (pago, M04-M10) → Master (premium, M11-M14) |
| Pricing | Explorer R$0 / Builder R$497 / Master R$997. 12x sem juros, PIX -10% |
| Plataforma | Lemon Squeezy (5% fee, license keys, internacional) |
| Modelo FT | cex-brain:14b (GGUF via Ollama) = download exclusivo pra tier pago. Free users usam qwen3 genérico (quality ~7.0 vs ~9.0 com cex-brain) |

## O CEX em números

- 114 kinds, 107 builders, 12 pillars, 8 nuclei
- 7 CLIs integrados (claude, gemini, codex, pi, ollama)
- Pipeline 8F automatizado
- AutoResearch (cex_evolve.py) com 5172 iterações, 616 keeps
- Overnight flywheel autônomo
- ~456 artefatos .md no sistema

## SUA MISSÃO (N01 — Research)

Produza um **relatório de pesquisa de mercado** cobrindo:

### 1. Landscape competitivo
- Quem vende cursos de multi-agent systems? (CrewAI, AutoGen, LangChain Academy, etc.)
- Quem vende "knowledge systems"? (Notion courses, Obsidian courses, PKM courses)
- Quem vende cursos de prompt engineering avançado?
- Preços praticados (USD e BRL), formatos, plataformas usadas

### 2. Tamanho do mercado
- TAM: desenvolvedores interessados em AI agents
- SAM: devs que pagam por cursos de AI tools
- SOM: devs BR + PT que pagariam por curso em português
- Dados de plataformas: Hotmart/Kiwify categorias tech, Udemy AI courses

### 3. Análise de pricing
- Benchmark de cursos similares (preço médio, tiers, conversão estimada)
- O R$497 / R$997 está no range certo?
- Existe espaço pra tier Enterprise (R$2997)?

### 4. Tendências
- AI agent frameworks: crescimento, adoção, curva
- "Vibe coding" / "AI-assisted development" trend
- Demanda por fine-tuning local (Ollama, llama.cpp growth)

### 5. Riscos e gaps
- O que pode dar errado? (mercado satura, open-source commoditiza, etc.)
- O que nenhum concorrente oferece que CEX oferece? (moat analysis)

## Formato do output

```yaml
---
id: n01_output_monetization_research
kind: output_template
pillar: P05
domain: research
quality: null
tags: [monetization, research, market, competition, pricing]
---
```

Markdown estruturado com tabelas, dados concretos, fontes quando possível.
Não inventar números — se não souber, diga "estimativa" ou "dados indisponíveis".

## Ao finalizar

1. Salve em `N01_intelligence/output/output_monetization_research.md`
2. `git add N01_intelligence/ && git commit -m "[N01] Monetization market research"`
3. `python _tools/signal_writer.py n01 MONETIZE_CEX_COMPLETE 9.0`
