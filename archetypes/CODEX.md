# RECORDS CODEX -- Universal Meta-Construction Bible
## v6.0.0 | CEX DNA | LIVING | Updated with real data

---

## 0. PURPOSE
CEX DNA. Hierarchy: CODEX > _schema > _generator > templates > instances
Built from data of 9910 MD files, 783 golden, 42KB of distillation.

## 1. VARIABLES
- Tier 1: {{MUSTACHE}} = template engine resolves at generation
- Tier 2: [BRACKET] = human/agent resolves at authoring
- {{BRAND_UPPER}} = York fills on fork
- ${ENV_VAR} = system fills at runtime
- __auto__ = lifecycle fills automatically
- NEVER {single_curly} (deprecated) nor [PLACEHOLDER]

## 2. UNIVERSAL ANATOMY
YAML front: id, type, lp, quality, keywords(3+), long_tails(2+), bullets(3+), axioms(1+)
MD body: title, summary 1-line, sections by type (see meta-template)
Density >= 0.8 mandatory. Max 4KB (adjusted from 2KB based on data).
Prose > 3 lines forbidden. Bullets with max 80 chars.
Dual: every artifact .md has compiled/ counterpart (.yaml or .json per machine_format).

## 3. NAMING
Pattern: {lp}_{type}_{topic}.{ext}
Ex: p01_kc_ecommerce_br.md + .yaml (dual)
Rules: lowercase, snake_case, ASCII, max 50 chars

## 4. DIRECTORIES
Brain: P01-P12 (each with _schema.yaml, _generator.md, templates/, examples/)
Agent_groups: agent_groups/{name}/P01-P12 (real instances)
Meta: archetypes/ (CODEX, GLOSSARY, MANDAMENTOS, ROADMAP, META_TEMPLATE)

## 5. SCHEMAS = _schema.yaml per pillar
12 schemas created (78 kinds total). Validated in pre-commit.
Standard fields: max_bytes, quality_min, frontmatter_required, body_structure
Mandatory field v3.0: `machine_format` (yaml|json) -- defines compiled/ format.

## 6. GENERATORS = _generator.md per pillar
12 generators created (P01-P12 CORE+QUALITY+SCALE). Step-by-step instructions.
Anti-patterns listed. Density tiers documented.

## 7. META-TEMPLATE = archetypes/META_TEMPLATE.md
Template that generates templates. Shokunin: evolves during use.
Sections by type documented. Generation rules defined.

## 8. DUAL OUTPUT = .md (human) + .yaml/.json (machine)
Every artifact = 2 files. Exceptions: _schema (yaml only), _generator (md only)
Mandatory field in _schema.yaml: `machine_format` (yaml|json). 78 kinds: 64 yaml, 9 json.
Rule: every example MUST have compiled version in compiled/.
Compile: `python _tools/cex_compile.py --all` generates compiled/ in each pillar.
Routing: archetypes/DECISION_MAP.md (file -> pillar -> type -> format).

## 9. LIFECYCLE
CREATE > INDEX > READ > USE > RESULTS > NEW KC > repeat (flywheel)
ARCHIVE: quality<7 + age>30d. PROMOTE: used>10x + quality>9

## 10. DENSITY (REAL DATA)

| Tier | Density | Example |
|------|---------|---------|
| Elite | 90-95% | KC_knowledge_agent_069 (domain, YAML blocks, ASCII flow) |
| High | 80-88% | KC_knowledge_agent_358 (spec table, code examples) |
| Standard | 70-78% | KC_builder_agent_029 (good structure, some prose) |
| Low | <65% | REJECT or redo |

## 11. DISTILLATION INSIGHTS
- 98% golden have YAML frontmatter
- 82% golden have 5+ bullets (bullets correlate with quality)
- 99% lack keywords (biggest gap in organization-core)
- Semantic Bridge in 60% of golden templates (boosts retrieval)
- ISO count = agent maturity (10=baseline, 17=mature, 22+=golden)
- Skills with real metrics have 2x confidence vs without data
- 2 KC sub-templates: Domain (density 92%) vs Meta (density 88%)

## 12. ANTI-FRAGILITY
68 CORE fixed + _custom/ extensible. Promotion: 10x+quality>8=CORE.

## 13. FINAL STATE (v1.0.0 -- 2026-03-22)

| pillar | Schema | Generator | Templates | Examples | Completeness |
|----|--------|-----------|-----------|----------|------------|
| P01 Knowledge | YES | YES | 3 | 7 | CORE complete |
| P02 Model | YES | YES | 1 | 4 | CORE complete |
| P03 Prompt | YES | YES | 1 | 4 | CORE complete |
| P04 Tools | YES | YES | 1 | 3 | CORE complete |
| P05 Output | YES | YES | 1 | 0 | template only |
| P06-P12 | YES x7 | YES x7 | 0 | 0 | generator only |
| **Total** | **12** | **12** | **7** | **18** | v1.0.0 |

**Cumulative Metrics (6 Waves):**
- Wave 1: 42KB distilled, P01 schema v0, 1 golden example
- Wave 2: 12 schemas, 78 kinds, CORE+QUALITY+SCALE layers
- Wave 3: 12 generators, 7 templates, 18 examples, chain test PASS
- Wave 4: migration map (9916 files), 12 golden migrated, 22 candidates
- Wave 5: density report 88.6%, 3 validators, meta-docs v3
- Wave 6: bootstrap CLI, dogfood, ARCHITECTURE+CONTRIBUTING+CHANGELOG, v1.0 docs

## 14. DECISION HISTORY

| Wave | Decision | Reason |
|------|----------|--------|
| W1 | Max file size = 4KB (not 2KB) | Real data: golden avg ~3KB, 2KB truncated information |
| W1 | Dual output .md + .yaml | .md = human reading, .yaml = LLM embedding optimized |
| W2 | 12 LPs (not 8 or 16) | Complete coverage without overlap: P01-P04 CORE = sufficient for 95% of cases |
| W2 | 78 fixed kinds + _custom/ extensible | Schema stability + flexibility for specific domains |
| W3 | Meta-template before templates | Templates derived from meta = guaranteed consistency (DRY) |
| W3 | Generator ONLY for primary type | Secondary kinds: schema defines, human interpolates. Generates more types, less overhead |
| W4 | Migration map first, migrate after | Classifying 9916 files before migrating avoids reclassification rework |
| W4 | 12 golden first (not 638) | Quality > quantity. 12 perfect teach more than 638 mediocre |
| W5 | Density >= 0.80 mandatory (not 0.75) | Data: all 18 examples scored above 0.85. 0.80 = real floor |
| W5 | Elite = 0.90+ (not 0.95+) | 0.95 = only 1 example. 0.90 = 6 examples = healthy tier |
| W6 | Bootstrap CLI before mass migration | CLI lets any repo use CEX; mass migration = only organization-core |

## 15. CONSOLIDATED PRINCIPLES (6 Waves)

| # | Principle | Origin |
|---|-----------|--------|
| 1 | Density > volume | W1: 783 golden > 9127 mediocre |
| 2 | Schema first, generator second | W2-W3: schema = contract, generator = instruction |
| 3 | Real data beats estimates | W1: 4KB (not 2KB), 0.88 avg (not 0.75 assumed) |
| 4 | Flywheel: CEX generates CEX | W6: dogfood = framework self-applies its own principles |
| 5 | 12 perfect > 638 mediocre | W4: golden migration prioritizes quality over coverage |
| 6 | Meta-template = source of truth | W3: every template inconsistency = misalignment with META_TEMPLATE |
| 7 | Bullets with 80 chars = fast scan | W3: density analysis proved bullet-quality correlation |
| 8 | id == filename stem (always) | W3: chain test revealed silent inconsistencies without this rule |
| 9 | _custom/ for domains, CORE fixed | W5: anti-fragility = 78 stable kinds + isolated extensions |
| 10 | Validate early, validate often | W3: chain test before scaling prevented error propagation |

---
*CODEX v6.0.0 | 2026-03-27*