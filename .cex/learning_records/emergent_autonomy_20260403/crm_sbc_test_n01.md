# CRM Research Pipeline Test — São Bernardo do Campo

**Mission:** Execute automated CRM research pipeline on SBC as proof-of-concept

**Context:** Testing N03-built workflow `p12_wf_crm_research_pipeline` before scaling to 10+ Ring 2 cities

## 🎯 **WORKFLOW PARAMETERS**

### **Geography**
- **Target city:** São Bernardo do Campo, SP
- **Region:** ABC Paulista (Ring 1)  
- **Area:** 408.45 km²
- **Expected density:** 0.89 biz/km² (vs SCS 4.97/km²)
- **Expected businesses:** 35-45

### **Segments** 
Priority order for SBC discovery:
1. **pet_shop** — traditional pet stores
2. **banho_tosa** — grooming services  
3. **clinica_vet** — veterinary clinics
4. **hospital_24h** — 24h emergency vets
5. **ong** — pet NGOs/shelters

### **Depth**
- **Ring classification:** Ring 1 (high priority)
- **Contact completion target:** 60%+
- **Source diversity:** 4+ per business
- **Validation level:** Full (CNPJ + phone + email)

## 🔧 **PIPELINE EXECUTION**

**Workflow:** `P12_orchestration/compiled/p12_wf_crm_research_pipeline.yaml`

**Wave Structure:**
- **Wave 0:** N01 web research → collect raw businesses
- **Wave 1:** N05 validation + N06 scoring (parallel)  
- **Wave 2:** N04 CRM structuring + KCs
- **Wave 3:** N07 consolidation + commit

**Expected output:** `N04_knowledge/output/crm_structured_sbc.md`

## 🎯 **SUCCESS CRITERIA**

### **Quantitative:**
- **35+ businesses** discovered in SBC
- **60%+ contact completion** (phone/email/WhatsApp)
- **<2h total** execution time (5-wave pipeline)
- **95%+ CNPJ validation** rate

### **Qualitative:**
- Pipeline executes autonomously (no manual intervention)
- Cross-nucleus data flow works correctly
- Output format matches CRM standard
- Gemini nuclei (N01, N04) consolidate properly

## 🚀 **POST-EXECUTION**

After workflow completion:
1. Validate output quality vs. manual SCS research
2. Measure performance metrics vs. targets
3. Document pipeline improvements for Ring 2 scaling  
4. Archive SBC as template for remaining ABC cities

**Next cities after SBC validation:** Diadema → Mauá → Ribeirão Pires

---
**Scope:** crm_sbc_test  
**Priority:** High (proof-of-concept)  
**Estimated time:** 90-120 minutes (full 5-wave cycle)