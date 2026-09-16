#!/usr/bin/env bash
# Install the AnnaLocal MCP bridge into a self-contained venv (Linux/macOS).
set -euo pipefail

cd "$(dirname "$0")"

PY="${PYTHON:-python3}"
if ! command -v "$PY" >/dev/null 2>&1; then
  echo "Python 3.10+ not found (set PYTHON=/path/to/python)." >&2
  exit 1
fi

"$PY" -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt

VENV_PY="$PWD/.venv/bin/python"
SERVER="$PWD/aa_mcp.py"

cat <<MSG

MCP bridge installed.

Start a local endpoint first — either a real local Anna's Archive instance, or
the bundled dev fixture:

  ./.venv/bin/python dev/stub_aa_app.py --port 8000

Verify the bridge end to end:

  ./.venv/bin/python dev/smoke_test.py

Register with Claude Code:

  claude mcp add --transport stdio --scope user annas-local -- "$VENV_PY" "$SERVER"

Verify:

  claude mcp list          # expects: annas-local ... Connected
  # then inside Claude Code: /mcp
MSG
