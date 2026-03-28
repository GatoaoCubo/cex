# UPLOAD KIT | marca_agent v1.1.0

**Package**: iso_package | **Version**: 1.1.0 | **Date**: 2025-12-20
**Vector Store ID**: [TO_BE_ASSIGNED]
**Workflow ID**: [TO_BE_ASSIGNED]

---

## ARQUITETURA DE DEPLOY

```
+-------------------------------------------------------------+
|                    TARGET PLATFORMS                          |
+-------------------------------------------------------------+
|  OPENAI ASSISTANTS                                          |
|  +-- INSTRUCTIONS (campo do assistant)                      |
|      +-- system_instruction.md (COPIAR/COLAR conteudo)      |
+-------------------------------------------------------------+
|  FILE SEARCH (vector store)                                 |
|  +-- 8 arquivos (core MDs + system_instruction.md)          |
|      Chunk: 800 | Overlap: 200                              |
+-------------------------------------------------------------+
|  CLAUDE PROJECTS                                            |
|  +-- Project Knowledge: Upload 8 arquivos                   |
|  +-- Custom Instructions: system_instruction.md             |
+-------------------------------------------------------------+
|  CHATKIT / CUSTOM RAG                                       |
|  +-- Vector Store: All .md and .yaml files                  |
|  +-- System Prompt: system_instruction.md                   |
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

## 1. VECTOR STORE - FILE INVENTORY (8 Files)

### Core Files

| # | File | Tokens | Upload | Purpose |
|---|------|--------|--------|---------|
| 00 | manifest.yaml | ~200 | YES | Index and navigation |
| 01 | quick_start.md | ~700 | YES | 2-minute setup guide |
| 02 | prime.md | ~800 | YES | Agent identity and blocks |
| 03 | instructions.md | ~1500 | YES | 8-step workflow execution |

### Config Files

| # | File | Tokens | Upload | Purpose |
|---|------|--------|--------|---------|
| 06 | data/input_schema.yaml | ~700 | YES | Input validation rules |
| 07 | output_template.md | ~2700 | YES | 32-block output format |

### Validation

| # | File | Tokens | Upload | Purpose |
|---|------|--------|--------|---------|
| 20 | data/quality_dimensions.yaml | ~1400 | YES | 5D validation framework |

### System

| # | File | Tokens | Upload | Purpose |
|---|------|--------|--------|---------|
| - | system_instruction.md | ~500 | COPY/PASTE | ChatKit system prompt |

**Total Tokens**: ~8,700 tokens (excluding system_instruction)

---

## 2. DEPLOY CHECKLIST

### Step 1: Vector Store Upload

Upload these files in order:

```
[ ] 1. manifest.yaml (~200 tokens) - Index
[ ] 2. quick_start.md (~700 tokens) - Entry point
[ ] 3. prime.md (~800 tokens) - Identity
[ ] 4. instructions.md (~1500 tokens) - Workflow
[ ] 5. data/input_schema.yaml (~700 tokens) - Validation
[ ] 6. output_template.md (~2700 tokens) - Output format
[ ] 7. data/quality_dimensions.yaml (~1400 tokens) - Quality gates
```

### Step 2: Chunking Configuration

```yaml
chunking_strategy:
  type: static
  max_chunk_size_tokens: 800
  chunk_overlap_tokens: 200
```

### Step 3: System Instruction

**IMPORTANTE**: NAO fazer upload do system_instruction.md ao vector store.

1. Abrir `system_instruction.md`
2. Selecionar TODO o conteudo (Ctrl+A)
3. Copiar (Ctrl+C)
4. Colar no campo "Instructions" da plataforma (Ctrl+V)
5. Salvar

### Step 4: Enable Tools

```
[ ] File Search - ENABLED (conectar ao vector store)
[ ] Code Interpreter - OPTIONAL (para validacao automatica)
```

### Step 5: Test

Run test prompt:
```
Crie uma estrategia de marca para uma loja de cosmeticos naturais.
Produto: Cosmeticos Organicos para Pele Sensivel
Categoria: Beleza > Cosmeticos Naturais
Audience: Mulheres 25-40, conscientes, urbanas
Price: Premium (R$ 100-300)
```

---

## 3. PLATFORM-SPECIFIC NOTES

### OpenAI Assistants

```yaml
Configuration:
  Name: MARCA Agent
  Model: gpt-4.1 or gpt-4o
  Instructions: [system_instruction.md content]
  Tools:
    - file_search: enabled
    - code_interpreter: optional

Vector Store:
  Create new vector store
  Upload 7 files (exclude system_instruction.md)
  Configure: chunk=800, overlap=200
  Attach to file_search tool
```

**Verification**:
1. Test with sample brand brief
2. Verify 32-block output structure
3. Check consistency score >= 0.85
4. Check uniqueness score >= 8.0

### Claude Projects

```yaml
Configuration:
  Project Name: MARCA Agent
  Custom Instructions: [system_instruction.md content]

Knowledge Upload:
  Upload all 7 files to Project Knowledge
  No chunking configuration needed (Claude handles)

Conversation Starter:
  "Crie uma estrategia de marca para: [produto]"
```

### ChatKit / Custom RAG

```yaml
Configuration:
  System Prompt: [system_instruction.md content]
  Temperature: 0.7
  Max Tokens: 4096

Vector Store Setup:
  Documents: All 7 files
  Chunk Size: 800 tokens
  Overlap: 200 tokens
  Embedding: text-embedding-3-small or equivalent

Retrieval:
  Top K: 5
  Similarity Threshold: 0.7
```

---

## 4. EXPECTED OUTPUT

Output deve conter:

```
STRUCTURE:
- 7 secoes claramente demarcadas
- 32 blocos completos
- Scores de validacao no final

QUALITY:
- Taglines: 40-60 chars (strict)
- Arquetipo: Primario + Secundario com justificativa
- Cores: HEX + RGB + psicologia
- Consistency Score: >= 0.85
- Uniqueness Score: >= 8.0/10

FORMAT:
## SECAO 1: IDENTIDADE (Blocos 1-5)
## SECAO 2: POSICIONAMENTO (Blocos 6-10)
## SECAO 3: TOM DE VOZ (Blocos 11-15)
## SECAO 4: IDENTIDADE VISUAL (Blocos 16-19)
## SECAO 5: NARRATIVA (Blocos 20-24)
## SECAO 6: DIRETRIZES (Blocos 25-28)
## SECAO 7: VALIDACAO (Blocos 29-32)
```

---

## 5. TEST INPUTS

### Minimal Input

```json
{
  "product_name": "Garrafa Termica Premium",
  "category": "Casa > Utensilios",
  "target_audience": "Profissionais urbanos 25-45",
  "price_range": "Premium (R$ 100-300)"
}
```

### Full Input

```json
{
  "product_name": "Cosmeticos Organicos para Pele Sensivel",
  "category": "Beleza > Cosmeticos Naturais",
  "target_audience": "Mulheres 25-40, conscientes, urbanas",
  "price_range": "Premium (R$ 100-300)",
  "competitors": ["Natura", "Granado", "Simple Organic"],
  "inspirations": ["Aesop", "Glossier"],
  "product_category": "cosmetics"
}
```

### Compliance Test (Regulated Category)

```json
{
  "product_name": "Suplementos Proteicos Veganos",
  "category": "Saude > Suplementos",
  "target_audience": "Atletas e fitness enthusiasts, 20-35, veganos",
  "price_range": "Medio (R$ 50-100)",
  "product_category": "supplements"
}
```

Expected: ANVISA compliance rules in Block 27.

---

## 6. TROUBLESHOOTING

| Problema | Causa Provavel | Solucao |
|----------|----------------|---------|
| Output incompleto | File Search desabilitado | Habilitar File Search e conectar vector store |
| Falta secoes | Vector store nao indexado | Aguardar indexacao completa (~2 min) |
| Taglines fora do range | system_instruction incompleto | Re-copiar system_instruction.md |
| Arquetipo inconsistente | Falta prime.md | Verificar upload do arquivo |
| Compliance ausente | product_category nao informado | Incluir campo na input |
| Cores sem HEX/RGB | output_template.md ausente | Verificar upload |
| Score de validacao faltando | data/quality_dimensions.yaml ausente | Verificar upload |
| Output em ingles | Language default | Especificar "language": "pt-BR" |

---

## 7. INTEGRATION POINTS

### Upstream (Input Sources)

| Agent | Provides | Field Mapping |
|-------|----------|---------------|
| pesquisa_agent | Market research | competitors, market_data |
| user_brief | Product info | product_name, category, audience |

### Downstream (Output Consumers)

| Agent | Receives | Blocks Used |
|-------|----------|-------------|
| anuncio_agent | Brand voice | Blocks 11-15 (Voice) |
| photo_agent | Visual identity | Blocks 16-19 (Visual) |
| curso_agent | Brand context | Blocks 20-24 (Narrative) |

---

**Upload Kit Version**: 1.1.0
**Status**: DEPLOY READY
**Quality Score**: 8.5/10
**Date**: 2025-12-20
