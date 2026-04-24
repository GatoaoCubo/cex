---
id: p11_tm_n05
kind: threat_model
8f: F4_reason
pillar: P11
title: "Threat Model: CEX Operations Nucleus (N05)"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: n05_operations
domain: "multi-nucleus AI system security"
quality: 9.1
threat_level: 4
mitigation_status: partially_addressed
tags: [n05, operations, stride, security, multi-nucleus, runtime]
tldr: "STRIDE threat model for CEX multi-nucleus AI system: artifact repo, brand config, API keys, runtime state, git history, LLM context windows."
density_score: 1.0
related:
  - p12_wf_create_orchestration_agent
  - p01_kc_orchestration_best_practices
  - p01_kc_cex_orchestration_architecture
  - p01_ctx_cex_project
  - bld_knowledge_card_nucleus_def
  - p12_wf_orchestration_pipeline
  - bld_output_template_threat_model
  - p03_sp_orchestration_nucleus
  - p02_agent_creation_nucleus
  - p03_sp_n03_creation_nucleus
---

## 1. Scope

**System:** CEX N01-N07 multi-nucleus AI runtime (N05 ops focus). **In scope:** artifact repo, brand_config.yaml, API credentials, .cex/runtime/, git history, LLM context windows. **Out of scope:** cloud provider infra, LLM provider internals, end-user browsers. **Framework:** STRIDE + MITRE ATT&CK + MITRE ATLAS.

## 2. Assets and Actors

**Assets:** artifact repo (.md/.yaml) High/N03; brand_config.yaml Critical/N06; API keys Critical/N05; runtime state (.cex/runtime/) High/N07; git history High/N07; LLM context windows High/per-nucleus.

**Actors:** external attacker (API theft, Medium, Remote); rogue nucleus (unauthorized write, Low, Internal); malicious insider (exfiltration, High, Privileged); automated bot (signal storm, Low, Remote).

## 3. STRIDE Threat Analysis

L=Likelihood, I=Impact (C=Critical), St=O(Open)/Pt(Partial)/M(Mitigated)

| ID | Cat | Threat | Asset | L | I | CVSS | MITRE | St |
|----|-----|--------|-------|---|---|------|-------|----|
| I01 | I | API key in artifact committed to git | API keys | M | C | 9.1 | T1552.001 | O |
| I02 | I | brand_config.yaml exposed via compiled .yaml | Brand cfg | M | C | 8.8 | T1213 | O |
| T02 | T | brand_config.yaml overwritten (injected values) | Brand cfg | L | C | 8.4 | T1565.003 | O |
| D03 | D | Orphan process trees exhaust CPU/RAM | Infra | H | H | 7.5 | T1496 | Pt |
| S01 | S | Rogue nucleus forges signal with spoofed ID | Runtime | M | H | 7.5 | T1078 | O |
| E01 | E | Nucleus writes artifacts outside its directory | Repo | L | H | 7.4 | T1078.003 | O |
| I03 | I | Prior session data injected via memory | LLM ctx | M | H | 7.2 | AML.T0024 | O |
| T01 | T | Artifact modified post-F7 quality gate | Repo | M | H | 7.1 | T1565.001 | Pt |
| D02 | D | Infinite dispatch loop (failed nucleus retry) | Runtime | M | H | 7.0 | T1499.004 | Pt |
| E03 | E | Sub-agent spawns unauthorized child processes | Infra | L | H | 6.9 | T1053 | O |
| D01 | D | Signal storm saturates .cex/runtime/signals/ | Runtime | M | H | 6.8 | T1499 | Pt |
| S02 | S | Malicious process mimics valid N03 handoff | Repo | L | H | 6.8 | T1036 | O |
| R01 | R | Nucleus exits without git commit (no audit) | Git | M | H | 6.5 | T1070.004 | Pt |
| E02 | E | Nucleus self-scores, bypasses peer review | Repo | M | M | 5.5 | T1548 | Pt |
| R02 | R | Self-assigned quality score, no peer record | Repo | M | M | 5.0 | T1070 | O |

## 5. Mitigation Strategies

| ID | Control | NIST CSF | Owner |
|----|---------|----------|-------|
| I01 | Pre-commit secret scanner + .gitignore | PR.DS-5 | N05 |
| I02 | brand_config.yaml in .gitignore; CI read-only | PR.DS-1 | N06 |
| T02 | brand_validate.py schema check on every read | PR.IP-1 | N05 |
| D03 | taskkill /T tree-kill in dispatch.sh stop | RS.MI-3 | N05 |
| S01 | signal_writer validates nucleus ID vs PID registry | PR.AC-3 | N05 |
| D02 | max_retries=3 per wave (cex_mission_runner.py) | DE.CM-7 | N07 |
| E01 | cex_hygiene.py cross-nucleus directory audit | PR.AC-4 | N05 |
| R01 | F8 COLLABORATE: commit+signal required chain | DE.AE-3 | N07 |
| I03 | memory_select.py PII filter; session-scoped clear | PR.DS-5 | N04 |
| E02/S02/T01 | quality: null + frontmatter + fingerprint (pre-commit) | PR.IP-3 | N05 |

## 6. AI-Specific Threats (MITRE ATLAS)

| Threat | ATLAS ID | Mitigation |
|--------|----------|-----------|
| Prompt injection via handoff file | AML.T0051 | ASCII-only enforcement (cex_sanitize.py) |
| Context window exfiltration | AML.T0024 | memory_select.py PII filter; session clear |
| Model extraction via signal patterns | AML.T0005 | Signals carry score+nucleus+kind only |
| Adversarial artifact degrades RAG | AML.T0020 | cex_retriever.py threshold; quality gate |

## 7. Assumptions

- Single-machine (Windows 11, local git); cloud/multi-host excluded. API keys via OS env vars; no Vault.
- Nucleus identity convention-based (dir + PID), not cryptographically attested. CVSS scores are estimates.

## 8. Open Issues

| Issue | Owner | Due |
|-------|-------|-----|
| signal_writer nucleus-ID validation vs PID registry (S01) | N05 | 2026-05-01 |
| cex_hygiene.py cross-nucleus write detection (E01) | N05 | 2026-05-01 |
| memory_select.py PII filter (I03) | N04 | 2026-05-15 |
| Audit artifacts for quality != null (E02) | N05 | 2026-04-30 |
| brand_config.yaml integrity hash on boot (T02) | N06 | 2026-05-01 |

## 9. References

- STRIDE: Microsoft SDL | MITRE ATT&CK: https://attack.mitre.org
- MITRE ATLAS: https://atlas.mitre.org | NIST AI RMF: https://airc.nist.gov/Home
- ISO/IEC 23894:2021 | NIST SP 800-160 Vol. 2

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_create_orchestration_agent]] | downstream | 0.33 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.32 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.30 |
| [[p01_ctx_cex_project]] | upstream | 0.29 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.28 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.28 |
| [[bld_output_template_threat_model]] | upstream | 0.27 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.27 |
| [[p02_agent_creation_nucleus]] | upstream | 0.27 |
| [[p03_sp_n03_creation_nucleus]] | upstream | 0.26 |
