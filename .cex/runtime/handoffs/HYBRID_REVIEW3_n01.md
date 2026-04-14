---
mission: HYBRID_REVIEW3
nucleus: n01
wave: review
created: 2026-04-13
model: claude-opus-4-6
source_model: gemma4:26b (Wave 2 ML kinds)
---

# N01 -- Audit agent_computer_interface + training_method (26 ISOs)

## Your kinds
1. agent_computer_interface -- archetypes/builders/agent-computer-interface-builder/ (13 ISOs)
2. training_method -- archetypes/builders/training-method-builder/ (13 ISOs)

## Pre-flight check

```bash
ls archetypes/builders/agent-computer-interface-builder/ | grep -c bld_
ls archetypes/builders/training-method-builder/ | grep -c bld_
```
Both should return 13. If either is < 13, Wave 2 is incomplete -- wait for gemma4 signal before proceeding.

## Review protocol

### Step 1: Load systemic defects reference
Read `N01_intelligence/reports/master_systemic_defects.md` first.
You are looking for the 15 known defects (D01-D15) in gemma4-generated ISOs.
Priority checks: D01, D02, D03, D04, D05, D07, D08, D09, D12.

### Step 2: Per-kind audit

For each kind, open all 13 ISOs and score using 5D scoring:
- D1 Structural completeness (frontmatter, required fields, no blanks)
- D2 Domain accuracy (content matches the kind's real-world domain)
- D3 Density (>=0.85, not padded with generic prose)
- D4 CEX compliance (8F references, correct file naming, correct llm_function)
- D5 Industry alignment (terminology matches authoritative sources below)

**Score thresholds:**
- >= 8.0: leave as-is
- 6.0-7.9: surgical fix in place
- < 6.0: full rebuild following 8F pipeline

### Step 3: Industry citations to verify (must appear in correct ISOs)

**agent_computer_interface:**
- AutoGen (Microsoft): tool-use, function-calling patterns for agents
- LangGraph: state machine + tool-call loop architecture
- CrewAI: agent role definitions, delegation patterns
- MCP (Model Context Protocol / Anthropic): server/client tool interface
- ACI spec (Agent-Computer Interface): formal definition of ACI boundary
- OpenAI Assistants API: tool definitions, file attachments, code interpreter
- Check: bld_instruction should cover BECOME, not INJECT; bld_tools must list real CEX tools

**training_method:**
- SFT (Supervised Fine-Tuning): dataset format, loss function, epochs
- DPO (Direct Preference Optimization): Bradley-Terry model, preference pairs
- PPO (Proximal Policy Optimization): reward model, KL penalty, clip ratio
- LoRA / QLoRA: rank, alpha, target modules, memory footprint
- RLHF: reward model training, policy gradient, human preference collection
- Constitutional AI (Anthropic): critique-revision loop, RLAIF
- Check: bld_schema must include method_type, base_model, dataset_format fields

### Step 4: Known gemma4 contamination patterns to detect

1. D01: bld_system_prompt has llm_function=INJECT instead of BECOME
2. D04: Domain hallucination -- financial/trading terminology in ML training context
3. D07: bld_tools references fake tools (check vs real _tools/ directory)
4. D08: output_template has bare {{placeholders}} without guidance prose
5. D09: bld_architecture lists generic tech stacks (PyTorch, TensorFlow) not 13-ISO structure
6. D12: Unicode checkmarks or em-dashes in .md files that will be compiled (flag but do not auto-fix .py files)

### Step 5: Fix or rebuild

For surgical fixes: edit the ISO in place, note what changed.
For rebuilds: use the agent-computer-interface-builder or training-method-builder ISOs as spec.

### Step 6: Validate

```bash
python _tools/cex_wave_validator.py --scope archetypes/builders/agent-computer-interface-builder/
python _tools/cex_wave_validator.py --scope archetypes/builders/training-method-builder/
```
Fix any validator failures before committing.

### Step 7: Write audit reports

1. `N01_intelligence/audits/hybrid_review3_n01_aci.md` -- agent_computer_interface audit
2. `N01_intelligence/audits/hybrid_review3_n01_tm.md` -- training_method audit
3. `N01_intelligence/audits/hybrid_review3_n01.md` -- master summary (scores, fixes, remaining issues)

Use knowledge_card frontmatter for all 3 reports:
```yaml
---
id: hybrid_review3_n01_aci
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW3 Audit: agent_computer_interface (N01)"
version: 1.0.0
quality: null
tags: [audit, hybrid_review3, agent_computer_interface, gemma4, wave2]
domain: AI research quality assurance
created: "2026-04-13"
---
```

## Context (pre-loaded)

- Master defects: `N01_intelligence/reports/master_systemic_defects.md`
- Gold standard builder: `archetypes/builders/knowledge-card-builder/` (13 ISOs, all passing)
- Your prior audit: `N01_intelligence/audits/hybrid_review2_n01.md`
- Kind KC references: `P01_knowledge/library/kind/kc_agent_computer_interface.md` (if exists)

## Commit

```bash
git add archetypes/builders/agent-computer-interface-builder/ \
        archetypes/builders/training-method-builder/ \
        N01_intelligence/audits/hybrid_review3_n01*.md
git commit -m "[N01] HYBRID_REVIEW3: audit+fix agent_computer_interface + training_method (26 ISOs)"
```

## ON COMPLETION

```bash
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'complete', 9.0)"
```
