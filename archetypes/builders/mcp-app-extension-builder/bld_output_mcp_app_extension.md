---
kind: output_template
id: bld_output_template_mcp_app_extension
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for mcp_app_extension production
quality: 9.0
title: "Output Template MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, output_template]
tldr: "Template with vars for mcp_app_extension production"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_mcp_app_extension
  - bld_instruction_mcp_app_extension
  - bld_knowledge_card_mcp_app_extension
  - bld_schema_mcp_app_extension
  - p04_qg_mcp_app_extension
  - p03_sp_mcp_app_extension_builder
  - mcp-app-extension-builder
  - p10_lr_mcp_app_extension_builder
  - bld_collaboration_mcp_app_extension
  - bld_tools_mcp_app_extension
---

```markdown
```yaml
---
id: p04_mae_{{name}}.md
kind: mcp_app_extension
pillar: P04
app_id: {{app_id}}            <!-- e.g., 'com.acme.design-inspector' -->
version: {{version}}          <!-- SemVer, e.g., '1.0.0' -->
entry_url: {{entry_url}}      <!-- HTTPS iframe URL -->
spec_version: SEP-1865
quality: null
---
```

## App Manifest
| Field        | Value                                   |
|--------------|-----------------------------------------|
| app_id       | {{app_id}}                              <!-- Reverse-DNS or p04_mae slug -->
| entry_url    | {{entry_url}}                           <!-- HTTPS, iframe-loadable -->
| icon_url     | {{icon_url}}                            <!-- Optional HTTPS icon -->
| homepage     | {{homepage}}                            <!-- Public homepage -->

## Capabilities (SEP-1865)
- {{capability_1}}   <!-- e.g., 'tool:get_design_spec' -->
- {{capability_2}}   <!-- e.g., 'resource:component_library' -->

## Permissions
- {{permission_1}}   <!-- e.g., 'network:https://api.example.com' -- justification -->
- {{permission_2}}   <!-- e.g., 'clipboard:read' -- justification -->

## Lifecycle
```yaml
install:   handshake fetches manifest, validates signature, provisions sandbox
launch:    client spawns iframe, delivers session token via postMessage
terminate: client revokes token, clears sandbox state
```

## Sandbox Policy
- Iframe sandbox flags: allow-scripts, allow-same-origin (if required, justified)
- CSP: default-src 'self'; connect-src {{allowed_origins}}; frame-ancestors {{client_origin}}
- postMessage only; parent-frame DOM access FORBIDDEN (MCP + AAIF requirement)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_mcp_app_extension]] | downstream | 0.55 |
| [[bld_instruction_mcp_app_extension]] | upstream | 0.53 |
| [[bld_knowledge_card_mcp_app_extension]] | upstream | 0.51 |
| [[bld_schema_mcp_app_extension]] | downstream | 0.49 |
| [[p04_qg_mcp_app_extension]] | downstream | 0.44 |
| [[p03_sp_mcp_app_extension_builder]] | upstream | 0.44 |
| [[mcp-app-extension-builder]] | related | 0.36 |
| [[p10_lr_mcp_app_extension_builder]] | downstream | 0.31 |
| [[bld_collaboration_mcp_app_extension]] | downstream | 0.29 |
| [[bld_tools_mcp_app_extension]] | upstream | 0.27 |
