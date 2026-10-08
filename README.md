# Python Development Environment (`uv`)

A modern, fast Python development environment configured with Astral's [`uv`](https://docs.astral.sh/uv/) and [`uv_build`](https://docs.astral.sh/uv/concepts/projects/build/) build backend.

---

## 🚀 Environment Overview

- **Python Version**: CPython 3.12 (managed automatically by `uv`)
- **Package & Project Manager**: `uv`
- **Build Backend**: `uv_build` (configured in `pyproject.toml`)
- **Virtual Environment**: `.venv`
- **Testing**: `pytest`
- **Code Quality / Linter**: `ruff`

---

## 🛠️ Common Commands

### 1. Running the Project & Scripts
Run the package entrypoint directly:
```powershell
uv run py-dev
```

Run an arbitrary script or Python inline:
```powershell
uv run python -c "import sys; print(sys.version)"
```

### 2. Managing Dependencies
Add production dependencies:
```powershell
uv add requests pydantic
```

Add development dependencies:
```powershell
uv add --dev pytest ruff
```

Remove dependencies:
```powershell
uv remove requests
```

Sync dependencies with lockfile (`uv.lock`):
```powershell
uv sync
```

### 3. Testing & Code Quality
Run unit tests with pytest:
```powershell
uv run pytest
```

Check code formatting and lint rules:
```powershell
uv run ruff check
uv run ruff format
```

### 4. Building the Project
Build source distributions (`.tar.gz`) and wheels (`.whl`) with `uv_build`:
```powershell
uv build
```
Artifacts are generated in the `dist/` directory.

### 5. Managing Python Versions
List available or installed Python runtimes:
```powershell
uv python list
```

Install a different Python version:
```powershell
uv python install 3.13
```

Pin the project to a specific Python version:
```powershell
uv python pin 3.12
```

### 6. Activating the Virtual Environment (Optional)
`uv run` automatically uses the virtual environment without manual activation. If you prefer activating it in your shell:

- **PowerShell**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **Command Prompt (CMD)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
