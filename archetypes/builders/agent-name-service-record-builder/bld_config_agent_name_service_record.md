---
kind: config
id: bld_config_agent_name_service_record
pillar: P09
llm_function: CONSTRAIN
purpose: Runtime configuration for the agent_name_service_record builder -- paths, limits, naming, hooks
quality: 9.1
title: "Agent Name Service Record Builder -- Config"
version: "1.0.0"
author: wave7_n05
tags: [agent_name_service_record, builder, config]
tldr: "Naming pattern p04_ans_{{agent_slug}}.md, max 3072 bytes, output to P04_tools/, hooks for compile+score"
domain: "agent_name_service_record construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_agent_name_service_record
  - bld_architecture_agent_name_service_record
  - bld_instruction_agent_name_service_record
  - bld_system_prompt_agent_name_service_record
  - bld_collaboration_agent_name_service_record
  - bld_output_template_agent_name_service_record
  - bld_quality_gate_agent_name_service_record
  - bld_manifest_agent_name_service_record
  - bld_tools_kind
  - bld_schema_agent_name_service_record
---
# Agent Name Service Record Builder -- Config

> Runtime configuration for producing IETF ANS / CNCF AgentDNS registry-records.
> Artifacts declare discovery-endpoint URLs, protocol-adapter entries, and PKI-cert
> references for GoDaddy, Salesforce, and other registry operators.

## Naming Convention

| Asset | Pattern | Regex | Example |
|-------|---------|-------|---------|
| Artifact file | `p04_ans_{agent_slug}.md` | `^p04_ans_[a-z0-9_]+\.md$` | `p04_ans_billing_bot_acme.md` |
| Artifact id | `p04_ans_{agent_slug}` | `^p04_ans_[a-z0-9_]+$` | `p04_ans_billing_bot_acme` |
| Compiled YAML | `p04_ans_{agent_slug}.yaml` | `^p04_ans_[a-z0-9_]+\.yaml$` | `p04_ans_billing_bot_acme.yaml` |
| Builder dir | `agent-name-service-record-builder/` | -- | (fixed) |

**agent_slug derivation from ANS name:**

```
ANS name:    billing-bot.acme-corp.agents
agent_slug:  billing_bot_acme_corp          (replace hyphens with underscores, remove .agents)
file id:     p04_ans_billing_bot_acme_corp
```

## Paths

| Path | Description |
|------|-------------|
| `P04_tools/` | Output directory for all agent_name_service_record artifacts |
| `archetypes/builders/agent-name-service-record-builder/` | This builder's 13 ISO files |
| `P01_knowledge/library/kind/kc_agent_name_service_record.md` | Kind KC (if exists) |
| `.cex/kinds_meta.json` | Registry entry for `agent_name_service_record` kind |

## Limits

| Limit | Value | Notes |
|-------|-------|-------|
| max_bytes | 3072 | Per kinds_meta.json entry -- enforce at F7 GOVERN |
| min_quality | 8.0 | Publish threshold |
| target_quality | 9.0 | Standard production target |
| density_score | 0.85 | Information density floor |
| max_skills | 10 | capability_advertisement.skills array |
| max_protocol_adapters | 5 | protocol_adapters array (practical limit) |
| min_protocol_adapters | 1 | Hard gate H06 |
| max_concurrent | no limit | Integer, agent-specific |

## Hooks

### Pre-build hook (F1 CONSTRAIN)

```bash
# Verify output directory exists
mkdir -p P04_tools/
# Check for existing record (avoid duplicates)
ls P04_tools/p04_ans_*.md 2>/dev/null | grep "{agent_slug}" && echo "WARNING: record exists"
```

### Post-build hook (F8 COLLABORATE)

```bash
# Compile artifact to YAML
python _tools/cex_compile.py P04_tools/p04_ans_{agent_slug}.md
# Score the artifact
python _tools/cex_score.py --apply P04_tools/p04_ans_{agent_slug}.md
# Update search index
python _tools/cex_index.py
# Validate byte count
wc -c P04_tools/p04_ans_{agent_slug}.md
# if > 3072: trim capability_advertisement or lifecycle notes
# Git commit
git add P04_tools/p04_ans_{agent_slug}.md P04_tools/p04_ans_{agent_slug}.yaml
git commit -m "[N05] ANS record: {ans_name} -- {registry_operator} registry"
```

### Signal hook

```python
from _tools.signal_writer import write_signal
write_signal('n05', 'complete', 9.0)
# Replace 9.0 with actual score from cex_score.py output
```

## Validation Config

| Check | Tool | Command |
|-------|------|---------|
| YAML frontmatter | cex_compile.py | `python _tools/cex_compile.py {path}` |
| Quality gates | cex_score.py | `python _tools/cex_score.py --apply {path}` |
| Byte limit | bash wc | `wc -c {path}` -- must be <= 3072 |
| ASCII-only | cex_sanitize.py | `python _tools/cex_sanitize.py --check --scope P04_tools/` |
| Doctor check | cex_doctor.py | `python _tools/cex_doctor.py` |

## ASCII Enforcement

Per `.claude/rules/ascii-code-rule.md`:

| Forbidden | Replacement |
|----------|-------------|
| Em-dash (U+2014) | `--` |
| Smart quotes | Straight quotes `"` `'` |
| Accented chars in content | Unaccented ASCII equivalent |
| Any char > 0x7F in .md | Use `\uXXXX` escape in code blocks only |

ANS record `.md` files are content files (not code) and may contain non-ASCII
in YAML values only. Body text and all field values MUST be ASCII.

## Registry Operator Config

| Operator | Extra fields required | Discovery URL pattern |
|----------|----------------------|----------------------|
| godaddy | pki_cert_reference (mandatory) | `https://{domain}/.well-known/agent/{label}` |
| salesforce | pki_cert_reference (mandatory), crm_object_access (optional skill) | `https://{org}.my.salesforce.com/.well-known/agent/{label}` |
| cncf | None beyond schema | `https://{org-domain}/.well-known/agent/{label}` |
| self | None (pki_cert recommended) | Operator-defined URL |

## Environment Variables (optional)

| Variable | Purpose | Default |
|----------|---------|---------|
| `ANS_REGISTRY_OPERATOR` | Default operator for new records | `cncf` |
| `ANS_PKI_ISSUER` | Default CA issuer for PKI-cert references | (none) |
| `ANS_OUTPUT_DIR` | Override output directory | `P04_tools/` |
| `ANS_MAX_BYTES` | Override max_bytes limit | `3072` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_agent_name_service_record]] | upstream | 0.36 |
| [[bld_architecture_agent_name_service_record]] | upstream | 0.36 |
| [[bld_instruction_agent_name_service_record]] | upstream | 0.32 |
| [[bld_system_prompt_agent_name_service_record]] | upstream | 0.31 |
| [[bld_collaboration_agent_name_service_record]] | downstream | 0.31 |
| [[bld_output_template_agent_name_service_record]] | upstream | 0.28 |
| [[bld_quality_gate_agent_name_service_record]] | downstream | 0.27 |
| [[bld_manifest_agent_name_service_record]] | upstream | 0.26 |
| [[bld_tools_kind]] | upstream | 0.25 |
| [[bld_schema_agent_name_service_record]] | upstream | 0.24 |
