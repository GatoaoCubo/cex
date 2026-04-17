---
id: n05_audit_threat_model_builder
kind: audit_report
pillar: P11
title: "Audit: threat-model-builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: n05_ops
domain: security_operations
quality: 8.9
tags: [threat_model, audit, stride, mitre, n05]
tldr: "6 pass, 7 fix (no rebuilds) -- primary gaps: output template missing STRIDE structure, quality gate ID pattern mismatch, weights summed to 0.90"
---

## Summary

| ISO | Score Before | Score After | Action |
|-----|-------------|------------|--------|
| bld_instruction_threat_model | 7.5 | 9.0 | FIX: Added explicit 6-step STRIDE procedure, CVSS scoring, AI-specific attacks |
| bld_system_prompt_threat_model | 8.5 | 8.5 | PASS |
| bld_knowledge_card_threat_model | 8.5 | 8.5 | PASS |
| bld_quality_gate_threat_model | 6.5 | 9.0 | FIX: H02 ID pattern corrected (THREAT-XXXX -> p11_tm_*), weights fixed (0.90->1.00), H04 changed to STRIDE gate, H08 added (framework citation) |
| bld_output_template_threat_model | 5.5 | 9.0 | REBUILD: Full STRIDE matrix template with likelihood/impact, CVSS, MITRE technique IDs, AI addendum |
| bld_schema_threat_model | 7.5 | 8.5 | FIX: Body structure updated to match new STRIDE template sections |
| bld_examples_threat_model | 7.5 | 9.0 | FIX: Golden example rebuilt with STRIDE tables, CVSS scores, MITRE technique IDs, ATLAS addendum |
| bld_manifest_threat_model | 8.0 | 8.0 | PASS |
| bld_architecture_threat_model | 7.0 | 8.5 | FIX: Removed CEX-trading language, added P11 pillar positioning and downstream builder relationships |
| bld_collaboration_threat_model | 8.0 | 8.0 | PASS |
| bld_config_threat_model | 8.0 | 8.0 | PASS |
| bld_memory_threat_model | 8.0 | 8.0 | PASS |
| bld_tools_threat_model | 7.5 | 8.5 | FIX: Removed nonexistent cex_analyzer/cex_exporter/val_* tools; added OWASP Threat Dragon, MITRE ATT&CK Navigator, CVSS calculator |

**Total: 6 pass, 7 fixed, 0 rebuilt**

## Framework Coverage

| Framework | Referenced In | Citation Quality |
|-----------|--------------|-----------------|
| STRIDE | instruction, quality_gate, output_template, examples, schema, manifest | Procedural (step-by-step) |
| MITRE ATT&CK | system_prompt, knowledge_card, manifest, output_template, examples, tools | Technique IDs in examples |
| MITRE ATLAS | output_template, examples, knowledge_card | AI-specific techniques (AML.T*) |
| NIST AI RMF | knowledge_card, instruction, output_template | Framework function references |
| ISO/IEC 23894 | system_prompt, knowledge_card | Standard name only |
| NIST SP 800-160 | knowledge_card, output_template | References |
| CVSS | quality_gate, output_template, examples | Scoring method |
| OWASP | tools | External tool reference |

## Top 5 Security Gaps Found

1. **Output template had no STRIDE structure** -- a threat_model builder that doesn't enforce STRIDE is worse than useless. Rebuilt with full 6-category matrix.
2. **Quality gate ID pattern contradicted schema** -- H02 used `THREAT-XXXX` format while schema defined `^p11_tm_*`. All artifacts would fail H02 as soon as they were created.
3. **Weight sum error** -- soft scoring dimensions summed to 0.90 not 1.00. Scoring was systematically biased downward.
4. **No MITRE ATLAS coverage** -- AI-specific threat techniques (data poisoning, model inversion, adversarial examples) were mentioned in knowledge_card but not surfaced in the quality gate, output template, or examples as mandatory items.
5. **Tools referenced nonexistent executables** -- cex_analyzer.py, cex_exporter.py, val_checker.py, val_simulator.py do not exist in cex_sdk. Would mislead builders attempting to run validation.

## Recommendations

- Create `kc_stride_methodology.md` in P01_knowledge/library for shared STRIDE reference
- Consider adding `threat_model` to the AI Act Art. 9 compliance mapping (it IS a requirement for high-risk AI systems)
- Add a quality gate check: "Does this threat model cover all assets listed in the architecture diagram?" (traceability gate)
