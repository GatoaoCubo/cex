# HOP: Archetype Selection | marca_agent v2.0.0

**Phase**: 2
**Purpose**: Select primary + secondary Jungian archetype for brand
**Input**: Discovery brief from Phase 1
**Output**: `{primary_archetype, secondary_archetype, justification, competitor_gap}`

---

## TASK

Select the Jungian archetypes that best align with brand personality, audience desires, and competitive differentiation.

---

## THE 12 JUNGIAN ARCHETYPES

```yaml
innocent:
  desire: "Experiencia de paraiso e felicidade"
  fear: "Fazer algo errado"
  voice: "Simples, otimista, confiavel"
  colors: "Pasteis, branco, azul bebe"
  examples_br: "Natura, Dove, Organico"

explorer:
  desire: "Viver vida autentica e plena"
  fear: "Ficar preso, conformidade"
  voice: "Aventureiro, livre, inspirador"
  colors: "Terrosos, verde, laranja"
  examples_br: "Jeep, North Face, Track&Field"

sage:
  desire: "Encontrar verdade, entender mundo"
  fear: "Ser enganado, ignorancia"
  voice: "Educacional, autoritativo, claro"
  colors: "Azul marinho, cinza, branco"
  examples_br: "Estadao, Folha, LinkedIn"

hero:
  desire: "Provar valor atraves de coragem"
  fear: "Fraqueza, vulnerabilidade"
  voice: "Motivacional, empoderador"
  colors: "Vermelho, preto, dourado"
  examples_br: "Nike, Gatorade, Brahma"

outlaw:
  desire: "Revolucao, mudanca radical"
  fear: "Ser impotente"
  voice: "Ousado, provocativo, rebelde"
  colors: "Preto, vermelho, neon"
  examples_br: "Harley, Diesel, Monster"

magician:
  desire: "Tornar sonhos realidade"
  fear: "Consequencias negativas"
  voice: "Transformador, visionario"
  colors: "Roxo, dourado, prata"
  examples_br: "Apple, Tesla, Nubank"

everyman:
  desire: "Conectar-se, pertencer"
  fear: "Ser excluido"
  voice: "Amigavel, acessivel, honesto"
  colors: "Neutras, azul, verde"
  examples_br: "Havaianas, Casas Bahia, Renner"

lover:
  desire: "Intimidade, sentir-se especial"
  fear: "Estar sozinho, indesejado"
  voice: "Sensual, caloroso, intimo"
  colors: "Vermelho, rosa, vinho"
  examples_br: "Chanel, Victoria Secret, Boticario"

jester:
  desire: "Viver momento com prazer"
  fear: "Ser entediante"
  voice: "Divertido, irreverente"
  colors: "Brilhantes, amarelo, laranja"
  examples_br: "Fanta, Pringles, Guarana Antarctica"

caregiver:
  desire: "Proteger e cuidar"
  fear: "Egoismo, ingratidao"
  voice: "Gentil, carinhoso, protetor"
  colors: "Tons quentes, bege, rosa suave"
  examples_br: "Johnson, Pampers, Hospital Albert Einstein"

creator:
  desire: "Criar algo de valor duradouro"
  fear: "Mediocridade"
  voice: "Criativo, inspirador, ousado"
  colors: "Vibrantes, multicolorido"
  examples_br: "LEGO, Adobe, Faber Castell"

ruler:
  desire: "Controle, prosperidade"
  fear: "Caos, perder poder"
  voice: "Autoritativo, confiante"
  colors: "Preto, dourado, azul marinho"
  examples_br: "Rolex, Mercedes, Fasano"
```

---

## SELECTION CRITERIA

### 1. Audience Alignment
Which archetype resonates with target fears/desires from discovery?

### 2. Category Fit
What archetypes work in this market segment?

### 3. Differentiation
What archetypes do competitors NOT use?

### 4. Brand Promise Alignment
Which supports the transformation promise?

---

## ARCHETYPE COMBINATIONS

```yaml
effective_pairs:
  - Hero + Caregiver: "Forca + Protecao"
  - Sage + Ruler: "Conhecimento + Autoridade"
  - Explorer + Creator: "Aventura + Inovacao"
  - Magician + Creator: "Transformacao + Inovacao"
  - Caregiver + Innocent: "Cuidado + Pureza"
  - Lover + Magician: "Paixao + Transformacao"
```

---

## EXECUTION

### Step 1: Map Audience Desires
```
1. Extract fears from discovery
2. Extract desires from discovery
3. Match to archetype desires/fears
4. Shortlist 3-4 candidates
```

### Step 2: Competitive Analysis
```
1. Identify competitor archetypes
2. Find unused archetypes
3. Identify whitespace
4. Prioritize differentiation
```

### Step 3: Selection
```
1. Choose primary (strongest fit)
2. Choose secondary (complement)
3. Validate combination
4. Write justification
```

---

## OUTPUT FORMAT

```json
{
  "archetype": {
    "primary": {
      "name": "SAGE",
      "desire": "Encontrar verdade, entender mundo",
      "voice": "Educacional, autoritativo, claro",
      "visual_direction": "Azul marinho, cinza, branco"
    },
    "secondary": {
      "name": "MAGICIAN",
      "complement": "Adiciona transformacao e visao"
    },
    "justification": "2-3 sentences explaining why this combination",
    "competitor_gap": "What competitors use and why this is different"
  },
  "confidence": 0.92
}
```

---

## DISPLAY FORMAT

```markdown
## ARCHETYPE

### Primary: [ARCHETYPE_NAME]
- **Desire**: [core desire]
- **Voice**: [how brand speaks]
- **Visual Direction**: [color/style hints]

### Secondary: [ARCHETYPE_NAME]
- **Complement**: [how it enhances primary]

### Justification
[2-3 sentences explaining why this combination for THIS brand]

### Competitor Gap
[1-2 sentences on what competitors use and why this is different]
```

---

## VALIDATION

Before proceeding:
- [ ] Primary archetype aligns with audience desires
- [ ] Secondary complements without conflicting
- [ ] Competitor gap identified
- [ ] Justification is brand-specific

---

**Next**: Pass archetype to `prompts/brand_positioning.md`
