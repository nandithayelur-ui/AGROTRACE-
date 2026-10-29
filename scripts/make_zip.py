import os
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

EXCLUDE_DIRS = {
    ".venv", "venv", "node_modules", "artifacts", "cache",
    "local_cas", "dist", "__pycache__", ".pytest_cache", ".git", "runs"
}

EXCLUDE_EXTS = {".db", ".sqlite3", ".pyc", ".pyo"}


def create_source_zip(dest_zip: str = "src.zip"):
    dest_path = ROOT_DIR / dest_zip
    if dest_path.exists():
        dest_path.unlink()

    count = 0
    with zipfile.ZipFile(dest_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file_path in ROOT_DIR.rglob("*"):
            if not file_path.is_file():
                continue

            rel_parts = file_path.relative_to(ROOT_DIR).parts

            # Exclude directory matches
            if any(part in EXCLUDE_DIRS for part in rel_parts):
                continue

            # Exclude .env and database/compiled files
            if file_path.name == ".env" or file_path.suffix.lower() in EXCLUDE_EXTS:
                continue

            # Include evidence/ always
            zipf.write(file_path, arcname=str(file_path.relative_to(ROOT_DIR)))
            count += 1

    print(f"[OK] Archived {count} files into {dest_zip} ({dest_path.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    create_source_zip()
