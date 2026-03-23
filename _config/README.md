# _config/

CEX instance configuration. Secrets are gitignored.

## Files

| File | Gitignored | Purpose |
|------|:----------:|---------|
| `client_secret.json` | YES | Google OAuth credentials (from Cloud Console) |
| `token.json` | YES | Cached auth token (auto-generated) |
| `gdrive.yaml` | NO | Drive folder IDs after setup (shareable) |

## Setup

```bash
# 1. Get client_secret.json from Google Cloud Console
# 2. Place here
# 3. Run: python _tools/setup_gdrive.py --setup
# 4. Browser opens for OAuth consent
# 5. gdrive.yaml generated automatically
```
