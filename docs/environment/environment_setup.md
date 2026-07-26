# Development Environment Setup

## Purpose

Phase 0 establishes a reproducible development environment for Project
Intelligence before capability learning or robot implementation begins.

The environment requirement is:

> **ENV-001:** The authoritative WSL2 checkout shall build a ROS 2 package, run
> ROS communication and Gazebo, execute a CUDA calculation with PyTorch, and
> compile project mathematics from Quarto to PDF.

## Architecture decision

```text
Windows 11 host
└── WSL2 Ubuntu 24.04
    ├── authoritative Git checkout
    ├── ROS 2 Jazzy
    ├── Gazebo Harmonic
    ├── GCC, G++, and CMake
    ├── Python 3.12 project environment
    ├── PyTorch with CUDA
    └── Quarto with TinyTeX
```

The authoritative checkout is:

```text
/home/maxwell/Repos/robotics_autonomous
```

The repository is stored in the WSL Linux filesystem rather than `/mnt/c` or
`/mnt/d`. The Codex desktop app may access it through the Windows UNC path, but
build and verification commands run inside Ubuntu.

## Recorded toolchain

Versions were rechecked on 2026-07-23.

| Component | Recorded version or decision |
|---|---|
| Host | Windows 11 |
| Linux environment | Ubuntu 24.04.4 LTS under WSL2 |
| WSL kernel | `6.6.87.2-microsoft-standard-WSL2` |
| ROS | ROS 2 Jazzy |
| Simulator | Gazebo Harmonic, Gazebo Sim `8.11.0` |
| C compiler | GCC `13.3.0` |
| C++ compiler | G++ `13.3.0` |
| Build configuration | CMake `3.28.3` |
| Python | CPython `3.12.3` |
| Python environment manager | `uv 0.10.9` |
| PyTorch | `2.13.0+cu130` |
| PyTorch CUDA build | CUDA `13.0` |
| GPU | NVIDIA GeForce RTX 5070 Laptop GPU |
| GPU compute capability | `12.0` |
| Quarto | `1.9.38` |
| PDF toolchain | TinyTeX `2026.07`, LuaLaTeX |

## Python environment

The project environment is `.venv` in the repository root. It uses
`/usr/bin/python3.12` and has `include-system-site-packages = true` so ROS Python
packages installed under `/opt/ros/jazzy` remain available.

Activate it for project Python and PyTorch work:

```zsh
cd /home/maxwell/Repos/robotics_autonomous
source .venv/bin/activate
```

Deactivate it when a clean non-project Python shell is useful:

```zsh
deactivate
```

The virtual environment is not required for C++ ROS builds. For a clean ROS
build, leave it inactive and explicitly source the ROS installation.

## ROS workspace workflow

The ROS workspace is `ros_ws`. A shell uses two environment layers:

1. `/opt/ros/jazzy/setup.zsh` exposes the installed ROS distribution.
2. `ros_ws/install/setup.zsh` exposes packages built in this workspace.

After the first project package exists, build and use the workspace from Zsh:

```zsh
cd /home/maxwell/Repos/robotics_autonomous/ros_ws
source /opt/ros/jazzy/setup.zsh
colcon build
source install/setup.zsh
```

Use the clean-cache form after changing CMake or Python configuration:

```zsh
colcon build --cmake-clean-cache
```

The workspace-level `ros_ws/colcon_defaults.yaml` enables symbolic installs and
pins CMake package-processing scripts to the ROS-compatible interpreter:

```yaml
build:
  symlink-install: true
  cmake-args:
    - -DPython3_EXECUTABLE=/usr/bin/python3.12
```

Use the setup file matching the active shell. In Zsh, source `setup.zsh`, not
`setup.bash`.

## Quarto workflow

Project theory notes may use `.qmd` files containing Markdown, LaTeX mathematics,
and explanatory or executable code cells.

Check the toolchain:

```zsh
quarto --version
quarto list tools
quarto check
```

Render an individual theory note:

```zsh
cd /home/maxwell/Repos/robotics_autonomous
quarto render notes/<chapter>.qmd
```

The temporary Quarto smoke source and PDF were removed after successful verification; the result remains recorded in [environment_verification.md](environment_verification.md).

Jupyter is not required for prose, mathematics, or display-only code blocks. It
will be installed inside `.venv` only when a note first requires executable
Python cells. R, Julia, Chrome Headless Shell, and VeraPDF are also not Phase 0
requirements.

## Failures and workarounds

### Zsh sourced the Bash setup file

Sourcing `/opt/ros/jazzy/setup.bash` from Zsh produced a missing `setup.sh`
error. Use:

```zsh
source /opt/ros/jazzy/setup.zsh
```

### ROS Python imports were hidden

The project environment initially raised missing `yaml` and `catkin_pkg`
imports. The environment now includes system site packages so ROS-installed
Python dependencies remain visible.

### CMake selected the wrong Python executable

An early ROS build selected `/home/maxwell/.local/bin/python3.12`. The workspace
defaults now pass:

```text
-DPython3_EXECUTABLE=/usr/bin/python3.12
```

The clean-cache verification confirmed that the CMake cache uses
`/usr/bin/python3.12`.
