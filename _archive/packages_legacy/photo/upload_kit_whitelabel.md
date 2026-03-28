# PHOTO Agent - White-Label Upload Kit

> **Target**: Agencies reselling AI photography service
> **Time to deploy**: 30 minutes
> **Platform**: ChatKit, OpenAI Assistants, custom RAG

---

## What You're Deploying

A complete AI product photography agent that generates conversion-focused photo prompts using the 9-Scene CONVERSION Framework. Your clients receive professional AI photography prompts branded with YOUR agency name.

**Key Features**:
- 9-scene emotional conversion framework
- Brazilian e-commerce marketplace compliance
- Dual prompt strategy (grid + separate images)
- 100% autonomous execution
- Professional camera specs and lighting

---

## Pre-Deployment Checklist

```yaml
assets_needed:
  - [ ] Files from package directory
  - [ ] Your agency logo (optional, for documentation)
  - [ ] Agency branding details (name, URL, colors, email)

platform_requirements:
  - [ ] ChatKit account OR OpenAI Assistant API access
  - [ ] Vector store capability (file search)
  - [ ] Vision capability (image input)
  - [ ] Code interpreter (optional, for validation)

time_required: "30 minutes"
skill_level: "Intermediate"
```

---

## Step 1: Replace Placeholders (5 minutes)

Open `system_instruction_whitelabel.md` and replace these 6 placeholders:

```markdown
{{AGENCY_NAME}}        -> "Acme Marketing"
{{AGENCY_URL}}         -> "acmemarketing.com.br"
{{PRIMARY_COLOR}}      -> "#0D9488"
{{SECONDARY_COLOR}}    -> "#14B8A6"
{{SUPPORT_EMAIL}}      -> "support@acme.com"
{{AGENT_NAME}}         -> "PhotoGenius"
```

**Example**:
```markdown
BEFORE:
You are {{AGENT_NAME}}, the exclusive AI product photography assistant from {{AGENCY_NAME}}.

AFTER:
You are PhotoGenius, the exclusive AI product photography assistant from Acme Marketing.
```

**Find & Replace** (use your text editor):
1. Find `{{AGENCY_NAME}}` -> Replace with your agency name
2. Find `{{AGENCY_URL}}` -> Replace with your URL
3. Find `{{PRIMARY_COLOR}}` -> Replace with your primary HEX
4. Find `{{SECONDARY_COLOR}}` -> Replace with your secondary HEX
5. Find `{{SUPPORT_EMAIL}}` -> Replace with your support email
6. Find `{{AGENT_NAME}}` -> Replace with your agent's name

**Save as**: `SYSTEM_INSTRUCTION_BRANDED.md`

---

## Step 2: Upload Files to Vector Store (10 minutes)

### Files to Upload (16 total)

**Core Files** (required):
```
manifest.yaml
quick_start.md
prime.md
instructions.md
architecture.md
data/input_schema.yaml
output_template.md
data/camera_profiles.yaml
data/photography_styles.yaml
data/pnl_triggers.yaml
prompts/orchestrator.md
prompts/product_analysis.md
prompts/prompt_generator.md
prompts/scene_descriptions.md
data/quality_dimensions.yaml
SYSTEM_INSTRUCTION_BRANDED.md (your customized version)
```

### Upload Process (ChatKit)

1. Go to your ChatKit dashboard
2. Create new Assistant: "PhotoGenius" (or your agent name)
3. Navigate to **File Search** section
4. Click **Upload Files**
5. Select all 16 files above
6. Wait for upload completion (usually 1-2 minutes)
7. Verify all files appear in list

### Upload Process (OpenAI Assistants API)

```python
from openai import OpenAI
client = OpenAI(api_key="your-api-key")

# Create vector store
vector_store = client.vector_stores.create(
    name="PhotoGenius Knowledge Base"
)

# Upload files
file_paths = [
    "manifest.yaml",
    "quick_start.md",
    # ... (all 16 files)
]

for path in file_paths:
    with open(path, "rb") as f:
        client.vector_stores.files.upload(
            vector_store_id=vector_store.id,
            file=f
        )

print(f"Vector Store ID: {vector_store.id}")
```

---

## Step 3: Configure System Instruction (5 minutes)

Copy the ENTIRE content of `SYSTEM_INSTRUCTION_BRANDED.md` (your customized version) into the **System Instruction** field.

**Where to paste**:
- **ChatKit**: Settings > System Instruction
- **OpenAI API**: `instructions` parameter when creating Assistant

**Verify**:
- All placeholders replaced (no `{{...}}` remaining)
- Agency name appears in identity section
- Footer includes your branding

---

## Step 4: Configure Input Schema (3 minutes)

Copy from `data/input_schema.yaml`:

```json
{
  "type": "object",
  "properties": {
    "product_image": {
      "type": "string",
      "description": "Image URL or uploaded file"
    },
    "product_description": {
      "type": "string",
      "description": "Basic product description"
    },
    "color": {
      "type": "string",
      "description": "HEX color code"
    },
    "material": {
      "type": "string",
      "description": "Product material and finish"
    },
    "target_audience": {
      "type": "string",
      "description": "Who buys this product"
    }
  },
  "required": ["product_image"]
}
```

**Where to paste**:
- **ChatKit**: Settings > Input Schema
- **OpenAI API**: `response_format` parameter

---

## Step 5: Enable Capabilities (2 minutes)

Enable these capabilities in your assistant settings:

```yaml
required:
  - File Search: YES
  - Vision (image input): YES

optional:
  - Code Interpreter: YES (for validation)
  - Web Browsing: NO (not needed)
```

**ChatKit Path**: Settings > Capabilities
**OpenAI API**: Set `tools` parameter

```python
tools=[
    {"type": "file_search"},
    {"type": "code_interpreter"}  # optional
]
```

---

## Step 6: Test Deployment (5 minutes)

### Test Case 1: Simple Product

**Input**:
```
Product Image: [upload thermal_bottle.jpg]
Description: "Stainless steel thermal bottle"
```

**Expected Output**:
```
PART 1: IMAGE (3x3 grid with 9 scenes)

PART 2: TEXT MARKDOWN
- Product Analysis table with #HEX color
- 7 Emotional Contexts
- PROMPT 1: Grid 3x3 (code block)
- PROMPT 2: 9 Separate Images (code block)
- How to Use instructions
- Footer with YOUR agency branding
```

### Test Case 2: Detailed Product

**Input**:
```
Product Image: [upload wireless_earbuds.jpg]
Description: "Premium wireless earbuds"
Color: "#1A202C"
Material: "Matte plastic + silicone tips"
Audience: "Tech professionals 25-40"
```

**Expected Output**:
- Same structure as Test Case 1
- More detailed product analysis
- Contextualized emotional triggers
- Agency footer present

### Validation Checklist

```yaml
output_validation:
  - [ ] IMAGE 3x3 grid generated (if using gpt-image-1)
  - [ ] Product analysis table present with #HEX
  - [ ] 7 emotional contexts listed
  - [ ] PROMPT 1 starts with {user_image} {seed:[RANDOM]}
  - [ ] PROMPT 2 starts with {user_image} {seed:[RANDOM]}
  - [ ] Both prompts in code blocks
  - [ ] "How to Use" section included
  - [ ] Footer shows YOUR agency name
  - [ ] Footer shows YOUR agency URL
  - [ ] Footer shows YOUR support email
```

---

## Step 7: Client Onboarding Template

Use this template when onboarding clients:

```markdown
# PhotoGenius - AI Product Photography

Welcome to PhotoGenius, your AI-powered product photography assistant from Acme Marketing.

## How to Use

1. **Upload** your product image
2. **Add** optional details (description, color, material)
3. **Receive** professional AI photo prompts in 2 formats:
   - PROMPT 1: 3x3 Grid (1 image with 9 scenes)
   - PROMPT 2: 9 Separate Images (recommended)

## What You Get

- 9 conversion-focused scenes based on consumer psychology
- Professional camera specs (Canon EOS R5 equivalent)
- Marketplace compliance (white backgrounds, 8K resolution)
- Ready-to-use prompts for Gemini, DALL-E, Midjourney

## Pricing

[INSERT YOUR PRICING HERE]
- Per-image: R$ XX
- Monthly plan (XX images): R$ XXX
- Enterprise: Custom

## Support

Email: support@acme.com
Website: acmemarketing.com.br
```

---

## Pricing Suggestions (Brazilian Market)

Based on market research for AI photography services:

| Tier | Price | Includes |
|------|-------|----------|
| **Pay-Per-Use** | R$ 25-40 per product | Single 9-scene prompt set |
| **Starter** | R$ 199/month | 10 products/month |
| **Professional** | R$ 499/month | 30 products/month |
| **Enterprise** | R$ 1,499/month | Unlimited + priority support |

**Profit Margin**:
- Cost: ~R$ 5-10 per generation (API costs)
- Revenue: R$ 25-40 per generation
- Margin: 60-75%

---

## Marketing Copy Template

```markdown
## Fotos de Produto que VENDEM - Criadas por IA

Transforme suas fotos de produto em 9 cenas profissionais que ativam gatilhos emocionais de compra.

### O que voce recebe:
- 9 prompts de fotografia baseados em psicologia do consumidor
- Especificacoes profissionais de camera e iluminacao
- Conformidade com marketplaces brasileiros (ML, Amazon, Shopee)
- 2 formatos: Grid 3x3 OU 9 imagens separadas

### Framework CONVERSION:
1. Hero Trust - Primeira impressao confiavel
2. Problem State - "EU tenho esse problema"
3. Solution Moment - "Isso FUNCIONA!"
4. Transformation - "EU QUERO esse resultado"
5. Social Belonging - "Pessoas como eu usam"
6. Benefit Proof - "Posso VER a qualidade"
7. Emotional Peak - "Vou me SENTIR assim"
8. Lifestyle Dream - "Essa e MINHA vida futura"
9. Marketplace - "Pronto para comprar"

### Precos:
[SEU PRICING AQUI]

### Contato:
{{AGENCY_NAME}} | {{AGENCY_URL}} | {{SUPPORT_EMAIL}}
```

---

## Troubleshooting

### Issue: Placeholders still showing

**Problem**: Output shows `{{AGENCY_NAME}}` instead of your name
**Solution**:
1. Verify you replaced ALL 6 placeholders in `system_instruction_whitelabel.md`
2. Re-copy the ENTIRE file to System Instruction
3. Clear cache and test again

### Issue: Prompts missing {user_image}

**Problem**: Generated prompts don't start with `{user_image} {seed:[RANDOM]}`
**Solution**:
1. Verify `SYSTEM_INSTRUCTION_BRANDED.md` was uploaded to vector store
2. Check "Rule 1: Anchor Tag" section is present
3. Re-upload file if corrupted

### Issue: No image generation

**Problem**: Agent returns text but no 3x3 grid image
**Solution**:
1. Verify gpt-image-1 capability is enabled
2. Check if platform supports native image generation
3. Use PROMPT 2 (9 separate) as primary recommendation

### Issue: Output doesn't match template

**Problem**: Missing sections or wrong format
**Solution**:
1. Verify all 16 files uploaded successfully
2. Check `output_template.md` is in vector store
3. Review `instructions.md` for workflow steps

---

## Advanced Customization

### Custom Camera Profiles

Edit `data/camera_profiles.yaml` to add your preferred camera specs:

```yaml
hero_trust:
  camera: "Sony A7R IV"
  lens: "85mm f/1.8"
  aperture: "f/8"
  iso: 100
  lighting: "High-key softbox"
```

### Custom Emotional Triggers

Edit `data/pnl_triggers.yaml` to adjust psychological triggers:

```yaml
scene_1:
  trigger: "Trust + Professionalism"
  purpose: "Trustworthy first impression"
  background: "#FFFFFF"
```

### Custom Quality Thresholds

Edit `data/quality_dimensions.yaml`:

```yaml
fidelity_threshold: 0.90
emotional_alignment_threshold: 8.0
marketplace_compliance: true
```

---

## Legal & Compliance

### Terms of Service Template

```markdown
## PhotoGenius - Terms of Service

1. **Service**: AI-generated photography prompts for product images
2. **Ownership**: Client owns all generated prompts and resulting images
3. **Usage**: Prompts may be used for commercial purposes
4. **Liability**: {{AGENCY_NAME}} is not responsible for AI generator outputs
5. **Refunds**: Available within 7 days if output doesn't match specifications
6. **Support**: Email support included at {{SUPPORT_EMAIL}}
```

### Privacy Policy Notes

- Client images are processed but not stored permanently
- Vector store files contain no client-specific data
- AI generators (Gemini, DALL-E) have their own privacy policies

---

## Success Metrics

Track these KPIs for your white-label deployment:

```yaml
usage_metrics:
  - Active clients per month
  - Images generated per client
  - Conversion rate (trial to paid)
  - Average revenue per user (ARPU)

quality_metrics:
  - Client satisfaction score (CSAT)
  - Prompt quality rating (1-10)
  - Support ticket volume
  - Churn rate

financial_metrics:
  - Monthly recurring revenue (MRR)
  - Customer acquisition cost (CAC)
  - Lifetime value (LTV)
  - Profit margin
```

---

## Support & Maintenance

### Monthly Maintenance Tasks

```yaml
monthly:
  - [ ] Review client feedback
  - [ ] Update camera profiles if needed
  - [ ] Test with new AI generator versions
  - [ ] Refresh documentation
  - [ ] Monitor API costs

quarterly:
  - [ ] Analyze usage patterns
  - [ ] Consider pricing adjustments
  - [ ] Evaluate competition
  - [ ] Plan feature updates
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-20 | Initial white-label upload kit |

---

*PHOTO Agent White-Label Upload Kit v1.0.0*
*Developed for agency reselling | Production-ready deployment*
