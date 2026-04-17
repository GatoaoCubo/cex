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
