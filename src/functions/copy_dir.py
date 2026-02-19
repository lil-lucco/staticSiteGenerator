import os
import shutil


def _log_copy(src_path, dst_path, log_path):
    if not log_path:
        return
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"COPIED {src_path} -> {dst_path}\n")


def _copy_recursive(source, dest, log_path):
    for entry in os.listdir(source):
        source_path = os.path.join(source, entry)
        dest_path = os.path.join(dest, entry)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
            _log_copy(source_path, dest_path, log_path)
        else:
            os.mkdir(dest_path)
            _copy_recursive(source_path, dest_path, log_path)


def copy_dir(source, dest, log_path=None):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    _copy_recursive(source, dest, log_path)
