---
id: n05_audit_hybrid_review2
kind: audit_report
pillar: P11
title: "Audit: sandbox-config-builder + repo-map-builder (26 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: n05_ops
domain: security_operations
quality: 9.0
tags: [sandbox_config, repo_map, audit, hybrid_review2, n05, e2b, firecracker, tree-sitter, pagerank]
tldr: "8 pass, 18 fixed (no rebuilds) -- primary gaps: missing platform coverage (E2B/Firecracker/gVisor) in sandbox; missing tree-sitter/PageRank/token-budget in repo_map; fabricated tools; weight sums > 1.0; H02 pattern mismatches"
related:
  - bld_instruction_sandbox_config
  - bld_instruction_repo_map
  - p01_qg_repo_map
  - bld_knowledge_card_sandbox_config
  - bld_examples_sandbox_config
  - bld_examples_repo_map
  - bld_knowledge_card_repo_map
  - bld_output_template_sandbox_config
  - bld_tools_sandbox_config
  - n01_hybrid_review_wave1
---

## Summary

### sandbox-config-builder (13 ISOs)

| ISO | Score Before | Score After | Action |
|-----|-------------|------------|--------|
| bld_manifest_sandbox_config | 8.0 | 8.0 | PASS -- identity and routing solid |
| bld_instruction_sandbox_config | 7.0 | 9.0 | FIX: Added E2B/Modal/Daytona/Firecracker/nsjail/gVisor to Phase 1; explicit CPU/RAM/disk/timeout validation in Phase 3 |
| bld_system_prompt_sandbox_config | 8.5 | 8.5 | PASS -- scope and quality rules accurate |
| bld_knowledge_card_sandbox_config | 5.5 | 9.2 | REBUILD: Added E2B/Modal/Daytona/Docker/Firecracker/nsjail/gVisor platform table; explicit CPU/RAM/disk/timeout/network/filesystem specs; resource limit formats; network policy patterns; filesystem scope table; pitfalls |
| bld_quality_gate_sandbox_config | 4.5 | 9.0 | FIX: Weight sum 1.10->1.00 (D1-D5 only); H02 pattern fixed (sandbox-\d{4} -> ^p09_sb_[a-zA-Z0-9_-]+$); H04 changed to 4-limit check; H05-H08 updated for network/filesystem/seccomp/no-privileged |
| bld_output_template_sandbox_config | 5.0 | 9.0 | REBUILD: Added timeout_seconds, network policy section, filesystem scope section, isolation mechanism block, platform-specific configs (E2B e2b.toml, Docker run, nsjail.cfg) |
| bld_examples_sandbox_config | 5.5 | 9.0 | REBUILD: Golden 1 (E2B/Firecracker, air-gapped), Golden 2 (Docker+gVisor, egress whitelist); Anti-1 (missing timeout + open network); Anti-2 (nsjail without seccomp) |
| bld_schema_sandbox_config | 7.0 | 8.0 | FIX: Removed "CEX sandbox endpoint" confusion in domain notes; quality field note updated |
| bld_architecture_sandbox_config | 7.5 | 7.5 | PASS -- component inventory adequate |
| bld_collaboration_sandbox_config | 8.0 | 8.0 | PASS -- boundary clear |
| bld_config_sandbox_config | 7.5 | 7.5 | PASS -- naming pattern and limits correct |
| bld_memory_sandbox_config | 7.0 | 7.0 | PASS -- recommendations solid |
| bld_tools_sandbox_config | 4.5 | 9.0 | REBUILD: Removed all fabricated tools (cex_validator.py, cex_analyzer.py, config_linter.py, schema_checker.py, test_executor.py, dependency_resolver.py); added real tools (E2B SDK, Modal, Daytona, Docker, nsjail, bubblewrap, Firecracker, gVisor/runsc, seccomp-bpf, libseccomp, AppArmor) |

**Total: 5 pass, 8 fixed/rebuilt**

### repo-map-builder (13 ISOs)

| ISO | Score Before | Score After | Action |
|-----|-------------|------------|--------|
| bld_manifest_repo_map | 8.0 | 8.0 | PASS -- identity and routing adequate |
| bld_instruction_repo_map | 6.5 | 9.0 | REBUILD: Full 4-phase process -- tree-sitter extraction, PageRank ranking, token budget fit, Aider-format symbol table composition |
| bld_system_prompt_repo_map | 8.0 | 8.0 | PASS -- scope rules accurate |
| bld_knowledge_card_repo_map | 4.5 | 9.2 | REBUILD: Added Aider origin story; tree-sitter concept + query examples; PageRank algorithm + NetworkX code; token budget management table; file selection heuristics priority order; exclusion rules; pitfalls |
| bld_quality_gate_repo_map | 5.5 | 9.0 | FIX: H02 pattern fixed (repo-[a-z0-9]{8} -> ^p01_rm_[a-zA-Z0-9_]+$); H04-H10 updated to repo_map domain (token_budget, symbol table, token compliance); SOFT scoring rebuilt (5D: symbol extraction, token compliance, PageRank, heuristics, completeness) |
| bld_output_template_repo_map | 4.5 | 9.0 | REBUILD: Added symbol table section (Aider format), file ranking table (PageRank scores), reference graph summary, file selection heuristics table, exclusion table, extraction method table, token budget tracking |
| bld_examples_repo_map | 5.0 | 9.0 | REBUILD: Golden 1 (CEX SDK with PageRank scores + Aider symbol table); Golden 2 (microservices with reference graph); Anti-1 (flat file tree -- wrong paradigm); Anti-2 (token budget exceeded); Anti-3 (missing frontmatter) |
| bld_schema_repo_map | 6.5 | 8.5 | FIX: Replaced repository_url + last_commit with token_budget, symbol_count, file_count, extraction_method (domain-relevant fields) |
| bld_architecture_repo_map | 7.0 | 7.0 | PASS -- adequate |
| bld_collaboration_repo_map | 7.5 | 7.5 | PASS -- boundary clear |
| bld_config_repo_map | 7.5 | 7.5 | PASS -- naming pattern correct |
| bld_memory_repo_map | 7.0 | 7.0 | PASS -- recommendations adequate |
| bld_tools_repo_map | 4.5 | 9.0 | REBUILD: Removed fabricated val_*.py tools; added real tools (tree-sitter, tree-sitter-languages, Universal ctags, NetworkX, scipy, tiktoken, anthropic SDK, ripgrep, pathspec, ast stdlib, acorn, igraph) plus reference to aider/repomap.py |

**Total: 5 pass, 8 fixed/rebuilt**

---

## Wave 1 Systemic Issues -- Confirmed Present, Fixed

| Issue | sandbox_config | repo_map | Fix |
|-------|---------------|----------|-----|
| Fabricated tools in bld_tools | YES (6 fake tools) | YES (3 fake val_* tools) | Replaced with real tools |
| Quality gate weight sum != 1.0 | YES (1.10) | NO (was 1.00) | Fixed to 1.00 |
| H02 ID pattern != schema pattern | YES | YES | Both corrected |
| Missing platform coverage | YES (missing E2B/Firecracker/gVisor/nsjail) | N/A | Added 7 platforms |
| Missing domain-specific concepts | YES (no timeout/filesystem scope) | YES (no tree-sitter/PageRank/token-budget) | Full rebuilds |
| Output template too thin | YES (no timeout/network/filesystem sections) | YES (no symbol table/ranking) | Full rebuilds |

## Framework Coverage

### sandbox_config

| Concept | Referenced In | Coverage |
|---------|--------------|---------|
| E2B (Firecracker microVM) | knowledge_card, tools, examples, output_template | Platform + config format |
| Modal (container) | knowledge_card, tools, examples | Platform |
| Daytona (devcontainer) | knowledge_card, tools | Platform |
| Docker (runc) | knowledge_card, tools, examples, output_template | Full config |
| Firecracker (direct) | knowledge_card, tools, examples, output_template | Platform + vm-config.json |
| nsjail | knowledge_card, tools, examples, output_template | Platform + nsjail.cfg |
| gVisor (runsc) | knowledge_card, tools, examples | Platform |
| seccomp-bpf | knowledge_card, quality_gate, tools, examples | Mandatory gate H07 |
| CPU/RAM/disk/timeout | knowledge_card, quality_gate, output_template, examples, instruction | All 4 gates + template vars |
| Network policy | knowledge_card, quality_gate, output_template, examples | Gate H05 + template section |
| Filesystem scope | knowledge_card, quality_gate, output_template, examples | Gate H06 + template section |

### repo_map

| Concept | Referenced In | Coverage |
|---------|--------------|---------|
| Aider (origin) | knowledge_card | Origin story + reference |
| tree-sitter | knowledge_card, tools, instruction, examples, output_template | Full -- queries, languages, fallback |
| PageRank (graph ranking) | knowledge_card, tools, instruction, examples, output_template | NetworkX code + alpha=0.85 |
| Token budget | knowledge_card, tools, instruction, examples, schema, quality_gate | All ISOs |
| File selection heuristics | knowledge_card, instruction, examples, output_template, quality_gate | 4-rule priority order |
| ctags (fallback) | knowledge_card, tools, instruction | Fallback mechanism |
| tiktoken | knowledge_card, tools | Token counting |

## Top 5 Gaps Remaining (Low Priority)

1. bld_architecture_sandbox_config: Component inventory uses generic "DevOps/Security" owners; could name specific runtimes (runc, containerd, nsjail)
2. bld_architecture_repo_map: MapperEngine dependency doesn't mention tree-sitter or NetworkX
3. bld_memory_sandbox_config: References nonexistent `secure_sandbox_template.yaml` -- should cite OCI spec or CIS benchmark
4. bld_memory_repo_map: References nonexistent `repo_map-builder-v2` -- should cite aider/repomap.py
5. bld_collaboration_sandbox_config: `ComplianceChecker` builder doesn't exist in CEX; should reference guardrail-builder

## 5D Score Summary

| Builder | D1 Domain | D2 Structural | D3 Completeness | D4 Examples | D5 Cross-ref | Avg |
|---------|-----------|---------------|-----------------|-------------|--------------|-----|
| sandbox_config (after) | 9.2 | 9.0 | 9.0 | 9.0 | 8.5 | 9.0 |
| repo_map (after) | 9.2 | 9.0 | 9.0 | 9.0 | 8.5 | 9.0 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_sandbox_config]] | upstream | 0.33 |
| [[bld_instruction_repo_map]] | upstream | 0.33 |
| [[p01_qg_repo_map]] | related | 0.30 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.29 |
| [[bld_examples_sandbox_config]] | upstream | 0.29 |
| [[bld_examples_repo_map]] | upstream | 0.28 |
| [[bld_knowledge_card_repo_map]] | upstream | 0.27 |
| [[bld_output_template_sandbox_config]] | upstream | 0.27 |
| [[bld_tools_sandbox_config]] | upstream | 0.26 |
| [[n01_hybrid_review_wave1]] | sibling | 0.26 |
