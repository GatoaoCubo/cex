# Mission: ADVANCED BUSINESS DISCOVERY PIPELINE — N03 Build Task

**Output**: `N03_builder/compiled/advanced_discovery_pipeline.yaml`
**Signal**: `python _tools/signal_writer.py n03 complete 9.0 ADV_DISCOVERY_PIPELINE`
**Commit + signal when done.**

---

## ⚡ MISSION OVERVIEW — BUILD THE ULTIMATE BUSINESS DISCOVERY ENGINE

**Context**: N01 Research validou 8 técnicas avançadas de discovery com 6-9x improvement vs métodos manuais. Agora N03 deve construir pipeline completa, modular e context-aware.

**Validated ROI**: 50+ businesses descobertos em 2h de teste (só São Bernardo)
**Estimated Total Market**: 1,200+ businesses missing no ABC
**Target Coverage**: 90%+ do mercado estimado

---

## 🎯 CORE ARCHITECTURE REQUIREMENTS

### **System Philosophy: Context-Aware Variable Engine**
Pipeline deve adaptar automaticamente baseado em:
- **Region Type**: urban_dense|suburban|rural
- **Business Density**: high|medium|low  
- **Niche Specificity**: broad|focused|ultra_niche
- **Market Maturity**: established|emerging|saturated
- **Data Availability**: rich|moderate|sparse

### **Modular Structure Required**
```
cex_discovery_pipeline/
├── core/                    # 4 módulos principais
├── miners/                  # 8 técnicas validadas
├── agents/                  # 4 background agents
├── config/                  # 4 configuration files
└── output/                  # Results & analytics
```

---

## 🏗️ ARTIFACTS TO BUILD (15 MODULES + 4 CONFIGS)

### **TIER 1: CORE FOUNDATION (P0 - Build First)**

#### **Artifact 1: Context Engine**
```yaml
kind: context_engine
pillar: P03
title: "Context-Aware Discovery Configuration Engine"
purpose: "Analyzes region, niche, and market characteristics to auto-configure pipeline execution"
key_functions:
  - analyze_region_type: "population_density, economic_profile, digital_presence"
  - analyze_niche_complexity: "specificity_level, keyword_complexity, market_maturity"  
  - generate_execution_strategy: "technique_priorities, agent_selection, quality_gates"
context_variables:
  region_types: ["urban_dense", "suburban_spread", "rural_sparse"]
  niche_levels: ["broad_ecosystem", "focused_specialty", "ultra_niche"]
  execution_modes: ["comprehensive", "fast_scan", "premium_deep"]
```

#### **Artifact 2: Master Orchestrator**
```yaml
kind: pipeline_orchestrator  
pillar: P03
title: "Advanced Discovery Pipeline Orchestrator"
purpose: "Coordinates parallel miners and background agents based on context"
key_functions:
  - execute_discovery_mission: "Main entry point for natural language requests"
  - spawn_mining_agents: "Parallel execution of 8 validated techniques"
  - orchestrate_background_agents: "Validation, deduplication, enrichment"
  - consolidate_results: "Cross-source data fusion with quality gates"
execution_patterns:
  parallel_mining: "Tier1 premium miners run simultaneously"
  background_agents: "Validator, deduplicator, enricher run async"
  wave_execution: "High-yield first, support techniques second"
```

#### **Artifact 3: Agent Dispatcher**
```yaml
kind: agent_dispatcher
pillar: P03  
title: "Background Agent Management System"
purpose: "Spawns and manages specialist agents via Agent tool with run_in_background=True"
agent_types:
  - validator_agent: "Phone/address validation via APIs"
  - deduplicator_agent: "Cross-source fuzzy matching + ML"
  - enricher_agent: "Data enhancement via external APIs"
  - competitor_agent: "Competitive intelligence analysis"
spawn_pattern: |
  await self.agent_tool.invoke({
      "description": f"{agent_type} background processing",
      "prompt": agent_prompt,
      "run_in_background": True,
      "subagent_type": "general-purpose"
  })
```

### **TIER 2: PREMIUM MINERS (P0-P1 - Validated 90%+ Eficácia)**

#### **Artifact 4: Google Maps Advanced Miner**
```yaml
kind: google_maps_miner
pillar: P03
title: "Google Maps Browser Automation Miner"
purpose: "Highest-yield business discovery via browser automation + anti-detection"
validation_status: "✅ TESTED - 95% eficácia, dados mais completos"
key_features:
  - browser_session_pool: "FIRECRAWL sessions com rotation anti-detection"
  - micro_geography_scan: "Busca bairro-por-bairro baseado em densidade"
  - structured_extraction: "name, rating, reviews, phone, address, hours"
  - people_also_search: "Descoberta adicional via seção relacionados"
  - screenshot_backup: "Fallback para casos de parsing failure"
context_adaptation:
  high_density: "exhaustive_neighborhood_scan"
  medium_density: "strategic_hotspot_scan"
  low_density: "broad_area_scan"
```

#### **Artifact 5: Facebook Business Intelligence Miner**
```yaml
kind: facebook_business_miner
pillar: P03
title: "Facebook Business Pages Discovery Engine"
purpose: "Volume discovery via business pages sem login requirement"
validation_status: "✅ TESTED - 95% eficácia, maior volume (10 novos descobertos)"
key_features:
  - parallel_page_discovery: "Busca simultânea por múltiplos patterns"
  - business_intelligence: "followers, engagement, contact, services"
  - contextual_patterns: "Adapta search terms baseado em niche/region"
  - social_validation: "Cross-reference com outras fontes"
search_patterns:
  location_category: 'site:facebook.com "são bernardo" "pet shop"'
  business_specific: 'site:facebook.com "banho tosa" "veterinário"'
  micro_niche: 'site:facebook.com "hotel gato" "maine coon"'
```

#### **Artifact 6: Yellow Pages Fusion Miner**
```yaml
kind: yellow_pages_miner
pillar: P03
title: "Multi-Source Directory Mining Engine"
purpose: "Parallel mining Apontador + TeleListas + GuiaMais + others"
validation_status: "✅ TESTED - 90% eficácia, telefones validados"
sources:
  - apontador: "https://www.apontador.com.br"
  - telelistas: "https://www.telelistas.net"
  - guiamais: "https://www.guiamais.com.br"
  - encontrasp: "https://www.encontrasp.com.br"
cross_validation: "Phone + address validation across sources"
data_quality: "Highest phone/address accuracy rate"
```

#### **Artifact 7: CEP Micro-Geography Scanner**
```yaml
kind: cep_geography_miner
pillar: P03
title: "CEP-Based Hidden Business Discovery"
purpose: "Reveals 'invisible' businesses via micro-geographic search"
validation_status: "✅ TESTED - 90% eficácia, descobre ocultos"
discovery_method: 'Google search: "pet shop CEP 09720" reveals local businesses'
strategy_adaptation:
  urban_dense: "cep_by_block (granular)"
  suburban: "cep_by_district (moderate)"
  rural: "cep_by_municipality (broad)"
proven_yield: "4+ novos businesses per CEP code tested"
```

### **TIER 3: SUPPORT MINERS (P1-P2 - 70-85% Eficácia)**

#### **Artifact 8: Delivery Apps Miner**
```yaml
kind: delivery_apps_miner
pillar: P03
title: "iFood + Delivery Platform Business Discovery"
purpose: "Discovers businesses via delivery platform listings"
validation_status: "✅ TESTED - 85% eficácia, multi-location confirmation"
platforms:
  - ifood: "pet shops com delivery ativo"
  - rappi: "produtos pet delivery"
  - uber_eats: "pet food delivery"
unique_value: "Confirms multi-location businesses + operational status"
```

#### **Artifact 9: Marketplace Reverse Miner**
```yaml
kind: marketplace_miner
pillar: P03
title: "Mercado Livre + OLX Business Discovery"
purpose: "Reverse discovery via marketplace seller analysis"
validation_status: "✅ TESTED - 80% eficácia, businesses 'invisíveis'"
discovery_patterns:
  business_sales: '"passo ponto pet shop" reveals active businesses'
  equipment_sales: '"mesa tosa" indicates operating pet shops'
  location_confirmation: "Cross-reference addresses with other sources"
```

#### **Artifact 10: Waze Directory Miner**
```yaml
kind: waze_directory_miner
pillar: P03
title: "Waze Business Listings Discovery"
purpose: "Navigation-based business discovery with validated addresses"
validation_status: "✅ TESTED - 85% eficácia, telefones + navegação"
unique_value: "Provides navigation-validated addresses + phone numbers"
data_quality: "High address accuracy due to GPS validation"
```

### **TIER 4: BACKGROUND AGENTS (P1-P2)**

#### **Artifact 11: Phone & Address Validator Agent**
```yaml
kind: validator_agent
pillar: P02
title: "Background Contact Data Validation Agent"
purpose: "Real-time phone/address validation via external APIs"
validation_apis:
  - twilio_lookup: "Phone number validation"
  - google_places: "Address geocoding"
  - here_geocoding: "Alternative address validation"
quality_thresholds:
  phone_confidence: 0.85
  address_confidence: 0.80
execution_mode: "background parallel via Agent tool"
```

#### **Artifact 12: Cross-Source Deduplicator Agent**
```yaml
kind: deduplicator_agent
pillar: P02
title: "Intelligent Business Deduplication Agent"
purpose: "Cross-source duplicate detection via ML + fuzzy matching"
algorithms:
  - fuzzy_name_matching: "Business name similarity"
  - phone_exact_matching: "Exact phone number matches"
  - address_geospatial: "GPS coordinate proximity"
confidence_weights:
  phone_match: 0.8
  address_match: 0.6
  name_match: 0.4
execution_mode: "background parallel processing"
```

#### **Artifact 13: Business Intelligence Enricher Agent**
```yaml
kind: enricher_agent
pillar: P02
title: "Business Data Enhancement Agent"
purpose: "Enriches discoveries with external API data + social signals"
enrichment_sources:
  - google_places_api: "Reviews, ratings, hours, photos"
  - social_apis: "Instagram/Facebook follower data"
  - business_apis: "CNPJ validation via Receita Federal"
enhancement_level: "configurable basic|standard|comprehensive"
execution_mode: "background enhancement pipeline"
```

### **TIER 5: CONFIGURATION SYSTEM (P1)**

#### **Config 1: Expandable Niche Definitions**
```yaml
file_path: config/niche_definitions.yaml
purpose: "Extensible business type definitions for any niche"
structure:
  pet_ecosystem:
    core_types: ["pet_shop", "clinica_vet", "banho_tosa"]
    specialized_types: ["hotel_cachorro", "hotel_gato", "cat_cafe"]
    micro_niches: ["maine_coon_breeder", "reptile_specialist"]
    search_patterns:
      primary_keywords: ["pet", "animal", "veterinário"]
      secondary_keywords: ["banho", "tosa", "ração"]
expansion_framework: "Template for adding new niches (restaurant, beauty, auto)"
```

#### **Config 2: Regional Profiles**
```yaml  
file_path: config/region_profiles.yaml
purpose: "Geographic configurations and optimization patterns"
profiles:
  sao_bernardo_campo:
    type: "urban_dense"
    population: 833000
    business_density: "high"
    optimal_techniques: ["google_maps", "facebook", "cep_scan"]
  abc_metropolitano:
    type: "metropolitan"
    cities: ["sao_bernardo", "santo_andre", "sao_caetano"]
    execution_strategy: "multi_city_parallel"
```

### **TIER 6: INTERFACE & ANALYTICS (P2)**

#### **Artifact 14: Natural Language Query Processor**
```yaml
kind: query_processor
pillar: P03
title: "Natural Language to Pipeline Configuration Converter"
purpose: "Converts user requests to executable pipeline configurations"
examples:
  - input: "Find cat hotels in São Paulo"
    output: "business_types: [hotel_gato], location: sao_paulo, scope: metropolitan"
  - input: "Discover pet groomers in ABC with premium services"
    output: "business_types: [banho_tosa_premium], location: abc_region, filters: premium"
```

#### **Artifact 15: Performance Analytics Engine**
```yaml
kind: analytics_engine
pillar: P01
title: "Pipeline Performance & Optimization Analytics"
purpose: "Tracks performance, optimizes technique weights, learning system"
metrics:
  - discovery_yield_per_technique: "ROI measurement"
  - quality_score_distribution: "Data accuracy tracking"
  - execution_time_optimization: "Performance tuning"
learning_system: "Adapts technique weights based on historical performance"
```

---

## 🎯 CRITICAL IMPLEMENTATION REQUIREMENTS

### **Context Variables Integration**
Every module MUST accept and respond to context variables:
```python
def execute(self, search_params, context_config):
    # Context variables guide execution:
    if context_config.region_type == "urban_dense":
        return self._high_density_strategy(search_params)
    elif context_config.region_type == "suburban":
        return self._medium_density_strategy(search_params)
    # etc...
```

### **Pipeline Extensibility**
- **New Niches**: Add via `niche_definitions.yaml` without code changes
- **New Regions**: Add via `region_profiles.yaml` configuration
- **New Techniques**: Plugin architecture for additional miners
- **New APIs**: Configurable API endpoints for validation/enrichment

### **Quality Gates Enforcement**
```python
quality_gates = {
    "phone_validation": context_config.phone_confidence_threshold,
    "address_validation": context_config.address_confidence_threshold,
    "duplicate_detection": context_config.similarity_threshold,
    "business_existence": context_config.existence_confidence
}
```

### **Background Agent Integration**
All background agents MUST use:
```python
await self.agent_tool.invoke({
    "description": "Agent background task",
    "prompt": agent_specific_prompt,
    "run_in_background": True,  # CRITICAL
    "subagent_type": "general-purpose"
})
```

---

## 🚀 SUCCESS CRITERIA & VALIDATION

### **Performance Targets**
- **Discovery Yield**: 6-9x improvement vs manual methods (validated in tests)
- **Data Quality**: 85%+ validated phone/address contacts
- **Execution Time**: Regional scan 2-4 hours comprehensive
- **Coverage**: 90%+ of estimated market size
- **Deduplication**: <5% duplicate rate across sources

### **Functional Requirements**
- ✅ **Natural Language Interface**: Accept plain English requests
- ✅ **Context Adaptation**: Auto-optimize based on region/niche
- ✅ **Parallel Execution**: Miners + agents run simultaneously
- ✅ **Quality Validation**: Real-time phone/address validation
- ✅ **Cross-Source Fusion**: Intelligent deduplication and merging
- ✅ **Extensible Architecture**: Add niches/regions via configuration

### **Validation Test Cases**
```python
# Test 1: São Bernardo Pet Discovery (validated baseline)
expected_yield = 150  # 3x current 50 test discoveries
quality_threshold = 0.85
execution_time_max = 4_hours

# Test 2: Ultra-niche Discovery  
query = "Find Maine Coon breeders in São Paulo metropolitan"
expected_yield = 5-15  # Ultra-specific niche
quality_threshold = 0.90  # Higher quality for rare businesses

# Test 3: Multi-region Discovery
query = "Map veterinary clinics in ABC region" 
expected_yield = 200+ # 3 cities combined
execution_mode = "parallel_multi_city"
```

---

## 📦 DELIVERABLES CHECKLIST

### **Code Modules (15 artifacts)**
- [ ] Context Engine (core/context_engine.py)
- [ ] Master Orchestrator (core/orchestrator.py)  
- [ ] Agent Dispatcher (core/discovery_dispatcher.py)
- [ ] Google Maps Miner (miners/tier1_premium/google_maps_miner.py)
- [ ] Facebook Business Miner (miners/tier1_premium/facebook_business_miner.py)
- [ ] Yellow Pages Miner (miners/tier1_premium/yellow_pages_miner.py)
- [ ] CEP Geography Miner (miners/tier1_premium/cep_geography_miner.py)
- [ ] Delivery Apps Miner (miners/tier2_support/delivery_apps_miner.py)
- [ ] Marketplace Miner (miners/tier2_support/marketplace_miner.py)
- [ ] Waze Directory Miner (miners/tier2_support/waze_directory_miner.py)
- [ ] Validator Agent (agents/validator_agent.py)
- [ ] Deduplicator Agent (agents/deduplicator_agent.py)
- [ ] Enricher Agent (agents/enricher_agent.py)
- [ ] Query Processor (core/query_processor.py)
- [ ] Analytics Engine (core/analytics_engine.py)

### **Configuration Files (4 configs)**
- [ ] niche_definitions.yaml (extensible business types)
- [ ] region_profiles.yaml (geographic configurations)
- [ ] technique_weights.yaml (dynamic prioritization)
- [ ] quality_gates.yaml (validation rules)

### **Integration Requirements**
- [ ] FIRECRAWL browser automation integration
- [ ] Agent tool background execution integration
- [ ] External APIs integration (phone/address validation)
- [ ] Cross-source deduplication algorithms
- [ ] Natural language processing for query parsing

### **Documentation & Testing**
- [ ] API documentation for all modules
- [ ] Configuration examples for different use cases
- [ ] Performance benchmarks vs manual methods
- [ ] Extensibility guide for new niches/regions

---

## ⚡ EXECUTION PRIORITY & TIMELINE

### **Week 1: Core Foundation**
- Context Engine + basic orchestrator
- Google Maps Miner (highest ROI) 
- Basic phone/address validator

### **Week 2: Premium Expansion**
- Facebook Business Miner
- Agent dispatcher with background execution
- Configuration system (niche_definitions + region_profiles)

### **Week 3: Intelligence Layer**
- All Tier1 miners operational
- Advanced deduplication agent
- Natural language query processor

### **Week 4: Full Pipeline**
- All support miners active
- Analytics and optimization engine
- Comprehensive testing and validation

---

## 🎯 CONTEXT FROM N01 VALIDATED RESEARCH

**N01 Testing Results Summary:**
- **Google Maps Browser**: 95% eficácia, dados mais completos
- **Facebook Business**: 95% eficácia, 10 novos businesses descobertos
- **CEP Micro-Geography**: 90% eficácia, reveals hidden businesses  
- **Yellow Pages**: 90% eficácia, telefones validados
- **Total**: 50+ businesses descobertos em 2 horas teste (só São Bernardo)

**Market Size Estimates:**
- São Bernardo: 1,200+ businesses missing (atual: 32, esperado: 200-300)
- Santo André: 1,100+ businesses missing (atual: 29, esperado: 150-250)
- São Caetano: 14+ businesses missing (atual: 76, esperado: 90-120)

**Proven Techniques Ready for Implementation:**
- Browser automation via FIRECRAWL ✅ tested
- Background agents via Agent tool ✅ validated
- Cross-source data fusion ✅ patterns identified
- Context-based optimization ✅ density patterns confirmed

---

## 💎 QUALITY REQUIREMENTS

- **8F Pipeline Compliance**: All artifacts follow F1-F8 validation
- **Brand Integration**: Auto-inject GATO³ context via brand_config.yaml
- **Error Handling**: Graceful degradation when APIs/sources fail  
- **Logging**: Comprehensive execution tracking for optimization
- **Security**: API keys management + rate limiting compliance
- **Performance**: Parallel execution + resource optimization

---

**N03: BUILD THIS ULTIMATE BUSINESS DISCOVERY ENGINE**

**Expected Result**: 
- 90%+ market coverage improvement
- 6-9x discovery yield vs manual methods  
- Context-aware adaptability for any niche/region
- Background parallel execution for maximum efficiency
- Learning system that improves performance over time

**This will be the most advanced business discovery system built - proven by real testing, designed for infinite extensibility!** 🎯

**Commit message**: "[N03] Advanced Business Discovery Pipeline — 15 modules, context-aware, 6-9x validated ROI"