---
id: p12_spawn_admin_nucleus
kind: spawn_config
pillar: P12
version: "1.0.0"
created: "2023-10-05"
director: "admin"
mode: solo
model: "opus"
flags:
  - "--dangerously-skip-permissions"
  - "--no-chrome"
  - "-p"
mcp_profile: ".mcp-admin.json"
timeout_seconds: 1200
prompt_inline: false
handoff_path: ".handoffs/admin_task.md"
quality: null
---
