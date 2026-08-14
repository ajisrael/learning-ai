#!/usr/bin/env bash
#
# One-shot per-machine setup for the course environment (Milestone 0.1).
# Creates a project-local, uv-managed CPython 3.12 (.local/python) and a venv
# (.venv) built on it, then installs the phase 0-1 stack.
#
# Run this on every machine you work from (laptop, GTX-970 box, R610). It is
# the source of truth for the shared toolchain - see
# curriculum/environment-setup.md.
set -euo pipefail
cd "$(dirname "$0")/.."

# uv-managed CPythons live INSIDE the repo, so no OS package manager can ever
# upgrade or remove the interpreter the venv points at (no dangling symlinks).
export UV_PYTHON_INSTALL_DIR="$PWD/.local/python"

if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found - install it first: curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
  exit 1
fi

echo "==> CPython 3.12 via uv (managed, project-local)"
uv python install 3.12 --force

echo "==> Project venv on the uv-managed Python"
uv venv --python 3.12 --relocatable .venv

echo "==> Phase 0-1 stack"
uv pip install --python .venv/bin/python \
    numpy pandas matplotlib seaborn scikit-learn jupyterlab ipykernel

echo
echo "Done. Sanity check (should be 3.12.x under $PWD/.local/python):"
"$PWD/.venv/bin/python" --version
"$PWD/.venv/bin/python" -c "import numpy, pandas, sklearn, matplotlib; print('imports ok')"
