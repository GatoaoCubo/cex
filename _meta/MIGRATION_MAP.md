# MIGRATION MAP — codexa-core → CEX
## Wave 4 Classification | Generated 2026-03-22 | PYTHA

> Base: ~9916 MD files in codexa-core
> Method: full count + 30-sample KC + 20-sample agent/skill + infra audit
> Status: CLASSIFICATION COMPLETE — ready for Wave 5 migration execution

---

## SUMARIO EXECUTIVO

| LP | Nome | Arquivos | Acao |
|----|------|----------|------|
| P01 | Knowledge | 667 | migrate (519) + archive (148) |
| P02 | Model/Agents | 2563 | migrate (2558) + review (5) |
| P03 | Prompt | 1051 | migrate (638) + archive (413) |
| P04 | Tools/Skills | 128 | migrate (128) |
| P08 | Architecture | ~133 | migrate |
| P09 | Config | ~57 | migrate |
| P10 | Memory | ~55 | migrate |
| P11 | Feedback | ~47 | migrate |
| P12 | Orchestration | ~499 | migrate (handoffs = archive after exec) |
| ARCHIVE | low_quality | ~561+ | archive |
| INVESTIGATE | unclassified | ~4596 | audit Wave 5 |
| **TOTAL** | | **~9916** | |

---

## P01 — KNOWLEDGE (667 arquivos)

### Sub-tipos Identificados (amostra: 30 KCs)

| LP | Tipo | Contagem | Fonte | Acao | Exemplos |
|----|------|----------|-------|------|---------|
| P01 | knowledge_card (domain) | ~290 | records/pool/knowledge/KC_* (domain=research/knowledge/marketing) | migrate | KC_SHAKA_090, KC_EDISON_027, KC_LILY_010 |
| P01 | knowledge_card (meta) | ~170 | records/pool/knowledge/KC_* (domain=meta, KC_SESSION_*) | migrate | KC_PYTHA_088, KC_PYTHA_227, KC_SESSION_20260228 |
| P01 | research_note | ~75 | records/pool/knowledge/KC_*_RESEARCH_*, *_PESQUISA_* | migrate | KC_PYTHA_001, KC_PYTHA_PESQUISA_ONTOLOGY |
| P01 | reference_card | ~55 | records/pool/knowledge/ (quick-ref, pitch, index) | migrate | KC_YORK_TCG_GRADING, KC_PYTHA_135_ELEVATOR_PITCH |
| P01 | few_shot_example | ~5 | records/pool/knowledge/KC_*_USAGE_EXAMPLE* | migrate | KC_PYTHA_065_USAGE_EXAMPLE |
| P01 | rag_source (brand) | ~9 | records/pool/knowledge/brand_codexa/ | migrate | KC_PYTHA_004_CODEXA_POSICIONAMENTO |
| P01 | context_doc (generated) | ~10 | records/pool/knowledge/generated/ | migrate | KC_SHAKA_006_SESSION_METRICS |
| ARCHIVE | low_quality | ~53 | records/pool/knowledge/KC_* (quality_score < 7) | archive | (quality_score: 1-6, stub KCs) |

**Notas de classificacao:**
- 300 KCs com `domain: meta` → maioria knowledge_card (meta), ~20% sao reference_card
- 58 com `domain: research` → research_note (70%) ou knowledge_card (30%)
- 96 `domain: marketing` → knowledge_card (domain) com foco em copy/conversao
- 428 KCs com quality >= 9.0 — candidatos prioritarios para migracao Wave 5
- 148 KCs com quality < 7.0 — archive imediato (nao migrar)
- .json KC files (KC_LAUNCH_PATTERNS_CPL_2025.llm.json): tratar como context_doc

---

## P02 — MODEL / AGENTS (2563 arquivos)

### Agents (125 diretorios, 2216 MDs totais)

| LP | Tipo | Contagem | Fonte | Acao | Notas |
|----|------|----------|-------|------|-------|
| P02 | agent (completo, iso>=10) | 120 dirs | records/agents/*/iso_vectorstore/ | migrate | Todos os 20 sampled tinham 10-11 ISOs |
| P02 | agent (stub, iso<5) | 5 dirs | records/agents/* (iso_vectorstore vazio) | review | Avaliar se promover ou arquivar |
| P02 | agent (golden, iso>=17) | 6 dirs | records/agents/* (iso>=17 files) | migrate + P07 | security_scanner(20), postgres_pro(18), etc. |
| P02 | mental_model | ~7 | records/agents/*/mental_model.yaml | migrate → P10 | Cruzam com P02+P10 |

### Satellites (347 MDs em records/satellites/)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P02 | boot_config + mental_model | ~140 | records/satellites/*/PRIME_*.md | migrate |
| P08 | satellite_spec | ~7 | records/satellites/*/mental_model.yaml | migrate → P08 |
| P02 | agent (satellite instance) | ~200 | records/satellites/*/iso_vectorstore/ | migrate |

**Metricas agents:**
- ISO baseline (10 files): 120 agents (96%) — 100% baseline ISO coverage
- ISO maduro (>=17 files): 6 agents (5%) — golden candidates
- Stubs (<5 ISO): 5 agents (4%) — revisar antes de migrar
- Media ISO por agent: ~17.7 MDs totais por dir

---

## P03 — PROMPTS / TEMPLATES (1051 arquivos)

| LP | Tipo | Contagem | Fonte | Acao | Notas |
|----|------|----------|-------|------|-------|
| P03 | action_prompt | ~251 | records/pool/prompts/ (HOP_ nao-archive) | migrate | HOP ativo em subdirs: edison/, lily/, shaka/, etc. |
| P03 | prompt_template | ~120 | records/ (TPL_* files) | migrate | Incluem TPL de agents + satellites |
| P03 | prompt_template (ISO output) | ~124 | records/agents/*/iso_vectorstore/*OUTPUT_TEMPLATE* | migrate | Um por agent = baseline |
| P03 | system_prompt | ~50 | records/ (system-level, boot prompts) | migrate | .claude/rules/ parcialmente |
| P03 | chain | ~27 | records/pool/prompts/ (HOPs multi-step) | migrate | HOP_PYTHA_003_HYBRID_RAG, etc. |
| P03 | instruction | ~66 | records/agents/*/blocks/ + AGT_*_TEMPLATES | migrate | blocks/ subdirs em agents/ |
| ARCHIVE | executed_output | ~263 | records/pool/prompts/_archive/research/*EXECUTED_OUTPUT* | archive | Outputs de execucao, nao templates |
| ARCHIVE | test_artifact | ~150 | records/pool/prompts/_archive/*TEST_ARTIFACT* | archive | Artefatos de teste, nao reutilizaveis |

**Notas:**
- 51% dos 700 HOPs = archive (executed_output + test_artifact)
- 49% dos HOPs = action_prompt reutilizavel
- ISO_*_OUTPUT_TEMPLATE = prompt_template estruturado (1 por agent)
- TPL_ prefix = templates formais com {{MUSTACHE}} vars

---

## P04 — TOOLS / SKILLS (128 arquivos)

| LP | Tipo | Contagem | Fonte | Acao | Notas |
|----|------|----------|-------|------|-------|
| P04 | skill | 128 | records/skills/*/SKILL.md | migrate | 1 SKILL.md por skill dir |
| P04 | skill (golden, quality>=9) | ~15 | records/skills/* (metricas reais documentadas) | migrate + P07 | spawn_solo, continuous_batching, etc. |

**Notas:**
- 128 skill dirs com 1 SKILL.md cada (single-file structure)
- Sem ISO structure (diferente de agents)
- 4 dirs podem ter 0 MDs — verificar antes de migrar
- Skills com metricas reais (confidence 2x per CODEX insight)

---

## P07 — EVALS (estimativa)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P07 | unit_eval | ~30 | records/core/tests/ | migrate |
| P07 | golden_test | ~6 | records/agents/* (iso>=17) + KC quality>=9.5 | migrate |
| P07 | smoke_eval | ~15 | records/core/tests/ + records/framework/docs/ | migrate |
| P07 | scoring_rubric | ~5 | records/core/ + CODEX density tiers | migrate |

---

## P08 — ARCHITECTURE (~133 arquivos)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P08 | law | ~15 | records/framework/docs/LAWS_v3_PRACTICAL.md + records/obsidian-publish/laws/ | migrate |
| P08 | pattern | ~40 | records/framework/docs/*PATTERN* + records/core/ | migrate |
| P08 | satellite_spec | ~20 | records/satellites/*/PRIME_*.md (spec sections) | migrate |
| P08 | diagram | ~18 | records/framework/docs/*ARCHITECTURE*, *DIAGRAM* | migrate |
| P08 | component_map | ~40 | records/framework/docs/ + records/core/docs/ | migrate |

---

## P09 — CONFIG (~57 arquivos)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P09 | runtime_rule | ~10 | .claude/rules/ (encoding.md, navigation.md, etc.) | migrate |
| P09 | permission | ~7 | .claude/rules/ (boot-autonomy-flags.md, multi_repo.md) | migrate |
| P09 | path_config | ~15 | records/framework/docs/ (KEY_PATHS, SPAWN_PLAYBOOK) | migrate |
| P09 | env_config | ~15 | records/core/config/ + records/framework/ | migrate |
| P09 | feature_flag | ~10 | records/core/ feature flags + .claude/settings.json | migrate |

---

## P10 — MEMORY (~55 arquivos)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P10 | mental_model | ~10 | .claude/mental_models/*.yaml + records/satellites/*/mental_model.yaml | migrate |
| P10 | brain_index | ~15 | records/core/brain/ (index files, audit docs) | migrate |
| P10 | learning_record | ~25 | records/core/learning/ + .claude/rules/codexa-learning.md | migrate |
| P10 | axiom | ~5 | .claude/mental_models/laws.yaml + CODEX MANDAMENTOS | migrate |

---

## P11 — FEEDBACK (~47 arquivos)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P11 | quality_gate | ~15 | records/core/ + records/framework/docs/ (quality rules) | migrate |
| P11 | lifecycle_rule | ~12 | records/framework/docs/ + records/core/learning/ | migrate |
| P11 | guardrail | ~10 | records/framework/docs/ + .claude/rules/STELLA_RULES.md | migrate |
| P11 | bugloop | ~5 | records/core/ bugloop configs | migrate |
| P11 | optimizer | ~5 | records/core/ optimizer scripts | migrate |

---

## P12 — ORCHESTRATION (~499 arquivos)

| LP | Tipo | Contagem | Fonte | Acao |
|----|------|----------|-------|------|
| P12 | handoff | 443 | .claude/handoffs/*.md | archive-after-exec (executados) / migrate (templates) |
| P12 | spawn_config | ~6 | records/framework/powershell/*.ps1 | migrate |
| P12 | workflow | ~30 | records/core/workflows/ + records/framework/docs/ | migrate |
| P12 | dag | ~10 | records/core/workflows/ (dependency chains) | migrate |
| P12 | dispatch_rule | ~10 | records/framework/docs/ + .claude/rules/STELLA_RULES.md | migrate |

**Nota handoffs:** 443 handoffs em .claude/handoffs/ sao instrucoes de execucao por satelite.
- Handoffs completados (signal presente) → archive
- Handoff templates reusaveis → migrate como P12 handoff
- Estimativa: ~50 templates + ~393 executados (archive)

---

## ARCHIVE — Low Quality & Obsolete (~561+ arquivos)

| Categoria | Contagem | Fonte | Criterio |
|-----------|----------|-------|----------|
| KC low quality | 148 | records/pool/knowledge/ | quality_score < 7.0 |
| HOP executed outputs | 263 | records/pool/prompts/_archive/research/*EXECUTED_OUTPUT* | outputs, nao templates |
| HOP test artifacts | 150 | records/pool/prompts/_archive/*TEST_ARTIFACT* | testes, nao reutilizaveis |
| Handoffs executados | ~393 | .claude/handoffs/ (com signal complete) | missao completa |

---

## INVESTIGATE — Unclassified (~4596 arquivos)

Arquivos ainda nao contabilizados nos buckets acima:

| Origem | Estimativa | Prioridade | Acao |
|--------|-----------|-----------|------|
| records/obsidian-publish/ | ~500 | LOW | audit — mostly duplicates of KC/laws |
| records/core/ (nao classificados) | ~300 | MEDIUM | audit — reports, outputs, misc |
| records/framework/ (nao classificados) | ~400 | MEDIUM | audit — scaffold, brain, python |
| records/pool/ (nao-KC, nao-prompt) | ~800 | HIGH | audit — FAT, ADW, other pool types |
| records/ (outros subdirs) | ~2596 | LOW | audit — atlas_inbox, misc |

**Acao recomendada Wave 5:** PYTHA executa audit pass em cada origem INVESTIGATE.

---

## GOLDEN CANDIDATES (quality >= 9.5)

Pre-identificados para P07 golden_test e pool prioritario:

| Arquivo | LP | Tipo | Quality | Satelite |
|---------|-----|------|---------|---------|
| KC_EDISON_027_LLM_SECURITY_GUARDRAILS | P01 | knowledge_card | 9.5 | EDISON |
| KC_PYTHA_001_AUDIO_TTS_PROVIDERS | P01 | research_note | 10.0 | PYTHA |
| KC_PYTHA_088_CODEXA_DEPLOY_ARCHITECTURE | P01 | knowledge_card (meta) | 10.0 | PYTHA |
| KC_SHAKA_049_KNOWLEDGE_CARD | P01 | reference_card | 10.0 | SHAKA |
| KC_PYTHA_PESQUISA_ONTOLOGY_DESIGN | P01 | research_note | 9.2 | PYTHA |
| security_scanner (agent) | P02 | agent | ~9.5 | ATLAS |
| postgres_pro (agent) | P02 | agent | ~9.0 | ATLAS |
| continuous_batching (skill) | P04 | skill | ~9.0 | STELLA |
| spawn_solo (skill) | P04 | skill | ~9.0 | STELLA |

**Total goldens estimados:** 428 KCs quality>=9 + 6 agents golden + ~15 skills = ~449 candidatos

---

## PLANO DE EXECUCAO — Wave 5

### Ordem recomendada (por impacto + volume)

```
Wave 5.1 (PYTHA): Migrate P01 KCs (519 quality>=7)
Wave 5.2 (PYTHA): Migrate P03 Prompts (638 active)
Wave 5.3 (PYTHA): Migrate P04 Skills (128)
Wave 5.4 (EDISON): Migrate P02 Agents (125 dirs)
Wave 5.5 (PYTHA): Migrate P08-P12 Infra (~339)
Wave 5.6 (PYTHA): Audit INVESTIGATE (~4596)
Wave 5.7 (ALL): Archive pass (clean .claude/handoffs/ + low-quality)
```

### Scripts sugeridos
```bash
# Contar por bucket antes de migrar
find records/pool/knowledge -name "KC_*" -newer _meta/MIGRATION_MAP.md | wc -l

# Verificar quality gate antes de migrate
grep -l "quality_score: [0-6]" records/pool/knowledge/KC_*.md | wc -l

# Lista de stubs para review
for d in records/agents/*/; do
  c=$(find "$d/iso_vectorstore" -name "*.md" 2>/dev/null | wc -l)
  [ "$c" -lt 5 ] && echo "$d: iso=$c"
done
```

---

*MIGRATION_MAP v1.0 | PYTHA | Wave 4.1 Classification | 2026-03-22*
*Base: codexa-core ~9916 MD files | Method: count + 30-sample KC + 20-sample agent/skill*
