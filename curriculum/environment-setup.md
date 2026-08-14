# Environment Setup Guide

**Goal:** a working, free, reproducible environment on every machine you'll touch for this course. This is Milestone 0.1's deliverable.

**The one rule:** each machine gets a consistent Python toolchain (`uv` + a project venv). The ML stack below is identical everywhere; only the machine-specific extras (GPU driver, Ollama) differ. If two machines disagree on numpy, bugs appear that are not yours.

## Your three machines

| Machine | Role this course | What gets installed |
| --- | --- | --- |
| **Laptop (Arch)** | Primary work: notebooks, coding, experiments that fit in RAM | `uv` + Python + ML stack + Jupyter |
| **GTX-970 box** (2TB NVMe, fresh OS) | Small PyTorch training/experiments (phase 2-3 scale) | OS + NVIDIA driver (legacy 470) + PyTorch `cu118` |
| **R610 (Proxmox)** | CPU inference box: Ollama for quantized LLMs (phases 4-5) | Ollama + a 7B model, reachable over LAN |

## Shared: Python toolchain (all machines)

Use `uv` everywhere - it installs Python itself, makes venvs in seconds, and is the same on all three boxes.

```bash
# install uv (if not already present) - macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# per project: create the course environment
uv venv .venv
uv pip install --python .venv/bin/python \
    numpy pandas matplotlib seaborn scikit-learn jupyterlab ipykernel

# every time you work in the repo:
source .venv/bin/activate
```

The package list is deliberately small - it covers phases 0-1. PyTorch is added per-machine (it differs: CPU vs cu118). Everything else is added as phases need it.

## Laptop (Arch)

On Arch, do **not** mix pacman's python packages with pip/uv in the same environment - that is the #1 source of breakage. Let `uv` own Python entirely:

```bash
# system deps only (git is assumed; add nothing else python-related from pacman)
sudo pacman -S --needed git curl

# then the shared uv setup above
```

Verify: `python -c "import numpy, pandas, sklearn, matplotlib; print('ok')"` inside the venv.

**Git hygiene (mandatory):** this repo is your course repo. Commit the milestone examples you modify so your decisions are logged. Add a `.venv/` to `.gitignore` if not already ignored.

## GTX-970 box (fresh OS on the 2TB NVMe)

This card is **Maxwell, compute capability 5.2 (sm_52)** - NVIDIA's legacy list. The constraint that decides everything:

- CUDA **12.x does not support Maxwell**. The last CUDA 11.8 (cu118) PyTorch wheels go up to **torch 2.7.1**; after that only CUDA 12 builds exist.
- NVIDIA's last driver branch supporting Maxwell is the **legacy 470.x** series.

So this box is pinned to: **legacy driver + CUDA 11.8 toolchain + torch cu118 (2.7.1 or earlier).** It will never run the latest PyTorch - that is fine, phase 2-3 scale does not need it.

```bash
# Ubuntu 22.04 LTS (recommended for the box - best legacy-driver support)
sudo apt install nvidia-driver-470        # the last driver that supports Maxwell
reboot
nvidia-smi                                # should list the GTX 970, driver 470.x

# then the shared uv setup, plus PyTorch built for CUDA 11.8:
uv venv .venv
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

- **GTX-970 box OS:** Ubuntu 22.04 LTS recommended for driver-470 support. If you'd rather run Arch or Debian there, driver packages differ (`nvidia-470xx-dkms` on Arch; `nvidia-legacy-470xx-driver` on Debian) - say so and I'll adjust.
- **R610 container vs VM:** a Proxmox LXC container is lighter and fine for CPU inference; a VM is more isolated. Either works.
- **Laptop GPU:** if the laptop also has an NVIDIA GPU, the same cu118 rule applies there; otherwise laptop stays CPU-only.

## Cost

$0. Free tiers: Kaggle GPU (30h/wk) for phase 2-3 big runs, added when needed.
