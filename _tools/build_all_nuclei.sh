#!/bin/bash
# CEX Nucleus Auto-Build -- generic, no hardcoded agent names
# User fills seeds with their own names before running
# Usage: bash _tools/build_all_nuclei.sh [--dry-run]

set -e
cd "$(dirname "$0")/.."

echo "============================================================"
echo "  CEX Nucleus Builder -- All 7 Nuclei"
echo "  Seeds: _seeds/seed_n{01-07}.txt"
echo "  Fill {{VARIABLES}} in seeds before running!"
echo "============================================================"

# Build order: Engineering first (self-build), then infra, then output
NUCLEI="N03:Engineering N07:Admin N04:Knowledge N01:Research N05:Operations N02:Marketing N06:Commercial"

for entry in $NUCLEI; do
    IFS=: read nuc domain <<< "$entry"
    echo ""
    echo "=== $nuc ($domain) ==="
    python _tools/cex_nucleus_builder.py --nucleus $nuc --name "$domain" --domain "$domain" "$@"
done

echo ""
echo "=== VALIDATE ==="
python _tools/cex_doctor.py 2>/dev/null || echo "Doctor: run manually"

echo ""
echo "=== DONE ==="
