#!/usr/bin/env bash

set -euo pipefail

# Resolve model string for a nucleus from nucleus_models.yaml via Python.
# Usage: MODEL=$(cex_resolve_model "n03" "claude-opus-4-6")
cex_resolve_model() {
  local nucleus="$1"
  local fallback="${2:-claude-opus-4-6}"
  local resolved
  resolved=$(python3 -c "
import sys, os
sys.path.insert(0, os.environ.get('CEX_ROOT', '.'))
try:
    from _tools.cex_model_resolver import get_model_string
    print(get_model_string('$nucleus'))
except Exception:
    print('$fallback')
" 2>/dev/null) || resolved="$fallback"
  printf '%s' "${resolved:-$fallback}"
}

cex_run_claude_boot() {
  local repo_root="$1"
  local nucleus="$2"
  local model="$3"
  local cli_name="$4"
  local agent_card="$5"
  local settings_path="$6"
  local sys_prompt="$7"
  local initial_template="$8"
  shift 8

  local home_dir
  home_dir="${HOME:-${USERPROFILE:-}}"
  if [[ -z "$home_dir" ]]; then
    echo "HOME or USERPROFILE must be set." >&2
    return 2
  fi

  local handoff_path="${CEX_HANDOFF_PATH:-${CEX_HANDOFF:-}}"
  local -a forward_args=()
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --handoff)
        shift
        if [[ $# -eq 0 ]]; then
          echo "--handoff requires a path." >&2
          return 2
        fi
        handoff_path="$1"
        ;;
      --handoff=*)
        handoff_path="${1#*=}"
        ;;
      *)
        forward_args+=("$1")
        ;;
    esac
    shift
  done

  if [[ -z "$handoff_path" ]]; then
    handoff_path="$repo_root/.cex/runtime/handoffs/${nucleus}_task.md"
  fi

  if ! command -v claude >/dev/null 2>&1; then
    echo "claude was not found in PATH." >&2
    return 127
  fi

  export HOME="$home_dir"
  export CEX_HOME="$home_dir"
  export CLAUDECODE=""
  CEX_NUCLEUS="$(printf '%s' "$nucleus" | tr '[:lower:]' '[:upper:]')"
  export CEX_NUCLEUS
  export CEX_ROOT="$repo_root"
  export CEX_HANDOFF="$handoff_path"
  export CEX_HANDOFF_PATH="$handoff_path"

  cd "$repo_root"

  local initial_msg="${initial_template//__HANDOFF__/$handoff_path}"
  local -a cli_args=(
    "--dangerously-skip-permissions"
    "--permission-mode" "bypassPermissions"
    "--no-chrome"
    "--model" "$model"
    "--name" "$cli_name"
    "--append-system-prompt" "$agent_card"
    "--append-system-prompt" ".cex/config/context_self_select.md"
    "--append-system-prompt" "$sys_prompt"
  )

  if [[ -f "$settings_path" ]]; then
    cli_args+=("--settings" "$settings_path")
  fi

  cli_args+=("${forward_args[@]}")
  cli_args+=("$initial_msg")

  exec claude "${cli_args[@]}"
}
