# HOP: Product Analysis | photo_agent v10.1.0

**Phase**: 2
**Purpose**: Analyze product image and extract attributes
**Input**: Product image
**Output**: `{PRODUTO, COR, MATERIAL, FORMA}`

---

## TASK

Visually analyze the product image and extract 4 key attributes for prompt generation.

---

## EXTRACTION RULES

### PRODUTO (Product Description)
```yaml
purpose: Short, accurate product description
format: "[Type] [Material/Style] [Key Feature]"
max_words: 10
language: Portuguese

examples:
  - "Arranhador de gato sisal natural torre vertical"
  - "Bolsa feminina couro legitimo marrom"
  - "Fone de ouvido bluetooth over-ear preto"
  - "Caneca ceramica artesanal azul"

extraction_focus:
  - What is the product category?
  - What is the primary material?
  - What is the distinguishing feature?
```

### COR (Primary Color)
```yaml
purpose: Exact hex color code
format: "#XXXXXX"
method: Sample dominant color from product

examples:
  - "#8B7355" (natural sisal brown)
  - "#2C3E50" (dark blue-gray)
  - "#F5F5F5" (off-white)
  - "#C0392B" (deep red)

extraction_focus:
  - What is the dominant product color?
  - Avoid background colors
  - Use most representative area
```

### MATERIAL (Material and Finish)
```yaml
purpose: Material type and surface finish
format: "[Material principal] com [acabamento/detalhe]"
max_words: 8

examples:
  - "Sisal natural com base MDF"
  - "Couro legitimo com costura aparente"
  - "Plastico ABS com acabamento fosco"
  - "Ceramica esmaltada com detalhes dourados"

extraction_focus:
  - What is the main material?
  - What is the surface finish?
  - Any secondary materials?
```

### FORMA (Shape/Format)
```yaml
purpose: Physical shape and structure
format: "[Forma] [Dimensao/Estrutura]"
max_words: 6

examples:
  - "Torre vertical 3 plataformas"
  - "Formato retangular compacto"
  - "Design arredondado ergonomico"
  - "Estrutura circular com alca"

extraction_focus:
  - What is the overall shape?
  - Any structural features?
  - Relative proportions
```

---

## EXECUTION

### Step 1: Visual Scan
```
1. Identify product category
2. Note primary features
3. Assess materials
4. Observe structure
```

### Step 2: Color Extraction
```
1. Find most representative color area
2. Avoid shadows and highlights
3. Convert to hex
4. Verify accuracy
```

### Step 3: Material Analysis
```
1. Identify visible materials
2. Note surface finish (matte, glossy, textured)
3. Identify secondary materials
4. Describe in PT-BR
```

### Step 4: Form Description
```
1. Describe overall shape
2. Note structural elements
3. Include distinguishing features
4. Keep concise
```

---

## OUTPUT FORMAT

```json
{
  "analysis": {
    "PRODUTO": "Arranhador de gato sisal natural torre vertical",
    "COR": "#8B7355",
    "MATERIAL": "Sisal natural com base MDF",
    "FORMA": "Torre vertical 3 plataformas"
  },
  "confidence": {
    "PRODUTO": 0.95,
    "COR": 0.90,
    "MATERIAL": 0.85,
    "FORMA": 0.92
  },
  "notes": "Product clearly visible, good lighting"
}
```

---

## DISPLAY FORMAT

```markdown
## Analise do Produto

| Atributo | Valor |
|----------|-------|
| **Produto** | Arranhador de gato sisal natural torre vertical |
| **Cor** | #8B7355 |
| **Material** | Sisal natural com base MDF |
| **Forma** | Torre vertical 3 plataformas |
```

---

## ERROR HANDLING

### Low Visibility
```yaml
if product_obscured:
  request: "Imagem com produto mais visivel"
  action: describe_what_is_visible
```

### Multiple Products
```yaml
if multiple_products:
  action: focus_on_main_product
  note: "Focando no produto principal"
```

### Uncertain Material
```yaml
if material_unclear:
  action: describe_visually
  format: "Material [aspecto visual] com [acabamento]"
```

---

## VALIDATION

Before proceeding:
- [ ] PRODUTO is descriptive and accurate
- [ ] COR is valid 6-digit hex
- [ ] MATERIAL includes finish type
- [ ] FORMA describes structure

---

**Next**: Pass analysis to `prompt_generator.md`
