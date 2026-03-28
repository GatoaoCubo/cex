# UPLOAD KIT | anuncio_agent v5.0.0

**Package**: iso_package | **Version**: 5.0.0 | **Date**: 2025-12-18

---

## ARQUITETURA DE DEPLOY

```
+-------------------------------------------------------------+
|                    OPENAI ASSISTANT                         |
+-------------------------------------------------------------+
|  INSTRUCTIONS (campo do assistant)                          |
|  +-- system_instruction.md (COPIAR/COLAR conteudo)          |
+-------------------------------------------------------------+
|  FILE SEARCH (vector store)                                 |
|  +-- All files in this package                              |
|      Chunk: 800 | Overlap: 200                              |
+-------------------------------------------------------------+
|  CODE INTERPRETER                                           |
|  +-- validator.py (upload separado)                         |
+-------------------------------------------------------------+
```

---

## VECTOR STORE SETTINGS

```yaml
chunking_strategy:
  type: static
  max_chunk_size_tokens: 800
  chunk_overlap_tokens: 200
```

---

## FILE INVENTORY

### Core
| File | Upload |
|------|--------|
| quick_start.md | YES |
| prime.md | YES |
| instructions.md | YES |
| architecture.md | YES |
| output_template.md | YES |
| system_instruction.md | YES (as Instructions field) |

### Config
| File | Upload |
|------|--------|
| data/input_schema.yaml | YES |
| data/copy_rules.yaml | YES |
| data/marketplace_specs.yaml | YES |
| data/persuasion_patterns.yaml | YES |
| data/execution_plans.yaml | YES |
| data/quality_dimensions.yaml | YES |

### Execution HOPs
| File | Upload |
|------|--------|
| prompts/orchestrator.md | YES |
| prompts/main_agent.md | YES |
| prompts/titulo_generator.md | YES |
| prompts/keywords_expander.md | YES |
| prompts/bullet_points.md | YES |
| prompts/descricao_builder.md | YES |
| prompts/qa_validation.md | YES |
| prompts/frameworks.md | YES |
| prompts/ads_enrichment.md | YES |

---

## CODE INTERPRETER (Separate Upload)

| File | Upload To |
|------|-----------|
| validator.py | Code Interpreter (NAO vai no vector store) |

---

## SYSTEM INSTRUCTION (Copiar/Colar)

**IMPORTANTE**: NAO fazer upload deste arquivo. Copiar o CONTEUDO e colar no campo "Instructions" do Assistant.

**Arquivo**: `system_instruction.md`

**Como fazer**:
1. Abrir `system_instruction.md`
2. Selecionar TODO o conteudo (Ctrl+A)
3. Copiar (Ctrl+C)
4. Ir no OpenAI Playground > Assistants > seu assistant
5. Colar no campo "Instructions" (Ctrl+V)
6. Salvar

---

## DEPLOY CHECKLIST

```
VECTOR STORE
[ ] 1. Criar novo Vector Store (ou usar existente)
[ ] 2. Configurar: chunk=800, overlap=200
[ ] 3. Upload todos os arquivos listados
[ ] 4. Aguardar indexacao completa

CODE INTERPRETER
[ ] 5. Upload validator.py ao Code Interpreter

SYSTEM INSTRUCTION
[ ] 6. Abrir system_instruction.md
[ ] 7. Copiar TODO conteudo
[ ] 8. Colar no campo "Instructions" do Assistant

TOOLS
[ ] 9. Habilitar: File Search
[ ] 10. Habilitar: Code Interpreter
[ ] 11. Conectar Vector Store ao File Search

SAVE & TEST
[ ] 12. Salvar Assistant
[ ] 13. Testar com produto exemplo
[ ] 14. Verificar output (titulos, keywords, bullets, descricao)
[ ] 15. Rodar validator.py (score >= 0.90)
```

---

## TEST INPUT

```
Produto: Whey Protein Isolado 1kg
Categoria: Suplementos > Proteinas
Head Terms: whey, proteina, suplemento, hipertrofia
Price: R$ 149 - R$ 199
```

---

## EXPECTED OUTPUT

Output deve ser:
- Widget format com separadores ====
- ZERO emojis
- ZERO metadados (chars, scores)
- Texto PURO copy-ready
- Titulos 58-60 chars
- Keywords 2 blocos x 115-120 termos
- 10 Bullets 250-299 chars cada
- Descricao >= 3300 chars (StoryBrand)

---

## TROUBLESHOOTING

| Problema | Solucao |
|----------|---------|
| Output com emojis | Verificar se system_instruction.md foi copiado corretamente |
| Output incompleto | Verificar se File Search esta habilitado e conectado |
| Validacao falha | Verificar se validator.py foi uploadado ao Code Interpreter |
| Titulos longos | Agent deve corrigir automaticamente, se nao corrigir, re-copiar system_instruction |

---

**Upload Kit Version**: 5.0.0
**Status**: DEPLOY READY
**Date**: 2025-12-18
