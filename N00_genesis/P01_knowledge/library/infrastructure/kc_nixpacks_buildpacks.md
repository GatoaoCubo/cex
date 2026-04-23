---
id: p01_kc_nixpacks_buildpacks
kind: knowledge_card
pillar: P01
domain: infrastructure
quality: 9.0
density_score: 0.88
name: Nixpacks Buildpacks
description: Nixpacks build system configuration, providers, auto-detection, and deployment patterns
tags: [nixpacks, buildpacks, deployment, docker, nix, railway, vercel]
version: "1.0"
created: 2026-04-01
related:
  - KC_N05_NIXPACKS_BUILDPACKS
  - p01_kc_deploy_paas
  - p06_schema_railway_toml
  - kc_agents_md
  - bld_sp_tools_software_project
  - spec_zero_install
  - p01_kc_railway_platform_deep
  - p01_kc_python_project_structure
  - p05_output_railway_toml
  - p02_agent_software_project_manifest
---

# Nixpacks Buildpacks

Nixpacks is an app build system that creates Docker images from source code using providers and Nix packages. Zero-config auto-detection with customizable `nixpacks.toml` configuration.

## Quick Reference

```toml
# nixpacks.toml
[variables]
NODE_VERSION = "18"
PYTHON_VERSION = "3.11"

[phases.build]
cmds = ["npm run build", "pip install -r requirements.txt"]

[phases.start]
cmd = "npm start"

[providers]
python = "3.11"
node = "18"

[nix]
packages = ["postgresql", "redis", "ffmpeg"]
```

**Core Commands:**
- `nixpacks build .` — Build Docker image locally
- `nixpacks plan .` — Show build plan without building
- `nixpacks --version` — Check version

**File Detection Order:**
1. `nixpacks.toml` (explicit config)
2. Language files (`package.json`, `requirements.txt`, `Cargo.toml`)
3. Framework detection (Next.js, Django, Rails)
4. Fallback to static provider

## Key Concepts

### **Provider System**
Auto-detects language/framework and applies build strategy. Common providers:
- **Python**: Detects `requirements.txt`, `poetry.lock`, `Pipfile`, `setup.py`
- **Node.js**: Detects `package.json`, supports npm/yarn/pnpm
- **Go**: Detects `go.mod`, builds single binary
- **Rust**: Detects `Cargo.toml`, optimized release builds
- **Static**: HTML/CSS/JS, serves with nginx

### **Build Phases**
Four sequential phases executed in container:
- **setup**: Install language runtime and system dependencies
- **install**: Install project dependencies (`npm install`, `pip install`)
- **build**: Run build commands (`npm run build`, compilation)
- **start**: Define startup command for runtime

### **Nix Integration**
Leverages Nix package manager for system dependencies:
```toml
[nix]
packages = ["postgresql", "imagemagick", "git"]
```
Provides reproducible builds across environments with exact package versions.

### **Environment Variables**
Build-time and runtime variable handling:
```toml
[variables]
DATABASE_URL = "postgres://..."  # Runtime
NODE_ENV = "production"          # Build + runtime
```

### **Custom Providers**
Override auto-detection with explicit provider:
```toml
[providers]
python = "3.11"  # Force Python 3.11
node = false     # Disable Node.js provider
```

### **Multi-Language Support**
Handle polyglot applications:
```toml
[providers]
python = "3.11"
node = "18"

[phases.install]
cmds = [
  "pip install -r requirements.txt",
  "npm install"
]
```

## Patterns

### **Python + Poetry Pattern**
```toml
[variables]
PYTHON_VERSION = "3.11"

[providers]
python = "3.11"

[phases.install]
cmds = ["poetry install --no-dev"]

[phases.build]
cmds = ["poetry run python manage.py collectstatic --noinput"]

[phases.start]
cmd = "poetry run gunicorn app:app"

[nix]
packages = ["poetry"]
```

### **Node.js + Build Optimization**
```toml
[variables]
NODE_VERSION = "18"
NODE_ENV = "production"

[providers]
node = "18"

[phases.install]
cmds = ["npm ci --only=production"]

[phases.build]
cmds = [
  "npm run build",
  "npm prune --production"
]

[phases.start]
cmd = "npm start"
```

### **Full-Stack Next.js + Database**
```toml
[variables]
NODE_VERSION = "18"
DATABASE_URL = "$DATABASE_URL"

[providers]
node = "18"

[phases.build]
cmds = [
  "npm run db:migrate",
  "npm run build"
]

[phases.start]
cmd = "npm start"

[nix]
packages = ["postgresql"]
```

## Golden Rules

### **Minimize Build Time**
- Use `.nixpacksignore` to exclude unnecessary files
- Leverage Docker layer caching with consistent dependency installs
- Separate dependency installation from application code changes
- Use `npm ci` instead of `npm install` for production builds

### **Explicit Configuration**
- Always specify exact versions in `nixpacks.toml`
- Use explicit provider configuration over auto-detection for production
- Define all required system packages in `[nix]` section
- Set environment variables explicitly rather than relying on defaults

### **Production Optimization**
- Install only production dependencies (`--no-dev`, `--only=production`)
- Use optimized start commands (gunicorn, PM2, not dev servers)
- Enable build caching where possible
- Configure health checks and graceful shutdowns in start command

## References

- **Official Docs**: https://nixpacks.com/docs
- **GitHub Repo**: https://github.com/railwayapp/nixpacks
- **Provider Reference**: https://nixpacks.com/docs/providers
- **Nix Packages**: https://search.nixos.org/packages
- **Railway Integration**: https://docs.railway.app/deploy/nixpacks
- **Example Configs**: https://github.com/railwayapp/nixpacks/tree/main/examples

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[KC_N05_NIXPACKS_BUILDPACKS]] | sibling | 0.67 |
| [[p01_kc_deploy_paas]] | sibling | 0.31 |
| [[p06_schema_railway_toml]] | downstream | 0.31 |
| [[kc_agents_md]] | sibling | 0.30 |
| [[bld_sp_tools_software_project]] | downstream | 0.28 |
| [[spec_zero_install]] | related | 0.28 |
| [[p01_kc_railway_platform_deep]] | sibling | 0.25 |
| [[p01_kc_python_project_structure]] | sibling | 0.23 |
| [[p05_output_railway_toml]] | downstream | 0.23 |
| [[p02_agent_software_project_manifest]] | downstream | 0.22 |
