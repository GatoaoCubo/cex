#!/bin/bash
# CEX status line -- shows tier + repo + branch + changes
TIER="${CEX_TIER:-dev}"
TIER=$(echo "$TIER" | tr '[:lower:]' '[:upper:]')
if [ -d .git ]; then
  BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  REM_NAME="${CEX_REMOTE:-origin}"
  REMOTE=$(git config --get "remote.$REM_NAME.url" 2>/dev/null | sed 's/.*\///' | sed 's/\.git$//')
  CHANGES=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
  printf "[%s] %s@%s (%s)" "$TIER" "$REMOTE" "$BRANCH" "$CHANGES"
else
  printf "[%s] no-repo" "$TIER"
fi
