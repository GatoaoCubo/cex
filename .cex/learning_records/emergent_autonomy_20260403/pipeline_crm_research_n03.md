# HANDOFF N01 → N03: CRM Research Pipeline Automation

**Missão:** Construir pipeline automatizada de research CRM para replicação em múltiplas cidades

**Context:** N01 desenvolveu metodologia manual eficaz (26→112+ contatos em ABC). Agora precisa de artefatos que automatizem essa pipeline para escalar para 10+ cidades.

## 🎯 **OBJETIVOS N03**

### **1. Agent CRM Research Orchestrator**
**Tipo:** `agent`  
**Propósito:** Coordenar research multi-fonte para descoberta businesses pet

**Capabilities:**
- Sequenciar busca por fases (1-8)
- Gerenciar rate limits APIs (SERPER/FIRECRAWL)
- Consolidar dados de múltiplas fontes
- Aplicar scoring automático (potencial A/B/C)

### **2. Search Strategy Configuration**
**Tipo:** `search_tool`  
**Propósito:** Configurar termos de busca otimizados por segmento pet

**Include:**
- Termos primários por vertical
- Long-tail keywords locais
- Negative keywords (filtros)
- Regional variations (ABC vs Interior)

### **3. Data Validation Pipeline** 
**Tipo:** `validator`
**Propósito:** Validar qualidade contatos descobertos

**Rules:**
- Telefone: formato BR válido
- CNPJ: validação algoritmica
- Email: formato + domínio ativo
- Website: SSL + response 200

### **4. CRM Structure Template**
**Tipo:** `response_format`  
**Propósito:** Padronizar output research multi-cidade

**Schema:**
```yaml
cidade:
  nome: string
  uf: string
  ring: 1|2|3
  densidade_estimada: float

business:
  nome: string
  cnpj?: string
  telefone?: string
  whatsapp?: string
  email?: string
  website?: string
  endereco: string
  segmento: enum[12_tipos]
  potencial: A|B|C
  fonte_descoberta: string
  data_discovery: datetime
```

### **5. Multi-Source Retriever**
**Tipo:** `retriever`  
**Propósito:** Orquestrar coleta dados de 6+ fontes simultaneamente

**Sources:**
- Google Search (SERPER)
- Diretórios (TeleListas via FIRECRAWL)
- Social (Instagram/Facebook via FIRECRAWL)
- Delivery (iFood/Rappi via FETCH)
- Business directories (via EXA)
- CNPJ databases (via FETCH)

### **6. Geographic Density Analyzer**
**Tipo:** `analyzer`  
**Propósito:** Calcular densidade businesses/km² para priorização

**Metrics:**
- Density score (biz/km²)
- Market saturation estimate
- Competition analysis
- Expansion priority (1-10)

## 📋 **PIPELINE PHASES (para automação)**

### **Phase 1: City Setup**
```yaml
input: cidade_nome, uf
process: 
  - Load geographic boundaries
  - Estimate market size
  - Set search parameters
output: city_config.yaml
```

### **Phase 2: Multi-Search Discovery**
```yaml
input: city_config.yaml
process:
  - Parallel search 4 terms (pet shop, banho tosa, veterinario, distribuidor)
  - Rate limit management
  - Dedup by phone/address
output: raw_businesses.json
```

### **Phase 3: Directory Enrichment**
```yaml
input: raw_businesses.json
process:
  - Scrape TeleListas city page
  - Cross-reference existing data
  - Add missing businesses
output: enriched_businesses.json
```

### **Phase 4: Contact Validation**
```yaml
input: enriched_businesses.json
process:
  - Validate phone numbers
  - Check email formats
  - Test website accessibility
  - CNPJ lookup when available
output: validated_contacts.json
```

### **Phase 5: Social Discovery**
```yaml
input: validated_contacts.json
process:
  - Instagram hashtag search
  - Facebook page discovery
  - Google Reviews mining
  - Add social contacts
output: social_enhanced.json
```

### **Phase 6: Delivery Platform Mining**
```yaml
input: social_enhanced.json
process:
  - iFood city search
  - Rappi pet category
  - Cross-reference existing
output: delivery_enhanced.json
```

### **Phase 7: Scoring & Classification**
```yaml
input: delivery_enhanced.json
process:
  - Apply potential scoring (A/B/C)
  - Ring classification (1/2/3)
  - Segment categorization
  - Completeness scoring
output: scored_crm.json
```

### **Phase 8: CRM Output Generation**
```yaml
input: scored_crm.json
process:
  - Generate markdown table
  - Sort by potential + ring
  - Add summary statistics
  - Validate schema compliance
output: output_crm_[cidade].md
```

## 🔧 **TOOLS INTEGRATION**

### **Agent Orchestrator deve usar:**
```python
# Core research tools
tools = [
    "mcp__google-search__search_web",  # SERPER equivalent
    "mcp__firecrawl__firecrawl_scrape", # Directory scraping
    "mcp__fetch__fetch",               # Direct URL access
    "mcp__firecrawl__firecrawl_search" # Semantic discovery
]
```

### **Rate Limits a considerar:**
- SERPER: 2500 queries/month
- FIRECRAWL: 500 scrapes/month  
- FETCH: unlimited
- EXA: 1000 searches/month

## 🎯 **SUCCESS CRITERIA**

### **Quantitativos:**
- **40+ businesses** descobertos por cidade média
- **60%+ taxa** conversão contato direto
- **4+ fontes** simultâneas por business
- **<2h** tempo total research cidade

### **Qualitativos:**
- Pipeline replicável sem intervenção manual
- Output padronizado cross-cidade
- Tracking de source attribution
- Error handling robusto

## 📁 **DELIVERABLES ESPERADOS**

1. **`agent_crm_research_orchestrator.md`** (P02_agents/)
2. **`search_tool_pet_business_discovery.md`** (P03_tools/)  
3. **`validator_business_contact_quality.md`** (P04_validation/)
4. **`response_format_crm_output_standard.md`** (P05_formats/)
5. **`retriever_multi_source_business_intel.md`** (P06_retrieval/)
6. **`analyzer_geographic_business_density.md`** (P07_analytics/)

## 🚀 **NEXT STEP**

Após N03 construir artefatos → N01 testa pipeline em **São Bernardo do Campo** como prova de conceito antes de escalar para 10+ cidades Ring 2.

**Deadline:** Construção completa pipeline para teste SBC dentro de 24h.

---
**From:** N01 Research Nucleus  
**To:** N03 Build Nucleus  
**Priority:** High  
**Estimated effort:** 6-8 artifacts, ~4h build time