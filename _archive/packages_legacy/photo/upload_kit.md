# PHOTO AGENT | UPLOAD KIT v4.1 (MONOBLOCO + IMAGE GEN)

## ARCHITECTURE

```
                    CHATKIT ASSISTANT
                          |
         +----------------+----------------+
         |                |                |
    INSTRUCTIONS     VECTOR STORE    CODE INTERPRETER
    (copy/paste)     (file search)    (validator.py)
         |                |                |
    system_          18 files         validator.py
    instruction.md   (*.md, *.yaml)
```

---

## DEPLOY CHECKLIST

### Step 1: Create Assistant
```
[ ] Open ChatKit
[ ] Create new Assistant
[ ] Name: "photo_agent"
[ ] Model: gpt-4.1 or higher
```

### Step 2: System Instruction
```
[ ] Open: system_instruction.md
[ ] Copy COMPLETE content
[ ] Paste into "Instructions" field of Assistant
```

### Step 3: Vector Store
```
[ ] Create Vector Store in ChatKit
[ ] Upload files from package directory
[ ] Configure: chunk=800, overlap=200
[ ] Enable "File Search" on Assistant
```

### Step 4: Code Interpreter
```
[ ] Upload validator.py separately
[ ] Enable "Code Interpreter" on Assistant
```

### Step 5: Capabilities
```
[ ] Enable "Vision" (image input)
[ ] Enable "File Search"
[ ] Enable "Code Interpreter"
[ ] Enable "Image Generation" (gpt-image-1)
```

### Step 6: Response Schema (IMPORTANT - 2 FIELDS)
```
[ ] Open "Response Schema" in Assistant
[ ] Paste the JSON below:
```

```json
{
  "name": "response_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "productName": {
        "type": "string",
        "description": "Nome do produto analisado"
      },
      "prompts": {
        "type": "string",
        "description": "Prompts completos em formato markdown (analise + grid + 9 cenas)"
      }
    },
    "required": [
      "productName",
      "prompts"
    ],
    "additionalProperties": false,
    "title": "response_schema"
  }
}
```

### Step 7: Test
```
[ ] Send product image
[ ] Verify: JSON with 2 fields (productName + prompts)
[ ] Verify: prompts contain complete markdown (analise + OUTPUT 1 + OUTPUT 2)
[ ] Verify: No truncation
[ ] Verify: All prompts start with {user_image}
[ ] Verify: GENERATED IMAGE appears in chat (gpt-image-1)
[ ] Verify: Image is clickable for download
```

---

## FILE INVENTORY

### Core (for Vector Store)
| # | File | Tokens | Purpose |
|---|------|--------|---------|
| 00 | manifest.yaml | ~300 | Package info |
| 01 | quick_start.md | ~200 | Entry point |
| 02 | prime.md | ~400 | Identity (CONVERSION) |
| 03 | instructions.md | ~500 | Coordinator |
| 04 | architecture.md | ~300 | Tech arch |
| 05 | output_template.md | ~600 | 2-field + widget |
| 06 | data/input_schema.yaml | ~100 | Input validation |
| 07 | data/camera_profiles.yaml | ~200 | Camera specs |
| 08 | data/photography_styles.yaml | ~200 | Emotion styles |
| 09 | data/pnl_triggers.yaml | ~200 | 9 PNL triggers |
| 10 | prompts/orchestrator.md | ~400 | Pipeline |
| 11 | prompts/product_analysis.md | ~400 | Product analysis |
| 12 | prompts/prompt_generator.md | ~400 | Prompt generation |
| 13 | prompts/scene_descriptions.md | ~400 | Scene specs |

### Separate
| File | Destination | Purpose |
|------|-------------|---------|
| system_instruction.md | Instructions field | Copy/paste |
| upload_kit.md | Reference only | Deploy guide |

---

## RESPONSE SCHEMA v4.0 (2 FIELDS)

```json
{
  "name": "response_schema",
  "strict": true,
  "schema": {
    "type": "object",
    "properties": {
      "productName": {
        "type": "string",
        "description": "Nome do produto analisado"
      },
      "prompts": {
        "type": "string",
        "description": "Prompts completos em formato markdown"
      }
    },
    "required": ["productName", "prompts"],
    "additionalProperties": false,
    "title": "response_schema"
  }
}
```

---

## TROUBLESHOOTING

### Widget nao renderiza
- Verify if JSON has 2 fields: productName + prompts
- prompts must be STRING (not object)
- Newlines must be escaped (\n)

### Truncamento
- v4.0 monobloco resolves this problem
- If persists, verify if Response Schema has only 2 fields

### Citations vazando
- Verify if SYSTEM_INSTRUCTION v4.0 was copied
- STRIP CITATIONS section must be at top

### JSON invalido
- Verify escaping of quotes in prompts
- Verify if newlines are \n (not literal)

### Prompts sem {user_image}
- system_instruction.md v4.0 requires {user_image} in all prompts
- Without this, Gemini invents the product

---

## MIGRATION v3.x -> v4.0

| Aspect | v3.x (3 outputs) | v4.0 (monobloco) |
|--------|------------------|------------------|
| Schema | Multiple fields | 2 string fields |
| Widget | Separate grid | Markdown renderer |
| Schema tokens | ~500 | ~50 |
| Truncation risk | HIGH | LOW |
| gpt-1-image | OUTPUT 3 | Removed (Gemini only) |

To migrate:
1. Replace Response Schema (N fields -> 2 fields)
2. Replace SYSTEM_INSTRUCTION
3. Test with product image

---

## QUICK TEST

```
Input: [product image]
Expected:
- JSON with 2 fields: productName + prompts
- productName: product name
- prompts: markdown string with:
  - Analise do Produto (6 atributos + 7 contextos)
  - OUTPUT 1: Grid 3x3 prompt
  - OUTPUT 2: 9 individual prompts
  - Como Usar
  - Confidence score
- NO internal citations (citeturn*, etc.)
- ALL prompts start with {user_image} {seed:[RANDOM]}
```

---

## NOTES

### v4.1: gpt-image-1 reintroduced

v4.1 reintroduces automatic image generation:

1. **JSON monobloco**: 2 fields (productName + prompts) for widget
2. **gpt-image-1**: Generates Grid 3x3 image automatically
3. **Image in chat**: Appears AFTER JSON, clickable for download

### Execution flow:
```
INPUT (image) -> ANALISE -> JSON (2 campos) -> GERAR IMAGEM (gpt-image-1)
```

### Widget reorganizado:
- **TOP**: TextArea with prompts (easy to copy)
- **BELOW**: Rendered Markdown (visualization)

The user can:
- Use prompts in Gemini (with {user_image})
- Download generated image directly from chat
- Adapt prompts for Midjourney by removing {user_image}

---

**v4.1** | Monobloco + Image Gen | 2-Field Schema + gpt-image-1 | CONVERSION Framework
