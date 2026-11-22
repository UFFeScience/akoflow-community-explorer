#!/bin/sh
set -eu

workspace=/home/ovvesley/Workspace/akoflow-community-explorer
prompt_file="$workspace/automation/worker-prompt.md"
state_dir="$workspace/.automation"

mkdir -p "$state_dir"
exec /usr/local/bin/codex exec \
  --sandbox danger-full-access \
  -c 'approval_policy="never"' \
  --cd "$workspace" \
  --add-dir /home/ovvesley/Workspace/akoflow-examples \
  --add-dir /home/ovvesley/Workspace/akoflow \
  --output-last-message "$state_dir/last-message.md" \
  - < "$prompt_file"
