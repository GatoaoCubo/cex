---
kind: quality_gate
id: p11_qg_interface
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of interface artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Interface"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, interface, contract, bilateral, integration, versioning, compatibility]
tldr: "Gates ensuring interface artifacts define complete bilateral contracts with typed methods, versioning strategy, backward compatibility guarantees, and mock specs."
domain: "interface — bilateral integration contracts defining methods, I/O schemas, versioning, and compatibility between agents"
created: "2026-03-27"
updated: "2026-03-27"
density_score: 0.92
related:
  - bld_instruction_interface
  - p11_qg_input_schema
  - p11_qg_agent_computer_interface
  - p10_lr_interface_builder
  - bld_knowledge_card_interface
  - p11_qg_handoff
  - p03_sp_interface_builder
  - p11_qg_instruction
  - bld_examples_interface
  - bld_architecture_interface
---

## Quality Gate

# Gate: Interface
## Definition
| Field     | Value |
|-----------|-------|
| metric    | weighted soft score + all hard gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.5 for golden |
| operator  | AND (all hard) + weighted average (soft) |
| scope     | any artifact with `kind: interface` |
## HARD Gates
All must pass. Any failure = immediate reject.
| ID  | Check | Fail Condition |
|-----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches `^[a-z][a-z0-9_-]+$` | Uppercase, spaces, or leading digit |
| H03 | ID equals filename stem | `id: agent_a_b` in file `agent_b_c.md` |
| H04 | Kind equals literal `interface` | Any other kind value |
| H05 | Quality field is `null` | Any non-null value |
| H06 | All required fields present | Missing: methods, provider, consumer, or version |
| H07 | Every method has both `input` and `output` defined | Any method with only one side defined |
| H08 | `provider` and `consumer` are distinct identifiers | Same value in both fields |
| H09 | `version` follows semver (`^\d+\.\d+\.\d+$`) | Non-semver version string |
| H10 | At least one method defined | Empty or missing methods list |
## SOFT Scoring
Total weights sum to 100%.
| ID  | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|-----|-----------|--------|--------|-------|-------|
| S01 | Type precision | 1.0 | All method inputs and outputs use typed field definitions | Typed but incomplete coverage | Untyped — described in prose only |
| S02 | Backward compatibility | 1.0 | Compatibility policy stated (breaking vs non-breaking changes defined) | Policy mentioned but vague | No compatibility statement |
| S03 | Versioning strategy | 1.0 | Version bump rules documented (what triggers major/minor/patch) | Semver used but bump rules absent | No versioning guidance |
| S04 | Deprecation path | 0.5 | Deprecated methods marked + migration path to replacement provided | Deprecated methods marked, no migration | No deprecation policy |
| S05 | Error contract | 1.0 | Error responses typed per method (error codes, shapes) | Generic error response defined | No error contract |
| S06 | Mock specification | 1.0 | Mock inputs and expected outputs for at least 2 methods | One method has mock data | No mock spec |
| S07 | Bilaterality enforced | 1.0 | Both provider and consumer roles clearly scoped; no unilateral creep | Mostly bilateral with minor leakage | Reads as a unilateral input schema |
| S08 | Method naming | 0.5 | Method names use verb_noun pattern (e.g., `get_status`, `send_result`) | Names present but inconsistent | Arbitrary names |
| S09 | Timeout and SLA | 0.5 | Expected response time or SLA documented per method | Overall SLA present, not per-method | None |
| S10 | Signal distinction | 0.5 | Interface defines synchronous request-response, not fire-and-forget | Mostly clear | Indistinguishable from a signal |
**Score = sum(pts * weight) / sum(max_pts * weight) * 10**
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Golden | Publish to pool as golden integration contract |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |
## Bypass
| Field | Value |
|-------|-------|
| Conditions | Prototyping integration between two new agents where final method signatures are not yet known |
| Approver | Both provider and consumer team leads |

## Examples

# Examples: interface-builder
## Golden Example
INPUT: "Define o contrato between researcher (research) e marketer (marketing) for entrega de research results"
OUTPUT:
```yaml
id: p06_iface_research_to_marketing
kind: interface
pillar: P06
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
contract: "Research results delivery from researcher to marketer"
provider: "researcher"
consumer: "marketer"
methods:
  - name: "get_research_summary"
    input: {topic: string, max_sources: integer}
    output: {summary: string, sources: list, confidence: float}
    description: "Returns distilled research summary with sources and confidence score"
  - name: "get_competitor_data"
    input: {competitor_name: string, marketplace: string}
    output: {pricing: object, listings: list, rating: float}
    description: "Returns structured competitor data for a specific marketplace"
backward_compatible: true
deprecation: null
mock:
  enabled: true
  example_payloads:
    - method: "get_research_summary"
      input: {topic: "decoraction minimalist", max_sources: 5}
      output: {summary: "Tendencia crescente em 2026...", sources: ["url1", "url2"], confidence: 0.87}
domain: "agent_group-integration"
quality: null
tags: [interface, shaka, lily, research, marketing, agent_group-integration]
tldr: "Bilateral contract for researcher to deliver research results to marketer marketing workflows."
density_score: 0.91
```
## Contract Definition
researcher (research agent_group) provides structured research data to marketer (marketing agent_group).
marketer calls methods to get research summaries and competitor data for marketing campaigns.
## Methods
| # | Name | Input | Output | Description |
|---|------|-------|--------|-------------|
| 1 | get_research_summary | {topic, max_sources} | {summary, sources, confidence} | Distilled research with sources |
| 2 | get_competitor_data | {competitor_name, marketplace} | {pricing, listings, rating} | Structured competitor intel |
## Versioning
- **Version**: 1.0.0
- **Backward compatible**: yes
- **Changes from previous**: initial release
- **Migration notes**: none
## Mock Specification
```json
{
  "method": "get_research_summary",
  "input": {"topic": "decoraction minimalist", "max_sources": 5},
  "output": {"summary": "Tendencia crescente em 2026...", "sources": ["url1", "url2"], "confidence": 0.87}
}
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p06_iface_ pattern (H02 pass)
- kind: interface (H04 pass)
- 15+ required fields present (H06 pass)
- methods has 2 entries with name/input/output/description (H07 pass)
- backward_compatible is boolean (H08 pass)
- provider and consumer specified (H09 pass)
- tldr <= 160 chars, dense (S01 pass)
- tags list len >= 3, includes "interface" (S02 pass)
- YAML parses cleanly (H01 pass)
## Anti-Example
INPUT: "Interface between researcher e marketer"
BAD OUTPUT:
```yaml
id: shaka_lily_interface
kind: integration
pillar: Schema
contract: researcher-marketer
methods: "get data from researcher"
backward_compatible: maybe
quality: 9.0
tags: interface
```
researcher sends data to marketer when needed.
FAILURES:
1. id: no `p06_iface_` prefix -> H02 FAIL
2. kind: "integration" not "interface" -> H04 FAIL
3. pillar: "Schema" not "P06" -> H03 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. methods: string instead of list[object] -> H07 FAIL
6. backward_compatible: "maybe" not boolean -> H08 FAIL
7. provider/consumer: missing -> H09 FAIL
8. tags: string not list, len < 3 -> S02 FAIL
9. contract: not descriptive -> S05 FAIL
10. body: filler prose ("when needed") -> S07 FAIL

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
