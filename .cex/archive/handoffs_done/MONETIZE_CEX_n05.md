# Mission: MONETIZE_CEX — N05 Operations Perspective
**Nucleus**: N05 Operations | **Model**: codex/o3 | **Priority**: HIGH
**Output**: `N05_operations/output/output_monetization_infra.md`
**Signal on complete**: `python _tools/signal_writer.py n05 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto + texto + exercícios |
| Pricing | Explorer R$0 / Builder R$497 / Master R$997 |
| Plataforma | Lemon Squeezy (license keys, digital delivery, 5% fee) |
| Modelo FT | cex-brain:14b GGUF (~10GB) = download exclusivo tier pago |

## SUA MISSÃO (N05 — Operations)

Produza um **plano de infraestrutura e automação** cobrindo:

### 1. Repo público — DevOps prep
- GitHub Actions workflow: lint YAML frontmatter, run cex_doctor.py, test suite
- Branch strategy: `main` (stable, tagged releases) vs `dev` (WIP)
- Release automation: tag → changelog → GitHub release → notify Lemon Squeezy
- Pre-commit hooks já existem — auditar e documentar

### 2. Lemon Squeezy integration
- Webhook setup: purchase → trigger download access
- License key validation: script que verifica key antes de baixar cex-brain GGUF
- Criar `_tools/cex_license.py`: validate key → download model → install Ollama
- Customer data: o que armazenar (email, key, tier) — mínimo pra LGPD

### 3. Model distribution pipeline
- Training: script que exporta dataset → treina QLoRA → merge → quantize GGUF
- Hosting: HuggingFace Hub (gated model) ou S3+CloudFront (CDN)
- Download: `cex_license.py --activate KEY` → verifica → baixa → `ollama create`
- Versionamento: como atualizar cex-brain sem quebrar installs existentes
- Estimativa de custos: bandwidth pra GGUF de 10GB × N downloads/mês

### 4. Course delivery infra
- Vídeo: YouTube unlisted (grátis, CDN do Google) vs Vimeo Pro (~$20/mo) vs Bunny.net ($5/mo)
- Texto: GitHub private repo (alunos ganham acesso) vs Notion (fácil) vs Astro site (custom)
- Exercícios: como verificar completion? (aluno roda `cex_doctor.py --course-check`?)

### 5. Monitoring e analytics
- GitHub: stars, clones, forks (já tem API)
- Lemon Squeezy: vendas, churn, LTV (dashboard nativo)
- Curso: completion rate por módulo (como medir?)
- Alertas: rate limit hit, model download failures, webhook failures

### 6. Cost analysis
- Tabela de custos fixos vs variáveis
- Breakeven: quantos alunos pra cobrir custos?
- Cenários: 10 alunos/mês, 50 alunos/mês, 100 alunos/mês

### 7. Automações a criar

| Script | O que faz | Prioridade |
|--------|-----------|-----------|
| `cex_license.py` | Validate key + download model | P0 |
| `cex_setup.py` | First-run installer (deps, ollama, etc) | P0 |
| `cex_course_check.py` | Verify student completed module | P1 |
| GitHub Action: release | Tag → changelog → GH release | P0 |
| GitHub Action: doctor | PR → run cex_doctor.py | P1 |
| Webhook handler | Lemon Squeezy → grant access | P0 |

## Formato do output

```yaml
---
id: n05_output_monetization_infra
kind: output_template
pillar: P05
domain: operations
quality: null
tags: [monetization, infra, ci-cd, lemon-squeezy, distribution, automation]
---
```

Código de exemplo pra scripts críticos. Diagramas de fluxo. Tabelas de custos.

## Ao finalizar

1. Salve em `N05_operations/output/output_monetization_infra.md`
2. `git add N05_operations/ && git commit -m "[N05] Monetization infrastructure plan"`
3. `python _tools/signal_writer.py n05 MONETIZE_CEX_COMPLETE 9.0`
