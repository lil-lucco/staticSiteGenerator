import shutil
from pathlib import Path


def _log_copy(src_path, dst_path, log_path):
    if not log_path:
        return
    with Path(log_path).open("a", encoding="utf-8") as f:
        f.write(f"COPIED {src_path} -> {dst_path}\n")


def _copy_recursive(source, dest, log_path):
    for source_path in source.iterdir():
        dest_path = dest / source_path.name

        if source_path.is_file():
            shutil.copy(source_path, dest_path)
            _log_copy(source_path, dest_path, log_path)
        else:
            dest_path.mkdir()
            _copy_recursive(source_path, dest_path, log_path)


def copy_dir(source, dest, log_path=None):
    source = Path(source)
    dest = Path(dest)
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir()
    _copy_recursive(source, dest, log_path)
