# PESQUISA AGENT | UPLOAD KIT v4.0 (MONOBLOCO)

## ARCHITECTURE

```
                    CHATKIT ASSISTANT
                          |
         +----------------+----------------+
         |                |                |
    INSTRUCTIONS     VECTOR STORE    CODE INTERPRETER
    (copy/paste)     (file search)    (validator.py)
         |                |                |
    system_          package files    validator.py
    instruction.md   (*.md, *.yaml)
```

---

## DEPLOY CHECKLIST

### Step 1: Create Assistant
```
[ ] Abrir ChatKit / OpenAI Assistants / Claude Projects
[ ] Criar novo Assistant
[ ] Nome: "pesquisa_agent"
[ ] Model: gpt-4.1 ou superior (ou claude-sonnet)
```

### Step 2: System Instruction
```
[ ] Abrir: system_instruction.md
[ ] Copiar conteudo COMPLETO
[ ] Colar no campo "Instructions" do Assistant
```

### Step 3: Vector Store
```
[ ] Criar Vector Store na plataforma
[ ] Upload todos os arquivos do pacote (arrastar pasta)
[ ] Configurar: chunk=800, overlap=200
[ ] Habilitar "File Search" no Assistant
```

### Step 4: Code Interpreter
```
[ ] Upload validator.py separadamente (se OpenAI)
[ ] Habilitar "Code Interpreter" no Assistant
```

### Step 5: Capabilities
```
[ ] Habilitar "Web Search"
[ ] Habilitar "File Search"
[ ] Habilitar "Code Interpreter"
```

### Step 6: Response Schema (IMPORTANTE - 2 CAMPOS)
```
[ ] Abrir "Response Schema" no Assistant
[ ] Colar o JSON abaixo:
```

```json
{
  "name": "response_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "productName": {"type": "string"},
      "report": {"type": "string"}
    },
    "required": [
      "productName",
      "report"
    ],
    "additionalProperties": false,
    "title": "response_schema"
  }
}
```

### Step 7: Test
```
[ ] Enviar: "Pesquisa: whey protein isolado"
[ ] Verificar: JSON com 2 campos (productName + report)
[ ] Verificar: report contem markdown completo
[ ] Verificar: Sem truncamento
[ ] Verificar: Sem citacoes internas (citeturn*, etc.)
[ ] Verificar: Confidence >= 0.60
```

---

## FILE INVENTORY

### Core (para Vector Store)
| File | Purpose |
|------|---------|
| manifest.yaml | Package info |
| quick_start.md | Entry point |
| prime.md | Identity |
| instructions.md | Coordinator |
| architecture.md | Tech arch |
| output_template.md | 2-field + template |
| system_instruction.md | System prompt |
| examples.md | Usage examples |
| error_handling.md | Error recovery |
| data/input_schema.yaml | Input validation |
| data/execution_plan.yaml | 9-phase plan |
| data/marketplaces.yaml | 9 BR MPs |
| data/research_config.yaml | Config |
| data/execution_plans.yaml | Plans |
| data/quality_dimensions.yaml | 5D scoring |
| prompts/orchestrator.md | Pipeline |
| prompts/query_generation.md | Queries HOP |
| prompts/marketplace_search.md | Search HOP |
| prompts/seo_taxonomy.md | SEO HOP |

### Separados
| File | Destino | Purpose |
|------|---------|---------|
| system_instruction.md | Instructions field | Copy/paste |

---

## RESPONSE SCHEMA v4.0 (2 CAMPOS)

```json
{
  "name": "response_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "productName": {
        "type": "string",
        "description": "Nome do produto ou marca pesquisado"
      },
      "report": {
        "type": "string",
        "description": "Relatorio completo em formato markdown"
      }
    },
    "required": ["productName", "report"],
    "additionalProperties": false,
    "title": "response_schema"
  }
}
```

---

## TROUBLESHOOTING

### Widget nao renderiza
- Verificar se JSON tem 2 campos: productName + report
- report deve ser STRING (nao objeto)
- Newlines devem estar escapadas (\n)

### Truncamento
- v4.0 monobloco resolve este problema
- Se persistir, verificar se Response Schema tem apenas 2 campos

### Citations vazando
- Verificar se system_instruction.md v4.0 foi copiada
- Secao STRIP CITATIONS deve estar no topo

### JSON invalido
- Verificar escaping de aspas no report
- Verificar se newlines sao \n (nao literal)

---

## QUICK TEST

```
Input: "Pesquisa: curso de IA do Rafael Milagre - VIVER DE IA"
Expected:
- JSON com 2 campos: productName + report
- productName: "Viver de IA"
- report: string markdown com toda pesquisa
- SEM citacoes internas (citeturn*, etc.)
- Confidence >= 0.60
```

---

## MIGRACAO v3.x -> v4.0

| Aspecto | v3.x (12 campos) | v4.0 (monobloco) |
|---------|------------------|------------------|
| Schema | 12 campos strings | 2 campos strings |
| Tokens schema | ~500 | ~50 |
| Risco truncamento | ALTO | BAIXO |
| Parsing errors | Frequente | Raro |

Para migrar:
1. Substituir Response Schema (12 -> 2 campos)
2. Substituir system_instruction.md
3. Testar com produto exemplo

---

**v4.0** | Monobloco | 2-Field Schema | Citation-Stripped | Markdown Report
