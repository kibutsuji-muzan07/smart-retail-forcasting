from pathlib import Path

def find_project_root(marker_files=("README.md", ".gitignore", ".env")):
    path = Path.cwd().resolve()
    for parent in [path] + list(path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent
    raise FileNotFoundError("Project root not found")