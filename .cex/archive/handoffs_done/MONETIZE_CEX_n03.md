# Mission: MONETIZE_CEX — N03 Engineering Perspective
**Nucleus**: N03 Engineering | **Model**: claude/opus-4 | **Priority**: HIGH
**Output**: `N03_engineering/output/output_monetization_architecture.md`
**Signal on complete**: `python _tools/signal_writer.py n03 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto + texto + exercícios práticos |
| Currículo | 3 tracks: Foundations(free) → Builder(R$497) → Master(R$997) |
| Plataforma | Lemon Squeezy (license keys, 5% fee) |
| Modelo FT | cex-brain:14b (GGUF) = download exclusivo tier pago via license key |

## SUA MISSÃO (N03 — Engineering)

Produza uma **arquitetura técnica do produto** cobrindo:

### 1. Preparação do repo para público
- O que precisa ser limpo/removido antes de tornar MIT? (secrets, paths hardcoded, dados pessoais)
- `.gitignore` review — o que NÃO vai pro repo público
- README.md público vs o CLAUDE.md interno
- Onboarding: o que acontece quando alguém clona e roda pela primeira vez?
- `cex_setup.py` ou `setup.sh` — installer automático (Python deps, Ollama pull, etc.)

### 2. Arquitetura de distribuição do cex-brain
- Como gerar o GGUF (pipeline: export data → train QLoRA → merge → quantize → GGUF)
- Onde hospedar (HuggingFace Hub, Ollama registry, S3+CloudFront)
- License key verification: como o download verifica que o user pagou?
  - Opção A: Lemon Squeezy webhook → gera link temporário
  - Opção B: License key no Modelfile header → API verifica na primeira run
  - Opção C: Gated repo no HuggingFace (manual approval)
- Tamanho estimado do GGUF (14B Q5_K_M ≈ 10GB) — viável pra download?

### 3. Plataforma do curso
- Opções técnicas: Lemon Squeezy + GitHub private repo? Lemon Squeezy + conteúdo externo?
- Como entregar vídeo (YouTube unlisted? Vimeo OTT? Self-hosted?)
- Como entregar texto (GitHub wiki? Notion? Custom site com Astro/Next?)
- Exercícios: como verificar que o aluno completou? (checkpoint files no CEX dele?)

### 4. CI/CD para o produto
- Repo público: pre-commit hooks, GitHub Actions (lint, test, doctor)
- Versioning: como taggear releases que o curso referencia
- Curso: como atualizar módulos sem quebrar referências

### 5. Segurança e compliance
- MIT license: o que permite e o que não protege
- Dados do user no `/init` — LGPD/GDPR se armazenados na plataforma
- Modelo FT: licença do base model (Qwen3 é Apache 2.0 — OK pra venda?)

### 6. Esforço estimado
- Tabela de tasks com estimativa de horas pra cada componente
- O que pode ser automatizado vs manual
- MVP: o que é mínimo pra lançar o primeiro tier (Builder)?

## Formato do output

```yaml
---
id: n03_output_monetization_architecture
kind: output_template
pillar: P05
domain: engineering
quality: null
tags: [monetization, architecture, distribution, ci-cd, security]
---
```

Diagramas em ASCII/mermaid. Tabelas pra estimativas. Código de exemplo pra scripts críticos.

## Ao finalizar

1. Salve em `N03_engineering/output/output_monetization_architecture.md`
2. `git add N03_engineering/ && git commit -m "[N03] Monetization technical architecture"`
3. `python _tools/signal_writer.py n03 MONETIZE_CEX_COMPLETE 9.0`
