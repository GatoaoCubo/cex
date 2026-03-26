---
id: p04_skill_cex_forge
name: cex_forge
description: "Gerador universal de prompts para artefatos CEX — le schema + template + seeds e monta prompt pronto para LLM"
user_invocable: true
trigger: "Quando precisar gerar qualquer artefato CEX valido (KC, agent, skill, prompt, etc)"
phases:
  - "1. Load schema (_schema.yaml do LP target)"
  - "2. Extract type rules (constraints, frontmatter, body_structure)"
  - "3. Load template (via TYPE_TO_TEMPLATE.yaml mapping)"
  - "4. Build prompt (schema rules + template + seeds + context)"
  - "5. Validate prompt (structure, size, placeholders)"
  - "6. Output prompt (stdout ou --output file)"
when_to_use: "Criar artefatos CEX validos para qualquer LP (P01-P12) e qualquer tipo (69 tipos disponiveis)"
when_not_to_use: "Editar artefatos existentes (use Edit direto); validar artefatos prontos (use cex_validate.py)"
examples:
  - "python cex_forge.py --lp P01 --type knowledge_card --seeds 'RAG,embeddings' --context 'texto sobre RAG'"
  - "python cex_forge.py --lp P02 --type agent --seeds 'scraper,web' --context-file notes.md"
  - "python cex_forge.py --list-types --lp P04"
lp: P04
type: skill
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: edison
domain: meta-construction
quality: 9.0
tags: [forge, generation, artifact, template, schema, prompt]
---

# CEX Forge — Gerador Universal de Artefatos

## Purpose
cex_forge.py eh a ferramenta central de geracao do CEX. Transforma schema rules + templates + seed words em prompts prontos para LLM que produzem artefatos CEX validos. NAO chama LLM diretamente — gera o prompt que o LLM consome.

## Workflow Phases

### Phase 1: Load Schema
- **Input**: `--lp P01` (LP target P01-P12)
- **Action**: Le `{LP_DIR}/_schema.yaml`, extrai tipos disponiveis
- **Output**: Dict com name, description, types

### Phase 2: Extract Type Rules
- **Input**: `--type knowledge_card` (tipo do artefato)
- **Action**: Extrai constraints (max_bytes, density_min, quality_min), frontmatter (required + cex), body_structure (variantes), validation rules
- **Output**: Dict com todas as regras do tipo

### Phase 3: Load Template
- **Input**: Tipo do artefato
- **Action**: Consulta `archetypes/TYPE_TO_TEMPLATE.yaml` para mapear tipo > template path, le o template .md
- **Output**: String do template com {{MUSTACHE}} vars (ou None se GAP)

### Phase 4: Build Prompt
- **Input**: Schema + rules + template + seeds + context
- **Action**: Monta prompt estruturado com 8 secoes: header, role, schema rules, frontmatter, body structure, validation, template, seeds, context, output instructions
- **Output**: Prompt completo em Markdown (~2-8KB)

### Phase 5: Validate Prompt
- **Input**: Prompt gerado + rules
- **Action**: Checa estrutura (## headers), placeholders ({{MUSTACHE}}), frontmatter section, tamanho (< 20KB), max_bytes mencionado
- **Output**: Lista de warnings (0 = clean)

### Phase 6: Output
- **Input**: Prompt + `--output` flag
- **Action**: Salva em arquivo ou imprime em stdout
- **Output**: Prompt pronto para consumo por LLM

## Anti-Patterns
- Rodar forge sem seeds: prompt generico, artefato vago
- Seeds > 10 palavras: dilui foco, LLM perde direcao
- Context > 5KB: prompt fica muito grande, LLM trunca
- Ignorar warnings: artefato gerado pode violar schema

## Metrics
| Metrica | Valor | Nota |
|---------|-------|------|
| Tipos suportados | 69 | Todos os tipos de P01-P12 |
| Templates com cobertura | ~80% | ~20% sao GAP (sem template) |
| Prompt size medio | 3-5KB | Dentro do budget de context |
| Validation accuracy | ~95% | 5% de false positives em warnings |
| Execution time | < 1s | Pure Python, sem I/O externo |

## Usage

```bash
# Generate KC prompt
python cex_forge.py --lp P01 --type knowledge_card --seeds "RAG,embedding,search"

# Generate agent prompt with context file
python cex_forge.py --lp P02 --type agent --seeds "scraper,web" --context-file notes.md

# List available types for a LP
python cex_forge.py --list-types --lp P04
```

## Input / Output

```yaml
input:
  lp: string        # P01-P12 target LP
  type: string      # Type within LP (e.g. knowledge_card)
  seeds: string     # Comma-separated seed words (5-10 optimal)
  context: string   # Optional context text (<5KB)

output:
  prompt: string    # Complete LLM-ready prompt (2-8KB)
  warnings: list    # Validation warnings (0 = clean)
```

## Cross-References
- cex_validate (P04.cli_tool): Validates output artifacts
- brain_query (P04.mcp_server): Provides context for seeds
