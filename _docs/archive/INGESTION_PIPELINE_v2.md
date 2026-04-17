# CEX Ingestion Pipeline v2 — Dual Output

**Version**: 2.0.0 | **Supersedes**: INGESTION_PIPELINE.md

## Core Principle

**Specialist drops file → System processes → Output goes to BOTH repo AND Drive.**
The specialist never touches Git. They see results in their own Drive folder.

## Architecture

```
SPECIALIST (Google Drive)              SYSTEM (CEX Instance)
─────────────────────────             ──────────────────────

📁 joao/                              records/inbox/raw/
  frameworks.pdf          ──sync──→     gdrive_joao_frameworks.pdf
                                            │
                                       TRIAGE (auto-classify)
                                            │
                                       DISTILL (agent_group)
                                            │
                                       QUALITY GATE
                                       ├── >= 7.0 APPROVED
                                       │   ├→ records/pool/knowledge/KC_COPY_001.md
                                       │   └→ Drive: joao/_processados/frameworks_RESULTADO.md
                                       └── < 7.0 REJECTED
                                           └→ Drive: joao/_rejeitados/frameworks_FEEDBACK.md
```

## Drive Structure (Per Person, Not Per Domain)

```
organization Conhecimento/
  joao_copywriter/             ← Joao drops ANYTHING here
    _processados/              ← System returns approved results
    _rejeitados/               ← System returns rejected with feedback
  maria_amazon/                ← Maria drops ANYTHING here
    _processados/
    _rejeitados/
  pedro_fotografo/             ← Pedro drops ANYTHING here
    _processados/
    _rejeitados/
  _por_dominio/                ← Optional: domain-specific drops
    marketing/
    pesquisa/
    ecommerce/
  _templates/                  ← Templates for specialists
```

## Resultado File Format (uploaded back to Drive)

```markdown
# Resultado: {original_filename}

## Status: APROVADO ✅ | Score: 8.5/10

## O que foi extraido
- 3 frameworks de copywriting identificados
- 12 regras de persuasao catalogadas
- 5 templates de titulo gerados

## Artefato gerado
- **ID**: KC_COPY_FRAMEWORKS_001
- **Tipo**: Knowledge Card (P01)
- **Dominio**: Marketing (marketing_agent)
- **Qualidade**: 8.5/10

## Feedback
Otimo conteudo! O framework StoryBrand foi especialmente
util. Para proxima contribuicao, considere:
- Incluir exemplos reais de aplicacao
- Adicionar metricas de conversao quando disponivel

## Proximo passo
Nenhuma acao necessaria. Artefato ja integrado ao sistema.

---
*Processado em 2026-03-23 por knowledge_agent | Pipeline CEX v2.0*
```

## Rejection File Format

```markdown
# Feedback: {original_filename}

## Status: NECESSITA REVISAO ⚠️ | Score: 4.2/10

## Problema identificado
O conteudo esta muito generico e sem estrutura clara.
Nao foi possivel extrair artefatos com qualidade >= 7.0.

## Sugestoes para melhorar
1. Organize em topicos claros (problema → solucao → resultado)
2. Inclua dados ou exemplos concretos
3. Separe conceitos diferentes em arquivos diferentes
4. Use o template disponivel em _templates/

## O que fazer
- Revise o arquivo original
- Aplique as sugestoes acima
- Jogue novamente na pasta (sem o prefixo _FEEDBACK)
- Sera reprocessado automaticamente

---
*Feedback gerado em 2026-03-23 por knowledge_agent | Pipeline CEX v2.0*
```

## Triage Rules

System auto-classifies based on content analysis, NOT folder location:

| Content Detected | Agent_group | Pool Destination |
|-----------------|-----------|-----------------|
| Copy, titulos, persuasao | marketing_agent | pool/knowledge/ or pool/marketing/ |
| Dados, planilhas, metricas | commercial_agent | pool/data/ |
| Concorrentes, mercado, trends | research_agent | pool/research/ |
| Codigo, API, arquitetura | builder_agent | pool/specs/ |
| Frameworks, metodologias | knowledge_agent | pool/knowledge/ |
| Fotos, visual, design | marketing_agent | pool/marketing/ |

Specialist does NOT need to choose. Just drop and forget.

## Dual Output Contract

Every processed file MUST produce:

1. **Pool artifact** (Git commit) — for the system
2. **Resultado/Feedback file** (Drive upload) — for the specialist
3. **Move original** to `_processados/` or `_rejeitados/` in Drive

No silent processing. Specialist ALWAYS gets feedback.
