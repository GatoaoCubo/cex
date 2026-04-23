---
kind: output_template
id: bld_output_template_sandbox_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for sandbox_config production
quality: 9.1
title: "Output Template Sandbox Config"
version: "1.1.0"
author: n05_ops
tags: [sandbox_config, builder, output_template]
tldr: "Sandbox config template: resource limits (CPU/RAM/disk/timeout), network policy, filesystem scope, isolation mechanism"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_examples_sandbox_config
  - bld_instruction_sandbox_config
  - bld_knowledge_card_sandbox_config
  - p09_qg_sandbox_config
  - n05_audit_hybrid_review2
  - bld_tools_sandbox_config
  - bld_output_template_code_executor
  - bld_examples_code_executor
  - p10_lr_code_executor_builder
  - bld_knowledge_card_code_executor
---

```yaml
---
id: p09_sb_{{name}}
kind: sandbox_config
pillar: P09
title: "{{title}}"
version: "1.0.0"
created: "{{date}}"
updated: "{{date}}"
author: "{{author}}"
domain: "{{domain}}"
quality: null
tags: [sandbox_config, {{extra_tags}}]
tldr: "{{one_line_description}}"
sandbox_type: "{{sandbox_type}}"  # isolated | shared | hybrid
platform: "{{platform}}"          # e2b | modal | daytona | docker | firecracker | nsjail | gvisor
---

## Resource Limits

| Resource | Limit | Unit | Notes |
|----------|-------|------|-------|
| CPU | {{cpu_limit}} | cores (fractional OK) | e.g. 0.5, 1, 2 |
| RAM | {{memory_mb}} | MB | OOM kills sandbox on exceed |
| Disk | {{disk_mb}} | MB | Ephemeral scratch only |
| Timeout | {{timeout_seconds}} | seconds | Wall-clock; SIGKILL on exceed |
| Max processes | {{max_pids}} | count | cgroup pids.max |

## Network Policy

```
network:
  mode: `{{network_mode}}`        # none | bridge | host | custom
  egress: `{{egress_policy}}`     # none | whitelist | all
  allowed_hosts: `{{allowed_hosts_list}}`   # [] for air-gapped
  allowed_ports: `{{allowed_ports_list}}`   # [] for no outbound
  dns: `{{dns_enabled}}`          # false for air-gapped
```

## Filesystem Scope

```
filesystem:
  root: `{{sandbox_root}}`        # e.g. /tmp/sandbox or /var/sandbox
  read_only_root: `{{ro_root}}`   # true | false
  scratch_dir: `{{scratch_path}}` # ephemeral writable area (tmpfs)
  scratch_size_mb: `{{scratch_mb}}`
  mounts:
    - path: `{{mount_path}}`
      source: `{{host_path}}`
      read_only: `{{mount_ro}}`
```

## Isolation Mechanism

```
isolation:
  runtime: `{{runtime}}`          # runc | runsc | nsjail | firecracker | qemu
  namespaces: [pid, net, mnt, uts, ipc, user]
  seccomp_profile: `{{seccomp_profile}}`  # default | custom | none
  apparmor_profile: `{{apparmor_profile}}`  # null if not applicable
  capabilities:
    drop: [ALL]
    add: `{{required_capabilities}}`  # e.g. [NET_BIND_SERVICE]
  no_new_privs: true
```

## Audit & Logging

```
audit:
  syscall_logging: `{{syscall_log}}`  # true | false
  log_destination: `{{log_path}}`     # /var/log/sandbox/ or syslog
  log_retention_days: `{{log_days}}`
```

## Platform-Specific Config

### E2B
```toml
# e2b.toml
[template]
dockerfile = "`{{dockerfile_path}}`"
[resources]
vcpu = `{{cpu_limit}}`
memory_mb = `{{memory_mb}}`
timeout = `{{timeout_seconds}}`
```

### Docker
```bash
docker run \
  --cpus `{{cpu_limit}}` \
  --memory `{{memory_mb}}`m \
  --network `{{network_mode}}` \
  --read-only \
  --tmpfs /tmp:size=`{{scratch_mb}}`m \
  --cap-drop ALL \
  --security-opt seccomp=`{{seccomp_profile}}` \
  `{{image_name}}`
```

### nsjail
```
# nsjail.cfg
time_limit: `{{timeout_seconds}}`
rlimit_cpu: `{{cpu_limit_int}}`
rlimit_as: `{{memory_bytes}}`
log_fd: 2
mount { src: "`{{sandbox_root}}`" dst: "/" is_bind: true rw: false }
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_sandbox_config]] | downstream | 0.65 |
| [[bld_instruction_sandbox_config]] | upstream | 0.57 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.45 |
| [[p09_qg_sandbox_config]] | downstream | 0.31 |
| [[n05_audit_hybrid_review2]] | downstream | 0.30 |
| [[bld_tools_sandbox_config]] | upstream | 0.30 |
| [[bld_output_template_code_executor]] | sibling | 0.30 |
| [[bld_examples_code_executor]] | downstream | 0.27 |
| [[p10_lr_code_executor_builder]] | downstream | 0.26 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.26 |
