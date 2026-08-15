"""Working example - Milestone 0.1: verify your environment.

Run:  python3 projects/phase-0/milestone-0.1/verify_environment.py

Prints the version of every package this course starts with, plus optional
checks for GPU (PyTorch CUDA) and the R610/Ollama inference box. Runs on all
three machines - the same script tells you what is missing everywhere.

Modifications to try (from phase-0-setup-python-math.md, M0.1.1 - M0.1.3):
 [x]  M0.1.1  add a jupyter --version check, or change the output format
 [x]  M0.1.2  run it in a bare shell (no venv) and watch it fail on imports
 [x]  M0.1.3  Ollama + nvidia-smi checks are written and dormant; fill in
            OLLAMA_HOST when the R610 comes online (Project 4.0)
"""

import importlib
import sys

print(f"Python: {sys.version.split()[0]}")

# The core course stack - all required for Phase 1.
required = ["jupyterlab", "numpy", "pandas", "matplotlib", "seaborn", "sklearn"]
for name in required:
    try:
        mod = importlib.import_module(name)
        print(f"  {name:<15} {mod.__version__}")
    except ImportError:
        print(f"  {name:<15} MISSING - install it in your venv")

# Optional machine-specific checks (fail gracefully on machines without them).
print("\nOptional checks:")
try:
    import torch
    cuda_ok = torch.cuda.is_available()
    print(f"  torch         {torch.__version__}  | CUDA available: {cuda_ok}")
    if cuda_ok:
        print(f"    GPU: {torch.cuda.get_device_name(0)}")
        print(f"    arch list: {torch.cuda.get_arch_list()}")
except ImportError:
    print("  torch         not installed (fine until phase 2-3)")

import subprocess
try:
    out = subprocess.run(["nvidia-smi", "--query-gpu=name,driver_version",
                          "--format=csv,noheader"],
                         capture_output=True, text=True, timeout=5)
    if out.returncode == 0:
        print(f"  nvidia-smi    {out.stdout.strip()}")
    else:
        print("  nvidia-smi    not found or no GPU on this machine")
except FileNotFoundError:
    print("  nvidia-smi    not found or no GPU on this machine")

# Ollama reachability (edit the IP to match your R610). Off by default.
OLLAMA_HOST = ""  # e.g. "http://192.168.1.50:11434"
if OLLAMA_HOST:
    try:
        out = subprocess.run(["curl", "-s", f"{OLLAMA_HOST}/api/tags"],
                             capture_output=True, text=True, timeout=5)
        print(f"  ollama        reachable: {'yes' if out.returncode == 0 else 'no'}")
    except FileNotFoundError:
        print("  ollama        curl not found")

print("\nIf any REQUIRED package is MISSING, your env is broken - fix the venv,")
print("not your code. That distinction is Milestone 0.1's whole point.")
