#!/usr/bin/env bash
# cex_export_public.sh -- Create a clean public repo from the CEX source
#
# Usage: bash _tools/cex_export_public.sh [target_dir]
#
# Creates a squashed initial commit (no history, no blobs, no secrets).
# The user MUST rotate all API keys before running this.

set -euo pipefail

SOURCE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${1:-$SOURCE_DIR/../cex-public}"

echo "[1/6] Checking prerequisites..."

# Verify .env is gitignored and not tracked
if git -C "$SOURCE_DIR" ls-files --error-unmatch .env 2>/dev/null; then
    echo "[FAIL] .env is tracked in git. Remove it first: git rm --cached .env"
    exit 1
fi

# Verify no secrets in staged files
if grep -rn "sk-ant-\|sk-proj-\|gsk_\|AIza" "$SOURCE_DIR"/*.md "$SOURCE_DIR"/*.yaml 2>/dev/null; then
    echo "[FAIL] Possible API keys found in tracked files. Clean them first."
    exit 1
fi

echo "[2/6] Creating target directory: $TARGET_DIR"
rm -rf "$TARGET_DIR"
mkdir -p "$TARGET_DIR"

echo "[3/6] Copying files (respecting .gitignore)..."
cd "$SOURCE_DIR"
# Use git ls-files to get only tracked + unignored files
git ls-files -z | while IFS= read -r -d '' file; do
    dir=$(dirname "$file")
    mkdir -p "$TARGET_DIR/$dir"
    cp "$file" "$TARGET_DIR/$file"
done

# Also copy untracked but not ignored files (new docs, examples)
git ls-files -z --others --exclude-standard | while IFS= read -r -d '' file; do
    dir=$(dirname "$file")
    mkdir -p "$TARGET_DIR/$dir"
    cp "$file" "$TARGET_DIR/$file"
done

echo "[4/6] Removing private files from export..."
# Remove anything that should not be public
rm -rf "$TARGET_DIR/.cex/runtime/" 2>/dev/null || true
rm -rf "$TARGET_DIR/.cex/cache/" 2>/dev/null || true
rm -rf "$TARGET_DIR/.cex/learning_records/" 2>/dev/null || true
rm -rf "$TARGET_DIR/.cex/benchmarks/" 2>/dev/null || true
rm -rf "$TARGET_DIR/_reports/" 2>/dev/null || true
rm -rf "$TARGET_DIR/_archive/" 2>/dev/null || true
rm -rf "$TARGET_DIR/_external/" 2>/dev/null || true
rm -rf "$TARGET_DIR/_showoff/" 2>/dev/null || true
rm -f "$TARGET_DIR/.env" 2>/dev/null || true
rm -f "$TARGET_DIR/.env."* 2>/dev/null || true
rm -f "$TARGET_DIR/n0"[1-7]"_task.md" 2>/dev/null || true

# Strip instance-specific memory from operational nuclei (N01-N07)
# N00_genesis/P10_memory/ contains EXAMPLES (keep for reference)
for n in 1 2 3 4 5 6 7; do
    rm -rf "$TARGET_DIR/N0${n}_"*/P10_memory/ 2>/dev/null || true
done

# Strip brand config if present (instance-specific identity)
rm -f "$TARGET_DIR/.cex/brand/brand_config.yaml" 2>/dev/null || true

# Strip course content (monetized infoproducts, not OSS)
rm -rf "$TARGET_DIR/_courses/" 2>/dev/null || true

echo "[5/6] Initializing clean git repo..."
cd "$TARGET_DIR"
git init
git add -A
git commit -m "CEXAI v10.4.0 -- initial public release

Cognitive Exchange AI: typed knowledge system for LLM agents.
293 kinds, 298 builders, 3563 ISOs, 12 pillars, 8 nuclei, 8F pipeline.
Seven Artificial Sins. Intelligence compounds when exchanged.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

echo "[6/6] Done."
echo ""
echo "Public repo created at: $TARGET_DIR"
echo "  Commits: $(git rev-list --count HEAD)"
echo "  Files:   $(git ls-files | wc -l)"
echo "  Size:    $(du -sh . | cut -f1)"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Review: git log --stat"
echo "  3. Verify P10_memory stripped: find . -path '*/P10_memory/*' | wc -l (should show N00 examples only)"
echo "  4. Create GitHub repo: gh repo create GatoaoCubo/cex --public"
echo "  5. Push: git remote add origin https://github.com/GatoaoCubo/cex.git && git push -u origin main"
echo ""
echo "REMINDER: Rotate ALL API keys in your .env BEFORE making the repo public."
