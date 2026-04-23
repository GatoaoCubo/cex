---
id: n05_output_monetization_infra
kind: output_validator
pillar: P05
title: "CEX Monetization Infrastructure Plan"
version: 1.0.0
created: 2026-04-02
author: n05_operations
domain: monetization
quality: 9.1
tags: [monetization, infra, ci-cd, lemon-squeezy, distribution, automation]
tldr: "Complete infrastructure automation plan for CEX monetization via Lemon Squeezy + GGUF model distribution + course delivery."
density_score: null
related:
  - p04_output_github_actions
  - n03_output_monetization_architecture
  - p01_kc_github_actions
  - p01_kc_git_hooks_ci
  - KC_N05_API_HEALTH_MONITORING
  - p01_kc_fastapi_patterns
  - skill
  - bld_knowledge_card_webhook
  - bld_sp_output_template_software_project
  - bld_tools_changelog
---

# CEX Monetization Infrastructure Plan

## Executive Summary
Infrastructure automation for CEX monetization via public repo + paid course model:
- **Repo**: MIT license on GitHub with CI/CD automation
- **Payments**: Lemon Squeezy (5% fee) handling tiers: Explorer R$0 / Builder R$497 / Master R$997
- **Model**: cex-brain:14b GGUF (~10GB) exclusive to paid tiers
- **Course**: Hybrid format with video + text + exercises

---

## 1. Public Repo DevOps Prep

### GitHub Actions Workflow
```yaml
# .github/workflows/cex-ci.yml
name: CEX CI/CD Pipeline
on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install yamllint
          
      - name: Validate YAML frontmatter
        run: |
          find . -name "*.md" -exec python _tools/cex_validate_frontmatter.py {} \;
          
      - name: Run CEX Doctor
        run: python _tools/cex_doctor.py --ci
        
      - name: Test Suite
        run: python -m pytest _tools/test_suite.py -v
```

### Branch Strategy
| Branch | Purpose | Protection |
|--------|---------|------------|
| `main` | Stable releases, tagged versions | Required PR review, status checks |
| `dev` | Work-in-progress, continuous integration | Status checks only |
| `release/v*` | Release preparation | Auto-created from main on tag |

### Release Automation
```bash
# .github/workflows/release.yml
name: Auto Release
on:
  push:
    tags: ['v*']

jobs:
  release:
    steps:
      - name: Generate Changelog
        run: python _tools/cex_changelog.py ${{ github.ref_name }}
        
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          generate_release_notes: true
          files: |
            CHANGELOG.md
            
      - name: Notify Lemon Squeezy
        run: |
          curl -X POST "${{ secrets.LEMON_SQUEEZY_WEBHOOK_URL }}" \
            -H "Content-Type: application/json" \
            -d '{"event":"release", "version":"${{ github.ref_name }}"}'
```

### Pre-commit Hooks Audit
Existing hooks in `.git/hooks/`:
- `pre-commit`: Runs `cex_doctor.py --pre-commit`
- `post-commit`: Updates `_tools/cex_index.py`
- **ENHANCEMENT**: Add YAML linting and frontmatter validation

---

## 2. Lemon Squeezy Integration

### Webhook Setup
```python
# _tools/cex_webhook_handler.py
from fastapi import FastAPI, Request, HTTPException
import hmac
import hashlib
import os
from datetime import datetime

app = FastAPI()

@app.post("/webhook/lemon-squeezy")
async def handle_purchase(request: Request):
    """Handle Lemon Squeezy purchase webhooks."""
    payload = await request.body()
    signature = request.headers.get("X-Signature")
    
    # Verify webhook signature
    secret = os.getenv("LEMON_SQUEEZY_WEBHOOK_SECRET")
    expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(signature, expected):
        raise HTTPException(status_code=401, detail="Invalid signature")
    
    data = await request.json()
    
    # Process purchase
    if data["meta"]["event_name"] == "order_created":
        await grant_download_access(data["data"])
    
    return {"status": "ok"}

async def grant_download_access(order_data):
    """Grant model download access for paid tiers."""
    email = order_data["attributes"]["user_email"]
    variant_name = order_data["attributes"]["variant_name"]
    
    # Generate license key
    license_key = generate_license_key()
    
    # Store in customer database
    await store_customer_data(email, license_key, variant_name)
    
    # Send license key via email
    await send_license_email(email, license_key, variant_name)
```

### License Key Validation
```python
# _tools/cex_license.py
import click
import requests
import os
from pathlib import Path

@click.command()
@click.option('--activate', help='License key to activate')
@click.option('--verify', is_flag=True, help='Verify existing license')
def main(activate, verify):
    """CEX License Manager - Model Download & Activation."""
    
    if activate:
        activate_license(activate)
    elif verify:
        verify_license()
    else:
        click.echo("Use --activate KEY or --verify")

def activate_license(key: str):
    """Validate key and download cex-brain model."""
    
    # Verify key with Lemon Squeezy API
    response = requests.post(
        "https://api.lemonsqueezy.com/v1/licenses/validate",
        headers={"Authorization": f"Bearer {os.getenv('LEMON_SQUEEZY_API_KEY')}"},
        json={"license_key": key}
    )
    
    if response.status_code != 200:
        click.echo(f"❌ Invalid license key")
        return
    
    data = response.json()
    tier = data["meta"]["variant_name"]  # Builder/Master
    
    if tier in ["Builder", "Master"]:
        click.echo(f"✅ License valid for {tier} tier")
        download_model(tier, key)
        install_ollama_model()
    else:
        click.echo(f"❌ {tier} tier doesn't include model access")

def download_model(tier: str, key: str):
    """Download cex-brain GGUF from secure endpoint."""
    download_url = f"https://models.cex.ai/cex-brain-14b.gguf?key={key}"
    
    model_path = Path.home() / ".cex" / "models" / "cex-brain-14b.gguf"
    model_path.parent.mkdir(exist_ok=True)
    
    click.echo("📥 Downloading cex-brain:14b (~10GB)...")
    
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(model_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    click.echo(f"✅ Model downloaded to {model_path}")

def install_ollama_model():
    """Create Ollama model from GGUF."""
    os.system("ollama create cex-brain -f ~/.cex/models/Modelfile")
    click.echo("✅ cex-brain model installed in Ollama")

if __name__ == '__main__':
    main()
```

### Customer Data Storage (LGPD-compliant)
```yaml
# customer_schema.json - Minimal data retention
{
  "email": "user@example.com",          # Required for license delivery
  "license_key": "CEX-XXXXX-XXXXX",     # Required for validation
  "tier": "Builder",                    # Required for feature access
  "created_at": "2026-04-02T10:00:00Z", # Required for audit
  "last_download": "2026-04-02T10:30:00Z" # Optional for analytics
}
```

**LGPD Compliance**:
- **Data minimization**: Only email, key, tier stored
- **Retention**: 2 years after license expiry
- **Right to deletion**: Automated via `cex_license.py --delete-account`
- **Data portability**: JSON export available

---

## 3. Model Distribution Pipeline

### Training Pipeline
```python
# _tools/cex_train_brain.py
import subprocess
from pathlib import Path

def export_dataset():
    """Export CEX artifacts to training dataset."""
    subprocess.run([
        "python", "_tools/cex_export_dataset.py",
        "--output", "cex_brain_dataset.jsonl",
        "--format", "instruction_following",
        "--filter", "quality>=8.0"
    ])

def train_qlora():
    """Train QLoRA adapter on CEX dataset."""
    subprocess.run([
        "python", "-m", "axolotl.cli.train",
        "configs/cex_brain_qlora.yml"
    ])

def merge_and_quantize():
    """Merge QLoRA + quantize to GGUF."""
    # Merge adapter
    subprocess.run([
        "python", "-m", "axolotl.cli.merge_lora",
        "configs/cex_brain_qlora.yml",
        "--lora-model-dir", "outputs/cex-brain"
    ])
    
    # Quantize to GGUF
    subprocess.run([
        "python", "llama.cpp/convert.py", 
        "merged_model/",
        "--outfile", "cex-brain-14b.gguf",
        "--outtype", "q4_k_m"
    ])

if __name__ == "__main__":
    export_dataset()
    train_qlora() 
    merge_and_quantize()
    print("✅ cex-brain:14b GGUF ready for distribution")
```

### Hosting Options

| Option | Cost | Bandwidth | CDN | Gated Access |
|--------|------|-----------|-----|--------------|
| **HuggingFace Hub** | Free | 1TB/month | Global | ✅ Gated repo |
| **AWS S3 + CloudFront** | $23/month | Pay-per-GB | Global | ✅ Signed URLs |
| **Bunny.net CDN** | $5/month + usage | $0.01/GB | Global | ✅ Token auth |

**Recommendation**: HuggingFace Hub for simplicity, S3+CloudFront for scale.

### Download & Version Management
```python
# _tools/cex_model_version.py
def check_model_updates():
    """Check for cex-brain model updates."""
    current_version = get_local_model_version()
    latest_version = get_remote_model_version()
    
    if latest_version > current_version:
        print(f"🔄 cex-brain update available: {latest_version}")
        print("Run: cex_license.py --update")
        return True
    return False

def update_model():
    """Download latest model without breaking existing installs."""
    # Download to temp location
    download_model_version(get_remote_model_version(), temp=True)
    
    # Backup current model
    backup_current_model()
    
    # Atomic swap
    os.rename("~/.cex/models/cex-brain-14b.gguf.new", 
              "~/.cex/models/cex-brain-14b.gguf")
    
    # Update Ollama
    os.system("ollama rm cex-brain && ollama create cex-brain -f ~/.cex/models/Modelfile")
```

### Cost Estimates
**10GB GGUF × Download Volume**:
- **10 downloads/month**: ~$2/month bandwidth
- **50 downloads/month**: ~$8/month bandwidth  
- **100 downloads/month**: ~$15/month bandwidth

**HuggingFace**: Free up to 1TB/month (100 downloads)

---

## 4. Course Delivery Infrastructure

### Video Hosting Options

| Platform | Cost | Bandwidth | Analytics | DRM |
|----------|------|-----------|-----------|-----|
| **YouTube Unlisted** | Free | Unlimited | Basic | ❌ |
| **Vimeo Pro** | $20/month | 1TB/year | Advanced | ✅ |
| **Bunny.net Stream** | $5/month + $1/100GB | Pay-per-view | Custom | ✅ |

**Recommendation**: YouTube Unlisted for MVP, Vimeo Pro for production.

### Content Delivery

| Component | Solution | Access Control |
|-----------|----------|----------------|
| **Videos** | YouTube unlisted playlists | Link-based access |
| **Text** | GitHub private repo | Collaborator access |
| **Exercises** | CEX tasks in repo | Student runs locally |

### Student Access Management
```python
# _tools/cex_course_access.py
def grant_course_access(email: str, tier: str):
    """Grant GitHub repo access for course content."""
    
    # Builder/Master tiers get course access
    if tier in ["Builder", "Master"]:
        # Add to GitHub repo collaborators
        subprocess.run([
            "gh", "api", "/repos/cex/course-content/collaborators",
            "-X", "PUT",
            "-f", f"username={get_github_username(email)}",
            "-f", "permission=read"
        ])
        
        # Send course welcome email
        send_course_welcome_email(email, tier)

def verify_course_completion(student_email: str, module: str):
    """Verify student completed module exercises."""
    
    # Student runs: cex_doctor.py --course-check module_01
    # This creates: ~/.cex/course/completion_module_01.json
    # We check for file existence + valid schema
    
    completion_file = Path.home() / ".cex" / "course" / f"completion_{module}.json"
    
    if completion_file.exists():
        with open(completion_file) as f:
            data = json.load(f)
            return data.get("status") == "completed"
    
    return False
```

### Exercise Verification System
```bash
# Student runs this after each module
python _tools/cex_doctor.py --course-check module_01

# Creates completion proof:
# ~/.cex/course/completion_module_01.json
{
  "module": "module_01",
  "completed_at": "2026-04-02T10:00:00Z",
  "exercises_passed": 5,
  "cex_doctor_score": 9.2,
  "artifacts_created": ["agent_personal.md", "knowledge_card_react.md"]
}
```

---

## 5. Monitoring & Analytics

### GitHub Metrics (Free)
```python
# _tools/cex_analytics.py
import requests

def get_github_metrics():
    """Fetch GitHub repo analytics."""
    
    response = requests.get(
        "https://api.github.com/repos/cex-org/cex",
        headers={"Authorization": f"token {os.getenv('GITHUB_TOKEN')}"}
    )
    
    data = response.json()
    return {
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "clones": get_clone_stats(),
        "traffic": get_traffic_stats()
    }
```

### Lemon Squeezy Dashboard (Native)
- **Revenue**: Monthly recurring, one-time sales
- **Churn**: Subscription cancellations  
- **LTV**: Customer lifetime value
- **Conversion**: Visitor-to-customer funnel

### Course Completion Tracking
```python
# _tools/cex_course_analytics.py
def get_completion_rates():
    """Analyze course completion by module."""
    
    students = get_all_students()
    completion_data = {}
    
    for module in ["01_foundations", "02_builders", "03_advanced"]:
        completed = 0
        for student in students:
            if verify_course_completion(student["email"], module):
                completed += 1
        
        completion_data[module] = {
            "completion_rate": completed / len(students),
            "avg_time_to_complete": get_avg_completion_time(module)
        }
    
    return completion_data
```

### Alert Configuration
```yaml
# alerts.yml
alerts:
  - name: "Model download failures"
    condition: "error_rate > 5%"
    notification: "slack_webhook"
    
  - name: "License validation failures" 
    condition: "validation_failures > 10/hour"
    notification: "email"
    
  - name: "Course completion drop"
    condition: "completion_rate < 60%"
    notification: "dashboard_alert"
```

---

## 6. Cost Analysis

### Fixed Costs (Monthly)
| Service | Cost | Purpose |
|---------|------|---------|
| **Lemon Squeezy** | 5% of sales | Payment processing |
| **Domain + SSL** | $10 | cex.ai domain |
| **HuggingFace Pro** | $9 | Private model hosting |
| **GitHub Pro** | $4 | Private course repo |
| **Email service** | $5 | Transactional emails |
| **Monitoring** | $5 | Uptime + alerts |
| **TOTAL** | $33 + 5% sales | Base infrastructure |

### Variable Costs (Per Student)
| Tier | Revenue | Variable Cost | Margin |
|------|---------|---------------|--------|
| **Explorer** | R$0 | $0 | N/A (lead gen) |
| **Builder** | R$497 (~$90) | $4.50 (5%) | $85.50 (95%) |
| **Master** | R$997 (~$180) | $9.00 (5%) | $171.00 (95%) |

### Breakeven Analysis
**Fixed costs**: $33/month = $396/year

**Breakeven scenarios**:
- **4 Builder students/year**: 4 × $85.50 = $342 (near breakeven)
- **2 Master students/year**: 2 × $171 = $342 (near breakeven)
- **Mixed (2 Builder + 1 Master/year)**: $171 + $171 = $342 (near breakeven)

### Growth Projections

| Students/Month | Monthly Revenue | Monthly Profit | Annual Profit |
|----------------|-----------------|----------------|---------------|
| **10 Builder** | $855 | $822 | $9,864 |
| **50 Builder** | $4,275 | $4,242 | $50,904 |
| **100 Builder** | $8,550 | $8,517 | $102,204 |

**Conservative estimate**: 10 students/month = $9,864/year profit

---

## 7. Critical Automation Scripts

### P0 Scripts (Launch blockers)

#### cex_license.py
```python
# PRIORITY: P0 - Core monetization
# FUNCTIONALITY: License validation + model download
# DEPENDENCIES: requests, click, ollama
# ESTIMATED EFFORT: 8 hours
```

#### cex_setup.py  
```python
# PRIORITY: P0 - First-run installer
# FUNCTIONALITY: Install deps, ollama, validate environment
# DEPENDENCIES: subprocess, pathlib
# ESTIMATED EFFORT: 6 hours

def install_dependencies():
    """Install Python dependencies + Ollama."""
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Install Ollama (cross-platform)
    if platform.system() == "Windows":
        subprocess.run(["winget", "install", "Ollama.Ollama"])
    else:
        subprocess.run(["curl", "-fsSL", "https://ollama.ai/install.sh", "|", "sh"])

def verify_setup():
    """Verify CEX environment health."""
    subprocess.run(["python", "_tools/cex_doctor.py", "--setup-check"])
```

#### GitHub Action: Release
```yaml
# PRIORITY: P0 - Release automation
# FUNCTIONALITY: Tag → changelog → GitHub release
# ESTIMATED EFFORT: 4 hours
```

#### Webhook Handler
```python
# PRIORITY: P0 - Payment processing
# FUNCTIONALITY: Lemon Squeezy → grant access
# DEPENDENCIES: fastapi, hmac, requests
# ESTIMATED EFFORT: 10 hours
```

### P1 Scripts (Quality of life)

| Script | Effort | Purpose |
|--------|--------|---------|
| `cex_course_check.py` | 4h | Verify module completion |
| `GitHub Action: doctor` | 2h | PR validation |
| `cex_analytics.py` | 6h | Usage metrics collection |

---

## Implementation Timeline

### Week 1: Foundation
- [ ] Setup Lemon Squeezy account + webhook endpoint
- [ ] Create GitHub Actions for CI/CD
- [ ] Implement `cex_license.py` core validation

### Week 2: Distribution
- [ ] Setup HuggingFace Hub model hosting
- [ ] Implement model download + Ollama integration
- [ ] Test end-to-end license → download → install flow

### Week 3: Course Infrastructure
- [ ] Setup GitHub private repo for course content
- [ ] Implement student access automation
- [ ] Create exercise verification system

### Week 4: Launch Prep
- [ ] Full system testing with real Lemon Squeezy payments
- [ ] Monitoring & alerts configuration
- [ ] Documentation + troubleshooting guides

---

## Success Metrics

### Technical KPIs
- **License activation success rate**: >95%
- **Model download completion rate**: >90% 
- **Course completion rate**: >60%
- **System uptime**: >99.5%

### Business KPIs  
- **Conversion rate** (visitor → paid): >2%
- **Monthly recurring students**: 10+ (conservative)
- **Customer satisfaction**: >4.5/5 (course ratings)
- **Support ticket volume**: <5/month

### Risk Mitigation
- **Payment failure**: Lemon Squeezy 99.9% uptime SLA
- **Model hosting**: HuggingFace + S3 backup
- **Course access**: GitHub Enterprise backup plan
- **License validation**: Local caching + offline mode

**Infrastructure ready for 10x growth from day one.**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_output_github_actions]] | upstream | 0.50 |
| [[n03_output_monetization_architecture]] | related | 0.40 |
| [[p01_kc_github_actions]] | upstream | 0.30 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.25 |
| [[KC_N05_API_HEALTH_MONITORING]] | related | 0.21 |
| [[p01_kc_fastapi_patterns]] | upstream | 0.21 |
| [[skill]] | downstream | 0.20 |
| [[bld_knowledge_card_webhook]] | downstream | 0.19 |
| [[bld_sp_output_template_software_project]] | downstream | 0.19 |
| [[bld_tools_changelog]] | upstream | 0.18 |
