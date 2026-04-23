#!/usr/bin/env bash
# Setup CEX git hooks.
# Usage: bash _tools/setup_hooks.sh

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"

echo "Setting git hooks path to .githooks..."
git config core.hooksPath .githooks

# Ensure hook is executable
chmod +x "$REPO_ROOT/.githooks/pre-commit" 2>/dev/null || true

echo "Done. Pre-commit hook active."
echo "Test with: git commit --dry-run"
