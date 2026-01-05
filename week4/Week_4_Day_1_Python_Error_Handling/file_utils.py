from pathlib import Path


def read_file_safe(path: Path) -> str:
    """Read a file and return its contents."""
    try:
        return path.read_text()
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} does not exist")
