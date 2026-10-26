#!/usr/bin/env bash
# Install AI Marketing Agent Team skills into Hermes Agent (~/.hermes/skills/marketing/)
set -euo pipefail
SRC="$(cd "$(dirname "$0")/marketing" && pwd)"
DEST="${HERMES_HOME:-$HOME/.hermes}/skills/marketing"
mkdir -p "$DEST"
cp -R "$SRC"/. "$DEST"/
echo "Installed $(find "$DEST" -name SKILL.md | wc -l | tr -d ' ') marketing skills -> $DEST"
echo "Verify:  hermes skills list | grep -i marketing"
echo "Use:     /marketing-orchestrator   or   /brand-setup"
