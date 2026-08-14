# Environment Setup Guide

**Goal:** a working, free, reproducible environment on every machine you'll touch for this course. This is Milestone 0.1's deliverable.

**The one rule:** each machine gets a consistent Python toolchain (`uv` + a project venv) built on a **uv-managed CPython pinned to the same version everywhere — never the system/OS Python**. The ML stack below is identical everywhere; only the machine-specific extras (GPU driver, Ollama) differ. If two machines disagree on numpy — or on the interpreter numpy runs under — bugs appear that are not yours.

**Why not the system Python:** a venv created with `/usr/bin/python` symlinks its interpreter to that OS binary. When the OS package manager later upgrades or removes that Python (Arch's `pacman`, Ubuntu's `apt`), the symlink dangles and the venv silently breaks. The managed CPython here lives **inside the repo** (`.local/python`), so OS upgrades can never touch it.

## Your three machines

| Machine | Role this course | What gets installed |
| --- | --- | --- |
| **Laptop (Arch)** | Primary work: notebooks, coding, experiments that fit in RAM | `uv` + Python + ML stack + Jupyter |
| **GTX-970 box** (2TB NVMe, fresh OS) | Small PyTorch training/experiments (phase 2-3 scale) | OS + NVIDIA driver (legacy 470) + PyTorch `cu118` |
| **R610 (Proxmox)** | CPU inference box: Ollama for quantized LLMs (phases 4-5) | Ollama + a 7B model, reachable over LAN |

## Provisioning the remote boxes (Ansible)

Ansible is how the non-laptop machines (GTX-970 box, R610) get their toolchain, run from the laptop as the control node. A role installs `uv`, then runs the tracked `./scripts/setup-env.sh` — the same script the laptop uses, so every machine gets an identical, project-local, uv-managed CPython 3.12:

- The script handles `uv python install 3.12` + `uv venv --python 3.12 --relocatable .venv` + the phase 0-1 stack. Never `apt install python3-pip` and pip into the system Python on a target — `apt` upgrades its own `python3` exactly like `pacman` does, so a system-python venv gets the same dangling-symlink breakage.
- The GTX-970 box adds torch after the script (cu118, see below); the R610 needs no extra Python.
- Pin **3.12 on every target**, matching the laptop. Version drift between machines is what the one rule exists to prevent.
- Ansible's own `ansible_python_interpreter` can stay on the target's system Python — it is independent of the course venv. On the laptop, Ansible is the pacman `ansible` package (a dependency of the system `python`) — that interpreter stays untouched and is never the course interpreter.

## Shared: Python toolchain (all machines)

`uv` everywhere. Each repo carries its own CPython (`.local/python`) and venv (`.venv`), created by the tracked setup script — the single source of truth:

```bash
# install uv (if not already present) - macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# per machine, from the repo root:
./scripts/setup-env.sh
```

What the script does (and why, so a fresh machine is not magic):

- `UV_PYTHON_INSTALL_DIR=<repo>/.local/python` — CPython 3.12 lives inside the repo, so no OS package manager (`pacman`, `apt`) owns it. `uv venv --python 3.12 --relocatable .venv` builds the venv on that interpreter — there is **no symlink to `/usr/bin/python`** for an OS upgrade to dangle.
- Installs `numpy pandas matplotlib seaborn scikit-learn jupyterlab ipykernel`.

Interactive shells use direnv: the tracked `.envrc` exports `UV_PYTHON_INSTALL_DIR`, `VIRTUAL_ENV`, and prepends `.venv/bin` to `PATH`, so `python` inside `learning-ai` is the venv. First use: `direnv allow`. Machines without direnv just `source .venv/bin/activate`. Resolution chain: `python` → `.venv/bin/python` → `.local/python/cpython-3.12.x/...`.

The package list is deliberately small - it covers phases 0-1. PyTorch is added per-machine (it differs: CPU vs cu118). Everything else is added as phases need it.

## Laptop (Arch)

On Arch, do **not** mix pacman's python packages with pip/uv in the same environment - that is the #1 source of breakage. Let `uv` own Python entirely. Note that `python` is *already installed* on a box like this one — but only as a dependency of other packages (`ansible`, `kitty`, `waybar`, `gdb`, ...) and it gets upgraded by `pacman -Syu`. Never build the course venv on it; `./scripts/setup-env.sh` (with `UV_PYTHON_INSTALL_DIR` pointed into the repo) makes that impossible to do by accident:

```bash
# system deps only (git is assumed; add nothing else python-related from pacman)
sudo pacman -S --needed git curl

# uv is on PATH via home-manager; then:
./scripts/setup-env.sh
direnv allow            # first cd; `.envrc` maps `python` to the venv

# sanity-check the venv is NOT the system python:
uv python find                 # must be under .local/python/..., not /usr/bin
.venv/bin/python --version     # 3.12.x, independent of `pacman -Q python`
```

Verify: `python -c "import numpy, pandas, sklearn, matplotlib; print('ok')"` inside the venv.

**Git hygiene (mandatory):** this repo is your course repo. Commit the milestone examples you modify so your decisions are logged. `.gitignore` (tracked) already excludes `.local/`, `.venv/`, `__pycache__/`, `*.egg-info/` — don't commit the environment, only `scripts/setup-env.sh` and `.envrc`, which are the reproducibility.

## GTX-970 box (Ubuntu 22.04 LTS on the 2TB NVMe)

This box runs **Ubuntu 22.04 LTS** - the best-supported base for the legacy driver this card needs. This card is **Maxwell, compute capability 5.2 (sm_52)** - NVIDIA's legacy list. The constraint that decides everything:

- CUDA **12.x does not support Maxwell**. The last CUDA 11.8 (cu118) PyTorch wheels go up to **torch 2.7.1**; after that only CUDA 12 builds exist.
- NVIDIA's last driver branch supporting Maxwell is the **legacy 470.x** series.

So this box is pinned to: **legacy driver + CUDA 11.8 toolchain + torch cu118 (2.7.1 or earlier).** It will never run the latest PyTorch - that is fine, phase 2-3 scale does not need it. It also uses the **same uv-managed Python 3.12 as the laptop** — torch 2.7.1/cu118 supports Python 3.9-3.13, so 3.12 is the version that works on every machine. Ubuntu's `apt` upgrades its own `python3` exactly like pacman does, so never build the venv on `/usr/bin/python3` (same dangling-symlink rule).

```bash
# Ubuntu 22.04 LTS is already installed on this box.
sudo apt install nvidia-driver-470        # the last driver that supports Maxwell
reboot
nvidia-smi                                # should list the GTX 970, driver 470.x

# then the shared setup, plus PyTorch built for CUDA 11.8:
./scripts/setup-env.sh
uv pip install --python .venv/bin/python \
    torch==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu118

# verify the wheel actually contains Maxwell kernels (some builds dropped them):
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_arch_list())"
```

If `torch.cuda.is_available()` is `False`, or `get_arch_list()` lacks `sm_52`, you have two options: try an older cu118 build (e.g. `torch==2.4.1`), **or run CPU** - valid for everything in phases 2-3. Do not burn more than a few hours on this; CPU is the stated fallback.

## R610 (Proxmox) - Ollama inference box

```bash
# on Proxmox: create a container/VM for ollama (Debian template, ~32GB RAM)
# give it a static IP, then:
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b          # or qwen2.5:7b - pick one 7B-class model
# serve on the LAN (not just localhost):
OLLAMA_HOST=0.0.0.0 ollama serve
```

Verify **from your laptop**: `curl http://<r610-ip>:11434/api/tags` returns the model list, and `ollama run llama3.1:8b` answers a prompt over the LAN.

## Verification (Milestone 0.1 checkpoint)

On the laptop, run `projects/phase-0/milestone-0.1/verify_environment.py`. It prints versions of every package this course starts with and reports GPU + Ollama availability as optional checks, so the same script works on every machine.

## Open questions to confirm as you set up

- **GTX-970 box OS:** decided - Ubuntu 22.04 LTS.
- **R610 container vs VM:** a Proxmox LXC container is lighter and fine for CPU inference; a VM is more isolated. Either works.
- **Laptop GPU:** if the laptop also has an NVIDIA GPU, the same cu118 rule applies there; otherwise laptop stays CPU-only.

## Cost

$0. Free tiers: Kaggle GPU (30h/wk) for phase 2-3 big runs, added when needed.
